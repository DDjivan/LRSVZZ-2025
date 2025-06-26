import sqlite3

conn = sqlite3.connect("data/produits.db")
c = conn.cursor()

# Création des tables
c.execute("CREATE TABLE IF NOT EXISTS products (name TEXT PRIMARY KEY)")

# Produits à insérer
products = [
    ("Tranche Pâtissière"),
    ("Chocolats"),
    ("Sandwitch Œuf Thon"),
    ("Sandwitch Jambon Beurre"),
    ("Quiche Lorraine"),
    ("Cannette 33cl de Coca Cola"),
    ("Cannette 33cl de Lipton Ice Tea"),
]

# Insertion seulement si le produit n'existe pas déjà (par nom)
for name in products:
    try:
        c.execute("INSERT INTO products VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} existe déjà, ignoré.")

conn.commit()
conn.close()
