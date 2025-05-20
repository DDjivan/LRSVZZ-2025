# Raspberry Pi 

![400](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdUqR7V3iTRMHx9IjhJyjIzrAZC87YA1EP8RUSUe5E_eizSCTrJOvvTvR_df053OSU_J2VpQKkw5OmDSXjNcv03opDjbPKZX4JaBeIY3rQXt_WD1IuiIcxIlZihKU4LTymnhtWoSw?key=L4A1ejDVxs0i06ERmyTYIKsb)
Lite = pas de DE = un serveur quoi 

Le serveur (RPi 2 chez Djivan) 

| Hostname | raspberrypi-server |
| -------- | ------------------ |
| Username | dd                 |
| Password | lrsvzz             |
| Addresse | 90.22.255.6        |
Le (ou les) client qui sont les Raspberry Pi 4 à l'ESIEE qui doivent se connecter à `eduroam`. 

| Hostname | raspberrypi-client1                                           |
| -------- | ------------------------------------------------------------- |
| Username | nous                                                          |
| Password | lrsvzz                                                        |
| Addresse | dynamique, à déterminer sur http://90.22.255.6:50000/view_ips |

Comment s'y connecter ? Par exemple, voilà comment se connecter au serveur. 
Pour exécuter des commandes, se connecter en SSH. 
```
ssh dd@90.22.255.6
```

Pour accéder aux fichiers via un explorateur de fichiers, entrer cette adresse. 
```
sftp://dd@90.22.255.6/home/
```

**Pour que la plateforme du site web fonctionne, il faut :** 
1. Naviguer dans le dossier contenant le fichier texte avec toutes les données. 
```bash
cd /home/pojet
```
2. Activer l'environnement virtuel Python. 
```bash
. .venv/bin/activate
```
3. Exécuter le script Python. 
```bash
python LRSVZZ-2025/server_ip-getter-displayer.py
```

Vérifier en allant sur http://90.22.255.6:50000/view_ips ! 

## Challenge : Configurer Le Réseau 
Objectif : se connecter à `eduroam`. 
### Échec 
~~Première étape : customiser l’installation de l’OS pour qu’il connaisse un local hotspot~~ 

wpa_supplicant.conf 

[https://github.com/asparatu/raspberrypi-wpa-supplicant.conf](https://github.com/asparatu/raspberrypi-wpa-supplicant.conf) 

https://blog.iamlevi.net/2017/01/connect-raspberry-pi-peap-mschap-v2-wifi/ 

Première étape : installer un OS sans préconfigurer le réseau. 

Deuxième étape : modifier le fichier de configuration du réseau : 
`/etc/wpa_supplicant/wpa_supplicant.conf`. 

Troisième étape : entrer un nom d'utilisateur et le hash de son mot de passe. 
```bash
echo -n "plaintext_password_here" | iconv -t utf16le | openssl md4
```
Toutefois, md4 n'est plus pris en charge on dirait... 

Alors utilisons un script Python. 
```bash
pip install ntlm
```
Le hash de mon mot de passe : 
```
375abaf5de0420c373533afbc7f0def9
```

```
/etc/wpa_supplicant/wpa_supplicant.conf
```

```bash
cd etc/wpa_supplicant/
```
```bash
sudo nano wpa_supplicant.conf
```

Ajouter les lignes suivantes. 
```c
country=FR
network={
        ssid="eduroam"
        priority=1
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="vartanij@esiee.fr"
        password=hash:375abaf5de0420c373533afbc7f0def9
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
}
```

Redémarrer la configuration. 
```bash
sudo systemctl restart wpa_supplicant
```

Command pour debug. Mais elle est illisible. 
```bash
sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -d
```

### Problème 
```
Wi-Fi is currently blocked by rfkill. 
Use raspi-config to set the country before use.
```

### Solution 
Par ligne de commande et fichiers de configuration, c'est compliqué. 
Passons par l'interface graphique. 
Utiliser l'interface graphique en installant Raspberry Pi OS 64 bit **mais pas Lite**. 

1. LMB sur l'icône réseau en haut à droite 
2. LMB sur Wi-Fi Country... 
3. Sélectionner `FR  France` 
4. Sélectionner `eduroam` 
5. Changer "Authentication" à "Protected EAP (PEAP)" 
6. Cocher "No CA certificate is required" 
7. Changer "Inner authentication" à "MSCHAPv2" 
8. Entrer "Username" et "Password" 
9. LMB sur "Connect" 

En bref : 

| Ligne                             | Valeur                   |
| --------------------------------- | ------------------------ |
| Wi-Fi security                    | WPA & WPA2 Enterprise    |
| **Authentication**                | **Protected EAP (PEAP)** |
| Anonymous identity                |                          |
| Domain                            |                          |
| CA certificate                    | (None)                   |
| CA certificate password           |                          |
| Show passwords                    | O                        |
| **No CA certificate is required** | **Ø**                    |
| PEAP version                      | Automatic                |
| **Inner authentication**          | **MSCHAPv2**             |
| **Username**                      | `vartanij@esiee.fr`      |
| **Password**                      | \*\*\*\*                 |


## Ajouter le script au démarrage  
Être à la racine utilisateur. 
```bash
cd
```
Clone le repo. 
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
## Gérer le script 
View a list of existing `cron` jobs for current user: 
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

Alice tu devrais connaître tout ça normalement. 
### Tentative à ignorer 
Lancer le script python au démarrage en modifiant le fichier `/etc/crontab`.
```bash
sudo nano /etc/crontab
```

```
@reboot pi python3 /home/pi/myscript.py
```

```
@reboot pi python3 /home/pi/LRSVZZ-2025/client_ip-sender.py
```






