

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




##### problem 1b





##### problem 1c





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














































