# Homework 3B: Potential flow, PDE type, eigenstructure, and Mach number 

Total: 100 points

Instructions. Show your reasoning clearly and keep your notation consistent. Unless stated otherwise, assume fields are smooth enough for the manipulations you perform (chain rule, product rule, differentiation under the integral sign, etc.). You may use results stated in the lecture notes except in places where you are explicitly asked to derive those results.




## Problem 1: Classification from the principal matrix

> [!exercise] Exercise 1
> Preamble. This problem gives you one concrete PDE and asks you to execute the full classification workflow from Lecture 11: build the principal matrix, compute its eigenstructure, diagonalize the principal part, and identify the coordinate change that produces a canonical form.
> 
> Consider the constant-coefficient second-order PDE
> 
> $$
> \phi_{\xi \xi}+4 \phi_{\xi \zeta}-5 \phi_{\zeta \zeta}=0 .
> $$
> 
> (a) Principal matrix
> 
> Write the principal matrix $\mathbf{K}$ such that the principal part may be written as
> 
> $$
> \left(\begin{array}{ll}
> \partial_{\xi} & \partial_{\zeta}
> \end{array}\right) \mathbf{K}\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
> $$
> 
> (b) Eigenvalues and eigenvectors
> 
> Compute the eigenvalues and a corresponding eigenvector for each eigenvalue.
> (c) Classification
> 
> Use the signs of the eigenvalues to classify the PDE as elliptic, hyperbolic, or parabolic.
> (d) Diagonalization and canonical form
> 
> Let $\mathbf{V}$ be the matrix whose columns are your (appropriately normalized) eigenvectors. Show that rotating coordinates via
> 
> $$
> \binom{\xi^{\prime}}{\zeta^{\prime}}=\mathbf{V}^{T}\binom{\xi}{\zeta}
> $$
> 
> diagonalizes the principal part, and write the PDE in the canonical form
> 
> $$
> \lambda_{1} \phi \xi^{\prime} \xi^{\prime}+\lambda_{2} \phi \zeta_{\zeta^{\prime} \zeta^{\prime}}=0 .
> $$
> 
> (e) Explicit coordinate transformation
> 
> Write $\xi^{\prime}$ and $\zeta^{\prime}$ explicitly as linear combinations of $\xi$ and $\zeta$ (i.e. give the formulas for $\xi^{\prime}(\xi, \zeta)$ and $\zeta^{\prime}(\xi, \zeta)$ from your $\mathbf{V}$ ).


##### Problem a

To match the Lecture 11 matrix form

$$
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right)
\mathbf{K}
\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
=
A \phi_{\xi \xi}+2 B \phi_{\xi \zeta}+C \phi_{\zeta \zeta},
$$

we must choose $A=1$, $2 B=4$, and $C=-5$. Hence

$$
\mathbf{K}=\left(\begin{array}{cc}
1 & 2 \\
2 & -5
\end{array}\right) .
$$

Indeed,

$$
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right)
\left(\begin{array}{cc}
1 & 2 \\
2 & -5
\end{array}\right)
\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
=
\phi_{\xi \xi}+4 \phi_{\xi \zeta}-5 \phi_{\zeta \zeta} .
$$

##### Problem b

The eigenvalues are obtained from

$$
\operatorname{det}(\mathbf{K}-\lambda \mathbf{I})
=
\left|\begin{array}{cc}
1-\lambda & 2 \\
2 & -5-\lambda
\end{array}\right|
=
(1-\lambda)(-5-\lambda)-4
=
\lambda^{2}+4 \lambda-9 .
$$

Therefore

$$
\lambda_{1,2}=\frac{-4 \pm \sqrt{16+36}}{2}=-2 \pm \sqrt{13} .
$$

I will order them as

$$
\lambda_{1}=-2+\sqrt{13}, \qquad \lambda_{2}=-2-\sqrt{13} .
$$

For $\lambda_{1}=-2+\sqrt{13}$, solve $(\mathbf{K}-\lambda_{1}\mathbf{I})\boldsymbol{v}_{1}=0$:

$$
\left(\begin{array}{cc}
3-\sqrt{13} & 2 \\
2 & -3-\sqrt{13}
\end{array}\right)
\binom{x}{y}
=
\binom{0}{0} .
$$

One convenient choice is

$$
\boldsymbol{v}_{1} \propto \binom{3+\sqrt{13}}{2} .
$$

For $\lambda_{2}=-2-\sqrt{13}$, solve $(\mathbf{K}-\lambda_{2}\mathbf{I})\boldsymbol{v}_{2}=0$:

$$
\left(\begin{array}{cc}
3+\sqrt{13} & 2 \\
2 & -3+\sqrt{13}
\end{array}\right)
\binom{x}{y}
=
\binom{0}{0} .
$$

One convenient choice is

$$
\boldsymbol{v}_{2} \propto \binom{3-\sqrt{13}}{2} .
$$

To prepare for part (d), normalize them:

$$
\boldsymbol{v}_{1}=
\frac{1}{\sqrt{26+6 \sqrt{13}}}
\binom{3+\sqrt{13}}{2},
\qquad
\boldsymbol{v}_{2}=
\frac{1}{\sqrt{26-6 \sqrt{13}}}
\binom{3-\sqrt{13}}{2}.
$$

##### Problem c

Since

$$
\lambda_{1}=-2+\sqrt{13}>0,
\qquad
\lambda_{2}=-2-\sqrt{13}<0,
$$

