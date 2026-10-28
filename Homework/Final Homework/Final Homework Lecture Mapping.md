

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




##### problem 1a

**What does this part ask us to evaluate?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 33, end 38 — These lines ask for the Eulerian time derivative $d^E q=\partial_t q^E|_{\boldsymbol{x}}$, but evaluated at the material point labeled $\boldsymbol{x}_0$. The key distinction is that the derivative is still Eulerian, so the spatial point is held fixed during differentiation and the material-point substitution happens afterward.
- **Which lecture lines define $q^L$, $q^E$, and the independent-variable distinction?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 57, end 78 — These lines define Lagrangian and Eulerian field representations and explicitly warn that $q^L(\boldsymbol{x}_0,t)$ and $q^E(\boldsymbol{x},t)$ are not interchangeable functions. This is the main notation guardrail for part (a).
- **Which lecture lines give the flow-map bridge needed to express the result in terms of $q^L$?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 88, end 114 — These lines give $q^L(\boldsymbol{x}_0,t)=q^E(\phi(\boldsymbol{x}_0,t),t)$ and $q^E(\boldsymbol{x},t)=q^L(\phi^{-1}(\boldsymbol{x},t),t)$. For part (a), use the second identity to rewrite $q^E$ in terms of $q^L$, differentiate at fixed $\boldsymbol{x}$, and then evaluate at $\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)$.
- **Which lecture lines explain the “differentiate first, then substitute” rule?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 157, end 175 — These lines explain that Eulerian velocity is obtained by differentiating the motion map at fixed label and only then substituting $\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x},t)$. The same kind of care is needed here, except part (a) reverses the danger: $d^E$ differentiates at fixed $\boldsymbol{x}$, and only afterward should the result be evaluated along $\phi(\boldsymbol{x}_0,t)$.
- **Which lecture lines give a worked chain-rule template to adapt carefully?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 191, end 250 — These lines work through the chain rule for a composed Eulerian field evaluated along a particle path. Part (a) uses the opposite composition direction, $q^E(\boldsymbol{x},t)=q^L(\phi^{-1}(\boldsymbol{x},t),t)$, so this is not copied directly, but it is useful as the class-style model for writing every chain-rule term and held-fixed variable explicitly.
- **Which prior homework gives the closest model for the chain-rule setup?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 1/Homework 1; Flow Descriptions, Transport, and Integral Conservation.md`, start 68, end 76 — Homework 1 Problem 1(d) uses $x=\phi(x_0,t)$, defines $q^L=q^E\circ\phi$, and asks for a careful chain-rule computation with the held-fixed variable stated. It is the closest previous homework template for this notation.

**What definition must be kept explicit?**

- **(Definition) Eulerian derivative $d^E$** — The derivative $\partial_t q^E(\boldsymbol{x},t)$ taken at fixed spatial location $\boldsymbol{x}$. If it is evaluated at a material point, the evaluation is $(d^E q)(\phi(\boldsymbol{x}_0,t),t)$, but the derivative itself was not taken following the material element.




##### problem 1b

**What does this part ask us to express?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 42, end 47 — These lines ask for $d^L q$ at a spatial point $\boldsymbol{x}$ using Eulerian variables $q^E(\boldsymbol{x},t)$ and $\boldsymbol{u}^E(\boldsymbol{x},t)$. The expected result is the Eulerian form of the material derivative.
- **Which lecture lines define the Lagrangian derivative at fixed material label?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 121, end 151 — These lines define the fixed-label time derivative and explain why following a material element naturally means holding $\boldsymbol{x}_0$ fixed. This is the definition of $d^L$ used in part (b).
- **Which lecture lines derive the Eulerian form by chain rule?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 374, end 425 — This is the most directly relevant derivation for a general field $q$. It rewrites $q^L(\boldsymbol{x}_0,t)$ as $q^E(\phi(\boldsymbol{x}_0,t),t)$, differentiates at fixed $\boldsymbol{x}_0$, recognizes the trajectory derivative as velocity, and then evaluates at the Eulerian point.
- **Which lecture lines give the compact final operator?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative.md`, start 448, end 462 — These lines state the result in both representations:
  $$
  \left(\frac{Dq}{Dt}\right)^L(\boldsymbol{x}_0,t)=\partial_t q^L(\boldsymbol{x}_0,t),
  \qquad
  \left(\frac{Dq}{Dt}\right)^E(\boldsymbol{x},t)=\partial_t q^E(\boldsymbol{x},t)+(\boldsymbol{u}^E\cdot\nabla)q^E(\boldsymbol{x},t).
  $$
  This should be the main formula source for the final answer.
- **Which typed-note lines are useful as a compact sanity check?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Typed Notes.md`, start 111, end 164, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Typed Notes.md`, start 182, end 200 — These lines give a shorter version of the material-derivative chain rule and then explain why the convective term appears. Use them as secondary support only; the main notes should control notation if there is any conflict.
- **Which prior homework reinforces the conceptual comparison with part (a)?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 1/Homework 1; Flow Descriptions, Transport, and Integral Conservation.md`, start 34, end 49, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 1/Homework 1; Flow Descriptions, Transport, and Integral Conservation.md`, start 57, end 76 — Homework 1 Problem 1(b) gives the standard chain-rule material derivative, while Problem 1(c)-(d) explains the ambiguity caused by using one unmarked $q(x,t)$. Those lines are useful for the requested 2-3 sentence comparison between $d^E$ and $d^L$.

