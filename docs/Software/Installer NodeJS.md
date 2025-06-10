https://nodejs.org/en/download 
## Installer 
Sur une machine Linux. 
### Installer NODE 
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Relancer le shell (ou `CTRL+D`) 

~~Installer NVM 22~~ 
```
nvm install 22
```

Installer NVM 24 
```
nvm install 24
```


Vérifier la version de Node.js et npm : 
```bash
node -v
nvm current
npm -v
```
### Installer Yarn : 
Non : 
```bash
corepack enable yarn
```

Oui : 
```bash
corepack install
```

Vérifier Yarn : 
```bash
yarn -v  
```




## Désinstaller 
Tout désinstaller : 
```
rm -rf ~/.nvm
```

