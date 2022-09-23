#include <Arduino.h>
const int SW = 2;
int ping = 0;
IRAM_ATTR void buttonPushed(){
  Serial.println("still alive");
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(100);
  Serial.println("Booting");
  attachInterrupt(SW,buttonPushed,FALLING);

}

void loop() {
  // put your main code here, to run repeatedly:
  int i =0;
  for (;;){
    i++;

  }
}
