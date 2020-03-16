#include <Servo.h>

Servo s1;
Servo s2;
int pos = 0;
int pos2=0;

void setup() {
  s1.attach(10);
  s2.attach(11);   
  s1.write(40);
  s2.write(40);
}
void loop() {
}
