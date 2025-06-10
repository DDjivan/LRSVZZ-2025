https://cli.vuejs.org/#getting-started 

## Avec NPM 
Installer Vue.js 
```bash
npm install -g @vue/cli
```

Créer un projet Vue. 
```bash
vue create test-d-app-001
```

Prendre la première option. 
```
Vue CLI v5.0.8  
? Please pick a preset:    
❯ Default ([Vue 3] babel, eslint)    
 Default ([Vue 2] babel, eslint)    
 Manually select features
```

Choisir NPM. 
```
Vue CLI v5.0.8  
? Please pick a preset: Default ([Vue 3] babel, eslint)  
? Pick the package manager to use when installing dependencies:    
 Use Yarn    
❯ Use NPM
```

Installer Vuetify. 
```bash
vue add vuetify
```

Choisir l'option par défaut. 
```  
📦  Installing vue-cli-plugin-vuetify...  
  
  
added 8 packages, and audited 925 packages in 1s  
  
118 packages are looking for funding  
 run `npm fund` for details  
  
8 vulnerabilities (4 moderate, 4 high)  
  
To address all issues (including breaking changes), run:  
 npm audit fix --force  
  
Run `npm audit` for details.  
✔  Successfully installed plugin: vue-cli-plugin-vuetify  
  
? Choose a preset: (Use arrow keys)  
 Vuetify 2 - Configure Vue CLI (advanced)    
❯ Vuetify 2 - Vue CLI (recommended)    
 Vuetify 2 - Prototype (rapid development)    
 Vuetify 3 - Vite (preview)    
 Vuetify 3 - Vue CLI (preview)
```

## Avec YARN 
https://vuejs.org/guide/quick-start.html 
 
```
yarn dlx create-vue@latest
```


```
◇  Project name (target directory):  
│  vue-project
```

1. **Router (SPA development)**: **Select this** if you want to navigate between different pages or views in your application. It’s useful for a simple web platform.
2. **ESLint (error prevention)**: **Select this** to help catch any potential errors in your code as you go along. It can be helpful even if you're not familiar with JavaScript.
3. **Prettier (code formatting)**: **Select this** to ensure your code is consistently formatted, which can make it easier to read and maintain.

```
◆  Install Oxlint for faster linting? (experimental)  
│  ○ Yes / ● No
```

```
Scaffolding project in /var/home/dd/Documents/Git/LRSVZZ-2025/web/frontend/vue-project...  
│  
└  Done. Now run:  
  
  cd vue-project  
  yarn  
  yarn format  
  yarn dev
```

Ça fonctionne pas du tout 

## Avec NPM partie 2 
```bash
npm create vue@latest
```

```bash
cd DOSSIER
```
```bash
npm install
```
```bash
npm run dev
```

Fonctionne, mais pas une bonne idée. 