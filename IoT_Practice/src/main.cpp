#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(15,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(15,1);
  delay(1000);
  digitalWrite(15,0);
  delay(1000);
}