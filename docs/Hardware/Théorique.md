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
### Modélisation 
Torseur d'action mécanique avec $i \in \{1,2,3,4\}$ : 
$$
F(\text{route} \to S_i) = 
\begin{Bmatrix}
	T_{ri} \cdot \vec{x} + N_{ri} \cdot \vec{z} 
	\\
	\vec0
\end{Bmatrix}_{I_{i}}
$$

Limite de roulement sans glissement : $T_{ri,\text{max}} = f \times N_{ri, \text{max}}$. 
$$
F(S \to S_i) = 
\begin{Bmatrix}
	X_i \cdot \vec{x} + Y_i \cdot \vec{y} + Z_i \cdot \vec{z} \\
	L_i \cdot \vec{x} + N_i \cdot \vec{z}
\end{Bmatrix}_{A_{i}}
$$


$$
F(S_{\text{moteur}_3}\to S_3) = 
\begin{Bmatrix}
	\vec{0} \\
	C_{m_3} \cdot \vec{y} 
\end{Bmatrix}_{A_{3}}
$$
$$
F(S_{\text{moteur}_4}\to S_4) = 
\begin{Bmatrix}
	\vec{0} \\
	C_{m_4} \cdot \vec{y} 
\end{Bmatrix}_{A_{4}}
$$



$$
F(P \to S) = 
\begin{Bmatrix}
	-mg\vec{z} \\
	\vec0 
\end{Bmatrix}_{G}
$$
Avec $i \in \{1,2\}$ : 
$$
F(S \to F_i) = 
\begin{Bmatrix}
	X_{F_i} \cdot \vec{x} + Y_{F_i} \cdot \vec{y} + Z_{F_i} \cdot \vec{z} \\
	L_{F_i} \cdot \vec{x} + M_{F_i} \cdot \vec{y}
\end{Bmatrix}_{A_{i}}
$$

$$
F(F_i \to S_i) = 
\begin{Bmatrix}
	X_{F_i S_i} \cdot \vec{x_i} + Y_{F_i S_i} \cdot \vec{y_i} + Z_{F_i S_i} \cdot \vec{z_i} \\
	L_{F_i S_i} \cdot \vec{x_i} + N_{F_i S_i} \cdot \vec{z_i}
\end{Bmatrix}_{A_{i}}
$$



PFD sur les roues arrières

$$\ {D}({S_i/R_0}) = \ {F}({S \rightarrow S_i)} + \ {F}{(\text{roue} \rightarrow S_i)} + \ {F} ({S_{rot_i}\rightarrow S_i)}$$

masse des roues négligeable $$\vec{D}_{S_i/R_0} = \begin{Bmatrix}
	 \vec{0} \\
	\vec{0}\\ \end{Bmatrix}_{\forall P}$$


$$
\vec{M}_{Ai}({\text{roue} \rightarrow S_i)} = \vec{M}_{I_i}({S_i \rightarrow S_i)} + \left( \overrightarrow{A_iI_i} \right) \wedge \vec{T}_{rix} + \vec{N}_{r_i} \vec{z}
$$

$$ = \vec{O} + ({-R}\vec{z})\wedge\vec{T}_{ri}\vec{x} = -R\vec{T}_{ri}\vec{y}
$$

On a alors
$$\begin{align}
X_3 + T_{r3} = 0 \quad (1) \\
Y_3 = 0 \quad (2) \\
Z_3 + N_{r3} = 0 \quad (3) \\
L_3 = 0 \quad  (4) \\
C_{m3} - R\,T_{r3} = 0 \quad  (5) \\
N_3 = 0 \quad  (6)
\end{align}
$$

Pareil pour $S_4$

----------------------------------------------------------------------
PFD sur la fusée

$$
\begin{align}
D(F_i/R_0) = {F}(_{\text{S}\rightarrow F_i}) + {F}(_{S_i \rightarrow F_i}) \\
= {F}(_{S \rightarrow F_i}) - {F}(_{F_i \rightarrow S_i}) \\
\end{align}
$$

