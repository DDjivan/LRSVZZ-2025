# Markdown 
C'est un "langage de programmation". 
C'est lisible même sans un éditeur de texte comme [Obsidian](docs/Guides/Obsidian.md). 

Il a de nombreuses bibliothèques permettant de le convertir au format [HTML](HTML.md). Dans le cadre de notre projet, voir [Bibliothèque Python](#Bibliothèque%20Python).  

## Liens 
https://daringfireball.net/projects/markdown/ 
https://fr.wikipedia.org/wiki/Markdown 
https://www.markdownguide.org/ 

## Syntaxe 
### Modifier le texte en l'entourant de caractères 
**Italique** -> astérisque : `*texte*` 
**Gras** -> double astérisque : `**texte**` 
**Barré** -> double tilde (`ALT GR + é`) : `~~texte~~` 

**Code** -> backtick (`ALT GR + è`) : \`texte\` 

**Bloc de code** -> triple backticks : 
\`\`\`
code
\`\`\`
qui devient : 
```
code
```

**Bloc de code avec couleurs** -> triple backticks avec langage : 
\`\`\`python
def print(arg) : return "texte"  # comment 
\`\`\`
qui devient : 
```python
def print(arg) : return "texte"  # comment 
```

**Surligner** -> double égal : `==texte==` 

### Modifier le texte en ajoutant un caractère au début 
Titre -> croisillon / hashtag puis espace : `# texte` 
Sous-titre, sous-sous-tire... -> plusieurs croisillons : `## texte` 

Citation -> plus grand que puis espace : `> texte` 

Liste -> tiret espace : `- texte`
Liste numérotée -> nombre point espace : `1. texte ` 



## Syntaxe spécifique à Obsidian 
Ne vraiment pas hésiter à lire la documentation d'usage : 
![](Obsidian.md#^Documentation) 

Obsidian utilise beaucoup les références. 
Références à des fichiers -> doubles crochets : `[[note.md]]`. 
Références à un document -> crochet puis parenthèse : `[texte](https://lien)`

Ajouter un point d'exclamation `!` au début d'une référence permet de la transformer en aperçu (embed). 
https://help.obsidian.md/embeds 


## Bibliothèque Python 
Il y a deux bibliothèques qui permettent de convertir du contenu Markdown en [HTML](HTML.md). 

- `markdown` 
- `markdown2` 

Pour prendre en charge [MathJax](MathJax), un outil qui affiche des équations [[LaTeX]], penser à utiliser la fonction `markdown`, tel que l'exemple suivant. 

```python
html_data = markdown(DATA, extensions=['tables', 'footnotes', 'fenced_code', 'breaks', 'mdx_math', 'code-friendly'])
```


