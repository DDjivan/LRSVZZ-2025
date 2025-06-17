# Back-end 
## En bref 
Permet de créer les adresses à naviguer et à accéder. 
Peut envoyer du contenu [HTML](../Guides/HTML.md) (qui contient [CSS](../Guides/CSS.md) et [JavaScript](../Guides/JavaScript.md)), ce dernier gérant tout ce qui est [Front-end](Front-end.md). 

Dans le cadre du projet, du contenu [Markdown](../Guides/Markdown.md) est utilisé, qui est converti en HTML. 

## Choix 
**Choix du langage :** [Python](../Guides/Python.md). 

**Choix de la bibliothèque :** [Flask](../Guides/Flask.md). 

## Initialiser un environnement 
En suivant les [instructions Flask](https://flask.palletsprojects.com/en/stable/installation/) : 

1. Créer un nouveau dossier et y naviguer. 
```bash
mkdir -p EXEMPLEBACKEND && cd $_
```

2. Créer un environnement virtuel. 
```bash
python3 -m venv .venv
```

3. Activer l'environnement virtuel 
```bash
. .venv/bin/activate
```

4. Installer la bibliothèque 
```bash
pip install Flask
```

## Lancer le script Python 
### 1. `flask` dans le terminal (non recommandé) 
En créant un fichier `app.py` et en y mettant du code Python utilisant Flask, on peut exécuter la ligne suivante pour lancer la plateforme. 
```bash
flask run
```

Pour y accéder de n’importe quelle adresse IP et pas seulement [http://localhost:5000](http://localhost:5000) , on peut exécuter la ligne suivante. 
```bash
flask run --host=0.0.0.0
```

Pour plus de paramètres. 
```bash
flask --app app.py run --host=0.0.0.0 --port=5000 --debug
```

### 2. `main` dans le script (recommandé) 
**Toutefois,** le mieux est de faire tout ça dans le script Python directement. Tel que : 
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
```

## Utiliser Flask 
Les deux fonctions sont nécessaires. 
```python
from flask import Flask, render_template
```

4. Installer la bibliothèque `markdown2`. 
```bash
pip install markdown2
```