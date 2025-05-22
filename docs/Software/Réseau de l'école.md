# Le réseau de l'école 
## Informations 
Les réseaux Wi-Fi `ESIEE` et `eduroam` semblent être les mêmes, mis à part l'authentification. 

Le port 50000 est possiblement ouvert. 

## S'y connecter 
**Objectif :** se connecter au réseau Wi-Fi `eduroam`. 
### Échec 
~~Première étape : customiser l’installation de l’OS pour qu’il connaisse un local hotspot~~ 

`wpa_supplicant.conf` 

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

#### Problème 
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







