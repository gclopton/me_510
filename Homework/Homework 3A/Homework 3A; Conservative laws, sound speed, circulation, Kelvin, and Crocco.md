


Total: 100 points

Instructions. Show your reasoning clearly and keep your notation consistent. Unless stated otherwise, assume fields are smooth enough for the manipulations you perform (chain rule, product rule, differentiation under the integral sign, Stokes' theorem, etc.). When a field is declared non-smooth (e.g. a discontinuity), do not use pointwise derivatives at the jump. You may use results stated in the lecture notes except in places where you are explicitly asked to derive those results.

## Problem 1: Interpreting conservative vs. non-conservative forms points)

Preamble. A central message of Lecture 8 is that conservative PDEs are designed to be interpreted as local encodings of integral balance laws, and that this interpretation remains meaningful even when a solution develops discontinuities (e.g. shocks). In contrast, non-conservative (primitive) forms reorganize the same physics into a particle-based form that relies on smoothness.

In this problem, you will practice that interpretation directly on a simple 1D setting and then connect it back to compressible flow.



> [!question] 1a
> **Interpreting a conservative PDE at a discontinuity**
> 
> Consider the scalar 1-D conservation law
> 
> $$
> \partial_{t} U+\partial_{x} F(U)=0, \quad x \in[a, b]
> $$
> 
> where $F(U)$ computes a flux operation involving a piecewise-smooth solution $U(x, t)$, which has a single moving jump discontinuity located at $x=c t$.
> 
> 
> 
> Explain why this conservation law is written in conservative differential form. Then, given the fact that $U$ has a moving jump discontinuity, provide the mathematical equation that correctly interprets the conservation law. (Hint: should that governing equation be written in differential form?).

The point of writing
$$
\partial_t U+\partial_x F(U)=0
$$
in conservative differential form is that it is (for smooth fields) the local encoding of an integral balance law: $U(x,t)$ is the density of some conserved extensive quantity (per unit length in $x$), and $F(U)$ is the associated flux through a point. In 1D, this form is designed so that, upon integrating over a control volume and using the fundamental theorem of calculus, $\partial_x F$ becomes a boundary flux difference. In particular, the correct “governing equation” to associate to the conservative PDE is the fixed-control-volume balance: for every fixed sub-interval $[x_L,x_R]\subset[a,b]$,
$$
\frac{d}{dt}\int_{x_L}^{x_R} U(x,t)\,dx+F(U(x_R,t))-F(U(x_L,t))=0.
$$
This integral statement still makes sense even when $U$ is only piecewise smooth, and it is therefore the correct mathematical interpretation of the conservation law when a jump discontinuity is present; the pointwise differential expression $\partial_x F(U)$ is not interpreted classically at the jump.

Let the discontinuity be at $x_s(t)=ct$, and define the one-sided limits
$$
U_L(t):=\lim_{x\to x_s(t)^-}U(x,t),\qquad U_R(t):=\lim_{x\to x_s(t)^+}U(x,t),
$$
with corresponding fluxes $F_L(t):=F(U_L(t))$ and $F_R(t):=F(U_R(t))$. Interpreting the conservation law through its integral meaning and shrinking a control volume onto the jump yields the Rankine–Hugoniot jump condition (this is the correct “equation at the discontinuity”):
$$
c\,(U_R-U_L)=F_R-F_L.
$$

One clean way to see this is to work in a shock-attached coordinate $\xi:=x-ct$ (so the discontinuity sits at $\xi=0$). Define $V(\xi,t):=U(\xi+ct,t)$, so that $V(\xi,t)$ is piecewise smooth with a stationary jump at $\xi=0$.

$$
\begin{aligned}
0
&=\partial_t U(x,t)+\partial_x F(U(x,t)) \\
&=\left(\partial_t V(\xi,t)-c\,\partial_\xi V(\xi,t)\right)+\partial_\xi F(V(\xi,t)) \qquad (\xi=x-ct,\; V(\xi,t)=U(\xi+ct,t))\\
&=\partial_t V(\xi,t)+\partial_\xi\big(F(V(\xi,t))-c\,V(\xi,t)\big),
\end{aligned}
$$
so (in the sense of the conservative interpretation) $V$ satisfies the conservation law
$$
\partial_t V+\partial_\xi\big(F(V)-cV\big)=0.
$$
Integrating this conservative form over the fixed interval $\xi\in[-\varepsilon,\varepsilon]$ gives
$$
\begin{aligned}
0
&=\frac{d}{dt}\int_{-\varepsilon}^{\varepsilon} V(\xi,t)\,d\xi+\big(F(V(\varepsilon,t))-cV(\varepsilon,t)\big)-\big(F(V(-\varepsilon,t))-cV(-\varepsilon,t)\big) \\
&\xrightarrow[\varepsilon\to 0]{} (F_R-cU_R)-(F_L-cU_L),
\end{aligned}
$$
so $(F_R-cU_R)=(F_L-cU_L)$, i.e. $c\,(U_R-U_L)=F_R-F_L$.




> [!question] 1.b
> **(b) Why the conservative interpretation survives loss of smoothness**
>
In 4-6 sentences, explain why the conservative formulation still has a clear physical meaning even though $\partial_{x} F(U)$ is not classically defined at the jump. Your explanation should explicitly reference the control-volume (flux) viewpoint.

The conservative form is built so that its fundamental meaning is an integral control-volume balance. For any fixed interval, the time rate of change of the total amount of $U$ inside equals the net flux through the endpoints. That statement does not require $U$ to be differentiable; it only requires that $U$ and the boundary flux values be well-defined almost everywhere (piecewise smooth is enough) so that the integrals and endpoint fluxes make sense. At a jump, the discontinuity is treated as an internal moving boundary across which a flux mismatch must be compensated by transport of $U$ by the moving interface, which is exactly what the Rankine–Hugoniot condition enforces. In this way, even though $\partial_x F(U)$ cannot be evaluated pointwise at the jump, the net flux into/out of any control volume remains well-defined and the conservation statement remains unambiguous. The conservative PDE is therefore interpreted as holding in the weak (integral/distributional) sense, which is precisely the form compatible with shocks and other discontinuities.




> [!question] 1c
> **(c) Why the non-conservative form does not admit the same interpretation**
> 
> Now consider the formally related non-conservative form
> 
> $$
> \partial_{t} U+A(U) \partial_{x} U=0, \quad A(U):=\frac{d F}{d U}
> $$
> 
> In 4-6 sentences, explain why this form does not admit an equally direct boundary-flux interpretation when $U$ contains a jump. Be precise about what quantity is no longer well-defined and what step in the conservative interpretation has no analog here.

The non-conservative form $\partial_t U+A(U)\partial_x U=0$ is obtained from $\partial_t U+\partial_x F(U)=0$ by applying the chain rule $\partial_x F(U)=\frac{dF}{dU}\,\partial_x U$, and that step is valid only when $U$ is sufficiently smooth. If $U$ has a jump, then $\partial_x U$ is not a classical function (it contains a singular distribution concentrated at the discontinuity), so the product $A(U)\,\partial_x U$ is not classically well-defined at the jump because $A(U)$ has no single value there and the “multiply-by-$A(U)$” operation has no canonical meaning on that singular part. Because the equation is not written as a spatial derivative of a flux, integrating it over a control volume does not immediately reduce the spatial term to a difference of boundary fluxes by the fundamental theorem of calculus, so there is no direct control-volume statement of “rate of change inside = flux out − flux in” encoded by this form. In other words, the conservative interpretation survives by reverting to an integral balance with boundary fluxes, but the primitive form has no analogous boundary-flux object built into it once smoothness (and hence the chain rule identity linking it back to $\partial_x F(U)$) is lost.




> [!question] 1d
> **(d) Connection to compressible flow (Euler equations)**
> 
> Using the discussion in Lecture 8, answer briefly:
> (i) Identify (by writing them down) the conservative forms of mass, momentum, and totalenergy for inviscid compressible flow.
> (ii) For one of these governing equations, give an example of a commonly used nonconservative/primitive form (e.g. a material-derivative form) and explain ( $1-3$ sentences) why it is still useful despite its limitations at discontinuities.

(i) The conservative forms are
$$
\partial_{t}\rho+\nabla\cdot(\rho\boldsymbol{u})=0,
$$
$$
\partial_{t}(\rho\boldsymbol{u})+\nabla\cdot(\rho\boldsymbol{u}\otimes\boldsymbol{u})=-\nabla p+\rho\boldsymbol{f},
$$
and
$$
\partial_{t}(\rho E)+\nabla\cdot\big((\rho E+p)\boldsymbol{u}\big)=\rho\boldsymbol{f}\cdot\boldsymbol{u}-\nabla\cdot\boldsymbol{q}_h+\rho\dot{q}_h,
\qquad
E:=e+\frac{1}{2}|\boldsymbol{u}|^{2}.
$$
Here $\rho$ is density, $\boldsymbol{u}$ is velocity, $p$ is pressure, $\boldsymbol{f}$ is body force per unit mass, $\boldsymbol{q}_h$ is heat flux, $\dot{q}_h$ is a volumetric heat addition rate per unit mass, and $\otimes$ denotes the outer product. (For the adiabatic Euler equations with no heat transfer, set $\boldsymbol{q}_h=\boldsymbol{0}$ and $\dot{q}_h=0$.). 

(ii) For example, the momentum equation is often rewritten (for smooth solutions) in primitive/material-derivative form as
$$
\rho\frac{D\boldsymbol{u}}{Dt}=-\nabla p+\rho\boldsymbol{f},
\qquad
\frac{D}{Dt}:=\partial_t+\boldsymbol{u}\cdot\nabla.
$$
This form is still useful because it directly expresses Newton’s second law for a moving fluid element (explicitly isolating the material acceleration), which is often the most transparent form for physical reasoning and for deriving further smooth-flow results, even though it must be used with care at discontinuities where $D\boldsymbol{u}/Dt$ is not well-defined.




## Problem 2: The speed of sound as a thermodynamic response points)

Preamble. Lecture 9 motivates the speed of sound as a thermodynamic measure of how pressure responds to infinitesimal density changes under a fast, reversible response:

$$
a^{2}:=\left(\frac{\partial p}{\partial \rho}\right)_{s} .
$$

> [!question] 2a
> **(a) Why these variables?**
> In 2-4 sentences each, explain why it is natural to treat:
> (i) pressure as the response variable,
> (ii) density as the perturbation variable,
> (iii) entropy as the quantity held fixed (isentropic response).

(i) Pressure is the natural response variable because compressive/expansive disturbances in a compressible medium manifest mechanically through pressure forces: in the momentum equation, it is $\nabla p$ that accelerates fluid elements. In the “thermodynamic thought experiment” of a fast, weak compression, the question “how much restoring force do we get back?” is precisely “how much does $p$ change?”. Thus $(\partial p/\partial \rho)$ measures the stiffness of the medium in the variable that actually drives the mechanical response.

(ii) Density is the natural perturbation variable because compression is fundamentally a volume change of a material element, and $\rho=m/V$ encodes that compression in a convenient local scalar. In compressible flow, kinematics couples directly to $\rho$ through continuity (for smooth fields, $\frac{D\rho}{Dt}=-\rho\,\nabla\cdot\boldsymbol{u}$), so small dilatations correspond to small density changes. Using $\rho$ therefore makes the perturbation both thermodynamically meaningful (how “packed” the material is) and consistent with the variables that appear in the governing equations.

(iii) Entropy is held fixed because the definition is meant to capture a fast, reversible material response: the perturbation is assumed quick enough that heat transfer and irreversible mechanisms have no time to act, so there is no entropy change during the response. In the inviscid/adiabatic limit emphasized in Lecture 9, each fluid element satisfies $\frac{Ds}{Dt}=0$, and small acoustic disturbances are therefore modeled as locally isentropic. Writing $a^{2}=(\partial p/\partial \rho)_s$ makes that modeling assumption explicit by specifying the thermodynamic path along which the derivative is taken.



> [!question] 2b
> **(b) Why a derivative / linear response makes sense**
> Explain why it is physically reasonable to define a local quantity using an infinitesimal perturbation and a linear response (i.e. why the definition involves a derivative). State clearly what assumptions are embedded in doing this.

It is physically reasonable to use a derivative because the “sound-speed” thought experiment concerns very small-amplitude disturbances: if a material element undergoes an infinitesimal compression, then the pressure change is correspondingly small and the first-order (linear) relation between increments is the dominant effect. Thermodynamically, if the fluid admits an equation of state $p=p(\rho,s)$ that is smooth near the local state $(\rho,s)$, then for sufficiently small perturbations with $s$ held fixed one has the first-order approximation
$$
\delta p \approx \left(\frac{\partial p}{\partial \rho}\right)_{s}\,\delta\rho,
$$
and the coefficient $(\partial p/\partial \rho)_s$ is exactly the local proportionality constant captured by the partial derivative (equivalently, by its limit definition). Defining a local property this way also matches how small disturbances propagate in the governing PDEs: linearization about a base state produces wave equations whose characteristic speeds depend only on these first-order response coefficients.

The assumptions embedded in this definition are: local thermodynamic equilibrium (so a state relation $p=p(\rho,s)$ is meaningful pointwise), smoothness of that relation (so the derivative exists), and a timescale separation in which the perturbation is fast and weak enough that heat transfer and irreversible mechanisms do not significantly change the entropy during the response (hence “hold $s$ fixed”). Implicitly, one also assumes the disturbance amplitude is small enough that higher-order nonlinear terms are negligible over the scale of interest; when disturbances are large (e.g. shocks), the linear-response derivative no longer characterizes the full pressure–density relation across the wave.



> [!question] 2c
> **(c) Why it has units and meaning of a speed**
> Using dimensional analysis, show that $a^{2}$ has units of speed squared. Then, in $2-4$ sentences, explain why this thermodynamic thought experiment can be interpreted as giving the speed at which small disturbances travel through the material.

First check units. Pressure has dimensions
$$
[p]=\frac{\text{force}}{\text{area}}=\frac{M L T^{-2}}{L^{2}}=M L^{-1}T^{-2},
$$
and density has dimensions
$$
[\rho]=\frac{\text{mass}}{\text{volume}}=\frac{M}{L^{3}}=M L^{-3}.
$$
Therefore
$$
\left[\left(\frac{\partial p}{\partial \rho}\right)_{s}\right]=\frac{[p]}{[\rho]}
=\frac{M L^{-1}T^{-2}}{M L^{-3}}
=L^{2}T^{-2}
=\left[\left(\frac{L}{T}\right)^{2}\right],
$$
so $a^{2}$ has units of speed squared and $a$ has units of speed.

The physical meaning is that $(\partial p/\partial\rho)_s$ measures the stiffness of the medium to rapid, reversible compression: it is the proportionality between a small density increase and the restoring pressure increase. When the Euler equations are linearized about a uniform base state, the coupling between continuity (relating $\delta\rho$ to the velocity divergence) and momentum (relating acceleration to $\nabla\,\delta p$) produces a wave equation whose characteristic propagation speed depends exactly on this stiffness coefficient. Thus the same local thermodynamic response that tells us “how strongly pressure reacts to compression” sets the speed at which small compressive disturbances (sound waves) travel through the material.





> [!question] 2d
> **(d) Is the speed of sound a flow property?**
> Is it? If not, what is it a property of?

In general, the speed of sound is not a property of the flow field (it is not set by the velocity or by how the fluid is moving); it is a property of the material’s thermodynamic state and equation of state. By definition,
$$
a^{2}=\left(\frac{\partial p}{\partial \rho}\right)_{s},
$$
so $a$ is determined by how the material responds to an isentropic density perturbation at the local state (equivalently, by the local “stiffness” of the medium). For a given constitutive model, $a$ is therefore set by the local thermodynamic variables (e.g. for a calorically perfect ideal gas, $a^{2}=\gamma p/\rho=\gamma RT$, so $a$ depends on temperature/state, not on the flow speed).





## Problem 3: Time derivative of circulation for a material loop ( 20 points)

Preamble. Let $C(t)$ be a material loop moving with the fluid velocity $\boldsymbol{u}(\boldsymbol{x}, t)$. Define the circulation

$$
\Gamma(t):=\oint_{C(t)} \boldsymbol{u} \cdot d \boldsymbol{\ell}
$$

A key kinematic identity used in Kelvin's theorem is

$$
\frac{d \Gamma}{d t}=\oint_{C(t)} \frac{D \boldsymbol{u}}{D t} \cdot d \boldsymbol{\ell}
$$

In this problem you will derive this identity carefully and connect it to the "time derivatives of integrals" framework of Lecture 2.

> [!question] 3a
> **(a) Which time derivative is this? (Lecture 2 language)**
> 
> In 5-10 sentences, explain which sense of time derivative is being taken when differentiating $\Gamma(t)$. Your explanation should explicitly reference the Lecture 2 distinction between comparing values at corresponding points on a moving domain versus comparing values carried by material elements through a fixed domain. Also explain why the Reynolds transport theorem is not the relevant tool for this derivative.

The derivative $\frac{d\Gamma}{dt}$ is the time derivative of a line integral over a moving domain, namely the curve $C(t)$. In the Lecture 2 language, the comparison being made is “at corresponding points on the moving domain”: we label points on the loop by a fixed curve parameter and differentiate holding that label fixed, so we compare the integrand at the same labeled point of $C(t)$ as the loop moves and deforms. Because $C(t)$ is a material loop, those corresponding points are the same material fluid elements at all times, so the time derivative of the composite field $\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)$ produces the material derivative $\frac{D\boldsymbol{u}^{E}}{Dt}$ evaluated along the loop (rather than the Eulerian partial derivative $\partial_t\boldsymbol{u}^{E}$ at fixed $\boldsymbol{x}$). The remaining time dependence comes from the fact that the line element $d\boldsymbol{\ell}$ also changes as the loop stretches and rotates, so one must differentiate both $\boldsymbol{u}^{E}$ and $d\boldsymbol{\ell}$.

