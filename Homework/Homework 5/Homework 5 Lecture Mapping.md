


# Problem 1: Centered expansion fan and simple-wave structure

_( 65 points, plus 4 possible extra credit)_

> [!exercise]
> We consider steady, inviscid, supersonic flow undergoing a turning through a corner located at the origin. The upstream flow is uniform, with Mach number $M_1>1$, velocity magnitude $V_1$, and flow angle $\theta_1=0$. The wall turns the flow through a negative angle $\theta_2<0$, generating an expansion.
> 
> 
> 
> 
> 
> ![[Pasted image 20260509005506.png|500]]
> 
> 
> 
> 
> **(a) Characteristic structure**
> 
> Sketch the characteristic families ( $C_{+}$and $C_{-}$) in the following regions:
> (i) upstream of the corner,
> (ii) within the expansion fan,
> (iii) downstream of the fan.
> 
> Clearly indicate which characteristics are straight and which are curved, and explain why.
> 
> 
> **(b) Invariant structure and physical interpretation**
> 
> Using your sketch, argue which characteristic invariant is constant throughout the expansion region.
> 
> Explain:
> (i) why this invariant remains constant globally,
> (ii) what this implies about how the flow variables must vary within the fan.
> 
> 
> **(c) Solution strategy**
> 
> Based on your reasoning above, explain how the flow can be solved within the expansion region.
> 
> Your answer should:
> 
> 
> - describe the role of the constant invariant,
> - identify the independent variable governing the solution,
> - outline the steps needed to compute the flow state.
> 
> You may reference the algorithm provided in the lecture notes.
> 
> 
> 
> **(d) Numerical solution**
> 
> Using the procedure described above, compute the flow state within the expansion fan for
> 
> $$
> M_1=2.4, \quad T_1=300 K, \quad \theta_2=-12^{\circ} .
> $$
> 
> 
> For this computation, you may assume a calorically perfect gas with $\gamma=1.4$ and $R= 287 \mathrm{~J} /(\mathrm{kgK})$. You should choose a consistent normalization for the upstream state (e.g., specify $a_1$ or $T_1$ ) and use the fact that the flow is isentropic within the expansion fan to relate velocity and sound speed through the fan.
> 
> Plot the following as functions of the turning angle:
> 
> $$
> M(\theta), \quad V(\theta), \quad a(\theta) .
> $$
> 
> 
> 
> **(e) Characteristic-based visualization**
> 
> Create an accurate plot for the solution you just obtained (i.e., use code, don't just sketch it) that includes:
> - the wall,
> - representative $C_{+}$and $C_{-}$characteristic families,
> - characteristics upstream, within, and downstream of the fan,
> - one characteristic that originates upstream, propagates through the fan, and continues downstream.
> 
> Clearly distinguish between straight and curved segments.
> 
> 
> **(f) Bonus: flow evolution along a characteristic**
> 
> Color the traced characteristic from part (e) according to the magnitude of the velocity along the curve.
> 
> 




##### problem 1.a

- **Lecture 16, lines 282-286, eq. (1.25):** This is the basic characteristic definition you need for the sketch:
  $$
  C_{+}: \frac{dy}{dx}=\tan(\theta-\mu), \qquad C_{-}: \frac{dy}{dx}=\tan(\theta+\mu).
  $$
  Every region in the sketch should be drawn from these two local directions.

- **Lecture 16, lines 310-314:** These lines explain why the characteristic directions change in nonuniform supersonic flow. The slopes depend on the local flow angle $\theta$ and the local Mach angle $\mu=\sin^{-1}(1/M)$, so they are fixed only in uniform regions.

- **Lecture 16, lines 1032 and 1044-1060:** This is the direct source for the upstream, fan, and downstream characteristic structure. The upstream and downstream regions are uniform, so both characteristic families are straight and parallel there. The $C_{+}$characteristics pass through the fan, curve while the state changes, and become straight again after the fan.

- **Lecture 16, lines 1064-1068:** This is the direct source for the centered fan rays. The expansion fan itself is formed by the $C_{-}$family, whose rays emanate from the corner and are bounded by the first ray at direction $\theta_1+\mu_1$ and the last ray at direction $\theta_2+\mu_2$.


##### problem 1.b

- **Lecture 16, lines 681-722, especially lines 711-722:** These lines derive the invariant form of the compatibility relations. They show that the characteristic ODEs can be written as
  $$
  \frac{d}{d\ell_{\pm}}\left(\theta \pm v(V)\right)=0,
  $$
  so a particular combination of turning angle and Prandtl-Meyer variable is conserved along each characteristic family.

- **Lecture 16, lines 796-801, eq. (3.9):** This is the clean invariant statement to quote:
  $$
  \theta+v(M)=\text{constant along } C_{+}, \qquad
  \theta-v(M)=\text{constant along } C_{-}.
  $$
  Use this to identify which invariant is available from each family.

- **Lecture 16, lines 1062 and 1072-1091:** This is the key centered-fan simplification. Since all $C_{+}$characteristics originate in the same upstream uniform state, their $I_{+}$ values are not merely constant along individual curves; they are the same across the whole fan. Therefore
  $$
  \theta+v(M)=I
  $$
  holds globally throughout the expansion region.

- **Lecture 16, lines 1100-1110:** These lines explain the physical interpretation. The $C_{-}$rays still carry their own invariant values, but those values vary from ray to ray. The global $C_{+}$invariant collapses the problem to a one-parameter simple-wave structure, so $M$ and $\theta$ cannot vary independently inside the fan.


##### problem 1.c

- **Lecture 16, lines 1120-1148, eqs. (4.1)-(4.2):** This is the starting point for the solution strategy. The upstream state fixes
  $$
  I=\theta_1+v(M_1),
  $$
  and the fan satisfies
  $$
  \theta+v(M)=\theta_1+v(M_1).
  $$
  This is the constant-invariant relation that replaces a full two-family marching solve.

- **Lecture 16, lines 724-789, especially eq. (3.8):** These lines define the Prandtl-Meyer function
  $$
  v(M)=\sqrt{\frac{\gamma+1}{\gamma-1}}\tan^{-1}\!\left(\sqrt{\frac{\gamma-1}{\gamma+1}(M^2-1)}\right)-\tan^{-1}\!\left(\sqrt{M^2-1}\right).
  $$
  You need this formula because the computational solution is obtained by evaluating and inverting $v(M)$.

- **Lecture 16, lines 1208-1242, eqs. (4.5)-(4.6):** This is the lecture algorithm the problem explicitly points toward. Select a value of $\theta$ in the fan, solve
  $$
  v(M)=v(M_1)-(\theta-\theta_1),
  $$
  compute $\mu=\sin^{-1}(1/M)$, and assign that state to the $C_{-}$ray with direction
  $$
  \alpha=\theta+\mu.
  $$

- **Lecture 16, lines 734-765 and 953-959:** These lines give the energy/Bernoulli relation needed to recover sound speed and velocity magnitude after finding $M$. For a calorically perfect gas,
  $$
  a^2\left(1+\frac{\gamma-1}{2}M^2\right)=\text{constant},
  $$
  and then $V=aM$.


##### problem 1.d

- **Lecture 16, lines 784-789, eq. (3.8):** Use this formula to compute $v(M_1)$ for $M_1=2.4$ and to invert for each interior Mach number.

- **Lecture 16, lines 1152-1188, eqs. (4.3)-(4.4):** These lines give the downstream relation. With $\theta_1=0$ and $\theta_2=-12^\circ$, the positive turning magnitude is $\delta=12^\circ$, and the downstream Mach number satisfies
  $$
  v(M_2)=v(M_1)+\delta.
  $$

- **Lecture 16, lines 1208-1217, eq. (4.5):** These are the lines to use for the plotted interior states. Sweep $\theta$ from $0$ to $-12^\circ$ and solve
  $$
  v(M(\theta))=v(M_1)-(\theta-\theta_1).
  $$
  This gives the data for the $M(\theta)$ plot.

- **Lecture 16, lines 734-765 and 953-959:** These are the thermodynamic reconstruction lines. With $T_1=300\ \mathrm{K}$, $\gamma=1.4$, and $R=287\ \mathrm{J/(kgK)}$, compute $a_1=\sqrt{\gamma R T_1}$, preserve the stagnation value of $a^2(1+(\gamma-1)M^2/2)$, then compute $a(\theta)$ and $V(\theta)=M(\theta)a(\theta)$.


##### problem 1.e

- **Lecture 16, lines 282-286 and 302-306:** These lines provide the plotting slopes for both characteristic families:
  $$
  C_{+}: \tan(\theta-\mu), \qquad C_{-}: \tan(\theta+\mu).
  $$
  Use the local numerical values of $\theta$ and $\mu$ from part (d), not one fixed freestream Mach angle.

- **Lecture 16, line 1032:** This figure caption is the best single guide for what the visualization must contain: straight $C_{-}$characteristics upstream and downstream, $C_{-}$rays inside the fan, and $C_{+}$characteristics that are straight upstream, curve through the fan, and straighten downstream.

- **Lecture 16, lines 1052-1068:** These lines explain which plotted segments should be straight and which should be curved. Uniform regions produce straight, parallel characteristics; inside the fan the changing state bends the $C_{+}$family, while the centered $C_{-}$family appears as straight rays from the corner.

- **Lecture 16, lines 1218-1238, eq. (4.6):** These lines give the construction of the fan rays:
  $$
  \alpha=\theta+\mu, \qquad y=x\tan(\alpha).
  $$
  This is the most direct lecture source for generating the representative $C_{-}$fan characteristics accurately in code.

- **Lecture 16, lines 1058-1060:** These lines support the traced characteristic requested in the problem. A $C_{+}$characteristic that originates upstream passes through the fan, changes slope continuously as $\theta$ and $M$ change, and exits as a straight downstream characteristic with slope $\tan(\theta_2-\mu_2)$.


##### problem 1.f

- **Lecture 16, lines 1208-1242:** These lines say that each ray in the fan corresponds to a unique flow state. For coloring a traced characteristic by velocity, use the state associated with the local fan ray it crosses.

- **Lecture 16, lines 734-765 and 953-959:** These lines provide the actual velocity magnitude reconstruction. Once the local Mach number has been obtained from the Prandtl-Meyer relation, compute $a(M)$ from the isentropic energy relation and then color the curve by $V(M)=a(M)M$.


# Problem 2: Compression, smoothness, and shock formation ( 35 points)




> [!exercise]
> 
> We now consider compressive turning, $\theta_2>\theta_1$, and examine how the characteristic structure differs from the expansion case.
> 
> Figure 1 shows a sharp corner that turns the flow inward at a point, while Fig. 2 shows a smooth wall that gradually compresses the flow. In this problem, you will compare how compression develops in these two settings.
> 
> 
> **(a) Corner compression and immediate breakdown**
> Consider the sharp-corner compression shown in Fig. 1.
> 
> 
> 
> ![[Pasted image 20260509025815.png]]
> 
> 
> (i) Sketch the characteristic families that would arise if one attempted to construct a smooth centered compression analogous to the centered expansion fan.
> 
> 
> (ii) Based on your sketch, explain why this smooth construction breaks down. Your answer should explicitly address what happens to neighboring characteristics and what this implies about the flow state at points where they intersect.
> 
> 
> (iii) What physical structure replaces the invalid smooth solution? Briefly explain your reasoning.
> 
> 
> 
> 
> 
> **(b) Smooth compression and delayed breakdown**
> 
> Now consider the smooth compression geometry shown in Fig. 2.
> (i) Sketch the characteristic families for the smooth compression region. Your sketch should distinguish the family that carries the wall-imposed compression from the family that originates in the upstream uniform flow.
> 
> 
> (ii) Explain why a locally smooth compression can exist in this case, even though the sharpcorner compression fails. Your answer should reference the fact that the turning is distributed over a finite region rather than imposed at a single point.
> 
> 
> (iii) Is this smooth compression region a fully general two-family characteristic marching problem, or does it still have a degenerate/simple-wave structure? Explain. In particular, discuss what happens to the invariant carried by the characteristic family that originates in the upstream uniform flow.
> 
> 
> (iv) Explain why smooth compression waves may nevertheless eventually lead to shock formation. Your answer should describe the role of characteristic convergence and intersection.
> 
> If part of the flow is compressed smoothly while another part undergoes a shock, what qualitative differences would you expect in the downstream states of these regions? Briefly comment on how such differences might affect how the flow can (or cannot) recombine downstream.
> 




##### problem 2.a

- **Lecture 16, lines 1044-1068:** Use these lines as the expansion template, then reverse the sign of the turning to reason about a centered compression attempt. In the expansion case, the $C_{-}$rays spread from a convex corner. For a sharp compression corner, the analogous smooth construction would make the relevant characteristics crowd together rather than spread apart.

- **Lecture 16, lines 282-286 and 310-325:** These lines explain why neighboring characteristics change their directions as the state changes. In compression, the flow is being turned inward and decelerated relative to the expansion case, so the characteristic geometry tends toward convergence. This is the mathematical basis for sketching neighboring compression characteristics as intersecting rather than fanning apart.

- **Lecture 16, lines 668-677:** These lines state that a smooth solution point is determined by information arriving along characteristic curves. Once neighboring characteristics from the same attempted centered compression overlap or cross, the smooth construction tries to assign incompatible states to the same physical point, so the single-valued smooth solution has broken down.

- **Lecture 16, lines 1012 and Lecture 8, lines 99-137:** These are the smooth-flow limitation lines. Lecture 16 says the characteristic method applies to smooth, isentropic regions and needs additional relations in the presence of shocks. Lecture 8 explains why conservative/integral form is required once discontinuities appear.

- **Lecture 15, lines 29-39 and 41-145, especially lines 134-145:** These lines are the lecture source for what replaces the invalid smooth compression solution: a shock discontinuity governed by jump conditions. The shock separates smooth regions, and the jump conditions determine the downstream state from the upstream state and shock orientation.

- **Lecture 15, lines 224-226:** This is the closest lecture comparison to a two-dimensional compression corner. It states that in the wedge problem, the shock produces a sudden change in flow direction and thermodynamic state, with the shock angle determined by the upstream Mach number, shock angle, and flow deflection angle.


##### problem 2.b

- **Lecture 16, lines 1023-1025:** These lines explicitly distinguish the centered fan from more general smooth-turning flows. They say that a continuously turning boundary still adjusts through characteristic propagation, but the centered-fan simplifications no longer apply in the same closed-form way.

- **Lecture 16, lines 843-861 and 963-987:** These lines give the general smooth characteristic-marching picture. A known curve or boundary generates new solution points by intersecting characteristics, applying invariants, and repeating. This is the correct lecture background for a smooth wall that distributes the compression over a finite region.

- **Lecture 16, lines 1062 and 1079-1098:** These lines explain the degeneracy caused by one family originating from an upstream uniform region. The same idea is needed for part (b)(iii): the family coming from upstream carries the same invariant throughout the smooth compression region, so the flow still has simple-wave character rather than being a fully general two-family marching problem.

- **Lecture 16, lines 1100-1110:** These lines explain how the other family supplies the variation across the simple wave. For the smooth compression case, the wall-imposed family changes from one characteristic to the next, while the upstream-originating family keeps its invariant fixed.

- **Lecture 16, lines 897-908 and 1008-1012:** These lines are the best lecture source for delayed breakdown. The local construction assumes characteristic directions remain well behaved between neighboring points. If the compression causes characteristics to converge strongly enough that they intersect, the smooth isentropic characteristic description fails and shock/discontinuity relations are required.

- **Lecture 15, lines 29-39 and Lecture 9, lines 18-22 and 51-55:** Use these lines for the downstream-state comparison. Smooth compression can be treated as isentropic within the ideal smooth-flow model, while a shock is an irreversible discontinuity that changes the thermodynamic state. Therefore a smoothly compressed region and a shocked region generally do not emerge with matching entropy, pressure, density, and velocity, which makes downstream recombination nontrivial.
