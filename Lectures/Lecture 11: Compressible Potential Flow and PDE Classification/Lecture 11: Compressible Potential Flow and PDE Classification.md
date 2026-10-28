## 1 From Kelvin's theorem to a velocity potential

In Lecture 10, we established Kelvin's circulation theorem. Under the assumptions of

- inviscid flow,
- conservative body forces,
- isentropic motion,
the circulation around any material loop satisfies

$$
\frac{d \Gamma}{d t}=0
$$

In particular, if the initial circulation is zero, then it remains zero for all time. By Stokes' theorem, this implies that the vorticity vanishes:

$$
\nabla \times \boldsymbol{u}=0
$$

In a simply connected domain, a curl-free vector field must be expressible as the gradient of a scalar potential. This is not a new result - it is precisely the geometric statement we invoked in Lecture 10 when discussing conservative fields.

Therefore, under the above assumptions,

$$
\boldsymbol{u}=\nabla \phi_{n},
$$

where $\phi_{n}(\boldsymbol{x}, t)$ is a scalar velocity potential. (The subscript $n$ reminds us that we are still working with the full nonlinear equation.)

This is already a dramatic simplification. The three velocity components are now determined by a single scalar field. But we have not yet used continuity, nor have we closed the system thermodynamically. Our next goal is to derive a governing equation for $\phi_{n}$.

## 2 Unsteady Bernoulli and elimination of density

### 2.1 Momentum in enthalpy form

For inviscid flow with conservative body forces absorbed into a potential, the momentum equation can be written in primitive form as

$$
\boldsymbol{u}_{t}+(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}+\frac{1}{\rho} \nabla p=0
$$

From Lecture 10, we recall that for isentropic motion,

$$
\nabla h=\frac{1}{\rho} \nabla p
$$

where $h$ is the specific enthalpy.
Substituting $\boldsymbol{u}=\nabla \phi_{n}$ gives

$$
\nabla \phi_{n, t}+\left(\nabla \phi_{n} \cdot \nabla\right) \nabla \phi_{n}+\nabla h=0 .
$$

Using the standard vector identity

$$
(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}=\nabla\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)-\boldsymbol{u} \times(\nabla \times \boldsymbol{u})
$$

and recalling that $\boldsymbol{u}=\nabla \phi_{n}$ implies

$$
\nabla \times \boldsymbol{u}=\nabla \times\left(\nabla \phi_{n}\right)=\mathbf{0}
$$

we obtain

$$
\left(\nabla \phi_{n} \cdot \nabla\right) \nabla \phi_{n}=\nabla\left(\frac{1}{2}\left|\nabla \phi_{n}\right|^{2}\right)
$$

Conservation of momentum therefore becomes

$$
\nabla\left(\phi_{n, t}+\frac{1}{2}\left|\nabla \phi_{n}\right|^{2}+h\right)=0 .
$$

Since the gradient of this quantity vanishes, the quantity itself must be spatially uniform. That is,

$$
\phi_{n, t}+\frac{1}{2}\left|\nabla \phi_{n}\right|^{2}+h=C(t)
$$

### 2.2 Absorbing the time-dependent constant

The function $C(t)$ depends only on time. Such a term may be absorbed into the definition of the potential without changing the velocity field.

Define

$$
\tilde{\phi}_{n}(\boldsymbol{x}, t)=\phi_{n}(\boldsymbol{x}, t)-\int^{t} C(\tau) d \tau
$$

Then

$$
\nabla \tilde{\phi}_{n}=\nabla \phi_{n}, \quad \tilde{\phi}_{n, t}=\phi_{n, t}-C(t)
$$

Substituting into the Bernoulli relation eliminates the constant and gives

$$
\tilde{\phi}_{n, t}+\frac{1}{2}\left|\nabla \tilde{\phi}_{n}\right|^{2}+h(\rho)=0
$$

Since the velocity depends only on spatial gradients of the potential, we may (without loss of generality) relabel $\tilde{\phi}_{n}$ as $\phi_{n}$.

### 2.3 Eliminating $\rho$ : the nonlinear potential equation

Define the Bernoulli quantity

$$
B:=-\phi_{n, t}-\frac{1}{2}\left|\nabla \phi_{n}\right|^{2}
$$

Then Bernoulli gives

$$
h(\rho)=B
$$

For isentropic flow, $h$ is a function of $\rho$ alone and may be inverted. Thus we may regard

