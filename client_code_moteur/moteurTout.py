import moteur_args as mot
from rechercheChemin import *
from testFeed import *
import time
import RPi.GPIO as GPIO


class Robot:
    def __init__(self):
        # Initialiser la direction du robot (0 = haut, 1 = droite, 2 = bas, 3 = gauche)
        self.pi=mot.init_pi()
        self.gpioM1=12
        self.gpioM2=13
        self.directions = ["haut", "droite", "bas", "gauche"]
        self.direction_index = 0  # Direction initiale (0 = haut)
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 23
        self.ECHO = 24
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    def avancer(self,presObstacle):
        """Simule l'avancement du robot d'une certaine distance."""
        duree_avance=1
        trancheSeuil=5 #pas de descente du seuil
        seuil=30 #seuil d'arret en cm'
        self.pi.set_servo_pulsewidth(self.gpioM1, 500)
        self.pi.set_servo_pulsewidth(self.gpioM2, 2500)
        if presObstacle : #Si obstacle, avancer avec descente du seuil d'arrêt'
            for iter in range(trancheSeuil) :
                while GPIO.input(self.ECHO) == 0:
                    duree_debut = time.time()
                while GPIO.input(self.ECHO) == 1:
                    duree_fin = time.time()

                duree_impulsion = duree_fin - duree_debut
                distance = duree_impulsion * (34000/2)
                distance = round(distance, 2)
                if distance <seuil - iter*seuil/trancheSeuil : #si obstacle imprévu, arrêt et attente.
                    self.stopMoteurs()
                    while distance <seuil - iter*seuil/trancheSeuil :
                        while GPIO.input(self.ECHO) == 0:
                            duree_debut = time.time()
                        while GPIO.input(self.ECHO) == 1:
                            duree_fin = time.time()

                        duree_impulsion = duree_fin - duree_debut
                        distance = duree_impulsion * (34000/2)
                        distance = round(distance, 2)
                    self.pi.set_servo_pulsewidth(self.gpioM1, 500)
                    self.pi.set_servo_pulsewidth(self.gpioM2, 2500)
                time.sleep(duree_avance/trancheSeuil)

        else :
            for iter in range(trancheSeuil) :
                while GPIO.input(self.ECHO) == 0:
                    duree_debut = time.time()
                while GPIO.input(self.ECHO) == 1:
                    duree_fin = time.time()

                duree_impulsion = duree_fin - duree_debut
                distance = duree_impulsion * (34000/2)
                distance = round(distance, 2)
                if distance <seuil : #si obstacle imprévu, arrêt et attente.
                    self.stopMoteurs()
                    while distance <seuil :
                        while GPIO.input(self.ECHO) == 0:
                            duree_debut = time.time()
                        while GPIO.input(self.ECHO) == 1:
                            duree_fin = time.time()

                        duree_impulsion = duree_fin - duree_debut
                        distance = duree_impulsion * (34000/2)
                        distance = round(distance, 2)
                    self.pi.set_servo_pulsewidth(self.gpioM1, 500)
                    self.pi.set_servo_pulsewidth(self.gpioM2, 2500)
                time.sleep(duree_avance/trancheSeuil)

        direction = self.directions[self.direction_index]
        print(f"Le robot avance vers {direction}.")
        self.stopMoteurs()

    def stopMoteurs(self):
        self.pi.set_servo_pulsewidth(self.gpioM1, 1500)
        self.pi.set_servo_pulsewidth(self.gpioM2, 1500)

    def tourner(self, angle):
        self.stopMoteurs()
        """Fait tourner le robot d'un certain angle (90° ou -90°)."""
        if angle not in [90, -90]:
            print("L'angle doit être 90° ou -90°.")
            return
        # Tourner à droite (90°) ou à gauche (-90°)
        a0,a1=lire_feedback_servos(ads)
        if angle == 90:
            aFinal=(a0-273)%360
            mot.start_pin(self.pi, self.gpioM1, -1)
            mot.start_pin(self.pi, self.gpioM2, -1)
            while not(aFinal-10<a0 & a0<aFinal+10):
                time.sleep(0.1)
            self.direction_index = (self.direction_index + 1) % 4  # Tourner à droite
        else:
            aFinal=(a0+273)%360
            mot.start_pin(self.pi, self.gpioM1, 1)
            mot.start_pin(self.pi, self.gpioM2, 1)
            while not(aFinal-10<a0 & a0<aFinal+10):
                time.sleep(0.1)
            self.direction_index = (self.direction_index - 1) % 4  # Tourner à gauche
        self.stopMoteurs()
        direction = self.directions[self.direction_index]
        print(f"Le robot se dirige maintenant vers {direction}.")

    def afficher_direction(self):
        """Affiche la direction actuelle du robot."""
        direction = self.directions[self.direction_index]
        print(f"Direction actuelle du robot : {direction}.")

    def set_direction(self,nDirect):
        self.stopMoteurs()
        nIndex=self.directions.index(nDirect)
        if nIndex == self.direction_index :
            print("")
        elif nIndex== ((self.direction_index +1)%4) :
            self.tourner(90)
        elif nIndex== ((self.direction_index -1)%4) :
            self.tourner(-90)
        else :
            self.tourner(90)
            self.tourner(90)
        self.direction_index = nIndex
        self.stopMoteurs()

# Exemple d'utilisation de la classe Robot
if __name__ == "__main__":
    robot = Robot()
    image_path = "grille.png"  # image d'entrée
    block_size = 20

    grid, start, end = load_grid_from_image_blocks(image_path, block_size=block_size)
    chemin = astar_directions(grid, start, end)
    obstacleA=analyze_path_with_obstacle_ahead(grid, start, end)
    print(chemin)
    try :
        for i in range(len(chemin)) :
            robot.set_direction(chemin[i])
            robot.avancer(obstacleA[i])
            time.sleep(1)
        robot.stopMoteurs()
        opposite_directions = {
        "haut": "bas",
        "bas": "haut",
        "gauche": "droite",
        "droite": "gauche"
        }
        # --- Inversion du chemin pour retour arrière ---
        chemin_inverse = [opposite_directions[dir] for dir in reversed(chemin)]
        print("Retour arrière :", chemin_inverse)
        obstacleR=analyze_path_with_obstacle_ahead(grid, end, start)
        for j in range(len(chemin_inverse)):
            robot.set_direction(chemin_inverse[j])
            time.sleep(1)
            robot.avancer(obstacleR[j])
            time.sleep(1)
    finally :
        robot.stopMoteurs()
        GPIO.cleanup()

