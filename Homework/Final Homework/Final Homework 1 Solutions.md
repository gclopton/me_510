

Grady Clopton
Final Homework

# Problem 1: Lagrangian and Eulerian perspectives



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



# Problem 2: Hyperbolic structure of compressible flow




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





# Problem 3: Shock tube problem



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




![[Untitled Page.png]]




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

The sound-speed relation follows from $a^2=\gamma p/\rho$:

$$
\begin{aligned}
\frac{a_3^2}{a_4^2}
&=
\frac{\gamma p_3/\rho_3}{\gamma p_4/\rho_4}\\
&=
\frac{p_3}{p_4}\frac{\rho_4}{\rho_3}\\
&=
\frac{p_*}{p_4}
\left[
\left(\frac{p_*}{p_4}\right)^{1/\gamma}
\right]^{-1}\\
&=
\left(\frac{p_*}{p_4}\right)^{1-1/\gamma}\\
&=
\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/\gamma},
\end{aligned}
$$

so

$$
\begin{aligned}
a_3
&=
a_4\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}.
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

The shock-speed expression comes from mass conservation across the moving shock:

$$
\begin{aligned}
\rho_1(u_s-u_1)
&=
\rho_2(u_s-u_2)\\
\rho_1u_s
&=
\rho_2(u_s-u_*)\\
\rho_1u_s
&=
\rho_2u_s-\rho_2u_*\\
\rho_2u_*
&=
\rho_2u_s-\rho_1u_s\\
\rho_2u_*
&=
(\rho_2-\rho_1)u_s\\
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

Inside the expansion fan, $\xi=u-a$ and the invariant $I_+$ is constant:

$$
\begin{aligned}
\xi
&=
u-a,\\
u+\frac{2a}{\gamma-1}
&=
u_4+\frac{2a_4}{\gamma-1}.
\end{aligned}
$$

Since $u_4=0$, substitute $u=\xi+a$:

$$
\begin{aligned}
u+\frac{2a}{\gamma-1}
&=
\frac{2a_4}{\gamma-1}\\
\xi+a+\frac{2a}{\gamma-1}
&=
\frac{2a_4}{\gamma-1}\\
\xi+a\left(1+\frac{2}{\gamma-1}\right)
&=
\frac{2a_4}{\gamma-1}\\
\xi+a\left(\frac{\gamma-1}{\gamma-1}+\frac{2}{\gamma-1}\right)
&=
\frac{2a_4}{\gamma-1}\\
\xi+a\left(\frac{\gamma+1}{\gamma-1}\right)
&=
\frac{2a_4}{\gamma-1}\\
a\left(\frac{\gamma+1}{\gamma-1}\right)
&=
\frac{2a_4}{\gamma-1}-\xi\\
a(\gamma+1)
&=
2a_4-(\gamma-1)\xi\\
a(\xi)
&=
\frac{2a_4-(\gamma-1)\xi}{\gamma+1}\\
&=
\frac{\gamma-1}{\gamma+1}
\left(
u_4+\frac{2a_4}{\gamma-1}-\xi
\right).
\end{aligned}
$$

Then

$$
\begin{aligned}
u(\xi)
&=
\xi+a(\xi)\\
&=
\xi+\frac{2a_4-(\gamma-1)\xi}{\gamma+1}\\
&=
\frac{(\gamma+1)\xi}{\gamma+1}
+\frac{2a_4-(\gamma-1)\xi}{\gamma+1}\\
&=
\frac{(\gamma+1)\xi+2a_4-(\gamma-1)\xi}{\gamma+1}\\
&=
\frac{[(\gamma+1)-(\gamma-1)]\xi+2a_4}{\gamma+1}\\
&=
\frac{2\xi+2a_4}{\gamma+1}\\
&=
\frac{2(a_4+\xi)}{\gamma+1}.
\end{aligned}
$$

The density and pressure in the isentropic fan are

$$
\begin{aligned}
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