![](attachments/Pasted%20image%2020250619132805.png)

On néglige la masse des moteurs (peut être abusif)

$$
\begin{align}
\vec{F}_{F_i \rightarrow S_i} =\ & 
\left(
X_{F_i/S_i} (\cos(\theta_i) \vec{x} + \sin(\theta_i) \vec{y}) 
+ Y_{R_{S_i}} \cos(\theta_i) \vec{j} 
+ Z_{R_{S_i}} \sin(\theta_i) \vec{k}
\right) \nonumber \\
& + L_{R_{S_i}} \vec{i} + N_{R_{S_i}} \vec{k} \tag{0} \\[2ex]
X_{F_i} - X_{R_{S_i}} \cos(\theta_i) + Y_{R_{S_i}} \sin(\theta_i) &= 0 \tag{1} \\
Y_{F_i} - Y_{R_{S_i}} \cos(\theta_i) - Z_{R_{S_i}} \cos(\theta_i) &= 0 \tag{2} \\
Z_{F_i} - Z_{R_{S_i}} &= 0 \tag{3} \\
L_{F_i} - L_{R_{S_i}} \cos(\theta_i) &= 0 \tag{4} \\
M_{F_i} - L_{R_{S_i}} \sin(\theta_i) &= 0 \tag{5} \\
N_{R_{S_i}} &= 0 \tag{6}
\end{align}
$$

$$
% Hypothèses : les moteurs avant sont négligés (inertie négligeable)

\[
\vec{D}(\vec{F}_{E/S_i}) = \vec{F}(E \to S_i) + \vec{F}(\text{roue} \to S_i)
\]

\[
\text{On se place au point } A_i
\]

\[
\vec{M}_{A_i}(\text{roue}/S_i) = \vec{M}_{A_i}(\text{roue}/S_i) + \vec{A}_i \wedge \left( \vec{T}_{n_i} \vec{i} + \vec{N}_{n_i} \vec{j} \right)
\]

\[
\vec{\delta} + \vec{R}_{n_i} \wedge \vec{T}_{n_i} = \vec{R}_{n_i} \vec{j}
\]

\begin{align}
X_{F_i/S_i} \cos(\theta_i) + Y_{F_i/S_i} \sin(\theta_i) + T_{n_i} &= 0 \tag{13} \\
X_{R_{S_i}} \sin(\theta_i) + Y_{F_i/S_i} \cos(\theta_i) &= 0 \tag{14} \\
2T_{n_i} + N_{n_i} &= 0 \tag{15} \\
4F_{S_i} \cos(\theta_i) &= 0 \tag{16} \\
L_{F_i/S_i} \sin(\theta_i) + R_{T_{n_i}} &= 0 \tag{17} \\
N_{F_i/S_i} &= 0 \tag{18}
\end{align}

$$

$$
% PFD : somme des forces et moments

\[
\vec{D}(\vec{S}/\vec{R_0}) = \vec{F}(\text{roue} \rightarrow S_i) 
+ \vec{F}(\text{roue}_2 \rightarrow S_i) 
+ \vec{F}(\text{roue}_3 \rightarrow S_i) 
+ \vec{F}(P \rightarrow S)
\]

\[
\vec{M}_{G_i}(\text{roue} \rightarrow S_i) 
= \vec{M}_{G_i}(\text{roue}/S_i) + \vec{G}_i \wedge \vec{F}(\text{roue} \rightarrow S_i)
\]

\[
= 
\left( x_{G_i} \vec{i} + y_{G_i} \vec{j} + z_{G_i} \vec{k} \right)
\wedge 
\left( T_{n_i} \vec{i} + N_{n_i} \vec{j} \right)
\]

\[
= -\sin(\theta_i) \delta g \vec{j} + \delta g \vec{j}
\quad \text{avec} \quad 
N_{n_i} = (x_{G_i} \vec{j} - y_{G_i} \vec{i})
\]

