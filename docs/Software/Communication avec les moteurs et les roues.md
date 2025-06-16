# Communication avec les moteurs et les roues 
## Où 
Dans le dossier "Test Code Moteur", deux versions de scripts. 

1. [moteurMarche.py](../../Test%20Code%20Moteur/moteurMarche.py) 
2. [moteur.py](../../Test%20Code%20Moteur/moteur.py) 
3. 2025-06-12 : [moteur_args.py](../../Test%20Code%20Moteur/moteur_args.py) 

Le daemon `pigpiod` (Pi GPIO daemon) est nécessaire aux scripts. 
Il est lancé au démarrage avec `systemd`, qu'on contrôle avec la commande `systemctl`. 

Obtenir des informations sur le daemon, s'il est actif et/ou s'il se lance au démarrage. 
```bash
systemctl status pigpiod
```

Pour qu'il s'active au démarrage, utiliser `enable`. 
```bash
sudo systemctl enable pigpiod
```

Dans le cas contraire. 
```bash
sudo systemctl disable pigpiod
```

## Ressources 
https://www.theengineeringprojects.com/2022/04/create-pwm-signal-in-raspberry-pi-4-using-python.html 

Deux types de pins : 
- hardware, de 1 à 40 
- GPIO, 12, 13, 18, 19... 

![Carte des pins](https://images.theengineeringprojects.com/image/webp/2022/04/09.jpg.webp?ssl=1)

![PWM](https://images.theengineeringprojects.com/image/webp/2022/04/8-2.jpg.webp?ssl=1)



