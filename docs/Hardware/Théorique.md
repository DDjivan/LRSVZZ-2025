# Théorique 
On veut : 

- dimensionner le moteur 
- dimensionner la batterie 
- rendre le système stable 

## Cinématique 
### Modélisation 
On cherche la relation entre la vitesse de rotation des roues et la vitesse du robot et sa vitesse de rotation par rapport au sol. 

![schéma_modélisation.jpg](attachments/schéma_modélisation.jpg)

Un 

- $S$ est le châssis 
- $R_0$ est le référentiel terrestre 
- $S_i$ est la roue n°i (il y en a quatre) 
- $F_i$ est la fusée n°i (il y en a deux) 

Deux 

- $A_i$ est un point qui représente le point de contact entre la roue n°$i$ et le sol 
- $R$ est le rayon de la roue 
- $\omega$ est la vitesse de rotation 

Trois 

- $\vec{x},\vec{y},\vec{z} \in S$ 
- $\vec{x_0}, \vec{y_0}, \vec{z_0} \in S_0$ 
- $\vec{x_1},\vec{y_1},\vec{z_1} \in F_1$ 
- $\vec{x_2},\vec{y_2},\vec{z_2} \in F_2$ 
- $S_1$ et $S_2$ sont respectivement confondues avec $F_1$ et $F_2$ 
- $S_4$ et $S_3$ sont confondues avec $S$ 

Condition de roulement sans glissement : 
$$
\vec{V}(A_4, S/R_0) = R\omega_{S_4/S} \cdot \vec{x} \tag{1}
$$

$$
\vec{V}(A_3, S/R_0)=R\omega_{S_3/S} \cdot \vec{x} \tag{2}
$$

Rotation d'une roue par rapport à $R_0$, obtenu par composition des vitesses de rotation. 
$$\vec{\Omega}(S_3/R_0) = \omega_{S_3/S} \cdot \vec{y} + \omega_{S/R_0} \cdot \vec{z} \tag{3}$$
$$\vec{\Omega}(S_4/R_0) = \omega_{S_4/S} \cdot \vec{y} + \omega_{S/R_0} \cdot \vec{z} \tag{4}$$

### Étape 1 

Relation entre vitesse de rotation des roues et la vitesse du châssis. 

$$
R\omega_{S_4/S} \cdot \vec{x} + R\omega_{S_3/S} \cdot \vec{x} =
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
R\omega_{S_4/S} \cdot \vec{x} - R\omega_{S_3/S} \cdot \vec{x} =
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
= \bigg(\overrightarrow{A_4 I_4}+\overrightarrow{I_4 I} \bigg)
\wedge \vec{\Omega}(S/R_0) 
- \Bigg( 
	\bigg(
		\overrightarrow{A_3 I_3} 
		+ \overrightarrow{I_3 I_4} 
		+ \overrightarrow{I_4 I}
	\bigg) 
	\wedge \vec{\Omega}(S/R_0) 
\Bigg)
$$

$$
= \bigg( -R\vec{z}+\overrightarrow{I_4 I} \bigg)
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
= - \Bigg( 
	\bigg( 
		L\vec{y} 
	\bigg) 
	\wedge {\omega}_{S/R_0} \cdot \vec{z}  
\Bigg)
$$

