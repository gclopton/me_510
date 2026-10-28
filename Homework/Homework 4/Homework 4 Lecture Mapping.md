
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




##### problem a.i

- **Lecture 14, lines 190-197, eqs. (1.15)-(1.17):** This is the starting boundary-value problem. It gives the governing PDE
  $$
  \left(1-M_\infty^2\right)\phi_{xx}+\phi_{yy}=0,
  $$
  the wall condition
  $$
  \phi_y(x,0)=U_\infty f'(x),
  $$
  and the far-field condition $\phi\to 0$ as $y\to\infty$. Part (a)(i) starts here.

- **Lecture 14, lines 210-223, eqs. (2.1)-(2.2):** This is the subsonic reduction. The lecture introduces
  $$
  \xi=\sqrt{1-M_\infty^2}\,x
  $$
  and shows that the PDE becomes Laplace's equation
  $$
  \phi_{\xi\xi}+\phi_{yy}=0.
  $$
  You need these lines to justify why the subsonic solution is built from decaying harmonic modes.

- **Lecture 14, lines 232-253, eqs. (2.3)-(2.6):** This rewrites the wall boundary condition in the stretched coordinate:
  $$
  \phi_y(\xi,0)=U_\infty\sqrt{1-M_\infty^2}\,f_\xi(\xi).
  $$
  This step is easy to miss, but it is essential because the boundary forcing is now expressed in $\xi$, not in $x$.

- **Lecture 14, lines 261-275, eqs. (2.7)-(2.8):** This is the Fourier decomposition step. It expands $f(\xi)$ and $f_\xi(\xi)$ into wavenumbers and explicitly says the boundary forcing is a superposition of independent modes. This is the lecture justification for solving one mode at a time and then adding them.

- **Lecture 14, lines 284-358, eqs. (2.9)-(2.16):** This is the single-mode derivation. It applies separation of variables and shows that the decaying subsonic mode has the form
  $$
  \phi_k(\xi,y)=e^{-ky}\left[\alpha_k\cos(k\xi)+\beta_k\sin(k\xi)\right].
  $$
  These lines tell you the structural form of each modal contribution.

- **Lecture 14, lines 368-393, eqs. (2.17)-(2.18):** This is the final result to quote for part (a)(i). Equation (2.18) is the closed-form subsonic solution:
  $$
  \phi(\xi,y)=U_\infty\sqrt{1-M_\infty^2}\sum_{k>0}e^{-ky}\left[a_k\sin(k\xi)-b_k\cos(k\xi)\right].
  $$
  This is the exact lecture result you use when writing the subsonic answer.


##### problem a.ii

- **Lecture 14, lines 190-197, eqs. (1.15)-(1.17):** Same starting point as part (a)(i). The supersonic derivation uses the same PDE and the same wall boundary condition before changing variables.

- **Lecture 14, lines 453-480, eqs. (3.1)-(3.3):** This is the first supersonic step. The lecture defines
  $$
  \mu=\sqrt{M_\infty^2-1},\qquad \eta=\mu y,
  $$
  and reduces the PDE to the wave equation
  $$
  \phi_{\eta\eta}-\phi_{xx}=0.
  $$
  You need these lines to justify a characteristic or traveling-wave solution.

- **Lecture 14, lines 487-519, eqs. (3.4)-(3.7):** This is the characteristic decomposition:
  $$
  \phi(x,y)=F(x+\mu y)+G(x-\mu y).
  $$
  The same passage also gives the causality argument for dropping the $F$ family and retaining only
  $$
  \phi(x,y)=G(x-\mu y).
  $$
  These lines explain why the supersonic solution has only one characteristic family.

- **Lecture 14, lines 524-556, eqs. (3.8)-(3.10):** This is the wall-matching step. The lecture uses the boundary condition to determine $G$ and obtains the final closed-form result
  $$
  \phi(x,y)=-\frac{U_\infty}{\mu}f(x-\mu y).
  $$
  Equation (3.10) is the exact result to quote for part (a)(ii).




##### problem b

