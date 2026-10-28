


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
> ![[Pasted image 20260509005802.png]]
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




