import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

print("Lecture de l'état de ECHO pendant 5 secondes :")
start = time.time()
while time.time() - start < 5:
    print(GPIO.input(24))
    time.sleep(0.1)

GPIO.cleanup()
