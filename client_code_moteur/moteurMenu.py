import moteur_args.py


def stopMoteurs():
    global pi,gpioM1,gpioM2
    stop_pin(pi,gpioM1)
    stop_pin(pi,gpioM2)

def testSimple():
    start_pin(pi, gpioM1, 0.5)
    start_pin(pi, gpioM2, -0.5)
    time.sleep(3)
    stopMoteurs()
    start_pin(pi, gpioM1, 0.5)
    start_pin(pi, gpioM2, -0.5)
    time.sleep(3)
    stopMoteurs()

def scriptTest():
    print("Script de test à faire")

if __name__ == '__main__' :
    try :
        pi = init_pi()
        gpioM1=12
        gpioM2=13
        while True :
            printT("Heure :")
            print("Rappel que les ports GPIO 12 et 13, soit pins 32 et 33 correspondent aux moteurs. un arrêt forcé par Ctrl-C arrêtera tout de suite les moteurs. Dans la partie code, les moteurs ne sont pas automatiquement arrêtés lors de l'exécution des scripts, il ne faut jamais oublier de les arrêter !!")
            print("\n------------------------------------")
            print("1. COUPER LES MOTEURS !1!1! ")
            print("2. Faire tourner deux moteurs avec paramètres")
            print("3. Faire simplement tourner deux moteurs (pour tester rapidement)")
            print("4. Exécuter un script")
            print("5. Quitter")
            choix=input("Choisir une option (le nombre)")
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