$$
\rho=\rho(B)
$$

Thermodynamic identity. For isentropic flow, $h$ is a function of $\rho$ alone. We now derive the relation between $h$ and $\rho$.

From the Gibbs relation under isentropic conditions ( $d s=0$ ),

$$
d h=\frac{1}{\rho} d p
$$

Dividing by $d \rho$ gives

$$
\frac{d h}{d \rho}=\frac{1}{\rho} \frac{d p}{d \rho}
$$

By definition of the sound speed,

$$
a^{2}=\left(\frac{\partial p}{\partial \rho}\right)_{s}
$$

Therefore,

$$
\frac{d h}{d \rho}=\frac{a^{2}}{\rho}
$$

Since $h=B$, we also have

$$
\rho^{\prime}(B)=\frac{\rho}{a^{2}}
$$

Here and in what follows, the prime denotes ordinary differentiation with respect to the scalar argument:

$$
\rho^{\prime}(B):=\frac{d \rho}{d B}
$$

This derivative is not a spatial or temporal derivative, but the thermodynamic derivative of density viewed as a function of the Bernoulli variable $B$.

Rewrite continuity. Continuity reads

$$
\rho_{t}+\nabla \cdot\left(\rho \nabla \phi_{n}\right)=0
$$

Using $\rho=\rho(B)$ and the chain rule:

$$
\rho_{t}=\rho^{\prime}(B) B_{t}, \quad \nabla \rho=\rho^{\prime}(B) \nabla B
$$

Also expand

$$
\nabla \cdot\left(\rho \nabla \phi_{n}\right)=\nabla \rho \cdot \nabla \phi_{n}+\rho \nabla^{2} \phi_{n}
$$

Hence,

$$
\rho^{\prime}(B) B_{t}+\rho^{\prime}(B) \nabla B \cdot \nabla \phi_{n}+\rho \nabla^{2} \phi_{n}=0
$$

Compute $B_{t}$ and $\nabla B$. From

$$
B=-\phi_{n, t}-\frac{1}{2}\left|\nabla \phi_{n}\right|^{2}
$$

we obtain

$$
B_{t}=-\phi_{n, t t}-\nabla \phi_{n} \cdot \nabla \phi_{n, t},
$$

and

$$
\nabla B=-\nabla \phi_{n, t}-\left(\nabla \nabla \phi_{n}\right) \nabla \phi_{n} .
$$

Here $\nabla \nabla \phi_{n}$ denotes the Hessian matrix of second derivatives,

$$
\nabla \nabla \phi_{n}=\left(\begin{array}{lll}
\phi_{n, x x} & \phi_{n, x y} & \phi_{n, x z} \\
\phi_{n, y x} & \phi_{n, y y} & \phi_{n, y z} \\
\phi_{n, z x} & \phi_{n, z y} & \phi_{n, z z}
\end{array}\right)
$$

Substitute and simplify. After substitution and algebra (grouping symmetric terms), we obtain

$$
-\frac{1}{a^{2}}\left(\phi_{n, t t}+2 \nabla \phi_{n} \cdot \nabla \phi_{n, t}+\left(\nabla \phi_{n}\right)^{T}\left(\nabla \nabla \phi_{n}\right) \nabla \phi_{n}\right)+\nabla^{2} \phi_{n}=0 .
$$

Thus the term

$$
\left(\nabla \phi_{n}\right)^{T}\left(\nabla \nabla \phi_{n}\right) \nabla \phi_{n}
$$

is a quadratic form involving the second derivatives of $\phi_{n}$.
Multiplying by $a^{2}$ gives the final nonlinear equation:

$$
\phi_{n, t t}+2 \nabla \phi_{n} \cdot \nabla \phi_{n, t}+\left(\nabla \phi_{n}\right)^{T}\left(\nabla \nabla \phi_{n}\right) \nabla \phi_{n}-a^{2} \nabla^{2} \phi_{n}=0
$$

Here $a=a(\rho)$ and $\rho=\rho(B)$ with

$$
B=-\phi_{n, t}-\frac{1}{2}\left|\nabla \phi_{n}\right|^{2} .
$$

This is the full nonlinear unsteady compressible potential equation.
The nonlinear equation derived above is exact under the assumptions of inviscid, isentropic, irrotational flow. Its structure is highly nonlinear: the coefficients depend on $\nabla \phi_{n}$ and on the sound speed $a(\rho)$, which itself depends on $\phi_{n}$ through the Bernoulli relation.

