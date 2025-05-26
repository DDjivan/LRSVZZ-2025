
#### OBJECTIF : Pouvoir se connecter depuis son PC à la Raspberry Pi

Lien utile : 
[https://www.raspberrypi.com/documentation/computers/getting-started.html](https://www.raspberrypi.com/documentation/computers/getting-started.html)

##### 1. Préparer la carte micro SD avec Raspberry Pi Imager via Eduroam directement

- Insérer la carte micro SD dans son PC.
- Ouvrir Raspberry Pi Imager.
- Sélectionner "Choose OS" → sélectionner “Raspberry Pi OS (32-bit)” (sans interface)
- Sélectionner “Choose Storage” → sélectionner la carte microSD
- Valider et modifier les paramètres comme suit : 
	- Hostname : raspberrypi1.local (par défaut)
	- Enable SSH : cocher cette case → choisir ''Use password authentication''    
	- Set username : pi
	- Set password : 12345678  
	- Configure wireless LAN : cocher cette case 
		- SSID : **eduroam**    
		- Password : azerty 
		- Wireless LAN country : FR  
- Cliquer sur “Save”.    
- Cliquer sur “Write” pour flasher la carte SD avec toutes ces options.

#####  2. Insérer la carte micro SD et démarrer le Raspberry Pi

- Une fois l’étape 1 terminée, éjecter la carte micro SD du PC.  
- L'insérer dans la Raspberry Pi.  
- Brancher l’alimentation de la Raspberry Pi (vérification via clignotement de la LED verte).
- La Raspberry PI va démarrer et se connecter au Wi-Fi automatiquement.

##### 3. Trouver l’adresse IP de la Raspberry Pi (ou utiliser son nom)

###### OPTION 1 : Par nom d’hôte

Ouvrir un terminal et taper : ssh pi@raspberrypi1.local
Cela demande un mot de passe (celui qu'on a configuré dans l'étape1 : azerty)

**Conclusion :** Cette démarche n'a pas fonctionné et nous n'avons pas compris pourquoi donc on est passé à l'option 2.

###### OPTION 2 : Par adresse IP directe

1. Télécharger Advanced IP Scanner.
2. Chercher l’appareil nommé “raspberrypi1” ou alors une nouvelle adresse IP qui s'est connectée au réseau. 
3. Noter son adresse IP
4. S'y connecter via SSH : dans un terminal, écrire la commande ''ssh pi@IP''.


**Conclusion :** Pour cette démarche, on est également bloqués. 
Soit la commande ssh fonctionne mais on arrive pas à s'authentifier. 
Soit on ne parviens pas à trouver l’adresse IP car sur Eduroam il y a beaucoup trop d'appareils connectés et donc d'adresses IP.

**Solution :** Ne comprenant pas pourquoi nous n'arrivons pas à nous authentifier, on a décidé de refaire la préparation de la carte micro SD via un autre réseau qu'Eduroam qui est restreint => **un partage de connexion**. 





- Ensuite, je me suis connecté via le partage de connexion d’Alice, pour pouvoir retrouver plus facilement l’adresse IP et vérifier le mot de passe configuré, car il me renvoyait une erreur d’identifiants incohérents.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPfgtBOOIktYMzJydTlXOU8csNWGG_PfbLUEZ8qlom9ov1KJa9S0Rou8aGUzNYjfaNwncnQ0iu8UoemeFWiKWNjuoOe047v3yNvkzE7gJC2yuUjyMIXAmRfUwbXB-4IU3Arifj?key=L4A1ejDVxs0i06ERmyTYIKsb)

- J’ai refait la manipulation chez moi, en utilisant le partage de connexion, et j’ai également revérifié le mot de passe — mais cela ne fonctionne toujours pas. L’erreur affichée indique que la clé d'identité du Raspberry Pi a changé, ce qui fait que SSH refuse la connexion par sécurité. Cela s'explique par le fait que j’ai réinstallé le système sur la carte SD afin de reprendre toute la configuration depuis le début.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfphikRzrWEuadfuQTkOKx5ZX0EaVnrrujNKX91co1T99-6V89G7AThjO5b4yTQehYHZsL8wozqS0pHmF2Q58VarPWXRkHWP-jmg8AXFIyNoRfUB0QD4rR4SciYR_Vajwx2y5yi3w?key=L4A1ejDVxs0i06ERmyTYIKsb)

