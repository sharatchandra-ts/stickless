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
  SerialBT.begin("DrumStick1");
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

  float ax = a.acceleration.x;
  float ay = a.acceleration.y;
  float az = a.acceleration.z;

  float accMagnitude = sqrt(ax*ax + ay*ay + az*az);
  unsigned long now = millis();

  if (accMagnitude > threshold && !hitDetected && (now - lastHitTime > 300)) {
    hitDetected = true;
    lastHitTime = now;

    String soundType = "snare"; // default

    // crude direction classification
    if (az > 15) soundType = "kick";
    else if (ax > 15) soundType = "snare";
    else if (ax < -15) soundType = "hihat";
    else if (az < -15) soundType = "crash";

    SerialBT.println(soundType);
    Serial.print("HIT: ");
    Serial.println(soundType);
  }

  if (accMagnitude < 5.0) {
    hitDetected = false;
  }

  delay(5);
}
