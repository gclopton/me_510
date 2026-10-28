
# Problem 1: Thermodynamic closure and linearized pressure response (20 points)



> [!exercise]
> 
> Preamble. A central theme of this course is that compressible-flow governing equations require both conservation laws and thermodynamic closure. In this problem, you will connect the thermodynamic definition of sound speed to a linearized pressure-density relation and interpret what that relation means physically. Consider a calorically perfect ideal gas in a uniform reference state ( $p_{\bullet}, p_*, T_*$ ). Suppose the gas experiences a small, fast, reversible disturbance so that the response is locally isentropic.
> 
> 
> **(a) Thermodynamic definition and interpretation**
> 
> State the thermodynamic definition of sound speed,
> 
> $$
> a^2=\left(\frac{\partial p}{\partial \rho}\right)_s,
> $$
> 
> and explain briefly why pressure is the response variable, density is the perturbation variable, and entropy is held fixed.
> 
> 
> **(b) Linearized pressure response**
> 
> 
> 
> Use a first-order expansion about the reference state to derive a linearized relation between $p^{\prime}$ and $\rho^{\prime}$ of the form
> 
> $$
> p^{\prime}=a_*^2 \rho^{\prime}
> $$
> 
> 
> Be explicit about what quantity is being linearized, what state the derivative is evaluated at, and what assumptions justify this approximation.
> 
> **(c) Physical interpretation**
> 
> 
> 
> In 3-5 sentences, explain what this relation means physically. Why does it make sense that a thermodynamic derivative governs the response of small compressive disturbances?
> 
> **(d) Material property versus flow property**
> 
> 
> 
> Comment briefly on whether the sound speed should be viewed primarily as a material/thermodynamic property or a flow property, and explain your reasoning.


##### problem 1.a
- Lecture 9, lines 107-125: introduces the thermodynamic thought experiment, states the fast/weak/isentropic assumptions, and explains why the derivative is taken with entropy held fixed.
- Lecture 9, lines 127-140: gives the definition
  $$
  a^{2}:=\left(\frac{\partial p}{\partial \rho}\right)_{s}
  $$
  and interprets it as the stiffness of the medium to compression.
- Lecture 8, lines 269-289: explains that pressure appears mechanically in the governing equations but is determined by the thermodynamic state, which is useful for explaining why pressure is the response variable.
- Lecture 10, lines 119-129: explains that pressure generally depends on $(\rho,s)$ and that under isentropic conditions it reduces to a function of density alone, which helps justify why density is the perturbation variable and entropy is held fixed.

##### problem 1.b
- Lecture 10, lines 119-129: pressure is initially viewed as $p=p(\rho,s)$ and then, under isentropic conditions, as $p=p(\rho)$; this is the structural starting point for linearizing pressure with respect to density.
- Lecture 9, lines 114-125: states the assumptions behind the local linear response, namely a small, fast, reversible disturbance with entropy fixed.
- Lecture 9, lines 137-140: identifies the derivative in the linearization as
  $$
  a^{2}=\left(\frac{\partial p}{\partial \rho}\right)_{s}.
  $$
- Lecture 9, lines 143-151: gives the ideal-gas specialization for sound speed, useful when evaluating the derivative at the reference state for a calorically perfect ideal gas.
- Note: the lectures provide the ingredients for the first-order expansion, but they do not appear to write the exact Taylor-linearized relation $p' = a_*^2 \rho'$ verbatim.

##### problem 1.c
- Lecture 9, lines 127-140: explains that $(\partial p/\partial \rho)_s$ measures the stiffness of the medium and that this stiffness sets the characteristic speed of small compressive disturbances.
- Lecture 9, lines 153-161: interprets Mach number as a comparison between flow advection and the medium's ability to communicate pressure changes acoustically, which helps with the physical explanation of the linearized relation.

##### problem 1.d
- Lecture 9, lines 119-125: explicitly states that the derivative defining sound speed is a material property and depends on the thermodynamic behavior of the fluid, not on its motion.
- Lecture 9, lines 143-151: for a calorically perfect ideal gas, shows that the speed of sound depends on the thermodynamic state of the fluid.
- Lecture 8, lines 269-289: supports the distinction between mechanical appearance in the flow equations and thermodynamic determination from state variables, which is useful for explaining why sound speed is primarily a material/thermodynamic property rather than a flow property.