- Pour supprimer l’ancienne clé SSH stockée sur mon PC, j’ai exécuté la commande suivante ssh-keygen -R raspberrypi.local

Ensuite, j’ai réessayé de me connecter, mais le problème de mot de passe persiste. Je n’ai donc pas pu avancer davantage pour aujourd’hui. Je prévois de reprendre demain, soit en essayant à nouveau avec l’adresse IP, soit en testant une connexion directe via un câble Ethernet. À réfléchir. et puis continuer ensuite à travailler sur le code et lire les cours de Louise en robotique. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXecNd8GJ_h8p0Dzkm4DbkhfemL3TviTC-v6Jfd57n9T1PZr8Z17xhDUS7oWKa_EJdFes2lesz3tuW2QG1jqTIabomds54EkzJxE6pN7wravcH0vE2LkgWIwYTSwSZcup72M4B4s?key=L4A1ejDVxs0i06ERmyTYIKsb)


13/05

J’ai remofié la configuration lors de l’installation et le nom de projet j’ai mis pi, c’est bon, ça marche. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVmLzD7vHWS0IGCOPorABu0mc-YF9f3nI54I9Lbjhbzpy8EnYnDM-eclQAAYR2Ff_N_x_VzgzyTa9gPzJrisWJYh8jDoXBPo1N6grnIjxQIWD27NVgzq7AmZb9XBF3vOHxn5nLXw?key=L4A1ejDVxs0i06ERmyTYIKsb)

Je passe maintenant au prochaine étape afin de préparer la raspberry pour la programmation : 

1- Faire les mises à jour du système

Les commandes à utiliser sur l'invite pi@raspberrypi:~ $ : 

- **sudo apt update** : Cette commande vérifie ce qui peut être mis à jour.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdkSAZ6vNry50W4luEXtt0CV4BHVlMXI1hUOMLzXcyZYxcuNvxTBNB8uKbojHDb4tfbJ6qHqbN5A9kgLTWRPwVoGvQLThD1zLV6VLq7qndzPY5vgQxvpHWaEDyaHdLP5CE9fuUqpQ?key=L4A1ejDVxs0i06ERmyTYIKsb)

- **sudo apt full-upgrade -y** : Celle-ci installe toutes les mises à jour disponibles.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8z3M-kyatV35-DjZvuJqN0pF8HTOgQ-PbYvkG_ORaRzlmkFGnFIAzcOWo0S_32mTU9Pnck_LJdr2pQ00Fvo8oo3boQSEEmVJpHqNBNfQzn4EcwWNSy_4EXteIMuQsyjT2HVhG0A?key=L4A1ejDVxs0i06ERmyTYIKsb)

…..

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfVNwNWDZu5Gf-Ni0ltGOx7j9NZBdsnDx7vOdnQRV-hiJLzVIsVpL7tUeocFy-I89hOtsj-r3ZHdpni4pSPoDIdH4dH5ieLjbAY8R9eGY2rHJri2iVXT51BsbplNCvV8o-9tY9apw?key=L4A1ejDVxs0i06ERmyTYIKsb)

-sudo reboot : Redémarre le Raspberry Pi pour appliquer les changements.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeE5L8p06JrRXliZn42gGdNxbQnkr_sAgz5fazqFnbHNzAz82jex5xZx2b442_owmiir8krnTppDJpbuSDLjw0VNpXXu09iCdaj7B4BBDEbWJvcpcDCK_52ydhKeGpaKgTRRZAYIQ?key=L4A1ejDVxs0i06ERmyTYIKsb)

Je me connecte à nouveau sur la raspberry 

J’ai installé MobaXterm. 

Je lis maintenant le rapport de Louise.**



Là c'est avec connexion d'Alice mais Djivan a reussi à écrire un script avec Eduroam directement donc pas besoin 