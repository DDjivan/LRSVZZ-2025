import moteur_args as mot
from rechercheChemin import *
import spidev
import time

class Robot:
    def __init__(self):
        # Initialiser la direction du robot (0 = haut, 1 = droite, 2 = bas, 3 = gauche)
        self.pi=mot.init_pi()
        self.gpioM1=12
        self.gpioM2=13
        self.directions = ["haut", "droite", "bas", "gauche"]
        self.direction_index = 0  # Direction initiale (0 = haut)
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)  # Bus SPI 0, périphérique CS0
        self.spi.max_speed_hz = 1000000  # Fréquence adaptée au MCP3204

    def avancer(self):
        """Simule l'avancement du robot d'une certaine distance."""

        self.pi.set_servo_pulsewidth(self.gpioM1, 500)
        self.pi.set_servo_pulsewidth(self.gpioM2, 2500)
        time.sleep(1)
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
        if angle == 90:
            mot.start_pin(self.pi, self.gpioM1, -1)
            mot.start_pin(self.pi, self.gpioM2, -1)
            time.sleep(1)
            self.direction_index = (self.direction_index + 1) % 4  # Tourner à droite
        else:
            mot.start_pin(self.pi, self.gpioM1, 1)
            mot.start_pin(self.pi, self.gpioM2, 1)
            time.sleep(1)
            self.direction_index = (self.direction_index - 1) % 4  # Tourner à gauche
        self.stopMoteurs()
        direction = self.directions[self.direction_index]
        print(f"Le robot se dirige maintenant vers {direction}.")

    def afficher_direction(self):
        """Affiche la direction actuelle du robot."""
        direction = self.directions[self.direction_index]
        print(f"Direction actuelle du robot : {direction}.")


        # --- Fonction de lecture MCP3204 ---
    def read_adc(self,channel):
        if not 0 <= channel <= 3:
            raise ValueError("Canal invalide : 0 à 3 uniquement")
        start_bit = 0b00000110
        command = (channel & 0b11) << 6
        result = self.spi.xfer2([start_bit, command, 0x00])
        value = ((result[1] & 0b00001111) << 8) | result[2]
        return value

    # --- Conversion en degrés ---
    def adc_to_degrees(self,raw_value):
        """
        Convertit la valeur ADC brute en angle en degrés.
        Hypothèse : 0 V = 0°, 3.3 V = 180°
        """
        voltage = raw_value * 3.3 / 4095  # Convertir en volts
        angle = (voltage / 3.3) * 360     # Proportion linéaire
        return angle

        # --- Retourne les valeurs d'angles---
    def getAngles(self):
        raw = self.read_adc(0)  # Lecture sur canal CH0
        angle = self.adc_to_degrees(raw)
        angle0= angle
        raw = self.read_adc(1)  # Lecture sur canal CH0
        angle = self.adc_to_degrees(raw)
        angle1=angle
        return (angle0,angle1)

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
    print(chemin)
    try :
        for i in chemin :
            robot.set_direction(i)
            robot.avancer()
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

        for direction in chemin_inverse:
            robot.set_direction(direction)
            time.sleep(1)
            robot.avancer()
            time.sleep(1)
    finally :
        stop_moteurs(robot)

