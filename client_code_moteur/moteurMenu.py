import moteur_args as mot
import time

def stopMoteurs():
    global pi,gpioM1,gpioM2
    mot.stop_pin(pi,gpioM1)
    mot.stop_pin(pi,gpioM2)

def testParamètres():
    print("\n--------------------------------------\n")
    ligne = input("\nCe test permet de faire tourner deux moteurs avec des paramètres différents. le format est le suivant : VITESSE1 VITESSE2 TEMPS\nPar exemple pour faire tourner dans des sens opposés pendant 3 secondes : '1 -1 3' \n")
    try:
        parts = ligne.strip().split()
        vitesse1=parts[0]
        vitesse2=parts[1]
        temps=parts[2]
        mot.start_pin(pi, gpioM1, vitesse1)
        mot.start_pin(pi, gpioM2, vitesse2)
        time.sleep(temps)
    except:
        print("\nProblème lors de l'interprétation des paramètres\n")
    finally:
        stopMoteurs()
        print("\nFin du test Paramétré.\n--------------------------------------\n")

def testSimple():
    mot.start_pin(pi, gpioM1, 0.5)
    mot.start_pin(pi, gpioM2, -0.5)
    time.sleep(3)
    mot.stopMoteurs()
    mot.start_pin(pi, gpioM1, 0.5)
    mot.start_pin(pi, gpioM2, -0.5)
    time.sleep(3)
    mot.stopMoteurs()

def scriptTest():
    print("Script de test à faire")

if __name__ == '__main__' :
    try :
        pi = mot.init_pi()
        gpioM1=12
        gpioM2=13
        while True :
            print("--------------------------------------")
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
            elif choix == "2":
                testParamètres()
            elif choix == "3":
                testSimple()
            elif choix == "4":
                scriptTest()
            elif choix == "5":
                print("Fin des tests, arrêt des moteurs.")
                break
    finally :
        stopMoteurs()
        pi.stop()

