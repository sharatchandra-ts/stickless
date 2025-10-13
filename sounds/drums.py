import serial
import pygame
import time

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load your drum sounds
try:
    kick_sound = pygame.mixer.Sound("kick.wav")      # For DOWN hit
    snare_sound = pygame.mixer.Sound("snare.wav")    # For RIGHT hit
    print("✅ Sounds loaded successfully!")
except Exception as e:
    print(f"❌ Error loading sounds: {e}")
    print("Please make sure 'kick.wav' and 'snare.wav' are in the same folder")
    exit()

# Serial connection to ESP32
try:
    # Change 'COM3' to your actual port
    ser = serial.Serial('COM5', 115200, timeout=1)
    print("✅ Connected to ESP32")
except serial.SerialException:
    print("❌ Failed to connect to ESP32")
    print("Check your COM port and make sure ESP32 is connected")
    exit()

def play_sound(sound_type):
    """Play different sounds based on hit type"""
    if sound_type == "KICK":
        print("🥁 DOWN hit - Playing KICK")
        kick_sound.play()
    elif sound_type == "SNARE":
        print("🎵 RIGHT hit - Playing SNARE")
        snare_sound.play()

print("🎵 Virtual Drum Kit Started!")
print("Move the sensor:")
print("  - DOWN for KICK sound")
print("  - RIGHT for SNARE sound")
print("Press Ctrl+C to stop")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            if line == "KICK":
                play_sound("KICK")
            elif line == "SNARE":
                play_sound("SNARE")
                
except KeyboardInterrupt:
    print("\n👋 Stopping drum kit...")
    ser.close()
    pygame.quit()