$$
= - \Bigg( 
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
= -L {\omega}_{S/R_0} \cdot \vec{x}
$$

Selon $\vec{x}$ : 
$$
R\omega_{S_4/S} - R\omega_{S_3/S} 
= -L {\omega}_{S/R_0} 
$$

Donc : 
$$
\boxed{
	{\omega}_{S/R_0}
	= \frac{R}{L} (\omega_{S_3/S} - \omega_{S_4/S} )
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

PFD sur la fusée

$$
\begin{align}
D(F_i/R_0) = {F}(_{\text{S}\rightarrow F_i}) + {F}(_{S_i \rightarrow F_i}) \\
= {F}(_{S \rightarrow F_i}) - {F}(_{F_i \rightarrow S_i}) \\
\end{align}
$$

![](attachments/Pasted%20image%2020250619132805.png)


$$

F(F_i \to S_i) = 

\begin{Bmatrix}

X_{F_i S_i} \cdot \vec{x_i} + Y_{F_i S_i} \cdot \vec{y_i} + Z_{F_i S_i} \cdot \vec{z_i} \\

L_{F_i S_i} \cdot \vec{x_i} + N_{F_i S_i} \cdot \vec{z_i}

\end{Bmatrix}_{A_{i}}

$$

  

On néglige la masse des moteurs (peut être abusif)

  
  

$$

\vec{F}_{F_i \to S_i} =

\left\{

\begin{array}{c}

X_{F_iS_i} \big(\cos(\theta_i) \vec{x} + \sin(\theta_i) \vec{y} \big) 

+  Y_{F_iS_i} \big(\cos(\theta_i) \vec{y} - \sin(\theta_i) \vec{x} \big)

+ Z_{F_iS_i} \vec{z} \\[1em]

\quad L_{F_iS_i} \big(\cos(\theta_i) \vec{x} + \sin(\theta_i) \vec{y} \big)  + N_{R_{S_i}} \vec{z}

\end{array}

\right\}_{A_i}

$$

  
  

$$

\begin{align}

X_{F_i} - X_{F_iS_i} \cos(\theta_i) + Y_{F_iS_i} \sin(\theta_i) &= 0 \tag{7} \\

Y_{F_i} - X_{F_iS_i} \sin(\theta_i) - Y_{F_iS_i} \cos(\theta_i) &= 0 \tag{8} \\

Z_{F_i} - Z_{F_iS_i} &= 0 \tag{9} \\

L_{F_i} - L_{F_iS_i} \cos(\theta_i) &= 0 \tag{10} \\

M_{F_i} - L_{F_iS_i} \sin(\theta_i) &= 0 \tag{11} \\

N_{F_iS_i} &= 0 \tag{12}

\end{align}

$$

  

PFD sur les roue avant (inertie negligé)

$$

\begin{align}

D(S_i/R_0) = {F}(\text{Route} \rightarrow S_i) + {F}(F_i \rightarrow S_i) \\

\end{align}

$$

On se place au point $A_i$

  

$$

\vec{M}_{Ai}({\text{Route} \rightarrow S_i)} = \vec{M}_{I_i}({\text{Route}\rightarrow S_i)} + \left( \overrightarrow{A_iI_i} \right) \wedge (-{T}_{ri}\vec{x} + \vec{N}_{r_i} \vec{z})

$$

$$ = \vec{O} + ({-R}\vec{z})\wedge-T_{ri}\vec{x} = R *T_{ri}\vec{y}

$$

  

$$

\begin{align}

X_{F_iS_i} \cos(\theta_i) - Y_{F_iS_i} \sin(\theta_i) + T_{ri} &= 0 \tag{13} \\

X_{F_iS_i}\sin(\theta_i) + Y_{F_iS_i} \cos(\theta_i)&= 0 \tag{14} \\

Z_{F_iS_i} + N_i &= 0 \tag{15} \\

L_{F_iS_i} \cos(\theta_i) &= 0 \tag{16} \\

L_{F_iS_i} \sin(\theta_i) + R T_{ri} &= 0 \tag{17} \\

N_{F_iS_i} &= 0 \tag{18}

\end{align}

$$

  

PFD appliqué à tout le systeme

  

$$

\begin{align}

D(\Sigma/R_0) = \Sigma_{i=1}^{4}{F}(\text{Route} \rightarrow S_i) + {F}(P \rightarrow S) \\

\end{align}

$$

  

$$

\begin{align}

D(S/R_0) = \Sigma_{i=1}^{4}{F}(\text{Route} \rightarrow S_i) + {F}(P \rightarrow S) \\

\end{align}

$$

  

$$

\vec{M}_{G}({\text{Route} \rightarrow S_i)} = \vec{M}_{I_i}({\text{Route}\rightarrow S_i)} + \left( \overrightarrow{GI_i} \right) \wedge (-{T}_{ri}\vec{x} + \vec{N}_{r_i} \vec{z})

$$

$$

\vec{M}_{G}({\text{Route} \rightarrow S_i)} = \vec{M}_{I_i}({\text{Route}\rightarrow S_i)} + \left( \overrightarrow{GI_i} \right) \wedge (-{T}_{ri}\vec{x} + \vec{N}_{r_i} \vec{z})

$$

$$

=(x_G \vec{x} + y_G \vec{y} + z_G \vec{z}) \wedge ({T}_{ri}\vec{x} + \vec{N}_{r_i} \vec{z}) 

$$

  

$$

={T}_{ri}(-y_G \vec{z} + z_G \vec{y}) + N_{r_i}(-x_G\vec{y} +  y_G\vec{x}) 

$$

$$

\begin{align}

T_{r_1}+T_{r_2}+T_{r_3}+T_{r_4} &= Rd_x \tag{13}\\

0 &= Rd_y \tag{14} \\

N_{r_1}+N_{r_2}+N_{r_3}+N_{r_4}-mg &= Rd_z \tag{15} \\

y_G(N_{r_1}+N_{r_2}+N_{r_3}+N_{r_4}) &= δ_x \tag{16} \\

z_G(T_{r_1}+T_{r_2}+T_{r_3}+T_{r_4}) - x_G(N_{r_1}+N_{r_2}+N_{r_3}+N_{r_4}) &= δ_y \tag{17} \\

-y_G(T_{r_1}+T_{r_2}+T_{r_3}+T_{r_4}) &= δ_z \tag{18}

\end{align}

$$

  
  

$$

\text{On a avec les équations (16),(17) et (5) :}

$$

$$

\text{Dans le cas } \theta_i \neq \frac{\pi}{2}(2k+1)\text{ et } \theta_i \neq k\pi 

\Rightarrow \cos(\theta_i) \neq 0

$$

  

$$

\begin{align}

L_{F_{r_i}} \cos(\theta_i) &= 0 

\quad \Rightarrow \quad 

L_{F_{r_i}} = 0 

\\

  

L_{F_{r_i}} \sin(\theta_i) + R T_{r_i} &= 0 

\quad \Rightarrow \quad 

T_{r_1} = T_{r_2} = 0 

\\

  

C_{m_i} - R T_{r_i} &= 0 

\quad \Rightarrow \quad 

T_{r_3} = \frac{C_{m_3}}{R} \text{ et } T_{r_4} = \frac{C_{m_4}}{R}

  

\end{align}

$$

$$

\text{On a alors avec l'équations (5) et (19):}

$$

$$

\frac{C_{m_3}}{R} + \frac{C_{m_4}}{R} = Rd_x 

$$

## CALCULE DE RDX

$$

\text{Pour obtenir } R_d

$$

$$

\vec{R}_d(S/R_0) = m \frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0}

$$

$$
\text{calcule de }V(G,S/R_0)
$$
$$
\vec{V}(G,S/R_0) = \vec{V}(C,S/R_0) + \vec{GC}\wedge\vec{\Omega}(S/R_0) 
$$
$$
\text{avec } \vec{CG} = x_0 \vec{x} + y_0 \vec{y} +  z_0 \vec{z}
$$$$
\vec{V}(G,S/R_0) = \vec{V}(C,S/R_0) + \omega_{SR_0}(x_0 \vec{y} - y_0 \vec{x})
$$
$$
\text{calcule de } \frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0}
$$
$$
\text{calcule de } \frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0} \text{ (utulisation de la formule de derviation vectorielle)}
$$
$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0}  = \frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{S} + \vec{\Omega}(S/R_0) \wedge \vec{V}(G,S/R_0)
$$
$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0}  = \frac{d\vec{V}(C,S/R_0)}{dt} + \frac{d\omega_{SR_0}}{dt}(x_0 \vec{y} - y_0 \vec{x}) + \omega_{SR_0}\vec{z} \wedge (\vec{V}(C,S/R_0) + \omega_{SR_0}(x_0 \vec{y} - y_0 \vec{x}))
$$
$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0} = \dot{V}(C,S/R_0)\vec{x} + \dot{\omega}_{SR_0}(x_0 \vec{y} - y_0 \vec{x}) + \omega_{SR_0} \vec{z} \wedge (V(C,S/R_0)\vec{x} + \omega_{SR_0}(x_0 \vec{y} - y_0 \vec{x}))
$$
$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0} = \dot{V}(C,S/R_0)\vec{x} + \dot{\omega}_{SR_0}(x_0 \vec{y} - y_0 \vec{x}) -\omega_{SR_0}(V(C,S/R_0) - y_0 {\omega}_{SR_0} )\vec{y}+ \omega_{SR_0}x_0 \vec{y} - \omega_{SR_0}^2 x_0 \vec{x}
$$
$$
\text{Simplification } V(C,S/R_0) = V  \text{ et } \omega_{SR_0} = \omega
$$

