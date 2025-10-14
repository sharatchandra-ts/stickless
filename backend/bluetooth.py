import serial
import pygame
import time

# replace COM6 with your Bluetooth COM port
ser = serial.Serial("COM6", 115200, timeout=50)

KICK_THRESHOLD = 15
SNARE_THRESHOLD = 15
DEBOUNCE_MS = 200

last_time = 0
now = 0

pygame.mixer.init()

def play_sound(sound_type):
    try:
        kick_sound = pygame.mixer.Sound("sounds/kick.wav")
        snare_sound = pygame.mixer.Sound("sounds/snare.wav")
    except Exception as e:
        print(f"Error loading sounds: {e}")   
        exit()

    if sound_type == "KICK":
        print("KICK")
        kick_sound.play()
    elif sound_type == "SNARE":
        print("SNARE")
        snare_sound.play()

while True:
    try:
        line = ser.readline().decode().strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) != 4:
            continue  # bad line

        now = int(time.time() * 1000)

        # timestamp, accelX, accelY, accelZ
        t, x, y, z = parts
        x = float(x)
        y = float(y)
        z = float(z)

        # simple hit detection
        if abs(x) > SNARE_THRESHOLD and now - last_time > DEBOUNCE_MS:
            play_sound("SNARE")
            last_time = now
        if abs(y) > KICK_THRESHOLD and now - last_time > DEBOUNCE_MS:
            play_sound("KICK")
            last_time = now
        # optionally add hihat/crash using z or other axes
        # if abs(z) > CRASH_THRESHOLD and now - last_time > DEBOUNCE_MS:
        #     print("CRASH")
        #     last_time = now

    except Exception as e:
        print("Error:", e)