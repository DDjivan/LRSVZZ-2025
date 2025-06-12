# from pigpio import pi
import time
from argparse import ArgumentParser
from datetime import datetime

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

def printT(arg) -> None:
    time = datetime.now().isoformat().replace('T', ' ')
    print(f"{time} — {arg}")

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

def init_pi():
    arg_pi = pi()

    if not arg_pi.connected:
        raise Exception("pigpiod n'est pas lancé. Exécuter 'sudo pigpiod'.")

    return arg_pi



def send_impulsion_to_pin(arg_pi, pin_number:int, largeur_d_impulsion:int):
    if largeur_d_impulsion < 500 or largeur_d_impulsion > 2500:
        raise Exception("Valeur hors plage (500 - 2500 µs)")
    else:
        arg_pi.set_servo_pulsewidth(pin_number, largeur_d_impulsion)
        printT(f"INFO: Envoi {largeur_d_impulsion} µs à pin GPIO {pin_number}")



def stop_pin(arg_pi, pin_number:int):
    send_impulsion_to_pin(arg_pi, pin_number, 0)
    # Apparemment on peut aussi envoyer 1500 ? 
    # arg_pi.stop()



def start_pin(arg_pi, pin_number:int, speed:float):

    if speed > 1 or speed < -1:
        raise Exception("Speed doit être dans l'intervalle [-1, 1].")

    largeur_d_impulsion = 1500 + speed*1000

    send_impulsion_to_pin(arg_pi, pin_number, largeur_d_impulsion)



# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

def main():
    notre_parser = ArgumentParser(description='Envoyer une impulsion à un pin GPIO.')
    notre_parser.add_argument(
        '-p', '--pin', type=int, choices=[12, 13, 18, 19], required=True,
        help="Pin GPIO. PWM0: 12, 18. PWM1: 13, 19."
        )
    notre_parser.add_argument(
        '-s', '--speed', type=float, required=True,
        help="Vitesse entre -1 et 1. Mettre 0 arrête le moteur."
        )

    nos_args = notre_parser.parse_args()

    printT("Contrôle du FS90R (pigpio, impulsion en µs)")
    # printT("Tape une largeur d'impulsion (µs), ex : 1500 pour stop, 1000 ou 2000 pour tourner")
        
    notre_pi = init_pi()

    printT("hello")

    if nos_args.speed == 0:
        stop_pin(notre_pi, nos_args.pin)
    else:
        start_pin(notre_pi, nos_args.pin, nos_args.speed)
        time.sleep(2)
        stop_pin(notre_pi, nos_args.pin)

    notre_pi.stop()
    


if __name__ == '__main__' :
    main()
    print("")
