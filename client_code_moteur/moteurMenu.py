import moteur_args as mot
import time
from testFeed import *

def stopMoteurs():
    global pi,gpioM1,gpioM2
    mot.stop_pin(pi,gpioM1)
    mot.stop_pin(pi,gpioM2)

def testParamètres():
    ligne = input(
        "Ce test permet de faire tourner deux moteurs avec des paramètres différents.\n"
        "Format : VITESSE1 VITESSE2 TEMPS\n"
        "Exemple : '1 -1 3' → moteurs en sens opposés pendant 3 secondes\n> "
    )
    try:
        parts = ligne.strip().split()
        if len(parts) != 3:
            raise ValueError("Trois paramètres sont requis.")

        vitesse1 = float(parts[0])
        vitesse2 = float(parts[1])
        temps = float(parts[2])
        assert temps>0
        mot.start_pin(pi, gpioM1, vitesse1)
        mot.start_pin(pi, gpioM2, vitesse2)
        time.sleep(temps)

    except Exception as e:
        print(f"\nProblème lors de l'interprétation des paramètres : {e}\n")

    finally:
        stopMoteurs()
        print("\nFin du test Paramétré.\n--------------------------------------\n")

def testSimple():
    print("Les moteurs tournent dans un sens.")
    mot.start_pin(pi, gpioM1, 0.5)
    mot.start_pin(pi, gpioM2, 0.5)
    time.sleep(3)
    stopMoteurs()
    print("Puis dans l'autre.")
    time.sleep(3)
    mot.start_pin(pi, gpioM1, -0.5)
    mot.start_pin(pi, gpioM2, -0.5)
    time.sleep(3)
    stopMoteurs()
    print("Fin.")

def checkInterval(x,m,M,m1,M1) :
    return (m<x[0]) & (x[0]<M) & (m1<x[1]) & (x[1]<M1)

def scriptTest():
    a=getAngles()
    aFinal=( (a[0]+273)%273 , (a[1]+273)%273 )
    mot.start_pin(pi, gpioM1, 0.5)
    mot.start_pin(pi, gpioM2, 0.5)
    print("val finale",aFinal)
    while (not checkInterval(getAngles(),aFinal[0]-5,aFinal[0]+5,aFinal[1]-5,aFinal[1]+5)) :
            print("angle",getAngles())
            time.sleep(0.01)
    stopMoteurs()

if __name__ == '__main__' :
    # --- Initialisation SPI ---
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Bus SPI 0, périphérique CS0
    spi.max_speed_hz = 1000000  # Fréquence adaptée au MCP3204
    try :
        pi = mot.init_pi()
        gpioM1=12
        gpioM2=13
        while True :
            print("\n--------------------------------------")
            mot.printT("\n")
            print("Rappel que les ports GPIO 12 et 13, soit pins 32 et 33 correspondent aux moteurs. un arrêt forcé par Ctrl-C arrêtera tout de suite les moteurs. Dans la partie code, les moteurs ne sont pas automatiquement arrêtés lors de l'exécution des scripts, il ne faut jamais oublier de les arrêter !!")
            print("\n------------------------------------")
            print("1. COUPER LES MOTEURS !1!1! ")
            print("2. Faire tourner deux moteurs avec paramètres")
            print("3. Faire simplement tourner deux moteurs (pour tester rapidement)")
            print("4. Exécuter un script")
            print("5. Quitter")
            print("--------------------------------------\n")
            choix=input("Choisir une option (le nombre): ")
            print("\n--------------------------------------\n")
            if choix == "1":
                stopMoteurs()
                print("MOTEURS COUPES !1!1")
            elif choix == "2":
                testParamètres()
            elif choix == "3":
                testSimple()
            elif choix == "4":
                scriptTest()
            elif choix == "5":
                break
    finally :
        print("\n--------------------------------------\n")
        print("Fin des tests, arrêt des moteurs.")
        print("\n--------------------------------------\n")
        stopMoteurs()
        pi.stop()

