## `fetch-ip` 
Dans le crontab ([Script au démarrage](Script%20au%20démarrage.md)) d'un client, ajouter la ligne suivante. 
```ini
@reboot python3 /home/nous/LRSVZZ-2025/fetch-ip/client_ip-sender.py
```

Le serveur doit quant à lui exécuter le script suivant. 
```bash
python server_ip-getter-displayer.py
```

Penser à être dans le bon répertoire, et d'avoir l'environnement virtuel Python d'activé pour avoir accès à la bibliothèque Flask. 
```bash
cd LRSVZZ-2025/fetch-ip/
```
```bash
. .venv/bin/activate
```

Vérifier en allant sur http://90.22.255.6:50000/view_ips ! 

## `fetch-ip-auto` 
En cours. 
Voir [Chemin de communication](Chemin%20de%20communication.md). 

Dans le crontab ([Script au démarrage](Script%20au%20démarrage.md)) d'un client, ajouter la ligne suivante. 
```ini
@reboot bash /home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel.sh
```
