


**Instructions:** Show your reasoning clearly and keep your notation consistent. Unless stated otherwise, assume all fields are smooth enough for the manipulations you perform (chain rule, differentiation under the integral sign, divergence theorem, etc.). You may use any results stated in the lecture notes.



# Problem 1: Interpreting the material derivative ( 22 points)

**Preamble:** In this problem, we will temporarily abandon the careful Eulerian-Lagrangian notation and flow-map framework developed in lecture. We do this not because it is recommended, but to examine a commonly used "standard" derivation of the material derivative and to identify where interpretation and hidden assumptions enter.

A typical derivation of the material derivative might start with: Let $q(x, t)$ be a scalar field defined over space and time, and let $x(t)$ denote the trajectory of a moving point satisfying

$$
\dot{x}(t)=u(x(t), t) .
$$


> [!question] (a) Interpreting the objects being differentiated
> 
> 
> [5 pts]
> 
> Answer the following conceptual questions (brief but precise):
> (i) What is the mathematical meaning of the function $q(x, t)$ ? What are its independent variables?
> (ii) What is $x(t)$ ? Is it a spatial coordinate, a material label, or something else?
> (iii) In the composite quantity $q(x(t), t)$ : which variables are independent, which are functions of time, and in what sense is this quantity Eulerian or Lagrangian?






> [!question] (b) The standard derivation
> 
> 
> 
> 
> Using the chain rule, show that
> 
> $$
> \frac{d}{d t} q(x(t), t)=\frac{\partial q}{\partial t}(x(t), t)+\dot{x}(t) \cdot \nabla q(x(t), t),
> $$
> 
> and then, substituting $\dot{x}(t)=u(x(t), t)$, obtain
> 
> $$
> \frac{D q}{D t}=\frac{\partial q}{\partial t}+\boldsymbol{u} \cdot \nabla q .
> $$
> 
> 





> [!Question] (c) Where ambiguity enters
> 
> 
> 
> In 2-4 sentences each:
> (i) Where is it implicitly assumed that the derivative is taken following a material element?
> (ii) Think about the function $q$. Discuss how this use of single function blurs the lines between Eulerian and Lagrangian perspectives, and what ambiguity this introduces in the material derivative derivation.




> [!Question] (d) Resolution using flow maps and representations
> 
> Return to the notational framework developed in our lectures. Let $x=\phi\left(x_0, t\right)$ be the material flow map, and define
> 
> $$
> q^L\left(x_0, t\right):=q^E\left(\phi\left(x_0, t\right), t\right) .
> $$
> (i) Compute $\frac{\partial}{\partial t}\left[q^L\left(x_0, \cdot\right)\right]_{x_0}(t)$, explicitly stating what is held fixed.
> (ii) Rewrite the result entirely in terms of Eulerian quantities $q^E(x, t)$ and $\boldsymbol{u}^E(\boldsymbol{x}, t)$, and show that it agrees with the result from part (b).
> 




# Problem 2: Jacobian transport identity and volume change (18 points)

Let $x=\psi(\xi, t)$ be a smooth invertible domain map with deformation gradient $F=\nabla_{\xi} \psi$ and Jacobian $J=\operatorname{det} F$. Define the domain velocity

$$
\boldsymbol{w}^E(x, t):=\left.\frac{\partial}{\partial t} \psi(\xi, \cdot)\right|_{\xi}(t), \quad x=\psi(\xi, t) .
$$

> [!Question] (a) Prove the Jacobian transport identity
> 
> 
> $$
> \left.\frac{\partial J}{\partial t}(\xi, t)\right|_{\xi}=J(\xi, t) \nabla \cdot x_x w^E(x, t), \quad x=\psi(\xi, t) .
> $$
> 
>
>Hint: You may use Jacobi's formula $\dot{J}=J \operatorname{tr}\left(F^{-1} \dot{F}\right)$, where the dot> denotes $\partial_t$ at fixed $\xi$. 




> [!Question] (b)
> Specialize to the material map $\psi=\phi$ (so $\boldsymbol{w}^E=\boldsymbol{u}^E$ ). Interpret physically what $J_\phi$ represents, and explain what $\nabla \cdot \boldsymbol{u}=0$ implies for $J_\phi$.




