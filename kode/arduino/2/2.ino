#include <Servo.h>

Servo s1;
Servo s2;
int pos = 0;
int pos2=0;

void setup() {
  s1.attach(10);//x
  s2.attach(11);//y
  s1.write(30);
  s2.write(30); 
}
void loop() {
//////////////// 2 /////////////////////
  for (pos = 0; pos <= 70; pos += 1) {
    pos2=70-pos;
    pos2+=10; 
    s2.write(pos);           
    delay(15);  
  }
  for (pos = 70; pos >= 0; pos -= 1) { 
    pos2=70-pos;
    pos2+=10;
    s2.write(pos);              
    delay(15);                                       
  } 
}