\begin{align}
T_{n_1} + T_{n_2} + T_{n_3} + T_{n_4} &= R_{\delta g} \tag{19} \\
0 &= R_{\delta g} \tag{20} \\
N_{n_1} + N_{n_2} + N_{n_3} + N_{n_4} &= mg = R_{\delta g} \tag{21} \\
y_{G_i}(N_{n_1} + N_{n_2} + N_{n_3} + N_{n_4}) &= \delta x \tag{22} \\
2\delta \left( T_{n_1} + T_{n_2} + T_{n_3} + T_{n_4} \right) 
\left( \frac{N_{n_1} + N_{n_2} + N_{n_3} + N_{n_4}}{4} \right) \delta x &= \delta g \tag{23} \\
- y_G (T_{n_1} + T_{n_2} + T_{n_3} + T_{n_4}) &= \delta g \tag{24}
\end{align}
$$

$$
\documentclass[12pt]{article}
\usepackage{amsmath,amssymb}
\usepackage{physics}
\usepackage{tcolorbox}
\usepackage[margin=2.5cm]{geometry}
\pagestyle{empty}

\begin{document}

\[
\text{On a avec les équations (16) et (17) :}
\]

\begin{align}
L_{F_{S_i}} \cos(\theta_i) &= 0 \quad \Rightarrow \quad L_{F_{S_i}} = 0 \quad \text{si } \cos(\theta_i) \ne 0 \tag{16} \\
L_{F_{S_i}} \sin(\theta_i) + R T_{n_i} &= 0 \quad \Rightarrow \quad T_{n_i} = 0 \quad \text{si } \sin(\theta_i) \ne 0 \tag{17}
\end{align}

\[
\text{Dans le cas } \theta_i = \dfrac{\pi}{2} \Rightarrow \cos(\theta_i) = 0, \ \sin(\theta_i) = 1
\]

\[
\Rightarrow L_{F_{S_i}} \sin(\theta_i) + R T_{n_i} = 0 \Rightarrow T_{n_i} = 0
\]

\begin{tcolorbox}[colback=blue!5, colframe=blue!75!black]
\[
T_{n_1} = 0, \quad T_{n_2} = 0
\]
\end{tcolorbox}

\vspace{1em}

\[
C_{m_i} = R T_{n_i} \Rightarrow T_{n_i} = \frac{C_{m_i}}{R} \tag{18}
\]

\[
\frac{C_{m_1}}{R} + \frac{C_{m_2}}{R} = R \delta x \tag{19}
\]

\[
\text{Pour obtenir } R_d
\]

\vspace{1em}

\[
\vec{R}_d = \dv{t} \left( R \vec{V}_{G/R} \right)_R 
= m \dv{t} \left( \vec{V}_{G/R} \right)_R
\]

\[
\vec{R}_d(S/R) = \dv{t} \left( \int_S \rho \vec{V}_{G/S} \, dV \right)_{R_0}
= m \dv{\vec{V}_{G/S}}{t}
\]

\begin{tcolorbox}[colback=green!5, colframe=green!60!black]
\[
6 \text{ ddl pour } \Sigma = 6 \text{ ddl pour } S 
\quad \text{car les autres masses sont négligées}
\]
\end{tcolorbox}

\end{document}
$$


$$
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

\section*{Cinématique - Vitesse}

\[
\vec{V}(G/S|R_0) = \vec{V}(G/S|R) + \vec{\omega}_{\Sigma/R} \wedge \vec{CG}
\]

\[
\vec{V}(G/S|R_0) = \frac{R}{2}(\omega_{S} + \omega_{SS}) \vec{j}_R + x_G \dot{\theta} \vec{i}_S + y_G \dot{\theta} \vec{j}_S + \omega_{SR_0} \wedge \vec{g}
\]

\[
= \frac{R}{2} (\omega_{S} + \omega_{SS} + \omega_{R}) \vec{j}_R - x_G \dot{\theta} \vec{j}_S + y_G \dot{\theta} \vec{i}_S
\]

Définitions :
\[
\vec{i}_S = \cos(\theta) \vec{i}_R - \sin(\theta) \vec{j}_R
\quad ; \quad
\vec{j}_S = \cos(\theta) \vec{j}_R + \sin(\theta) \vec{i}_R
\]