the eigenvalues have opposite signs. Therefore the PDE is hyperbolic.

##### Problem d

Let

$$
\mathbf{V}=
\left(\begin{array}{ll}
\boldsymbol{v}_{1} & \boldsymbol{v}_{2}
\end{array}\right)
=
\left(\begin{array}{cc}
\dfrac{3+\sqrt{13}}{\sqrt{26+6 \sqrt{13}}} & \dfrac{3-\sqrt{13}}{\sqrt{26-6 \sqrt{13}}} \\
\dfrac{2}{\sqrt{26+6 \sqrt{13}}} & \dfrac{2}{\sqrt{26-6 \sqrt{13}}}
\end{array}\right) .
$$

Because the columns are orthonormal eigenvectors of the symmetric matrix $\mathbf{K}$, we have

$$
\mathbf{V}^{T} \mathbf{K} \mathbf{V}
=
\boldsymbol{\Lambda}
=
\left(\begin{array}{cc}
\lambda_{1} & 0 \\
0 & \lambda_{2}
\end{array}\right) .
$$

Now define the rotated coordinates by

$$
\binom{\xi^{\prime}}{\zeta^{\prime}}
=
\mathbf{V}^{T}
\binom{\xi}{\zeta} .
$$

By the Lecture 11 chain-rule relation,

$$
\binom{\partial_{\xi}}{\partial_{\zeta}}
=
\mathbf{V}
\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}} .
$$

Hence the principal part becomes

$$
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right)
\mathbf{K}
\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
=
\left(\begin{array}{ll}
\partial_{\xi^{\prime}} & \partial_{\zeta^{\prime}}
\end{array}\right)
\mathbf{V}^{T} \mathbf{K} \mathbf{V}
\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}} \phi
=
\left(\begin{array}{ll}
\partial_{\xi^{\prime}} & \partial_{\zeta^{\prime}}
\end{array}\right)
\boldsymbol{\Lambda}
\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}} \phi .
$$

Therefore the PDE is diagonalized to

$$
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}}=0,
$$

that is,

$$
(-2+\sqrt{13}) \phi_{\xi^{\prime} \xi^{\prime}}+(-2-\sqrt{13}) \phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

Equivalently,

$$
(\sqrt{13}-2) \phi_{\xi^{\prime} \xi^{\prime}}-(\sqrt{13}+2) \phi_{\zeta^{\prime} \zeta^{\prime}}=0,
$$

which is the canonical hyperbolic form.

##### Problem e

Since $\xi^{\prime}=\boldsymbol{v}_{1}^{T}(\xi, \zeta)^{T}$ and $\zeta^{\prime}=\boldsymbol{v}_{2}^{T}(\xi, \zeta)^{T}$, the explicit coordinate transformation is

$$
\xi^{\prime}=
\frac{3+\sqrt{13}}{\sqrt{26+6 \sqrt{13}}} \, \xi
+
\frac{2}{\sqrt{26+6 \sqrt{13}}} \, \zeta,
$$

and

$$
\zeta^{\prime}=
\frac{3-\sqrt{13}}{\sqrt{26-6 \sqrt{13}}} \, \xi
+
\frac{2}{\sqrt{26-6 \sqrt{13}}} \, \zeta .
$$

Any simultaneous sign change of an eigenvector gives an equivalent transformed coordinate system, so these formulas are one valid Lecture 11 choice.




## Problem 2: Eigenvectors, local directions, and characteristics ( $\mathbf{3 7}$ points)

