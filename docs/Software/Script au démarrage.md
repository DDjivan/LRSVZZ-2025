Objectif : lancer un script au démarrage d'un appareil Linux. 

## Quoi et où 
- [server_ip-getter-displayer](../../server_ip-getter-displayer.py) 
- [client_ip-sender](../../client_ip-sender.py) 

## Comment 
- `cron` pour des tâches simples 
- `systemd` pour plus de contrôle et de fiabilité 

### `cron` / `crontab`
**`cron`** est un processus qui s'occupe de tâches planifiées, pour les appareils qui tournent un OS de type Unix. 

**`crontab`** est un fichier qui contient une liste de commandes à être exécutées. 

Pour exécuter un script au démarrage par exemple, ajouter cette ligne : 
```CRONTAB
@reboot /usr/bin/python3 /CHEMIN/VERS/LE_SCRIPT.PY
```

Pour modifier le `crontab`, exécuter cette ligne : 
```bash
crontab -e
```


### Service `systemd`
Créer un fichier de service `systemd` dans `/etc/systemd/system/`. 
Par exemple, pour un fichier de service qui s'appelle `NOM_DU_SERVICE.service`, il faut qu'il possède ce genre de contenu : 
```ini
[Unit]
Description=DESCRIPTION D'UN SCRIPT PYTHON 

[Service]
ExecStart=/usr/bin/python3 /CHEMIN/VERS/LE_SCRIPT.PY
Restart=always

[Install]
WantedBy=multi-user.target
```
Il faut le démarrer avec cette commande : 
```bash
sudo systemctl enable NOM_DU_SERVICE.service
  ```

### Méthodes spécifiques à une Raspberry Pi
Broches GPIO : Si le script interagit avec des broches GPIO, il faut peut-être utiliser une bibliothèque comme RPi.GPIO et s'assurer que le script s'exécute après l'initialisation du système GPIO. 

## Utiliser `cron`  
### Exemple d'usage 
**Cet exemple concerne le script qui envoie l'adresse IP au serveur.**

Être à la racine utilisateur. 
```bash
cd
```
Clone le repo s'il n'est pas présent. 
```bash
git clone https://github.com/DDjivan/LRSVZZ-2025
```
Copier le chemin du script Python client en faisant LMB dessus et "Copy Path(s)". 

Modifier le fichier `crontab` de l'utilisateur : 
```bash
crontab -e
```
Écrire la ligne suivante à la fin. 
```bash
@reboot python3 /home/nous/LRSVZZ-2025/client_ip-sender.py
```
Redémarrer. 
### Gérer le script 
Voir le contenu du `crontab` de l'utilisateur courant. 
```bash
crontab -l
```

`ps aux` permet de voir la liste des process (`ps` permet d'obtenir des informations sur les process). `grep` permet de garder uniquement les lignes de la sortie de `ps aux` contenant l'argument, ici `py`. 
```bash
ps aux | grep py
```

La deuxième colonne est le PID (Process ID). Besoin de tuer le process ? 
```bash
kill INSÉRER_PID_ICI
```

> [!info] À propos 
> 
> Alice et Djivan ayant suivi l'élective Systèmes d'Exploitation, ils sont censés connaître tout ça (normalement). 

> [!tip] Astuce 
> 
> Les fichiers `crontab` existent physiquement sur le stockage. Il y en a un situé à `/etc/crontab`, mais ce n'est pas celui de l'utilisateur courant. 
