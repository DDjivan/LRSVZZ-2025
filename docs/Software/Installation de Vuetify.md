(Benjamin)
Fait sur Kubuntu, pour la simplicité par rapport à Windows où il y avait des problèmes d'installation.

[Vidéo d'initiation du site de vuetify](https://www.vuemastery.com/courses/beautify-with-vuetify/getting-started-with-vuetify/)

Ne pas oublier d'installer Vue...
```
npm install -g @vue/cli
```
Pour commencer simplement, créer un projet test :
```
benyade@benyade-20ve:~/test$ npm create vuetify@latest

> test@0.1.0 npx
> "create-vuetify"


Vuetify.js - Material Component Framework for Vue

✔ Project name: … test
✔ Which preset would you like to install? › Default (Adds routing, ESLint & SASS variables)
✔ Use TypeScript? … No / Yes
✔ Would you like to install dependencies with yarn, npm, pnpm, or bun? › npm
✔ Install Dependencies? … No / Yes

```
Puis après ça, on lance :
```
cd test
npm run dev
```
On obtient : 
```
 VITE v6.3.5  ready in 584 ms  
  
 ➜  Local:   http://localhost:3000/  
 ➜  Network: use --host to expose  
 ➜  press h + enter to show help
```
Pour pouvoir voir la partie Network et se connecter, il faut modifier le fichier package.json dans le dossier test, et remplacer dans la partie "scripts" la ligne 
```
dev : "vite"
```
Par :
```
"dev": "vite --host",
```
On a alors :
```
benyade@benyade-20ve:~/test$ npm run dev  
  
> test@0.0.0 dev  
> vite --host  
  
  
 VITE v6.3.5  ready in 465 ms  
  
 ➜  Local:   http://localhost:3000/  
 ➜  Network: http://147.215.206.226:3000/  
 ➜  press h + enter to show help
```
![](attachments/Pasted%20image%2020250521102357.png)

Etant sur eduroam, je peux accéder à ce site avec mon téléphone en me mettant sur eduroam dessus.
![300](attachments/Pasted%20image%2020250521102601.png)
==wow very gud wp==


![](https://perso.esiee.fr/~zhangbe/wow.gif)

Maintenant, pour la prise main des composants de base, voir la [page sur les composants de Vuetify.](https://vuetifyjs.com/en/components/all/#containment)

En lien :
[[Communication par Vuetify avec un téléphone]]