> [!exercise] 2
> 
> Preamble. In question 1, you diagonalized the coefficient matrix K by an orthogonal change of variables, which produced a canonical principal part
> 
> $$
> \lambda_1 \phi \xi^{\prime} \xi^{\prime}+\lambda_2 \phi \zeta_{\zeta^{\prime} \zeta^{\prime}}
> $$
> 
> 
> In this problem you will connect that diagonalization to a concrete directional interpretation: the eigenvectors of $\mathbf{K}$ determine preferred directions in the $(\xi, \zeta)$ plane for the second-derivative operator acting on $\phi$.
> 
> Assume K is a constant, symmetric $2 \times 2$ matrix with eigenpairs $\left(\lambda_1, v_1\right)$ and $\left(\lambda_2, v_2\right)$, where $v_1, v_2$ are orthonormal.
> 
> **(a) (Directional second derivatives)**
> 
> Let $s \in \mathbb{R}^{2}$ be a unit vector and define the directional derivative $\partial_{s}:=s \cdot\left(\partial_{\xi}, \partial_{\zeta}\right)$. Show that
> 
> $$
> \partial_{s s} \phi=s^{T}\left(\begin{array}{ll}
> \phi_{\xi \xi} & \phi_{\xi \zeta} \\
> \phi_{\xi \zeta} & \phi_{\zeta \zeta}
> \end{array}\right) s .
> $$
> 
> That is, letting the Hessian be
> 
> $$
> \boldsymbol{H}(\phi):=\left(\begin{array}{ll}
> \phi_{\xi \xi} & \phi_{\xi \zeta} \\
> \phi_{\xi \zeta} & \phi_{\zeta \zeta}
> \end{array}\right)
> $$
> 
> show that the second directional derivative is obtained by evaluating the quadratic form induced by $\boldsymbol{H}(\phi)$ in the direction $\boldsymbol{s}$.
> 
> **(b) (Interpreting $\mathbf{K}$ via directional curvatures)**
> 
> Now consider the principal part operator
> 
> $$
> \mathcal{L}_{\text {prin }} \phi=\left(\begin{array}{ll}
> \partial_{\xi} & \partial_{\zeta}
> \end{array}\right) \mathbf{K}\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
> $$
> 
> Recall that $\mathbf{K}$ is symmetric and admits an orthonormal eigendecomposition
> 
> $$
> \mathbf{K}=\mathbf{V} \boldsymbol{\Lambda} \mathbf{V}^{T}, \quad \mathbf{V}=\left(\begin{array}{ll}
> \boldsymbol{v}_{1} & \boldsymbol{v}_{2}
> \end{array}\right), \quad \boldsymbol{\Lambda}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}\right)
> $$
> 
> Using this fact, rewrite $\mathcal{L}_{\text {prin }} \phi$ so that it is expressed as a sum of terms, each involving a directional second derivative in the quadratic form obtained in part (a) [4 points].
> 
> Use this representation to argue for the role that $\mathbf{K}$ plays in setting the principal component of the PDE [3 points]. Your answer should express precisely how $\mathbf{K}$ determines which directional second derivatives appear in $\mathcal{L}_{\text {prin }} \phi$, and how strongly they are weighted.
> Hint: You may find it useful to recall that the eigendecomposition $\mathbf{K}=\mathbf{V} \mathbf{\Lambda V}^{T}$ can be written as a sum of rank one matrices
> 
> $$
> \mathbf{K}=\lambda_{1} \boldsymbol{v}_{1} \boldsymbol{v}_{1}^{T}+\lambda_{2} \boldsymbol{v}_{2} \boldsymbol{v}_{2}^{T}
> $$
> 
> **(c) (Preferred directions from eigenvectors)**
> 
> Let $\mathbf{V}=\left[\boldsymbol{v}_{1} \boldsymbol{v}_{2}\right]$ be an orthogonal eigenvector matrix for $\mathbf{K}$ (so $\boldsymbol{v}_{1}, \boldsymbol{v}_{2}$ are orthonormal). Define new directional derivatives by
> 
> $$
> \binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}}=\mathbf{V}^{T}\binom{\partial_{\xi}}{\partial_{\zeta}}, \quad \text { i.e. } \quad \partial_{\xi^{\prime}}=\partial_{\boldsymbol{v}_{1}}, \quad \partial_{\zeta^{\prime}}=\partial_{\boldsymbol{v}_{2}}
> $$
> 
> Show that the principal part becomes
> 
> $$
> \lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}}
> $$
> 
> 
> 
> Then interpret this result in words [ $\mathbf{4}$ points]: what does it say about the role of $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$ as distinguished directions? (Hint: use your final boxed identity from part (b).)
> 
> **(d) (Hyperbolic case and characteristic directions)**
> 
> Assume $\lambda_{1}>0$ and $\lambda_{2}<0$ (hyperbolic).
> 
> Starting from the diagonal principal part from part (c),
> 
> $$
> \lambda_{1} \phi \xi^{\prime} \xi^{\prime}+\lambda_{2} \phi{\zeta^{\prime} \zeta^{\prime}}=0
> $$
> 
> write $\lambda_{2}=-\left|\lambda_{2}\right|$ and divide the equation by $\lambda_{1}$ [3 points].
> Then introduce the rescaled coordinate
> 
> $$
> \tilde{\zeta}^{\prime}:=\sqrt{\frac{\left|\lambda_{2}\right|}{\lambda_{1}}} \zeta^{\prime},
> $$
> 
> and show that the equation becomes
> 
> $$
> \phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}}=0
> $$
> 
> 
> 
> Using the Lecture 11 result that
> 
> $$
> \phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}}=\left(\partial_{\xi^{\prime}}+\partial_{\tilde{\zeta}^{\prime}}\right)\left(\partial_{\xi^{\prime}}-\partial_{\tilde{\zeta}^{\prime}}\right) \phi,
> $$
> 
> state the two characteristic families in the $\left(\xi^{\prime}, \tilde{\zeta}^{\prime}\right)$ plane [1 points].
> Then, in 4-6 sentences, explain why these families represent directions along which information propagates [ $\mathbf{2}$ points]. Your explanation should reference the characteristic variables $\eta=\xi^{\prime}+\tilde{\zeta}^{\prime}$ and $\mu=\xi^{\prime}-\tilde{\zeta}^{\prime}$ and the resulting general form $\phi=f(\eta)+g(\mu)$ (from Lecture 11).
> 
> **(e) (Back to the original coordinates)**
> 
> In part (d) the characteristic families in the hyperbolic canonical variables ( $\xi^{\prime}, \tilde{\zeta}^{\prime}$ ) are the straight lines
> 
> $$
> \xi^{\prime}+\tilde{\zeta}^{\prime}=\text { constant }, \quad \xi^{\prime}-\tilde{\zeta}^{\prime}=\text { constant. }
> $$
> 
> Use the coordinate change from part (c),
> 
> $$
> \binom{\xi^{\prime}}{\zeta^{\prime}}=\mathbf{V}^{T}\binom{\xi}{\zeta}, \quad \tilde{\zeta}^{\prime}=\alpha \zeta^{\prime}, \quad \alpha=\sqrt{\frac{\left|\lambda_{2}\right|}{\lambda_{1}}},
> $$
> 
> to write these characteristic families as two families of straight lines in the original $(\xi, \zeta)$-plane [3 points].
> 
> Hint: A line in $(\xi, \zeta)$ can be written as $\boldsymbol{n}^{T}(\xi, \zeta)^{T}=$ constant, where $\boldsymbol{n}$ is the unit normal vector to the line. Identify the two normals $\boldsymbol{n}_{ \pm}$in terms of $\mathbf{V}, \alpha$, and the vectors $\boldsymbol{e}_{1}=(1,0)^{T}$, $\boldsymbol{e}_{2}=(0,1)^{T}$.
> 
> Finally, explain in $2-4$ sentences what geometric information is carried by $\mathbf{V}$ (i.e. what it tells you about directions in the original coordinates) [2 points].
> 


