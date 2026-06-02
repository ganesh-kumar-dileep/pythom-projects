#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <ArduinoOTA.h>

#define IN1 25
#define IN2 26
#define IN3 16
#define IN4 17
#define trig 5
#define echo 18
#define ENA 21
#define ENB 19
#define LED 2

long duration;
int distance;
int distanceL = 0;
int distanceR = 0;
const char* ssid = "Your wifi ssid";
const char* password = "wifi password";
int serverFailCount = 0;
int maxServerFails = 3;

const char* serverUrl = "server url";
const char* distUrl = "server url";

void forward(int PWM);
void backward(int PWM);
void stop();
int ultrasonic();
bool send_distance();
bool receive_status();
void obstacle_avoidance();
void left();
void right();

void setup() {
  Serial.begin(115200);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(LED, OUTPUT);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected!");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  ArduinoOTA.begin();

  ArduinoOTA.setHostname("esp32-car");
  //ArduinoOTA.setPassword("esp123");

  ArduinoOTA.onStart([](){
    stop();
    Serial.println("OTA Start");
  });

  ArduinoOTA.onEnd([]() {
  Serial.println("\nOTA End");
  });
  
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
  });
  
  ArduinoOTA.begin();
  
  Serial.println("OTA Ready");
  }

void loop() {
  ArduinoOTA.handle();

  ultrasonic();
  if (WiFi.status() == WL_CONNECTED) {

    bool sendok = send_distance();
    bool receiveok = receive_status();

    if (sendok && receiveok)
    {
      serverFailCount = 0;
    }
    else
    {
      serverFailCount++;
    }

    if (serverFailCount == maxServerFails)
    {
      stop();
      digitalWrite(LED, HIGH);
    }

  }

  delay(200);
  
}

void forward(int PWM)
{
  stop();
  analogWrite(ENA, PWM);
  analogWrite(ENB, PWM);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN4, HIGH);
}

void stop()
{
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void backward(int PWM)
{
  stop();
  analogWrite(ENA, PWM);
  analogWrite(ENB, PWM);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
}

void left()
{
  stop();
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  delay(600);
}

void right()
{
  stop();
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  digitalWrite(IN4, HIGH);
  digitalWrite(IN2, HIGH);
  delay(600);
}
void obstacle_avoidance()
{
  stop();
  delay(100);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  delay(600);
  distanceL = ultrasonic();

  stop();
  delay(100);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN4, HIGH);
  delay(1000);
  distanceR = ultrasonic();

  stop();
  delay(100);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN3, HIGH);
  delay(600);
  stop();
  delay(500);
}

int ultrasonic()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(5);

  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH, 30000);
  
  distance = duration * (0.034/2);

  Serial.println("Distance: ");
  Serial.print(distance);
  //Serial.print(" cm");

  return distance;
}

bool receive_status()
{
    HTTPClient client;

    client.begin(serverUrl);

    int httpCode = client.GET();

    if (httpCode > 0) {
      String response = client.getString();

      Serial.print("Response: ");
      Serial.println(response);

      StaticJsonDocument<200> doc;
      DeserializationError error = deserializeJson(doc, response);

      if (!error) {
        const char* carStatus = doc["status"];
        int pwm = doc["pwm"];

        if (carStatus && String(carStatus) == "f") {
          forward(pwm);
          Serial.println("Forward");
        } 
        else if (carStatus && String(carStatus) == "r") {
          backward(pwm);
          Serial.println("Backward");
        } 
        else if (carStatus && String(carStatus) == "s") {
          stop();
          Serial.println("STOP");
        } 
        else if (carStatus && String(carStatus) == "oa") {
          stop();
          delay(2000);
          obstacle_avoidance();
          if (distanceR > distanceL){
            right();
          }
          if (distanceL > distanceR){
            left();
          }
        }
        
        
      } else {
        Serial.println("JSON parse failed");
      }
      return true;
    } else {
      Serial.print("HTTP error: ");
      Serial.println(httpCode);
      return false;
    }

    client.end();
}

bool send_distance()
{
  HTTPClient client;
  client.begin(distUrl);
  client.addHeader("Content-Type", "application/json");

  StaticJsonDocument<100> doc;
  doc["distance"] = distance;

  String jsonData;
  serializeJson(doc, jsonData);
  int httpCode = client.POST(jsonData);

  if (httpCode>0)
  {
    return true;
  }

  else
  {
    return false;
  }
  client.end();
}
