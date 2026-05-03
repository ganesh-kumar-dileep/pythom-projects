#define LDR A0
int ldrValue;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LDR, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  ldrValue = analogRead(LDR);
  delay(500);
  Serial.println(resistance);
}