This is not the “material elements through a fixed region” situation that motivates the Reynolds transport theorem in Lecture 2. Reynolds transport is the appropriate tool when the integration region is a control volume and you must account for material transport across its boundary via flux terms. Here the integration domain itself is a material object, so there is no advective flux of fluid elements through the domain boundary to track; instead, one differentiates an integral on a moving curve by holding the curve labels fixed and applying chain and product rules.



> [!question] 3b
> **(b) Step-by-step derivation of $\frac{d \Gamma}{d t}$**
> 
> Introduce a curve flow map describing the motion of the material loop:
> 
> $$
> \boldsymbol{x}=\boldsymbol{\psi}(\alpha, t), \quad \alpha \in[0,1], \quad \boldsymbol{\psi}(0, t)=\boldsymbol{\psi}(1, t)
> $$
> 
> where $\alpha$ is a fixed reference label for points on the loop. Define the line element as
> 
> $$
> d \ell=\partial_{\alpha} \psi(\alpha, t) d \alpha
> $$
> 
> Because $C(t)$ is a material loop, the curve moves with the fluid. Express this assumption using Eulerian velocity notation by stating the appropriate evolution equation for $\boldsymbol{\psi}$ in terms of $\boldsymbol{u}^{E}$.
> 
> Using Eulerian fields and the curve flow map, write the circulation as
> 
> $$
> \Gamma(t)=\int_{0}^{1} \boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha, t), t) \cdot \partial_{\alpha} \boldsymbol{\psi}(\alpha, t) d \alpha
> $$
> 
> Differentiate this expression with respect to time while holding the curve label $\alpha$ fixed (i.e. comparing corresponding points on the moving loop, in the sense of Lecture 2). Your derivation should:
> 
> - clearly apply the chain rule to the Eulerian velocity field $\boldsymbol{u}^{E}(\psi(\alpha, \cdot), \cdot)$,
> - apply the product rule to account for the time dependence of both factors in the integrand,
> - use the material-motion assumption for $\boldsymbol{\psi}$ to identify the material derivative of $\boldsymbol{u}^{E}$,
> - explicitly identify and justify the cancellation that occurs because the loop is closed.
> 
> Conclude that
> 
> $$
> \frac{d \Gamma}{d t}=\oint_{C(t)} \frac{D \boldsymbol{u}^{E}}{D t} \cdot d \boldsymbol{\ell}
> $$
> 