# Problem 2: Interpreting coupled quasi-one-dimensional forcing

> [!exercise]
>
> Preamble. In Lectures 5-7, the quasi-one-dimensional governing equations were reorganized into an input-output framework relating imposed driving increments to local flow responses. In this problem, you will use that framework qualitatively to reason about how multiple simultaneous drivers interact. Your focus should be on interpretation rather than algebra.
> Consider steady quasi-one-dimensional flow of a calorically perfect gas. Suppose that over a short region of a duct the following small driving increments occur simultaneously:
> 
> $$
> \varepsilon_A<0, \quad \varepsilon_{T_0}>0, \quad \varepsilon_f=0
> $$
> 
> 
> You may assume the local input-output structure
> 
> $$
> \varepsilon_{\text {out }}=C(M) \varepsilon_{\text {in }}
> $$
> 
> and reason qualitatively without computing coefficients explicitly.
> 
> **(a) Subsonic response**
> 
> 
> Assume $M<1$. Without computing coefficients explicitly, predict qualitatively how $u, p$, and $T$ respond to the imposed drivers. Explain your reasoning physically.
> 
> **(b) Supersonic response**
> 
> 
> Repeat part (a) for $M>1$, again explaining your reasoning physically.
> 
> **(c) Competing effects**
> 
> 
> Explain how geometric forcing (area decrease) and heat addition compete in their influence on the flow. Your answer should address both acceleration and thermodynamic-state effects.
> 
> **(d) System-level interpretation**
> 
> Explain why the net response cannot be inferred from any single governing equation in isolation. Why is the coupled quasi-one-dimensional system viewpoint essential here?


##### problem 2.a
- Lecture 6, lines 44-77: identifies the imposed drivers $\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}$ and the flow responses $\varepsilon_u, \varepsilon_p, \varepsilon_\rho, \varepsilon_T$.
- Lecture 6, lines 174-215: gives the explicit input-output map $\varepsilon_{\mathrm{out}} = C(M)\varepsilon_{\mathrm{in}}$, including the rows needed to reason about the signs of $u$, $p$, and $T$ responses when $\varepsilon_A<0$, $\varepsilon_{T_0}>0$, and $\varepsilon_f=0$.
- Lecture 6, lines 219-235: explains how to read the rows and columns of $C(M)$ as responses to individual drivers, and notes that the same structure applies to $p$ and $T$, not just $u$.
- Lecture 7, lines 31-72: interprets area forcing physically and gives the subsonic sign rule that area decrease accelerates the flow.
- Lecture 7, lines 105-127: interprets heat/work forcing physically and gives the subsonic sign rule that heat addition accelerates the flow.
- Lecture 7, lines 129-137: synthesizes why Mach number controls the qualitative response.

##### problem 2.b

- Lecture 6, lines 44-77: identifies the imposed drivers $\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}$ and the flow responses $\varepsilon_u, \varepsilon_p, \varepsilon_\rho, \varepsilon_T$.
- Lecture 6, lines 174-215: gives the explicit input-output map $\varepsilon_{\mathrm{out}} = C(M)\varepsilon_{\mathrm{in}}$, including the rows needed to reason about the signs of $u$, $p$, and $T$ responses when $\varepsilon_A<0$, $\varepsilon_{T_0}>0$, and $\varepsilon_f=0$.
- Lecture 6, lines 219-235: explains how to read the rows and columns of $C(M)$ as responses to individual drivers, and notes that the same structure applies to $p$ and $T$, not just $u$.
- Lecture 7, lines 38-72: interprets area forcing physically and gives the supersonic sign rule that area decrease decelerates the flow.
- Lecture 7, lines 105-127: interprets heat/work forcing physically and gives the supersonic sign rule that heat addition decelerates the flow.
- Lecture 7, lines 129-137: synthesizes why Mach number controls the qualitative response.

##### problem 2.c

- Lecture 7, lines 38-72: area forcing by itself, including the sign reversal with Mach number.
- Lecture 7, lines 105-127: heat/work forcing by itself, including the sign reversal with Mach number.
- Lecture 7, lines 129-139: synthesis explaining that Mach number governs how pressure work and kinetic energy are exchanged, which is the key idea for discussing competition between geometric forcing and heat addition.
- Lecture 6, lines 206-215: explicit $C(M)$ matrix, useful for seeing that geometry and heat input affect not only velocity but also pressure and temperature.
- Lecture 5, lines 219-242: energy relation showing how $\varepsilon_{T_0}$ couples thermal forcing to $\varepsilon_T$ and $\varepsilon_u$.
- Lecture 5, lines 245-275: equation-of-state closure $\varepsilon_p = \varepsilon_\rho + \varepsilon_T$, useful for discussing thermodynamic-state effects rather than just acceleration.

