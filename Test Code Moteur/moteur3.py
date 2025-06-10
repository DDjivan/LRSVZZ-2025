import pigpio
import time

SERVO1_PIN = 12  # Pin du servo1
# Initialisation de pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Erreur : pigpiod ne tourne pas. Lancer 'sudo pigpiod' d'abord.")
    exit()


while True :


