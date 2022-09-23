#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sw = digitalRead(2);
  Serial.println(sw);
  delay(500);

}