**What definition must be kept explicit?**

- **(Definition) Lagrangian derivative $d^L$** — The derivative following the same material element. In Eulerian variables, it is not just $\partial_t q^E$; it is $\partial_t q^E+\boldsymbol{u}^E\cdot\nabla q^E$, because the material element samples spatial variation while moving.





##### problem 1c

**What does this part ask us to rewrite?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 51, end 64 — These lines start from Eulerian continuity and ask for a Lagrangian statement in terms of $\rho^L(\boldsymbol{x}_0,t)$ and the motion of the fluid element. The answer should explain why the Eulerian flux/divergence structure no longer appears in the same explicit form.
- **Which lecture lines give the Eulerian continuity equation and the primitive mass equation?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure.md`, start 12, end 26, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure.md`, start 34, end 44 — The first span gives the conservative Eulerian equation $\partial_t\rho+\nabla\cdot(\rho\boldsymbol{u})=0$. The second span rewrites mass conservation as $D\rho/Dt+\rho\nabla\cdot\boldsymbol{u}=0$, which is the local form to translate into Lagrangian variables.
- **Which lecture lines define Lagrangian density and the mass-Jacobian relation?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 3 and 4: Integral Conservation Laws for Compressible Flow/Lecture 3 and 4: Integral Conservation Laws for Compressible Flow.md`, start 51, end 73 — These lines define $\rho^L(\boldsymbol{x}_0,t)=\rho^E(\phi(\boldsymbol{x}_0,t),t)$ and state
  $$
  \rho^E(\phi(\boldsymbol{x}_0,t),t)J_\phi(\boldsymbol{x}_0,t)=\rho_0(\boldsymbol{x}_0),
  \qquad
  \rho^L(\boldsymbol{x}_0,t)=\frac{\rho_0(\boldsymbol{x}_0)}{J_\phi(\boldsymbol{x}_0,t)}.
  $$
  This is the cleanest final Lagrangian mass-conservation statement.
- **Which lecture lines explain how the fluid-element motion enters through $J_\phi$?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 2: Reynolds Transport Theorem/Lecture 2: Reynolds Transport Theorem.md`, start 132, end 138 — These lines give the Jacobian transport identity $\partial_t J_\psi=J_\psi\nabla\cdot\boldsymbol{w}^E$. For a material map, set $\psi=\phi$ and $\boldsymbol{w}^E=\boldsymbol{u}^E$, giving $\partial_t J_\phi=J_\phi(\nabla\cdot\boldsymbol{u}^E)\circ\phi$. This explains why density changes are encoded by material volume change.
- **Which Lecture 2 lines give the cleanest direct route from Eulerian continuity to Lagrangian mass conservation?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 2: Reynolds Transport Theorem/Lecture 2: Reynolds Transport Theorem.md`, start 237, end 261 — These lines show
  $$
  \partial_t(q^LJ_\phi)=J_\phi\left(\partial_t q^E+\nabla\cdot(q^E\boldsymbol{u}^E)\right)
  $$
  evaluated at $\boldsymbol{x}=\phi(\boldsymbol{x}_0,t)$. Setting $q=\rho$ and using Eulerian continuity makes the right-hand side zero immediately, giving $\partial_t(\rho^LJ_\phi)=0$. This is probably the most efficient class-consistent derivation for part (c).
- **Which Lecture 2 lines explain why the boundary-flux term disappears for material motion?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 2: Reynolds Transport Theorem/Lecture 2: Reynolds Transport Theorem.md`, start 290, end 293 — These lines state that when the region moves with the fluid, $\boldsymbol{w}^E=\boldsymbol{u}^E$, the relative boundary flux vanishes. This is useful for explaining why the Lagrangian form follows a material element instead of including an explicit Eulerian flux through the boundary.
- **Which Lecture 8 lines help explain conservative versus particle-following interpretations?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure.md`, start 99, end 137 — These lines are written for momentum and shocks, so they should not be treated as the main mass derivation. They are still useful interpretive support: conservative form has a boundary-flux meaning, while primitive/material form describes smooth particle-following dynamics. That contrast helps explain which Eulerian flux terms are absorbed when rewriting continuity in Lagrangian form.
- **Which prior homework should guide the Jacobian and continuity reasoning?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 1/Homework 1; Flow Descriptions, Transport, and Integral Conservation.md`, start 82, end 110, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 1/Homework 1; Flow Descriptions, Transport, and Integral Conservation.md`, start 241, end 260 — Homework 1 Problem 2 is the Jacobian transport identity and volume-change interpretation; Homework 1 Problem 4 derives the differential continuity equation from mass conservation. Together they give the geometric and conservation-law pieces needed for part (c).

**What definitions must be kept explicit?**

- **(Definition) $J_\phi$** — The Jacobian determinant $J_\phi=\det(\nabla_{\boldsymbol{x}_0}\phi)$, measuring the material volume change of the fluid element labeled by $\boldsymbol{x}_0$.
- **(Definition) Lagrangian mass conservation** — The compact Lagrangian statement is $\partial_t[\rho^L(\boldsymbol{x}_0,t)J_\phi(\boldsymbol{x}_0,t)]=0$, equivalently $\rho^LJ_\phi=\rho_0$. The Eulerian divergence term no longer appears as a separate flux term because the material description follows the same fluid element; compression/expansion is carried by $J_\phi$.

##### problem 1 figure check

**Are there figures we need to inspect or reproduce for Problem 1?**

- **Which relevant lecture/homework folders contain image embeds for this topic?** I checked the relevant Lecture 1, Lecture 2, Lecture 3-4, and Homework 1 files for figure references and Obsidian image embeds. The relevant Lagrangian/Eulerian and continuity passages are text-and-equation based; no source figure appears to be required for Problem 1.
- **What figure would be optional if we wanted one?** A simple schematic of $\boldsymbol{x}_0\mapsto\phi(\boldsymbol{x}_0,t)$, with $q^L(\boldsymbol{x}_0,t)=q^E(\phi(\boldsymbol{x}_0,t),t)$, could help visually, but it would be a new explanatory figure rather than a figure copied from the notes.





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








##### problem 2a

**What does this part ask us to diagonalize?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 95, end 116 - These lines introduce the scalar second-order PDE
  $$
  A\phi_{xx}+2B\phi_{xy}+C\phi_{yy}=0
  $$
  and ask for the principal matrix form using $\boldsymbol{K}=\left[\begin{array}{cc}A&B\\B&C\end{array}\right]$, followed by an orthogonal coordinate transformation that removes the mixed derivative.
- **Which lecture lines explain why only the principal part matters?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 249, end 255, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 270, end 295 - These spans explain the frozen-coefficient principal-part viewpoint used for classifying compressible-flow PDEs. They justify ignoring lower-order terms and focusing on the symmetric coefficient matrix multiplying the second derivatives.
- **Which lecture lines give the exact matrix form for the second-order principal part?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 314, end 343 - This is the direct source for writing
  $$
  \left(\begin{array}{cc}\partial_\xi&\partial_\zeta\end{array}\right)\boldsymbol{K}\binom{\partial_\xi}{\partial_\zeta}\phi,
  \qquad
  \boldsymbol{K}=\left(\begin{array}{cc}A&B\\B&C\end{array}\right).
  $$
  For the final problem, replace $(\xi,\zeta)$ by $(x,y)$ unless we explicitly introduce canonical coordinates.
- **Which lecture lines give the coordinate transformation that removes the cross derivative?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 345, end 392 - These lines define $\boldsymbol{K}=\boldsymbol{V}\boldsymbol{\Lambda}\boldsymbol{V}^T$, set $(\xi',\zeta')^T=\boldsymbol{V}^T(\xi,\zeta)^T$, transform the derivative vector by the chain rule, and arrive at
  $$
  \lambda_1\phi_{\xi'\xi'}+\lambda_2\phi_{\zeta'\zeta'}.
  $$
  This is the main class template for part (a).
- **Which later lecture gives a physical worked example of this same diagonalization?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 12: Frozen Compressible Potential Equation, 1D and 2D Reductions, and Streamfunction Formulation/Lecture 12: Frozen Compressible Potential Equation, 1D and 2D Reductions, and Streamfunction Formulation.md`, start 151, end 261 - Lecture 12 applies the Lecture 11 matrix framework to steady two-dimensional compressible potential flow with
  $$
  \boldsymbol{K}_{2D}=a_*^2\boldsymbol{I}-\boldsymbol{u}_*\boldsymbol{u}_*^T.
  $$
  This is not needed for the generic derivation, but it is a useful physical example of finding eigenvectors, eigenvalues, and canonical coordinates from a symmetric principal matrix.