```python
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


gamma = 1.4
rho4 = 1.0
p4 = 100000.0
u4 = 0.0
rho1 = 0.125
p1 = 10000.0
u1 = 0.0
t_final = 0.01


def expansion_velocity(p_star):
    a4 = math.sqrt(gamma * p4 / rho4)
    exponent = (gamma - 1.0) / (2.0 * gamma)
    return u4 + 2.0 * a4 / (gamma - 1.0) * (1.0 - (p_star / p4) ** exponent)


def shock_velocity_relation(p_star):
    return u1 + (p_star - p1) * math.sqrt(
        (2.0 / ((gamma + 1.0) * rho1))
        / (p_star + ((gamma - 1.0) / (gamma + 1.0)) * p1)
    )


def pressure_residual(p_star):
    return expansion_velocity(p_star) - shock_velocity_relation(p_star)


def bisect_root(lo, hi, tol=1e-10, max_iter=200):
    f_lo = pressure_residual(lo)
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = pressure_residual(mid)
        if abs(f_mid) < tol or abs(hi - lo) < tol:
            return mid
        if f_lo * f_mid <= 0.0:
            hi = mid
        else:
            lo = mid
            f_lo = f_mid
    return 0.5 * (lo + hi)


a4 = math.sqrt(gamma * p4 / rho4)
a1 = math.sqrt(gamma * p1 / rho1)
p_star = bisect_root(p1, p4)
u_star = expansion_velocity(p_star)
rho3 = rho4 * (p_star / p4) ** (1.0 / gamma)
a3 = a4 * (p_star / p4) ** ((gamma - 1.0) / (2.0 * gamma))
pressure_ratio = p_star / p1
rho2 = rho1 * (
    (pressure_ratio + ((gamma - 1.0) / (gamma + 1.0)))
    / (1.0 + ((gamma - 1.0) / (gamma + 1.0)) * pressure_ratio)
)
a2 = math.sqrt(gamma * p_star / rho2)
u_s = rho2 * u_star / (rho2 - rho1)

xi_head = u4 - a4
xi_tail = u_star - a3
x_head = xi_head * t_final
x_tail = xi_tail * t_final
x_contact = u_star * t_final
x_shock = u_s * t_final


def fan_state(xi):
    a = (gamma - 1.0) / (gamma + 1.0) * (u4 + 2.0 * a4 / (gamma - 1.0) - xi)
    u = xi + a
    rho = rho4 * (a / a4) ** (2.0 / (gamma - 1.0))
    p = p4 * (a / a4) ** (2.0 * gamma / (gamma - 1.0))
    return rho, u, p


def solution_at(x, t):
    xi = x / t
    rho = np.empty_like(x)
    u = np.empty_like(x)
    p = np.empty_like(x)

    mask4 = xi < xi_head
    mask_fan = (xi >= xi_head) & (xi <= xi_tail)
    mask3 = (xi > xi_tail) & (xi < u_star)
    mask2 = (xi >= u_star) & (xi < u_s)
    mask1 = xi >= u_s

    rho[mask4] = rho4
    u[mask4] = u4
    p[mask4] = p4
    rho[mask_fan], u[mask_fan], p[mask_fan] = fan_state(xi[mask_fan])
    rho[mask3] = rho3
    u[mask3] = u_star
    p[mask3] = p_star
    rho[mask2] = rho2
    u[mask2] = u_star
    p[mask2] = p_star
    rho[mask1] = rho1
    u[mask1] = u1
    p[mask1] = p1
    return rho, u, p


x = np.linspace(-4.5, 6.2, 2600)
rho, u, p = solution_at(x, t_final)

fig, axes = plt.subplots(3, 1, figsize=(8.2, 8.4), sharex=True)
axes[0].plot(x, rho, color="#1f77b4", linewidth=2)
axes[0].set_ylabel(r"$\rho\;[\mathrm{kg/m^3}]$")
axes[1].plot(x, u, color="#d62728", linewidth=2)
axes[1].set_ylabel(r"$u\;[\mathrm{m/s}]$")
axes[2].plot(x, p, color="#2ca02c", linewidth=2)
axes[2].set_ylabel(r"$p\;[\mathrm{Pa}]$")
axes[2].set_xlabel(r"$x\;[\mathrm{m}]$")

for ax in axes:
    ax.grid(True, alpha=0.25)
    for loc, style, color in [
        (x_head, ":", "#777777"),
        (x_tail, ":", "#777777"),
        (x_contact, "--", "#111111"),
        (x_shock, "-", "#111111"),
    ]:
        ax.axvline(loc, linestyle=style, color=color, linewidth=1.1, alpha=0.8)

axes[0].set_title(r"Shock-tube solution at $t=0.01\,\mathrm{s}$")
axes[0].text(x_head, axes[0].get_ylim()[1] * 0.92, "fan head", rotation=90, va="top", ha="right", fontsize=8)
axes[0].text(x_tail, axes[0].get_ylim()[1] * 0.92, "fan tail", rotation=90, va="top", ha="left", fontsize=8)
axes[0].text(x_contact, axes[0].get_ylim()[1] * 0.92, "contact", rotation=90, va="top", ha="left", fontsize=8)
axes[0].text(x_shock, axes[0].get_ylim()[1] * 0.92, "shock", rotation=90, va="top", ha="left", fontsize=8)

output_dir = Path("/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/images")
output_dir.mkdir(exist_ok=True)
fig.tight_layout()
fig.savefig(output_dir / "problem3_state_profiles.png", dpi=200)
plt.show()
```