Because $C(t)$ is a material loop, each curve label $\alpha$ moves with the local fluid velocity. In Eulerian notation, that assumption is
$$
\partial_t \boldsymbol{\psi}(\alpha,t)=\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t),\qquad \alpha\in[0,1].
$$

Now start from the parameterized circulation
$$
\Gamma(t)=\int_{0}^{1}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha,
\qquad
d\boldsymbol{\ell}=\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha,
$$
and differentiate with respect to $t$ while holding $\alpha$ fixed:
$$
\begin{aligned}
\frac{d\Gamma}{dt}
&=\frac{d}{dt}\int_{0}^{1}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha \\
&=\int_{0}^{1}\frac{d}{dt}\Big(\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\Big)\,d\alpha \\
&=\int_{0}^{1}\Big(\frac{d}{dt}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\Big)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha
\;+\;\int_{0}^{1}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\frac{d}{dt}\big(\partial_\alpha\boldsymbol{\psi}(\alpha,t)\big)\,d\alpha .
\end{aligned}
$$
Apply the chain rule to the Eulerian velocity field composed with the curve map:
$$
\begin{aligned}
\frac{d}{dt}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)
&=\partial_t\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)+\big(\partial_t\boldsymbol{\psi}(\alpha,t)\cdot\nabla\big)\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t) \\
&=\partial_t\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)+\big(\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\nabla\big)\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t) \\
&=\frac{D\boldsymbol{u}^{E}}{Dt}(\boldsymbol{\psi}(\alpha,t),t),
\end{aligned}
$$
where we used the material-motion assumption $\partial_t\boldsymbol{\psi}=\boldsymbol{u}^{E}(\boldsymbol{\psi},t)$ in the second line.

