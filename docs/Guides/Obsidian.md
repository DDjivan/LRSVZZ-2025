# Obsidian 
Obsidian est un logiciel gratuit mais pas open source, disponible sur toutes les plateformes (Linux, Windows, même iOS). 

## Liens 
- Site officiel : https://obsidian.md/ 
- Documentation très sympathique : https://help.obsidian.md/ ^Documentation
- Linux (Flatpak) : https://flathub.org/apps/md.obsidian.Obsidian ^Linux
- Installateurs dont celui pour Windows (`.exe`) : https://github.com/obsidianmd/obsidian-releases/releases/latest/ ^Windows

- Documentation pour les développeurs : https://docs.obsidian.md/Home 

## En bref 
C'est un éditeur de texte au format [About/Guides/Markdown](About/Guides/Markdown). 
Il fonctionne en "Vault" : c’est tout simplement un **dossier sur ton ordinateur** qui contient tes notes en **fichiers Markdown** 

Tous les fichiers sont sur le repo [GitHub](docs/Guides/GitHub.md). 

## Pourquoi 
Application légère et rapide, sous [[Electron]]/[[Chromium]] ce qui lui permet d'être sur n'importe quel système d'exploitation pour bureau. 
Elle est personnalisable, possède des plugins et une [[API]], qui la rend versatile et puissante. 
Son interface est également intuitive et jolie. 
Étant donné que les notes sont au format [Markdown](docs/Guides/Markdown.md), les modifications sont visibles dans le repo et ses commits. 

Alternatives : 
- Microsoft Word : ne permet pas le versioning, propriétaire 
- Joplin 
- ==se renseigner== 

## Problèmes 
### Export PDF 
L'export PDF n'est pas agréable à lire, surtout dans le cas de [Guide espace de travail](docs/Guides/Guide%20espace%20de%20travail.md). 
Le problème ? Les images étaient régulièrement sur la page suivante, le texte pertinent n'était donc pas proche. 

La première solution a été de créer un snippet CSS afin de créer des règles pour les titres, images, embed et paragraphes. Ces snippets sont placés ici : `.obsidian/snippets/`. Toutefois, ils semblent être limités, et ne conviennent pas pour la tâche. (idéalement, il faudrait un saut de page avant chaque titre, sauf si avant le titre, il y a un autre titre)

La deuxième solution (qui est actuellement utilisée) est simplement d'ajouter des sauts de pages manuels, en insérant le texte HTML suivant dans une note : 
```html
<div style="page-break-after: always;"></div>

```
Bien penser à garder une ligne vide après avoir inséré cette ligne de texte. 
