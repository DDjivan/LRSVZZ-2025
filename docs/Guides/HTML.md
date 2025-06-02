# HTML 
Hypertext Markup Language. 

## En bref 
Le fond d'une page web. 

## Liens 
https://fr.wikipedia.org/wiki/Hypertext_Markup_Language 


## Comment 
### Explication 
Il y a deux types de composants. Avec et sans contenu. 
Un composant `acCOMP` avec contenu doit avoir une paire de fermeture avec un slash. 
```HTML
<acCOMP> CONTENU ICI </acCOMP>
```
Un composant `scCOMP` sans contenu ne doit pas être fermé. 
```HTML
<scCOMP>
```

Des paramètres sont indiqués dans le composant. 
```HTML
<COMP PARAMETRE=VALEUR>
```

### Brève liste 
Composants sans contenu, abréviés par SC : 
- Déclaration du type de document ; 
- Commentaire (un peu particulier) ; 
- Insertion d'image ; 
- Saut de ligne ; 
- Ligne horizontale ; 
- Bouton ; 

Composants avec contenu, abréviés par AC : 
- `html`, `body` ; 
- Tout ce qui est zone de texte (`p`, `h1`, `h2`... ) ; 
- Tout ce qui est style de texte (`heavy`, `oblique`... ) ; 

### Longue liste 
Commentaire (SC). 
```html
<!-- Un commentaire, 
     qui peut être sur plusieurs lignes -->
```

Au début du document (SC). 
```html
<!DOCTYPE html> 
```

Puis indiquer le contenu HTML (AC). 
```html
<html>
...
</html>
```

Dans celui-ci, il y a le `head` et le `body` (AC). 

#### `head` (AC) 
Tout ce qui sera style et informations de l'onglet. 

`title` (AC) qui donne un titre à l'onglet. 

`link` (SC) qui ajoute la référence à **un** fichier [CSS](CSS.md). 
```html
<link rel="stylesheet" href="NOM_DU_FICHIER.css">
```

`link` (SC) qui ajoute une icône 
```html
<link rel="stylesheet" href="NOM_DU_FICHIER.css">
```

#### `body` (AC) 
Tout ce qui sera sur la page. 

`div` (AC) permet de grouper des éléments juste pour de la logique. 

Tableaux (AC) : `table`, `tr`, `th`, `td`. Commencer par `table`. 
- `tr` est une rangée (table row ?) 
- `th` est une valeur en haut d'une colonne (table head ?) 
- `td` est une valeur de colonne (table data ?) 

`iframe` (AC) : une page dans une page. 
```html
<iframe src="LIEN"></iframe>
```

