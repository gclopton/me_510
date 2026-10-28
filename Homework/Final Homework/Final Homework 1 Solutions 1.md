



**Instructions.** Show your reasoning clearly and keep your notation consistent. Unless stated otherwise, assume sufficient smoothness for the manipulations you perform. You may use results from the lecture notes without re-deriving them, but you must clearly explain how and why they apply.



> [!question]
> 
> **Problem 1:** Lagrangian and Eulerian perspectives
> 
> (30 points)
> 
> Let $q$ be a scalar quantity with Lagrangian and Eulerian representations
> 
> $$
> q^L\left(x_0, t\right), \quad q^E(x, t),
> $$
> 
> related through the flow map $x=\phi\left(x_0, t\right)$.
> Define the Eulerian time-derivative operator $d^E$ by
> 
> $$
> \left(d^E q\right)(\boldsymbol{x}, t):=\frac{\partial q^E}{\partial t}(\boldsymbol{x}, t),
> $$
> 
> and the Lagrangian time-derivative operator $d^L$ by
> 
> $$
> \left(d^L q\right)\left(x_0, t\right):=\frac{\partial q^L}{\partial t}\left(x_0, t\right) .
> $$
> 
> **(a) Eulerian derivative evaluated at a material point**
> 
> [10 pts]
> 
> Evaluate $\left(d^E q\right)$ at a material point $\boldsymbol{x}_0$.
> Your final answer should be expressed in terms of $q^L$ and the flow map. Clearly indicate how the chain rule is applied.
> 
> 
> 
> **(b) Lagrangian derivative in Eulerian form**
> 
> [10 pts]
> 
> Express ( $d^L q$ ) at a spatial point $\boldsymbol{x}$, and in terms of Eulerian variables $q^E(\boldsymbol{x}, t)$ and $\boldsymbol{u}^E(\boldsymbol{x}, t)$.
> Compare your result with part (a), and explain in 2-3 sentences how the two derivatives differ conceptually.
> 
> 
> 
> **(c) Conservation of mass in Lagrangian form**
> 
> [10 pts]
> 
> Starting from the Eulerian continuity equation
> 
> $$
> \partial_t \rho^E+\nabla \cdot\left(\rho^E \boldsymbol{u}^E\right)=0,
> $$
> 
> rewrite this equation in terms of Lagrangian variables.
> Your final expression should be written in terms of $\rho^L\left(x_0, t\right)$ and the motion of the fluid element.
> 
> Briefly explain which terms from the Eulerian form no longer appear explicitly, and why.
> 
> 





##### problem 1.a

Let

$$
\begin{aligned}
\boldsymbol{\psi}(\boldsymbol{x},t)
&=\phi^{-1}(\boldsymbol{x},t),\\
\boldsymbol{x}
&=\phi(\boldsymbol{x}_0,t),\\
\boldsymbol{F}(\boldsymbol{x}_0,t)
&=\nabla_{\boldsymbol{x}_0}\phi(\boldsymbol{x}_0,t).
\end{aligned}
$$

Then

$$
\begin{aligned}
q^L(\boldsymbol{x}_0,t)
&=q^E(\phi(\boldsymbol{x}_0,t),t),\\
q^E(\boldsymbol{x},t)
&=q^L(\phi^{-1}(\boldsymbol{x},t),t),\\
q^E(\boldsymbol{x},t)
&=q^L(\boldsymbol{\psi}(\boldsymbol{x},t),t).
\end{aligned}
$$

The Eulerian derivative is taken at fixed $\boldsymbol{x}$ first, and only afterward evaluated at the material point $\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)$:

$$
\begin{aligned}
\left(d^E q\right)(\phi(\boldsymbol{x}_0,t),t)
&=\left[\left.\frac{\partial q^E}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}\\
&=\left[\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}}q^L(\boldsymbol{\psi}(\boldsymbol{x},t),t)\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}\\
&=\left[
\frac{\partial q^L}{\partial t}(\boldsymbol{\psi}(\boldsymbol{x},t),t)
+\frac{\partial q^L}{\partial x_{0j}}(\boldsymbol{\psi}(\boldsymbol{x},t),t)
\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)
\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}\\
&=
\frac{\partial q^L}{\partial t}(\boldsymbol{x}_0,t)
+\frac{\partial q^L}{\partial x_{0j}}(\boldsymbol{x}_0,t)
\left[\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}.
\end{aligned}
$$

To express $\partial_t\boldsymbol{\psi}|_{\boldsymbol{x}}$ in terms of the flow map, differentiate the inverse-map identity at fixed $\boldsymbol{x}$:

$$
\begin{aligned}
\boldsymbol{x}
&=\phi(\boldsymbol{\psi}(\boldsymbol{x},t),t),\\
\boldsymbol{0}
&=\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}}\boldsymbol{x},\\
\boldsymbol{0}
&=\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}}\phi(\boldsymbol{\psi}(\boldsymbol{x},t),t),\\
0_i
&=\frac{\partial \phi_i}{\partial t}(\boldsymbol{\psi}(\boldsymbol{x},t),t)
+\frac{\partial \phi_i}{\partial x_{0j}}(\boldsymbol{\psi}(\boldsymbol{x},t),t)
\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t),\\
\frac{\partial \phi_i}{\partial x_{0j}}(\boldsymbol{\psi}(\boldsymbol{x},t),t)
\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)
&=-\frac{\partial \phi_i}{\partial t}(\boldsymbol{\psi}(\boldsymbol{x},t),t),\\
\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)
&=-\left[F^{-1}(\boldsymbol{\psi}(\boldsymbol{x},t),t)\right]_{ji}
\frac{\partial \phi_i}{\partial t}(\boldsymbol{\psi}(\boldsymbol{x},t),t),\\
\left[\left.\frac{\partial \psi_j}{\partial t}\right|_{\boldsymbol{x}}(\boldsymbol{x},t)\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}
&=-\left[F^{-1}(\boldsymbol{x}_0,t)\right]_{ji}
\frac{\partial \phi_i}{\partial t}(\boldsymbol{x}_0,t).
\end{aligned}
$$

Substituting this into the chain-rule expression gives