- **Subsonic construction:** Use Lecture 14, lines 261-275 for the superposition principle and lines 388-393 for the final summed formula, eq. (2.18). Those are the exact lines that let you build $\phi$ by adding the contributions from the three wall modes.

- **Subsonic implementation detail:** Also keep Lecture 14, lines 232-245 in view. They remind you that the boundary condition and Fourier decomposition are written in the stretched coordinate $\xi$, so when coding the subsonic case you must be careful about where the $\sqrt{1-M_\infty^2}$ factor enters.

- **Supersonic construction:** Use Lecture 14, lines 552-557, eq. (3.10). That one formula is enough to generate the full supersonic field once you substitute $M_{\text{sup}}=2.0$ and $U_\infty=1.0$.

- **Why the two contour plots should differ:** Lecture 14, lines 94-102 classify the subsonic PDE as elliptic, and lines 449-450 state that the supersonic PDE is hyperbolic with disturbances traveling along characteristic directions. Those are the lecture lines behind the qualitative contrast you should expect in the plots.




##### problem c.i

- **Lecture 14, lines 279-280:** This is the first place the lecture states the key structure in words: each imposed wavenumber persists horizontally, while the $y$-dependence determines how the response extends away from the wall. Use these lines when explaining what persists.

- **Lecture 14, lines 342-350, especially line 350:** These lines are the main answer to part (c)(i). They show that the vertical factor is
  $$
  e^{-ky},
  $$
  and explicitly state that larger $k$ decays more rapidly with $y$. This is the lecture basis for saying that short-wavelength features diminish first, while longer-wavelength features persist farther from the wall.

- **Lecture 14, lines 388-393, eq. (2.18):** This is the formula you should point to when discussing the plot mathematically. The factor $e^{-ky}$ is visible directly in the final subsonic solution.

- **Lecture 14, lines 436-441:** This is the summary version. It restates that the vertical dependence is evanescent and that the decay rate is proportional to wavenumber. These lines are useful if you want a compact citation after giving the full explanation.

- **Optional PDE-type support:** Lecture 14, lines 94-102 say the subsonic PDE is elliptic and that disturbances propagate globally. If you want the more abstract version, Lecture 11, lines 516-518 explain that elliptic equations have no real characteristic directions and are globally coupled to boundary data.




##### problem c.ii

- **Lecture 14, lines 449-450:** This is the first direct statement of the answer. It says the supersonic PDE is hyperbolic and that disturbances do not propagate globally but instead travel along characteristic directions.

- **Lecture 14, lines 487-509, eqs. (3.4)-(3.6):** These lines introduce the two characteristic families
  $$
  F(x+\mu y),\qquad G(x-\mu y),
  $$
  or equivalently the characteristic variables
  $$
  s_+=x+\mu y,\qquad s_-=x-\mu y.
  $$
  Use these lines to answer the part of the question asking whether the disturbance fills the domain or organizes along specific directions.

- **Lecture 14, lines 512-519, eq. (3.7):** These lines give the causality argument for keeping only the $G(x-\mu y)$ family. They explain why information propagates away from the wall and downstream rather than from downstream back upstream.

- **Lecture 14, lines 552-560, eq. (3.10) and interpretation:** This is the most concrete citation. The solution
  $$
  \phi(x,y)=-\frac{U_\infty}{\mu}f(x-\mu y)
  $$
  shows that the wall profile is transported along lines
  $$
  x-\mu y=\text{const}.
  $$
  These are the directions you should identify in the plot.

- **Optional PDE-type support:** Lecture 11, lines 464-506 explain the general hyperbolic picture: disturbances propagate along characteristics, and data can only be imposed where characteristics enter the domain.



##### problem c.iii

- **Subsonic formula to use:** Lecture 14, lines 382-393, eqs. (2.17)-(2.18). These are the formulas that split the solution into modal pieces $\phi_k$ and the total sum $\phi=\sum_k\phi_k$.

- **Subsonic mechanism to cite:** Lecture 14, lines 342-350. The lecture states that each mode has the decay factor $e^{-ky}$ and that larger $k$ decays faster. This is the exact reason your norm-based contribution should shift from the higher wavenumbers near the wall toward the lowest wavenumber farther away.