Next, differentiate the line-element factor. Since $\alpha$ is held fixed, we may commute derivatives:
$$
\frac{d}{dt}\big(\partial_\alpha\boldsymbol{\psi}(\alpha,t)\big)
=\partial_\alpha\big(\partial_t\boldsymbol{\psi}(\alpha,t)\big)
=\partial_\alpha\big(\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\big).
$$
Substitute these identities into $\frac{d\Gamma}{dt}$:
$$
\begin{aligned}
\frac{d\Gamma}{dt}
&=\int_{0}^{1}\frac{D\boldsymbol{u}^{E}}{Dt}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha
\;+\;\int_{0}^{1}\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\big(\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\big)\,d\alpha \\
&=\int_{0}^{1}\frac{D\boldsymbol{u}^{E}}{Dt}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha
\;+\;\int_{0}^{1}\partial_\alpha\!\left(\frac{1}{2}\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\right|^{2}\right)\,d\alpha .
\end{aligned}
$$
Because the loop is closed, $\boldsymbol{\psi}(0,t)=\boldsymbol{\psi}(1,t)$, and $\boldsymbol{u}^{E}$ is single-valued as a function of position, the boundary values match:
$$
\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(1,t),t)\right|^{2}
\;=\;
\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(0,t),t)\right|^{2}.
$$
Therefore the second integral vanishes:
$$
\int_{0}^{1}\partial_\alpha\!\left(\frac{1}{2}\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(\alpha,t),t)\right|^{2}\right)\,d\alpha
=\frac{1}{2}\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(1,t),t)\right|^{2}-\frac{1}{2}\left|\boldsymbol{u}^{E}(\boldsymbol{\psi}(0,t),t)\right|^{2}
=0.
$$
Hence
$$
\frac{d\Gamma}{dt}
=\int_{0}^{1}\frac{D\boldsymbol{u}^{E}}{Dt}(\boldsymbol{\psi}(\alpha,t),t)\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha
=\oint_{C(t)}\frac{D\boldsymbol{u}^{E}}{Dt}\cdot d\boldsymbol{\ell}.
$$