- **Which prior homework gives the closest worked version?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3B/Homework 3B Solutions.md`, start 183, end 270 - Homework 3B Problem 1(d) carries out the same diagonalization for a concrete matrix, including the derivative-vector transformation and the final diagonal canonical form. Use it to match the written style and avoid inventing a different notation.
- **Which midterm solution is another useful worked precedent?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Midterm/Midterm.md`, start 233, end 329 - Midterm Problem 4 diagonalizes the steady two-dimensional potential-flow matrix, aligns $\xi'$ and $\zeta'$ with the eigenvectors, and writes the canonical principal part. This is a special-case version of part (a) and should be treated as a style/example reference, not as the main derivation.

**What definition must be kept explicit?**

- **(Definition) Principal matrix $\boldsymbol{K}$** - The symmetric matrix encoding the coefficients of the highest-order part of $A\phi_{xx}+2B\phi_{xy}+C\phi_{yy}$. Its eigenvectors set the rotated coordinate directions, and its eigenvalues become the weights on the pure second derivatives after diagonalization.



##### problem 2b

**How do we identify hyperbolicity and the characteristic directions?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 119, end 124 - These lines ask for the condition on $A,B,C$, the hyperbolic canonical form, and the characteristic directions in the original $(x,y)$ coordinates.
- **Which lecture lines state the hyperbolic canonical case?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 394, end 506 - This is the main source for the hyperbolic case. It says hyperbolicity corresponds to $\lambda_1$ and $\lambda_2$ having opposite signs, gives the canonical form $\phi_{\xi'\xi'}-\phi_{\zeta'\zeta'}=0$, factors the operator, introduces $\eta=\xi'+\zeta'$ and $\mu=\xi'-\zeta'$, and explains why the characteristic curves are the lines $\xi'\pm\zeta'=\text{constant}$.
- **Which lecture lines give the contrast with elliptic behavior?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 507, end 516 - These lines are useful for the explanation because they say elliptic equations have no real characteristic directions. This clarifies why the hyperbolic condition is really the condition for real characteristic families.
- **How do we translate the eigenvalue condition into $A,B,C$?** The lecture gives the eigenvalue-sign condition, and the final problem asks for the coefficient condition. Since
  $$
  \det\boldsymbol{K}=AC-B^2,
  $$
  the two eigenvalues have opposite signs exactly when $\det\boldsymbol{K}<0$, which is
  $$
  B^2-AC>0.
  $$
  That is the coefficient form to state in part (b).
