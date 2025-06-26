from flask import Flask

from flask_routes.app_home import app_home
from flask_routes.app_home import app_home
from flask_routes.app_docs import app_docs
from flask_routes.app_dev import app_dev
from flask_routes.app_fetch_ip import app_ip
from flask_routes.app_canvas_draw import app_canvas
from flask_routes.app_canvas_upload import app_upload

from flask import render_template, request, redirect, url_for
from os import path
import sqlite3
from flask_socketio import SocketIO, emit

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app = Flask(__name__)
socketio = SocketIO(app)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app.register_blueprint(app_home)
app.register_blueprint(app_docs)
app.register_blueprint(app_dev)
app.register_blueprint(app_ip)
app.register_blueprint(app_canvas)
app.register_blueprint(app_upload)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

def get_products():
    conn = sqlite3.connect("data/gestion.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

@app.route('/client')
def web_client() :
    products = get_products()
    return render_template("client.html", products=products)


@app.route("/commander", methods=["POST"])
def commander():
    # Récupérer la destination choisie dans le formulaire
    destination = request.form.get("destination")

    # Récupérer la liste des produits (keys dans request.form pour quantités)
    produits_commandes = []
    for key in request.form:
        if key.startswith("quantite_"):
            qty = int(request.form.get(key, 0))
            if qty > 0:
                # Récupérer le nom du produit (remplacer underscores par espaces)
                produit = key[len("quantite_"):].replace('_', ' ')
                produits_commandes.append((produit, qty))

    if not produits_commandes:
        return "Aucun produit sélectionné", 400

    conn = sqlite3.connect("data/gestion.db")
    c = conn.cursor()

    # Insérer la commande et récupérer son ID
    c.execute("INSERT INTO orders (destination, date) VALUES (?, datetime('now'))", (destination,))
    order_id = c.lastrowid

    # Insérer les produits commandés dans order_items
    for produit, quantite in produits_commandes:
        c.execute("INSERT INTO order_items (order_id, product_name, quantity) VALUES (?, ?, ?)",
                  (order_id, produit, quantite))
    conn.commit()
    conn.close()

    socketio.emit("new order")

    return redirect(url_for('web_client'))

@app.route('/gestion')
def web_gestion() :
    return render_template('gestion.html',products=get_products())

@app.route('/ajouter-produit', methods=['POST'])
def ajouter_produit():
    data = request.get_json()
    name = data.get('name')
    try:
        conn = sqlite3.connect("data/gestion.db")
        c = conn.cursor()
        c.execute("INSERT INTO products (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        return '', 204
    except sqlite3.IntegrityError:
        return 'Produit déjà existant', 409

@app.route('/supprimer-produit', methods=['POST'])
def supprimer_produit():
    data = request.get_json()
    name = data.get('name')
    conn = sqlite3.connect("data/gestion.db")
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    return '', 204

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

@app.route('/vendeur', methods=['GET', 'POST'])
def web_server():
    conn = sqlite3.connect("data/gestion.db")
    c = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        order_id = request.form.get('order_id')
        if not order_id:
            return "ID commande manquant", 400

        if action in ['refuser', 'envoyer']:
            # Supprimer la commande et ses items dans les deux cas (plus de suivi)
            c.execute("DELETE FROM order_items WHERE order_id = ?", (order_id,))
            c.execute("DELETE FROM orders WHERE id = ?", (order_id,))
            conn.commit()

            return redirect(url_for('web_server'))

    # Afficher toutes les commandes (toutes les commandes sont en attente tant qu'elles existent)
    c.execute("""
        SELECT id, destination, date
        FROM orders
        ORDER BY date DESC
    """)
    commandes = c.fetchall()

    commandes_detaillees = []
    for cmd in commandes:
        order_id, destination, date = cmd
        c.execute("SELECT product_name, quantity FROM order_items WHERE order_id = ?", (order_id,))
        items = c.fetchall()
        commandes_detaillees.append({
            'id': order_id,
            'destination': destination,
            'date': date,
            'order_items': items   # <-- changer "items" en "order_items"
        })


    conn.close()
    return render_template('vendeur.html', commandes=commandes_detaillees)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    socketio.run(app,host='0.0.0.0', port=50000, debug=True)
