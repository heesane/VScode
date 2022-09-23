#include <Arduino.h>
#include <SoftwareSerial.h>

SoftwareSerial swSer(13,12);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  swSer.begin(9600);
  pinMode(15,OUTPUT);
  delay(2000);
  Serial.println("Waiting for command");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(swSer.available()){
    int cmd = swSer.read();
    if(cmd == 1){
      digitalWrite(15,HIGH);
      Serial.println("on");
      delay(100);
    } else if(cmd == 2){
      digitalWrite(15,LOW);
      Serial.println("off");
    }
    
  }

}