
# Problem 1: Wavy-wall solutions and PDE structure



> [!exercise]
> (30 points)
> We consider the small-disturbance compressible potential equation
> 
> $$
> \left(1-M_{\infty}^2\right) \phi_{x x}+\phi_{y y}=0, \quad \phi_y(x, 0)=U_{\infty} f^{\prime}(x)
> $$
> 
> 
> Let
> 
> $$
> f(x)=\sin (x)+\sin (3 x)+\sin (6 x)
> $$
> 
> **(a) Solution construction**
> 
> [8 pts]
> 
> Using results derived in the lecture notes, write the form of the solution $\phi(x, y)$ for:
> **(i) subsonic flow ( $M_{\infty}<1$ ),**
> 
> [4 pts]
> **(ii) supersonic flow $\left(M_{\infty}>1\right)$.**
> 
> [4 pts]
> **(b) Computational exploration**
> 
> [8 pts]
> 
> Using linear superposition, construct $\phi(x, y)$ for both subsonic and supersonic cases. Generate contour plots of $\phi(x, y)$ over the same $(x, y)$ domain for both cases. Consider: $M_{\text {sub }}= 0.6, M_{\text {sup }}=2.0, U_{\text {inf }}=1.0$.
> **(c) Structure and interpretation**
> 
> [14 pts]
> 
> Answer the following. Your answer should include explanations using the plots from (b), the mathematical expression for the solution derived in class, and (where appropriate) your knowledge about how PDE type informs the result.
> (i) How does the influence of the wall geometry change with distance from the wall in the subsonic case? Which features persist and which diminish?
> 
> [4 pts]
> (ii) In the supersonic case, does the disturbance fill the domain or organize along specific directions? Describe these directions.
> 
> [4 pts]
> (iii) Choose a set of heights $\left\{y_1, y_2, y_3\right\}$ representative of spanning from near-wall to far-field. At each of these heights, compute
> 
> $$
> \operatorname{Contribution}_k(y)=\frac{\left\|\phi_k(x, y)\right\|}{\left\|\phi_{\text {total }}(x, y)\right\|}
> $$
> 
> 
> In this expression, $\|\cdot\|$ denotes the standard vector 2-norm associated with the following vector: the norm $\|f(x, y)\|$ comes from evaluating, at the given $y$ location, the vector $\boldsymbol{f}=\left[f\left(x_1, y\right), f\left(x_2, y\right), \ldots, f\left(x_n, y\right)\right]$ where $\left\{x_1, \ldots, x_n\right\}$ denote the points use to represent the domain in the horizontal direction. $\|f(x, y)\|$ is then the standard vector 2-norm of the vector $f$.
> 
> Using these results, describe which wavenumber dominates at each height and how this dominance changes with increasing $y$. Explain your observations using the mathematical form of the solution.
> [6 pts]
> 
> 
> 





# Problem 2: Pressure coefficient and drag




> [!exercise]
> (25 points)
> We now examine the drag induced by a small-amplitude wall $(y=\varepsilon f(x))$.
> 
> **(a) Drag expression**
> 
> [5 pts]
> 
> Starting from the pressure drag per unit span
> 
> $$
> D=\int_{\text {wall }}\left(p-p_{\infty}\right) n_x d s
> $$
> 
> show that, up to an overall constant prefactor, the drag may be written as
> 
> $$
> D \sim \int_{\text {wall }} C_p(x, f(x))\left(-f^{\prime}(x)\right) d x
> $$
> 
> **(b) Order-of-magnitude reasoning**
> 
> [5 pts]
> 
> Explain why it is sufficient to approximate
> 
> $$
> C_p(x, f(x))=C_p(x, 0)+O(\varepsilon)
> $$
> 
> and why higher-order corrections are not needed for the drag at leading order.
> 
> **(c) Subsonic case**
> 
> [5 pts]
> 
> Argue as to whether the drag is zero or nonzero in the subsonic case, using the known form of the analytical solution.
> 
> **(d) Supersonic case**
> 
> [5 pts]
> 
> Argue as to whether the drag is zero or nonzero in the supersonic case, using the known form of the analytical solution.
> 
> **(e) Interpretation**
> 
> [5 pts]
> 
> In 3-5 sentences, explain why the type of the governing equation (elliptic vs. hyperbolic) determines whether the drag is zero or nonzero.




# Problem 3: Cone flow - modeling structure



> [!exercise]
> (20 points)
> We now turn to supersonic flow past a cone. Your explanation to each question should be 3-6 sentences, and use physical and mathematical justifications as appropriate.
> 
> 
> **(a) Problem decomposition**
> 
> [4 pts]
> 
> Explain why the flow must be divided into: an upstream region, a shock surface, a downstream region.
> Why are the non-conservative form of the differential equations not valid at the shock? In what sense are the conservative form of the equations valid, and which form of the governing equations used to derive the jump conditions?
> **(b) Wedge vs. cone**
> 
> [4 pts]
> 
> Explain why the wedge problem can be solved algebraically but the cone problem requires solving an ODE downstream of the shock.
> Your explanation should reference the role of geometry and flow dimensionality.
> **(c) Jump conditions**
> 
> [4 pts]
> 
> What information do the jump conditions provide? Why do they not fully determine the downstream flow?
> **(d) Conical similarity**
> 
> [4 pts]
> 
> Explain how conical similarity reduces the governing equations to an ODE in $\theta$.
> **(e) Iterative structure**
> 
> [4 pts]
> 
> Describe the procedure used to determine the shock angle $\theta_s$. Your description should include the role of an initial guess, how the downstream solution is computed, and how the boundary condition at the cone surface is enforced. Your answer may be given as a "pseudo-code" for an algorithm, or as a paragraph summary.


# Problem 4: Supersonic cone flow (computational)




> [!exercise]
> (25 points)
> 
> Consider steady, inviscid, axisymmetric flow of a calorically perfect gas with
> 
> $$
> \gamma=1.4, \quad M_{\infty}=2.5,
> $$
> 
> over a cone with half-angle
> 
> $$
> \theta_c=10^{\circ} .
> $$
> 
> 
> For convenience, choose a nondimensional freestream:
> 
> $$
> R=1, \quad a_{\infty}=1, \quad p_{\infty}=1 .
> $$
> 
> (a) Compute and plot the solution
> 
> [12 pts]
> 
> Develop a code that solves for the downstream flow, using the algorithm you summarized in the prior question.
> Report the computed shock angle $\theta_s$ and plot $u_r(\theta), u_\theta(\theta), p(\theta)$.
> (b) Synthesis
> 
> [6 pts]
> 
> In 2-4 sentences each, answer:
> 
> 
> (i) How does the flow evolve from the shock to the cone surface?
> 
> [2 pts]
> (ii) Why is the cone boundary condition not satisfied immediately behind the shock?
> 
> [2 pts]
> (iii) What role does the ODE play that the jump conditions alone cannot?
> 
> [2 pts]
> (c) Comparison with wavy-wall flow
> 
> [7 pts]
> 
> State 2-4 key distinctions between the supersonic cone-flow problem and the wavy-wall problem studied earlier in this homework. Each distinction should be written in $3-5$ sentences, using both mathematical structure and physical interpretation for justification.