##### problem 2.d

- Lecture 5, lines 63-68: continuity relation in $\varepsilon$-form.
- Lecture 5, lines 177-190: momentum relation in $\varepsilon$-form.
- Lecture 5, lines 219-242: energy relation in $\varepsilon$-form.
- Lecture 5, lines 245-275: equation-of-state closure.
- Lecture 6, lines 36-77: explains why the problem must be treated by splitting the variables into drivers and responses rather than reading any one equation in isolation.
- Lecture 6, lines 79-145: shows how the four governing equations are collected into a coupled linear system.
- Lecture 6, lines 164-235: explains the matrix interpretation and the input-output map, which is the clearest lecture material for why the net response is a coupled system effect.
# Problem 3: Linearized acoustic equations from conservation laws

> [!exercise]
> 
> Preamble. By this stage of the course, we have studied conservation laws, thermodynamic closure, and the interpretation of governing-equation structure. In this problem, you will bring those threads together by deriving a linearized one-dimensional compressible-flow system for small disturbances about a uniform base state. The goal is not yet to classify or solve the resulting PDE, but to expose where the linearized wave structure comes from.
> 
> Consider inviscid, one-dimensional compressible flow with no body forces. Start from the conservative forms of mass and momentum conservation,
> 
> $$
> \partial_t \rho+\partial_x(\rho u)=0, \quad \partial_t(\rho u)+\partial_x\left(\rho u^2+p\right)=0
> $$
> 
> 
> Assume a uniform base state
> 
> $$
> \rho(x, t)=\rho_*+\rho^{\prime}(x, t), \quad u(x, t)=u_*+u^{\prime}(x, t), \quad p(x, t)=p_*+p^{\prime}(x, t),
> $$
> 
> where primes denote small disturbances.
> 
> **(a) Linearized continuity equation**
> 
> 
> 
> Substitute the perturbation expansion into the continuity equation and retain only first-order terms to derive the linearized mass equation.
> 
> 
> **(b) Linearized momentum equation**
> 
> 
> Substitute the perturbation expansion into the momentum equation and retain only first-order terms to derive the linearized momentum equation.
> 
> **(c) Thermodynamic closure**
> 
> 
> Assume the disturbance is locally isentropic and use the relation
> 
> $$
> p^{\prime}=a_*^2 \rho^{\prime}
> $$
> 
> to close the linearized system. Briefly justify why this assumption is appropriate for small acoustic disturbances.
> 
> **(d) Coupled perturbation system**
> 
> [5 pts]
> 
> Write the resulting equations clearly as a coupled linear system for the perturbation variables.
> 
> **(e) Interpretation**
> 
> 
> In 3-5 sentences per item, explain the following:
> (i) Why does this system already suggest propagating disturbances, even before solving or classifying the equations? Your answer should reference the coupling structure of the linearized equations and the role of compressibility.
> (ii) Why is conservation of energy not needed to close the system here? In your explanation, discuss (i) how the assumption of locally isentropic disturbances reduces the number of independent thermodynamic variables, and (ii) how this leads to the closure relation $p^{\prime}=a_*^2 \rho^{\prime}$.


##### problem 3.a
- Lecture 8, lines 12-26: gives the conservative PDE forms, including the mass equation
  $$
  \partial_t \rho + \nabla \cdot (\rho \mathbf{u}) = 0,
  $$
  which is the starting point for the 1D continuity linearization.
- Lecture 8, lines 8-10: explains why PDE form is useful for studying local coupling, propagation, and disturbances.
- Note: the lectures provide the governing conservation law, but they do not appear to carry out the explicit first-order perturbation expansion for the continuity equation verbatim.

##### problem 3.b

- Lecture 8, lines 14-24: gives the conservative momentum equation
  $$
  \partial_t (\rho \mathbf{u}) + \nabla \cdot (\rho \mathbf{u} \otimes \mathbf{u}) = - \nabla p + \rho \mathbf{f},
  $$
  which is the starting point for the 1D momentum linearization.
