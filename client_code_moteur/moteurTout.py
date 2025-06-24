import moteur_args as mot
from rechercheChemin import *
import spidev
import time

# --- Initialisation du robot ---
def init_robot():
    robot = {}
    robot["pi"] = mot.init_pi()
    robot["gpioM1"] = 12
    robot["gpioM2"] = 13
    robot["directions"] = ["haut", "droite", "bas", "gauche"]
    robot["direction_index"] = 0
    robot["spi"] = spidev.SpiDev()
    robot["spi"].open(0, 0)
    robot["spi"].max_speed_hz = 1000000
    return robot

# --- Fonctions de mouvement ---
def avancer(robot):
    pi = robot["pi"]
    pi.set_servo_pulsewidth(robot["gpioM1"], 500)
    pi.set_servo_pulsewidth(robot["gpioM2"], 2500)
    time.sleep(1)
    direction = robot["directions"][robot["direction_index"]]
    print(f"Le robot avance vers {direction}.")
    stop_moteurs(robot)

def stop_moteurs(robot):
    pi = robot["pi"]
    pi.set_servo_pulsewidth(robot["gpioM1"], 0)
    pi.set_servo_pulsewidth(robot["gpioM2"], 0)

def tourner(robot, angle):
    stop_moteurs(robot)
    if angle not in [90, -90]:
        print("L'angle doit être 90° ou -90°.")
        return
    pi = robot["pi"]
    if angle == 90:
        mot.start_pin(pi, robot["gpioM1"], -1)
        mot.start_pin(pi, robot["gpioM2"], -1)
        time.sleep(1)
        robot["direction_index"] = (robot["direction_index"] + 1) % 4
    else:
        mot.start_pin(pi, robot["gpioM1"], 1)
        mot.start_pin(pi, robot["gpioM2"], 1)
        time.sleep(1)
        robot["direction_index"] = (robot["direction_index"] - 1) % 4
    stop_moteurs(robot)
    direction = robot["directions"][robot["direction_index"]]
    print(f"Le robot se dirige maintenant vers {direction}.")

def afficher_direction(robot):
    direction = robot["directions"][robot["direction_index"]]
    print(f"Direction actuelle du robot : {direction}.")

# --- ADC ---
def read_adc(robot, channel):
    if not 0 <= channel <= 3:
        raise ValueError("Canal invalide : 0 à 3 uniquement")
    start_bit = 0b00000110
    command = (channel & 0b11) << 6
    result = robot["spi"].xfer2([start_bit, command, 0x00])
    value = ((result[1] & 0b00001111) << 8) | result[2]
    return value

def adc_to_degrees(raw_value):
    voltage = raw_value * 3.3 / 4095
    angle = (voltage / 3.3) * 360
    return angle

def get_angles(robot):
    raw0 = read_adc(robot, 0)
    raw1 = read_adc(robot, 1)
    return (adc_to_degrees(raw0), adc_to_degrees(raw1))

# --- Direction ---
def set_direction(robot, nDirect):
    stop_moteurs(robot)
    nIndex = robot["directions"].index(nDirect)
    current = robot["direction_index"]
    if nIndex == current:
        pass
    elif nIndex == (current + 1) % 4:
        tourner(robot, 90)
    elif nIndex == (current - 1) % 4:
        tourner(robot, -90)
    else:
        tourner(robot, 90)
        tourner(robot, 90)
    robot["direction_index"] = nIndex
    stop_moteurs(robot)

# --- Programme principal ---
if __name__ == "__main__":
    robot = init_robot()
    image_path = "grille.png"
    block_size = 20

    grid, start, end = load_grid_from_image_blocks(image_path, block_size=block_size)
    chemin = astar_directions(grid, start, end)
    print(chemin)

    try:
        for direction in chemin:
            set_direction(robot, direction)
            time.sleep(1)
            avancer(robot)
            time.sleep(1)
    finally:
        stop_moteurs(robot)