\[
= \frac{R}{2}(\omega_S + \omega_{SS} + \omega_R) \vec{j}_R + y_G \cos(\theta) \vec{j}_R - x_G \sin(\theta) \vec{j}_R
\]

\section*{Dérivée temporelle}

\[
\frac{d}{dt} \left( \vec{V}(G/S|R_0) \right)_{R_0}
= \frac{d}{dt} \left( \vec{V}(G/S|R) \right)_R
+ \vec{\omega}_{\Sigma/R_0} \wedge \vec{V}(G/S|R)
\]

\[
= \frac{R}{2} \dot{\omega}_S + \dot{\omega}_{SS}) \vec{j}_R + y_G \dot{\omega}_{SR_0} \vec{i}_S - x_G \dot{\omega}_{SR_0} \vec{j}_S
\]

\[
+ \omega_{SR_0} \wedge 
\left(
\frac{R}{2} (\omega_S + \omega_{SS}) \vec{j}_R + y_G \vec{i}_S - x_G \vec{j}_S
\right)
\]

\end{document}
$$

$$
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

\section*{Cours — Accélération}

\[
\vec{R}_d = \left[ \frac{d}{dt} \vec{V}(G/R_0) \right]_R - m \left[ \frac{d}{dt} \vec{V}(G/R_0) \right]
\]

\[
= m \left[ \frac{d}{dt} \vec{V}(G/S,R) \right]_R
\]

---

\[
\vec{V}(G/S,R_0) = \vec{V}(G/S,R) + \vec{GR} \wedge \vec{\omega}_{S/R_0}
\]

\[
\vec{GR} = x_G \vec{i}_S + y_G \vec{j}_S + z_G \vec{k}_S
\quad \Rightarrow \quad \vec{GR} = \vec{GO}
\]

\[
= \vec{V}(G/S,R) + \vec{\omega}_{S/R_0} \wedge (x_G \vec{i}_S + y_G \vec{j}_S)
\]

---

\[
\frac{d}{dt} \vec{V}(G/S,R_0) = \left[ \frac{d}{dt} \vec{V}(G/S,R) \right]_S + \vec{\omega}_{S/R_0} \wedge \vec{V}(G/S,R)
\]

Développement :

\[
= \vec{V}(G/S,R) + \dot{\vec{\omega}}_{S/R_0} \wedge (x_G \vec{i}_S + y_G \vec{j}_S)
\]

\[
+ \vec{\omega}_{S/R_0} \wedge \left( \vec{V}(G/S,R) - \vec{\omega}_{S/R_0} \wedge (x_G \vec{i}_S + y_G \vec{j}_S) \right)
\]

---

\subsection*{Simplification finale}

\[
\vec{V}(G/S,R_0) = \vec{V}(G/S,R) + \vec{\omega}_{S/R_0} \wedge \vec{GR}
\]

En dérivant, on obtient l'accél

$$

$$
\documentclass{article}
\usepackage{amsmath, tikz}
\usepackage{geometry}
\geometry{margin=2cm}

\begin{document}

\section*{Relation de vitesse entre deux points d’un solide}

\vspace{0.5cm}

\[
\vec{V}_{A_1/S|R_0} - \vec{V}_{A_3/S|R_0} = R \, \omega_{SS} - R \, \omega_{S3}
\]

---

\section*{Schéma cinématique}

\begin{center}
\begin{tikzpicture}[scale=1]
  % Roues
  \draw[thick] (-2,1) circle(0.3);
  \draw[thick] (2,1) circle(0.3);

  \node at (-2,1.5) {$\odot$};
  \node at (2,1.5) {$\odot$};

  % Châssis
  \draw[thick] (-2.5,0.7) -- (2.5,0.7);
  \draw[thick] (-2.5,0.7) -- (-2.5,0.2);
  \draw[thick] (2.5,0.7) -- (2.5,0.2);
  \draw[thick] (-2.5,0.2) -- (2.5,0.2);

  % Axe central
  \draw[thick] (0,0.2) -- (0,-1);
  \node at (0,-1.3) {Châssis};

  % Vitesse
  \node at (2,1.8) {$-2V$};