However, an important structural observation is that the equation is quasilinear. That is, it is linear in its highest-order (second) derivatives, even though the coefficients multiplying those derivatives depend on lower-order quantities (specifically, the first derivatives of $\phi_{n}$ ).

This distinction matters.
For second-order PDEs, the qualitative behavior of solutions (elliptic, hyperbolic, or parabolic) is determined entirely by the principal part: the collection of highest-order derivatives. Lower-order terms influence amplitudes and forcing, but they do not determine the fundamental character of information propagation.

Because the equation is quasilinear, we may examine its local behavior near any spacetime point by freezing the coefficients of the highest-order derivatives at that point. In other words, we treat the
local velocity components and sound speed as constants in a sufficiently small neighborhood. This locally frozen equation is linear with constant coefficients. Its structure reveals the type of the PDE at that point. In the next section, we will adopt this frozen coefficient approach to reveal the type of PDE that arises under different situations, and use that to inform what boundary conditions we need what solutions we can expect from the PDE.

## 3 Local linear structure of the unsteady nonlinear equation

We will make progress understanding the qualitative behavior of solutions by exploring how the equations behave locally, i.e., near a fixed spacetime point ( $\boldsymbol{x}_{*}, t_{*}$ ).

At that point, we freeze the coefficients.
That is, we evaluate the local velocity components

$$
u_{*}=\phi_{n x}\left(\boldsymbol{x}_{*}, t_{*}\right), \quad v_{*}=\phi_{n y}\left(\boldsymbol{x}_{*}, t_{*}\right), \quad w_{*}=\phi_{n z}\left(\boldsymbol{x}_{*}, t_{*}\right),
$$

and the local sound speed $a_{*}=a\left(\boldsymbol{x}_{*}, t_{*}\right)$, and treat them as constants in a sufficiently small neighborhood. From this perspective, the equations are locally linear about this flow-thermodynamic state.

### 3.1 Extracting the principal (highest-order) part

We now return to the nonlinear potential equation derived in Section 2.3. To analyze the qualitative behavior of solutions, we isolate the principal part of the equation: the collection of terms containing second derivatives of $\phi_{n}$. All other terms involve at most first derivatives of $\phi_{n}$ and are therefore referred to as lower-order terms.

This distinction is not arbitrary. For second-order PDEs, the classification into elliptic, hyperbolic, or parabolic depends only on the coefficients multiplying the second derivatives. Lower-order terms influence amplitudes and forcing, but they do not determine how information propagates.

Extracting the second-derivative terms from the nonlinear equation, we obtain

$$
\begin{aligned}
\phi_{n t t}+2 u \phi_{n x t}+2 v \phi_{n y t}+ & 2 w \phi_{n z t}+\left(u^{2}-a^{2}\right) \phi_{n x x}+\left(v^{2}-a^{2}\right) \phi_{n y y}+\left(w^{2}-a^{2}\right) \phi_{n z z} \\
& +2 u v \phi_{n x y}+2 u w \phi_{n x z}+2 v w \phi_{n y z}
\end{aligned}
$$

where $u, v, w$ and $a$ are evaluated from the full nonlinear solution.
We replace the variable coefficients by the locally frozen constants and drop terms involving derivatives of strictly lower differential order than the highest derivatives present in the equation. This process yields a linear equation with constant coefficients, representing the linearized principal part of the PDE we care about:

$$
\begin{gathered}
\phi_{n t t}+2 u_{*} \phi_{n x t}+2 v_{*} \phi_{n y t}+2 w_{*} \phi_{n z t}+\left(u_{*}^{2}-a_{*}^{2}\right) \phi_{n x x}+\left(v_{*}^{2}-a_{*}^{2}\right) \phi_{n y y}+\left(w_{*}^{2}-a_{*}^{2}\right) \phi_{n z z} \\
+2 u_{*} v_{*} \phi_{n x y}+2 u_{*} w_{*} \phi_{n x z}+2 v_{*} w_{*} \phi_{n y z}=0 .
\end{gathered}
$$

This locally frozen linear equation governs the leading-order behavior of the nonlinear equation near ( $\boldsymbol{x}_{*}, t_{*}$ ). Its structure determines the PDE type at that point.

## 4 Why classify second-order PDEs?

