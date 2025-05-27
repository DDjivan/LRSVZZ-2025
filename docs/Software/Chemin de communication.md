# Comment communiquer entre RPi 
Plusieurs manières. 
- SSH 

## Tunnel SSH 
### 1 - Créer le tunnel 
Lancer un tunnel SSH inversé. 
```bash
ssh -R PORT:localhost:22 USERNAME@ADRESSEIP
```
   - `PORT` : port à choisir pour établir la communication. 
   - `USERNAME` : nom d'utilisateur de l'ordinateur distant. 
   - `ADRESSEIP` : adresse IP (idéalement statique) de l'ordinateur distant. 

Cette commande va techniquement lancer une session SSH. Pas besoin de l'utiliser, il faut simplement la laisser active pour que le tunnel soit ouvert sur le port indiqué. 
### 2 - Se connecter en SSH 
Il est à présent possible de lancer une session SSH, mais il faut préciser le port. 
L'adresse IP à indiquer est toujours `localhost`. 
```bash
ssh -p PORT USERNAME@localhost
```
   - `PORT` : même port indiqué dans la première partie. 
   - `USERNAME` : nom d'utilisateur de l'ordinateur qui a lancé le tunnel. 

### En bref 
1. Sur la RPi 4. 
```bash
ssh -R 50001:localhost:22 dd@90.22.255.6
```

2. Sur la RPi 2. 
```bash
ssh -p 50001 nous@localhost
```

## Envoyer des commandes par SSH 
Commande pour le serveur. S'assurer que le client a un tunnel d'ouvert d'abord. 
```bash
ssh -p 50001 nous@localhost "echo 'Current date: $(date)' > ~/TEST.txt"
```

### Problème 
Le mot de passe du client est systématiquement demandé. 

Solution : Generate SSH key pair on the server and copy the public key to the client. 

Faire les étapes suivantes le serveur : 
1. Générer les clés. 
```bash
ssh-keygen -t rsa -b 4096
```

```
Enter file in which to save the key (/home/nous/.ssh/id_rsa):
```
Appuyer sur ENTER pour que l'option par défaut soit choisie (`~/.ssh/id_rsa`). 
```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
```
Appuyer deux fois sur ENTER pour ne pas mettre de passphrase. 

2. Envoyer la clé publique du serveur au client. 
```bash
ssh-copy-id -p 50001 nous@localhost
```

3. Tester la connexion automatique. 
```bash
ssh -p 50001 nous@localhost
```

Normalement, aucun mot de passe ne devrait être demandé ! 

L'inverse devrait également être fait. 
#### En bref 
1. Sur la RPi 4. 
```bash
ssh -R 50001:localhost:22 dd@90.22.255.6
```

2. Sur la RPi 2 (qui a une paire de clés). 
```bash
ssh-copy-id -p 50001 nous@localhost
```

3. Sur n'importe quel ordinateur (qui a une paire de clés) pour se connecter à la RPi 2. 
```bash
ssh-copy-id dd@90.22.255.6
```

4. Sur n'importe quel ordinateur (qui a une paire de clés) pour se connecter à une RPi 4. 
```bash
ssh-copy-id nous@ADRESSEIP
```


## Envoyer des commandes en SSH via Web 
Sur le serveur, lancer le back-end et front-end [Flask](../Guides/Flask.md) : 
```bash
cd /home/dd/LRSVZZ-2025/fetch-ip-auto/
```
```bash
python server_script-launcher.py
```

S'assurer d'avoir un tunnel SSH de lancé sur le port 50001. 

Aller sur cette page pour tester : http://90.22.255.6:50000/ 

Un fichier de test sera créé sur la Raspberry appelé `TEST.txt` à la racine utilisateur. 