- **Which prior homework gives a worked classification example?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3B/Homework 3B Solutions.md`, start 171, end 181 - Homework 3B classifies a concrete PDE as hyperbolic by checking that one eigenvalue is positive and the other is negative. This is a useful sanity check for the sign logic.
- **Which prior homework gives the most direct back-to-original-coordinates formula?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3B/Homework 3B Solutions.md`, start 574, end 726 - This span rescales the diagonal hyperbolic form, factors it, identifies $\xi'\pm\tilde{\zeta}'=\text{constant}$, and then transforms those line families back to the original coordinates. The final formula there,
  $$
  \left[\boldsymbol{V}(\alpha\boldsymbol{e}_1\pm\boldsymbol{e}_2)\right]^T\binom{\xi}{\zeta}=\text{constant},
  $$
  is the closest prior-work template for part (b)(iii). Adapt it to $(x,y)$ and to the scaling chosen from $\lambda_1,\lambda_2$.
- **Which prior homework gives a simple wavy-wall characteristic example in $(x,y)$?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 4/Homework 4.md`, start 82, end 131 - Homework 4 Problem 1(a.ii) factors the supersonic wavy-wall equation and writes the characteristic families as $x\pm\mu y=\text{constant}$ before selecting the downstream-propagating family. This is a useful concrete example for part (b)(iii), especially for recognizing that the characteristic lines in the original variables come from the factored hyperbolic operator.
- **Which physical classification example supports the sign criterion?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 12: Frozen Compressible Potential Equation, 1D and 2D Reductions, and Streamfunction Formulation/Lecture 12: Frozen Compressible Potential Equation, 1D and 2D Reductions, and Streamfunction Formulation.md`, start 263, end 289, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Midterm/Midterm.md`, start 301, end 329 - These lines show the same same-sign/opposite-sign classification in the steady potential-flow setting: subsonic gives elliptic behavior, sonic gives degeneracy, and supersonic gives hyperbolic behavior. They are secondary examples only; Lecture 11 remains the main generic source.

**What definition must be kept explicit?**

- **(Definition) Characteristic directions for the second-order form** - After diagonalizing and scaling the hyperbolic principal part, the characteristic variables are the combinations that factor the operator. In canonical coordinates they are $\xi'\pm\zeta'=\text{constant}$; in original coordinates, the same line families are obtained by applying the inverse coordinate rotation and any hyperbolic rescaling.



##### problem 2c

**How does the first-order system reduce along characteristic curves?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 126, end 148 - These lines introduce the first-order system $\boldsymbol{A}(\boldsymbol{q})\boldsymbol{q}_x+\boldsymbol{B}(\boldsymbol{q})\boldsymbol{q}_y=0$, give the left-eigenvector relation $\boldsymbol{\alpha}^T\boldsymbol{B}=\lambda\boldsymbol{\alpha}^T\boldsymbol{A}$, and ask us to show that along $dy/dx=\lambda$ the PDE system becomes an ODE.
- **Which lecture lines introduce the first-order compressible-flow system?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 23, end 58, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 60, end 96 - These spans derive the steady inviscid compressible equations in primitive variables and write them in the matrix form $\boldsymbol{A}(\boldsymbol{q})\boldsymbol{q}_x+\boldsymbol{B}(\boldsymbol{q})\boldsymbol{q}_y=0$. This is exactly the setting of part (c).
- **Which lecture lines connect first-order systems with the second-order classification idea?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 98, end 119 - These lines explicitly compare the second-order principal matrix $\boldsymbol{K}$ with the first-order system and ask for an analogous representation in which the equations decouple along preferred directions.
- **Which lecture lines show diagonalization and reduction along curves?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 121, end 188 - These lines freeze the local state, diagonalize $\boldsymbol{C}_*=\boldsymbol{A}^{-1}\boldsymbol{B}$, obtain $w_{i,x}+\lambda_i w_{i,y}=0$, and show that along $dy/dx=\lambda_i$ the total derivative satisfies $dw_i/dx=0$. This is the same chain-rule structure required in part (c), though the homework states it using a left eigenvector $\boldsymbol{\alpha}^T$ rather than the lecture's $w_i$ notation.
- **Which lecture lines give the exact left-null-vector derivation used by the final problem?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 100, end 185 - Lecture 17 uses $(t,x)$ instead of the final problem's $(x,y)$, but the algebra is exactly the same. It defines a curve, writes the total derivative, obtains $\boldsymbol{A}\,d\boldsymbol{q}/dt+(\boldsymbol{B}-\lambda\boldsymbol{A})\boldsymbol{q}_x=0$, introduces $\boldsymbol{\alpha}^T(\boldsymbol{B}-\lambda\boldsymbol{A})=\boldsymbol{0}^T$, and premultiplies to get a pure ODE. This is the best source for the final's specific condition $\boldsymbol{\alpha}^T\boldsymbol{B}=\lambda\boldsymbol{\alpha}^T\boldsymbol{A}$.
- **Which lecture lines give the hyperbolicity criterion for first-order systems?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 190, end 200 - These lines state that the system is hyperbolic when the eigenvalues are real and the matrix has a complete set of eigenvectors. They also explain that these real directions are where information propagates.
- **Which lecture lines give the determinant condition for characteristic slopes?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 202, end 212 - This span gives
  $$
  \det(\boldsymbol{B}-\lambda\boldsymbol{A})=0,
  \qquad
  \lambda=\frac{dy}{dx}.
  $$
  It is the determinant version of the final problem's left-eigenvector condition $\boldsymbol{\alpha}^T(\boldsymbol{B}-\lambda\boldsymbol{A})=0$.
- **Which lecture lines explain the physical compressible-flow meaning?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 300, end 325 - These lines state that characteristic directions depend on the local flow state, real characteristic directions exist only for $M>1$ in that compressible-flow example, and the solution at a point depends on information carried from upstream along the characteristic curves.

**What definition must be kept explicit?**

- **(Definition) First-order characteristic slope** - A slope $\lambda=dy/dx$ is characteristic when there is a nonzero left vector $\boldsymbol{\alpha}^T$ satisfying $\boldsymbol{\alpha}^T(\boldsymbol{B}-\lambda\boldsymbol{A})=0$. Multiplying the PDE by $\boldsymbol{\alpha}^T$ gives $\boldsymbol{\alpha}^T\boldsymbol{A}(\boldsymbol{q}_x+\lambda\boldsymbol{q}_y)=0$, and along $dy/dx=\lambda$ this becomes an ODE involving $d\boldsymbol{q}/dx$.



##### problem 2d

**How should the structural comparison table be filled?**

- **Which final-homework lines define the table?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 151, end 165 - These lines ask for a side-by-side comparison of eigenvalues, eigenvectors, hyperbolicity, and characteristic directions for second-order scalar PDEs versus first-order systems.
- **Which lecture lines should control the second-order side of the table?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 345, end 392, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 11: Compressible Potential Flow and PDE Classification/Lecture 11: Compressible Potential Flow and PDE Classification.md`, start 394, end 506 - These spans define the roles of $\lambda_1,\lambda_2$ and $\boldsymbol{V}$ for the scalar second-order equation: eigenvalues weight the pure second derivatives and their signs determine type, while eigenvectors set the canonical coordinate directions. The characteristic directions appear after scaling and factorizing the hyperbolic canonical operator.
- **Which lecture lines should control the first-order side of the table?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 121, end 200, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 202, end 212 - These spans define the first-order role of eigenvalues as slopes $\lambda_i=dy/dx$, eigenvectors as the variables/projections that decouple the system, and hyperbolicity as real eigenvalues with a complete eigenvector set.
- **Which lecture lines clarify the left-eigenvector row of the table?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 165, end 185 - These lines show that the left null vector $\boldsymbol{\alpha}^T$ is not just decorative notation: it selects the linear combination of equations that removes the transverse derivative and leaves the ODE along the characteristic. This should inform the "role of eigenvectors" entry for the first-order-system column.
- **Which lecture lines explicitly compare the two structures?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 98, end 119, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 190, end 197 - These are the best sources for the prose in the table. They say the first-order construction is the analog of the second-order principal-part diagonalization, but for systems the structure comes from diagonalizing coefficient matrices rather than factorizing a scalar second-order operator.
- **Which prior homework gives the best language for eigenvectors as geometric directions?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3B/Homework 3B Solutions.md`, start 492, end 538, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3B/Homework 3B Solutions.md`, start 540, end 572 - These lines explain that $\boldsymbol{K}$ weights second directional derivatives along its eigenvectors. This is useful for the "role of eigenvectors" row on the second-order side.

