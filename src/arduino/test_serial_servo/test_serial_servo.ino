#include <Servo.h>

const int SERVO_BALANCE_X = 35;
const int SERVO_BALANCE_Y = 35;

const int SERVO1_PIN = 11;
const int SERVO2_PIN = 10;
//:::::::::::::::::::::::::::::::\\

Servo servo1;
Servo servo2;

String inData;  // Buffer for getting data
int servo1_angle = 10;
int servo2_angle = 10;

void setup()
{
  Serial.begin(115200);
  servo1.attach(SERVO1_PIN);
  servo2.attach(SERVO2_PIN);

  servo1.write(SERVO_BALANCE_X);
  servo2.write(SERVO_BALANCE_Y);
}

void loop()
{
  if (Serial.available() > 0) {

    // Reading angle of the servo1
    inData = Serial.readStringUntil(':');
    servo1_angle = inData.toInt();

    // Reading angle of the servo2
    inData = Serial.readStringUntil('$');
    servo2_angle = inData.toInt();

    // Writing mapped angles to servos
    servo1.write(servo1_angle);
    servo2.write(servo2_angle);
  }

}
