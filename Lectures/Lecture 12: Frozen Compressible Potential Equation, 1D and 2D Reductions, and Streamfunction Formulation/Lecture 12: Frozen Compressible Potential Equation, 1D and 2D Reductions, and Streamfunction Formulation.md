## 1 Returning to the frozen compressible potential equation

In Lecture 11 we derived the nonlinear compressible potential equation governing inviscid, isentropic, irrotational flow. We then observed that although the equation is nonlinear, it is quasilinear: it is linear in its highest-order derivatives, with coefficients depending on the local flow state.

To understand the qualitative behavior of solutions, we extracted the principal (highest-derivative) part and froze the coefficients locally at a point ( $\boldsymbol{x}_{*}, t_{*}$ ). This produced a linear constant-coefficient equation that governs the local behavior of disturbances. Because PDE classification depends only on the principal part, the frozen equation determines whether the flow behaves elliptically, hyperbolically, or parabolically at that point.

Today we apply that machinery directly to compressible potential flow.
The frozen linear equation derived in Lecture 11 was

$$
\begin{aligned}
& \phi_{t t}+2 u_{*} \phi_{x t}+2 v_{*} \phi_{y t}+2 w_{*} \phi_{z t} \\
+ & \left(u_{*}^{2}-a_{*}^{2}\right) \phi_{x x}+\left(v_{*}^{2}-a_{*}^{2}\right) \phi_{y y}+\left(w_{*}^{2}-a_{*}^{2}\right) \phi_{z z} \\
+ & 2 u_{*} v_{*} \phi_{x y}+2 u_{*} w_{*} \phi_{x z}+2 v_{*} w_{*} \phi_{y z}=0
\end{aligned}
$$

where $\left(u_{*}, v_{*}, w_{*}\right)$ and $a_{*}$ denote the locally frozen velocity components and sound speed. To emphasize that we are now working with a locally frozen linear equation, we drop the subscript $n$ and write the result in terms of $\phi$.

This equation contains four independent variables ( $x, y, z, t$ ). However, most physically relevant problems fall into simpler categories. Rather than attempting to analyze the full four-variable system, we now consider two important reductions that capture the essential physics.

## 2 Two physically important reductions

The full potential equation describes three-dimensional, time-dependent compressible flow. Yet in practice, many important problems involve only two independent variables at a time. Two particularly significant cases are:
(i) Unsteady one-dimensional flow: disturbances depending on ( $x, t$ ) only.
(ii) Steady two-dimensional flow: disturbances depending on $(x, y)$ only.

These two reductions correspond to two distinct classes of physical phenomena.
Unsteady one-dimensional flow models acoustic wave propagation, nozzle transients, and smallamplitude disturbances moving through a uniform stream. In such problems, variations in the transverse directions are negligible, and the essential question is how disturbances evolve in time along a preferred spatial direction.

Steady two-dimensional flow, by contrast, models external aerodynamics: flow over airfoils, around bodies, and through channels in which time variation is negligible but spatial structure is essential. In these problems the independent variables are purely spatial, and the central question is how information propagates within the spatial domain.

These two settings lead to very different mathematical behaviors. One involves time evolution; the other does not. One supports propagating waves; the other may behave like Laplace's equation. The difference turns out to be governed entirely by the eigenstructure of the principal coefficient matrix - and ultimately by the Mach number.

We now analyze these two reductions in turn.

## 3 Unsteady one-dimensional compressible potential flow

We now restrict attention to disturbances depending only on $(x, t)$. The linearized system is then

$$
\phi_{t t}+2 u_{*} \phi_{x t}+\left(u_{*}^{2}-a_{*}^{2}\right) \phi_{x x}=0
$$

This is a second-order PDE in the two independent variables $(t, x)$. To classify it, we write it in canonical matrix form.

## Principal coefficient matrix

Introduce the vector of derivatives

$$
\left(\begin{array}{ll}
\partial_{t} & \partial_{x}
\end{array}\right)
$$

so that the principal part can be written as

$$
\left(\begin{array}{ll}
\partial_{t} & \partial_{x}
\end{array}\right) \mathbf{K}_{1 D}\binom{\partial_{t}}{\partial_{x}} \phi=0
$$

where

$$
\mathbf{K}_{1 D}=\left(\begin{array}{cc}
1 & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}
\end{array}\right) .
$$

The qualitative behavior of the equation is determined entirely by the eigenvalues of this symmetric matrix.

## Eigenvalues of the coefficient matrix

The coefficient matrix is

$$
\mathbf{K}_{1 D}=\left(\begin{array}{cc}
1 & u_{*} \\
u_{*} & u_{*}^{2}-a_{*}^{2}
\end{array}\right) .
$$

To classify the equation, we compute its eigenvalues from

$$
\operatorname{det}\left(\mathbf{K}_{1 D}-\lambda I\right)=0 .
$$

A short calculation gives the characteristic polynomial

$$
\lambda^{2}-\left(1+u_{*}^{2}-a_{*}^{2}\right) \lambda-a_{*}^{2}=0
$$

