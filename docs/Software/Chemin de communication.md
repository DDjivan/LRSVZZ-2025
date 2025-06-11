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

#### `fetch-ip-auto` 
Dans le `crontab`, ajouter la ligne suivante. 
```bash
@reboot bash ~/LRSVZZ-2025/fetch-ip-auto/tunnel/client_tunnel.sh
```

## Envoyer des commandes par SSH 
Commande pour le serveur. S'assurer que le client a un tunnel d'ouvert d'abord. 
```bash
ssh -p 50001 nous@localhost "echo 'Current date: $(date)' > ~/TEST.txt"
```

### Utiliser l'authentification par clés SSH 
**Problème :** Le mot de passe du client est systématiquement demandé. 

**Solution :** Générer une paire de clés SSH sur le serveur et copier la clé publique sur le client

Faire les étapes suivantes le serveur : [Clés SSH](Clés%20SSH.md). 

Normalement, aucun mot de passe ne devrait être demandé ! 

L'inverse devrait également être fait. 

#### En bref 
Ne pas oublier de préciser un port. 

1. Sur la RPi 4. 
```bash
ssh -R 50001:localhost:22 dd@90.22.255.6 -N
```
`-N` permet de ne pas ouvrir de session, mais de juste créer le tunnel. 

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

~~S'assurer d'avoir un tunnel SSH de lancé sur le port 50001.~~ 
S'assurer que le client a bien le `crontab` contient la ligne suivante. 

![](récupérer%20l'adresse%20IP%20locale.md#^crontab)

Aller sur cette page pour tester : http://90.22.255.6:50000/ 

Un fichier de test sera créé sur la Raspberry appelé `TEST.txt` à la racine utilisateur. 