- **Supersonic formula to use:** Lecture 14, lines 552-557, eq. (3.10). The solution is
  $$
  \phi(x,y)=-\frac{U_\infty}{\mu}f(x-\mu y).
  $$
  This is the key contrast with the subsonic case.

- **Supersonic interpretation to cite:** Lecture 14, line 560. The lecture says the wall shape is imprinted into the flow and propagates along characteristic lines. Since there is no factor like $e^{-ky}$ multiplying the modes, the relative modal amplitudes do not systematically decay with height; they are translated in phase instead.

- **Compact contrast statement:** Lecture 14, lines 684-697 summarize the same difference in regime language: subsonic behavior is tied to elliptic structure and cancellation, while supersonic behavior is tied to hyperbolic propagation along characteristics.







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




##### problem 2.a

- **Lecture 14, lines 138-150, eqs. (1.10)-(1.11):** These lines define the pressure coefficient
  $$
  C_p=\frac{p-p_\infty}{\frac12\rho_\infty U_\infty^2}
  $$
  and give the linearized relation
  $$
  C_p=-\frac{2}{U_\infty}\phi_x.
  $$
  You need these lines because part (a) asks you to rewrite the drag in terms of $C_p$, so you must know exactly how $p-p_\infty$ is related to $C_p$.

- **Lecture 14, lines 612-629, eq. (3.14):** This is the geometry step. The lecture parameterizes the wall, writes the unit normal and arclength element, and then simplifies them to
  $$
  \boldsymbol{n}\,ds=\left(-f'(x),1\right)\,dx.
  $$
  These are the exact lines that convert the surface integral over the wall into an $x$-integral involving the wall slope.

- **Lecture 14, lines 632-643, eq. (3.15):** This is the closest lecture match to the statement of part (a). It projects the pressure force onto the streamwise direction and derives
  $$
  D\propto \epsilon\int C_p(x,f(x))\,f'(x)\,dx.
  $$
  This is the exact passage to use for the drag-expression step. If your homework writes the integrand with $-f'(x)$ instead, treat that as a sign-convention issue tied to the chosen normal direction; the relevant lecture geometry is still in lines 618-629.


##### problem 2.b

- **Lecture 14, lines 598-605, eq. (3.13):** This is the main citation for part (b). The lecture expands the pressure coefficient about the reference line $y=0$:
  $$
  C_p(x,f(x))=C_p(x,0)+f(x)C_{p,y}(x,0)+O(\epsilon^2).
  $$
  Since the wall amplitude is small, $f(x)=O(\epsilon)$, these lines are exactly where the order-of-magnitude reasoning comes from.

- **Lecture 14, lines 650-655, eq. (3.16):** These lines substitute the expansion into the drag formula and show that
  $$
  D\propto \epsilon\int C_p(x,0)f'(x)\,dx+O(\epsilon^2).
  $$
  This is the exact lecture passage that answers why higher-order corrections are unnecessary at leading order: once the prefactor $\epsilon$ from the wall amplitude is already present, the next correction contributes only at higher order.

- **Lecture 14, lines 600-608:** These lines provide the surrounding explanation in words: pressure acts on the actual wall $y=f(x)$, but evaluating on $y=0$ is the leading approximation. Use these lines if you want the verbal justification in addition to the equations.


##### problem 2.c

- **Lecture 14, lines 396-429, especially eq. (2.20):** This is the subsonic surface-pressure formula:
  $$
  C_p(x,0)=-2(1-M_\infty^2)\sum_{k>0}k\left[a_k\cos(k\xi(x))+b_k\sin(k\xi(x))\right].
  $$
  These lines tell you the mathematical form of $C_p$ in the subsonic regime.

- **Lecture 14, lines 658-666:** This is the lecture's direct subsonic drag conclusion. It states that in the subsonic case, $C_p(x,0)$ is in phase with the wall shape $f(x)$, so the leading-order drag reduces to
  $$
  \int f(x)f'(x)\,dx=\frac12\int \frac{d}{dx}\left(f(x)^2\right)\,dx=0
  $$
  over one period. These are the exact lines you need to argue that the leading-order subsonic drag is zero.

- **Lecture 14, lines 684-686:** This is the compact interpretation line. It summarizes the subsonic result as cancellation caused by pressure being tied to the wall shape. Use this if you want a short conceptual citation after the algebraic one.


##### problem 2.d

- **Lecture 14, lines 562-589, especially eq. (3.12):** This is the supersonic surface-pressure formula:
  $$
  C_p(x,0)=\frac{2}{\mu}f'(x).
  $$
  This is the key mathematical input for the supersonic drag argument.

- **Lecture 14, lines 668-679, especially eq. (3.17):** This is the lecture's direct supersonic drag conclusion. Substituting the supersonic pressure law into the leading-order drag gives
  $$
  D\propto \int \left(f'(x)\right)^2\,dx>0.
  $$
  These are the exact lines you need to argue that the supersonic drag is nonzero and positive at leading order.

- **Lecture 14, lines 592 and 682:** These lines give the physical interpretation. They say the supersonic pressure is in phase with the wall slope, so the pressure forces no longer cancel over a wavelength. Use them when writing the explanation around the algebra.


##### problem 2.e

- **Lecture 14, lines 94-98:** These lines give the regime classification in the specific wavy-wall setting: subsonic flow is elliptic and disturbances propagate globally, while supersonic flow is hyperbolic and disturbances propagate along characteristic directions. This is the lecture-specific PDE-type framing for part (e).

- **Lecture 14, lines 684-687:** This is the cleanest direct answer to part (e). The lecture explicitly contrasts the two regimes:
  subsonic pressure is tied to the wall shape and cancels in $\int C_pf'\,dx$, while supersonic pressure is tied to the wall slope and yields $\int (f')^2\,dx$ with nonzero drag.

- **Optional abstract support from Lecture 11:** If you want the general PDE-language behind that contrast, use Lecture 11, lines 252-255 and 272-274 for the statement that PDE type is determined by the principal part, Lecture 11, lines 468-506 for the hyperbolic picture of directional propagation along characteristics, and Lecture 11, lines 514-518 for the elliptic picture of global boundary coupling with no real characteristic directions.



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



##### problem 3.a

- **Lecture 15, lines 17-27, §1.1:** These lines give the high-level decomposition into upstream region, shock surface, and downstream region. They are the best first citation for why the flow must be split into three pieces: the upstream state is known, the shock transmits information through conservation laws, and the downstream region is smooth but unknown.

- **Lecture 15, lines 31-39, §1.2:** These lines explain why the differential equations are valid in the upstream and downstream regions but not at the shock. The key sentence is that the shock produces finite jumps over an infinitesimally thin layer, so the differential form is not valid pointwise there, and one must return to the integral conservation laws.

- **Lecture 15, lines 41-43, §1.3:** These lines say explicitly which form of the equations is used to derive the jump conditions: the integral conservation laws applied to a thin control volume straddling the shock.

- **Lecture 15, lines 47-53, §1.3 Control-volume formulation:** These lines specify the assumptions used in deriving the jump conditions: steady, inviscid, adiabatic flow. Use them if you need to explain the physical setting of the jump derivation.

- **Lecture 15, lines 271-282, §2.1:** These lines are the complementary downstream statement. They say that in the smooth region between shock and cone, the governing equations may be used in differential form. This is useful if you want to contrast “integral form at the shock” with “differential form in the smooth downstream region.”


##### problem 3.b

- **Lecture 15, lines 222-235, §1.7:** This is the main answer to the wedge-versus-cone comparison. It explains that in the wedge problem the downstream flow is uniform immediately behind the shock, so the boundary condition is enforced right at the shock and the shock angle follows from an algebraic relation.

- **Lecture 15, lines 228-234, §1.7:** These lines give the cone-side contrast. The downstream cone flow is not uniform; it fills a continuous region between the shock and the cone surface and must adjust smoothly throughout that region. This is the exact reason the cone problem requires a differential system rather than an algebraic closure.

- **Lecture 15, lines 230-234, §1.7:** These lines are the most surgical citation for the key difference: immediately behind the shock, $u_\theta$ is generally not zero, so the cone boundary condition is not automatically satisfied. The flow must evolve from $\theta=\theta_s$ to $\theta=\theta_c$, which is why an ODE is required.

- **Lecture 15, lines 232-234, §1.7:** These lines give the geometry argument the prompt asks for. They explain that axisymmetric cone flow has additional geometric freedom relative to the 2D wedge, so the required turning is distributed throughout the downstream region instead of occurring entirely across the shock.


##### problem 3.c

- **Lecture 15, lines 134-145, eqs. (1.9)-(1.12):** These are the jump conditions themselves:
  $$
  \rho_1u_{n1}=\rho_2u_{n2},\qquad
  p_1+\rho_1u_{n1}^2=p_2+\rho_2u_{n2}^2,
  $$
  $$
  u_{t1}=u_{t2},\qquad
  h_1+\frac12|\boldsymbol{u}_1|^2=h_2+\frac12|\boldsymbol{u}_2|^2.
  $$
  These are the exact lines to cite when answering what information the jump conditions provide.

- **Lecture 15, lines 145-146:** These lines explain the role of the jump conditions: for a given upstream state and a specified shock orientation, they determine the downstream state immediately behind the shock. This is the precise scope of what the jump conditions do determine.

- **Lecture 15, lines 237-241, §1.8:** These lines explain why the jump conditions do not determine the full downstream flow. They only determine the state immediately behind the shock for a given $\theta_s$; the rest of the flow still has to be found in the region $\theta\in[\theta_c,\theta_s]$.

- **Lecture 15, lines 243-257, eqs. (1.18)-(1.19):** These lines give the missing downstream requirement: the flow must satisfy the cone-surface condition
  $$
  u_\theta(\theta_c)=0
  $$
  after evolving through the downstream region. This is the cleanest citation for why the jump conditions alone are insufficient.

- **Lecture 15, lines 726-731 and 737-751, §§2.5-2.6:** These lines make the same point in ODE language: the shock provides the initial state, but the cone surface imposes an additional constraint that the integrated solution must satisfy.


##### problem 3.d

- **Lecture 15, lines 202-220, §1.6:** This is the conceptual introduction to conical similarity. It states the assumption
  $$
  u_r=u_r(\theta),\quad u_\theta=u_\theta(\theta),\quad p=p(\theta),\quad \rho=\rho(\theta)
  $$
  and explains physically that the flow is invariant along rays from the apex. These lines are the best place to start the explanation.

- **Lecture 15, lines 358-370, eqs. (2.8)-(2.9):** These lines apply the assumption in Chapter 2. They say explicitly that all $r$-derivatives vanish:
  $$
  \frac{\partial(\cdot)}{\partial r}=0.
  $$
  This is the mechanical step that converts the PDE system into equations in $\theta$ only.

- **Lecture 15, lines 376-459, eqs. (2.10)-(2.20):** These lines show the reduced continuity and momentum equations after applying conical similarity in spherical coordinates. This is the detailed derivation showing how the original PDEs collapse to $\theta$-dependent relations.

- **Lecture 15, lines 452-462, eqs. (2.18)-(2.20):** These are the cleanest summary equations for the reduced ODE system before thermodynamic elimination. Use these lines if you want the compact result after the derivation.

- **Lecture 15, lines 676-694, eqs. (2.46)-(2.48):** These lines give the final Taylor-Maccoll system:
  $$
  \frac{du_r}{d\theta}=u_\theta,\qquad
  \frac{du_\theta}{d\theta}=\frac{u_ru_\theta^2-a^2(2u_r+u_\theta\cot\theta)}{a^2-u_\theta^2},
  $$
  with
  $$
  a^2=(\gamma-1)\left[h_0-\frac12(u_r^2+u_\theta^2)\right].
  $$
  This is the exact endpoint of the “reduces to an ODE in $\theta$” story.


##### problem 3.e

- **Lecture 15, lines 781-797, Algorithm 1:** This is the best single citation for the iterative structure. It lays out the full procedure: choose a candidate shock angle, compute the post-shock state, integrate the Taylor-Maccoll system, evaluate the residual, and update the bracket until convergence.

- **Lecture 15, lines 801-835, §3.2:** These lines cover the initialization step. For a chosen $\theta_s$, the jump conditions give the downstream post-shock state, and lines 817-823 project that state into the spherical variables used by the Taylor-Maccoll equations.

- **Lecture 15, lines 837-886, §3.3:** These lines explain how the downstream solution is computed: solve the Taylor-Maccoll initial value problem from $\theta=\theta_s$ down to $\theta=\theta_c$, using the post-shock state as the initial condition.

- **Lecture 15, lines 888-910, eqs. (3.1)-(3.2):** These lines define the residual
  $$
  R(\theta_s):=u_\theta(\theta_c)
  $$
  and explain that the correct shock angle is the one for which
  $$
  R(\theta_s)=0.
  $$
  This is the exact lecture statement of how the cone boundary condition is enforced.

- **Lecture 15, lines 919-963, eqs. (3.3)-(3.6):** These lines give the actual root-finding update: bracket the root, use bisection, and stop when either the residual or bracket width is below tolerance. These are the exact lines to cite if you want the algorithm in pseudo-code form.

- **Lecture 15, lines 974-980:** This is the compact summary sentence for the whole procedure. It explicitly says that the shock angle is obtained by combining shock initialization, Taylor-Maccoll integration, and residual evaluation within an iterative root-finding loop.


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




##### problem 4.a

- **Lecture 15, lines 781-797, Algorithm 1:** This is the top-level computational workflow for the entire problem. It tells you exactly what your code must do: choose a candidate shock angle, compute the post-shock state, integrate the Taylor-Maccoll system, evaluate the residual at the cone surface, and iterate until convergence.

- **Lecture 15, lines 737-751, eq. (2.50):** These lines give the initial conditions for the downstream ODE solve at the shock:
  $$
  u_r(\theta_s)=u_{t2},\qquad u_\theta(\theta_s)=-u_{n2}.
  $$
  This is the exact lecture step that converts the post-shock jump-condition output into the variables used by the Taylor-Maccoll system.

- **Lecture 15, lines 676-694, eqs. (2.46)-(2.48):** These are the ODEs you actually integrate:
  $$
  \frac{du_r}{d\theta}=u_\theta,\qquad
  \frac{du_\theta}{d\theta}=\frac{u_ru_\theta^2-a^2(2u_r+u_\theta\cot\theta)}{a^2-u_\theta^2},
  $$
  with
  $$
  a^2=(\gamma-1)\left[h_0-\frac12(u_r^2+u_\theta^2)\right].
  $$
  These are the exact equations needed to build the integrator.

- **Lecture 15, lines 837-886, §3.3:** These lines explain how the ODE solve is posed numerically: it is an initial value problem in $\theta$, integrated from $\theta_s$ down to $\theta_c$, with the right-hand side recomputed from the current state and $a^2$ at each step. Use these lines for the implementation logic and the direction of integration.

- **Lecture 15, lines 888-910, eqs. (3.1)-(3.2):** These lines define the residual
  $$
  R(\theta_s):=u_\theta(\theta_c),
  $$
  and say the correct shock angle is the one satisfying $R(\theta_s)=0$. This is the exact criterion your code must use to decide whether a trial shock angle is acceptable.

- **Lecture 15, lines 919-963, eqs. (3.3)-(3.6):** These lines give the actual root-finding step for $\theta_s$: bracket the root, use bisection, and stop when the residual or bracket width is below tolerance. This is the most surgical lecture citation for the shock-angle computation.


##### problem 4.b.i

- **Lecture 15, lines 726-727, §2.5 Interpretation:** These lines give the broad dynamical picture: the shock provides the initial state, and the cone surface imposes the constraint the solution must satisfy. This is the cleanest big-picture sentence for how the downstream flow evolves.

- **Lecture 15, lines 837-859, §3.3:** These lines explain that once the post-shock state is set at $\theta=\theta_s$, the flow is integrated inward toward the cone surface at $\theta=\theta_c$. This is the direct lecture description of the downstream evolution.

- **Lecture 15, lines 885-886 and 894-910:** These lines explain what you look for at the end of that evolution: whether the integrated solution reaches the cone with $u_\theta(\theta_c)=0$. Use these lines when describing how the flow “adjusts” from the shock to the cone.


##### problem 4.b.ii

- **Lecture 15, lines 226-234, §1.7:** These are the main lines for this question. They explain that unlike the wedge case, the cone shock does not generally produce a downstream state that immediately satisfies the cone-surface boundary condition. In particular, $u_\theta$ is not zero just behind the shock.

- **Lecture 15, lines 753-760, eq. (2.51):** These lines state the actual cone boundary condition:
  $$
  u_\theta(\theta_c)=0.
  $$
  This is the exact mathematical condition that is not automatically met immediately behind the shock.

- **Lecture 15, lines 767-769:** These lines add the key dependence on shock angle: only for particular values of $\theta_s$ does the integrated solution satisfy the cone boundary condition. This is useful if you want to explain why the boundary condition cannot be enforced locally at the shock.


##### problem 4.b.iii

- **Lecture 15, lines 145-146, from Chapter 1:** These lines state what the jump conditions do provide: for a given upstream state and specified shock orientation, they determine the downstream state immediately behind the shock.

- **Lecture 15, lines 243-257, eqs. (1.18)-(1.19):** These lines show what remains after the jump conditions: the downstream flow must be determined throughout the region
  $$
  \theta\in[\theta_c,\theta_s]
  $$
  and must satisfy
  $$
  u_\theta(\theta_c)=0.
  $$
  This is the exact lecture basis for saying the ODE does something the jump conditions alone cannot.

- **Lecture 15, lines 676-694 and 726-727:** These lines show that the Taylor-Maccoll equations provide the evolution law from the post-shock state to the cone surface. That is the role of the ODE: it carries the flow through the downstream region rather than only across the shock.

- **Lecture 15, lines 903-913:** These lines give the root-finding interpretation. The ODE turns the boundary-value problem into a scalar residual problem for $\theta_s$, which is impossible to set up from the jump conditions alone.


##### problem 4.c

- **Distinction 1: shock-plus-ODE problem versus direct boundary-value problem.**
  Use Lecture 15, lines 17-27 and 781-797 for the cone side: the cone problem splits into upstream, shock, and downstream regions, and the solution requires shock initialization plus Taylor-Maccoll integration plus root finding for $\theta_s$. Use Lecture 14, lines 190-197 for the wavy-wall side: the wavy-wall problem is posed directly as a boundary-value problem for a scalar small-disturbance potential equation with a prescribed wall boundary condition and far-field condition.

- **Distinction 2: nonlinear ODE system versus linear scalar PDE.**
  Use Lecture 15, lines 676-694 for the cone side: the downstream flow is governed by the nonlinear Taylor-Maccoll system for $u_r(\theta)$ and $u_\theta(\theta)$, with $a^2$ coupled algebraically through Bernoulli. Use Lecture 14, lines 94-102 for the wavy-wall side: the small-disturbance wavy-wall equation is a linear second-order PDE whose type is determined by the freestream Mach number.

- **Distinction 3: unknown shock angle versus known geometry forcing.**
  Use Lecture 15, lines 765-769 and 888-963 for the cone side: the shock angle $\theta_s$ is not known a priori and must be found iteratively by enforcing $u_\theta(\theta_c)=0$. Use Lecture 14, lines 524-557 for the supersonic wavy-wall side: once the wall shape $f(x)$ is specified, the solution is given explicitly by
  $$
  \phi(x,y)=-\frac{U_\infty}{\mu}f(x-\mu y),
  $$
  so there is no analogous free boundary or outer-geometry parameter to solve for.

- **Distinction 4: continuous downstream adjustment versus wall-imprinted characteristic transport.**
  Use Lecture 15, lines 228-234 and 839-886 for the cone side: the post-shock flow must evolve continuously through the region between shock and cone until it becomes tangent to the cone surface. Use Lecture 14, lines 449-560 for the wavy-wall side: in the supersonic small-disturbance problem, the wall geometry is imprinted into the flow and transported along characteristic lines $x-\mu y=\text{const}$, giving an explicit characteristic solution rather than a nonlinear downstream relaxation problem.


