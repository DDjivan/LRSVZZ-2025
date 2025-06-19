# MathJax 
D'après [la page Wikipédia de LaTeX](https://fr.wikipedia.org/wiki/LaTeX#Distributions_TeX) : 

> MathJax : une bibliothèque en JavaScript permettant de formater des formules mathématiques du format TeX vers le format MathML ou SVG. Publiée sous licence Apache. 

## Liens 
https://www.mathjax.org 
https://fr.wikipedia.org/wiki/MathJax 

## Comment 
Dans le fichier [HTML](HTML.md), penser à ajouter ceci. 

```html
<head>

	<!-- ... -->
	
    <script type="text/javascript" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <script>
	    window.MathJax = {
	    tex: {
	        inlineMath: [['$', '$'], ['(', ')']],
	        displayMath: [['$$', '$$'], ['[', ']']] 
	    },
	    options: {
	        skipHtmlTags: []
	    }
	    };
    </script>
	
	<!-- ... -->
	
</head>
```

Merci à Ilann (`ilo80`) sur le Discord du Club\*Nix. 


