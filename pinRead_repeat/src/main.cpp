#include <Arduino.h>
int count = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(500);
  Serial.println("Starting");
  pinMode(2,INPUT);
}

void loop() {

  // put your main code here, to run repeatedly:
  Serial.println("Count :");  Serial.println(count);
  delay(100);
  if(digitalRead(2) == LOW){
    count++;
  }

}