$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0} = \dot{V} \vec{x} + \dot{\omega}(x_0 \vec{y} - y_0 \vec{x}) - \omega (V - y_0 \omega) \vec{y} + \omega x_0 \vec{y} - \omega^2 x_0 \vec{x}
$$

$$
\frac{d}{dt} [ \vec{V}(G,S/R_0) ]_{R_0}
= (\dot{V} - \dot{\omega} y_0 - \omega^2 x_0) \vec{x}
+ (\dot{\omega} x_0 - \omega V - y_0 \omega^2) \vec{y}
$$

On a alors selon e_x
$$
\begin{align}

\frac{C_{m_3}}{R} + \frac{C_{m_4}}{R} &= m(\dot{V} - \dot{\omega} y_0 - \omega^2 x_0)
\\
C_{m_3} + C_{m_4} &= Rm(\dot{V} - \dot{\omega} y_0 - \omega^2 x_0)
\end{align}
$$


## Equation moteur
resultat clasique sur les moteur CC

$C = kI$      $E=K_{E}\omega$

Loi des maille 
![[Pasted image 20250629182842.png]]

$$
U = RI + E
$$

On se place dans le cas U=constante

  

$$
\begin{align}

I &=\frac{U-E}{R}
\\
C &= kI = \frac{k}{R}(U-E)
\\
C &=  \frac{k}{R}(U-K_{E}\omega)
\end{align}


