# Software 
Cette note englobe tout ce qui est logiciel, technique, fonctionnel. 
À la fois ce qu'il sera sur le serveur, et sur la carte d'un robot. 

> [!warning] Attention
> Bien que le modèle 3D utilise des logiciels (voire du code), il ne fait pas partie de cette section, mais de celle de [[Design]]. 

## Quoi 
Un logiciel divisé en plusieurs programmes, qui fonctionneraient idéalement par [Couplage faible](docs/Guides/Couplage%20faible.md). 

Voici des idées de programmes. 

Pour le serveur : 
- Récepteur d'informations 
- Gestion des programmes 
- Interface web 

Pour le client : 
- Envoyeur d'informations, dont l'adresse IP 
- Communication avec les moteurs et les roues 
- Synthèse vocale 

## Comment 
Pour le moment, il a été décidé que [[Python]] soit l'unique langage de programmation à utiliser, dû à sa simplicité et familiarité. 

Toutefois, la section [[Hardware]] indique qu'on utilise des [Raspberry Pi](docs/Guides/Raspberry%20Pi.md). [VARTANIAN Djivan](VARTANIAN%20Djivan) : Je suppose qu'écrire en C ou en C++ serait mieux, mais c'est à voir plus tard. 

Il faudrait comprendre comment un ordinateur fonctionne : [[Process]], [[Thread]], automatismes ([[cron]]), ce qu'il se passe à la mise en veille/redémarrage... 

## Où 
Tous les fichiers de développement sont pour le moment à la racine du repo. 
==Il faudrait peut-être faire des branches.== 