##### Problem a

Let

$$
\boldsymbol{s}=\binom{s_{1}}{s_{2}}, \qquad |\boldsymbol{s}|=1,
$$

so that

$$
\partial_{\boldsymbol{s}}=s_{1} \partial_{\xi}+s_{2} \partial_{\zeta} .
$$

Because $\boldsymbol{s}$ is constant,

$$
\partial_{s s} \phi
=
\partial_{\boldsymbol{s}}\left(\partial_{\boldsymbol{s}} \phi\right)
=
\left(s_{1} \partial_{\xi}+s_{2} \partial_{\zeta}\right)\left(s_{1} \phi_{\xi}+s_{2} \phi_{\zeta}\right)
=
s_{1}^{2} \phi_{\xi \xi}+s_{1} s_{2} \phi_{\xi \zeta}+s_{2} s_{1} \phi_{\zeta \xi}+s_{2}^{2} \phi_{\zeta \zeta} .
$$

Using equality of mixed partials, $\phi_{\zeta \xi}=\phi_{\xi \zeta}$, this becomes

$$
\partial_{s s} \phi=s_{1}^{2} \phi_{\xi \xi}+2 s_{1} s_{2} \phi_{\xi \zeta}+s_{2}^{2} \phi_{\zeta \zeta} .
$$

Now compute the quadratic form induced by the Hessian:

$$
\boldsymbol{s}^{T} \boldsymbol{H}(\phi) \boldsymbol{s}
=
\left(\begin{array}{ll}
s_{1} & s_{2}
\end{array}\right)
\left(\begin{array}{cc}
\phi_{\xi \xi} & \phi_{\xi \zeta} \\
\phi_{\xi \zeta} & \phi_{\zeta \zeta}
\end{array}\right)
\binom{s_{1}}{s_{2}}
=
s_{1}^{2} \phi_{\xi \xi}+2 s_{1} s_{2} \phi_{\xi \zeta}+s_{2}^{2} \phi_{\zeta \zeta} .
$$

Therefore

$$
\partial_{s s} \phi=\boldsymbol{s}^{T} \boldsymbol{H}(\phi) \boldsymbol{s} .
$$

This shows that the second directional derivative is exactly the Hessian quadratic form evaluated in the direction $\boldsymbol{s}$.

##### Problem b

Let

$$
\boldsymbol{D}:=\binom{\partial_{\xi}}{\partial_{\zeta}} .
$$

Then

$$
\mathcal{L}_{\text {prin }} \phi
=
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right) \mathbf{K}\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
=
\boldsymbol{D}^{T} \mathbf{K} \boldsymbol{D} \phi .
$$

Using

$$
\mathbf{K}=\lambda_{1} \boldsymbol{v}_{1} \boldsymbol{v}_{1}^{T}+\lambda_{2} \boldsymbol{v}_{2} \boldsymbol{v}_{2}^{T},
$$

we obtain

$$
\mathcal{L}_{\text {prin }} \phi
=
\boldsymbol{D}^{T}\left(\lambda_{1} \boldsymbol{v}_{1} \boldsymbol{v}_{1}^{T}+\lambda_{2} \boldsymbol{v}_{2} \boldsymbol{v}_{2}^{T}\right) \boldsymbol{D} \phi
=
\lambda_{1} \boldsymbol{D}^{T} \boldsymbol{v}_{1} \boldsymbol{v}_{1}^{T} \boldsymbol{D} \phi+\lambda_{2} \boldsymbol{D}^{T} \boldsymbol{v}_{2} \boldsymbol{v}_{2}^{T} \boldsymbol{D} \phi .
$$

Since $\boldsymbol{D}^{T} \boldsymbol{v}_{i}=\boldsymbol{v}_{i}^{T} \boldsymbol{D}=\partial_{\boldsymbol{v}_{i}}$, it follows that

$$
\mathcal{L}_{\text {prin }} \phi
=
\lambda_{1}\left(\boldsymbol{v}_{1}^{T} \boldsymbol{D}\right)\left(\boldsymbol{v}_{1}^{T} \boldsymbol{D}\right) \phi+\lambda_{2}\left(\boldsymbol{v}_{2}^{T} \boldsymbol{D}\right)\left(\boldsymbol{v}_{2}^{T} \boldsymbol{D}\right) \phi
=
\lambda_{1} \partial_{v_{1} v_{1}} \phi+\lambda_{2} \partial_{v_{2} v_{2}} \phi .
$$

