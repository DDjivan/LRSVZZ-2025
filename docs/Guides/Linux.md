# Linux 
Noyau open-source, mais fait plus souvent référence aux systèmes d'exploitation l'utilisant. 

## Quoi 
`cd` : change directory. 
- Changer de répertoire courant. 
```bash
cd NOM_DU_CHEMIN
```
- Aller à la racine utilisateur. 
```bash
cd
```



Obtenir l'adresse IP locale. 
```bash
ip a
```

Voir l'état du serveur de secure shell (SSH). 
```bash
systemctl status sshd 
```



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
1. Version basique 
```
top
```
2. Version améliorée 
```
htop
```
3. Meilleure version (pas installée par défaut) selon [VARTANIAN Djivan](VARTANIAN%20Djivan) 
```bash
btop
```



Chercher un package des repo de Debian sur une distribution Debian. 
```
apt search NOM_DU_PACKAGE
```

Installer un package des repo de Debian sur une distribution Debian. 
```
sudo apt install NOM_DU_PACKAGE
```


