# LaTeX 
Un langage. 

> LaTeX permet de rédiger des documents dont la mise en page est réalisée automatiquement en se conformant du mieux possible à des normes typographiques. Une fonctionnalité distinctive de LaTeX est son mode mathématique, qui permet de composer des formules complexes.
> 
> LaTeX est particulièrement utilisé dans les domaines techniques et scientifiques pour la production de documents de taille moyenne (tels que des articles) ou importante (thèses ou livres, par exemple). Néanmoins, il peut être employé pour générer des documents de types très variés (lettres ou transparents, par exemple). Enfin, de nombreux sites Internet — dont le texte est typiquement mis en forme par d’autres moyens — emploient un sous-ensemble de LaTeX pour composer notamment leurs formules mathématiques. 


## Liens 
https://fr.wikipedia.org/wiki/LaTeX 
https://www.latex-project.org/about/ 

### ==Ressources super utiles== 
Pour comprendre le principe : https://courses.cs.washington.edu/courses/cse311/17sp/latex/cheatsheet.pdf 

Une liste des caractères : https://quickref.me/latex 

Pour comprendre la réalisation d'un document : https://fg.informatik.uni-goettingen.de/file/latex-cheatsheet.pdf 

## Comment 
Un logiciel comme TeXstudio permet de facilement générer des PDF. 
Mais le fichier dans lequel il faut écrire (`.tex`) est juste du texte en clair, donc n'importe quel éditeur de texte fait l'affaire. 

Pour afficher des équations LaTeX sur une page web, utiliser [[MathJax]]. 

## Syntaxe Document 
==Uniquement pour les fichiers (`.tex`) !== 

Pour les titres : `\section{NOM}` 
Pour les sous-titres : `\subsection{NOM}` 
Pour les sous-sous-titres : `\subsubsection{NOM}` 

Ces derniers seront automatiquement présents dans la table des matières. 

Texte en évidence : `\emph{TEXTE_texte}` 
Texte en italique : `\textit{TEXTE_texte}` 
Texte en gras : `\textbf{TEXTE_texte}` 

> [!tip] Quelle différence ? 
> La commande `\emph{}` est utilisée **pour mettre en évidence du texte** (généralement en l'affichant en italique), alors que `\textit{}` place directement le texte en italique. 

Pour insérer une image ou un fichier PDF, il est conseillé d'utiliser une `figure`. 

```latex
\begin{figure}[H]
	\centering % centre 
	\includegraphics[width=LONGUEUR\textwidth]{CHEMIN_DU_FICHIER}
	\caption{DESCRIPTION}
\end{figure}
```

Afin que l'image soit adaptée à la taille de la page, `LONGUEUR` est idéalement une valeur entre 0 et 1 (qui sera multipliée par la longueur de la page). 

Pour les listes : 
```latex
\begin{STYLE_DE_LISTE}
	\item PREMIER ITEM 
	\item DEUXIÈME ITEM % ...
\end{STYLE_DE_LISTE}
```

Exemples de styles de liste : 
- à tiret : `itemize` 
- numérotées : `enumerate` 
- ... 

## Syntaxe Mathématiques 
À encadrer soit par une paire de dollars, soit une paire de double dollars. 
Donc soit `$équation$`, soit `$$équation centrée et grande et sur plusieurs lignes$$`. 

Indice : `_` 
Exposant : `^`  

Besoin de plus d'un caractère en indice/exposant ? Les mettre entre accolades. 
Exemple : `2^{x+1}` -> $2^{x+1}$ 

Ne jamais hésiter à mettre des groupes de caractères entre des accolades. Il vaut mieux en avoir trop que pas suffisamment. 

Fractions : `\frac{EN_HAUT}{EN_BAS}` 

Mettre du texte (pour les unités, "si ...", "donc...", etc.) : `\mathrm{TEXTE}` 
Espacer : `\,`, `\;`, `\quad`... 

Voir les ressources utiles de cette note ou les exemples déjà présents ([Théorique](../Hardware/Théorique.md)) pour des styles plus avancés. 

### TeXstudio 
[Flatpak](appstream:org.texstudio.TeXstudio) (le plus simple) 

Penser à installer les packages et outil LaTeX avec la commande suivante. 
```bash
flatpak install flathub org.freedesktop.Sdk.Extension.texlive//24.08
```

[Site officiel](https://www.texstudio.org/) 



