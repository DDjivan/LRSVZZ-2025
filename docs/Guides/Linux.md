# Linux 
Noyau open-source, mais fait plus souvent référence aux systèmes d'exploitation l'utilisant. 

## Comment 
S'y connecter à distance : [SSH et SFTP](../Software/SSH%20et%20SFTP.md). 

### Shell 
`CTRL+C` pour annuler la commande exécutée (cancel). 
`CTRL+D` pour se déconnecter (disconnect). 

### Commandes dans le terminal 
`cd` : change directory. 
- Changer de répertoire courant. 
```bash
cd NOM_DU_CHEMIN
```
- Aller à la racine utilisateur. 
```bash
cd
```

---

Obtenir l'adresse IP locale. 
```bash
ip a
```

Voir l'état du serveur de secure shell (SSH). 
```bash
systemctl status sshd 
```

---

`kill` : Envoyer un signal à un process, surtout pour l'arrêter. 
- Terminer un process. 
```bash
kill PID_ICI
```
- Mettre fin à un process (de force). 
```bash
kill -KILL PID_ICI
```

Obtenir des informations en temps réel sur les process. 
1. Version basique. 
```bash
top
```
2. Version améliorée. 
```bash
htop
```
3. Meilleure version (pas installée par défaut) selon [VARTANIAN Djivan](../People/VARTANIAN%20Djivan.md). 
```bash
btop
```

---

Chercher un package des repo de Debian sur une distribution Debian. 
```bash
apt search NOM_DU_PACKAGE
```

Installer un package des repo de Debian sur une distribution Debian. 
```bash
sudo apt install NOM_DU_PACKAGE
```


