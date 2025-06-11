# Cahier des charges fonctionnel 
Document obligatoire à réaliser. 

https://fr.wikipedia.org/wiki/Cahier_des_charges_fonctionnel 
https://fr.wikipedia.org/wiki/Cahier_des_charges 

## Comment 
Markdown est trop limité. 

Obsidian a des plugins de la communauté mais ils ne fonctionnent pas très bien. 
https://github.com/l1xnan/obsidian-better-export-pdf 
https://github.com/corentin-godefroy/Obsidian-BreakPage 

Google Docs est lent et mal organisé. 

Utilisons LaTeX. 

Dans le `.gitignore`, ces lignes doivent être ajoutées, car seul le `.tex` suffit. 
```ini
# NEW: LaTeX
*.aux
*.log
*.out
*.synctex.gz
docs/CDCF/*.pdf
*.toc
```

Logiciel utilisé par [VARTANIAN Djivan](VARTANIAN%20Djivan) : TeXstudio. 

- [Site officiel](https://www.texstudio.org/) 
- [Flatpak](appstream:org.texstudio.TeXstudio) 

## Où 
Fichier du CDCF : [cdcf-001.tex](CDCF/cdcf-001.tex). 

Template utilisé : https://chef-de-projet.fr/cahier-des-charges-fonctionnel/ 


