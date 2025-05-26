# Comment communiquer entre RPi 
Plusieurs manières. 
- SSH 

## Tunnel SSH 
### 1 - Create Tunnel 
On RPi4, run the following command to create a reverse SSH tunnel to RPi2. 
```bash
ssh -R 50000:localhost:22 user@RPi2_IP
```
   - Replace `user` with the username on RPi2. 
   - Replace `RPi2_IP` with the static IP address of RPi2. 

This command will allow RPi2 to connect to RPi4 via port 50000. 

Keep the SSH session open. This command needs to remain running for the tunnel to stay active. 

### 2 - Execute Scripts on RPi4 from RPi2
On RPi2, you can now SSH into RPi4 using the reverse tunnel. Use the following command:
```bash
ssh -p 50000 user@localhost
```
   - Replace `user` with your username on RPi4. 

### En bref  
1. RPi4. 
```bash
ssh -R 50000:localhost:22 user@RPi2_IP
```

2. RPi2. 
```bash
ssh -p 50000 user@localhost
```

3. Test command. 
```bash
echo "Current date: $(date)" > test.txt
   ```

#### Exemple 
On peut pas remplacer localhost par n'importe quoi il semble. 
Créer le tunnel : 
```bash
ssh -R 50000:localhost:22 dd@90.22.255.6
```

```bash
ssh -R 50001:localhost:22 dd@90.22.255.6
```

Se connecter en SSH : 
```bash
ssh -p 50000 nous@localhost
```

```bash
ssh -p 50001 nous@localhost
```

### Ideas 
- Make sure that SSH is installed and enabled on both Raspberry Pis with `systemctl` ; 
- Issues with permissions or connectivity? Check SSH configuration and firewall settings ; 
- Maybe set up SSH key authentication for easier access without needing to enter a password each time. 

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