$$
\begin{aligned}
\left(d^E q\right)(\phi(\boldsymbol{x}_0,t),t)
&=
\frac{\partial q^L}{\partial t}(\boldsymbol{x}_0,t)
+\frac{\partial q^L}{\partial x_{0j}}(\boldsymbol{x}_0,t)
\left[
-\left[F^{-1}(\boldsymbol{x}_0,t)\right]_{ji}
\frac{\partial \phi_i}{\partial t}(\boldsymbol{x}_0,t)
\right]\\
&=
\frac{\partial q^L}{\partial t}(\boldsymbol{x}_0,t)
-\frac{\partial q^L}{\partial x_{0j}}(\boldsymbol{x}_0,t)
\left[F^{-1}(\boldsymbol{x}_0,t)\right]_{ji}
\frac{\partial \phi_i}{\partial t}(\boldsymbol{x}_0,t)\\
&=
\frac{\partial q^L}{\partial t}(\boldsymbol{x}_0,t)
-\nabla_{\boldsymbol{x}_0}q^L(\boldsymbol{x}_0,t)\cdot
\left[
\boldsymbol{F}^{-1}(\boldsymbol{x}_0,t)\frac{\partial \phi}{\partial t}(\boldsymbol{x}_0,t)
\right].
\end{aligned}
$$

Therefore

$$
\boxed{
\left(d^E q\right)(\phi(\boldsymbol{x}_0,t),t)
=
\frac{\partial q^L}{\partial t}(\boldsymbol{x}_0,t)
-\nabla_{\boldsymbol{x}_0}q^L(\boldsymbol{x}_0,t)\cdot
\boldsymbol{F}^{-1}(\boldsymbol{x}_0,t)\frac{\partial \phi}{\partial t}(\boldsymbol{x}_0,t)
}
$$

where $\boldsymbol{F}=\nabla_{\boldsymbol{x}_0}\phi$.


##### problem 1.b

The Lagrangian derivative is taken at fixed material label:

$$
\begin{aligned}
\left(d^L q\right)(\boldsymbol{x}_0,t)
&=\left.\frac{\partial q^L}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t),\\
q^L(\boldsymbol{x}_0,t)
&=q^E(\phi(\boldsymbol{x}_0,t),t).
\end{aligned}
$$

Thus

$$
\begin{aligned}
\left(d^L q\right)(\boldsymbol{x}_0,t)
&=\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}_0}q^L(\boldsymbol{x}_0,t)\\
&=\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}_0}q^E(\phi(\boldsymbol{x}_0,t),t)\\
&=
\frac{\partial q^E}{\partial t}(\phi(\boldsymbol{x}_0,t),t)
+\frac{\partial q^E}{\partial x_i}(\phi(\boldsymbol{x}_0,t),t)
\left.\frac{\partial \phi_i}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t).
\end{aligned}
$$

Define the Eulerian velocity by

$$
\begin{aligned}
\boldsymbol{u}^E(\boldsymbol{x},t)
&=
\left[
\left.\frac{\partial \phi}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t)
\right]_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x},t)}.
\end{aligned}
$$

Now evaluate the Lagrangian derivative at the spatial point $\boldsymbol{x}$ by setting $\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x},t)$:

$$
\begin{aligned}
\left(d^L q\right)^E(\boldsymbol{x},t)
&=
\left[
\left(d^L q\right)(\boldsymbol{x}_0,t)
\right]_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x},t)}\\
&=
\left[
\frac{\partial q^E}{\partial t}(\phi(\boldsymbol{x}_0,t),t)
+\frac{\partial q^E}{\partial x_i}(\phi(\boldsymbol{x}_0,t),t)
\left.\frac{\partial \phi_i}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t)
\right]_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x},t)}\\
&=
\frac{\partial q^E}{\partial t}(\boldsymbol{x},t)
+\frac{\partial q^E}{\partial x_i}(\boldsymbol{x},t)u_i^E(\boldsymbol{x},t)\\
&=
\frac{\partial q^E}{\partial t}(\boldsymbol{x},t)
+\boldsymbol{u}^E(\boldsymbol{x},t)\cdot\nabla q^E(\boldsymbol{x},t).
\end{aligned}
$$

Therefore

$$
\boxed{
\left(d^L q\right)^E(\boldsymbol{x},t)
=
\partial_t q^E(\boldsymbol{x},t)
+\boldsymbol{u}^E(\boldsymbol{x},t)\cdot\nabla q^E(\boldsymbol{x},t)
}
$$

At the same spatial point,

$$
\begin{aligned}
\left(d^L q\right)^E(\boldsymbol{x},t)-\left(d^E q\right)(\boldsymbol{x},t)
&=
\left[
\partial_t q^E(\boldsymbol{x},t)
+\boldsymbol{u}^E(\boldsymbol{x},t)\cdot\nabla q^E(\boldsymbol{x},t)
\right]
-\partial_t q^E(\boldsymbol{x},t)\\
&=
\boldsymbol{u}^E(\boldsymbol{x},t)\cdot\nabla q^E(\boldsymbol{x},t).
\end{aligned}
$$

The Eulerian derivative measures the time rate of change seen at a fixed spatial point. The Lagrangian derivative measures the time rate of change experienced by the moving material element, so it includes the additional convective term $\boldsymbol{u}^E\cdot\nabla q^E$.


##### problem 1.c

Start with the Eulerian continuity equation:

$$
\begin{aligned}
\partial_t \rho^E+\nabla\cdot(\rho^E\boldsymbol{u}^E)
&=0.
\end{aligned}
$$

Expand the divergence term:

$$
\begin{aligned}
0
&=\partial_t \rho^E+\nabla\cdot(\rho^E\boldsymbol{u}^E)\\
&=\partial_t \rho^E+\partial_{x_i}(\rho^E u_i^E)\\
&=\partial_t \rho^E+u_i^E\partial_{x_i}\rho^E+\rho^E\partial_{x_i}u_i^E\\
&=\partial_t \rho^E+\boldsymbol{u}^E\cdot\nabla\rho^E+\rho^E\nabla\cdot\boldsymbol{u}^E.
\end{aligned}
$$

Use

$$
\begin{aligned}
\rho^L(\boldsymbol{x}_0,t)
&=\rho^E(\phi(\boldsymbol{x}_0,t),t),\\
\boldsymbol{u}^E(\phi(\boldsymbol{x}_0,t),t)
&=\left.\frac{\partial \phi}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t).
\end{aligned}
$$

Then

