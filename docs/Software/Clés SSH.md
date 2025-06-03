# Générer des clés SSH 
## Pourquoi 
Depuis un ordinateur, si on se connecte en SSH à un appareil, il ne nous connaît pas par défaut, et nous demande un mot de passe. 

Mais en donnant une clé SSH publique à l'appareil, aucun mot de passe ne devrait être demandé. 

## Comment 
Générer une paire de clés SSH sur un ordinateur, et copier sa clé publique vers un appareil dont on veut se connecter immédiatement. 

Faire les étapes suivantes sur l'ordinateur : 

1. Générer une clé privée et une clé publique. 
```bash
ssh-keygen -t rsa -b 4096
```

```
Enter file in which to save the key (~/.ssh/id_rsa):
```
Appuyer sur `ENTER` pour que l'option par défaut soit choisie (`~/.ssh/id_rsa`). 

```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
```
Appuyer deux fois sur `ENTER` pour ne pas mettre de passphrase. 

---

2. Envoyer la clé publique du serveur au client. 
```bash
ssh-copy-id USERNAME-APPAREIL@localhost
```

---

3. Tester la connexion automatique. 
```bash
ssh USERNAME-APPAREIL@localhost
```

