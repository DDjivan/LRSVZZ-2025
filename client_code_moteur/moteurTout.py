from moteur_args import *
#from testFeed import *
from rechercheChemin import *

class Robot:
    def __init__(self):
        # Initialiser la direction du robot (0 = haut, 1 = droite, 2 = bas, 3 = gauche)
        self.pi=init_pi()
        self.gpioM1=12
        self.gpioM2=13
        self.directions = ["haut", "droite", "bas", "gauche"]
        self.direction_index = 0  # Direction initiale (0 = haut)

    def avancer(self):
        """Simule l'avancement du robot d'une certaine distance."""
        self.pi.set_servo_pulsewidth(self.gpioM1, 1000)
        self.pi.set_servo_pulsewidth(self.gpioM2, 2000)
        time.sleep(5)
        direction = self.directions[self.direction_index]
        print(f"Le robot avance vers {direction}.")

    def stopMoteurs():
        self.pi.set_servo_pulsewidth(self.gpioM1, 0)
        self.pi.set_servo_pulsewidth(self.gpioM2, 0)

    def tourner(self, angle):
        """Fait tourner le robot d'un certain angle (90° ou -90°)."""
        if angle not in [90, -90]:
            print("L'angle doit être 90° ou -90°.")
            return

        # Tourner à droite (90°) ou à gauche (-90°)
        if angle == 90:
            self.direction_index = (self.direction_index + 1) % 4  # Tourner à droite
        else:
            self.direction_index = (self.direction_index - 1) % 4  # Tourner à gauche

        direction = self.directions[self.direction_index]
        print(f"Le robot tourne de {angle}° et se dirige maintenant vers {direction}.")

    def afficher_direction(self):
        """Affiche la direction actuelle du robot."""
        direction = self.directions[self.direction_index]
        print(f"Direction actuelle du robot : {direction}.")

    def set_direction(self,nDirect):
        nIndex=self.directions.index(nDirect)
        if nIndex == self.direction_index :
            print("")
        elif nIndex== (self.direction_index +1) :
            tourner(90)
        elif nIndex== (self.direction_index -1) :
            tourner(-90)
        else :
            tourner(90)
            tourner(90)
        self.direction_index = nIndex

# Exemple d'utilisation de la classe Robot
if __name__ == "__main__":
    robot = Robot()
    image_path = "grille.png"  # image d'entrée
    block_size = 20

    grid, start, end = load_grid_from_image_blocks(image_path, block_size=block_size)
    chemin = astar_directions(grid, start, end)
    print(chemin)
    try :
        for i in chemin :
            set_direction(i)
            avancer()
    finally :
        robot.stopMoteurs()
