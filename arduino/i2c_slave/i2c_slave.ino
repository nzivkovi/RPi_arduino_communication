#include <Wire.h>
#define SLAVE_ADDRESS 0x44
int rand_int_in_range(int lower, int upper) {
  return lower + (rand() % static_cast<int>(upper - lower + 1));
}

float rand_float_in_range(int lower, int upper) {
  return lower + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(upper - lower)));  
}

float leftWheelEncoder, rightWheelEncoder;
int leftIRSensor, centerIRSensor, rightIRSensor;

void setup() {
  Serial.begin(115200);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(sendData);

}

void updateValues() {
  leftWheelEncoder = rand_float_in_range(1, 10);
  rightWheelEncoder = rand_float_in_range(1, 10);

  leftIRSensor = rand_int_in_range(1, 10);
  centerIRSensor = rand_int_in_range(1, 10);
  rightIRSensor = rand_int_in_range(1, 10);
}

void loop() {
  updateValues();
}

void sendData() {
  Wire.write((char *)&leftWheelEncoder, sizeof(leftWheelEncoder));
  Wire.write((char *)&rightWheelEncoder, sizeof(rightWheelEncoder));
  Wire.write((char *)&leftIRSensor, sizeof(leftIRSensor));
  Wire.write((char *)&centerIRSensor, sizeof(centerIRSensor));
  Wire.write((char *)&rightIRSensor, sizeof(rightIRSensor));
}