**What comparison should the solution preserve?**

- **(Definition) Second-order hyperbolicity** - For $A\phi_{xx}+2B\phi_{xy}+C\phi_{yy}=0$, hyperbolicity means $B^2-AC>0$, equivalently the principal matrix has eigenvalues of opposite sign.
- **(Definition) First-order hyperbolicity** - For $\boldsymbol{A}\boldsymbol{q}_x+\boldsymbol{B}\boldsymbol{q}_y=0$, hyperbolicity means the characteristic eigenproblem has real slopes and enough independent eigenvectors/projections to reduce the system along real characteristic curves.



##### problem 2 figure and code check

**Which figures or code could be useful for Problem 2?**

- **Which relevant figure directly shows first-order characteristic information arriving at a point?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 659, end 675 - I inspected Figure 3.1, not just the caption. It shows two upstream points, $\boldsymbol{x}_{P+}$ and $\boldsymbol{x}_{P-}$, with a $+$ characteristic and a $-$ characteristic both pointing into the unknown point $\boldsymbol{x}_P$. This is the clearest visual match for part (c)'s statement that the PDE system reduces along real characteristic curves and that information reaches a point along characteristic families.
- **Which figure shows the characteristic-marching geometry?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 843, end 861 - I inspected Figure 3.2. It shows a known line of points with a $+$ characteristic from $\boldsymbol{x}_A$ and a $-$ characteristic from $\boldsymbol{x}_B$ intersecting at a new $\boldsymbol{x}_P$, then repeats the construction for the next pair of points. This is more computational than Problem 2 requires, but it is useful if we decide to draw a small schematic comparing first-order characteristic directions to second-order characteristic line families.
- **Which figure is related but not central?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 1031, end 1032 - I inspected Figure 4.1. It shows a centered expansion fan from a convex corner with upstream state $(M_1,\theta_1)$, downstream state $(M_2,\theta_2)$, and labeled first/last characteristics $\theta_1+\mu_1$ and $\theta_2+\mu_2$. This is useful as physical context for characteristic families in supersonic flow, but it is too specific for the abstract structural comparison in Problem 2.
- **Is there code used to produce the relevant figures?** I searched the relevant Lecture 11, Lecture 16, and Homework 3B folders for local plotting/code files and found no `.py`, `.ipynb`, MATLAB, Julia, R, image, or local figure-generation files. The figures in Lecture 16 are remote Mathpix image embeds.
- **Which code-like material might still be useful?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans/Lecture 16: Steady 2D Supersonic Flow, Characteristics, and Expansion Fans.md`, start 967, end 983 - This is pseudocode for a characteristic marching procedure, not figure-generation code. It reinforces the computational meaning of characteristic curves, but the solution to Problem 2 should not need to reproduce the algorithm unless we add an optional explanatory sketch.





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


##### problem 3a

**What wave structure needs to be sketched?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 177, end 205 - These lines define the initial shock-tube states, with Region 4 on the left and Region 1 on the right, and ask for an $x$-$t$ sketch showing the expansion fan, contact discontinuity, shock, and all regions.
- **Which lecture lines introduce the canonical shock-tube pattern?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 334, end 352 - These lines say that diaphragm rupture produces a left-going expansion fan, Region 3, a contact surface, Region 2, and a right-going shock. They also identify the expansion fan as a simple-wave region bounded by $C_{-}$ rays satisfying $dx/dt=u-a$.
- **Which figure should guide the basic sketch?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 376, end 378 - I inspected Figure 2.1 directly. It shows the initial diaphragm-separated tube, the physical $t>0$ region ordering, and the corresponding $x$-$t$ diagram. In the figure, the vertical axis is $x$ and the horizontal axis is $t$, so the plotted slopes represent $dx/dt$ directly. The expansion fan opens into negative $x$, the contact is a dashed line moving right, and the shock is a steeper solid line moving farther right.
- **Which lecture lines explain the fan geometry and compression-versus-expansion logic?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 380, end 425 - These lines state that $C_+$ carries the constant invariant through the simple-wave fan, while variation is associated with the $C_-$ family. They also explain that diverging characteristics correspond to an expansion wave and converging characteristics correspond to compression and eventual shock formation. This supports the qualitative shape of the fan and the reason the right-going compression is not drawn as a smooth fan.
- **Which lecture lines explain why the contact and shock appear?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 433, end 456 - These lines explain why a simple expansion is not enough for the full shock-tube solution: compression would make characteristics intersect, so the smooth solution breaks down and a discontinuity is required.
- **Which lecture lines define the contact discontinuity?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 458, end 490 - These lines state the contact conditions $u_2=u_3$ and $p_2=p_3$, the density jump $\rho_2\neq\rho_3$, and the contact speed $dx/dt=u_2=u_3$. This is the source for labeling the contact surface correctly.
- **Which lecture lines define the shock side of the sketch?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 492, end 533 - These lines identify the shock as the discontinuity connecting Region 2 to Region 1, state the Rankine-Hugoniot conditions, and explain that the shock speed $u_s$ is determined as part of the solution.
- **Which figure shows the more complete characteristic picture?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 535, end 553 - I inspected the image embedded at line 553. It overlays the full shock-tube region diagram with red $C_{-}$ characteristics, blue $C_{+}$ characteristics, the expansion fan, the contact, and the shock. This figure is more useful for part (d), but it is also helpful for making the part (a) sketch consistent with the characteristic families.

**What definitions must be kept explicit?**

- **(Definition) Region labels** - Region 4 is the initial high-pressure left state, Region 1 is the initial low-pressure right state, Region 3 is behind the expansion and left of the contact, and Region 2 is behind the shock and right of the contact.
- **(Definition) Contact surface** - A moving discontinuity in density and entropy, with continuous velocity and pressure: $u_2=u_3$ and $p_2=p_3$.
- **(Caution) Axis orientation** - Lecture 17's shock-tube figures put $t$ on the horizontal axis and $x$ on the vertical axis so that the drawn slopes equal $dx/dt$. If we make a conventional plot with $x$ horizontal and $t$ vertical, transpose the visual layout and use slopes $dt/dx=1/(u\pm a)$ for characteristic lines.



##### problem 3b

**What procedure determines the intermediate states?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 209, end 216 - These lines ask for the solution strategy, including the relations used in each region and how the unknown pressure is determined.
- **Which lecture lines set up the known states and unknowns?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 560, end 608 - These lines identify the known initial states $(u_4,p_4,\rho_4)$ and $(u_1,p_1,\rho_1)$, the region ordering, the contact reduction $u_2=u_3=u_*$ and $p_2=p_3=p_*$, and the remaining unknowns.
- **Which lecture lines give the thermodynamic relations for Region 3?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 612, end 686 - These lines derive the isentropic relations
  $$
  \frac{\rho_3}{\rho_4}=\left(\frac{p_*}{p_4}\right)^{1/\gamma},
  \qquad
  \frac{a_3}{a_4}=\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}.
  $$
  They are needed because Region 3 is reached through the isentropic expansion fan.
- **Which lecture lines give the expansion-fan relation for $u_*$?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 698, end 722 - These lines apply the constant $I_+$ invariant between Regions 4 and 3 and give
  $$
  u_*=u_4+\frac{2a_4}{\gamma-1}\left[1-\left(\frac{p_*}{p_4}\right)^{(\gamma-1)/(2\gamma)}\right].
  $$
  This is the left-side relation in the scalar equation for $p_*$.
- **Which lecture lines give the shock relation for $u_*$?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 723, end 747 - These lines use the Rankine-Hugoniot conditions to relate Region 1 to Region 2 and give the second expression for $u_*$ as a function of $p_*$. Equating this with the expansion-fan expression gives the nonlinear scalar equation for $p_*$.
- **Which lecture lines give the remaining state and shock-speed formulas?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 753, end 787 - These lines give $\rho_2$ from the shock relation, $u_s$ from mass conservation across the shock, and Algorithm 1 for computing all uniform states.
- **Which previous homework supports the discontinuity logic?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3A/Homework 3A; Solutions.md`, start 31, end 48, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 3A/Homework 3A; Solutions.md`, start 64, end 82 - Homework 3A explains why a conservative equation must be interpreted through an integral balance at a moving jump and derives the Rankine-Hugoniot condition. This is useful background for why the shock cannot be handled by the smooth characteristic equations alone.
- **Which lecture lines reinforce that shocks require conservative form?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure.md`, start 99, end 137 - These lines explain that conservative form keeps its control-volume meaning at discontinuities, while primitive form relies on smoothness. This supports the use of jump conditions at the shock.

