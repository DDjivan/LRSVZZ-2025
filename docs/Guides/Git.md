# Git 
Logiciel open source qui fait du versioning. 
Permet donc de revenir à une version précédente sans inquiétude. ^Explication

## Liens 
https://fr.wikipedia.org/wiki/Git 

## Comment  
Commandes essentielles pour cloner, mettre à jour et gérer le repo, surtout sur une [Raspberry Pi](Raspberry%20Pi.md). 

Cloner le repo. 
```bash
git clone https://github.com/DDjivan/LRSVZZ-2025
```
Cloner = Télécharger tous les fichiers pour la première fois. Si le dossier est déjà présent, il faudra pull. 

Naviguer dans le répertoire du dépôt. 
```bash
cd LRSVZZ-2025
```
`cd` = change directory. 

Obtenir des informations sur l'état du repo. 
```bash
git status
```

Mettre à jour le repo avec les dernières modifications de la branche `main`. 
```bash
git pull origin main
```
Remplacer `main` par le nom d'une autre branche si nécessaire. 


