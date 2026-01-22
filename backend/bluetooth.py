import serial
import serial.tools.list_ports
import pygame
import time

# List available ports
print("Available serial ports:")
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(f"  {p.device}")

# Try to open the port
try:
    serR = serial.Serial("COM7", 115200, timeout=50)
    # serL = serial.Serial("COM5", 115200, timeout=50)
except serial.SerialException as e:
    print(f"Could not open port COM6: {e}")
    print("Please check your device connection and port name.")
    exit(1)

KICK_THRESHOLD_R = 16
SNARE_THRESHOLD_R = 15
KICK_THRESHOLD_L = 4
SNARE_THRESHOLD_L = 4
DEBOUNCE_MS = 200

last_time_r = 0
last_time_l = 0
now = 0

pygame.mixer.init()

def play_sound(sound_type):
    try:
        kick_sound = pygame.mixer.Sound("sounds/kick.wav")
        snare_sound = pygame.mixer.Sound("sounds/snare.wav")
    except Exception as e:
        print(f"Error loading sounds: {e}")   
        exit()

    if sound_type == "KICK-R":
        print("KICK-R")
        kick_sound.play()
    elif sound_type == "SNARE-R":
        print("SNARE-R")
        snare_sound.play()
    if sound_type == "KICK-L":
        print("KICK-L")
        kick_sound.play()
    elif sound_type == "SNARE-L":
        print("SNARE-L")
        snare_sound.play()

while True:
    try:
        lineR = serR.readline().decode().strip()
        if not lineR:
            continue

        partsR = lineR.split(',')
        if len(partsR) != 4:
            continue  # bad line

        now = int(time.time() * 1000)

        # timestamp, accelX, accelY, accelZ
        tR, xR, yR, zR = partsR
        xR = float(xR)
        yR = float(yR)
        zR = float(zR)

        # simple hit detection
        if -(xR) > SNARE_THRESHOLD_R and now - last_time_r > DEBOUNCE_MS:
            play_sound("SNARE-R")
            last_time_r = now
        elif (yR) > KICK_THRESHOLD_R and now - last_time_r > DEBOUNCE_MS:
            play_sound("KICK-R")
            last_time_r = now
        # if -(y) > KICK_THRESHOLD and now - last_time > DEBOUNCE_MS:
        #     play_sound("KICK2")
        #     last_time = now
        # optionally add hihat/crash using z or other axes
        # if abs(z) > CRASH_THRESHOLD and now - last_time > DEBOUNCE_MS:
        #     print("CRASH")
        #     last_time = now

        lineL = serL.readline().decode().strip()
        if not lineL:
            continue

        partsL = lineL.split(',')
        if len(partsL) != 4:
            continue  # bad line

        # timestamp, accelX, accelY, accelZ
        tL, xL, yL, zL = partsL
        xL = float(xL)
        yL = float(yL)
        zL = float(zL)


        # simple hit detection
        if abs(xL) > SNARE_THRESHOLD_L and now - last_time_l > DEBOUNCE_MS:
            play_sound("SNARE-L")
            last_time_l = now
        elif abs(yL) > KICK_THRESHOLD_L and now - last_time_l > DEBOUNCE_MS:
            play_sound("KICK-L")
            last_time_l = now
        # if -(y) > KICK_THRESHOLD and now - last_time > DEBOUNCE_MS:
        #     play_sound("KICK2")
        #     last_time = now
        # optionally add hihat/crash using z or other axes
        # if abs(z) > CRASH_THRESHOLD and now - last_time > DEBOUNCE_MS:
        #     print("CRASH")
        #     last_time = now

    except Exception as e:
        print("Error:", e)