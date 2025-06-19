
21/05 - 22/05

**Les différentes caractéristiques des Raspberry :**

| Caractéristique     | Raspberry Pi 3               | Raspberry Pi 4                        | Raspberry Pi 5                         |
| ------------------- | ---------------------------- | ------------------------------------- | -------------------------------------- |
| Année de sortie     | 2018                         | 2019                                  | 2023                                   |
| Processeur          | Broadcom BCM2837B0 (1.4 GHz) | Broadcom BCM2711 (1.5 GHz)            | Broadcom BCM2712 (2.4 GHz)             |
| Architecture CPU    | 4x Cortex-A53 (ARMv8)        | 4x Cortex-A72 (ARMv8)                 | 4x Cortex-A76 (64-bit, ARMv8.2-A)      |
| RAM                 | 1 Go LPDDR2                  | 2, 4 ou 8 Go LPDDR4                   | 4 ou 8 Go LPDDR4X (plus rapide)        |
| GPU                 | VideoCore IV                 | VideoCore IV                          | VideoCore VII                          |
| Ports USB           | 4 (2x USB 2.0, 2x USB 2.0)   | 2x USB 2.0 + 2x USB 3.0               | 2x USB 2.0 + 2x USB 3.0 + PCIe support |
| Sortie vidéo        | HDMI (1x full-size)          | 2x micro-HDMI (4K@30Hz ou 1x 4K@60Hz) | 2x micro-HDMI (4K@60Hz)                |
| Ethernet            | 10/100 Mbps                  | Gigabit (via USB, limité ~300 Mbps)   | Véritable Gigabit                      |
| Wi-Fi / Bluetooth   | Wi-Fi 802.11n / BT 4.2       | Wi-Fi 802.11ac / BT 5.0               | Wi-Fi 802.11ac / BT 5.0                |
| Alimentation        | Micro-USB (5V/2.5A)          | USB-C (5V/3A)                         | USB-C (PD 5V/5A recommandé)            |
| Stockage            | microSD                      | microSD + USB boot                    | microSD + USB + PCIe NVMe (via HAT)    |
| Connectique GPIO    | 40 broches                   | 40 broches                            | 40 broches (compatible)                |
| Nouveautés majeures |                              | USB 3.0, Dual HDMI, plus de RAM       | PCIe, horloge RTC, meilleur CPU/GPU    |

**Comparaison de la raspberry 3 et 4 : 

CPU : 
- L’architecture A53 est entrée de gamme (smartphones low-cost). La Pi 4 est 2 à 3x plus rapide sur les tâches lourdes (navigation, vision).

RAM :
- 1 Go est trop juste pour faire tourner un OS + traitement d’image + serveur web. Risque de swap, ralentissement fort.

USB : 
- L’USB 2.0 est trop lent pour les caméras HD ou les LIDAR modernes (bande passante faible).

Wi-Fi : 
- Le Wi-Fi n limite le débit et la stabilité de communication pour du contrôle à distance.

GPU :
- Le GPU de la Pi 3 ne peut pas traiter la vidéo en 1080p en temps réel efficacement (important pour la détection caméra).

Donc, Raspberry 3 à utiliser. 

  
**Comparaison avec la Raspberry 5 :

Meilleur dans tout sauf le prix et très puissant donc pas nécessaire pour notre projet. 

**Comparaison avec le projet**

| Critère du projet                  | Raspberry pi 3                | Raspberry pi 4                 | Raspberry pi ’5                                  |
| ---------------------------------- | ----------------------------- | ------------------------------ | ------------------------------------------------ |
| Traitement d’image (caméra, LIDAR) | Trop lent (~200-300 ms/frame) | Trop lent (~200-300 ms/frame)  | Excellent (<30 ms/frame)                         |
| Navigation autonome avec ROS       | Risque de crash / lag         | Fonctionne bien avec ROS1/ROS2 | Fonctionne très bien (ultra fluide)              |
| Interface Web (site + contrôle)    | Lent à charger, pas fluide    | Fluide pour usage basique      | Très fluide, même animations 3D                  |
| Retour capteurs en temps réel      | Lag de données                | Stable                         | Très réactif                                     |
| Autonomie énergétique              | Faible consommation           | Moyenne                        | Plus énergivore (besoin batterie + grosse)       |
| Prix                               | Économique                    | équilibré                      | Chère pour un produit étudiant                   |
| Complexité de mise en œuvre        | Simple                        | Gérée facilement,              | Besoin de gestion thermique, SSD, plus technique |



**Conclusion : 

la raspberry pi 3 : Trop limitée
  
- Processeur trop lent pour traitement d’image et navigation ROS
- 1 Go de RAM : saturation rapide du système.
- Ports USB 2.0 : limitations matérielles pour les capteurs modernes.
- Risques : lags, plantages, perte de communication, lenteur de réaction.

la raspberry pi 4 : Le bon compromis

- CPU moderne (Cortex-A72) = jusqu’à 3x plus rapide.
- 4 Go de RAM : gestion fluide de ROS + vision.
- Ports USB 3.0 : pour caméras rapides, SSD, LIDAR.
- Support de Wi-Fi ac = meilleure communication distante.

la raspberry pi 5 : Trop puissante pour ce besoin

- Très hautes performances (AI, multitâche lourd, SSD PCIe)
- Mais consommation électrique + prix + complexité d’intégration non justifiés pour ce projet
- Plus utile dans un robot haut de gamme, ou avec IA avancée (ex : reconnaissance faciale, 3D mapping temps réel