The linearized potential equation we derived involves three spatial variables and time. However, many physically important problems depend primarily on only two independent variables.

For example:

- Unsteady one-dimensional wave propagation depends on $(x, t)$.
- Steady two-dimensional flow over an airfoil depends on $(x, y)$.
- Planar disturbances in uniform flow often depend on $(x, t)$.
- Steady planar potential flow depends on $(x, y)$.

In each of these cases, the governing equation reduces to a scalar second-order PDE in two independent variables.

It is therefore essential to understand the qualitative behavior of general second-order scalar PDEs in two variables. When reading these generic PDEs we study below, think of them as extracting the linearized equations above, extracting terms that are only associated with two independent variables (e.g., $(x, t),(x, y)$, etc). To avoid specifying one particular combination of independent variables, we instead will look at a linear PDE in terms of two generic independent variables, $(\xi, \zeta)$.

We now develop that theory in a clean, canonical setting.

## 5 Studying a canonical principal part PDE

Consider a general linear second-order PDE in two independent variables, with principle part clearly identified, as $(\xi, \zeta)$ :

$$
A \phi_{\xi \xi}+2 B \phi_{\xi \zeta}+C \phi_{\zeta \zeta}+(\text { lower-order terms })=0 .
$$

Lower-order terms involve first derivatives and zeroth-order (algebraic) terms.

### 5.1 Matrix form

The principal part may be written compactly as

$$
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right) \mathbf{K}\binom{\partial_{\xi}}{\partial_{\zeta}} \phi
$$

where

$$
\mathbf{K}=\left(\begin{array}{ll}
A & B \\
B & C
\end{array}\right)
$$

Thus the structure of the PDE is encoded in the symmetric matrix $\mathbf{K}$.

## 6 Diagonalization and canonical coordinates

Because $\mathbf{K}$ is symmetric, it admits an orthogonal eigen-decomposition:

$$
\mathbf{K}=\mathbf{V} \boldsymbol{\Lambda} \mathbf{V}^{T}
$$

where

$$
\Lambda=\left(\begin{array}{cc}
\lambda_{1} & 0 \\
0 & \lambda_{2}
\end{array}\right)
$$

Define new coordinates

$$
\binom{\xi^{\prime}}{\zeta^{\prime}}=\mathbf{V}^{T}\binom{\xi}{\zeta}
$$

Using the chain rule,

$$
\binom{\partial_{\xi}}{\partial_{\zeta}}=\mathbf{V}\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}}
$$

Substituting,

$$
\left(\begin{array}{ll}
\partial_{\xi} & \partial_{\zeta}
\end{array}\right) \mathbf{K}\binom{\partial_{\xi}}{\partial_{\zeta}}=\left(\begin{array}{ll}
\partial_{\xi^{\prime}} & \partial_{\zeta^{\prime}}
\end{array}\right) \Lambda\binom{\partial_{\xi^{\prime}}}{\partial_{\zeta^{\prime}}} .
$$

Thus the principal part becomes

$$
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}}
$$

Let us take a moment to appreciate this beautiful fact of linear algebra. We have diagonalized the principal part of the PDE; that is, we have identified suitable coordinates encoded in $\boldsymbol{V}$ such that the second-order (part of the) PDE reduces locally to a canonical diagonal form.

The behavior of the solution, boundary conditions needed, and general form of the principal part therefore depends on the signs of $\lambda_{1}$ and $\lambda_{2}$.

## 7 Three fundamental types

## Hyperbolic case: $\lambda_{1}$ and $\lambda_{2}$ have opposite signs

After diagonalization, suppose the principal part takes the form

$$
\phi_{\xi^{\prime} \xi^{\prime}}-\phi_{\zeta^{\prime} \zeta^{\prime}}=0
$$

This is the canonical hyperbolic equation in two variables.

Step 1: Factorization. The operator factors as

$$
\left(\partial_{\xi^{\prime}}+\partial_{\zeta^{\prime}}\right)\left(\partial_{\xi^{\prime}}-\partial_{\zeta^{\prime}}\right) \phi=0
$$

A product of two first-order differential operators vanishes. One natural way this can occur is if each factor annihilates $\phi$ separately. This observation reveals special directions in the $\left(\xi^{\prime}, \zeta^{\prime}\right)$ plane.

Step 2: Characteristic coordinates. Define new variables

$$
\eta=\xi^{\prime}+\zeta^{\prime}, \quad \mu=\xi^{\prime}-\zeta^{\prime}
$$

