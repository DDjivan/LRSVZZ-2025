from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__) # Initialise l'application Flask
CORS(app)  # Enable CORS for all routes

x=0

@app.route('/get_string', methods=['GET']) # Définit un point d'accès : /get_string
def get_string():
    global x
    """
    Cette fonction s'exécute quand une requête GET arrive sur /get_string
    """
    my_string = "Bonjour depuis Python ! n°"+ str(x) # Votre script Python génère cette chaîne
    x+=1
    return jsonify({"message": my_string}) # Convertit la chaîne en un objet JSON et le renvoie

if __name__ == '__main__':
    app.run(debug=True) # Lance le serveur Flask pour écouter les requêtes
