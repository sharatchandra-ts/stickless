#include "BluetoothSerial.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;
BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("DrumStick1");

  if (!mpu.begin()) {
    Serial.println("MPU6050 connection failed. Check wiring!");
    while (1);
  }

  Serial.println("READY");
} 

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  SerialBT.printf("%lu,%.3f,%.3f,%.3f\n", millis(), a.acceleration.x, a.acceleration.y, a.acceleration.z);

  /*
  float threshold = 200.0;

  float accX = a.acceleration.x;
  float accY = a.acceleration.y;
  // float accZ = a.acceleration.z;

  if (accY*accY > threshold + 100) {
    // Serial.println("KICK");
    SerialBT.println("KICK");
  }

  else if (accX*accX > threshold) {
    // Serial.println("SNARE");
    SerialBT.println("SNARE");

  }

  delay(100);
  */
}
