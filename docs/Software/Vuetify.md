# Vuetify 
## En bref 
Vuetify est un framework de composants pour [Vue.js](VueJS.md). Il fournit des composants d'interface utilisateur préfabriqués qui aident les développeurs à créer rapidement des applications web réactives et esthétiques. 

## Comment installer 
https://vuetifyjs.com/en/getting-started/installation/ 

Installer : 
```bash
npm create vuetify@latest
```

Choix : Barebones. 

Lancer le serveur de développement. 
```bash
npm run dev
```

Il y a besoin de `router` pour la gestion des routes. 
```bash
npm install vue-router
```

Créer le répertoire et fichier nécessaire (à confirmer). 
```
mkdir src/router
touch src/router/index.js
```

### Ce qui est à retenir pour lancer les deux process 
Back-end 
```bash
cd backend
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
```

Front-end 
```bash
cd frontend
```
```bash
npm run dev
```

## Quoi 
#benjamin 
~~5~~ 4 fichiers à décortiquer : 
- `app.py` 
- `main.js` 
- `App.vue`
- `Home.vue`
- ~~`index.js`~~ 
	- Inutile, il peut être supprimé. 
	- Il est censé permettre d'importer les plugins tels que Vuetify, mais le fichier `main.js` importe directement Vuetify depuis `vuetify.js` (ligne 3) 

### Interprétation des fichiers
Pour rappel, on a du côté front-end :

![600](attachments/Pasted%20image%2020250522135423.png)

![400](attachments/Pasted%20image%2020250522135452.png)

![200](attachments/Pasted%20image%2020250522135534.png) ![200](attachments/Pasted%20image%2020250522135555.png)

Et en back-end :
![400](attachments/Pasted%20image%2020250522135654.png)

#### `App.py` 
On fait tourner deux parties séparées. 
La première est le back-end avec Flask, à l'adresse 127.0.0.1:5000 par défaut. 

Dans `app.py`, il est nécessaire d'activer le CORS ([[../Guides/CORS]]) avec `CORS(app)`, puisque l'on a une partie front-end à une adresse différente de la partie back-end. 

L'adresse du front-end étant http://192.168.218.54:3000/, ça permet de gérer les requêtes entre le front-end et le back-end sur des origines différentes. 

==On peut pas avoir la même adresse ? Je pense qu'il y a quelque chose à comprendre.== 

#### `App.vue` 
Ce fichier permet avec "router-view", qui est une balise définie dans "vue-router", de voir l'ensembles des objets au bout des routes définies par le "main". 

Ici, elle va afficher l'objet de l'unique route définie par le main, qui est un chemin vers le composant Home.vue (défini dans le fichier `main.js`) qui sera affiché. 

Mis à part, `App.vue` définit simplement l'affichage du titre "Welcome to My Vuetify App" qui, sans route définie, serait le seul texte affiché sur la page. 

#### `Home.vue` 
La majorité du travail est faite dans ce fichier, dans la partie "script". 

- Le bloc data permet de définir les variables, comme "message" qui est utilisée dans la partie template (qui définit l'endroit où est utilisé "message"). 

- Le bloc methods définit les méthodes, il n'y en a qu'une seule utilisée dans ce fichier, "fetchData" qui est définie comme [Asynchrone](../Guides/Asynchrone.md).
	- fetchData va chercher à l'adresse du back-end, connue à l'avance car définie par Flask, la réponse attendue sous format json. Cette réponse a à priori un champs message, qui contient le message qui nous intéresse.

#### `Main.js` 
C'est le fichier principal qui va exécuter le code [[JavaScript]] pour lier les différentes parties du front-end. 

Mis à part les instructions qui permettent d'indiquer à l'application quels plugins utiliser (comme Vuetify et router), elle définit en premier lieu les routes, c'est à dire les chemins vers les différents composants qui forment la page. 

Le seul composant ici est le `Home.vue`.