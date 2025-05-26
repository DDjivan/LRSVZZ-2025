# Se connecter à distance 
## Nos Raspberry Pi 
![400](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUqR7V3iTRMHx9IjhJyjIzrAZC87YA1EP8RUSUe5E_eizSCTrJOvvTvR_df053OSU_J2VpQKkw5OmDSXjNcv03opDjbPKZX4JaBeIY3rQXt_WD1IuiIcxIlZihKU4LTymnhtWoSw?key=L4A1ejDVxs0i06ERmyTYIKsb)
Lite = headless = pas de DE (desktop environment) = un serveur. 

Il y a trois Raspberry Pi : 
- le serveur (RPi 2B chez Djivan) ; 
- les clients qui sont les RPi 4B à l'ESIEE qui doivent se connecter à `eduroam`. 

| Carte SD | SanDisk 58.03 GiB    | Logo Raspberry        | 32 GB                 |
| -------- | -------------------- | --------------------- | --------------------- |
| Modèle   | Raspberry Pi 2 B     | Raspberry Pi 4 B      | Raspberry Pi 4 B      |
| Hostname | `raspberrypi-server` | `raspberrypi-client1` | `raspberrypi-client2` |
| Username | `dd`                 | `nous`                | `nous`                |
| Password | `lrsvzz`             | `lrsvzz`              | `lrsvzz`              |
| Addresse | `90.22.255.6`        | Dynamique             | Dynamique             |
Dynamique = à déterminer sur http://90.22.255.6:50000/view_ips 

## Comment s'y connecter ? 
**Par exemple, comment se connecter au serveur.** 

Pour exécuter des commandes, se connecter en SSH. 
```bash
ssh dd@90.22.255.6
```

Pour accéder aux fichiers via un explorateur de fichiers, entrer cette adresse. 
```URL
sftp://dd@90.22.255.6/home/
```

## Plateforme web  
Allumer la plateforme web qui récupère et affiche les adresses IP. 
Il faut faire les étapes suivantes en SSH. 

1. Naviguer dans le dossier contenant le fichier texte avec toutes les données. 
```bash
cd LRSVZZ-2025/fetch-ip/
```

2. Activer l'environnement virtuel [Python](../Guides/Python.md). 
```bash
. .venv/bin/activate
```

3. Exécuter le script Python. 
```bash
python server_ip-getter-displayer.py
```

Vérifier en allant sur http://90.22.255.6:50000/view_ips ! 

