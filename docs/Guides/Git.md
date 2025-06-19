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


