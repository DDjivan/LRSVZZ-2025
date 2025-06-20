from flask import Flask, render_template

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

try:
    from markdown2 import markdown
    MARKDOWN_LIBRARY = 'markdown2'
except ImportError:
    try:
        from markdown import markdown
        MARKDOWN_LIBRARY = 'markdown'
    except ImportError:
        raise ImportError("No Markdown library available. Please install either markdown or markdown2.")

def md_to_html(md_data) :
    if MARKDOWN_LIBRARY == 'markdown2':
        html_data = markdown(md_data, extras=['tables', 'footnotes', 'fenced-code-blocks', 'break-on-newline'])
    else:
        html_data = markdown(md_data, extensions=['tables', 'footnotes', 'fenced_code', 'breaks'])

    return html_data

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

app = Flask(__name__)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from re import sub, MULTILINE

def convert_https_links(text):
    pattern = r'(?<!\]\()' + r'http(s)?://[^\s]+'

    # text_with_links = sub(pattern, r'[\1](\1)', text, flags=MULTILINE)

    def escape_underscores(match):
        url = match.group(0)
        escaped_url = url.replace('_', r'\_')
        return f'[{escaped_url}]({escaped_url})'

    text_with_links = sub(pattern, escape_underscores, text, flags=MULTILINE)

    return text_with_links

def convert_strikethrough_text(text):
    pattern = r'~~(.*?)~~'
    result = sub(pattern, r'<s>\1</s>', text)
    return result

def convert_highlighted_text(text):
    pattern = r'==(.*?)=='
    result = sub(pattern, r'<mark>\1</mark>', text)
    return result

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from os import path
import sqlite3

@app.route('/')
def web_home() :
    return render_template('index.html')

@app.route('/choix')
def web_choix() :
    return render_template('choix.html')

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
def get_products():
    conn = sqlite3.connect("data/gestion.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

from flask_socketio import SocketIO, emit

socketio = SocketIO(app)

@app.route('/client')
def web_client() :
    products = get_products()
    return render_template("client.html", products=products)

from flask import request
# Traitement de la commande

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


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

@app.route('/dev')
def web_dev() :
    return render_template('dev.html')

@app.route('/docs')
def web_doc() :
    sREADME = path.join('../', 'README.md')

    with open(sREADME, 'r', encoding='utf-8') as file:
        md_data = file.read()

    # html_data = markdown(md_data)
    html_data = markdown(md_data, extras={
        'breaks': {'on_newline': True, 'on_backslash': True},
        'tables': True,
        'footnotes': True
    })

    return render_template('doc.html', content=html_data)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

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

@app.route('/gestion')
def web_gestion() :
    return render_template('gestion.html',products=get_products())

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from flask import redirect, url_for

@app.route('/server', methods=['GET', 'POST'])
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
    return render_template('server.html', commandes=commandes_detaillees)


@app.route('/<path:filename>')
def web_markdown(filename:str) :

    sPath = path.join('../', filename)

    if not path.isfile(sPath):
        return render_template('doc.html', content=f'<h1>404 Not Found</h1>')

    with open(sPath, 'r', encoding='utf-8') as file:
        data = file.read()

    if not filename.endswith('.md'):
        return render_template('doc.html', content=f'<pre>{data}</pre>')

    data = convert_https_links(data)
    data = convert_strikethrough_text(data)
    data = convert_highlighted_text(data)

    html_data = md_to_html(data)

    # return render_template_string(html_data)
    return render_template('doc.html', content=html_data)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from flask import request
from datetime import datetime

sFile = '../fetch-ip/rpi4_ip.txt'

@app.route('/update_ip', methods=['POST'])
def update_ip() :
    hostname   = request.form['hostname']
    username   = request.form['username']
    ip_address = request.form['ip']

    current_time = datetime.now().isoformat().replace('T', ' ')  # ISO 8601 but remove the T

    # write datetime, IP address, hostname, and username in a file
    with open(sFile, 'a') as f :
        f.write(f'{current_time} - {ip_address} - {hostname} - {username}\n')

    return 'RPi2-Listener here. Well received the three of your data!', 200

@app.route('/view_ips', methods=['GET'])
def view_ips() :
    try :
        with open(sFile, 'r') as f :
            content = f.read()

        # return f'<pre>{content}</pre>'
        content = f'<pre>{content}</pre>'

    except FileNotFoundError :
        # return 'The file is empy: no IP addresses recorded yet.', 404
        content = "The file is empy: no IP addresses recorded yet."

    finally:
        new_content = md_to_html(content)
        return render_template('index.html', content=new_content)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

from subprocess import run
from datetime import datetime
# from json import load

@app.route('/execute_script')
def execute_script():

    sCommand = 'echo "JS to Python to Bash: $(date +%Y-%m-%dT%H:%M:%S.%6N)" > ~/TEST.txt'
    lRun = [sCommand]

    run(lRun, shell=True)

    current_time = datetime.now().isoformat().replace('T', ' ')

    return "JS to Python to HTML: " + current_time


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

@app.route('/moteurMarche')
def moteurMarche():

    run(
            ["ssh", "-p", "50001", "nous@localhost","python moteurMarche.py"],
            check=True
        )
    return "Moteur en marche"


# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- #

if __name__ == '__main__' :
    socketio.run(app,host='0.0.0.0', port=50000, debug=True)
