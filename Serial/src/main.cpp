#include <Arduino.h>
#include <SoftwareSerial.h>
SoftwareSerial swSer(13,12);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  swSer.begin(9600);
  Serial.println("Program is Ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
      swSer.write(Serial.read());
  }
}