$$

  

On se place dans le cas où U est constant... 

  

$$
C(\omega) = \frac{k \alpha U}{R} (1 - \frac{K_E}{\alpha U} \omega)
$$
$$
C(\omega) = - \frac{k K_E}{R} \omega + \frac{k \alpha U}{R} 
$$
  On pose $a =- \frac{k K_E}{R}$ et $b=\frac{k  U}{R}$ 
  
$$
C(\omega) = a\omega + b\alpha 
$$
On cherche à déterminer a et b avec des valeurs donné dans la datasheet des moteurs
On se place dans le cas $\alpha = 1$ (pas de modulation)

On se place au couple bloqué appelle ici $C_{max}$ (couple maximum ou la vitesse de rotation est alors nul)
$$
C(0) = C_{max} = a*0 + b
$$
On se place à la vitesse à vide ici noté $\omega_{max}$ 
$$
\begin{align}

C(\omega_{max}) = 0 &= a\omega_{max} + b 
\\
a\omega_{max} &= -b
\\
a &= \frac{-b}{\omega_{max}}
\\
a &= -\frac{C_{max}}{\omega_{max}}
\end{align}
$$
On a alors

$$

C(\omega) = -\frac{C_{max}}{\omega_{max}}\omega + C_{max}\alpha 
$$
## Equa diff (verifier le 2)


$$
C_{m_3} + C_{m_4} = Rm(\dot{V} - \dot{\omega} y_0 - \omega^2 x_0)
$$
Or $C_{m_3} + C_{m_4}$ peut s'écrire
$$
\begin{align}
C_{m_3} + C_{m_4} &= -\frac{C_{max}}{\omega_{max}}\omega_{m_3} + C_{max}\alpha_3 + -\frac{C_{max}}{\omega_{max}}\omega_{m_3} + C_{max}\alpha_4
 
\\
&= C_{max}(-\frac{\omega_{m_3}}{\omega_{max}} + \alpha_3  -\frac{\omega_{m_4}}{\omega_{max}} + \alpha_4)
\\
&= C_{max}(\alpha_3 + \alpha_4 -\frac{1}{\omega_{max}}(\omega_{m_3} + \omega_{m_4}))
\\
&= C_{max}(\alpha_3 + \alpha_4 -\frac{2}{R\omega_{max}}V)
\end{align}
$$
On a alors

$$
\ 0 = \dot{V} + \frac{2 C_{\text{max}}}{R^2 \omega_{\text{max}} m} V - y_G \dot{\omega} - x_G \omega^2 - \frac{C_{\text{max}} (\alpha_3 + \alpha_4)}{R m} \
$$

On note
$$
\lambda (t){\omega}_{m3} = \lambda(t) {\omega_{m}} = \omega_{m4} 
$$
On peu alors en plus d'exprmier $V$ et $\omega$ en fonction de $\lambda$ on peut aussi exprimer $\alpha$ 

$$E=K_{E}\omega$$ 


$$
\ 0 = \frac{R}{2} (\lambda + 1)\dot{\omega_m} + \frac{2 C_{\text{max}}}{R^2 \omega_{\text{max}} m} \cdot \frac{R}{2} (\lambda + 1)\omega_m - y_G \frac{R}{L} (1 - \lambda)\dot{\omega_m} - x_G \frac{R}{L} (1 - \lambda)^2 \omega_m^2 - \frac{ C_{\text{max}} (1 + \lambda) \alpha}{R m} \
$$



