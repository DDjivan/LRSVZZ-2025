https://vuetifyjs.com/en/getting-started/installation/ 

```bash
npm create vuetify@latest
```

Barebones is ok. 

Lancer : 
```bash
npm run dev
```

ROUTER ! 
```bash
npm install vue-router
```

```
mkdir src/router
touch src/router/index.js
```


### donc 
Backend 
```
cd backend
```

```
pip install -r requirements.txt
```

```
python app.py
```

Frontend 
```bash
npm run dev
```

~~5~~ 4 fichiers à décortiquer : 
app.py 
main.js 
App.vue
Home.vue
~~index.js~~ <-Inutile, on peut le supprimer. Il est censé permettre d'importer les plugins tels que Vuetify, mais le fichier "main.js" importe directement vuetify depuis "vuetify.js" (ligne 3)

### Interprétation des fichiers
Pour rappel, on a du côté frontend :

![](attachments/Pasted%20image%2020250522135423.png)![](attachments/Pasted%20image%2020250522135452.png)![](attachments/Pasted%20image%2020250522135534.png)![](attachments/Pasted%20image%2020250522135555.png)
Et en backend :
![](attachments/Pasted%20image%2020250522135654.png)

#### App.py 
On fait tourner deux parties séparées : Le backend avec Flask, à l'adresse 127.0.0.1:5000.
->127.0.0.1 est l'adresse locale
->5000 est le port par défaut attribué lorsque l'on exécute "app.run" dans le fichier app.py.

Dans le fichier app.py il est nécessaire d'activer le [[CORS]] ("CORS(app)") puisque l'on a une partie frontend à une adresse différente de la partie backend. (l'adresse du frontend est http://192.168.218.54:3000/)

#### App.vue
Ce fichier permet avec "router-view", qui est une balise définie dans "vue-router", de voir l'ensembles des objets au bout des routes définies par le "main". Ici, elle va afficher l'objet de l'unique route définie par le main, qui est un chemin vers le composant Home.vue qui sera affiché. Mis à part, App.vue définit simplement l'affichage du titre "Welcome to My Vuetify App" qui, sans routes définies, serait le seul texte affiché sur la page.
#### Home.vue
La majorité du travail est faite dans ce fichier, dans la partie "script". 
- Le bloc data permet de définir les variables, comme "message" qui est utilisée dans la partie template (qui définit l'endroit où est utilisé "message"). 
- Le bloc methods définit les méthodes, il n'y en a qu'une seule utilisée dans ce fichier, "fetchData" qui est définie comme [[Asynchrone]].
	->fetchData va chercher à l'adresse du backend, connue à l'avance car définie par Flask, la réponse attendue sous format json. Cette réponse a à priori un champs message, qui contient le message qui nous intéresse.

#### Main.js 
C'est le fichier principal qui va exécuter le code JS pour lier les différentes parties du frontend. Mis à part les instructions qui permettent d'indiquer à l'application quels plugins utiliser (comme Vuetify et router), elle définit en premier lieu les routes, c'est à dire les chemins vers les différents composants qui forment la page. Le seul composant ici est le Home.vue.