**What definition must be kept explicit?**

- **(Definition) Star state** - The shared pressure and velocity across the contact, $p_*=p_2=p_3$ and $u_*=u_2=u_3$. The scalar unknown $p_*$ is selected by matching the expansion-fan relation from the left to the shock relation from the right.



##### problem 3c

**What is needed to compute and plot $\rho(x)$, $u(x)$, and $p(x)$ at $t=0.01\,\mathrm{s}$?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 220, end 235 - These lines ask for the numerical solution at $t=0.01\,\mathrm{s}$ and plots of $\rho(x)$, $u(x)$, and $p(x)$.
- **Which lecture lines give the state-solving algorithm?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 688, end 787 - This span gives the equations needed to solve for $p_*$, compute $u_*$, compute $\rho_3$ and $a_3$, compute $\rho_2$, and compute $u_s$. These are the constants needed before constructing the piecewise profiles.
- **Which lecture lines give the self-similar expansion-fan solution?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 791, end 887 - These lines define $\xi=x/t$, identify the fan rays as $C_{-}$ characteristics with $\xi=u-a$, use the constant $I_+$ invariant, and derive
  $$
  a(\xi)=\frac{\gamma-1}{\gamma+1}\left(u_4+\frac{2a_4}{\gamma-1}-\xi\right),
  \qquad
  u(\xi)=\xi+a(\xi).
  $$
  They also give the fan boundaries $\xi_{\text{head}}=u_4-a_4$ and $\xi_{\text{tail}}=u_*-a_3$.