Thus the principal part is a weighted sum of directional second derivatives along the eigenvector directions. The matrix $\mathbf{K}$ determines precisely which directions appear through its eigenvectors $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$, and it determines how strongly each directional curvature contributes through the weights $\lambda_{1}$ and $\lambda_{2}$. Because these are the highest-order terms, $\mathbf{K}$ sets the local principal behavior of the PDE: the preferred directions, the relative strength of curvature in those directions, and, through the signs of the eigenvalues, the PDE type.

##### Problem c

By definition,

$$
\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}}
=
\mathbf{V}^{T}\binom{\partial_{\xi}}{\partial_{\zeta}},
\qquad
\mathbf{V}=\left(\begin{array}{ll}
\boldsymbol{v}_{1} & \boldsymbol{v}_{2}
\end{array}\right) .
$$

Therefore

$$
\partial_{\xi^{\prime}}=\boldsymbol{v}_{1}^{T}\binom{\partial_{\xi}}{\partial_{\zeta}}=\partial_{\boldsymbol{v}_{1}},
\qquad
\partial_{\zeta^{\prime}}=\boldsymbol{v}_{2}^{T}\binom{\partial_{\xi}}{\partial_{\zeta}}=\partial_{\boldsymbol{v}_{2}} .
$$

Substituting these identities into the result of part (b) gives

$$
\mathcal{L}_{\text {prin }} \phi
=
\lambda_{1} \partial_{v_{1} v_{1}} \phi+\lambda_{2} \partial_{v_{2} v_{2}} \phi
=
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}} .
$$

This shows that $\boldsymbol{v}_{1}$ and $\boldsymbol{v}_{2}$ are the distinguished directions selected by the principal matrix. In the original $(\xi, \zeta)$ plane they are the two orthonormal directions along which the principal operator measures curvature independently. Once the coordinates are aligned with these eigenvectors, the mixed derivative disappears and the operator decouples into one second derivative along $\boldsymbol{v}_{1}$ and one second derivative along $\boldsymbol{v}_{2}$. In this sense, the eigenvectors identify the preferred geometric directions of the PDE.

##### Problem d

Assume $\lambda_{1}>0$ and $\lambda_{2}<0$. Writing $\lambda_{2}=-\left|\lambda_{2}\right|$, the diagonal principal part becomes

$$
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}-\left|\lambda_{2}\right| \phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

Dividing by $\lambda_{1}$ gives

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\frac{\left|\lambda_{2}\right|}{\lambda_{1}} \phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

To make the coefficient of the second term equal to one, the chain rule requires the rescaling

$$
\tilde{\zeta}^{\prime}:=\sqrt{\frac{\lambda_{1}}{\left|\lambda_{2}\right|}} \, \zeta^{\prime} .
$$

Equivalently, if

$$
\alpha:=\sqrt{\frac{\left|\lambda_{2}\right|}{\lambda_{1}}},
$$

then $\tilde{\zeta}^{\prime}=\zeta^{\prime} / \alpha$. Since

$$
\partial_{\zeta^{\prime}}
=
\sqrt{\frac{\lambda_{1}}{\left|\lambda_{2}\right|}} \, \partial_{\tilde{\zeta}^{\prime}},
$$

we have

$$
\phi_{\zeta^{\prime} \zeta^{\prime}}
=
\frac{\lambda_{1}}{\left|\lambda_{2}\right|} \phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}} .
$$

Substituting into the previous equation yields

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}}=0 .
$$

By the Lecture 11 factorization result,

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}}
=
\left(\partial_{\xi^{\prime}}+\partial_{\tilde{\zeta}^{\prime}}\right)\left(\partial_{\xi^{\prime}}-\partial_{\tilde{\zeta}^{\prime}}\right) \phi .
$$

Hence the two characteristic families in the $\left(\xi^{\prime}, \tilde{\zeta}^{\prime}\right)$ plane are

$$
\xi^{\prime}+\tilde{\zeta}^{\prime}=\text { constant },
\qquad
\xi^{\prime}-\tilde{\zeta}^{\prime}=\text { constant } .
$$

Introducing the characteristic variables

$$
\eta=\xi^{\prime}+\tilde{\zeta}^{\prime}, \qquad \mu=\xi^{\prime}-\tilde{\zeta}^{\prime},
$$

Lecture 11 gives

$$
\phi_{\eta \mu}=0,
\qquad
\phi=f(\eta)+g(\mu) .
$$

This formula shows that the solution splits into two independent one-variable contributions. The term $f(\eta)$ is transported along curves $\eta=\text { constant }$, while the term $g(\mu)$ is transported along curves $\mu=\text { constant }$. Data prescribed on a noncharacteristic curve determine the two functions $f$ and $g$, and those functions then propagate along their respective characteristic families. In this sense, the characteristics are the directions along which information travels. The hyperbolic equation does not couple the solution equally in all directions; instead, it organizes the solution into two propagating families.

##### Problem e

Let

$$
\boldsymbol{x}:=\binom{\xi}{\zeta}, \qquad \boldsymbol{e}_{1}=\binom{1}{0}, \qquad \boldsymbol{e}_{2}=\binom{0}{1} .
$$

Since

$$
\binom{\xi^{\prime}}{\zeta^{\prime}}=\mathbf{V}^{T} \boldsymbol{x},
$$

we may write

$$
\xi^{\prime}=\boldsymbol{e}_{1}^{T} \mathbf{V}^{T} \boldsymbol{x},
\qquad
\zeta^{\prime}=\boldsymbol{e}_{2}^{T} \mathbf{V}^{T} \boldsymbol{x} .
$$

