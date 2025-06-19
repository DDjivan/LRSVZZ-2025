# CSS 
Cascading Style Sheets. 

## En bref 
~~La~~ Une forme d'une page web. 
A besoin d'être référencée dans le code HTML. 

## Liens 
https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade 


## Comment 
Similaire à l'écriture du C ou du Java -> accolades et points virgules. 

Commentaire. 
```css
/* Un commentaire, 
   qui peut être sur plusieurs lignes */
```

Classe : `.NOMDELACLASSE`

Identifiant : `#NOMDELIDENTIFIANT`

## Problèmes 
Page illisible sur un affichage plus petit, comme sur un téléphone ? 
Utiliser `@media` avec des paramètres, par exemple : 
```css
@media (min-width: 0px) and (max-width: 300px) {
	body {
		padding-left: 0%;
	}
}
```

Images qui dépassent le cadre de leur `div` ? Ajouter ceci. 
```css
/* ... */ img {
    max-width: 100%;  /* ensure images do not exceed width of container */
    height: auto;  /* auto = same aspect ratio */
    display: block;  /* center the image */
    /* margin: 0 auto; */ /* center the image horizontally */
}
```


