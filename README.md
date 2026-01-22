# Stickless 🎧🥁

**Stickless** is a DIY **Bluetooth-based virtual drum stick system** that converts real-time hand movements into drum sounds using an **ESP32 + MPU6050** and a **Python audio engine**. Each stick behaves like a real drumstick, detecting hits using acceleration data and triggering drum sounds wirelessly.

---

## 🎯 Project Overview

This project turns physical drumstick motions into digital drum hits. An **MPU6050 IMU** mounted on a stick captures acceleration data, which is streamed wirelessly via **Bluetooth Serial** to a computer. A **Python program** processes this data, detects hits (kick/snare), and plays realistic drum sounds using **Pygame**.

The system is designed to be:

* **Low latency**
* **Wireless**
* **Intuitive** (natural hand motion)
* **Expandable** (multiple sticks, more instruments)

---

## 🧠 System Architecture

**Hardware Layer**

* ESP32
* MPU6050 (Accelerometer + Gyroscope)
* Battery-powered handheld drum stick enclosure

**Communication Layer**

* Bluetooth Classic (Serial Profile)

**Software Layer**

* ESP32 firmware (Arduino)
* Python hit-detection + sound engine
* Pygame audio playback

---

## 🧩 Components Used

### Hardware

* ESP32 Dev Board
* MPU6050 IMU Sensor
* Li-ion / Li-Po Battery
* Custom / improvised drumstick enclosure
* Jumper wires

### Software

* Arduino IDE
* Python 3.x
* PySerial
* Pygame
* Adafruit MPU6050 library

---

## 🔌 ESP32 Firmware (Overview)

* Initializes Bluetooth with a custom device name (e.g., `DrumStick1`)
* Reads accelerometer data from MPU6050
* Streams timestamped acceleration data in CSV format:

  ```
  millis, accelX, accelY, accelZ
  ```
* Designed for high refresh rate and low overhead

---

## 🖥️ Python Audio Engine (Overview)

The Python script:

* Connects to the ESP32 via Bluetooth serial
* Parses incoming accelerometer data
* Applies **threshold-based hit detection**
* Uses **debouncing** to avoid double triggers
* Plays drum sounds using Pygame

### Instruments Mapped

| Axis   | Motion       | Sound |
| ------ | ------------ | ----- |
| X-axis | Side hit     | Snare |
| Y-axis | Downward hit | Kick  |

Thresholds are adjustable for sensitivity tuning.

---

## 🔊 Sound Playback

* Audio handled using `pygame.mixer`
* Supports `.wav` files
* Easily extendable to:

  * Hi-hat
  * Crash cymbal
  * Toms

---

## 🧪 Hit Detection Logic

* Uses acceleration magnitude and direction
* Simple rule-based detection for reliability
* Debounce window prevents multiple hits from a single motion

Example logic:

* Strong negative X → **Snare**
* Strong positive Y → **Kick**

---

## 🖼️ Hardware Images

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/4394c0b9-0520-4663-a8ff-6961e511de0a" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/df81d025-769d-4162-bb6c-555cdcc57081" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/e52d2690-9f64-4104-9be5-bf8ce0f6614b" />



---

## 🚀 How to Run

### 1. Flash ESP32

* Open Arduino IDE
* Install required libraries
* Upload firmware to ESP32

### 2. Pair Bluetooth Device

* Pair `DrumStick1` with your computer
* Note the assigned COM port

### 3. Run Python Script

* Install dependencies:

  ```bash
  pip install pyserial pygame
  ```
* Update COM port in the script
* Run the Python file

---

## 🔮 Future Improvements

* Dual-stick support (Left & Right)
* Velocity-sensitive sound playback
* Machine-learning-based hit classification
* MIDI output support
* DAW integration (Ableton / FL Studio)
* Improved filtering (Kalman / High-pass)

---

## 🛠️ Learning Outcomes

* IMU sensor data handling
* Bluetooth serial communication
* Real-time signal processing
* Embedded + desktop system integration
* Audio programming in Python

---

## 📌 Notes

* Thresholds depend on grip style and stick orientation
* Latency is primarily limited by Bluetooth serial speed
* Designed for experimentation and extensibility

---

## 👥 Contributors

* **Sharat** – Embedded systems, Bluetooth firmware, system integration
* **Shamanth** – Signal logic, hit detection tuning, testing
* **Shreesh** – Python audio engine, sound mapping, system debugging

---

ECE Undergraduate Project
**Project Name:** Stickless
