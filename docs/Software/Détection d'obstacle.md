
#### **Partie : LIDAR Benewake TF02**

Choses à savoir avant de coder :

1. Paramètres du TF02 Lidar 

![500](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd7mTjAX8ShDKk5xiI1zLm3ss8Mc6XKZMcRzQAXuosHmFkNXvJlxPGh2fmNHAde2xbSLJ1OXCKHdGrCirTP0EINbwgXxZKwV5Ki_VIJsyhkP5JtB5jvHIlTKrGmeO-neYK9nKI-?key=L4A1ejDVxs0i06ERmyTYIKsb)

![500](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPe1QqqSArB9Q75_TpSuHvxXzEJYGCO7ANg92jyxVpcSaZC7QZ9Z-iu-pja8fdRHpF8OA_dAZX1msh9YArCGsLkF146lMs-SU4aMvUg_hwMLYMOfiKF3tWp6kAnZsUkIz50-9k1A?key=L4A1ejDVxs0i06ERmyTYIKsb)

2. Format des données envoyées par le TF02 Lidar 

![500](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdZzi0E0bgC3lww5dCx-ZdUOkYb3x_mw9QaS38VHGrMdOAlgC7thA0EwCDCOH0thmtgC5zmI2tP3-PFxuP7eWz8-ERf7X3ey3Bt2f0wCO__z8RmIXqxa_59lHvEPcQ4WZF5W0rJtA?key=L4A1ejDVxs0i06ERmyTYIKsb)

![500](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeXTCCWw-wKp3XOP8jfSiNN0vwWzfJxNQwIhWyUl6zARPtkJPS6jW4j02xfs5VXgW7_bpaoDoKZJWh1M7kbeX44o2moOFwMMPxY8AmXrg_ZOTosfco7AYuD0jIw30nDU5DgcY8L?key=L4A1ejDVxs0i06ERmyTYIKsb)

**Exécution du code: **

1. Dans un terminal : ‘’cd /home/nous/LRSVZZ-2025’’ (où se trouve le programme)
2. Puis : ‘’python3 [lidar.py](http://lidar.py) ‘’

**Résultat pour le LIDAR : **

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfQ4hrJCqoiVzahMlisE9irlOwY4_g7iMuvYHaA6m1HAGT7AqdQD0ZjrmtoGT6cH0tTFXsVj0bjKCBFuCMQLMlMd8hUgwcRSsPr68-UHRORgxSrG73UfS2mCPPTDzMzJ5jnWNKsFg?key=L4A1ejDVxs0i06ERmyTYIKsb)

**Remarques :**

On remarque que la connexion en série a bien été établie et que visuellement, le LIDAR est bien allumé avec la présence de cercles rouges. Mais le LIDAR n’envoie pas de données. 

On a vérifié les branchements et l’alimentation du LIDAR et tout était correct. On se dit peut-être que les câbles du LIDAR étaient peut-être endommagés, c’est pourquoi on ne recevait aucune donnée. 

Ne trouvant pas la réelle source du problème, nous sommes passer à un autre capteur d’obstacles : **Le capteur ultrason HC-SR04**

#### **Partie : Capteur ultrason HC-SR04**

**Ce qu’il faut savoir avant de coder (Fonctionnement) :

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