##### problem 3.d

The characteristic speeds for one-dimensional unsteady compressible flow are

$$
\begin{aligned}
C_+:\qquad \frac{dx}{dt}&=u+a,\\
C_-:\qquad \frac{dx}{dt}&=u-a.
\end{aligned}
$$

For the constant regions, this gives

$$
\begin{aligned}
\text{Region 4:}\qquad
C_+:\frac{dx}{dt}
&=
u_4+a_4
=374.1657\ \mathrm{m/s},\\
C_-:\frac{dx}{dt}
&=
u_4-a_4
=-374.1657\ \mathrm{m/s},\\
\text{Region 3:}\qquad
C_+:\frac{dx}{dt}
&=
u_*+a_3
=608.7948\ \mathrm{m/s},\\
C_-:\frac{dx}{dt}
&=
u_*-a_3
=-22.2222\ \mathrm{m/s},\\
\text{Region 2:}\qquad
C_+:\frac{dx}{dt}
&=
u_*+a_2
=693.0341\ \mathrm{m/s},\\
C_-:\frac{dx}{dt}
&=
u_*-a_2
=-106.4615\ \mathrm{m/s},\\
\text{Region 1:}\qquad
C_+:\frac{dx}{dt}
&=
u_1+a_1
=334.6640\ \mathrm{m/s},\\
C_-:\frac{dx}{dt}
&=
u_1-a_1
=-334.6640\ \mathrm{m/s}.
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



![[images/problem3_characteristics.png|700]]

The blue curves are representative $C_+$ characteristics and the red curves are representative $C_-$ characteristics. The expansion fan is the bundle of left-running $C_-$ rays, the dashed black line is the contact trajectory $x=u_*t$, and the solid black line is the shock trajectory $x=u_s t$.