Terme en $\dot{\omega}_m$
$$
\ \frac{R}{2} (\lambda + 1)- y_G \frac{R}{L} (1 - \lambda)= R(-\lambda(\frac{1}{2}+\frac{y_G}{L})+ \frac{1}{2}-\frac{y_G}{L}) = a
$$
Terme en ${\omega}_m$
$$
\frac{ 2C_{\text{max}}}{R^2 \omega_{\text{max}} m} \frac{R}{2}(\lambda + 1) = \frac{ C_{\text{max}}}{R \omega_{\text{max}} m} (\lambda + 1) = b \
$$
Terme en ${\omega_m}^2$
$$
-x_G \frac{R}{L}{(1 - \lambda)}^2 = c
$$
Terme constant 
$$
\ - \frac{C_{\text{max}} (1 + \lambda) \alpha}{R m} = d \
$$
## Resolution Equa diff



$$0 = a \dot{W_m} + bW_m + c {W_m}^2 + d \quad $$
On considère la solution particulière constante $y_p = k$ puis on cherche k qui vérifie l’équation différentielle
$$0 = 0 + bk + c k^2 + d$$


On suppose $\Delta = b^2 - 4cd \geq 0$ car sinon k ne vérifie par l'équation dans R 
on verfie avec le traceur de courbe que pour nos valeurs du systeme relle on a bien delta positif ce qui est bien le cas

image

  

On prend $k_0 = \frac{-b + \sqrt{b^2 - 4cd}}{2c}$ car la racine negative n'est pas verifier par le systeme reel (vitesse de rotation negative pour une tension positive)


On la fonction suivante  $$z = y-y_p \Leftrightarrow y = z + y_p$$
qu'on injecte, on a donc 
$$
\begin{align}
0 &= a \dot{z} + b (z + \cancel{k_0}) + c (z^2+2k_0z + \cancel{{k_0}^2}) + \cancel{d}
\\
\Rightarrow 0 &= a \dot{z} + (b + 2c k_0){z} + c z^2
\end{align}
$$
Bernoulli ordre 2 on alors la fonction suivante  
$$h = z^{1-2} = z^{-1} \Leftrightarrow z = \frac{1}{h} \Rightarrow z'= - \frac{h'}{h^2}$$
qu'on injecte on a alors 
$$
\begin{align}
0 &= -a \frac{h'}{h^2} + (b + 2 c k_0)  \frac{1}{h} + c\frac{1}{h^2}
\\
\Rightarrow0 &= -a h' + (b + 2 c k_0) h + c
\end{align}
$$
On se retrouve avec une simple equation du premier ordre en h qu'on résout facilement

on a h de la forme
$$h(t) = A e^{\beta t} + C$$
On identifie
$$0 = -a \beta A e^{\beta x} + (b + 2c k_0)( A e^{\beta x} + C)+ c$$

On a les constantes égales et les exponentielles égales pour que la solution soit vrai pour tout t 

en terme constant on a
$$0 = (b + 2c k_0)C+c \Leftrightarrow C = -\frac{c}{(b + 2c k_0)}$$
en terme exponentielle on a 
$$
\begin{align}
0 &= -a \beta \cancel{A}f  \cancel{e^{f x}} + (b + 2c k_0) \cancel{A e^{f x}}
\\
\beta &= \frac{b + 2c k_0}{fa}
\end{align}
$$
On a alors 
$$ h(t) = A e^{\frac{b + 2c k_0}{fa}t} - \frac{c}{(b + 2c k_0)}$$
On a donc
$$y = z + y_p =  \frac{1}{h} + y_p = \frac{1}{ A e^{\frac{b + 2c k_0}{a}x} - \frac{c}{(b + 2c k_0)}} + k_0$$
On determine A grace au condition initiale
$$y(0) = W_0 = \frac{1}{ A e^0 - \frac{c}{(b + 2c k_0)}} + k_0 \quad\Leftrightarrow \quad W_0 = \frac{1}{A - \frac{c}{(b + 2c k_0)}} + k_0$$
$$W_0 \neq 0$$

$$\Leftrightarrow (A-\frac{c}{(b + 2c k_0)})(W_0-k_0) = 1$$

  

$$\Leftrightarrow A = \frac{1}{\omega_0-k_0} + \frac{c}{(b + 2c k_0)}$$

  

$$\Rightarrow y(t) = \frac{1}{(\frac{1}{\omega_0-k_0} + \frac{c}{(b + 2c k_0)}) e^{\frac{b + 2c k_0}{a}t} - \frac{c}{(b + 2c k_0)}} + k_0$$

