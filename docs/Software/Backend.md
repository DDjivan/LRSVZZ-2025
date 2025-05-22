## Backend 
**Choix du langage :** Python 

Bibliothèque Python Flask : 
https://flask.palletsprojects.com/en/stable/quickstart/

Bibliothèque Python Django : 
https://www.djangoproject.com/ 

**Choix de la bibliothèque :** Flask 

Soit Python, soit JavaScript. Je commence à regarder Python parce que familier et simple. 

En suivant les [instructions Flask](https://flask.palletsprojects.com/en/stable/installation/) : 

1. Créer un nouveau dossier et y naviguer. 

```bash
mkdir -p pojet && cd $_
```

2. Créer un environnement virtuel. 
```bash
python3 -m venv .venv
```

3. Activer l'environnement 
```bash
. .venv/bin/activate
```

4. Installer la bibliothèque 
```bash
pip install Flask
```



En créant un fichier `app.py` et en y mettant du code Python utilisant Flask, on peut exécuter la ligne suivante pour lancer la plateforme. 
```bash
flask run
```

Pour y accéder de n’importe quelle adresse IP et pas seulement [http://localhost:5000](http://localhost:5000) , on peut exécuter la ligne suivante 
```bash
flask run --host=0.0.0.0
```

```bash
flask --app app.py run --host=0.0.0.0 --port=5000 --debug
```

**Toutefois,** le mieux est de faire tout ça dans le script Python directement. Voir le script indiqué à cette section : [Intégration avec Flask sous Python](Database.md#Intégration%20avec%20Flask%20sous%20Python) 