> [!question] 3c
> **(c) Interpretation**
> 
> In 3-5 sentences, interpret the result
> 
> $$
> \frac{d \Gamma}{d t}=\oint_{C(t)} \frac{D \boldsymbol{u}}{D t} \cdot d \boldsymbol{\ell}
> $$
> 
> What does it say in words about how circulation evolves for a loop moving with the fluid?

This identity says that the rate of change of circulation around a loop that is carried by the fluid is obtained by integrating the material acceleration $\frac{D\boldsymbol{u}}{Dt}$ around that same loop. In other words, to know how $\Gamma(t)=\oint_{C(t)}\boldsymbol{u}\cdot d\boldsymbol{\ell}$ changes, you do not separately track the loop’s deformation; all of that geometry is already accounted for by taking the material derivative and integrating along the instantaneous material loop. The circulation can therefore change only if there is a nonzero net tangential component of acceleration accumulated around the loop; if $\frac{D\boldsymbol{u}}{Dt}$ is everywhere the gradient of a scalar potential (so its line integral around a closed curve vanishes), then $\Gamma(t)$ is conserved. This kinematic result is the key bridge to Kelvin’s theorem: once the momentum equation is used to rewrite $\frac{D\boldsymbol{u}}{Dt}$ in terms of forces, it becomes a statement about which forces can or cannot generate circulation.




## Problem 4: Completing Kelvin's circulation theorem

Preamble. Kelvin's theorem identifies conditions under which circulation around a material loop is conserved in inviscid flow. In this problem you will justify the relevant simplifying assumptions and then complete the thermodynamic step that makes pressure forces conservative under isentropic conditions.


> [!question] 4a
> **(a) Conservative body forces and why they drop out**
> 
> In many settings (e.g. gravity), body forces derive from a potential and therefore contribute no net circulation.
> 
> Explain what physical assumption is being made when we say the body force per unit mass is conservative, and give at least one concrete example where this is appropriate. Then show that if $\boldsymbol{f}=-\nabla \Phi$ for some scalar potential $\Phi(\boldsymbol{x})$, the circulation contribution from body forces vanishes:
> 
> $$
> \oint_{C(t)} \boldsymbol{f} \cdot d \boldsymbol{\ell}=0
> $$

Saying the body force per unit mass is conservative means we assume it derives from a scalar potential, so that the force does no net work around a closed loop and depends only on position (not on the path taken). Physically, this models body forces that are long-range and derivable from a potential energy, such as gravity in a fixed gravitational field. For example, near Earth’s surface one may take $\Phi(\boldsymbol{x})=g z$ (with $z$ the upward vertical coordinate and $g$ constant), so that $\boldsymbol{f}=-\nabla\Phi=-g\,\hat{\boldsymbol{z}}$.

To show the circulation contribution vanishes, assume
$$
\boldsymbol{f}(\boldsymbol{x})=-\nabla \Phi(\boldsymbol{x}),
$$
and parameterize the closed loop $C(t)$ at a fixed time by $\boldsymbol{x}=\boldsymbol{\psi}(\alpha,t)$, $\alpha\in[0,1]$, with $\boldsymbol{\psi}(0,t)=\boldsymbol{\psi}(1,t)$, so that $d\boldsymbol{\ell}=\partial_\alpha \boldsymbol{\psi}(\alpha,t)\,d\alpha$. Then
$$
\begin{aligned}
\oint_{C(t)}\boldsymbol{f}\cdot d\boldsymbol{\ell}
&=\int_{0}^{1}\boldsymbol{f}(\boldsymbol{\psi}(\alpha,t))\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha \\
&=-\int_{0}^{1}\nabla\Phi(\boldsymbol{\psi}(\alpha,t))\cdot\partial_\alpha\boldsymbol{\psi}(\alpha,t)\,d\alpha \\
&=-\int_{0}^{1}\partial_\alpha\big(\Phi(\boldsymbol{\psi}(\alpha,t))\big)\,d\alpha \\
&=-\Big(\Phi(\boldsymbol{\psi}(1,t))-\Phi(\boldsymbol{\psi}(0,t))\Big) \\
&=0,
\end{aligned}
$$
where the third line is the chain rule and the final line uses closure of the loop.