\end{tikzpicture}
\end{center}

---

\section*{Repère}

\begin{center}
\begin{tikzpicture}[scale=1]
  % Repère
  \draw[->] (0,0) -- (3,0) node[anchor=west] {$\vec{i}_S$};
  \draw[->] (0,0) -- (0,2) node[anchor=south] {$\vec{j}_S$};

  % Point A et C
  \node at (1.5,0) {C};
  \node at (0,-0.2) {A};

  % Vecteur R
  \node at (1,-0.5) {$R$};
\end{tikzpicture}
\end{center}

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Équations dynamiques}

\[
\Rightarrow \quad \frac{C_{m1}}{R} + \frac{C_{m2}}{R} - m \omega_{SR_0}^2 x_G^1
\]

\[
\Rightarrow \quad C_{m1} + C_{m2} = \frac{R}{m} x_G^1 \omega_{SR_0}^2 + m \left( \frac{R}{2} (\dot{\omega}_{S1S} + \dot{\omega}_{S3}) + \dot{y}_G \dot{\omega}_{SR_0} \right)
\]

---

\section*{Modèle moteur}

\[
\text{moteur :}
\begin{cases}
0 = E + R_e I \\
C_m = K_I I \\
E = K_E \omega_{S1S}
\end{cases}
\]

En remplaçant :

\[
I = \frac{U - K_E \omega_{S1S}}{R_e}
\]

---

\section*{Couple moteur}

\[
C_{m1} + C_{m2} = K_I \left( \frac{U - K_E \o

$$

$$
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Expression finale de la tension}

\[
\frac{K}{R_e} \left( U_e - 2 K_E \omega \right) = \frac{R}{m} \left( x_G^1 \omega_{SR_0}^2 + \frac{R}{2} \dot{\omega} + y_G \dot{\omega} \right)
\]

\bigskip

En isolant \( U_e \) :

\[
U_e = \frac{R_e R m}{K} \left( x_G^1 \omega_{SR_0}^2 + \frac{R}{2} \dot{\omega} + y_G \dot{\omega} \right) + 2 K_E \omega
\]

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Étude dynamique selon \( x \)}

Cas particuliers : \( \omega = 0 \) et \( \dot{\omega} = 0 \)

\[
C_{m3} + C_{m1} = m R \dot{V}
\]

---

\section*{Puissance}

\[
P = C_m \cdot \omega_m
\]

\[
\frac{P_{wm_3}}{\omega_{m_3}} + \frac{P_{wm_1}}{\omega_{m_1}} = m R \dot{V}
\]

---

\[
\frac{2P}{R (\omega_{m_3} + \omega_{m_1})} = m R \dot{V}
\]

---

\section*{Relations entre vitesses}

Si \( \omega = 0 \Rightarrow \dot{\theta} = \frac{R}{2L} (\omega_{m_3} - \omega_{m_1}) \Rightarrow \omega_{m_3} = \omega_{m_1} = \omega_m \)

\[
V = \frac{R}{2} (\omega_{m_3} + \omega_{m_1}) \Rightarrow V = R \omega_m
\Rightarrow V^2 = R^2 \omega_m^2
\]

---

\[
\frac{2P}{R \omega_m} = m R \dot{V} \Rightarrow \frac{2P}{R^2 \omega_m} = m \dot{V}
\Rightarrow \frac{2P}{V} = m \dot{V}
\]

---

\section*{Accélération}

\[
\Rightarrow \dot{V} = \frac{2P}{m V}
\Rightarrow \ddot{x} = \frac{2P}{m V}
\]

---

\textbf{Remarques :}

- Les dernières lignes semblent montrer une comparaison entre différentes expressions de masse \( m \lambda^2 \), avec des tests numériques.
- Dessins en bas de page : non pertinents pour transcription LaTeX.

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Modèle électrique du moteur à courant continu}

