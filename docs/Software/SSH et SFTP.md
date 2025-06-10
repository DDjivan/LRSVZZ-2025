# Se connecter à distance 
## Installation  
![400](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUqR7V3iTRMHx9IjhJyjIzrAZC87YA1EP8RUSUe5E_eizSCTrJOvvTvR_df053OSU_J2VpQKkw5OmDSXjNcv03opDjbPKZX4JaBeIY3rQXt_WD1IuiIcxIlZihKU4LTymnhtWoSw?key=L4A1ejDVxs0i06ERmyTYIKsb)

Logiciel utilisé : [Raspberry Pi Imager](appstream:org.raspberrypi.rpi-imager). 

Lite = headless = pas de DE (desktop environment) = un serveur. 
Mais il n'y a aucun inconvénient à utiliser une distribution avec DE comme un serveur. 

## Nos Raspberry Pi 
Il y a trois Raspberry Pi : 
- le serveur (RPi 2 B chez Djivan) ; 
- les clients qui sont les RPi 4 B à l'ESIEE qui doivent se connecter à `eduroam`. 

| Carte SD | SanDisk 58.03 GiB                        | Logo Raspberry        | 32 GB                 |
| -------- | ---------------------------------------- | --------------------- | --------------------- |
| Modèle   | Raspberry Pi 2 B                         | Raspberry Pi 4 B      | Raspberry Pi 4 B      |
| Hostname | `raspberrypi-server`                     | `raspberrypi-client1` | `raspberrypi-client2` |
| Username | `dd`                                     | `nous`                | `nous`                |
| Password | `caché`                                  | `lrsvzz`              | `lrsvzz`              |
| Addresse | `90.22.255.6`                            | Dynamique             | Dynamique             |

Dynamique = à déterminer sur http://90.22.255.6:50000/view_ips 

Pour faire tourner cette plateforme web qui récupère et affiche les adresses IP, voir [Récupérer l'adresse IP locale](Récupérer%20l'adresse%20IP%20locale.md). 

## Comment s'y connecter ? 
Pour exécuter des commandes, utiliser la commande SSH. 
```bash
ssh USERNAME@ADRESSEIP
```

Pour accéder aux fichiers via un explorateur de fichiers, entrer cette adresse. 
```URL
sftp://USERNAME@ADRESSEIP/CHEMIN/
```

### Exemple concret 
**Par exemple, comment se connecter au serveur (RPi 2).** 
```bash
ssh dd@90.22.255.6
```

```URL
sftp://dd@90.22.255.6/home/
```

### Recommandé 
Générer des [Clés SSH](Clés%20SSH.md). 

