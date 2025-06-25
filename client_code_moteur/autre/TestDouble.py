import RPi.GPIO as GPIO
import time
import pigpio

GPIO.setmode(GPIO.BCM)
Moteur_droit = 13
Moteur_gauche = 12
Trig = 23
Echo = 24

#GPIO.setup(Moteur_droit, GPIO.OUT)
#GPIO.setup(Moteur_gauche, GPIO.OUT)

GPIO.setup(Echo, GPIO.IN)
GPIO.setup(Trig, GPIO.OUT)

GPIO.output(Trig, False)

#Moteurs Setup
# Initialisation de pigpio
pi = pigpio.pi()
#Fin Moteurs Setup
try:
    while True:
        #verifier sil y a un obstacle
        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)
        while GPIO.input(Echo) == 0:
            duree_debut = time.time()
        while GPIO.input(Echo) == 1:
            duree_fin = time.time()
        duree_impulsion = duree_fin - duree_debut
        distance = duree_impulsion * (34000/2)
        distance = round(distance, 2)
        print ("Distance de lobstacle: ", distance, " cm")


        if distance > 20:
            #pas d'obstacle: on avance
            pi.set_servo_pulsewidth(Moteur_gauche, 2000) #Marche gauche
            pi.set_servo_pulsewidth(Moteur_droit, 1000) #Marche droite

            #GPIO.output(Moteur_droit,GPIO.HIGH)
            #GPIO.output(Moteur_gauche,GPIO.HIGH)

        else:
            #obstacle detecte: arrêt du moteur
            pi.set_servo_pulsewidth(Moteur_gauche, 1500) #Arrêt gauche
            pi.set_servo_pulsewidth(Moteur_droit, 1500) #Arrêt droite

        time.sleep(0.5)
finally:
    print("Arrêt PWM & libération...")
    pi.set_servo_pulsewidth(Moteur_gauche, 1500)
    pi.set_servo_pulsewidth(Moteur_droit, 1500)
    pi.stop()