\[
C = K_I i \qquad \text{(couple)}
\]
\[
E = K_E \omega \qquad \text{(force contre-électromotrice)}
\]

\[
U = R i + E
\]

---

\subsection*{Cas où la tension \( U \) est constante}

\[
U = R i + E = R i + K_E \omega
\Rightarrow i = \frac{U - K_E \omega}{R}
\]

\[
C = K_I i = \frac{K_I}{R}(U - K_E \omega)
\]

---

\subsection*{Remarques pratiques}

- Lorsqu'on utilise un hacheur (PWM), on applique une tension moyenne \( U = \alpha U_{\text{max}} \) (modulation en largeur d'impulsion).
- On se place dans le cas \( U \) constant, car ce n’est pas \( U \) qui varie, mais \( \alpha \).

---

\subsection*{Forme simplifiée du couple}

\[
C(\omega) = \frac{K_I U}{R} \left(1 - \frac{K_E}{U} \omega \right)
\]

On pose :
\[
\alpha = \frac{K_I U}{R}, \quad \beta = \frac{K_I K_E}{R}
\Rightarrow
C(\omega) = \alpha (1 - \delta \omega)
\]

---

\end{document}

$$


$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Détermination de \(\alpha\) et \(\delta\) dans la caractéristique \(C(\omega)\)}

\subsection*{Hypothèses}

- On sait que lorsque le moteur est bloqué, il exerce son \textbf{couple maximum} :
\[
C(0) = \alpha (1 - \delta \cdot 0) = \alpha = C_{\text{max}}
\]

- On sait aussi que lorsque \(\omega = \omega_{\text{max}}\), le moteur tourne à vide donc :
\[
C(\omega_{\text{max}}) = 0
\]

---

\subsection*{Détermination de \(\delta\)}

\[
C(\omega_{\text{max}}) = \alpha (1 - \delta \omega_{\text{max}}) = 0
\Rightarrow 1 - \delta \omega_{\text{max}} = 0
\Rightarrow \delta = \frac{1}{\omega_{\text{max}}}
\]

---

\subsection*{Formule finale du couple moteur}

\[
C(\omega) = C_{\text{max}} \left(1 - \frac{\omega}{\omega_{\text{max}}} \right)
\]

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Équation différentielle complète}

On part de l'équation :

\[
0 = \dot{V} - \frac{2 C_{\text{max}}}{R} V - y_G \dot{\omega} - \frac{x_G}{2} \omega^2 + \frac{2 C_{\text{max}} (x_G + \alpha_1)}{R m}
\]

---

On pose :

\[
\dot{\omega}_{m1} = \dot{\omega}_{m2} = \dot{\omega}_m, \quad \omega_{m1} = \omega_{m2} = \omega_m
\]

---

Développement :

\[
0 = \frac{R}{2} (\lambda + 1) \dot{\omega}_m 
- \frac{R^2 C_{\text{max}}}{R^2 \omega_{\text{max}} m} 
+ \frac{R}{2} \lambda \dot{\omega}_m 
+ x_G \left( \frac{1 - \lambda}{2} \omega_m^2 \right) 
- \frac{2 C_{\text{max}} (1 + \lambda) \alpha}{R m}
\]

---

\subsection*{Regroupement des termes}

\subsubsection*{Termes en \( \dot{\omega}_m \)}

\[
\frac{R}{2} \lambda \dot{\omega}_m + \frac{R}{2} (1 + \lambda) \dot{\omega}_m + y_G \frac{R}{2} \dot{\omega}_m = a
\]

---

\subsubsection*{Termes en \( \omega_m \)}

\[
\frac{R}{2} (1 + \lambda) y_G - \frac{R}{2} (1 - \lambda) x_G = \left( \text{second membre} \right)
\]

---

\subsubsection*{Termes en \( \omega_m^2 \)}

\[
x_G \frac{1 - \lambda}{2} = b
\]

---

\subsubsection*{Terme constant}

\[
- \frac{2 C_{\text{max}} (1 + \lambda) \alpha}{R m} = d
\]

---

