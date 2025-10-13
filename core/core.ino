#include <Wire.h>
#include <MPU9250.h>

MPU9250 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);  //is this code  SDA=21, SCL=22 in esp32

 
  delay(1000);
  
  if (!mpu.setup(0x68)) {
    Serial.println("MPU connection failed. Check wiring!");
    while (1);
  }

  Serial.println("READY"); 
  delay(1000);
}

void loop() {
  if (mpu.update()) {
    float accX = mpu.getAccX();
    float accY = mpu.getAccY();
    float accZ = mpu.getAccZ();
    
  
    if (accY > 4.0) {//for down
      Serial.println("KICK");

    }
    

    if (accX > 4.0) {// right swing 
      Serial.println("SNARE");
 
    }
    
    delay(50);
  }
}