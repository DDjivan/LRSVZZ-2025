# Git 
Logiciel open source qui fait du versioning, et bien plus. 
Permet donc de revenir à une version précédente sans inquiétude. ^Explication
Essentiel pour la réalisation de projet contenant du code et de la documentation. 

## Liens 
https://git-scm.com/ 
https://fr.wikipedia.org/wiki/Git 
https://github.com/git/git 

## Comment  
Commandes essentielles pour cloner, mettre à jour et gérer le repo, surtout sur une [Raspberry Pi](Raspberry%20Pi.md). 

Cloner le repo. 
```bash
git clone https://github.com/DDjivan/LRSVZZ-2025
```
Cloner = Télécharger tous les fichiers pour la première fois. Si le dossier est déjà présent, il faudra pull. 

Le reste de ces commandes sont à réaliser à l'intérieur du répertoire du repo cloné. 

Obtenir des informations sur l'état du repo. 
```bash
git status
```

Changer de branche, ou s'assurer d'être dans une branche. 
```bash
git switch NOM_DE_LA_BRANCHE
```
Il y a aussi `checkout`, mais il vaut mieux utiliser `switch`. 
```bash
git checkout NOM_DE_LA_BRANCHE
```

Mettre à jour le repo avec les dernières modifications de la branche actuelle. 
```bash
git pull
```

---

À ignorer : 
	Mettre à jour le repo avec les dernières modifications de la branche `main`. 
```bash
	git pull origin main
```
	Remplacer `main` par le nom d'une autre branche si nécessaire. 

## Problèmes 
Un conflit de fichier qui contient énormément de "current changes" et de "incoming changes", comme avec un fichier SVG ? 

En ouvrant le fichier avec VSCodium, (faire `Ctrl+Shift+P` et sélectionner "View: Reopen Editor with Text Editor" si la version texte ne s'affiche pas), il est possible de gérer plus facilement les différences. 

Utiliser la Command Palette (`Ctrl+Shift+P`) et sélectionner "Merge Conflict: Accept All Incoming" ou "Merge Conflict: Accept All Current" pour garder une version uniquement. 

Ensuite, faire "enregistrer sous" pour chacune des sélections fois pour créer les deux fichiers. 

[Source](https://stackoverflow.com/questions/52288120/how-can-i-accept-all-current-changes-in-vscode-at-once) 