- **Which lecture lines give the full piecewise structure?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 888, end 910 - These lines assemble the piecewise solution over Region 4, the fan, Region 3, Region 2, and Region 1. For the final computation, convert the similarity boundaries into positions by multiplying the speeds by $t=0.01\,\mathrm{s}$.
- **Which lecture lines give the thermodynamic conversion for $\rho$ and $p$?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 612, end 676 - These lines give $p=K\rho^\gamma$ and $a^2=\gamma p/\rho$. In the fan, use the Region 4 isentrope to recover $p(\xi)$ and $\rho(\xi)$ from $a(\xi)$; outside the fan, use the uniform states computed in part (b).
- **Which prior homework code is useful as a plotting pattern, even though it is not the same physics problem?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5.md`, start 399, end 480 - This Mathematica code builds tabulated solution data and plots multiple flow variables with `ListLinePlot`. It is not a shock-tube solver, but it is a useful vault-local model for plotting state variables after computing a parameterized compressible-flow solution.

**What definitions must be kept explicit?**

- **(Definition) Similarity variable** - $\xi=x/t$. The expansion fan is self-similar because it originates at $(0,0)$ and each fan ray is a line of constant $\xi$.
- **(Definition) Wave locations at fixed time** - At time $t$, the fan head is at $(u_4-a_4)t$, the fan tail is at $(u_*-a_3)t$, the contact is at $u_*t$, and the shock is at $u_st$.



##### problem 3d

**What is needed to plot the actual characteristic curves in the $x$-$t$ plane?**

- **Which final-homework lines define the task?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Final Homework/Final Homework.md`, start 240, end 248 - These lines ask for a code-generated update of the part (a) sketch showing both characteristic families, the expansion fan, and the shock trajectory.
- **Which lecture lines define the characteristic speeds?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 100, end 162 - These lines derive $dx/dt=\lambda$ and the two characteristic families
  $$
  \frac{dx}{dt}=u\pm a.
  $$
  These are the slopes to use when plotting $C_+$ and $C_-$ characteristics in each region.
