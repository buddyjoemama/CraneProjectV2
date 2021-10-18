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

uint8_t CAM_DOWN = B00001000;
uint8_t CAM_UP = B00000100;
uint8_t CAM_CW = B00100000;
uint8_t CAM_CCW = B00010000;

uint8_t PLAT_CW = B00000010;
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
// b1 = [x,x,cam_cw,cam_ccw,cam_d,cam_u,plat_cw,plat_ccw] = rot
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
    }
    else
    {
      HandleRotation(rot, currentSpeed);
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
    // b1 = [x,x,cam_cw,cam_ccw,cam_d,cam_u,plat_cw,plat_ccw] = rot
    // b2 = [v,v,v,v,v,v,v,v] = speed
    // b3 = [x,x,x,x,x,x,x,0|1] = mag (0 or 1)

    uint8_t byteZero = (uint8_t)buffer[0];
    
    String result = "{\"result\": {";
    result = String(result + "\"[bd,hd,hu,w,e,s,n,bu]\":" + rawByteZero + ",");
    result = String(result + "\"[x,x,cam_cw, cam_ccw, cam_d, cam_u, plat_cw, plat_ccw]\":" + rawByteOne + ",");
    result = String(result + "\"[v,v,v,v,v,v,v,v] (speed)\":" + rawByteTwo + ",");
    result = String(result + "\"[x,x,x,x,x,x,0|1] (magnet)\":" + rawByteThree + "},");
      result = String(result + "\"details\":{");
      result = String(result + "\"boom-down\":" + ((byteZero & BOOM_DOWN) == BOOM_DOWN));
      result = String(result + ",\"boom-up\":" + ((byteZero & BOOM_UP) == BOOM_UP));
      result = String(result + ",\"hook-down\":" + ((byteZero & HOOK_DOWN) == HOOK_DOWN));
      result = String(result + ",\"hook-up\":" + ((byteZero & HOOK_UP) == HOOK_UP));
      result = String(result + ",\"plat-north\":" + ((byteZero & NORTH) == NORTH));
      result = String(result + ",\"plat-east\":" + ((byteZero & EAST) == EAST));
      result = String(result + ",\"plat-south\":" + ((byteZero & SOUTH) == SOUTH));
      result = String(result + ",\"plat-west\":" + ((byteZero & WEST) == WEST));
      result = String(result + "}");
    result = String(result + "}");
    
    Serial.println(result);
  }
}

void HandleRotation(uint8_t rot, uint8_t currentSpeed)
{
  if ((rot & CAM_DOWN) == 8)
  {
    digitalWrite(camDnOutputPin, HIGH);
    digitalWrite(camUpOutputPin, LOW);
  }
  else if ((rot & CAM_UP) == CAM_UP)
  {
    digitalWrite(camDnOutputPin, LOW);
    digitalWrite(camUpOutputPin, HIGH);
  }
  else if ((rot & CAM_CW) == CAM_CW)
  {
    digitalWrite(camCcwOutputPin, LOW);
    digitalWrite(camCwOutputPin, HIGH);
  }
  else if ((rot & CAM_CCW) == CAM_CCW)
  {
    digitalWrite(camCcwOutputPin, HIGH);
    digitalWrite(camCwOutputPin, LOW);
  }
  else if ((rot & PLAT_CW) == PLAT_CW)
  {
    digitalWrite(ccwOutputPin, LOW);
    currentDirection = cwOutputPin;
  }
  else if ((rot & PLAT_CCW) == PLAT_CCW)
  {
    digitalWrite(cwOutputPin, LOW);
    currentDirection = ccwOutputPin;
  }

  if (currentDirection != 0)
  {
    analogWrite(currentDirection, currentSpeed);
    currentDirection = 0;
  }
}

void Shift(int northChip)
{
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, MSBFIRST, northChip);
  digitalWrite(latchPin, HIGH);
}
