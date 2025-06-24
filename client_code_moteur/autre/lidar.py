import serial
import time


port = "/dev/serial0"
baudrate = 115200
bytesize = 8
parity = 'N'
stopbits = 1


try:
    #print("Verification de la connexion du TF02 LIDAR")
    serie = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=1)
    print("Connexion du TF02 LIDAR en serie reussie")
except serial.SerialException as erreur:
    print("Erreur de connexion:", str(erreur))
    exit()

def lire_data_lidar():
    while True:
        print("Lecture des mesures du TF02 LIDAR:")
        if serie.in_waiting >= 9:  
            print("La trame est complete")
            data = serie.read(9)
            print(f"Lecture de {len(data)} octets")
            if len(data) == 9 and data[0] == 0x59 and data[1] == 0x59:
                print("Entete valide")
                distance_cm = data[2] + data[3] * 256
                checksum = sum(data[:8]) & 0xFF
                print("Calcul du checksum")
                if checksum == data[8]:
                    return {"distance_cm": distance_cm}
                else:
                    print("Erreur checksum")
            else:
                print("Entete invalide ou trame incomplete")
        else:
            print(f"Pas assez de donnees, seulement {serie.in_waiting} octets disponibles")
        time.sleep(0.01)

try:
    print("Demarrage du programme:")
    while True:
        mesure = lire_data_lidar()
        if mesure is not None:
            print(f"Distance de l'obstacle: {mesure['distance_cm']} cm")
        else:
            print("Pas de mesures valides")
        time.sleep(0.1)
        
except KeyboardInterrupt:
    serie.close()
    print("Arret propre du programme")

except Exception as error:
    serie.close()
    print(f"Arret du programme, erreur detectee:", str(error))
    
    