> [!question] (c)
> Show: if $\nabla \cdot \boldsymbol{u}=0$ and $J_\phi\left(x_0, 0\right)=1$, then $J_\phi\left(x_0, t\right) \equiv 1$ for all $t$. State the physical meaning.




# Problem 3: Interpreting the Reynolds transport theorem
(26 points)


In this problem, we examine a standard derivation of the Reynolds transport theorem (RTT). The goal is not to re-derive the theorem mechanically, but to identify where interpretive assumptions are made implicitly, how those assumptions are obscured by notation, and how the framework developed in lecture resolves these issues.



> [! ] (a) What is being differentiated?
> 
> 
> Consider the quantity
> 
> $$
> I(t):=\int_{\Omega(t)} q(x, t) d V,
> $$
> 
> where $\Omega(t)$ is a time-dependent region of space and $q(x, t)$ is a scalar field.
> Briefly answer the following:
> 


> [!Question] (i)
> What does $I(t)$ represent physically?


> [!Question] (ii) 
> In principle, what different meanings could the time derivative $\frac{d}{d t} I(t)$ have, depending on what is being compared in time?



> [! ] (b) Diagnosing interpretive and notational jumps in a standard RTT derivation
> 
> 
> 
> 
> A typical derivation of the Reynolds transport theorem is often presented in outline form as follows.
> 
> **Step I.** Consider the quantity
> 
> $$
> I(t):=\int_{\Omega(t)} q(x, t) d V
> $$
> 
> interpreted as "the amount of $q$ contained in the region $\Omega(t)$."
> **Step II**. Over a short time interval $[t, t+\Delta t]$, argue that the change in $I(t)$ consists of:
> - a change due to the explicit time dependence of $q$ within $\Omega(t)$,
> - a change due to fluid carrying $q$ as it enters or leaves through $\partial \Omega(t)$.
> 
> **Step III.** Approximate the amount of $q$ crossing a boundary element $d S$ during $\Delta t$ as
> 
> $$
> q(\boldsymbol{u}-\boldsymbol{w}) \cdot \boldsymbol{n} \Delta t d S
> $$
> 
> where $u$ is the fluid velocity and $w$ is the boundary velocity.
> 
> 
> **Step IV.** Divide by $\Delta t$, take the limit $\Delta t \rightarrow 0$, and combine the contributions to obtain
> 
> $$
> \frac{d}{d t} \int_{\Omega(t)} q d V=\int_{\Omega(t)} \partial_t q d V+\int_{\partial \Omega(t)} q(u-w) \cdot n d S
> $$
> 
> Answer the following questions.




> [!Question] (i)
> (i) Focusing on Step I, explain what interpretation of the time derivative $\frac{d}{d t} \int_{\Omega(t)} q d V$ is being implicitly adopted. What alternative, equally reasonable interpretation of this derivative is not being considered?



> [!Question] (ii)
> In Step II, identify a specific interpretive jump that is required for the argument to proceed. Explain how this interpretive choice is reflected (or not reflected) in the notation used for $q$.
>**Hint:** At this stage, is q still being treated purely as an Eulerian field evaluated at fixed spatial points?



> [!Question] .
> (iii) In Step III, identify what interpretation is required to proceed with the derivation, and where the corresponding notational imprecision. In particular, explain how the expression for the boundary contribution requires $q$ to be interpreted as a quantity attached to material elements, even though it is still written as $q(x, t)$.




> [!Question] .
> (iv) Briefly explain how the careful framework developed in Lecture 2 (distinguishing representations and what is held fixed before differentiating) avoids the ambiguities identified in parts (i)-(iii), without appealing to new physics or different final equations.




> [! ] (c) Comparison with the lecture framework
> 
> 
> Using the Reynolds transport theorem as derived in lecture:


> [!question] (i)
> Explain how the relevant interpretive choices are made before any differentiation occurs.


> [!question] (ii)
> Describe the role of "what is held fixed" in defining the time derivative at the integral level.


> [!question] (iii)
> Specialize the Reynolds transport theorem to the case $\boldsymbol{w}=0$ and compare it to the Eulerian time derivative of an integral over a moving domain. Do the results agree? Why or why not does this make sense?


