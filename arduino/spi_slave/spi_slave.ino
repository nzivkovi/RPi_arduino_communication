#include "pins_arduino.h"

long buf [4];
volatile byte pos;
volatile boolean processSpiData;
long spiData;

void spi_init()
{
  pinMode(MISO, OUTPUT); // have to send on master in, *slave out*
  SPCR |= _BV(SPE); // turn on SPI in slave mode
  SPCR |= _BV(SPIE); // turn on interrupts
  pos = 0;
  processSpiData = false;
}

void resetParameters()
{
  pos = 0;
  processSpiData = false;
}


long getLongFromBytes()
{
  long value = buf[3] | (buf[2] | (buf[1] | buf[0] << 8) << 8) << 8;
  return value;
}

void checkSPIData()
{
  if(processSpiData)
  {
    spiData = getLongFromBytes();
    Serial.println(spiData);
    resetParameters(); 
  }
}

// SPI interrupt routine
ISR (SPI_STC_vect)
{
  byte c = SPDR;
  buf [pos++] = c;
  if(pos==4)
  {
    processSpiData = true;
  }
}

void setup()
{
  Serial.begin(9600);
  spi_init();
}

void loop()
{
  checkSPIData();
}

