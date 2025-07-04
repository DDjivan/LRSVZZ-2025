# Software 
Cette note englobe tout ce qui est logiciel, technique, fonctionnel. 
À la fois ce qu'il sera sur le serveur, et sur la carte d'un robot. 

> [!warning] Attention
> Bien que le modèle 3D utilise des logiciels (voire du code), il ne fait pas partie de cette section, mais de celle de [Design](Design.md). 

## Quoi 
Un logiciel divisé en plusieurs programmes, qui fonctionneraient idéalement par [Couplage faible](docs/Guides/Couplage%20faible.md). 

Voici des idées de programmes. 

**Pour le serveur et le client :** 

- [Récupérer l'adresse IP locale](Software/Récupérer%20l'adresse%20IP%20locale.md) 
- [Chemin de communication](Software/Chemin%20de%20communication.md) 

Pour le serveur : 

- Gestion des programmes 
- Interface web 
	- [Back-end](Software/Back-end.md) (Framework Web) 
	- [Database](Software/Database.md) (Base de données) 
	- [Front-end](Software/Front-end.md) (Apparence) 
	- Communication avec les [Raspberry Pi](Guides/Raspberry%20Pi.md) 
	- Bibliothèque SSH 

Pour le client : 

- Pouvoir envoyer des commandes et accéder aux fichiers 
	- [Réseau de l'école](Software/Réseau%20de%20l'école.md) 
	- [SSH et SFTP](Software/SSH%20et%20SFTP.md) 
- Envoyeur d'informations, dont l'adresse IP 
	- [Récupérer l'adresse IP locale](Software/Récupérer%20l'adresse%20IP%20locale.md) 
	- [Communication avec les moteurs et les roues](Software/Communication%20avec%20les%20moteurs%20et%20les%20roues.md) 
	- [Feedback](Software/Feedback.md) 
- Synthèse vocale 

## Comment 
Pour le moment, il a été décidé que [Python](Guides/Python.md) soit l'unique langage de programmation à utiliser, dû à sa simplicité et familiarité. 

Toutefois, la section [Hardware](Hardware.md) indique qu'on utilise des [Raspberry Pi](Guides/Raspberry%20Pi.md). [Djivan](People/VARTANIAN%20Djivan.md) : Je suppose qu'écrire en C (ou en C++) serait mieux, mais c'est ~~à voir plus~~ trop tard. 

Il faudrait comprendre comment un ordinateur fonctionne : [Process](Guides/Process.md), [Thread](Guides/Thread.md), automatismes ([Script au démarrage](Software/Script%20au%20démarrage.md)), ce qu'il se passe à la mise en veille/redémarrage... 

## Où 
Tous les fichiers de développement sont pour le moment à la racine du repo. 