$$
\begin{aligned}
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
&=\left.\frac{\partial}{\partial t}\right|_{\boldsymbol{x}_0}\rho^E(\phi(\boldsymbol{x}_0,t),t)\\
&=\partial_t\rho^E(\phi(\boldsymbol{x}_0,t),t)
+\frac{\partial\rho^E}{\partial x_i}(\phi(\boldsymbol{x}_0,t),t)
\left.\frac{\partial \phi_i}{\partial t}\right|_{\boldsymbol{x}_0}(\boldsymbol{x}_0,t)\\
&=\partial_t\rho^E(\phi(\boldsymbol{x}_0,t),t)
+\frac{\partial\rho^E}{\partial x_i}(\phi(\boldsymbol{x}_0,t),t)
u_i^E(\phi(\boldsymbol{x}_0,t),t)\\
&=\partial_t\rho^E(\phi(\boldsymbol{x}_0,t),t)
+\boldsymbol{u}^E(\phi(\boldsymbol{x}_0,t),t)\cdot
\nabla\rho^E(\phi(\boldsymbol{x}_0,t),t).
\end{aligned}
$$

Evaluate the expanded continuity equation at $\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)$:

$$
\begin{aligned}
0
&=\left[
\partial_t \rho^E+\boldsymbol{u}^E\cdot\nabla\rho^E+\rho^E\nabla\cdot\boldsymbol{u}^E
\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}\\
&=
\left[
\partial_t \rho^E+\boldsymbol{u}^E\cdot\nabla\rho^E
\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}
+
\left[
\rho^E\nabla\cdot\boldsymbol{u}^E
\right]_{\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)}\\
&=
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\left[\nabla\cdot\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t).
\end{aligned}
$$

Thus the primitive Lagrangian form is

$$
\boxed{
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\left[\nabla\cdot\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)
=0
}
$$

To write this entirely in terms of material volume change, define

$$
\begin{aligned}
\boldsymbol{F}(\boldsymbol{x}_0,t)
&=\nabla_{\boldsymbol{x}_0}\phi(\boldsymbol{x}_0,t),\\
J_\phi(\boldsymbol{x}_0,t)
&=\det \boldsymbol{F}(\boldsymbol{x}_0,t).
\end{aligned}
$$

Now compute the time derivative of $J_\phi$:

$$
\begin{aligned}
\frac{\partial J_\phi}{\partial t}
&=\frac{\partial}{\partial t}\det\boldsymbol{F}\\
&=J_\phi\operatorname{tr}\left(\boldsymbol{F}^{-1}\frac{\partial \boldsymbol{F}}{\partial t}\right)\\
&=J_\phi\operatorname{tr}\left(\boldsymbol{F}^{-1}
\frac{\partial}{\partial t}\nabla_{\boldsymbol{x}_0}\phi\right)\\
&=J_\phi\operatorname{tr}\left(\boldsymbol{F}^{-1}
\nabla_{\boldsymbol{x}_0}\frac{\partial\phi}{\partial t}\right)\\
&=J_\phi\operatorname{tr}\left(\boldsymbol{F}^{-1}
\nabla_{\boldsymbol{x}_0}\left[\boldsymbol{u}^E(\phi(\boldsymbol{x}_0,t),t)\right]\right)\\
&=J_\phi\operatorname{tr}\left(\boldsymbol{F}^{-1}
\left[\nabla_{\boldsymbol{x}}\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)\boldsymbol{F}\right)\\
&=J_\phi\operatorname{tr}\left(
\left[\nabla_{\boldsymbol{x}}\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)\boldsymbol{F}\boldsymbol{F}^{-1}
\right)\\
&=J_\phi\operatorname{tr}\left(
\left[\nabla_{\boldsymbol{x}}\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)
\right)\\
&=J_\phi\left[\nabla\cdot\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t).
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\left[\nabla\cdot\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)
&=\frac{1}{J_\phi(\boldsymbol{x}_0,t)}
\frac{\partial J_\phi}{\partial t}(\boldsymbol{x}_0,t).
\end{aligned}
$$

Substitute this into the Lagrangian continuity equation:

$$
\begin{aligned}
0
&=
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\left[\nabla\cdot\boldsymbol{u}^E\right](\phi(\boldsymbol{x}_0,t),t)\\
&=
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\frac{1}{J_\phi(\boldsymbol{x}_0,t)}
\frac{\partial J_\phi}{\partial t}(\boldsymbol{x}_0,t)\\
0
&=
J_\phi(\boldsymbol{x}_0,t)
\left[
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\frac{1}{J_\phi(\boldsymbol{x}_0,t)}
\frac{\partial J_\phi}{\partial t}(\boldsymbol{x}_0,t)
\right]\\
&=
J_\phi(\boldsymbol{x}_0,t)
\frac{\partial \rho^L}{\partial t}(\boldsymbol{x}_0,t)
+\rho^L(\boldsymbol{x}_0,t)
\frac{\partial J_\phi}{\partial t}(\boldsymbol{x}_0,t)\\
0
&=
\frac{\partial}{\partial t}
\left[
\rho^L(\boldsymbol{x}_0,t)J_\phi(\boldsymbol{x}_0,t)
\right].
\end{aligned}
$$

Thus

$$
\boxed{
\frac{\partial}{\partial t}
\left[
\rho^L(\boldsymbol{x}_0,t)J_\phi(\boldsymbol{x}_0,t)
\right]
=0
}
$$

and hence

$$
\begin{aligned}
\rho^L(\boldsymbol{x}_0,t)J_\phi(\boldsymbol{x}_0,t)
&=\rho^L(\boldsymbol{x}_0,0)J_\phi(\boldsymbol{x}_0,0)\\
&=\rho_0(\boldsymbol{x}_0).
\end{aligned}
$$

If $J_\phi(\boldsymbol{x}_0,0)=1$, then

$$
\boxed{
\rho^L(\boldsymbol{x}_0,t)
=
\frac{\rho_0(\boldsymbol{x}_0)}{J_\phi(\boldsymbol{x}_0,t)}
}
$$

The Eulerian flux term $\nabla\cdot(\rho^E\boldsymbol{u}^E)$ no longer appears as a separate flux through a fixed spatial control volume. In the Lagrangian description the same material element is followed, so advection by $\boldsymbol{u}^E$ is absorbed into the fixed-label derivative and compression or expansion is carried by the Jacobian $J_\phi$.