From part (d), the characteristic families are

$$
\xi^{\prime} \pm \tilde{\zeta}^{\prime}=\text { constant }
\qquad \text { with } \qquad
\tilde{\zeta}^{\prime}=\frac{1}{\alpha} \zeta^{\prime},
\quad
\alpha=\sqrt{\frac{\left|\lambda_{2}\right|}{\lambda_{1}}} .
$$

Therefore

$$
\xi^{\prime} \pm \frac{1}{\alpha} \zeta^{\prime}=\text { constant } .
$$

Multiplying by $\alpha$ gives an equivalent line equation:

$$
\alpha \xi^{\prime} \pm \zeta^{\prime}=\text { constant } .
$$

Substituting $\xi^{\prime}=\boldsymbol{e}_{1}^{T} \mathbf{V}^{T} \boldsymbol{x}$ and $\zeta^{\prime}=\boldsymbol{e}_{2}^{T} \mathbf{V}^{T} \boldsymbol{x}$,

$$
\left(\alpha \boldsymbol{e}_{1} \pm \boldsymbol{e}_{2}\right)^{T} \mathbf{V}^{T} \boldsymbol{x}=\text { constant } .
$$

Equivalently,

$$
\left[\mathbf{V}\left(\alpha \boldsymbol{e}_{1} \pm \boldsymbol{e}_{2}\right)\right]^{T} \boldsymbol{x}=\text { constant } .
$$

Thus the two characteristic families in the original $(\xi, \zeta)$-plane are straight lines

$$
\left[\mathbf{V}\left(\alpha \boldsymbol{e}_{1}+\boldsymbol{e}_{2}\right)\right]^{T}\binom{\xi}{\zeta}=\text { constant },
\qquad
\left[\mathbf{V}\left(\alpha \boldsymbol{e}_{1}-\boldsymbol{e}_{2}\right)\right]^{T}\binom{\xi}{\zeta}=\text { constant } .
$$

A corresponding choice of unit normals is

$$
\boldsymbol{n}_{\pm}
=
\frac{\mathbf{V}\left(\alpha \boldsymbol{e}_{1} \pm \boldsymbol{e}_{2}\right)}{\sqrt{\alpha^{2}+1}} .
$$

Geometrically, $\mathbf{V}$ carries the eigenvector information of $\mathbf{K}$ back to the original coordinates. Its columns tell us which two orthogonal directions in the $(\xi, \zeta)$ plane diagonalize the principal part, so $\mathbf{V}$ fixes the orientation of the preferred directions selected by the PDE. After the additional hyperbolic rescaling, those directions determine the two characteristic line families in the original plane. In short, $\mathbf{V}$ tells us how the distinguished canonical directions sit inside the original coordinate system.




## Problem 3: Unsteady 1D potential flow revisited

> [!exercise] Exercise 3
> Preamble. Consider the linearized unsteady one-dimensional compressible potential equation
> 
> $$
> \phi_{t t}+2 u_{*} \phi_{x t}+\left(u_{*}^{2}-a_{*}^{2}\right) \phi_{x x}=0
> $$
> 
> In Lecture 12, this equation was shown to be hyperbolic and to admit traveling-wave solutions. In this problem, you will reinterpret that result using the principal-matrix and directional-curvature framework developed in Problem 2.
> 
> 
> **(a) Principal matrix and eigenvalues**
> (i) Write the principal matrix $\mathbf{K}_{1 D}$ associated with this PDE in the form
> 
> $$
> \mathcal{L}_{\text {prin }} \phi=\left(\begin{array}{ll}
> \partial_{t} & \partial_{x}
> \end{array}\right) \mathbf{K}_{1 D}\binom{\partial_{t}}{\partial_{x}} \phi
> $$
> 
> (ii) Compute the eigenvalues of $\mathbf{K}_{1 D}$ explicitly.
> (iii) Using your square-root expression for the eigenvalues (not the determinant shortcut), show directly that one eigenvalue is strictly positive and the other strictly negative for $a_{*}>0$. Conclude that the equation is hyperbolic.
> 
> 
> **(b) Eigenvectors as distinguished directions in ( $t, x$ )**
> (i) Compute eigenvectors $\boldsymbol{v}_{1}, \boldsymbol{v}_{2}$ of $\mathbf{K}_{1 D}$.
> (ii) Using the result of Problem 2(b), rewrite the principal part in the form
> 
> $$
> \mathcal{L}_{\text {prin }} \phi=\lambda_{1} \partial_{v_{1} v_{1}} \phi+\lambda_{2} \partial_{v_{2} v_{2}} \phi
> $$
> 
> (iii) Interpret this expression in words. What do the vectors $\boldsymbol{v}_{1}, \boldsymbol{v}_{2}$ represent geometrically in the $(t, x)$ plane? Why do these directions become distinguished directions for solution behavior?
> 
> 
> **(c) Canonical form and characteristic variables**
> Because the eigenvalues have opposite signs, the equation is hyperbolic.
> (i) Introduce new coordinates aligned with $\boldsymbol{v}_{1}, \boldsymbol{v}_{2}$ and show that, after appropriate rescaling, the principal part reduces to
> $$
> \phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
> $$
> (ii) Using the result from Lecture 11, state the two characteristic families in $\left(\xi^{\prime}, \zeta^{\prime}\right)$.
> (iii) Translate these families back into $(t, x)$ coordinates.
> 
> 
> **(d) Wave decomposition and physical interpretation**
> (i) State the general solution in ( $x, t$ ) variables.
> (ii) Explain, in 4-6 sentences, why disturbances propagate at speeds $u_{*} \pm a_{*}$ in the laboratory frame.
> (iii) Explain why upstream influence disappears when $\left|u_{*}\right|>a_{*}$.
> 
> 


