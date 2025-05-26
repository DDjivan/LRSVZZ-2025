
#### **Partie : LIDAR Benewake TF02  **

Liens utiles : 
1. [https://www.gotronic.fr/art-capteur-de-distance-lidar-tf02-26489.htm?srsltid=AfmBOopzcvSyq6VFaWZkgjbpm1jLJzc5FJ6IBRXjAak9vlPXAp5Zg52J](https://www.gotronic.fr/art-capteur-de-distance-lidar-tf02-26489.htm?srsltid=AfmBOopzcvSyq6VFaWZkgjbpm1jLJzc5FJ6IBRXjAak9vlPXAp5Zg52J)
2. [https://en.benewake.com/uploadfiles/2024/04/20240426135442695.pdf](https://en.benewake.com/uploadfiles/2024/04/20240426135442695.pdf)

Le LIDAR communique en UART (série)

**Etape 1 : Branchements**

1. Le fil rouge (alimentation) : sur 5V PWR
2. Le fil noir (masse) : sur GND
3. Le fil vert (RX du LIDAR) : sur Uart0 TX
4. Le fil blanc (TX du LIDAR) : sur Uart RX

Avec : 

- **TX** : Sortie de données série (transmission du capteur) => la Raspberry reçoit les données via cette broche 
- **RX** : Entrée de données série (réception du capteur) => le capteur reçoit les commandes de la Raspberry via cette broche

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjludK5bUNmdsMzb1D-rZB5RCBiPaPkreh6m9UZRY9PVQYZwIBE2fC936P49EzH64YmNDpollmqJ8ioqsVdHynerHLjXPgDopMEJF_y8REbklfuP6r6psEjupN1gO_SXYK7E81Nw?key=L4A1ejDVxs0i06ERmyTYIKsb)



**Etape 2 : Configurer la Raspberry Pi pour activer l'interface UART** 
Qui n’est pas activé par défaut

1. Se connecter à la raspberry pi => ssh
2. Dans un terminal : ‘’sudo raspi-config’’
3. Sélectionner ‘’interface options’’
4. Sélectionner ‘’serial port’’
5. Deux questions vont s'afficher : 
	- "Would you like a login shell to be accessible over serial?" Sélectionner ‘’non’’ car on veut pas que ce soit un terminal mais plutôt communiquer directement avec le lidar
	- “Would you like the serial port hardware to be enabled?" Sélectionner ‘’oui’’ car on veut activer les broches UART (8 et 10)
6. Sélectionner ‘’finish’’
7. Redémarrer le raspberry => ‘’oui’’ car les changements sur le port série ne prennent effet qu'après un redémarrage

**Etape 3 : Vérifier que le port série est bien prêt**

1. Dans un terminal : **‘’ls -l /dev/serial*’’** =>  affiche les ports série disponibles 

2. On devrait avoir **‘’lrwxrwxrwx 1 root root 7 May 20 08:46 /dev/serial0 -> ttyS0’’** ce qui veut dire que le port série (/dev/serial0) est bien configuré et lié au port matériel (ttyS0) qui est le port pour communiquer avec le LiDAR
    

**Etape 4 : Installation de la bibliothèque pyserial**
Pour que la raspberry puisse lire les données du Lidar via un programme python (permet la communication en série)

1. Dans un terminal : ‘’sudo apt update’’ => pour mettre à jour la liste des logiciels disponibles pour s'assurer que vous installez les dernières versions.
2. Puis : ‘’sudo apt install python3-pip’’ => outil qui permet d'installer des bibliothèques Python (comme pyserial)
3. Et enfin : ‘’sudo apt install python3-serial’’ 

**Etape 5 : Code**
[Détection d'obstacle](../Software/Détection%20d'obstacle.md)
#### **Partie : Capteur ultrason HC-SR04**

Liens utiles : 

1. [HC-SR04 datasheet(1/6 Pages) ETC2 | Ultrasonic Sensor](https://www.alldatasheet.com/html-pdf/1132203/ETC2/HC-SR04/111/1/HC-SR04.html)
2. [Projet Robotique](https://perso.esiee.fr/~hamouchr/el3007/projet/)
3. [python - What is the difference between BOARD and BCM for GPIO pin numbering? - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering) 
4. [https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf) 

**Branchements**

Ce qu’il faut savoir avant de brancher : 

La tension de sortie délivrée par la broche Echo du capteur HC-SR04 est de 5V. Or, la broche d'entrée du Rapsberry est conçue pour du 3,3 V au maximum.                                           Pour ne pas endommager le Rapsberry et le capteur, nous allons utiliser un pont diviseur de tension.

**Calcul :

**![350](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcMU3ny-RcU9NyL1Ngysl-JuBCv84tUy7yTFGYTxSv4rGdCQVovKHvOCmUa3HpmRb75GfGwQNWRG7y6VFs6t2RRwUmvnf1p6jp_hWLEa5a0epFPBKWGNQs28ZV76HC4gMOS4Rl1rw?key=L4A1ejDVxs0i06ERmyTYIKsb)

**Documentation des résistances :**

**![350](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3OIUr0H9yc-UEC6lfpTSiYttx2aIzeLkL1YWh0vF0nzTUc5TAYrC88HF26njDxGtrBfDBFBOemoIUN8EpHcuZ8mTbAx2XfPuyGBaaVbDI09Gi7Dwn9yiQCwWPHBj-KdElPutHmg?key=L4A1ejDVxs0i06ERmyTYIKsb)**

**Nous on a pris : R1 = 2.2kohm et R2 = 3.3kohm afin que ça marche**

**Branchements :**

On doit effectuer les branchements comme suit :

**![250](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfaSZK_wg8N0NHsu96GYKI_qj8nKdokvHZl30rlL5vrdslDcrD2wxLmVoaAi0mTlnoCN-Y1WGx-vyb3MFZlyrjCAhcW5x6eUPkS7g3z9eJz2ULHbMgxcB2aji4QXjod0_hQ6DE7fQ?key=L4A1ejDVxs0i06ERmyTYIKsb)**
**![400](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfjludK5bUNmdsMzb1D-rZB5RCBiPaPkreh6m9UZRY9PVQYZwIBE2fC936P49EzH64YmNDpollmqJ8ioqsVdHynerHLjXPgDopMEJF_y8REbklfuP6r6psEjupN1gO_SXYK7E81Nw?key=L4A1ejDVxs0i06ERmyTYIKsb)**

**Ce que ça donne en réalité :**

**![250](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfWI58MC2rBn86QThJJgOYIkpaLiu-THRWruhmThmPrnS_gwT6b8d5QOA3ZTx-f65VJm_EVTdPZCdVd0G7i5WfREv0ERb3rfKaWw3wet59rfeVLEQSMO1kaNJk31Y5OfDisi1TewA?key=L4A1ejDVxs0i06ERmyTYIKsb)**

**(Tuto des branchements : [Raspberry Pi, télémètre à ultrasons](https://raspberry-pi.developpez.com/cours-tutoriels/capteur/mag-pi-utiliser-port-gpio/partie-3-telemetre-ultrason/#:~:text=Afin%20d%27%C3%A9viter%20d%27endommager%20le%20Rapsberry%20Pi%2C%20nous%20allons,atteindre%20une%20tension%20supportable%20par%20le%20Rapsberry%20Pi.))**
