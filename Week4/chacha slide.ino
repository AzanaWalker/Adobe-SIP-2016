#include <Servo.h>
Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(11);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);

}

void stopServos(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void forwardServos(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}

void backwardServos(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);

}

void leftServos(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
}

void rightServos(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);

  
}
void loop() {
  leftServos();
  delay(870);
  rightServos();  
  delay(500);
  leftServos();
  delay(400);
  rightServos();
  delay(200);
  leftServos();
  delay(200);
  rightServos();
  delay(1000);
  stopServos();
  delay(800);
  leftServos();
  delay(860);
  rightServos();  
  delay(500);
  leftServos();
  delay(400);
  rightServos();
  delay(200);
  leftServos();
  delay(200);
  rightServos();
  delay(1000);
  stopServos();
  delay(2000);

  
  leftServos();
  delay(1250);
  stopServos();
  delay(500);
  backwardServos();
  delay(2000);
  stopServos();
  delay(500);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  stopServos();
  delay(200);
  rightServos();
  delay(500);

  //Rightfoot
  stopServos();
  delay(300);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  stopServos();
  delay(200);
  leftServos();
  delay(500);

  
  stopServos();
  delay(500);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  backwardServos();
  delay(100);
  forwardServos();
  delay(100);
  stopServos();
  delay(1000);

 

  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  rightServos();
  delay(200);
  forwardServos();
  delay(200);
  stopServos();
  delay(5000);
  
  
  
  
  // put your main code here, to run repeatedly:

}