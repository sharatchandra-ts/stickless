#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include "BluetoothSerial.h"

Adafruit_MPU6050 mpu;
BluetoothSerial SerialBT;

float threshold = 15.0;  
bool hitDetected = false;
unsigned long lastHitTime = 0;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("DrumStick1");  // name that shows in Bluetooth list
  Wire.begin();

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050");
    while (1);
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  Serial.println("Bluetooth DrumStick ready!");
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  float accMagnitude = sqrt(a.acceleration.x * a.acceleration.x +
                            a.acceleration.y * a.acceleration.y +
                            a.acceleration.z * a.acceleration.z);

  unsigned long now = millis();

  if (accMagnitude > threshold && !hitDetected && (now - lastHitTime > 300)) {
    hitDetected = true;
    lastHitTime = now;
    SerialBT.println("HIT");
    Serial.println("HIT!");
  }

  if (accMagnitude < 5.0) {
    hitDetected = false;
  }

  delay(5);
}