Let

$$
A:=1+u_{*}^{2}-a_{*}^{2} .
$$

Then the eigenvalues are

$$
\lambda=\frac{A \pm \sqrt{A^{2}+4 a_{*}^{2}}}{2}
$$

The key observation is that

$$
A^{2}+4 a_{*}^{2}>A^{2}
$$

so that

$$
\sqrt{A^{2}+4 a_{*}^{2}}>|A|
$$

Therefore,

$$
A+\sqrt{A^{2}+4 a_{*}^{2}}>0, \quad A-\sqrt{A^{2}+4 a_{*}^{2}}<0 .
$$

Hence one eigenvalue is strictly positive and the other strictly negative for all $a_{*}>0$. That is,
The unsteady one-dimensional compressible potential equation is always hyperbolic.
This conclusion is independent of the Mach number. Compressible flow in one spatial dimension always supports wave propagation.

You will show in a homework that the two characteristic families along which the solution evolves are the straight lines

$$
x-\left(u_{*}+a_{*}\right) t=\text { constant }, \quad x-\left(u_{*}-a_{*}\right) t=\text { constant } .
$$

Physical interpretation. The solution decomposes into two traveling waves:

$$
\phi(x, t)=f\left(x-\left(u_{*}+a_{*}\right) t\right)+g\left(x-\left(u_{*}-a_{*}\right) t\right) .
$$

Disturbances propagate at speed $a_{*}$ relative to the fluid. In the laboratory frame, waves move with speeds $u_{*} \pm a_{*}$.

If $\left|u_{*}\right|<a_{*}$ (subsonic flow), one family of waves travels upstream. If $\left|u_{*}\right|>a_{*}$ (supersonic flow), both families move downstream, so upstream influence is lost.

This finite-speed propagation is the defining physical feature of hyperbolic behavior.

## 4 Steady two-dimensional compressible potential flow

We now turn to the second important reduction: steady flow depending only on the spatial variables $(x, y)$. Time derivatives vanish, and the frozen principal part of the linearized potential equation reduces to

$$
\left(a_{*}^{2}-u_{*}^{2}\right) \phi_{x x}+\left(a_{*}^{2}-v_{*}^{2}\right) \phi_{y y}-2 u_{*} v_{*} \phi_{x y}=0
$$

where $\left(u_{*}, v_{*}\right)$ is the locally frozen velocity and $a_{*}$ is the locally frozen sound speed.
This is a second-order scalar PDE in the two independent variables ( $x, y$ ). As in Lecture 11, its qualitative behavior is governed entirely by the matrix multiplying the highest derivatives.

## Principal coefficient matrix

Introduce the gradient operator in vector form,

$$
\left(\begin{array}{ll}
\partial_{x} & \partial_{y}
\end{array}\right)
$$

so that the principal part can be written compactly as

$$
\left(\begin{array}{ll}
\partial_{x} & \partial_{y}
\end{array}\right) \mathbf{K}_{2 D}\binom{\partial_{x}}{\partial_{y}} \phi=0
$$

where

$$
\mathbf{K}_{2 D}=\left(\begin{array}{cc}
a_{*}^{2}-u_{*}^{2} & -u_{*} v_{*} \\
-u_{*} v_{*} & a_{*}^{2}-v_{*}^{2}
\end{array}\right)
$$

A key structural observation is that this matrix can be written as

$$
\mathbf{K}_{2 D}=a_{*}^{2} \mathbf{I}-\boldsymbol{u}_{*} \boldsymbol{u}_{*}^{T}
$$

where

$$
\boldsymbol{u}_{*}=\binom{u_{*}}{v_{*}}
$$

This rank-one structure allows us to determine the eigenvalues without lengthy computation.

## Eigenstructure via rank-one form

Consider first the operator

$$
\boldsymbol{u}_{*} \boldsymbol{u}_{*}^{T}
$$

Acting on $\boldsymbol{u}_{*}$ itself gives

$$
\left(\boldsymbol{u}_{*} \boldsymbol{u}_{*}^{T}\right) \boldsymbol{u}_{*}=\boldsymbol{u}_{*}\left(\boldsymbol{u}_{*}^{T} \boldsymbol{u}_{*}\right)=\left|\boldsymbol{u}_{*}\right|^{2} \boldsymbol{u}_{*}
$$

Thus $\boldsymbol{u}_{*}$ is an eigenvector of this rank-one operator with eigenvalue $\left|\boldsymbol{u}_{*}\right|^{2}$.
Now take any vector $\boldsymbol{v}_{\perp}$ perpendicular to $\boldsymbol{u}_{*}$. Then $\boldsymbol{u}_{*}^{T} \boldsymbol{v}_{\perp}=0$, and therefore

$$
\left(\boldsymbol{u}_{*} \boldsymbol{u}_{*}^{T}\right) \boldsymbol{v}_{\perp}=\boldsymbol{u}_{*}\left(\boldsymbol{u}_{*}^{T} \boldsymbol{v}_{\perp}\right)=0
$$