##### Problem a

To match the Lecture 11 and Lecture 12 principal-matrix form,

$$
\mathcal{L}_{\text {prin }} \phi
=
\left(\begin{array}{ll}
\partial_{t} & \partial_{x}
\end{array}\right) \mathbf{K}_{1 D}\binom{\partial_{t}}{\partial_{x}} \phi,
$$

we choose

$$
\mathbf{K}_{1 D}=
\left(\begin{array}{cc}
1 & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}
\end{array}\right) .
$$

Indeed,

$$
\left(\begin{array}{ll}
\partial_{t} & \partial_{x}
\end{array}\right)
\left(\begin{array}{cc}
1 & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}
\end{array}\right)
\binom{\partial_{t}}{\partial_{x}} \phi
=
\phi_{t t}+2 u_{*} \phi_{x t}+\left(u_{*}^{2}-a_{*}^{2}\right) \phi_{x x} .
$$

To compute the eigenvalues, solve

$$
\operatorname{det}\left(\mathbf{K}_{1 D}-\lambda \mathbf{I}\right)=0 .
$$

This gives

$$
\left|\begin{array}{cc}
1-\lambda & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}-\lambda
\end{array}\right|
=
\left(1-\lambda\right)\left(u_{*}^{2}-a_{*}^{2}-\lambda\right)-u_{*}^{2}
=
0,
$$

so

$$
\lambda^{2}-\left(1+u_{*}^{2}-a_{*}^{2}\right) \lambda-a_{*}^{2}=0 .
$$

Let

$$
A:=1+u_{*}^{2}-a_{*}^{2} .
$$

Then the eigenvalues are

$$
\lambda_{1,2}=\frac{A \pm \sqrt{A^{2}+4 a_{*}^{2}}}{2} .
$$

Now use this square-root expression directly. Since $a_{*}>0$, we have

$$
A^{2}+4 a_{*}^{2}>A^{2},
$$

and therefore

$$
\sqrt{A^{2}+4 a_{*}^{2}}>|A| .
$$

Hence

$$
A+\sqrt{A^{2}+4 a_{*}^{2}}>0,
\qquad
A-\sqrt{A^{2}+4 a_{*}^{2}}<0 .
$$

It follows that

$$
\lambda_{1}=\frac{A+\sqrt{A^{2}+4 a_{*}^{2}}}{2}>0,
\qquad
\lambda_{2}=\frac{A-\sqrt{A^{2}+4 a_{*}^{2}}}{2}<0 .
$$

Thus one eigenvalue is strictly positive and the other is strictly negative for every $a_{*}>0$. Therefore the equation is hyperbolic.

##### Problem b

For an eigenvalue $\lambda$, the eigenvector equation is

$$
\left(\mathbf{K}_{1 D}-\lambda \mathbf{I}\right)\binom{\alpha}{\beta}
=
\left(\begin{array}{cc}
1-\lambda & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}-\lambda
\end{array}\right)
\binom{\alpha}{\beta}
=
\binom{0}{0} .
$$

From the first row,

$$
\left(1-\lambda\right) \alpha+u_{*} \beta=0 .
$$

For $u_{*} \neq 0$, one convenient choice is therefore

$$
\boldsymbol{w}_{i}=
\binom{u_{*}}{\lambda_{i}-1},
\qquad i=1,2 .
$$

Indeed,

$$
\left(1-\lambda_{i}\right) u_{*}+u_{*}\left(\lambda_{i}-1\right)=0,
$$

so the first row is satisfied, and because $\lambda_{i}$ is an eigenvalue, the second row is then automatically satisfied as well. Thus, for $u_{*} \neq 0$,

$$
\boldsymbol{v}_{1} \propto \binom{u_{*}}{\lambda_{1}-1},
\qquad
\boldsymbol{v}_{2} \propto \binom{u_{*}}{\lambda_{2}-1} .
$$

If $u_{*}=0$, then

$$
\mathbf{K}_{1 D}=
\left(\begin{array}{cc}
1 & 0 \\
0 & -a_{*}^{2}
\end{array}\right),
$$

so the eigenvectors are simply $\boldsymbol{e}_{t}=(1,0)^{T}$ and $\boldsymbol{e}_{x}=(0,1)^{T}$. This is exactly the $u_{*} \to 0$ limit of the distinguished $t$- and $x$-directions.

To use the directional-curvature result from Problem 2(b), normalize the eigenvectors:

$$
\widehat{\boldsymbol{v}}_{i}
=
\frac{1}{\sqrt{u_{*}^{2}+\left(\lambda_{i}-1\right)^{2}}}
\binom{u_{*}}{\lambda_{i}-1},
\qquad i=1,2,
$$

for $u_{*} \neq 0$. Since $\mathbf{K}_{1 D}$ is symmetric, these normalized eigenvectors are orthonormal.

Therefore, by Problem 2(b),