> [!question] 4b
> **(b) From Gibbs relation to gradient form**
> 
> Start from the Gibbs relation
> 
> $$
> d h=T d s+\frac{1}{\rho} d p
> $$
> 
> Derive, step by step, the spatial-gradient identity
> 
> $$
> \frac{1}{\rho} \nabla p=\nabla h-T \nabla s .
> $$
> 
> Your steps should make clear how a thermodynamic differential identity is converted into a spatial vector identity (as discussed in lecture).

We start from the Gibbs relation (a thermodynamic identity for a simple compressible substance)
$$
d h=T\,d s+\frac{1}{\rho}\,d p.
$$
To convert this differential identity into a spatial-gradient identity, we interpret each thermodynamic variable as a field evaluated at a point in space and time under local thermodynamic equilibrium. In particular, view specific enthalpy as a state function of $(s,p)$,
$$
h=h(s,p),
$$
so that $s=s(\boldsymbol{x},t)$ and $p=p(\boldsymbol{x},t)$ imply
$$
h(\boldsymbol{x},t)=h\big(s(\boldsymbol{x},t),p(\boldsymbol{x},t)\big).
$$
The total differential of $h(s,p)$ is, by the chain rule,
$$
d h=\left(\frac{\partial h}{\partial s}\right)_{p} d s+\left(\frac{\partial h}{\partial p}\right)_{s} d p .
$$
Comparing this with the Gibbs relation $d h=T\,d s+\frac{1}{\rho}\,d p$ shows (pointwise, at the same thermodynamic state)
$$
\left(\frac{\partial h}{\partial s}\right)_{p}=T,
\qquad
\left(\frac{\partial h}{\partial p}\right)_{s}=\frac{1}{\rho}.
$$
Now take the spatial gradient of the composite field $h(\boldsymbol{x},t)=h(s(\boldsymbol{x},t),p(\boldsymbol{x},t))$. Applying the multivariable chain rule in spatial form gives
$$
\nabla h
=\left(\frac{\partial h}{\partial s}\right)_{p}\nabla s+\left(\frac{\partial h}{\partial p}\right)_{s}\nabla p
=T\,\nabla s+\frac{1}{\rho}\,\nabla p .
$$
Rearranging yields the desired identity,
$$
\frac{1}{\rho}\nabla p=\nabla h-T\nabla s.
$$




> [!question] 4c
> **(c) Isentropic simplification and conservative pressure forces**
> 
> Assume the flow is isentropic so that $s$ is spatially uniform (or at least constant along the region of interest). Use the result from the previous part to show that pressure forces are conservative in the sense that
> 
> $$
> \frac{1}{\rho} \nabla p=\nabla h
> $$
> 
> Explain briefly ( $2-4$ sentences) why this is the key step that allows Kelvin's theorem to hold for inviscid, isentropic flow.

If the flow is isentropic in the region of interest, then entropy is spatially uniform there, so
$$
\nabla s=\boldsymbol{0}.
$$
Substituting this into the identity from part (b),
$$
\frac{1}{\rho}\nabla p=\nabla h-T\nabla s,
$$
gives immediately
$$
\frac{1}{\rho}\nabla p=\nabla h.
$$

This is the key step for Kelvin’s theorem because it shows the pressure force per unit mass becomes a conservative (gradient) force under isentropic conditions. Therefore its contribution to the circulation evolution is a closed-loop integral of a gradient, $\oint_{C(t)}\frac{1}{\rho}\nabla p\cdot d\boldsymbol{\ell}=\oint_{C(t)}\nabla h\cdot d\boldsymbol{\ell}=0$, so pressure cannot generate circulation. Combined with conservative body forces (part (a)), the momentum equation then implies $\frac{d\Gamma}{dt}=0$ for a material loop in inviscid, isentropic flow.




> [!question] 4d
> **(d) Kelvin's theorem (putting the pieces together)**
> 
> Combine:
> 
> - the kinematic identity from Problem 3,
> - the inviscid momentum equation in primitive form,
> - the results of parts (a)-(c),
> to conclude that, under appropriate assumptions, the circulation around a material loop is conserved:
> 
> $$
> \frac{d \Gamma}{d t}=0
> $$
> 
> Clearly state the assumptions you used.

Start from the kinematic identity for a material loop (Problem 3):
$$
\frac{d\Gamma}{dt}=\oint_{C(t)}\frac{D\boldsymbol{u}}{Dt}\cdot d\boldsymbol{\ell}.
$$
Use the inviscid momentum equation in primitive form (Lecture 8),
$$
\rho\frac{D\boldsymbol{u}}{Dt}=-\nabla p+\rho\boldsymbol{f},
$$
and divide by $\rho$ to obtain
$$
\frac{D\boldsymbol{u}}{Dt}=-\frac{1}{\rho}\nabla p+\boldsymbol{f}.
$$
Substitute this into the circulation derivative:
$$
\frac{d\Gamma}{dt}
=\oint_{C(t)}\left(-\frac{1}{\rho}\nabla p+\boldsymbol{f}\right)\cdot d\boldsymbol{\ell}
=-\oint_{C(t)}\frac{1}{\rho}\nabla p\cdot d\boldsymbol{\ell}+\oint_{C(t)}\boldsymbol{f}\cdot d\boldsymbol{\ell}.
$$
Assume the body force per unit mass is conservative (part (a)), so $\boldsymbol{f}=-\nabla\Phi$ for some scalar potential $\Phi(\boldsymbol{x})$. Then
$$
\oint_{C(t)}\boldsymbol{f}\cdot d\boldsymbol{\ell}=-\oint_{C(t)}\nabla\Phi\cdot d\boldsymbol{\ell}=0.
$$
Assume the flow is isentropic in the region of interest so that $\nabla s=\boldsymbol{0}$, and use the thermodynamic result of parts (b)–(c) to conclude
$$
\frac{1}{\rho}\nabla p=\nabla h.
$$
Therefore,
$$
\oint_{C(t)}\frac{1}{\rho}\nabla p\cdot d\boldsymbol{\ell}
=\oint_{C(t)}\nabla h\cdot d\boldsymbol{\ell}
=0,
$$
since the line integral of a gradient around a closed loop vanishes. Putting these together gives
$$
\frac{d\Gamma}{dt}=0,
$$
which is Kelvin’s circulation theorem.

