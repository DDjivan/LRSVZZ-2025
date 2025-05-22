**Impressions 3D 



19 mai 

### 1. Design du coffre :

Avoir les dimensions et poids de : 

- une canette
- une bouteille d’eau
- un sandwich
- autres



Contrainte : 

- Que la charge de la nourriture ne dépasse pas 3.5 kg (sinon le robot risque d’avoir des difficultés pour avancer)  



|                                                                                                                                                                                                                                        | Dimensions (cm)                                                      | Poids (kg) |     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------- | --- |
| Sandwich<br><br>[Baguette - Wikipedia](https://en.wikipedia.org/wiki/Baguette?utm_source=chatgpt.com)<br><br>[CALORIES sandwich jambon-beurre](https://www.infocalories.fr/calories/calories-jambon-beurre.php?utm_source=chatgpt.com) | 35 (longueur)                 <br><br>6 (largeur)<br><br>4 (hauteur) | 0.27       |     |
| Canette (33cl)<br><br>[fiche technique 33cl canette](http://mgeffard.free.fr/REF/CFPO/HTML/UK/DevenirPartenaire/Importater/doc/fiche%20techniq%2033cl%20canette.pdf)                                                                   | 11.6 (hauteur)<br><br>6.6  (largeur)                                 | 0.37       |     |
| Bouteille (50cl)                                                                                                                                                                                                                       | 19 (hauteur) <br><br>7.5 (largeur)                                   | 0.55       |     |
| Reste                                                                                                                                                                                                                                  |                                                                      |            |     |

  
  
###### Dimensions du coffre : 

- Hauteur : 25 cm
- Longueur : 40 cm
- Largeur : 45 cm 



###### Combien de sandwichs : 

4 sandwichs                                       => 1.08 kg

  

Combien de canettes/bouteille : 

2 canettes / 2 bouteilles                  => 0.74 + 1.1 = 1.84 kg

  

Pour sandwichs + canettes + bouteilles :  2.92 kg

Donc pour la partie reste : 0.58 kg ( => max : 3.5kg)

  
  
  

Prototype de design

![Image (0)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(0).png)

  

##### Site de modèle 3D : 

[https://www.yeggi.com/q/robot+chassis/](https://www.yeggi.com/q/robot+chassis/)

[https://www.thingiverse.com/](https://www.thingiverse.com/) 

[https://www.printables.com/](https://www.printables.com/)

[https://cults3d.com/](https://cults3d.com/)

  

2. Design du châssis : 

Contrôler un robot à deux roues avec Raspberry Pi : 

[https://alcalyn.github.io/control-robot-two-engines/#:~:text=avec%20un%20radiateur-,Contr%C3%B4lez%20un%20deuxi%C3%A8me%20moteur,%2C%204A%20et%203%2C4EN%20](https://alcalyn.github.io/control-robot-two-engines/#:~:text=avec%20un%20radiateur-,Contr%C3%B4lez%20un%20deuxi%C3%A8me%20moteur,%2C%204A%20et%203%2C4EN%20). 

  
  

[https://www.thingiverse.com/thing:2151514](https://www.thingiverse.com/thing:2151514) 

![image](https://cdn.thingiverse.com/renders/36/fe/5e/5d/97/d2b5ca33bd970f64a6301fa75ae2eb22_display_large.jpg)

  

[https://www.thingiverse.com/thing:2945466](https://www.thingiverse.com/thing:2945466) 

![image](https://cdn.thingiverse.com/renders/06/7c/d9/87/08/8af37ecc3e74440de72d8741d51e9f7d_display_large.jpg)

  

[https://www.thingiverse.com/thing:4565409](https://www.thingiverse.com/thing:4565409) 

  
  

![image](https://cdn.thingiverse.com/assets/08/60/60/04/d6/large_display_Robot_Fusion3D_01_1000px.png)








--------------------------------------------------------------------------

## **Tuto FreeCAD**

### **1.Démarrage**


Pour commencer l'interface de FreeCAD ressemble a ceci, quand on ouvre le logiciel : 
![Image (1)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(1).png)


Pour faire une modélisation 3D, on ouvre un nouveau fichier vide. 

Il faut cliquer sur créer un corps puis créer une esquisse :
![Image (2)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(2).png)
![Image (3)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(3).png)


Ici on doit cliquer sur le plan XY pour créer un objet sur une surface horizontale.
![Image (4)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(4).png)


Maintenant on a accès à tout un panel d'outils : 
![Image (5)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(5).png)



### **2.Pour faire cube**


On clique sur cette outil pour créer un rectangle : 
![Image (6)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(6).png)


On aura quelque chose qui ressemble a ceci, dont on pourra changer la taille et pour passer au côté suivant il faut cliquer sur "tab" du clavier et enfin "entrée" du clavier pour que le rectangle soit définitif : 
![Image (7)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(7).png)


Ensuite on clique sur "Echap" pour ne plus avoir l'outil sur la souris.
On obtient ceci : 
![Image (8)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(8).png)


Evidemment pour rechanger les dimensions on peut double-cliquer sur les mesures et on obtient une fenêtre pop up comme ceci et cliquer sur "Entrée" pour valider : 
![Image(20)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image(20).png)


On peut cliquer deux fois sur le rectangle pour le déplacer (il faut qu'il soit allumer en vert).
![Image (9)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(9).png)


Enfin on peut fermer cette tâche pour maintenant le mettre en  3D : 
![Image (10)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(10).png)


Ensuite on voit que le rectangle/carré est vert.
⚠️ Il ne faut surtout pas cliquer autre part sinon l'outil ne détecte pas la forme pour le sortir en 3D.

Il faut cliquer sur "Protrusion" pour le sortir en 3D : 
![Image (11)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(11).png)


Maintenant dans la fenêtre tâche, on a ceci : 
![Image (12)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(12).png)
La case "Longueur" sert à choisir la hauteur du cube, une fois choisi la hauteur, il faut cliquer sur "Entrée" du clavier. 


On coche origine pour cacher les axes : 
![Image (13)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(13).png)


Voila le résultat final : 
![Image (14)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(14).png)
Un magnifique cube ✨


### **3.Navigation**


Pour se déplacer, on maintient la molette de la souris.
![Video (1)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Video%20(1).mp4)


Pour changer de perspective, on maintient la molette de la souris et le clique droit.
![Video (2)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Video%20(2).mp4)



### **4.Faire une boîte**



On clique une surface du cube : 
![Image (15)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(15).png)


Puis on clique sur "Evidement" : 
![Image (16)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(16).png)


Le choix de l'épaisseur des côtés est déterminé par la case "Epaisseur" : 
![Image (17)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(17).png)

Une fois le choix fait, on clique sur "Entrée" du clavier.


Voilà le résultat : 
![Image (18)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(18).png)


Evidement pour rechanger l'épaisseur, on double-clique ici et la fenêtre des tâches se réaffiche.
![Image (19)](Screenshots%20-%20Notes%20FreeCAD%20Alice/Image%20(19).png)



