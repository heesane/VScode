#include <Arduino.h>

int count = 0;
int pin = 13;

IRAM_ATTR void ISR00(){
  count++;
}

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("Starting");
  pinMode(pin,INPUT);
  attachInterrupt(pin,ISR00,FALLING);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("count :"); Serial.println(count);
  delay(100);
}
