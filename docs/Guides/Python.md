# Python 
Langage de programmation simple, lisible et très utilisé.
Parfait pour les prototypes, l’automatisation, l’IA, le web ou le scripting sur [Raspberry Pi](Raspberry%20Pi.md). 

## Liens 
https://fr.wikipedia.org/wiki/Python_(langage) 

## Environnement virtuel 
==Se renseigner sur la pertinence d'un environnement virtuel.==

https://pip.pypa.io/en/stable/installation/ 

https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments 

### Comment 
Créer l'environnement. 
```bash
cd LRSVZZ-2025/
```

```bash
python3 -m venv .venv
```

Activer l'environnement depuis la racine du repo. 
```bash
source .venv/bin/activate
```

Activer l'environnement depuis un dossier situé à la racine du repo. 
```bash
source ../.venv/bin/activate
```

Activer l'environnement depuis un dossier situé à la racine du repo. 
```bash
source LRSVZZ-2025/.venv/bin/activate
```

Désactiver l'environnement. 
```bash
deactivate
```

Installer les bibliothèques utilisées. 
```bash
pip install flask markdown2
```