Assumptions used: (1) $C(t)$ is a material loop moving with $\boldsymbol{u}$, and the fields are smooth enough for the chain rule/product rule manipulations in Problem 3; (2) inviscid momentum balance holds in primitive form; (3) the body force per unit mass is conservative, $\boldsymbol{f}=-\nabla\Phi$ (so the domain is taken to be such that $\Phi$ is single-valued, e.g. simply connected); (4) the flow is isentropic in the region of interest so that $\nabla s=\boldsymbol{0}$ and hence $\frac{1}{\rho}\nabla p=\nabla h$; (5) local thermodynamic equilibrium holds so the Gibbs relation is applicable pointwise.




## Problem 5: Crocco's theorem—interpretation and contrast with Kelvin (18 points)

Preamble. Crocco's theorem provides a complementary viewpoint to Kelvin's theorem by making explicit how thermodynamic structure (entropy and stagnation enthalpy) correlates with vorticity. In lecture, you saw forms of Crocco's relation such as (for an appropriate set of assumptions)

$$
\boldsymbol{\omega} \times \boldsymbol{u}=\nabla h_{0}-T \nabla s, \quad h_{0}:=h+\frac{1}{2}|\boldsymbol{u}|^{2},
$$

and you discussed physical interpretations of its terms.


> [!question] 5a
> **(a) Assumptions: Kelvin vs. Crocco**
> 
> List the key assumptions under which Kelvin's theorem holds. Then describe (briefly but precisely) the assumptions that enter the Crocco relation given above. Which Kelvin assumptions are relaxed in Crocco's setting, and what new terms appear as a result? Are there any assumptions in Kelvin's circulation theorem that persist in Crocco's theorem?

Kelvin’s circulation theorem is a statement about the evolution of circulation around a material loop $C(t)$, $\Gamma(t)=\oint_{C(t)}\boldsymbol{u}\cdot d\boldsymbol{\ell}$. The assumptions used to obtain $\frac{d\Gamma}{dt}=0$ are: inviscid momentum balance in primitive form,
$$
\rho\frac{D\boldsymbol{u}}{Dt}=-\nabla p+\rho\boldsymbol{f},
$$
conservative body forces per unit mass, $\boldsymbol{f}=-\nabla\Phi$ so that $\oint_{C(t)}\boldsymbol{f}\cdot d\boldsymbol{\ell}=0$, and isentropic motion in the region of interest so that entropy has no spatial variation there (equivalently $\nabla s=\boldsymbol{0}$, which makes the pressure force conservative via $\frac{1}{\rho}\nabla p=\nabla h$). One also assumes sufficient smoothness/local thermodynamic equilibrium so that the chain rule manipulations, the Gibbs relation, and the step where gradient integrates to zero around a closed loop step are legitimate (and, implicitly, that the relevant scalar potentials are single-valued on the domain).

The Crocco relation,
$$
\boldsymbol{\omega}\times\boldsymbol{u}=\nabla h_{0}-T\nabla s,\qquad h_{0}:=h+\frac{1}{2}|\boldsymbol{u}|^{2},
$$
is obtained by starting from the same inviscid momentum equation (typically also taking body forces to be conservative so they can be absorbed into a potential, as in lecture), rewriting the material acceleration using the vector identity
$$
\frac{D\boldsymbol{u}}{Dt}=\partial_t\boldsymbol{u}+(\boldsymbol{u}\cdot\nabla)\boldsymbol{u}
=\partial_t\boldsymbol{u}+\nabla\!\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)-\boldsymbol{u}\times(\nabla\times\boldsymbol{u}),
\qquad \boldsymbol{\omega}:=\nabla\times\boldsymbol{u},
$$
and converting the thermodynamic differential identity (Gibbs relation)
$$
d h=T\,d s+\frac{1}{\rho}\,d p
$$
into the spatial-gradient form $\frac{1}{\rho}\nabla p=\nabla h-T\nabla s$. The specific steady form written above additionally assumes $\partial_t\boldsymbol{u}=\boldsymbol{0}$ (in the unsteady form, the left-hand side would include the extra term $-\partial_t\boldsymbol{u}$, as in lecture). No isentropic assumption is imposed in Crocco’s setting; $s(\boldsymbol{x})$ is allowed to vary so $\nabla s$ can be nonzero.

Relative to Kelvin’s theorem, Crocco’s theorem relaxes the “isentropic/entropy-uniform” restriction, and as a consequence a new thermodynamic term appears: the entropy-gradient contribution $-T\nabla s$, which can act as a driver of rotational structure. Crocco’s relation also exposes an additional mechanism through $\nabla h_{0}$: spatial variation of stagnation enthalpy enters the balance on the same footing as entropy variation. At the same time, several Kelvin assumptions persist in the Crocco framework: the flow is still inviscid, conservative body forces are still assumed (or absorbed into the definition of $h_{0}$ if $\Phi$ is retained), and the same local thermodynamic assumptions (simple compressible substance and applicability of the Gibbs relation pointwise) are used.