\end{document}

$$


$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Conditions sur la vitesse et l'accélération}

Il faut des conditions pour la vitesse et l’accélération.

\[
\omega = \dot{\theta} - c
\]

On aboutit à une équation de la forme :

\[
0 = \dot{V} + \frac{2 C_{\text{max}}}{R \, \omega_{\text{max}}} V + \frac{2 C_{\text{max}}}{m}
\]

\end{document}

$$


$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Relation dynamique selon \( x \)}

Selon \( x \), on a :

\[
C_{m3} + C_{m1} = R m \left( \dot{V} - \dot{\omega} y_G - \omega^2 x_G \right)
\]

---

\subsection*{Modèle du couple moteur}

On suppose que les couples moteurs sont égaux :

\[
C_{m3} = C_{m1} = C_m = C_{\text{max}} \left( 1 - \frac{\omega_{m3}}{\omega_{\text{max}}} \right)
\]

Comme \( \omega_{m3} = \omega_{m4} = \omega_m \), on a :

\[
C_{m3} + C_{m1} = 2 C_{\text{max}} \left( 1 - \frac{\omega_m}{\omega_{\text{max}}} \right)
\]

---

\subsection*{Expression de \( \omega_m \)}

\[
\omega_m = \frac{V}{R}
\Rightarrow \frac{\omega_m}{\omega_{\text{max}}} = \frac{V}{R \omega_{\text{max}}}
\]

Donc :

\[
C_{m3} + C_{m1} = 2 C_{\text{max}} \left( 1 - \frac{V}{R \omega_{\text{max}}} \right)
\]

---

\subsection*{Équation finale}

\[
0 = \dot{V} + \frac{2 C_{\text{max}}}{R^2 \omega_{\text{max}} m} V - \dot{\omega} y_G - \omega^2 x_G - \frac{C_{\text{max}} (x_G + \alpha)}{R m}
\]

\end{document}
$$


$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Résolution de l'équation différentielle}

Variables : \( \dot{\omega}_m, \dot{V}, \omega_m, V \)

\[
0 = \frac{R}{2} \dot{\omega}_m (\omega_{m1} + \omega_{m2})
+ \frac{2 C_{\text{max}}}{R^2 \omega_{\text{max}} m} (\omega_{m1} + \omega_{m2})
- \frac{R}{2} \dot{\omega}_m (\omega_{m1} - \omega_{m2})
- \frac{R^2}{2} x_G (\omega_{m1} - \omega_{m2})^2
- \frac{2 C_{\text{max}} (x_G + \alpha)}{R m}
\]

---

\subsection*{Cas particuliers}

Si :
\[
\omega_{m3} = \alpha_2 \omega_{\text{max}}, \quad \omega_{m1} = \alpha_1 \omega_{\text{max}}
\]

Alors :
\[
\omega_{m1} + \omega_{m2} = (\alpha_1 + \alpha_2) \omega_{\text{max}}, \quad
\omega_{m1} - \omega_{m2} = (\alpha_1 - \alpha_2) \omega_{\text{max}}
\]

---

\subsection*{Changement de variable}

On note :

- \( \omega_{m1} = w \)
- \( C_{\text{max}} = C \)
- \( \omega_{\text{max}} = W \)
- \( R = A \)
- \( \theta = \delta \)
- \( B(\omega) = f(\alpha) \)
- \( B(\omega = 0) = D \)

---

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Résolution d’une équation différentielle}

On considère l'équation :

\[
0 = a \ddot{y} + b \dot{y} + c y^2 + d \quad \text{avec} \quad y = \omega_m
\]

---

