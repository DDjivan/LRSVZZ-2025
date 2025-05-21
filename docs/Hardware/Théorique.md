# Théorique 
On veut : 
- dimensionner le moteur 
- dimensionner la batterie 
- rendre le système stable 

## Cinématique 
### Modélisation 
On cherche la relation entre la vitesse de rotation des roues et la vitesse du robot et sa vitesse de rotation par rapport au sol. 

![](attachments/schéma_modélisation.jpg)

$S$ est le châssis 
$R_0$ est le référentiel terrestre 
$S_i$ est la roue n°i (il y en a quatre) 
$F_i$ est la fusée n°i (il y en a deux) 

$A_i$ est un point qui représente le point de contact entre la roue n°$i$ et le sol 
$R$ est le rayon de la roue 
$\omega$ est la vitesse de rotation 

$\vec{x},\vec{y},\vec{z} \in S$ 
$\vec{x_0},\vec{y_0},\vec{z_0} \in S_0$ 
$\vec{x_1},\vec{y_1},\vec{z_1} \in F_1$ 
$\vec{x_2},\vec{y_2},\vec{z_2} \in F_2$ 
$S_1$ et $S_2$ sont respectivement confondues avec $F_1$ et $F_2$ 
$S_4$ et $S_3$ sont confondues avec $S$ 

Condition de roulement sans glissement : 
$$\vec{V}(A_4, S/R_0) = R\omega_{S_4/S} \cdot \vec{x} \tag{1}$$
$$\vec{V}(A_3, S/R_0)=R\omega_{S_3/S} \cdot \vec{x} \tag{2}$$

Rotation d'une roue par rapport à $R_0$, obtenu par composition des vitesses de rotation. 
$$\vec{\Omega}(S_3/R_0) = \omega_{S_3/S} \cdot \vec{y} + \omega_{S/R_0} \cdot \vec{z} \tag{3}$$
$$\vec{\Omega}(S_4/R_0) = \omega_{S_4/S} \cdot \vec{y} + \omega_{S/R_0} \cdot \vec{z} \tag{4}$$

### Étape 1 
Relation entre vitesse de rotation des roues et la vitesse du châssis. 
$$
R\omega_{S_4/S} \cdot \vec{x} + R\omega_{S_3/S} \cdot \vec{x}
=
\vec{V}(A_4, S/R_0) + \vec{V}(A_3, S/R_0) 
\tag{1)+(2}
$$

Changement de point en $C$. 
$$ = 
\vec{V}(C,S/R_0) 
+ \overrightarrow{A_{4}C} \wedge \vec{\Omega}(S/R_0) 
+ \vec{V}(C,S/R_0) 
+ \overrightarrow{A_{3}C} \wedge \vec{\Omega}(S/R_0) 
$$
$$
= 2\vec{V}(C,S/R_0) + (-\frac{L}{2} + \frac{L}{2}) \cdot \vec{y} \wedge \omega_{S/R_0} \cdot \vec{y}
$$
Donc selon $x$, on a : 
$$
\boxed{
	\vec{V}(C,S/R_0) = \frac{R}{2}\bigg( \omega_{S_4/S} + \omega_{S_3/S} \bigg)
}
$$
### Étape 2 
Relation entre vitesse de rotation des roues et la **vitesse de rotation** du châssis. 
$$
R\omega_{S_4/S} \cdot \vec{x} - R\omega_{S_3/S} \cdot \vec{x}
=
\vec{V}(A_4, S/R_0) - \vec{V}(A_3, S/R_0) 
\tag{1)–(2}
$$

Changement de point en $I$, point sur l'axe de rotation du châssis par rapport au sol : $(I,\vec{z})$. 
$$= 
\vec{V}(I, S/R_0) + \overrightarrow{A_4 I} \wedge \vec{\Omega}(S/R_0) 
- \bigg(\vec{V}(I, S/R_0) + \overrightarrow{A_3 I} \wedge \vec{\Omega}(S/R_0) \bigg)
$$
$I$ centre de l'axe de rotation donc $\vec{V}(I, S/R_0) = \vec0$
On a alors : 
$$
= \overrightarrow{A_4 I} \wedge \vec{\Omega}(S/R_0) 
- \bigg( \overrightarrow{A_3 I} \wedge \vec{\Omega}(S/R_0) \bigg)$$
On décompose avec la relation de Chasles : 
$$
= 
\bigg(\overrightarrow{A_4 I_4}+\overrightarrow{I_4 I} \bigg)
\wedge \vec{\Omega}(S/R_0) 
- 
\Bigg( 
	\bigg(
		\overrightarrow{A_3 I_3} 
		+ \overrightarrow{I_3 I_4} 
		+ \overrightarrow{I_4 I}
	\bigg) 
	\wedge \vec{\Omega}(S/R_0) 
\Bigg)
$$

$$
= 
\bigg( -R\vec{z}+\overrightarrow{I_4 I} \bigg)
\wedge {\omega}_{S/R_0} \cdot \vec{z} 
- 
\Bigg( 
	\bigg( 
		-R\vec{z} + L\vec{y} +\overrightarrow{I_4I}
	\bigg) 
	\wedge {\omega}_{S/R_0} \cdot \vec{z}  
\Bigg)
$$

$$
= 
- 
\Bigg( 
	\bigg( 
		L\vec{y} 
	\bigg) 
	\wedge {\omega}_{S/R_0} \cdot \vec{z}  
\Bigg)
$$

$$
= 
- 
\Bigg( 
	\bigg( 
		L
	\bigg) 
	{\omega}_{S/R_0}
	\cdot \vec{x}
\Bigg)
$$

Donc : 
$$
R\omega_{S_4/S} \cdot \vec{x} - R\omega_{S_3/S} \cdot \vec{x}
=
-L {\omega}_{S/R_0} \cdot \vec{x}
$$

Selon $\vec{x}$ : 
$$
R\omega_{S_4/S} - R\omega_{S_3/S} 
=
-L {\omega}_{S/R_0} 
$$

Donc : 
$$
\boxed{
	\omega_{S_3/S} - \omega_{S_4/S} 
	=
	\frac{L}{R} {\omega}_{S/R_0}
}
$$

Fin de la cinématique. 

## Dynamique 