> [!question]
> **Problem 2:** Hyperbolic structure of compressible flow
> 
> (40 points)
> 
> In this problem, we compare the structure of compressible-flow equations written in second-order and first-order form.
> 
> Second-order formulation
> Consider the PDE
> 
> $$
> A \phi_{x x}+2 B \phi_{x y}+C \phi_{y y}=0 .
> $$
> 
> **(a) Diagonalization of the principal part**
> 
> [10 pts]
> 
> Write the principal part in matrix form using
> 
> $$
> \boldsymbol{K}=\left[\begin{array}{ll}
> A & B \\
> B & C
> \end{array}\right]
> $$
> 
> 
> Assuming $\boldsymbol{K}=\boldsymbol{V} \boldsymbol{\Lambda} \boldsymbol{V}^T$, transform the PDE into a coordinate system in which no crossderivative terms appear.
> 
> 
> **(b) Hyperbolicity and characteristic directions**
> 
> [10 pts]
> (i) State the condition on $A, B$, and $C$ under which the PDE is hyperbolic, and assume these conditions are met for the remainder of the problem.
> (ii) Write the transformed PDE in a form that makes this hyperbolicity explicit.
> (iii) Identify the characteristic directions in the original $(x, y)$ coordinates.
> 
> First-order formulation
> Now consider the system
> 
> $$
> \boldsymbol{A}(\boldsymbol{q}) \boldsymbol{q}_x+\boldsymbol{B}(\boldsymbol{q}) \boldsymbol{q}_y=0
> $$
> 
> **(c) Reduction along characteristic curves**
> 
> [10 pts]
> 
> Let $\boldsymbol{\alpha}^T$ and $\lambda$ satisfy
> 
> $$
> \boldsymbol{\alpha}^T \boldsymbol{B}=\lambda \boldsymbol{\alpha}^T \boldsymbol{A} .
> $$
> 
> 
> Consider a curve $y(x)$ such that $\frac{d y}{d x}=\lambda$.
> Show that along this curve, the system reduces to an ordinary differential equation involving a single derivative with respect to $x$.
> From this result:
> (i) explain why the system is hyperbolic,
> (ii) identify the characteristic directions.
> 
> 
> **(d) Structural comparison**
> 
> [10 pts]
> 
> Complete the following table:
> 
> 
>
>
> | Feature | Second-order PDE | First-order system |
> | :---: | :--- | :--- |
> | Role of eigenvalues |  |  |
> | Role of eigenvectors |  |  |
> | Condition for hyperbolicity |  |  |
> | Meaning of characteristic directions |  |  |
> 
> 
> 






##### problem 2.a

Let

$$
\begin{aligned}
\boldsymbol{r}
&=
\binom{x}{y},\\
\nabla_{\boldsymbol{r}}
&=
\binom{\partial_x}{\partial_y},\\
\boldsymbol{K}
&=
\left[
\begin{array}{cc}
A & B\\
B & C
\end{array}
\right].
\end{aligned}
$$

Then the principal part can be written as

$$
\begin{aligned}
\left(\begin{array}{cc}\partial_x&\partial_y\end{array}\right)
\boldsymbol{K}
\binom{\partial_x}{\partial_y}\phi
&=
\left(\begin{array}{cc}\partial_x&\partial_y\end{array}\right)
\left[
\begin{array}{cc}
A & B\\
B & C
\end{array}
\right]
\binom{\partial_x\phi}{\partial_y\phi}\\
&=
\left(\begin{array}{cc}\partial_x&\partial_y\end{array}\right)
\binom{A\partial_x\phi+B\partial_y\phi}{B\partial_x\phi+C\partial_y\phi}\\
&=
\partial_x(A\partial_x\phi+B\partial_y\phi)
+\partial_y(B\partial_x\phi+C\partial_y\phi).
\end{aligned}
$$

Since $A,B,C$ are the frozen principal coefficients,

$$
\begin{aligned}
\partial_x(A\partial_x\phi+B\partial_y\phi)
+\partial_y(B\partial_x\phi+C\partial_y\phi)
&=
A\partial_{xx}\phi
+B\partial_{xy}\phi
+B\partial_{yx}\phi
+C\partial_{yy}\phi\\
&=
A\phi_{xx}
+B\phi_{xy}
+B\phi_{xy}
+C\phi_{yy}\\
&=
A\phi_{xx}
+2B\phi_{xy}
+C\phi_{yy}.
\end{aligned}
$$

Thus

$$
\begin{aligned}
A\phi_{xx}+2B\phi_{xy}+C\phi_{yy}
&=
\nabla_{\boldsymbol{r}}^T\boldsymbol{K}\nabla_{\boldsymbol{r}}\phi.
\end{aligned}
$$

Because $\boldsymbol{K}$ is symmetric, write

$$
\begin{aligned}
\boldsymbol{K}
&=
\boldsymbol{V}\boldsymbol{\Lambda}\boldsymbol{V}^T,\\
\boldsymbol{V}^T\boldsymbol{V}
&=
\boldsymbol{I},\\
\boldsymbol{\Lambda}
&=
\left[
\begin{array}{cc}
\lambda_1 & 0\\
0 & \lambda_2
\end{array}
\right].
\end{aligned}
$$

Introduce the rotated coordinates

$$
\begin{aligned}
\boldsymbol{r}'
&=
\binom{\xi}{\zeta}
=
\boldsymbol{V}^T\boldsymbol{r},\\
\boldsymbol{r}
&=
\boldsymbol{V}\boldsymbol{r}'.
\end{aligned}
$$

The chain rule gives the derivative transformation