By the chain rule,

$$
\partial_{\xi^{\prime}}+\partial_{\zeta^{\prime}}=2 \partial_{\eta}, \quad \partial_{\xi^{\prime}}-\partial_{\zeta^{\prime}}=2 \partial_{\mu}
$$

The PDE becomes

$$
\phi_{\eta \mu}=0
$$

Step 3: Reduction to ordinary differential equations. The equation $\phi_{\eta \mu}=0$ implies that

$$
\partial_{\eta}\left(\partial_{\mu} \phi\right)=0
$$

Therefore $\partial_{\mu} \phi$ is independent of $\eta$. There exists a function $g(\mu)$ such that

$$
\partial_{\mu} \phi=g(\mu)
$$

Integrating with respect to $\mu$,

$$
\phi(\eta, \mu)=f(\eta)+G(\mu)
$$

where $f$ and $G$ are arbitrary functions.

Interpretation. The solution depends only on the combinations

$$
\eta=\xi^{\prime}+\zeta^{\prime}, \quad \mu=\xi^{\prime}-\zeta^{\prime}
$$

The curves

$$
\xi^{\prime}+\zeta^{\prime}=\text { constant }, \quad \xi^{\prime}-\zeta^{\prime}=\text { constant }
$$

are straight lines in the $\left(\xi^{\prime}, \zeta^{\prime}\right)$ plane. These are the characteristic curves. Note that in the full nonlinear equation, the coefficients depend on space (and on the solution itself), so the eigenvectors associated with the frozen coefficients vary from point to point. As a result, the characteristic directions vary spatially, and the characteristics are generally curved.

Along each characteristic curve, the PDE reduces to an ODE. The solution is constant (up to a prescribed functional form) along these directions.

This structure implies:

- Disturbances propagate along characteristic curves.
- The propagation is directional.
- The slope of the characteristics determines the propagation speed when $\zeta^{\prime}$ represents time.

If $\zeta^{\prime}$ is interpreted as a time-like variable and $\xi^{\prime}$ as space-like, then the characteristic slopes determine finite propagation speed. Only data lying within the characteristic cone influence a given point.

Determining the arbitrary functions. From the factorization, we obtained the general solution

$$
\phi(\eta, \mu)=f(\eta)+g(\mu)
$$

where $f$ and $g$ are arbitrary functions.
To determine these functions uniquely, appropriate data must be prescribed.
For a hyperbolic equation, local well-posedness is achieved by prescribing Cauchy data on a curve that is not characteristic. For example, along the curve $\zeta^{\prime}=0$ (which is transverse to the characteristic directions), one may prescribe

$$
\phi\left(\xi^{\prime}, 0\right)=F\left(\xi^{\prime}\right), \quad \partial_{\zeta^{\prime}} \phi\left(\xi^{\prime}, 0\right)=H\left(\xi^{\prime}\right) .
$$

Here $F$ and $H$ are given data functions. These determine the two arbitrary functions $f$ and $g$ appearing in the solution.

Substituting $\zeta^{\prime}=0$ gives

$$
\phi\left(\xi^{\prime}, 0\right)=f\left(\xi^{\prime}\right)+g\left(\xi^{\prime}\right)
$$

while differentiating and evaluating at $\zeta^{\prime}=0$ gives a second relation involving $f^{\prime}\left(\xi^{\prime}\right)$ and $g^{\prime}\left(\xi^{\prime}\right)$. Together, these determine $f$ and $g$ uniquely (locally).

Initial versus boundary data. It is important to distinguish between initial-value and boundaryvalue formulations.

For hyperbolic equations, the natural formulation is an initial-value problem: data are prescribed on a curve transverse to the characteristics, and the solution propagates away from that curve along characteristic lines.

In a bounded domain, boundary conditions may only be imposed where characteristics enter the domain. If a characteristic leaves the domain at a boundary point, the interior solution determines the boundary value there. Imposing additional data at such a location would overdetermine the problem.

This directional propagation of information is a defining feature of hyperbolic equations.
Elliptic: $\lambda_{1}$ and $\lambda_{2}$ have the same sign
After diagonalization and scaling, the canonical form is

$$
\phi_{\xi^{\prime} \xi^{\prime}}+\phi_{\zeta^{\prime} \zeta^{\prime}}=0
$$

i.e. Laplace's equation in the transformed variables.