- Lecture 8, lines 46-97: expands the momentum equation with product rules and shows how the terms are organized, which is useful background when expanding and retaining only first-order perturbation terms.
- Note: the lectures provide the governing momentum law and its smooth-flow organization, but they do not appear to write the explicit perturbation-linearized 1D momentum equation verbatim.

##### problem 3.c

- Lecture 9, lines 93-103: gives the local isentropic condition $Ds/Dt = 0$ under the idealized assumptions relevant for small acoustic disturbances.
- Lecture 9, lines 111-140: introduces the thermodynamic thought experiment for small, fast, reversible disturbances and defines
  $$
  a^2 = \left( \frac{\partial p}{\partial \rho} \right)_s .
  $$
- Lecture 9, lines 137-151: explains that this derivative governs the propagation of small compressive disturbances and gives the calorically perfect ideal-gas specialization.
- Lecture 10, lines 119-129: explains that pressure generally depends on $(\rho, s)$ but reduces to $p = p(\rho)$ under isentropic conditions, which is the structural basis of the closure relation.

##### problem 3.d

- Lecture 8, lines 12-24: gives the conservative mass and momentum equations that form the starting point of the linearized perturbation system.
- Lecture 8, lines 238-289: explains why conservation laws alone do not close the system and why a thermodynamic closure relation is needed.
- Lecture 9, lines 111-140: defines the sound-speed closure needed to connect $p'$ and $\rho'$.
- Lecture 10, lines 119-129: shows how isentropy reduces the thermodynamic dependence to a density-only relation, which is what makes the coupled linear system close without introducing additional thermodynamic unknowns.

##### problem 3.e

###### part i

- Lecture 8, lines 8-10: explains that PDE form exposes how variations are coupled and how disturbances propagate.
- Lecture 9, lines 137-140: says that the thermodynamic stiffness measured by $(\partial p / \partial \rho)_s$ sets the characteristic speed of small compressive disturbances.
- Lecture 12, lines 29-43: directly frames unsteady 1D compressible flow as acoustic-wave propagation and presents the corresponding linearized 1D equation, which is useful for the physical interpretation even though Problem 3 works with the first-order system instead of the potential equation.

###### part ii

- Lecture 8, lines 281-289: explains the general need for thermodynamic closure and, in the full Euler system, the role of pressure as a thermodynamically determined variable.
- Lecture 9, lines 93-103: gives the locally isentropic condition $Ds/Dt = 0$.
- Lecture 10, lines 119-129: explains that under isentropic conditions, entropy ceases to be an independent thermodynamic variable and pressure becomes a function of density alone.
- Lecture 9, lines 119-140: then identifies the linearized isentropic pressure-density response through
  $$
  a^2 = \left( \frac{\partial p}{\partial \rho} \right)_s,
  $$
  which is the key lecture support for explaining why a separate energy equation is not needed for closure in this small-disturbance isentropic setting.
# Problem 4: Steady 2D potential flow and Mach-number-dependent PDE type


> [!exercise]
> Preamble. For steady two-dimensional potential flow, Lecture 12 showed the locally frozen principal part can be written as
> 
> $$
> \left(\begin{array}{ll}
> \partial_x & \partial_y
> \end{array}\right) \mathbf{K}_{2 D}\binom{\partial_x}{\partial_y} \phi=0, \quad \mathbf{K}_{2 D}=a_*^2 \mathbf{I}-u_* u_*^T
> $$
> 
> where $\boldsymbol{u}_*=\left(u_*, v_*\right)$ and $M_*:=\left|\boldsymbol{u}_*\right| / a_*$.
> 
> 
> (a) Using the rank-one form, construct two orthonormal eigenvectors: one parallel to $u_*$ and one perpendicular to $\boldsymbol{u}_*$. State them explicitly.
> 
> (b) Compute the two eigenvalues of $\mathbf{K}_{2 D}$ and express them in terms of $a_*$ and $\left|u_*\right|$ (or in terms of $a$, and $M_4$ ).
> 
> (c) Use your eigenvalues to classify the PDE type for: $M_0<1, M_0=1$, and $M_0>1$. For each case, write the corresponding canonical principal part in $\left(\xi^{\prime}, \zeta^{\prime}\right)$ coordinates (up to an overall nonzero scaling).
> 
> (d) (Sketch) In the hyperbolic case $M_4>1$, sketch the two characteristic families in the $\left(\xi^{\prime}, \zeta^{\prime}\right)$ plane and indicate which directions correspond to "information propagation" in the steady spatial problem.