$$
\begin{aligned}
\nabla_{\boldsymbol{r}}\phi
&=
\left(\frac{\partial \boldsymbol{r}'}{\partial \boldsymbol{r}}\right)^T
\nabla_{\boldsymbol{r}'}\phi\\
&=
\left(\boldsymbol{V}^T\right)^T
\nabla_{\boldsymbol{r}'}\phi\\
&=
\boldsymbol{V}\nabla_{\boldsymbol{r}'}\phi.
\end{aligned}
$$

Equivalently, at the operator level,

$$
\begin{aligned}
\nabla_{\boldsymbol{r}}
&=
\boldsymbol{V}\nabla_{\boldsymbol{r}'},\\
\nabla_{\boldsymbol{r}}^T
&=
\nabla_{\boldsymbol{r}'}^T\boldsymbol{V}^T.
\end{aligned}
$$

Substitute these into the principal part:

$$
\begin{aligned}
\nabla_{\boldsymbol{r}}^T\boldsymbol{K}\nabla_{\boldsymbol{r}}\phi
&=
\left(\boldsymbol{V}\nabla_{\boldsymbol{r}'}\right)^T
\boldsymbol{K}
\left(\boldsymbol{V}\nabla_{\boldsymbol{r}'}\right)\phi\\
&=
\nabla_{\boldsymbol{r}'}^T\boldsymbol{V}^T
\boldsymbol{K}
\boldsymbol{V}\nabla_{\boldsymbol{r}'}\phi\\
&=
\nabla_{\boldsymbol{r}'}^T\boldsymbol{V}^T
\left(\boldsymbol{V}\boldsymbol{\Lambda}\boldsymbol{V}^T\right)
\boldsymbol{V}\nabla_{\boldsymbol{r}'}\phi\\
&=
\nabla_{\boldsymbol{r}'}^T
\left(\boldsymbol{V}^T\boldsymbol{V}\right)
\boldsymbol{\Lambda}
\left(\boldsymbol{V}^T\boldsymbol{V}\right)
\nabla_{\boldsymbol{r}'}\phi\\
&=
\nabla_{\boldsymbol{r}'}^T
\boldsymbol{I}
\boldsymbol{\Lambda}
\boldsymbol{I}
\nabla_{\boldsymbol{r}'}\phi\\
&=
\nabla_{\boldsymbol{r}'}^T
\boldsymbol{\Lambda}
\nabla_{\boldsymbol{r}'}\phi\\
&=
\left(\begin{array}{cc}\partial_\xi&\partial_\zeta\end{array}\right)
\left[
\begin{array}{cc}
\lambda_1 & 0\\
0 & \lambda_2
\end{array}
\right]
\binom{\partial_\xi}{\partial_\zeta}\phi\\
&=
\left(\begin{array}{cc}\partial_\xi&\partial_\zeta\end{array}\right)
\binom{\lambda_1\partial_\xi\phi}{\lambda_2\partial_\zeta\phi}\\
&=
\lambda_1\partial_{\xi\xi}\phi+\lambda_2\partial_{\zeta\zeta}\phi\\
&=
\lambda_1\phi_{\xi\xi}+\lambda_2\phi_{\zeta\zeta}.
\end{aligned}
$$

Therefore, in the rotated coordinate system,

$$
\boxed{
\lambda_1\phi_{\xi\xi}+\lambda_2\phi_{\zeta\zeta}=0
}
$$

and no cross-derivative term appears.


##### problem 2.b

The coefficient matrix is

$$
\begin{aligned}
\boldsymbol{K}
&=
\left[
\begin{array}{cc}
A & B\\
B & C
\end{array}
\right].
\end{aligned}
$$

Its determinant is

$$
\begin{aligned}
\det\boldsymbol{K}
&=
\left|
\begin{array}{cc}
A & B\\
B & C
\end{array}
\right|\\
&=
AC-B^2.
\end{aligned}
$$

Since $\det\boldsymbol{K}=\lambda_1\lambda_2$,

$$
\begin{aligned}
\lambda_1\lambda_2<0
&\Longleftrightarrow
\det\boldsymbol{K}<0\\
&\Longleftrightarrow
AC-B^2<0\\
&\Longleftrightarrow
B^2-AC>0.
\end{aligned}
$$

Thus the second-order equation is hyperbolic when

$$
\boxed{
B^2-AC>0.
}
$$

Assume the eigenvalues have been ordered so that

$$
\begin{aligned}
\lambda_1&>0,\\
\lambda_2&<0.
\end{aligned}
$$

Define

$$
\begin{aligned}
a&=\sqrt{\lambda_1},\\
b&=\sqrt{-\lambda_2}.
\end{aligned}
$$

Then

$$
\begin{aligned}
\lambda_1\phi_{\xi\xi}+\lambda_2\phi_{\zeta\zeta}
&=0\\
a^2\phi_{\xi\xi}-b^2\phi_{\zeta\zeta}
&=0\\
\left(a\partial_\xi+b\partial_\zeta\right)
\left(a\partial_\xi-b\partial_\zeta\right)\phi
&=0.
\end{aligned}
$$

The characteristic variables are found by taking the combinations annihilated by the first-order factors. For the factor $a\partial_\xi-b\partial_\zeta$,

$$
\begin{aligned}
\eta
&=
b\xi+a\zeta,\\
\left(a\partial_\xi-b\partial_\zeta\right)\eta
&=
a\partial_\xi(b\xi+a\zeta)
-b\partial_\zeta(b\xi+a\zeta)\\
&=
a b-b a\\
&=
0.
\end{aligned}
$$

For the factor $a\partial_\xi+b\partial_\zeta$,

$$
\begin{aligned}
\mu
&=
b\xi-a\zeta,\\
\left(a\partial_\xi+b\partial_\zeta\right)\mu
&=
a\partial_\xi(b\xi-a\zeta)
+b\partial_\zeta(b\xi-a\zeta)\\
&=
a b+b(-a)\\
&=
ab-ab\\
&=
0.
\end{aligned}
$$

So the two characteristic families in canonical coordinates are

$$
\boxed{
b\xi+a\zeta=\text{constant},
\qquad
b\xi-a\zeta=\text{constant}.
}
$$

Equivalently,

$$
\boxed{
\zeta=\mp\frac{b}{a}\xi+\text{constant}.
}
$$

To transform these families back to the original $(x,y)$ coordinates, write the columns of $\boldsymbol{V}$ as

$$
\begin{aligned}
\boldsymbol{V}
&=
\left[
\begin{array}{cc}
\boldsymbol{e}_1 & \boldsymbol{e}_2
\end{array}
\right],
\end{aligned}
$$

so that

$$
\begin{aligned}
\binom{\xi}{\zeta}
&=
\boldsymbol{V}^T\binom{x}{y},\\
\xi
&=
\boldsymbol{e}_1^T\binom{x}{y},\\
\zeta
&=
\boldsymbol{e}_2^T\binom{x}{y}.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
b\xi+a\zeta
&=
b\boldsymbol{e}_1^T\binom{x}{y}
+a\boldsymbol{e}_2^T\binom{x}{y}\\
&=
\left(b\boldsymbol{e}_1+a\boldsymbol{e}_2\right)^T
\binom{x}{y},
\end{aligned}
$$

and

$$
\begin{aligned}
b\xi-a\zeta
&=
b\boldsymbol{e}_1^T\binom{x}{y}
-a\boldsymbol{e}_2^T\binom{x}{y}\\
&=
\left(b\boldsymbol{e}_1-a\boldsymbol{e}_2\right)^T
\binom{x}{y}.
\end{aligned}
$$

Thus the characteristic line families in the original coordinates are

$$
\boxed{
\left(b\boldsymbol{e}_1+a\boldsymbol{e}_2\right)^T
\binom{x}{y}
=\text{constant},
\qquad
\left(b\boldsymbol{e}_1-a\boldsymbol{e}_2\right)^T
\binom{x}{y}
=\text{constant}.
}
$$

Equivalently, the line directions are perpendicular to those normals:

$$
\boxed{
\boldsymbol{d}_+
=
a\boldsymbol{e}_1-b\boldsymbol{e}_2,
\qquad
\boldsymbol{d}_-
=
a\boldsymbol{e}_1+b\boldsymbol{e}_2.
}
$$

The same characteristic directions can be written directly as slopes in the original coordinates. Let a characteristic line have slope

$$
\begin{aligned}
m&=\frac{dy}{dx}.
\end{aligned}
$$

Then a line with slope $m$ can be written as

$$
\begin{aligned}
y-mx&=\text{constant}.
\end{aligned}
$$

Its normal vector is

$$
\begin{aligned}
\boldsymbol{n}
&=
\binom{-m}{1}.
\end{aligned}
$$

The characteristic condition is that the principal symbol vanish on this normal:

$$
\begin{aligned}
\boldsymbol{n}^T\boldsymbol{K}\boldsymbol{n}
&=0.
\end{aligned}
$$

Expanding,

$$
\begin{aligned}
0
&=
\left(\begin{array}{cc}-m&1\end{array}\right)
\left[
\begin{array}{cc}
A & B\\
B & C
\end{array}
\right]
\binom{-m}{1}\\
&=
\left(\begin{array}{cc}-m&1\end{array}\right)
\binom{-Am+B}{-Bm+C}\\
&=
(-m)(-Am+B)+1(-Bm+C)\\
&=
Am^2-Bm-Bm+C\\
&=
Am^2-2Bm+C.
\end{aligned}
$$

Therefore

$$
\boxed{
A\left(\frac{dy}{dx}\right)^2
-2B\left(\frac{dy}{dx}\right)
+C
=0.
}
$$

If $A\neq 0$, this gives

$$
\boxed{
\frac{dy}{dx}
=
\frac{B\pm\sqrt{B^2-AC}}{A}.
}
$$


##### problem 2.c

Start with the first-order system

$$
\begin{aligned}
\boldsymbol{A}(\boldsymbol{q})\boldsymbol{q}_x
+\boldsymbol{B}(\boldsymbol{q})\boldsymbol{q}_y
&=
\boldsymbol{0}.
\end{aligned}
$$

Let $\boldsymbol{\alpha}^T$ and $\lambda$ satisfy

$$
\begin{aligned}
\boldsymbol{\alpha}^T\boldsymbol{B}
&=
\lambda\boldsymbol{\alpha}^T\boldsymbol{A}.
\end{aligned}
$$

Move all terms to one side:

$$
\begin{aligned}
\boldsymbol{\alpha}^T\boldsymbol{B}
-\lambda\boldsymbol{\alpha}^T\boldsymbol{A}
&=
\boldsymbol{0}^T,\\
\boldsymbol{\alpha}^T
\left(\boldsymbol{B}-\lambda\boldsymbol{A}\right)
&=
\boldsymbol{0}^T.
\end{aligned}
$$

Now premultiply the PDE system by $\boldsymbol{\alpha}^T$:

$$
\begin{aligned}
\boldsymbol{\alpha}^T
\left[
\boldsymbol{A}\boldsymbol{q}_x
+\boldsymbol{B}\boldsymbol{q}_y
\right]
&=
\boldsymbol{\alpha}^T\boldsymbol{0}\\
\boldsymbol{\alpha}^T\boldsymbol{A}\boldsymbol{q}_x
+\boldsymbol{\alpha}^T\boldsymbol{B}\boldsymbol{q}_y
&=
0\\
\boldsymbol{\alpha}^T\boldsymbol{A}\boldsymbol{q}_x
+\lambda\boldsymbol{\alpha}^T\boldsymbol{A}\boldsymbol{q}_y
&=
0\\
\boldsymbol{\alpha}^T\boldsymbol{A}
\left(
\boldsymbol{q}_x+\lambda\boldsymbol{q}_y
\right)
&=
0.
\end{aligned}
$$

Along a curve $y=y(x)$,

$$
\begin{aligned}
\frac{d\boldsymbol{q}}{dx}
&=
\frac{\partial\boldsymbol{q}}{\partial x}
+\frac{\partial\boldsymbol{q}}{\partial y}\frac{dy}{dx}\\
&=
\boldsymbol{q}_x+\boldsymbol{q}_y\frac{dy}{dx}.
\end{aligned}
$$

If

$$
\begin{aligned}
\frac{dy}{dx}&=\lambda,
\end{aligned}
$$

then

$$
\begin{aligned}
\frac{d\boldsymbol{q}}{dx}
&=
\boldsymbol{q}_x+\lambda\boldsymbol{q}_y.
\end{aligned}
$$

Substitute this into the premultiplied equation:

$$
\begin{aligned}
\boldsymbol{\alpha}^T\boldsymbol{A}
\left(
\boldsymbol{q}_x+\lambda\boldsymbol{q}_y
\right)
&=
0\\
\boldsymbol{\alpha}^T\boldsymbol{A}
\frac{d\boldsymbol{q}}{dx}
&=
0.
\end{aligned}
$$

Therefore, along the curve $dy/dx=\lambda$,

$$
\boxed{
\boldsymbol{\alpha}^T\boldsymbol{A}(\boldsymbol{q})
\frac{d\boldsymbol{q}}{dx}
=0.
}
$$

This is an ordinary differential equation along the characteristic curve because the only derivative that remains is the total derivative with respect to $x$ along $y(x)$.

For a nonzero vector $\boldsymbol{\alpha}$ to exist,

$$
\begin{aligned}
\boldsymbol{\alpha}^T
\left(\boldsymbol{B}-\lambda\boldsymbol{A}\right)
&=
\boldsymbol{0}^T
\end{aligned}
$$

must have a nontrivial left null vector. Hence

$$
\begin{aligned}
\det\left(\boldsymbol{B}-\lambda\boldsymbol{A}\right)
&=
0.
\end{aligned}
$$

The characteristic slopes are therefore the roots $\lambda_i$ of

$$
\boxed{
\det\left(\boldsymbol{B}-\lambda\boldsymbol{A}\right)=0,
\qquad
\frac{dy}{dx}=\lambda_i.
}
$$

The system is hyperbolic when these characteristic slopes are real and when there are enough independent characteristic directions, equivalently enough independent eigenvectors or left projections, to decompose the system into characteristic ODEs. The characteristic directions are the curves satisfying

$$
\boxed{
\frac{dy}{dx}=\lambda_i.
}
$$


##### problem 2.d

|               Feature                | Second-order PDE                                                                                                                                                                                                                       | First-order system                                                                                                                                                                                    |
| :----------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         Role of eigenvalues          | The eigenvalues $\lambda_1,\lambda_2$ of $\boldsymbol{K}$ become the coefficients of the pure second derivatives after rotation $\lambda_1\phi_{\xi\xi}+\lambda_2\phi_{\zeta\zeta}=0$. Their signs determine the type of the equation. | The values $\lambda_i$ from $\det(\boldsymbol{B}-\lambda\boldsymbol{A})=0$ are the slopes $dy/dx=\lambda_i$ of characteristic curves.                                                                 |
|         Role of eigenvectors         | The eigenvectors of $\boldsymbol{K}$ form the columns of $\boldsymbol{V}$ and define the rotated coordinates $(\xi,\zeta)^T=\boldsymbol{V}^T(x,y)^T$ in which the cross derivative disappears.                                         | The left vectors $\boldsymbol{\alpha}_i^T$ select the linear combinations of equations that reduce to ODEs: $\boldsymbol{\alpha}_i^T\boldsymbol{A}\,d\boldsymbol{q}/dx=0$ along $dy/dx=\lambda_i$.    |
|     Condition for hyperbolicity      | Hyperbolicity requires opposite-sign eigenvalues of $\boldsymbol{K}$, so $\lambda_1\lambda_2<0$, equivalently $B^2-AC>0$.                                                                                                              | Hyperbolicity requires real characteristic slopes $\lambda_i$ and a complete enough set of independent characteristic projections/eigenvectors to reduce the system along real characteristic curves. |
| Meaning of characteristic directions | They are the line families along which the factored hyperbolic operator reduces the second-order equation into first-order propagation directions. In canonical coordinates they are $b\xi\pm a\zeta=\text{constant}$.                 | They are curves $dy/dx=\lambda_i$ along which the PDE system reduces to ODE compatibility relations for selected combinations of the unknowns.                                                        |



> [!question]
> 
> **Problem 3:** Shock tube problem
> 
> (30 points)
> 
> We consider a one-dimensional shock tube containing a calorically perfect gas with $\gamma=1.4$.
> At time $t=0$, the gas is at rest and separated into two regions:
> 
> $$
> \begin{aligned}
> \text { Region } 4 \text { (left): } & \rho_4=1.0 \mathrm{~kg} / \mathrm{m}^3, \quad p_4=100,000 \mathrm{~Pa}, \\
> \text { Region } 1 \text { (right): } & \rho_1=0.125 \mathrm{~kg} / \mathrm{m}^3, \quad p_1=10,000 \mathrm{~Pa},
> \end{aligned}
> $$
> 
> with $u_1=u_4=0$.
> 
> 
> **(a) Wave structure**
> 
> [8 pts]
> 
> Sketch the $x-t$ diagram and identify:
> - the expansion fan,
> - the contact discontinuity,
> - the shock.
> 
> Clearly label all regions.
> 
> 
> 
> **(b) Solution strategy**
> 
> [8 pts]
> 
> Describe the procedure used to determine the intermediate states.
> Your answer should:
> - identify the relations used in each region,
> - explain how the unknown pressure is determined.
> 
> 
> 
> **(c) Numerical solution**
> 
> [8 pts]
> 
> Compute the solution at time
> 
> $$
> t=0.01 \mathrm{~s} .
> $$
> 
> 
> Plot:
> 
> $$
> \rho(x), \quad u(x), \quad p(x) .
> $$
> 
> 
> 
> 
> **(d) Characteristic-based visualization**
> 
> [6 pts]
> 
> Using code, update your sketch from part (a) to plot the actual characteristic curves for this problem in the $x-t$ plane.
> Your plot should clearly show:
> - both characteristic families,
> - the expansion fan,
> - the shock trajectory.
> 
> 
>


##### problem 3.a

The initial state has high pressure on the left and low pressure on the right:

$$
\begin{aligned}
\text{Region 4:}\qquad
&\rho_4=1.0\ \mathrm{kg/m^3},
\qquad
p_4=100000\ \mathrm{Pa},
\qquad
u_4=0,\\
\text{Region 1:}\qquad
&\rho_1=0.125\ \mathrm{kg/m^3},
\qquad
p_1=10000\ \mathrm{Pa},
\qquad
u_1=0.
\end{aligned}
$$

Since $p_4>p_1$, the diaphragm rupture sends an expansion fan into the high-pressure gas on the left and a shock into the low-pressure gas on the right. The two intermediate constant states are separated by a contact discontinuity. Thus the wave ordering from left to right is

$$
\boxed{
\text{Region 4}
\quad\longrightarrow\quad
\text{expansion fan}
\quad\longrightarrow\quad
\text{Region 3}
\quad\longrightarrow\quad
\text{contact}
\quad\longrightarrow\quad
\text{Region 2}
\quad\longrightarrow\quad
\text{shock}
\quad\longrightarrow\quad
\text{Region 1}.
}
$$

The contact discontinuity carries a density jump, but pressure and velocity are continuous across it:

$$
\begin{aligned}
u_2&=u_3=u_*,\\
p_2&=p_3=p_*,\\
\rho_2&\neq \rho_3.
\end{aligned}
$$

The wave trajectories in the $x$-$t$ plane are

$$
\begin{aligned}
\text{fan head:}\qquad &x=(u_4-a_4)t,\\
\text{fan tail:}\qquad &x=(u_*-a_3)t,\\
\text{contact:}\qquad &x=u_*t,\\
\text{shock:}\qquad &x=u_s t.
\end{aligned}
$$

For the computed states below, the sketch is:

![[images/problem3_wave_structure.png|700]]


##### problem 3.b

The sound speeds in the initial left and right states are

$$
\begin{aligned}
a_4
&=
\sqrt{\frac{\gamma p_4}{\rho_4}},\\
a_1
&=
\sqrt{\frac{\gamma p_1}{\rho_1}}.
\end{aligned}
$$

The expansion from Region 4 to Region 3 is isentropic. Therefore

$$
\begin{aligned}
\frac{\rho_3}{\rho_4}
&=
\left(\frac{p_*}{p_4}\right)^{1/\gamma},\\
\frac{a_3}{a_4}
&=
\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}.
\end{aligned}
$$

Across the left-going expansion fan, the invariant

$$
\begin{aligned}
I_+
&=
u+\frac{2a}{\gamma-1}
\end{aligned}
$$

is constant. Thus

$$
\begin{aligned}
u_3+\frac{2a_3}{\gamma-1}
&=
u_4+\frac{2a_4}{\gamma-1},\\
u_*+\frac{2a_4}{\gamma-1}
\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}
&=
u_4+\frac{2a_4}{\gamma-1},\\
u_*
&=
u_4+\frac{2a_4}{\gamma-1}
\left[
1-\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}
\right].
\end{aligned}
$$

Across the right-moving shock from Region 1 to Region 2, the Rankine-Hugoniot jump conditions give the shock-side relation

$$
\begin{aligned}
u_*
&=
u_1+
(p_*-p_1)
\left[
\frac{2}{(\gamma+1)\rho_1}
\frac{1}{p_*+\frac{\gamma-1}{\gamma+1}p_1}
\right]^{1/2}.
\end{aligned}
$$

The unknown pressure $p_*$ is determined by equating the expansion-side and shock-side values of $u_*$. Therefore $p_*$ solves

$$
\boxed{
u_4+\frac{2a_4}{\gamma-1}
\left[
1-\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}
\right]
-
u_1
-
(p_*-p_1)
\left[
\frac{2}{(\gamma+1)\rho_1}
\frac{1}{p_*+\frac{\gamma-1}{\gamma+1}p_1}
\right]^{1/2}
=0.
}
$$

After $p_*$ is known, compute

$$
\begin{aligned}
u_*
&=
u_4+\frac{2a_4}{\gamma-1}
\left[
1-\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}
\right],\\
\rho_3
&=
\rho_4\left(\frac{p_*}{p_4}\right)^{1/\gamma},\\
a_3
&=
a_4\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)},\\
\rho_2
&=
\rho_1
\frac{\frac{p_*}{p_1}+\frac{\gamma-1}{\gamma+1}}
{1+\frac{\gamma-1}{\gamma+1}\frac{p_*}{p_1}},\\
a_2
&=
\sqrt{\frac{\gamma p_*}{\rho_2}},\\
u_s
&=
\frac{\rho_2u_*}{\rho_2-\rho_1}.
\end{aligned}
$$


##### problem 3.c

For $\gamma=1.4$, the initial sound speeds are

$$
\begin{aligned}
a_4
&=
\sqrt{\frac{(1.4)(100000)}{1.0}}\\
&=
374.1657\ \mathrm{m/s},\\
a_1
&=
\sqrt{\frac{(1.4)(10000)}{0.125}}\\
&=
334.6640\ \mathrm{m/s}.
\end{aligned}
$$

Solving the scalar pressure equation gives

$$
\begin{aligned}
p_*&=30313.0178\ \mathrm{Pa},\\
u_*&=293.2863\ \mathrm{m/s},\\
\rho_3&=0.426319\ \mathrm{kg/m^3},\\
a_3&=315.5085\ \mathrm{m/s},\\
\rho_2&=0.265574\ \mathrm{kg/m^3},\\
a_2&=399.7478\ \mathrm{m/s},\\
u_s&=554.0803\ \mathrm{m/s}.
\end{aligned}
$$

Use the similarity variable

$$
\begin{aligned}
\xi&=\frac{x}{t}.
\end{aligned}
$$

The fan boundaries and discontinuity speeds are

$$
\begin{aligned}
\xi_{\mathrm{head}}
&=
u_4-a_4\\
&=
-374.1657\ \mathrm{m/s},\\
\xi_{\mathrm{tail}}
&=
u_*-a_3\\
&=
-22.2222\ \mathrm{m/s},\\
\xi_{\mathrm{contact}}
&=
u_*\\
&=
293.2863\ \mathrm{m/s},\\
\xi_{\mathrm{shock}}
&=
u_s\\
&=
554.0803\ \mathrm{m/s}.
\end{aligned}
$$

At $t=0.01\ \mathrm{s}$, these become

$$
\begin{aligned}
x_{\mathrm{head}}
&=
\xi_{\mathrm{head}}t\\
&=
-3.7417\ \mathrm{m},\\
x_{\mathrm{tail}}
&=
\xi_{\mathrm{tail}}t\\
&=
-0.2222\ \mathrm{m},\\
x_{\mathrm{contact}}
&=
u_*t\\
&=
2.9329\ \mathrm{m},\\
x_{\mathrm{shock}}
&=
u_s t\\
&=
5.5408\ \mathrm{m}.
\end{aligned}
$$

Inside the expansion fan,

$$
\begin{aligned}
a(\xi)
&=
\frac{\gamma-1}{\gamma+1}
\left(
u_4+\frac{2a_4}{\gamma-1}-\xi
\right),\\
u(\xi)
&=
\xi+a(\xi),\\
\rho(\xi)
&=
\rho_4\left(\frac{a(\xi)}{a_4}\right)^{2/(\gamma-1)},\\
p(\xi)
&=
p_4\left(\frac{a(\xi)}{a_4}\right)^{2\gamma/(\gamma-1)}.
\end{aligned}
$$

Therefore the full solution at $t=0.01\ \mathrm{s}$ is

$$
\begin{aligned}
(\rho,u,p)(x,t)
&=
\begin{cases}
(\rho_4,u_4,p_4),
& \xi<u_4-a_4,\\
(\rho(\xi),u(\xi),p(\xi)),
& u_4-a_4\leq \xi\leq u_*-a_3,\\
(\rho_3,u_*,p_*),
& u_*-a_3<\xi<u_*,\\
(\rho_2,u_*,p_*),
& u_*<\xi<u_s,\\
(\rho_1,u_1,p_1),
& \xi>u_s.
\end{cases}
\end{aligned}
$$

The plotted solution is:

![[images/problem3_state_profiles.png|700]]

The code used to compute the state and generate the plots is in `Homework/Final Homework/problem3_shock_tube.py`.


##### problem 3.d

The characteristic speeds for one-dimensional unsteady compressible flow are

$$
\begin{aligned}
C_+:\qquad \frac{dx}{dt}&=u+a,\\
C_-:\qquad \frac{dx}{dt}&=u-a.
\end{aligned}
$$

In each constant state, these are straight lines. In the expansion fan, the $C_-$ characteristics are the fan rays

$$
\begin{aligned}
x&=\xi t,
\qquad
u_4-a_4\leq \xi\leq u_*-a_3.
\end{aligned}
$$

The contact and shock trajectories are

$$
\begin{aligned}
x_{\mathrm{contact}}(t)
&=
u_*t,\\
x_{\mathrm{shock}}(t)
&=
u_s t.
\end{aligned}
$$

The code-generated characteristic plot is:

![[images/problem3_characteristics.png|700]]

The blue curves are representative $C_+$ characteristics and the red curves are representative $C_-$ characteristics. The expansion fan is the bundle of left-running $C_-$ rays, the dashed black line is the contact trajectory $x=u_*t$, and the solid black line is the shock trajectory $x=u_s t$.