> [!question] (iv)
> Create an analogy between these two derivatives of integrals and the Eulerian versus material time derivatives in the pointwise setting.



> [!question] (d) Outline of a careful re-derivation
> 
> 
> Outline (but do not fully execute) the steps required to re-derive the Reynolds transport theorem using the framework of Lecture 2. Your outline should make clear:
> - how the integral is parameterized,
> - what is held fixed when differentiating,
> - how boundary flux terms arise.




# Problem 4: Continuity and momentum in integral and differential form (18 points)

Assume inviscid stress so the traction is $t=-p n$. Consider a fixed control volume $\Omega$ (so $w=0$ ).


> [!question] (a)
> Starting from conservation of mass for a material system and using the Reynolds transport theorem, show
> 
> $$
> \frac{d}{d t} \int_{\Omega} \rho d V+\int_{\partial \Omega} \rho \boldsymbol{u} \cdot \boldsymbol{n} d S=0
> $$
> 
> 
> Then use the divergence theorem and the arbitrariness of $\Omega$ to obtain the differential continuity equation
> 
> $$
> \frac{\partial \rho}{\partial t}+\nabla \cdot(\rho u)=0
> $$
> 
> clearly stating any regularity assumptions.




> [!Question] (b)
> Starting from Newton's second law for a material system and using the Reynolds transport theorem, derive the inviscid integral momentum equation:
> 
> $$
> \frac{d}{d t} \int_{\Omega} \rho u d V+\int_{\partial \Omega} \rho u(u \cdot n) d S=-\int_{\partial \Omega} p n d S+\int_{\Omega} \rho f d V
> $$
> 
> 
> Convert to differential form, either in dyadic form $\frac{\partial}{\partial t}(\rho \boldsymbol{u})+\nabla \cdot(\rho \boldsymbol{u} \otimes \boldsymbol{u})+\nabla p=\rho \boldsymbol{f}$ or componentwise as
> 
> $$
> \frac{\partial}{\partial t}\left(\rho u_i\right)+\frac{\partial}{\partial x_j}\left(\rho u_i u_j\right)+\frac{\partial p}{\partial x_i}=\rho f_i .
> $$
> 
> (If you use dyadic notation, you may take $(u \otimes u)_{i j}=u_i u_j$.)





# Problem 5: Energy, enthalpy flux, stagnation properties (16 points)
Consider a fixed control volume $\Omega$, inviscid flow $(t=-p n)$, and allow heat flux $\boldsymbol{q}_h$. Let $E= e+\frac{1}{2}|u|^2+\Phi$.


> [!question] (a)
> Starting from the inviscid integral energy equation, show that the advective and pressurework boundary terms can be grouped as an enthalpy flux:
> 
> $$
> \int_{\partial \Omega}(\rho E+p) \boldsymbol{u} \cdot \boldsymbol{n} d S=\int_{\partial \Omega} \rho\left(h+\frac{1}{2}|\boldsymbol{u}|^2+\Phi\right) \boldsymbol{u} \cdot \boldsymbol{n} d S, \quad h=e+\frac{p}{\rho}
> $$
> 
> 


> [!question] (b)
> Using the reference relations for a calorically perfect ideal gas, show that
> 
> $$
> h_0:=h+\frac{1}{2}|u|^2=c_p T_0 \quad \Rightarrow \quad T_0=T+\frac{|u|^2}{2 c_p}
> $$
> 
> 
> 



> [!question] (c)
> (c) Consider a fixed control volume whose side boundary is everywhere tangent to the velocity field (i.e. a "streamtube" control volume) and which intersects the flow at one inlet crosssection and one outlet cross-section. Assume the flow is steady, inviscid, adiabatic, and has no body-force work ( $\Phi \equiv 0$ ). Using the integral mass and energy balances, show that $h_0=h+\frac{1}{2}|u|^2$ is the same at the inlet and outlet.




# Optional extra credit (up to 3 points)

> [!Question] Choose one:
> 
> (A) For a calorically perfect ideal gas, use $a=\sqrt{\gamma R T}$ and $M=|u| / a$ to express $T_0 / T$ in terms of $M$ and $\gamma$ only.
> (B) If the flow is also isentropic, use the isentropic stagnation relation to express $p_0 / p$ in terms of $M$ and $\gamma$ only.