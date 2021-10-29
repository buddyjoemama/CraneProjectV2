/*Begining of Auto generated code by Atmel studio */
#include <Arduino.h>

/*End of auto generated code by Atmel studio */

//Beginning of Auto generated function prototypes by Atmel Studio
void Shift(uint8_t northChip);
//End of Auto generated function prototypes by Atmel Studio

//Pin connected to latch pin (ST_CP) of 74HC595
const int latchPin = 8;
//Pin connected to clock pin (SH_CP) of 74HC595
const int clockPin = 10;
////Pin connected to Data in (DS) o f 74HC595
const int dataPin = 7;

const int magPin = 1;

const int ccwOutputPin = 5;
const int cwOutputPin = 6;

const int camCcwOutputPin = 9;
const int camCwOutputPin = 4;
const int camUpOutputPin = 3;
const int camDnOutputPin = 2;

void handleMessage(char *buffer);

void setup()
{
  Serial.begin(9600);

  while (!Serial)
    ;

  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(magPin, OUTPUT);
  pinMode(ccwOutputPin, OUTPUT);
  pinMode(cwOutputPin, OUTPUT);

  for (int i = 0; i <= 10; i++)
  {
    digitalWrite(i, LOW);
  }

  /*Shift(255);
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
  */

  pinMode(camCcwOutputPin, OUTPUT);
  pinMode(camCwOutputPin, OUTPUT);
  pinMode(camUpOutputPin, OUTPUT);
  pinMode(camDnOutputPin, OUTPUT);

  digitalWrite(camCcwOutputPin, LOW);
  digitalWrite(camCwOutputPin, LOW);
  digitalWrite(camUpOutputPin, LOW);
  digitalWrite(camDnOutputPin, LOW);
}

uint8_t CAM_CW =   B10000000;
uint8_t CAM_CCW =  B01000000;
uint8_t CAM_DOWN = B00100000;
uint8_t CAM_UP =   B00010000;

uint8_t PLAT_CW =  B00000010;
uint8_t PLAT_CCW = B00000001;

uint8_t BOOM_UP   = B10000000;
uint8_t HOOK_UP   = B01000000;
uint8_t HOOK_DOWN = B00100000;
uint8_t WEST      = B00010000;
uint8_t EAST      = B00001000;
uint8_t SOUTH     = B00000100;
uint8_t NORTH     = B00000010;
uint8_t BOOM_DOWN = B00000001;

// 4 byte protocol: [b0][b1][b2][b3]
// b0 = [bu,hu,hd,w,e,s,n,bd]
// b1 = [cam_cw,cam_ccw,cam_d,cam_u,plat_cw,x,xplat_ccw] = rot
// b2 = [v,v,v,v,v,v,v,v] = speed
// b3 = [x,x,x,x,x,x,x,0|1] = mag (0 or 1)

uint8_t currentSpeed = 0;
uint8_t currentDirection = 0;

uint8_t rot = 0;
uint8_t mag = 0;

const unsigned int MAX_LENGTH = 4;

void loop()
{
  while (Serial.available() > 0)
  {

    static char message[MAX_LENGTH];
    static unsigned int message_pos = 0;

    char inByte = Serial.read();

    if (message_pos <= MAX_LENGTH)
    {
      message[message_pos] = inByte;
      message_pos += 1;

      if (message_pos >= MAX_LENGTH)
      {
        handleMessage(message);
        message_pos = 0;
      }
    }
  }
}

