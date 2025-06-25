import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  

TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)



print("Demarrage de la lecture de la distance de l'obstacle")

GPIO.output(TRIG, False)  
time.sleep(2)

GPIO.output(TRIG, True)    
time.sleep(0.00001)

GPIO.output(TRIG, False)   


while GPIO.input(ECHO) == 0:   
    print("aa")
    duree_debut = time.time()
    

while GPIO.input(ECHO) == 1:
    print("b")
    duree_fin = time.time()
    
duree_impulsion = duree_fin - duree_debut

distance = duree_impulsion * (34000/2)
distance = round(distance, 2)
print ("Distance de lobstacle: ", distance, " cm")

GPIO.cleanup()
