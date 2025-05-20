# Plateforme Web 
Plusieurs éléments à assembler : 

- Backend (Framework Web) 
- Database (Base de données) 
- Frontend (Apparence) 
- Communication avec les Raspberry Pi 
- Bibliothèque SSH 

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

**Toutefois,** le mieux est de faire tout ça dans le script Python directement. Voir le script indiqué à cette section : [Intégration avec Flask sous Python](#Intégration%20avec%20Flask%20sous%20Python). 
## Database 
SQLite pour commencer simplement. 
https://sqlite.org/index.html 

SQLite est préinstallé. Vérifier l'installation : 
```bash
sqlite3 --version
```

### Test 1 
#### SQLite 
Créer (ou ouvrir) une base de données. 
```bash
sqlite3 instance/bdd_rpi.db
```

Créer un tableau. 
```sqlite
CREATE TABLE raspberry_pis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    delivery_step TEXT NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

Exemple d'ajout de lignes : 
```sqlite
INSERT INTO raspberry_pis (name, status, delivery_step) VALUES ('RPi4 #1', 'Connected', 'Idle');
INSERT INTO raspberry_pis (name, status, delivery_step) VALUES ('RPi4 #2', 'Disconnected', 'Busy');
```
~~Mais ça ne fonctionne pas... mais on dirait qu'après, curl -X POST fonctionne... ~~
ÇA FONCTIONNE ! 

Lire le tableau. 
```sqlite
SELECT * FROM raspberry_pis;
```

Lire la liste des tableaux. 
```sqlite
SELECT name FROM sqlite_master WHERE type='table';
```
#### Intégration avec Flask sous Python 
Installer ce module. 
```bash
pip install Flask-SQLAlchemy
```

app.py: 
```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/bdd_rpi.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.getcwd(), "instance", "bdd_rpi.db")}'
print("Current working directory:", os.getcwd())  # DEBUG
print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])  # DEBUG

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RaspberryPi(db.Model):
    __tablename__ = 'raspberry_pis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    delivery_step = db.Column(db.String(100), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/raspberrypis', methods=['GET'])
def get_raspberry_pis():
    raspberry_pis = RaspberryPi.query.all()
    print(raspberry_pis)  # DEBUG
    return jsonify([{
        'id': pi.id,
        'name': pi.name,
        'status': pi.status,
        'delivery_step': pi.delivery_step,
        'last_updated': pi.last_updated
    } for pi in raspberry_pis])


@app.route('/api/raspberrypis', methods=['POST'])
def add_raspberry_pi():
    data = request.json
    new_pi = RaspberryPi(
        name=data['name'],
        status=data['status'],
        delivery_step=data['delivery_step']
    )
    db.session.add(new_pi)
    db.session.commit()
    return jsonify({'id': new_pi.id}), 201

if __name__ == '__main__':
    # db.create_all()
    with app.app_context():  # Create an application context
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Çe ne devrait pas ressembler à ça après avoir lancé le script Python : 
```bash
dd@dd-b-framework:~$ curl http://127.0.0.1:5000/api/raspberrypis
[]
```
Mais à ça : 
```bash
dd@dd-b-framework:~$ curl http://127.0.0.1:5000/api/raspberrypis
[
  {
    "delivery_step": "Step 1",
    "id": 1,
    "last_updated": "Tue, 13 May 2025 12:15:07 GMT",
    "name": "RPi4 #1",
    "status": "Connected"
  },
  {
    "delivery_step": "Step 2",
    "id": 2,
    "last_updated": "Tue, 13 May 2025 12:15:07 GMT",
    "name": "RPi4 #2",
    "status": "Disconnected"
  }
]
```


#### IGNORE 
POST AVEC CURL: À NE PAS FAIRE PARCE QUE ÇA A L'AIR TROP GALÈRE SA RACE. 
```bash
curl -X POST http://127.0.0.1:5000/api/raspberrypis -H "Content-Type: application/json" -d '{"name": "RPi4 #1", "status": "Connected", "delivery_step": "Step 1"}'
```

## Frontend 
Jinja2??? Non. Rien à voir. 

Javascript??? 
- VueJS
	- https://vuejs.org/guide/introduction.html 
	- https://vuejs.org/about/faq.html 
- React 
	- https://react.dev/ 

On dirait que JS est obligatoire à utiliser si on veut que n'importe quel client puisse interagir avec la plateforme web. Surtout si je veux : 
- contenu de la page mis à jour dynamiquement 
	- en utilisant AJAX (Asynchronous JavaScript and XML), je crois 
- une seule page : Single Page Applications (SPAs) 
- contenu en temps réel, comme des notifs ou un chat, en utilisant des WebSockets 
- calcul du côté du client pour moins de charge côté serveur 

