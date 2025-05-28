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

### Service `systemd`
Créer un fichier de service `systemd` dans `/etc/systemd/system/`. 
Par exemple, pour un fichier de service qui s'appelle `NOM_DU_SERVICE.service`, il faut qu'il possède ce genre de contenu : 

```bash
sudo nano /etc/systemd/system/client_tunnel_de_ses_morts.service
```

```ini
[Unit]
Description=DESCRIPTION D'UN SCRIPT BASH DE SES MORTS
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
sudo systemctl enable client_tunnel_de_ses_morts.service
  ```



```bash
ssh -R 50001:localhost:22 dd@90.22.255.6 -N
```
```ini
@reboot ssh -R 50001:localhost:22 dd@90.22.255.6 -N
```
```ini
@reboot ssh -R 50001:localhost:22 dd@90.22.255.6 -N >> /home/nous/ssh_tunnel.log 2>&1
```
```ini
@reboot sleep 30 && ssh -R 50001:localhost:22 dd@90.22.255.6 -N >> /home/nous/ssh_tunnel.log 2>&1
```
```ini
@reboot /home/nous/start_ssh_tunnel.sh
```