$$
\mathcal{L}_{\text {prin }} \phi
=
\lambda_{1} \partial_{\widehat{v}_{1} \widehat{v}_{1}} \phi+\lambda_{2} \partial_{\widehat{v}_{2} \widehat{v}_{2}} \phi .
$$

This means that the principal part of the PDE is a weighted sum of second directional derivatives along two special directions in the $(t, x)$ plane. The vectors $\widehat{\boldsymbol{v}}_{1}$ and $\widehat{\boldsymbol{v}}_{2}$ are the two eigendirections selected by $\mathbf{K}_{1 D}$, so they are the directions in which the principal operator acts independently after diagonalization. Because $\lambda_{1}>0$ and $\lambda_{2}<0$, the operator measures curvature with opposite signs in these two directions. That sign opposition is the geometric signature of hyperbolic behavior and is what makes these eigendirections distinguished for the local propagation of disturbances.

##### Problem c

Let

$$
\mathbf{V}=\left(\begin{array}{ll}
\widehat{\boldsymbol{v}}_{1} & \widehat{\boldsymbol{v}}_{2}
\end{array}\right),
\qquad
\binom{\xi^{\prime}}{\zeta^{\prime}}=\mathbf{V}^{T}\binom{t}{x} .
$$

By the result of Problem 2(c),

$$
\mathcal{L}_{\text {prin }} \phi
=
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}} .
$$

Since $\lambda_{1}>0$ and $\lambda_{2}<0$, write $\lambda_{2}=-\left|\lambda_{2}\right|$. Then

$$
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}-\left|\lambda_{2}\right| \phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

Dividing by $\lambda_{1}$ gives

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\frac{\left|\lambda_{2}\right|}{\lambda_{1}} \phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

Now introduce the rescaled coordinate

$$
\tilde{\zeta}^{\prime}:=\sqrt{\frac{\lambda_{1}}{\left|\lambda_{2}\right|}} \, \zeta^{\prime} .
$$

Then

$$
\partial_{\zeta^{\prime}}
=
\sqrt{\frac{\lambda_{1}}{\left|\lambda_{2}\right|}} \, \partial_{\tilde{\zeta}^{\prime}},
\qquad
\phi_{\zeta^{\prime} \zeta^{\prime}}
=
\frac{\lambda_{1}}{\left|\lambda_{2}\right|} \phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}} .
$$

Therefore the equation becomes

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\tilde{\zeta}^{\prime} \tilde{\zeta}^{\prime}}=0 .
$$

Relabeling $\tilde{\zeta}^{\prime}$ as $\zeta^{\prime}$, we obtain the canonical form

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\zeta^{\prime} \zeta^{\prime}}=0 .
$$

By Lecture 11, the two characteristic families in $\left(\xi^{\prime}, \zeta^{\prime}\right)$ are

$$
\xi^{\prime}+\zeta^{\prime}=\text { constant },
\qquad
\xi^{\prime}-\zeta^{\prime}=\text { constant } .
$$

To translate these back into $(t, x)$, it is most convenient to factor the original operator directly:

$$
\phi_{t t}+2 u_{*} \phi_{x t}+\left(u_{*}^{2}-a_{*}^{2}\right) \phi_{x x}
=
\left(\partial_{t}+\left(u_{*}+a_{*}\right) \partial_{x}\right)\left(\partial_{t}+\left(u_{*}-a_{*}\right) \partial_{x}\right) \phi .
$$

For a first-order operator $\partial_{t}+c \partial_{x}$, the characteristic curves satisfy

$$
\frac{d x}{d t}=c,
$$

so the invariant is $x-c t$. Hence the two characteristic families in $(t, x)$ are

$$
x-\left(u_{*}+a_{*}\right) t=\text { constant },
\qquad
x-\left(u_{*}-a_{*}\right) t=\text { constant } .
$$

##### Problem d

Using the characteristic variables from part (c),

$$
\eta=x-\left(u_{*}+a_{*}\right) t,
\qquad
\mu=x-\left(u_{*}-a_{*}\right) t,
$$

the Lecture 11 hyperbolic solution formula gives

$$
\phi(x, t)=f(\eta)+g(\mu)
=
f\left(x-\left(u_{*}+a_{*}\right) t\right)+g\left(x-\left(u_{*}-a_{*}\right) t\right),
$$

where $f$ and $g$ are arbitrary functions determined by the data.

This formula shows that the solution is the sum of two traveling waves, each moving along one characteristic family. The argument of the first wave is constant on lines $x-\left(u_{*}+a_{*}\right) t=\text { constant }$, so that component moves with speed $u_{*}+a_{*}$. The argument of the second wave is constant on lines $x-\left(u_{*}-a_{*}\right) t=\text { constant }$, so that component moves with speed $u_{*}-a_{*}$. Relative to the fluid, the two disturbances move at speeds $\pm a_{*}$, and the background advection by the uniform flow shifts both by $u_{*}$ in the laboratory frame. Thus the observable propagation speeds are $u_{*} \pm a_{*}$.

When $\left|u_{*}\right|>a_{*}$, the two characteristic speeds $u_{*}+a_{*}$ and $u_{*}-a_{*}$ have the same sign as $u_{*}$. Therefore both wave families are convected in the same overall direction, and no characteristic carries information against the flow. In that regime there is no upstream-traveling family, so disturbances downstream cannot influence the solution upstream. This is why upstream influence disappears in supersonic flow.
