# Logiciel Inkscape 
Inkscape est un logiciel de dessin vectoriel gratuit open source. 

## Liens 
- [Site officiel](https://inkscape.org/fr/) 
- [Page Wikipédia](https://fr.wikipedia.org/wiki/Inkscape) 
- [Flatpak](appstream:org.inkscape.Inkscape) 
- [Téléchargements pour d'autres plateformes](https://inkscape.org/fr/release/) 

## Pourquoi 
Pour réaliser des affiches, le dessin vectoriel est essentiel, parce que la majorité des logiciels de photomontage sont du dessin bitmap. 

Alternatives : 

- Adobe Illustrator 
- LibreOffice - Draw 
- Karbon 

## Comment 
Format de fichier : `SVG`. 


## Problèmes 
### Importer d'autres fichiers 
Lors de l'import d'un SVG dans le document, quelle option choisir ? 

> SVG Image Import Type:
> 
> 🔘 Include SVG image as editable object(s) in the current file
> ⚪ Add SVG as new page(s) in the current file
> ⚪ Embed the SVG file in an image tag (not editable in this document)
> ⚪ Link the SVG file in an image tag (not editable in this document).
> ⚪ Open SVG image as separate document
> 
> DPI for rendered SVG: 96.00 
> \[...\] 

Utilisant un repo, la duplication de données est à éviter. Ainsi, la meilleure option serait de  **link the SVG file in an image tag**. 

Attention : l'import ajoute un chemin complet vers le fichier. Pour modifier cela, ouvrir le fichier dans un éditeur de texte, et trouver l'image. 
```xml
<image
preserveAspectRatio="none"
inkscape:svg-dpi="96"
width="160.02499"
height="92.324997"
xlink:href="file:///var/home/dd/Documents/Git/LRSVZZ-2025/docs/Design/FichiersPoster/Triple-logo_ESIEE_CCI_UGE.svg"
id="image1"
x="1099.9875"
y="635.83752" />
```

Changer la ligne en `xlink:href="Triple-logo_ESIEE_CCI_UGE.svg"` 

### Résolution 
Propriétés de l'objet. 