```python
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


gamma = 1.4
rho4 = 1.0
p4 = 100000.0
u4 = 0.0
rho1 = 0.125
p1 = 10000.0
u1 = 0.0
t_final = 0.01
x_min = -4.5
x_max = 6.2


def expansion_velocity(p_star):
    a4 = math.sqrt(gamma * p4 / rho4)
    exponent = (gamma - 1.0) / (2.0 * gamma)
    return u4 + 2.0 * a4 / (gamma - 1.0) * (1.0 - (p_star / p4) ** exponent)


def shock_velocity_relation(p_star):
    return u1 + (p_star - p1) * math.sqrt(
        (2.0 / ((gamma + 1.0) * rho1))
        / (p_star + ((gamma - 1.0) / (gamma + 1.0)) * p1)
    )


def pressure_residual(p_star):
    return expansion_velocity(p_star) - shock_velocity_relation(p_star)


def bisect_root(lo, hi, tol=1e-10, max_iter=200):
    f_lo = pressure_residual(lo)
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        f_mid = pressure_residual(mid)
        if abs(f_mid) < tol or abs(hi - lo) < tol:
            return mid
        if f_lo * f_mid <= 0.0:
            hi = mid
        else:
            lo = mid
            f_lo = f_mid
    return 0.5 * (lo + hi)


a4 = math.sqrt(gamma * p4 / rho4)
a1 = math.sqrt(gamma * p1 / rho1)
p_star = bisect_root(p1, p4)
u_star = expansion_velocity(p_star)
rho3 = rho4 * (p_star / p4) ** (1.0 / gamma)
a3 = a4 * (p_star / p4) ** ((gamma - 1.0) / (2.0 * gamma))
pressure_ratio = p_star / p1
rho2 = rho1 * (
    (pressure_ratio + ((gamma - 1.0) / (gamma + 1.0)))
    / (1.0 + ((gamma - 1.0) / (gamma + 1.0)) * pressure_ratio)
)
a2 = math.sqrt(gamma * p_star / rho2)
u_s = rho2 * u_star / (rho2 - rho1)

xi_head = u4 - a4
xi_tail = u_star - a3
x_head = xi_head * t_final
x_tail = xi_tail * t_final
x_contact = u_star * t_final
x_shock = u_s * t_final


def cplus_in_fan(tau, tau0):
    # In the fan, xi=x/t, xi=u-a, and dx/dt=u+a.
    # Solving t dxi/dt + xi = u+a gives
    # 2a4-(gamma-1)xi = C*t^{-2(gamma-1)/(gamma+1)}.
    power = 2.0 * (gamma - 1.0) / (gamma + 1.0)
    c = (2.0 * a4 - (gamma - 1.0) * xi_head) * tau0**power
    xi = (2.0 * a4 - c * tau ** (-power)) / (gamma - 1.0)
    return xi * tau


def plot_masked_line(axis, x_line, t_line, mask, **kwargs):
    indices = np.where(mask)[0]
    if len(indices) == 0:
        return
    splits = np.where(np.diff(indices) > 1)[0] + 1
    for group in np.split(indices, splits):
        if len(group) > 1:
            axis.plot(x_line[group], t_line[group], **kwargs)


fig, ax = plt.subplots(figsize=(8.0, 6.2))
t_vals = np.linspace(0.0, t_final, 300)

ax.plot(xi_head * t_vals, t_vals, color="black", linestyle=":", linewidth=1.5, label="fan head/tail")
ax.plot(xi_tail * t_vals, t_vals, color="black", linestyle=":", linewidth=1.5)
ax.plot(u_star * t_vals, t_vals, color="black", linestyle="--", linewidth=1.8, label="contact")
ax.plot(u_s * t_vals, t_vals, color="black", linestyle="-", linewidth=2.0, label="shock")

for xi in np.linspace(xi_head, xi_tail, 13):
    ax.plot(xi * t_vals, t_vals, color="#d62728", linewidth=1.0, alpha=0.75)

for x0 in np.linspace(x_min + 0.2, -0.4, 9):
    x_plus = x0 + (u4 + a4) * t_vals
    x_minus = x0 + (u4 - a4) * t_vals
    plot_masked_line(ax, x_plus, t_vals, x_plus <= xi_head * t_vals, color="#1f77b4", linewidth=0.9, alpha=0.45)
    plot_masked_line(ax, x_minus, t_vals, x_minus <= xi_head * t_vals, color="#d62728", linewidth=0.9, alpha=0.35)

for tau0 in np.linspace(0.0018, 0.009, 5):
    t_curve = np.linspace(tau0, t_final, 160)
    x_curve = cplus_in_fan(t_curve, tau0)
    valid = (x_curve >= xi_head * t_curve) & (x_curve <= xi_tail * t_curve)
    ax.plot(x_curve[valid], t_curve[valid], color="#1f77b4", linewidth=1.2, alpha=0.85)
    if np.any(valid):
        t_exit = t_curve[valid][-1]
        x_exit = x_curve[valid][-1]
        t_after = np.linspace(t_exit, t_final, 80)
        x_after = x_exit + (u_star + a3) * (t_after - t_exit)
        mask_after = (x_after >= xi_tail * t_after) & (x_after <= u_star * t_after)
        plot_masked_line(ax, x_after, t_after, mask_after, color="#1f77b4", linewidth=1.0, alpha=0.55)

for x0 in np.linspace(x_tail - 1.2, x_contact - 0.2, 4):
    x_plus = x0 + (u_star + a3) * t_vals
    x_minus = x0 + (u_star - a3) * t_vals
    mask_plus = (x_plus >= xi_tail * t_vals) & (x_plus <= u_star * t_vals)
    mask_minus = (x_minus >= xi_tail * t_vals) & (x_minus <= u_star * t_vals)
    plot_masked_line(ax, x_plus, t_vals, mask_plus, color="#1f77b4", linewidth=0.9, alpha=0.4)
    plot_masked_line(ax, x_minus, t_vals, mask_minus, color="#d62728", linewidth=0.9, alpha=0.35)

for x0 in np.linspace(x_contact + 0.15, x_shock - 0.2, 4):
    x_plus = x0 + (u_star + a2) * t_vals
    x_minus = x0 + (u_star - a2) * t_vals
    mask_plus = (x_plus >= u_star * t_vals) & (x_plus <= u_s * t_vals)
    mask_minus = (x_minus >= u_star * t_vals) & (x_minus <= u_s * t_vals)
    plot_masked_line(ax, x_plus, t_vals, mask_plus, color="#1f77b4", linewidth=0.9, alpha=0.4)
    plot_masked_line(ax, x_minus, t_vals, mask_minus, color="#d62728", linewidth=0.9, alpha=0.35)

for x0 in np.linspace(x_shock + 0.15, x_max - 0.2, 4):
    x_plus = x0 + (u1 + a1) * t_vals
    x_minus = x0 + (u1 - a1) * t_vals
    plot_masked_line(ax, x_plus, t_vals, x_plus >= u_s * t_vals, color="#1f77b4", linewidth=0.9, alpha=0.35)
    plot_masked_line(ax, x_minus, t_vals, x_minus >= u_s * t_vals, color="#d62728", linewidth=0.9, alpha=0.35)

ax.text(-4.0, 0.0085, "Region 4", fontsize=9)
ax.text((x_tail + x_contact) / 2, 0.0085, "Region 3", fontsize=9, ha="center")
ax.text((x_contact + x_shock) / 2, 0.0085, "Region 2", fontsize=9, ha="center")
ax.text(5.85, 0.0085, "Region 1", fontsize=9, ha="center")
ax.text((x_head + x_tail) / 2, 0.0045, "expansion fan", fontsize=9, rotation=20, ha="center")
ax.set_xlim(x_min, x_max)
ax.set_ylim(0.0, t_final)
ax.set_xlabel(r"$x\;[\mathrm{m}]$")
ax.set_ylabel(r"$t\;[\mathrm{s}]$")
ax.set_title(r"Shock-tube characteristic structure")
ax.grid(True, alpha=0.25)
ax.plot([], [], color="#1f77b4", label=r"$C_+$")
ax.plot([], [], color="#d62728", label=r"$C_-$")
ax.legend(loc="upper left", fontsize=8)

output_dir = Path("/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/images")
output_dir.mkdir(exist_ok=True)
fig.tight_layout()
fig.savefig(output_dir / "problem3_characteristics.png", dpi=200)
plt.show()
```
