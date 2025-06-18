import sqlite3

conn = sqlite3.connect("data/produits.db")
c = conn.cursor()

# Création des tables
c.execute("CREATE TABLE IF NOT EXISTS products (name TEXT PRIMARY KEY)")

# Produits à insérer
products = [
    ("Sand Witch à la fraise"),
    ("Ouiche Lorraine"),
    ("Docteur Poivre"),
    ("Coke"),
    ("Lèvre thon")
]

# Insertion seulement si le produit n'existe pas déjà (par nom)
for name in products:
    try:
        c.execute("INSERT INTO products VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} existe déjà, ignoré.")

conn.commit()
conn.close()