> [!question] 5b
> 
> **(b) Interpreting the Crocco terms**
> 
> Using the Crocco relation
> 
> $$
> \boldsymbol{\omega} \times \boldsymbol{u}=\nabla h_{0}-T \nabla s,
> $$
> 
> explain in words what it says about vorticity generation/organization in high-speed flows. In particular:
> 
> - What does a nonzero $\nabla s$ imply?
> - What does a nonzero $\nabla h_{0}$ imply?
> - Why do these mechanisms disappear under Kelvin's assumptions?

Crocco’s relation
$$
\boldsymbol{\omega}\times\boldsymbol{u}=\nabla h_{0}-T\nabla s
$$
organizes vorticity not as an independent “extra field,” but as something constrained by thermodynamic gradients. Geometrically, the left-hand side shows that the relation controls the component of vorticity not parallel to the velocity: it is the *cross-stream* rotational content that must adjust so that $\boldsymbol{\omega}\times\boldsymbol{u}$ balances the gradients on the right-hand side.

A nonzero $\nabla s$ indicates spatial entropy variation, which in compressible flow is the signature of non-isentropic behavior (entropy production or entropy being non-uniform due to heating/irreversibility). In Crocco’s balance, $-T\nabla s$ acts as a direct thermodynamic driver: if $\nabla s\neq \boldsymbol{0}$, then (unless the $\nabla h_{0}$ term exactly cancels it) the right-hand side is nonzero and the flow cannot remain everywhere irrotational in regions where $\boldsymbol{u}\neq \boldsymbol{0}$; rotational structure must appear/organize so that $\boldsymbol{\omega}\times\boldsymbol{u}$ matches this forcing.

A nonzero $\nabla h_{0}$ indicates spatial variation in stagnation enthalpy (total mechanical–thermal energy per unit mass carried by the flow, in the inviscid setting). In Crocco’s relation, $\nabla h_{0}$ is another driver of rotational structure: if the total energetic state varies from place to place, then the momentum balance cannot be purely potential, and vorticity must generally be present unless these gradients align in a special way with the velocity field.

These mechanisms disappear under Kelvin’s assumptions because Kelvin’s theorem imposes conditions that make both forcing terms conservative/absent: isentropy makes $\nabla s=\boldsymbol{0}$, and (in the Kelvin setting) the pressure term reduces to a pure gradient whose closed-loop integral vanishes, preventing circulation generation. In the stronger steady Crocco reading highlighted in lecture, if the flow is also isentropic and has uniform stagnation enthalpy so that $\nabla s=\boldsymbol{0}$ and $\nabla h_{0}=\boldsymbol{0}$, then the right-hand side is zero and Crocco reduces to $\boldsymbol{\omega}\times\boldsymbol{u}=\boldsymbol{0}$, which forces $\boldsymbol{\omega}=\boldsymbol{0}$ wherever $\boldsymbol{u}\neq \boldsymbol{0}$.




> [!question] 5c
> **(c) Physical sources of $\nabla s$ and $\nabla h_{0}$**
> 
> Give at least three distinct physical mechanisms that can produce spatial variation in entropy and/or stagnation enthalpy in compressible flow (e.g. shocks, heat addition, viscous effects, etc.). For each mechanism, state whether it primarily affects $s, h_{0}$, or both.

Shocks primarily create spatial variation in entropy $s$. A shock is a thin region of strong compression in which dissipative/irreversible physics (not captured by the inviscid model) produces entropy, so $s$ jumps across the shock and $\nabla s$ is nonzero in a shock-attached sense (a sharp gradient in the real flow, or a discontinuity in the inviscid idealization). In contrast, for an adiabatic shock with no external work input, the stagnation enthalpy $h_{0}=h+\frac{1}{2}|\boldsymbol{u}|^{2}$ is typically (to leading order) conserved, so shocks are most directly associated with $s$ rather than with changes in $h_{0}$.

Heat addition (volumetric heating $\dot{q}_{h}$ or conductive heat flux $\boldsymbol{q}_{h}$) produces spatial variation in both $h_{0}$ and $s$. Adding heat changes the energy content of fluid elements and therefore changes their stagnation enthalpy, while also supplying entropy (and, in realistic settings, often generating additional irreversible entropy production). If the heat input is localized in space (heated walls, localized burners, radiative heating regions), it naturally produces nonzero $\nabla h_{0}$ and/or $\nabla s$.

Viscous effects (e.g. boundary layers, shear layers, or any region with large velocity gradients) primarily produce spatial variation in entropy $s$. Viscous dissipation is an irreversible mechanism and therefore contributes positively to the local entropy production rate (Lecture 9), so it tends to create entropy gradients across shear layers and near walls. In many adiabatic internal flows, viscous action largely redistributes energy between kinetic and internal forms without requiring large changes in $h_{0}$, so the most robust signature is $\nabla s\neq\boldsymbol{0}$.

Shaft work or other mechanical energy input/extraction (fans, compressors, turbines, or prescribed work source terms) primarily produces spatial variation in $h_{0}$. Such devices change the total mechanical–thermal energy per unit mass carried by the flow, so they directly change stagnation enthalpy and hence generate $\nabla h_{0}$ when the work input is nonuniform in space. Depending on how idealized the process is, the associated entropy change may be small (nearly isentropic machines) or significant (real machines with losses), so in practice this mechanism can affect $h_{0}$ alone or both $h_{0}$ and $s$.