##### problem 4.a
- Lecture 12, lines 151-201: gives the steady 2D frozen principal part, defines the matrix $\mathbf{K}_{2D}$, and rewrites it in the rank-one form
  $$
  \mathbf{K}_{2D}=a_*^2 \mathbf{I}-\boldsymbol{u}_* \boldsymbol{u}_*^T,
  $$
  which is the starting point for constructing the parallel and perpendicular eigenvectors.
- Lecture 12, lines 203-241: shows directly that $\boldsymbol{u}_*$ is the parallel eigenvector direction and any $\boldsymbol{v}_\perp$ with $\boldsymbol{u}_*^T \boldsymbol{v}_\perp = 0$ is the perpendicular eigenvector direction.

##### problem 4.b

- Lecture 12, lines 203-259: derives the eigenvalues of $\mathbf{K}_{2D}$ from the rank-one structure and rewrites them in terms of both $a_*$, $|\boldsymbol{u}_*|$, and $M_*$.
- Lecture 12, lines 243-259 are the most direct lines for the final eigenvalue formulas.

##### problem 4.c

- Lecture 12, lines 243-289: uses the eigenvalues to classify the steady 2D potential equation as elliptic, parabolic, or hyperbolic according to whether $M_*<1$, $M_*=1$, or $M_*>1$.
- Lecture 11, lines 345-390: gives the general diagonalization procedure into canonical coordinates $(\xi',\zeta')$ and shows that the principal part becomes
  $$
  \lambda_1 \phi_{\xi'\xi'} + \lambda_2 \phi_{\zeta'\zeta'}.
  $$
- Lecture 11, lines 396-404: gives the canonical hyperbolic form.
- Lecture 11, lines 507-516: gives the canonical elliptic form.
- Lecture 11, lines 532-542: gives the canonical parabolic form.

##### problem 4.d

- Lecture 11, lines 396-475: develops the hyperbolic canonical form, factors the operator, and identifies the two characteristic families
  $$
  \xi' + \zeta' = \text{const}, \qquad \xi' - \zeta' = \text{const}.
  $$
- Lecture 11, lines 468-475: explains the interpretation of those characteristic curves as directions along which disturbances propagate.
- Lecture 12, lines 282-289: translates that generic hyperbolic interpretation back to steady supersonic potential flow, emphasizing that information propagates spatially along characteristics and that upstream regions cannot feel downstream disturbances.
# Problem 5: Synthesis and interpretation



> [!exercise]
> Instructions. Answer each prompt in 3-5 sentences. Prioritize clarity over length.
> (a) In the incompressible limit, what happens to the steady $2 D$ potential equation, and how should this be interpreted as a special case of the $M_*<1$ regime?
> (b) Why is the unsteady 1D compressible potential equation always hyperbolic? Give a physical interpretation.
> 


##### problem 5.a
- Lecture 12, lines 263-280: classifies the steady 2D potential equation for $M_*<1$ as elliptic and then states that, in the incompressible limit $M_* \to 0$, the equation reduces to Laplace's equation
  $$
  \phi_{xx} + \phi_{yy} = 0.
  $$
- Lecture 12, lines 265-289: explains how the incompressible limit fits into the broader subsonic/elliptic regime and how that affects the interpretation of information propagation and boundary data.
- Lecture 11, lines 507-516: gives the generic interpretation of elliptic PDEs, which is useful for explaining why the incompressible limit should be viewed as a special case of the $M_*<1$ regime rather than as a completely separate phenomenon.

##### problem 5.b

- Lecture 12, lines 37-45: gives the unsteady 1D frozen compressible potential equation.
- Lecture 12, lines 76-131: computes the eigenvalues of the principal coefficient matrix and shows that one is always positive and the other always negative, so the equation is always hyperbolic.
- Lecture 12, lines 133-149: gives the physical interpretation in terms of two traveling-wave families and finite-speed propagation at speeds $u_* \pm a_*$.
- Lecture 11, lines 396-475: provides the generic hyperbolic interpretation in terms of characteristic families and directional propagation, which supports the conceptual explanation requested in the problem.
