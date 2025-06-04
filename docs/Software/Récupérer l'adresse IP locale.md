## `fetch-ip` 
### Client 
Il faut ajouter ce [Script au démarrage](Script%20au%20démarrage.md) : `LRSVZZ-2025/fetch-ip/client_ip-sender.py`

Utilisons `cron`. Dans le `crontab` d'un client, ajouter la ligne suivante. 
```ini
@reboot python3 /home/nous/LRSVZZ-2025/fetch-ip/client_ip-sender.py
```

### Serveur 
Le serveur doit quant à lui exécuter un script qui héberge la page suivante. 
-> http://90.22.255.6:50000/view_ips 

Peu importe le script, il faut aller dans le bon répertoire, activer l'environnement virtuel Python (pour avoir accès à la bibliothèque Flask), puis lancer le script. 
#### Script moderne 
```bash
cd LRSVZZ-2025/second-python/
```

```bash
source ../.venv/bin/activate
```

```bash
python app.py
```

#### Script classique 
```bash
cd LRSVZZ-2025/fetch-ip/
```

```bash
source ../.venv/bin/activate
```

```bash
python server_ip-getter-displayer.py
```

## `fetch-ip-auto` 
Utilise un tunnel SSH ([Chemin de communication](Chemin%20de%20communication.md)). 

Il faut ajouter ce [Script au démarrage](Software/Script%20au%20démarrage.md) : 
`LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel.sh` 
Le script en question : [client_tunnel.sh](../../fetch-ip-auto/tunnel/client_tunnel.sh) 

Ce script utilise un fichier de configuration. 

Pour le moment, uniquement `cron` est utilisé. 

### Fichiers de configurations 
Il y a plusieurs types de fichiers de configurations 

- CFG : pas universel entre Bash et Python 
	- Python doit avoir un `[DEFAULT]`, et Bash ne doit rien avoir 
- YAML : pas built in à Python 
- JSON : parfait 
	- Attention : pas de "trailing comma" (de virgule à la fin) 
	- `jq` (processeur JSON) n'est pas toujours pré-installé sur [Linux](../Guides/Linux.md) 

### Lancer avec `cron` 
Utilisons `cron`. Dans le `crontab` d'un client, ajouter la ligne suivante. 
```ini
@reboot bash /home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel.sh
```
^crontab

```ini
@reboot bash /home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel02.sh
```
### Lancer avec un service `systemd` 
Créer un fichier de service `systemd` dans `/etc/systemd/system/`. 

```bash
sudo nano /etc/systemd/system/client_tunnel_dsm.service
```

Par exemple, pour un fichier de service qui s'appelle `NOM_DU_SERVICE.service`, il faut qu'il possède ce genre de contenu. 

```ini
[Unit]
Description=DESCRIPTION D'UN SCRIPT BASH DSM
After=network.target

[Service]
ExecStart=/usr/bin/bash /home/nous/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel.sh
Restart=always
User=nous
Environment=HOME=/home/nous
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

Il faut le démarrer avec cette commande : 
```bash
sudo systemctl enable client_tunnel_dsm.service
  ```