void handleMessage(char *buffer)
{
  String rotationResult = "\"rotation\": {}";
  
  rot = (uint8_t)buffer[1];
  currentSpeed = (uint8_t)buffer[2];
  mag = (uint8_t)buffer[3];

  // magic number signaling a change to speed
  if (mag == 255)
  {
    currentSpeed = (uint8_t)buffer[2];
    analogWrite(currentDirection, currentSpeed);
  }
  else
  {
    Shift(buffer[0]);

    // turn it all off
    if (rot == 0)
    {
      currentSpeed = 0;
      digitalWrite(camDnOutputPin, LOW);
      digitalWrite(camUpOutputPin, LOW);
      digitalWrite(camCcwOutputPin, LOW);
      digitalWrite(camCwOutputPin, LOW);
      
      digitalWrite(ccwOutputPin, LOW);
      digitalWrite(cwOutputPin, LOW);
    }
    else
    {
      rotationResult = HandleRotation(rot, currentSpeed);
    }

    if(mag == 1)
    {
      digitalWrite(magPin, HIGH);
    }
    else if(mag == 0) 
    {
      digitalWrite(magPin, LOW);
    }
    
    String rawByteZero = String((uint8_t)buffer[0], BIN);
    String rawByteOne = String(rot, BIN);
    String rawByteTwo = String(currentSpeed, BIN);
    String rawByteThree = String(mag, BIN);
    
    // 4 byte protocol: [b0][b1][b2][b3]
    // b0 = [bu,hu,hd,w,e,s,n,bd]
    // b1 = [cam_cw,cam_ccw,cam_d,cam_u, x, x, plat_cw,plat_ccw] = rot
    // b2 = [v,v,v,v,v,v,v,v] = speed
    // b3 = [x,x,x,x,x,x,x,0|1] = mag (0 or 1)

    uint8_t byteZero = (uint8_t)buffer[0];
    boolean boomDown = ((byteZero & BOOM_DOWN) == BOOM_DOWN);
    boolean boomUp = ((byteZero & BOOM_UP) == BOOM_UP);
    boolean hookDown = ((byteZero & HOOK_DOWN) == HOOK_DOWN);
    boolean hookUp = ((byteZero & HOOK_UP) == HOOK_UP);
    boolean platNorth = ((byteZero & NORTH) == NORTH);
    boolean platEast = ((byteZero & EAST) == EAST);
    boolean platSouth = ((byteZero & SOUTH) == SOUTH);
    boolean platWest = ((byteZero & WEST) == WEST);
    
    String result = "{\"result\": {";
    result = String(result + "\"[bd,hd,hu,w,e,s,n,bu]\":" + rawByteZero + ",");
    result = String(result + "\"[cam_cw, cam_ccw, cam_d, cam_u, x, x, plat_cw, plat_ccw]\":" + rawByteOne + ",");
    result = String(result + "\"[v,v,v,v,v,v,v,v] (speed)\":" + rawByteTwo + ",");
    result = String(result + "\"[x,x,x,x,x,x,0|1] (magnet)\":" + rawByteThree + "},");
      result = String(result + "\"details\":{");
      //result = String(result + "\"boom-down\":" + boomDown);
      //result = String(result + ",\"boom-up\":" + boomUp);
      //result = String(result + ",\"hook-down\":" + hookDown);
      //result = String(result + ",\"hook-up\":" + hookUp);
      //result = String(result + ",\"plat-north\":" + platNorth);
      //result = String(result + ",\"plat-east\":" + platEast);
      //result = String(result + ",\"plat-south\":" + platSouth);    
      //result = String(result + ",\"plat-west\":" + platWest);
      //result = String(result + "," + rotationResult);
      result = String(result + "}");
    result = String(result + "}");
    
    Serial.println(result);
  }
}

/**
* Handle the camera direction and return the result as a json string.
*/
String HandleRotation(uint8_t rot, uint8_t currentSpeed)
{
  String rotationResult = "\"rotation\": {";
  
  if ((rot & CAM_DOWN) == CAM_DOWN)
  {
    digitalWrite(camDnOutputPin, HIGH);
    digitalWrite(camUpOutputPin, LOW);
    rotationResult = String(rotationResult + "\"cameraDown\": true");
  }
  else if ((rot & CAM_UP) == CAM_UP)
  {
    digitalWrite(camDnOutputPin, LOW);
    digitalWrite(camUpOutputPin, HIGH);
    rotationResult = String(rotationResult + "\"cameraUp\": true");
  }
  else if ((rot & CAM_CW) == CAM_CW)
  {
    digitalWrite(camCcwOutputPin, LOW);
    digitalWrite(camCwOutputPin, HIGH);
    rotationResult = String(rotationResult + "\"cameraClockwise\": true");
  }
  else if ((rot & CAM_CCW) == CAM_CCW)
  {
    digitalWrite(camCcwOutputPin, HIGH);
    digitalWrite(camCwOutputPin, LOW);
    rotationResult = String(rotationResult + "\"cameraCounterClockwise\": true");
  }
  else if ((rot & PLAT_CW) == PLAT_CW)
  {
    digitalWrite(ccwOutputPin, LOW);
    currentDirection = cwOutputPin;
    rotationResult = String(rotationResult + "\"platformClockwise\": true");
  }
  else if ((rot & PLAT_CCW) == PLAT_CCW)
  {
    digitalWrite(cwOutputPin, LOW);
    currentDirection = ccwOutputPin;
    rotationResult = String(rotationResult + "\"platformCounterClockwise\": true");
  }

  if (currentDirection != 0)
  {
    analogWrite(currentDirection, currentSpeed);
    currentDirection = 0;
  }
  
  return String(rotationResult + "}");
}

/*
* Shift out a byte of data.
*/ 
void Shift(uint8_t northChip)
{
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, northChip);
  digitalWrite(latchPin, HIGH);
}
