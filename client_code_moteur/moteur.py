import pigpio
import time

SERVO_PIN = 12  # BCM, GPIO compatible PWM

# Initialisation de pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Erreur : pigpiod ne tourne pas. Lance 'sudo pigpiod' d'abord.")
    exit()

print("Contrôle interactif du FS90R (pigpio, impulsion en µs)")
print("Tape une largeur d'impulsion (µs), ex : 1500 pour stop, 1000 ou 2000 pour tourner")
print("Tape 'exit' pour quitter.")

try:
    while True:
        user_input = input("Impulsion µs (ex: 1000-2000): ")
        if user_input.lower() == "exit":
            break
        try:
            pulse_width = int(user_input)
            if 500 <= pulse_width <= 2500:
                pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)
                print(f"→ PWM : {pulse_width} µs")
            else:
                print("⚠️ Valeur hors plage (500 - 2500 us recommandés)")
        except ValueError:
            print("❌ Entrée invalide.")
finally:
    print("Arrêt PWM & libération...")
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