\subsection*{Recherche d'une solution particulière constante}

On cherche \( y = k \) qui annule l'équation différentielle :

\[
0 = a \cdot 0 + b \cdot 0 + c k^2 + d \Rightarrow c k^2 + d = 0
\]

On suppose que le discriminant est positif :

\[
\Delta = b^2 - 4ac \geq 0
\Rightarrow k = \frac{-b \pm \sqrt{b^2 - 4ac}}{2c}
\]

---

\subsection*{Méthode : changement de variable}

On pose :
\[
y = z \quad ; \quad y' = z' \quad ; \quad y'' = z''
\]

On injecte dans l'équation initiale :

\[
0 = a z'' + b z' + c z^2 + d
\Rightarrow 0 = a z'' + (b + 2c k) z' + c z^2
\]

---

\subsection*{Équation de Bernoulli (ordre 2)}

Équation obtenue :

\[
z'' + (b + 2 c k) z' + \frac{c}{a} z^2 = 0
\]

On pose \( z' = \frac{1}{h} \Rightarrow z = \frac{1}{h'} \Rightarrow z'' = - \frac{h'}{h^2} \)

On remplace dans l’équation :

\[
0 = -a \frac{h'}{h^2} + (b + 2 c k) \cdot \frac{1}{h} + \frac{c}{a}
\]

\[
\Rightarrow 0 = -a h' + (b + 2 c k) h + \frac{c}{h}
\]

---

\end{document}

$$


$$
\documentclass{article}
\usepackage{amsmath}
\usepackage[french]{babel}
\begin{document}

\section*{Résolution de l'équation en \( h(x) \)}

On suppose une solution de la forme :

\[
h(x) = A e^{\beta x} + C
\]

---

\subsection*{Identification des termes}

On remplace dans l’équation différentielle :

\[
0 = -a \beta e^{\beta x} + (b + 2 c k) A \beta e^{\beta x} + C + (-C)
\]

On regroupe les termes semblables. On identifie :

\[
0 = -a A \beta e^{\beta x} + (b + 2 c k) A e^{\beta x}
\]

On en déduit :

\[
\beta = \frac{b + 2 c k}{a}
\quad \Rightarrow \quad
h(x) = A e^{\frac{(b + 2 c k)}{a} x} - C
\]

---

\subsection*{Retour à la variable \( y \)}

Rappel : \( y = \frac{1}{h} \)

\[
y(x) = \frac{1}{A e^{\beta x} - C}
\]

---

\subsection*{Condition initiale}

Si on a \( y(0) = \omega_0 \), alors :

\[
\omega_0 = \frac{1}{A - C} \Rightarrow A = \frac{1}{\omega_0} + C
\]

---

\subsection*{Solution finale}

\[
y(x) = \frac{1}{\left(\frac{1}{\omega_0} + C \right) e^{\beta x} - C}
\]

---

\end{document}

$$

$$
\documentclass{article}
\usepackage{amsmath}
\begin{document}

\section*{Développement de la solution exponentielle}

On étudie l’expression complète issue de :

\[
y(x) = \frac{1}{A e^{\beta x} - C}
\]

On en déduit :

\[
y' = -\frac{A \beta e^{\beta x}}{(A e^{\beta x} - C)^2}, \quad
y'' = \frac{A^2 \beta^2 e^{2\beta x} - A \beta^2 C e^{\beta x}}{(A e^{\beta x} - C)^3}
\]

---

On remplace dans l’équation différentielle de départ :

\[
a y'' + b y' + c y^2 + d = 0
\]

\[
a \cdot \left( \text{expression de } y'' \right)
+ b \cdot \left( \text{expression de } y' \right)
+ c \cdot \left( \frac{1}{(A e^{\beta x} - C)^2} \right)
+ d = 0
\]

---

On factorise les puissances de \( e^{\beta x} \) :

\[
y = \frac{1}{A e^{\beta x} - C}
\Rightarrow \text{toutes les dérivées sont exprimées comme fractions en } e^{\beta x}
\]

---

\subsection*{Objectif}

Montrer que tous les termes s’annulent :

\[
-a \cdot \frac{A \beta^2 e^{\beta x}}{(A e^{\beta x} - C)^2}
+ b \cdot \left( \ldots \right)
+ c \cdot \left( \ldots \right)
= 0
\]

Cela confirme que :

\[
y(x) = \frac{1}{A e^{\beta x} - C}
\quad \text{est bien solution de l’équation.}
\]

---

\end{document}

$$