Interpretation. Elliptic equations have no real characteristic directions: the principal operator cannot be factored into first-order operators with real coefficients. As a result, information does not propagate along rays or curves in the domain. Instead, the solution at a point is coupled to the data everywhere on the boundary, and elliptic problems are typically posed as boundary-value problems rather than initial-value problems.

Example boundary conditions. Let $\Omega \subset \mathbb{R}^{2}$ be a bounded domain in $\left(\xi^{\prime}, \zeta^{\prime}\right)$. A common wellposed elliptic problem specifies data on the entire boundary:

$$
\phi=g \quad \text { on } \partial \Omega \quad \text { (Dirichlet) },
$$

or, alternatively,

$$
\partial_{n} \phi=g \quad \text { on } \partial \Omega \quad \text { (Neumann) },
$$

where $\partial_{n} \phi:=\boldsymbol{n} \cdot \nabla \phi$ and $\boldsymbol{n}$ is the outward unit normal. (Other mixes, such as Robin conditions, are also common.)

## Parabolic: one eigenvalue is zero

In the parabolic case, the principal matrix has one nonzero eigenvalue and one zero eigenvalue. After diagonalizing, the principal part reduces to a single second derivative:

$$
\lambda_{1} \phi_{\xi^{\prime} \xi^{\prime}}+\lambda_{2} \phi_{\zeta^{\prime} \zeta^{\prime}} \quad \leadsto \quad \phi_{\xi^{\prime} \xi^{\prime}}=0
$$

after scaling and relabeling so that $\lambda_{1} \neq 0$ and $\lambda_{2}=0$.

What this does (and does not) mean. The statement $\phi_{\xi^{\prime} \xi^{\prime}}=0$ describes a degeneracy of the principal part: there is curvature (second-derivative control) only in one direction ( $\xi^{\prime}$ ), while the other direction $\left(\zeta^{\prime}\right)$ does not appear at the same derivative order. This is why parabolic equations are often described as being "halfway" between elliptic and hyperbolic: they retain a smoothing second-derivative operator in one direction, but do not have the two-direction structure of elliptic problems or the two-family characteristic structure of hyperbolic problems.

Why the heat equation is parabolic. A familiar parabolic model is the heat equation

$$
\phi_{\zeta^{\prime}}=\kappa \phi_{\xi^{\prime} \xi^{\prime}} .
$$

Here the principal part (highest derivatives) is still $\phi_{\xi^{\prime}} \xi^{\prime}$. The first derivative $\phi_{\zeta^{\prime}}$ is lower order and therefore does not enter the principal matrix used for classification. Nevertheless, that lower-order term is crucial dynamically: it provides an evolution direction (often interpreted as time) along which diffusion acts.

Interpretation. Parabolic equations describe diffusion-like smoothing: variations in $\phi$ in the $\xi^{\prime}$ direction tend to be smoothed as one moves in the $\zeta^{\prime}$ direction. Information does not propagate along finite-speed characteristic lines as in the hyperbolic case; instead, disturbances spread (and smooth) as the solution evolves.

Example data to determine a solution. For a parabolic evolution problem such as $\phi_{\zeta^{\prime}}=\kappa \phi_{\xi^{\prime} \xi^{\prime}}$, one typically prescribes:

- Initial data at $\zeta^{\prime}=0$ :

$$
\phi\left(\xi^{\prime}, 0\right)=F\left(\xi^{\prime}\right)
$$

- Boundary data in $\xi^{\prime}$ (if $\xi^{\prime}$ lies in an interval, say $0<\xi^{\prime}<L$ ), for example Dirichlet conditions

$$
\phi\left(0, \zeta^{\prime}\right)=g_{0}\left(\zeta^{\prime}\right), \quad \phi\left(L, \zeta^{\prime}\right)=g_{L}\left(\zeta^{\prime}\right)
$$

These are the parabolic analogs of "initial-in-one-direction plus boundary-in-the-other": you evolve forward in $\zeta^{\prime}$ while enforcing boundary constraints in $\xi^{\prime}$.

## 8 Looking ahead

We have now developed a classification framework for scalar second-order PDEs in two variables.
In Lecture 12, we will return to the linearized compressible potential equation and determine:

- which regime corresponds to elliptic behavior,
- which corresponds to hyperbolic behavior,
- how the Mach number governs the transition,
- what this implies physically for compressible flow.