So $\boldsymbol{v}_{\perp}$ is an eigenvector with eigenvalue 0 .
We now apply the full matrix

$$
\mathbf{K}_{2 D}=a_{*}^{2} \mathbf{I}-\boldsymbol{u}_{*} \boldsymbol{u}_{*}^{T}
$$

Since $\mathbf{I}$ leaves eigenvectors unchanged, the same eigenvectors diagonalize $\mathbf{K}_{2 D}$. Acting on the parallel direction,

$$
\mathbf{K}_{2 D} \boldsymbol{u}_{*}=a_{*}^{2} \boldsymbol{u}_{*}-\left|\boldsymbol{u}_{*}\right|^{2} \boldsymbol{u}_{*}=\left(a_{*}^{2}-\left|\boldsymbol{u}_{*}\right|^{2}\right) \boldsymbol{u}_{*} .
$$

Acting on the perpendicular direction,

$$
\mathbf{K}_{2 D} \boldsymbol{v}_{\perp}=a_{*}^{2} \boldsymbol{v}_{\perp}
$$

Thus the two eigenvalues are

$$
\lambda_{\|}=a_{*}^{2}-\left|u_{*}\right|^{2}, \quad \lambda_{\perp}=a_{*}^{2}
$$

Introduce the local Mach number

$$
M_{*}=\frac{\left|\boldsymbol{u}_{*}\right|}{a_{*}}
$$

Then

$$
\lambda_{\|}=a_{*}^{2}\left(1-M_{*}^{2}\right), \quad \lambda_{\perp}=a_{*}^{2}
$$

The type of the PDE is therefore determined entirely by the sign of $1-M_{*}^{2}$.

## Classification by Mach number

Subsonic flow: $M_{*}<1$. Both eigenvalues are positive. The equation is elliptic.
Ellipticity means that disturbances influence the entire spatial domain. To determine a solution in a region $\Omega \subset \mathbb{R}^{2}$, boundary data must be supplied along the entire boundary $\partial \Omega$.

A common mathematical condition is a Dirichlet boundary condition,

$$
\phi=\phi_{b} \quad \text { on } \partial \Omega .
$$

In the incompressible limit $M_{*} \rightarrow 0$, we recover Laplace's equation,

$$
\phi_{x x}+\phi_{y y}=0
$$

which is purely elliptic.

Sonic flow: $M_{*}=1$. Here $\lambda_{\|}=0$. The equation degenerates and changes type. This is the transition between subsonic and supersonic behavior. The governing equation is parabolic in the direction of the flow.

Supersonic flow: $M_{*}>1$. Now $\lambda_{\|}<0$ while $\lambda_{\perp}>0$. The equation is hyperbolic.
Hyperbolicity in steady flow means that information propagates along spatial characteristic curves. Unlike the elliptic case, boundary data are not prescribed everywhere, but only along portions of the boundary from which characteristics enter the domain.

Physically, disturbances are confined within a cone of influence. Upstream regions cannot feel downstream disturbances.

Thus the Mach number does more than measure compressibility: it determines the mathematical type of the governing equation.

## 5 The compressible streamfunction formulation

So far we have described irrotational compressible flow using a velocity potential,

$$
\boldsymbol{u}=\nabla \phi .
$$

There is an alternative representation built directly from mass conservation.

## Streamfunction in two dimensions

For steady two-dimensional compressible flow, continuity reads

$$
\partial_{x}(\rho u)+\partial_{y}(\rho v)=0
$$

This equation is satisfied identically if we define a scalar function $\psi(x, y)$ such that

$$
\rho u=\partial_{y} \psi, \quad \rho v=-\partial_{x} \psi
$$

Indeed,

$$
\partial_{x}(\rho u)+\partial_{y}(\rho v)=\partial_{x}\left(\psi_{y}\right)+\partial_{y}\left(-\psi_{x}\right)=\psi_{x y}-\psi_{y x}=0
$$

Thus mass conservation is built in by construction.

## Structural perspective

This representation reflects a deeper mathematical structure.
In two dimensions, a divergence-free vector field can be expressed as the perpendicular gradient of a scalar function. In three dimensions, a divergence-free vector field can be written as

$$
\boldsymbol{F}=\nabla \times \boldsymbol{A},
$$

for some vector potential $\boldsymbol{A}$.
These representations are special cases of the Hodge decomposition: vector fields may be decomposed into irrotational (gradient) and solenoidal (curl) components.

The velocity potential corresponds to the irrotational part. The streamfunction corresponds to a mass-conserving representation.

## Governing equation for the streamfunction

Using the streamfunction definition together with the thermodynamic relations, one can derive a second-order PDE for $\psi$. Its principal coefficient matrix has the same eigenstructure as that of the potential formulation.

Thus the classification by Mach number is identical: subsonic flow yields an elliptic equation, supersonic flow yields a hyperbolic equation, and the sonic case marks the transition.

The algebra differs. The structure does not.
We have now seen how compressibility, through the Mach number, governs not only the physics of wave propagation but the mathematical type of the governing equation itself.

