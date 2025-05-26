Ce qu’il faut savoir avant de coder (Fonctionnement) :

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdWKAF0_Z_z2ZH-Mjg7hY2wYm4a6SKmiOUpVr8dgvirfd1wOZUUMN1go3EljpSItUqd-n7mijCY9lTmyJlZrgYzutjdizPIR0XGi06j0p4nMo48rDGqPXCifn6p8FNvgvALKXBs?key=L4A1ejDVxs0i06ERmyTYIKsb)**

1. On commence par mettre le signal de la broche TRIGGER du capteur à l’état LOW
2. On envoie une impulsion HIGH de 10us sur la broche TRIGGER du capteur
3. On remet ce signal à l’état LOW
4. Maintenant que nous avons envoyé notre impulsion, nous devons écouter le signal sur la broche ECHO. Elle reste à l’état HIGH pendant tout le temps que prend le signal pour aller et venir entre le capteur et l'obstacle détecté. Cette durée * vitesse du son (0.034cm/us) correspond à la distance aller-retour parcourue par le signal 
5. While Echo=0 alors : fin de l'émission des ultrasons par le capteur => duree_debut
6. While Echo=1 alors : détection du retour des ultrasons => duree_fin
Donc la durée à laquelle le signal sur la broche ECHO reste à l’état HIGH :                        duree_impulsion = duree_fin - duree_debut

Et donc distance = duree_impulsion * 34000/2

**Code :**
**![500](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAQ8rwULszM1ewxYtOQw9wwyUNbNz8526FczdXoSRDxwegLOCjmE4LaGzvabV5DZ4QfBH-4ABWzw1QuBaALZzbbA-hlJA2f53UYk0K6JeI6KDwvtn9EqKAUH-xhaR9sgfUZToavw?key=L4A1ejDVxs0i06ERmyTYIKsb)**

**Résultats :**
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcvhsXGoHVtVpuj_TpvGdl8ZTPrymNlwWVMOWz8vVW-Kvn-cz6RMMKny3lYMfnScc0p743RvGGB9gf_PicHTRoaBXrdgWiOPhVfrhu9OqoS_adid0X9wWB8QdzQrkNZyYX8LX7_1g?key=L4A1ejDVxs0i06ERmyTYIKsb)**
