/*Begining of Auto generated code by Atmel studio */
#include <Arduino.h>

/*End of auto generated code by Atmel studio */


//Beginning of Auto generated function prototypes by Atmel Studio
void Shift(int northChip);
//End of Auto generated function prototypes by Atmel Studio

//Pin connected to latch pin (ST_CP) of 74HC595
const int latchPin = 8;
//Pin connected to clock pin (SH_CP) of 74HC595
const int clockPin = 10;
////Pin connected to Data in (DS) of 74HC595
const int dataPin = 7;

const int magPin = 1;

const int ccwOutputPin = 5;
const int cwOutputPin = 6;

const int camCcwOutputPin = 9;
const int camCwOutputPin = 4;
const int camUpOutputPin = 3;
const int camDnOutputPin = 2;

void setup() {
  Serial.begin(9600);

  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(magPin, OUTPUT);
  pinMode(ccwOutputPin, OUTPUT);
  pinMode(cwOutputPin, OUTPUT);

  for(int i = 0; i <= 10; i++) {
    digitalWrite(i, LOW);
  }

  Shift(255);
  delay(2000);
  Shift(0);
  delay(2000);
  
  analogWrite(ccwOutputPin, 255);
  delay(1000);
  digitalWrite(ccwOutputPin, LOW);
  
  analogWrite(cwOutputPin, 255);
  delay(1000);
  digitalWrite(cwOutputPin, LOW);

  digitalWrite(magPin, HIGH);
  delay(1500);
  digitalWrite(magPin, LOW);

  pinMode(camCcwOutputPin, OUTPUT);
  pinMode(camCwOutputPin, OUTPUT);
  pinMode(camUpOutputPin, OUTPUT);
  pinMode(camDnOutputPin, OUTPUT);
  
  digitalWrite(camCcwOutputPin, LOW);
  digitalWrite(camCwOutputPin, LOW);
  digitalWrite(camUpOutputPin, LOW);
  digitalWrite(camDnOutputPin, LOW);

  for(int i = 0; i < 8; i++) {
    //Shift(1 << i);
    //delay(1500);
  }

  Shift(1); // boom up
  delay(1000);
  Shift(2); // N
  delay(1000);
  Shift(1 << 2); // S
  delay(1000);
  Shift(1 << 3); // E
  delay(1000);
  Shift(1 << 4); // W
  delay(1000);
  Shift(1 << 5); //hook up
  delay(1000);
  Shift(1 << 6); // hook down
  delay(1000);
  Shift(1 << 7); // boom down 
}

uint8_t CAM_DOWN = B00001000;
uint8_t CAM_UP = B00000100;
uint8_t CAM_CW = B00100000;
uint8_t CAM_CCW = B00010000;

uint8_t PLAT_CW = B00000010;
uint8_t PLAT_CCW = B00000001;

// 4 byte protocol: [b0][b1][b2][b3]
// b0 = [bd,hd,hu,w,e,s,n,bu]
// b1 = [x,x,cam_cw,cam_ccw,cam_d,cam_u,plat_cw,plat_ccw] = rot
// b2 = [v,v,v,v,v,v,v,v] = speed
// b3 = [x,x,x,x,x,x,x,0|1] = mag (0 or 1)

uint8_t currentSpeed = 0;
uint8_t currentDirection = 0;

uint8_t rot = 0;
uint8_t mag = 0;

void loop() {
  
  char buffer[4];

  if(Serial.available() > 0) {
    
    int numBytes = Serial.readBytes(buffer, 4);

    if(numBytes == 4) {
      
      rot = (uint8_t)buffer[1];
      currentSpeed = (uint8_t)buffer[2];
      mag = (uint8_t)buffer[3];

      // magic number signaling a change to speed
      if(mag == 255) 
      {      
        currentSpeed = (uint8_t)buffer[2];
        analogWrite(currentDirection, currentSpeed);      
        Serial.println("Updating speed");
      }
      else 
      {
        Shift(buffer[0]);
              
        // turn it all off
        if(rot == 0) {
          currentSpeed = 0;  
          digitalWrite(camDnOutputPin, LOW);
          digitalWrite(camUpOutputPin, LOW);
          digitalWrite(camCcwOutputPin, LOW);
          digitalWrite(camCwOutputPin, LOW);

          Serial.println("Rotation off");
        }
        
        if((rot & CAM_DOWN) == 8)
        {
          Serial.println("cam down");
          digitalWrite(camDnOutputPin, HIGH);
          digitalWrite(camUpOutputPin, LOW);
        }
        if((rot & CAM_UP) == CAM_UP)
        {
          Serial.println("cam up");
          digitalWrite(camDnOutputPin, LOW);
          digitalWrite(camUpOutputPin, HIGH);
        }
        if((rot & CAM_CW) == CAM_CW)
        {
          Serial.println("cam cw");
          digitalWrite(camCcwOutputPin, LOW);
          digitalWrite(camCwOutputPin, HIGH);
        }
        if((rot & CAM_CCW) == CAM_CCW)
        {
          Serial.println("cam ccw");
          digitalWrite(camCcwOutputPin, HIGH);
          digitalWrite(camCwOutputPin, LOW);
        }
        if((rot & PLAT_CW) == PLAT_CW)
        {
          Serial.println("plat cw");
          digitalWrite(ccwOutputPin, LOW);
          currentDirection = cwOutputPin;
        }
        if((rot & PLAT_CCW) == PLAT_CCW)
        {
          Serial.println("plat ccw");
          digitalWrite(cwOutputPin, LOW);
          currentDirection = ccwOutputPin;
        }
        
        analogWrite(currentDirection, currentSpeed);    
        
        if(mag == 1) {
          digitalWrite(magPin, HIGH);
          Serial.println("Mag on");
        }
        else if(mag == 0) {
          digitalWrite(magPin, LOW);
          Serial.println("Mag off");
        }
      }
    }
  }
}

void Shift(int northChip)
{
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, northChip);
  digitalWrite(latchPin, HIGH);
}