- **Which lecture lines give the compatibility/invariant structure behind the curves?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 165, end 230, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 235, end 330 - These lines derive the ODE relations along characteristics and the Riemann invariants $I_{\pm}=u\pm 2a/(\gamma-1)$. They explain what the plotted characteristic families carry.
- **Which lecture lines determine the fan rays to plot?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 346, end 352, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 824, end 887 - These lines say the expansion fan is the $C_{-}$ family, with rays satisfying $\xi=u-a$, bounded by $\xi_{\text{head}}=u_4-a_4$ and $\xi_{\text{tail}}=u_*-a_3$. In code, representative fan characteristics can be plotted as straight rays $x=\xi t$ for $\xi$ between those bounds.
- **Which lecture lines give the contact and shock trajectories?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 482, end 490, and `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 761, end 766 - These lines give the contact speed $dx/dt=u_*$ and the shock speed $u_s=\rho_2u_*/(\rho_2-\rho_1)$. Plot them as straight trajectories $x=u_*t$ and $x=u_st$.
- **Which figure should the code-generated plot resemble?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 535, end 553 - I inspected the embedded image. It shows red $C_{-}$ curves and blue $C_{+}$ curves over the shock-tube regions, with the shock as a solid black line and the contact as a dashed black line. This is the best visual target for part (d).
- **Which lecture lines explain how characteristic plotting generalizes?** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 912, end 988 - These lines describe tracing characteristics through smooth regions, combining invariants at intersections, and supplementing characteristic propagation with contact and shock conditions at discontinuities. Use this as conceptual support if the plot includes curves bending or terminating at the shock/contact.
- **Which prior homework code is a useful template for drawing characteristic families?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5.md`, start 521, end 711, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5.md`, start 734, end 843 - I inspected the code-produced Homework 5 figure at `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/images/Pasted image 20260509095505.png`. The physics is steady 2D expansion, not the unsteady shock tube, so do not copy its formulas. The useful part is the plotting pattern: compute characteristic slopes/curves, draw families with different colors/styles, mark fan boundaries, and optionally color a traced characteristic by a flow quantity.
- **Which prior homework gives the clearest fan-crossing construction?** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5 Lecture Solutions.md`, start 757, end 791, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5 Lecture Solutions.md`, start 793, end 850 - These lines parameterize a centered expansion fan by one family of straight rays and derive an ODE for a characteristic from the other family as it crosses the fan. I inspected the related figures at `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/images/Pasted image 20260509035745.png` and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/images/Pasted image 20260509062659.png`. The formulas are steady 2D formulas and must not be copied directly, but the plotting strategy transfers well to the shock-tube fan after replacing the fan parameter with $\xi=x/t$ and characteristic speeds with $u\pm a$.

**What code/figure caution should we preserve?**

- **(Caution) Lecture 17 figure code** - I found no local code that produced the Lecture 17 shock-tube figures. The Lecture 17 figures are embedded image files, while the only explicit code in the Lecture 17 note is Algorithm 1 for computing uniform states. Any code for Problem 3(d) should therefore be newly written from the Lecture 17 formulas, not copied from a hidden shock-tube plotting script.


##### problem 3 figure and code check

**Which figures and code were inspected for Problem 3?**

- **Lecture 17 Figure 2.1:** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 376, end 378 - The image shows the initial diaphragm-separated tube, the physical $t>0$ wave ordering, and a simplified $x$-$t$ diagram with the expansion fan, contact, and shock. This is the main sketch source for part (a).
- **Lecture 17 full characteristic sketch:** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 535, end 553 - The image shows both characteristic families overlaid on the full shock-tube structure. This is the main visual target for part (d).
- **Lecture 17 Algorithm 1:** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/Lecture 17 Unsteady 1D Compressible Flow.md`, start 769, end 787 - This is pseudocode for computing $p_*$, $u_*$, Region 3, Region 2, and $u_s$. It is directly relevant to parts (b) and (c).
- **Homework 5 plotting code:** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5.md`, start 521, end 711, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5.md`, start 734, end 843 - This code is useful only as a plotting template for characteristic families and colored characteristic segments. It should not be used as the shock-tube physics model.
- **Homework 5 Lecture Solutions fan-crossing figures:** `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5 Lecture Solutions.md`, start 204, end 208, and `/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 5/Homework 5 Lecture Solutions.md`, start 757, end 791 - I inspected both referenced Homework 5 images. They show straight rays from one characteristic family through a centered fan and a curved crossing characteristic from the other family. These are useful visual precedents for Problem 3(d), but only after translating the variables from steady $(x,y)$ flow to unsteady $(x,t)$ flow.
- **Non-relevant image checked:** `/Users/gradyclopton/ObsidianVaults/me_510/Lectures/Lecture 17 Unsteady 1D Compressible Flow/images/Pasted image 20260509025815.png` - I inspected this local image because it is in the Lecture 17 image folder, but it shows steady compressive turning through a sharp corner and a smooth wall. It is not needed for Problem 3.
