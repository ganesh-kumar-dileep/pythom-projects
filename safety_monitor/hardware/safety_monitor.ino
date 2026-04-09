#include<LiquidCrystal.h>
#define LED 8
#define trig 9
#define echo 10
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  lcd.begin(16, 2);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH);
  int distance = (duration*0.034)/2;       //0.034 is the speed of sound in cm/microsecond, The sound wave travels 2 sodes s0 /2
  Serial.println(distance);
  lcd.setCursor(0, 0);
  lcd.print("Dist: ");
  lcd.print(distance);
  lcd.print(" cm  ");

  
if (Serial.available() > 0)
  {char command = Serial.read();          //reads the incoming byte

    if (command == '1')
      {digitalWrite(LED, HIGH);
      lcd.print("STOP");}
    else
      {digitalWrite(LED, LOW);
      lcd.print("   ");}
  }
  
  delay(60);
  
}
