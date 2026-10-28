# Module 17: Unsteady 1D compressible flow 

Andres Goza

April 29, 2026

# Chapter 1

## Problem Formulation and Hyperbolic Structure

### 1.1 Motivation and Modeling Framework

In the previous module, we examined steady compressible flow in two spatial dimensions. That setting forced us to confront a fundamental feature of nonlinear compressible flow: the directions along which information propagates are not fixed, but instead depend on the local state of the flow itself. The resulting structure led naturally to the method of characteristics, in which the governing equations are analyzed along curves embedded within the spatial domain.

In the present module, we examine unsteady flow in one spatial dimension. This change is not merely a simplification of geometry. It reflects a different class of physical problems, in which the evolution of the flow in time plays a central role.

Many important compressible-flow phenomena arise in settings where the flow undergoes rapid temporal changes: disturbances introduced by boundary motion, the propagation of acoustic waves, or the evolution of initially nonuniform states. While such problems are generally multidimensional in their full form, their essential structure is often governed by the propagation of waves along preferred directions. The one-dimensional unsteady setting provides the simplest framework in which this propagation can be isolated and understood.

Our goal in this module is therefore to develop a framework for describing how information propagates through a compressible fluid in time.

Choice of formulation. As in earlier modules, there are multiple equivalent ways to represent compressible flow. In particular, under suitable assumptions, the governing equations may be written in terms of a scalar velocity potential, leading to a second-order partial differential equation. Indeed, in Module 3, we showed that the unsteady one-dimensional potential equation is hyperbolic, and we could in principle continue to utilize that formulation.

In the present setting, however, it is more natural to work directly with the primitive flow variables ( $\rho, u, p$ ). This choice is motivated by two considerations. First, unsteady problems are typically posed as initial-value problems, in which the initial state of the flow is specified directly in terms of physical variables such as velocity and pressure. Second, the formulations we will develop later in this module, including those involving discontinuities, require direct access to these variables.

This mirrors the approach taken in Module 6. There, we worked with the governing equations in primitive variables in order to expose their first-order structure and identify the characteristic directions of steady flow. We will adopt the same philosophy here.

Governing equations. We consider one-dimensional, unsteady, inviscid flow. Under these assumptions, the governing equations are the conservation of mass and momentum,

$$
\begin{align*}
\frac{\partial \rho}{\partial t}+\frac{\partial(\rho u)}{\partial x} & =0  \tag{1.1}\\
\frac{\partial u}{\partial t}+u \frac{\partial u}{\partial x}+\frac{1}{\rho} \frac{\partial p}{\partial x} & =0 \tag{1.2}
\end{align*}
$$

To close the system, we assume that the flow is isentropic within each smooth region, so that entropy is uniform locally and pressure may be expressed as a function of density alone. This allows us to write

$$
\begin{equation*}
d p=a^{2} d \rho \tag{1.3}
\end{equation*}
$$

where $a$ is the local speed of sound. This assumption applies within smooth portions of the flow. Across discontinuities such as shocks, entropy is no longer uniform and the flow must be analyzed using conservation laws and jump conditions.
We emphasize that these equations are not new. They are the one-dimensional specialization of the governing equations introduced earlier in the course. Our objective is not to re-derive them, but rather to analyze their structure in a way that reveals how disturbances propagate through the flow.

Anticipated structure. The system given by Eqs. (1.1)-(1.3) is a first-order system of partial differential equations in the variables ( $x, t$ ). Based on the results of Module 3, we already expect that the corresponding potential formulation is hyperbolic. It follows that this system, which is equivalent under the assumptions made here, must also admit real directions in spacetime along which information propagates.

In the following section, we will identify these directions using the same approach developed in Module 6. We will show that the governing equations admit two distinct families of curves in the $(x, t)$ plane along which the system reduces to ordinary differential equations. These curves will be interpreted as the paths along which disturbances travel through the flow.

### 1.2 Characteristic Structure and Compatibility Relations

We now analyze the structure of the governing system (1.1)-(1.3) in order to identify the directions in spacetime along which information propagates.

First-order system form. Following the approach developed in Module 6, we begin by writing the governing equations as a first-order system in vector form. Introducing the state vector

$$
\boldsymbol{q}=\left[\begin{array}{l}
u  \tag{1.4}\\
\rho
\end{array}\right],
$$

we expand Eqs. (1.1)-(1.3) to obtain

$$
\begin{equation*}
\rho_{t}+u \rho_{x}+\rho u_{x}=0 \tag{1.5}
\end{equation*}
$$

$$
\begin{equation*}
u_{t}+u u_{x}+\frac{a^{2}}{\rho} \rho_{x}=0 \tag{1.6}
\end{equation*}
$$

These equations may be written compactly as

$$
\begin{equation*}
\boldsymbol{A}(\boldsymbol{q}) \boldsymbol{q}_{t}+\boldsymbol{B}(\boldsymbol{q}) \boldsymbol{q}_{x}=0 \tag{1.7}
\end{equation*}
$$

where

$$
\boldsymbol{A}=\left[\begin{array}{ll}
1 & 0  \tag{1.8}\\
0 & 1
\end{array}\right], \quad \boldsymbol{B}=\left[\begin{array}{cc}
u & \frac{a^{2}}{\rho} \\
\rho & u
\end{array}\right]
$$

Equation (1.7) is the direct analog, in the $(x, t)$ plane, of the system developed in Module 6 for steady flow in $(x, y)$.

Characteristic directions. As in Module 6, we seek directions in spacetime along which the system reduces to an ordinary differential equation. Let a curve in the $(x, t)$ plane be defined by

$$
\begin{equation*}
\frac{d x}{d t}=\lambda \tag{1.9}
\end{equation*}
$$

Along such a curve, the total derivative of $\boldsymbol{q}$ is

$$
\begin{equation*}
\frac{d \boldsymbol{q}}{d t}=\boldsymbol{q}_{t}+\lambda \boldsymbol{q}_{x} . \tag{1.10}
\end{equation*}
$$

Substituting (1.10) into (1.7), we obtain

$$
\begin{equation*}
\boldsymbol{A} \frac{d \boldsymbol{q}}{d t}+(\boldsymbol{B}-\lambda \boldsymbol{A}) \boldsymbol{q}_{x}=0 \tag{1.11}
\end{equation*}
$$

For the system to reduce to an ODE along the curve, the term multiplying $\boldsymbol{q}_{x}$ must be singular. This leads to the characteristic condition

$$
\begin{equation*}
\operatorname{det}(\boldsymbol{B}-\lambda \boldsymbol{A})=0 \tag{1.12}
\end{equation*}
$$

Using (1.8), this condition becomes

$$
\operatorname{det}\left[\begin{array}{cc}
u-\lambda & \frac{a^{2}}{\rho}  \tag{1.13}\\
\rho & u-\lambda
\end{array}\right]=0,
$$

which simplifies to

$$
\begin{equation*}
(u-\lambda)^{2}-a^{2}=0 \tag{1.14}
\end{equation*}
$$

Solving (1.14) yields the two characteristic directions

$$
\begin{equation*}
\lambda=u \pm a, \tag{1.15}
\end{equation*}
$$

so that the characteristic curves satisfy

$$
\begin{equation*}
\frac{d x}{d t}=u \pm a \tag{1.16}
\end{equation*}
$$

Compatibility relations. We now determine how the flow variables evolve along the characteristic curves identified in (1.16). Starting from the transformed system (1.11), we observe that this equation involves both the directional derivative $d \boldsymbol{q} / d t$ and the spatial derivative $\boldsymbol{q}_{x}$. In order to obtain an ordinary differential equation along the characteristic direction, we must eliminate the $\boldsymbol{q}_{x}$ term.

This is made possible by the fact that, along a characteristic direction, the matrix $\boldsymbol{B}-\lambda \boldsymbol{A}$ is singular, as enforced by the condition (1.12). We therefore seek a nontrivial vector $\boldsymbol{\alpha}^{T}$ satisfying

$$
\begin{equation*}
\boldsymbol{\alpha}^{T}(\boldsymbol{B}-\lambda \boldsymbol{A})=\mathbf{0}^{T} \tag{1.17}
\end{equation*}
$$

that is, a left null vector of the matrix $\boldsymbol{B}-\lambda \boldsymbol{A}$.
Premultiplying (1.11) by $\boldsymbol{\alpha}^{T}$ and using (1.17), we obtain

$$
\begin{equation*}
\boldsymbol{\alpha}^{T} \boldsymbol{A} \frac{d \boldsymbol{q}}{d t}=0 \tag{1.18}
\end{equation*}
$$

This equation involves only the directional derivative along the characteristic curve and therefore represents an ordinary differential relation governing the evolution of the flow variables along that curve.

To make this relation explicit, we compute the left null vector. Using (1.8), the condition (1.17) becomes

$$
\boldsymbol{\alpha}^{T}\left[\begin{array}{cc}
u-\lambda & \frac{a^{2}}{\rho}  \tag{1.19}\\
\rho & u-\lambda
\end{array}\right]=\mathbf{0}^{T} .
$$

Letting $\boldsymbol{\alpha}^{T}=\left[\begin{array}{ll}\alpha_{1} & \alpha_{2}\end{array}\right]$, this yields the system

$$
\begin{align*}
\alpha_{1}(u-\lambda)+\alpha_{2} \rho & =0  \tag{1.20}\\
\alpha_{1} \frac{a^{2}}{\rho}+\alpha_{2}(u-\lambda) & =0 \tag{1.21}
\end{align*}
$$

For the characteristic directions $\lambda=u \pm a$ given by (1.15), these equations admit nontrivial solutions. A convenient choice of left null vectors is

$$
\boldsymbol{\alpha}^{T}=\left[\begin{array}{ll}
1 & \pm \frac{a}{\rho} \tag{1.22}
\end{array}\right]
$$

corresponding to the characteristic families $\lambda=u \pm a$.
Substituting (1.22) into (1.18) and recalling the definition of $\boldsymbol{q}$ in (1.4), we obtain

$$
\begin{equation*}
\frac{d u}{d t} \pm \frac{a}{\rho} \frac{d \rho}{d t}=0 \quad \text { along } \quad \frac{d x}{d t}=u \pm a \tag{1.23}
\end{equation*}
$$

Using the isentropic relation (1.3), this may be written equivalently as

$$
\begin{equation*}
\frac{d u}{d t} \pm \frac{1}{\rho a} \frac{d p}{d t}=0 \quad \text { along } \quad \frac{d x}{d t}=u \pm a \tag{1.24}
\end{equation*}
$$

Interpretation. Equations (1.16) and (1.24) show that the governing system admits two distinct families of curves in spacetime along which the flow variables evolve according to ordinary differential relations. These curves represent the paths along which disturbances propagate through the flow.
The characteristic speeds $u \pm a$ may be interpreted as the velocity of acoustic disturbances relative to the laboratory frame: the flow convects information at speed $u$, while sound waves propagate relative to the fluid at speed $\pm a$. The combination of these effects produces the two families of propagation directions identified above.
Equations (1.1)-(1.3) form a closed system governing one-dimensional unsteady compressible flow under the assumptions stated above.

# Chapter 2

## Riemann Invariants and the Simple-Wave Case

### 2.1 Riemann Invariants of Unsteady One-Dimensional Flow

We now build on the compatibility relations derived in Section 1.2 to identify quantities that are preserved along the characteristic curves. In Module 6, analogous invariant quantities played a central role in constructing solutions to the steady two-dimensional problem. Our goal here is to identify and interpret the corresponding invariants for the unsteady one-dimensional system.

Evolution along characteristic curves. Let $C_{ \pm}$denote the two families of characteristic curves defined by Eq. (1.16). We parametrize each curve as

$$
\begin{equation*}
C_{ \pm}: \quad\left(x_{ \pm}(t), t\right), \quad \frac{d x_{ \pm}}{d t}=u \pm a \tag{2.1}
\end{equation*}
$$

and define the flow variables restricted to these curves as

$$
\begin{equation*}
u_{ \pm}(t):=u\left(x_{ \pm}(t), t\right), \quad \rho_{ \pm}(t):=\rho\left(x_{ \pm}(t), t\right), \quad a_{ \pm}(t):=a\left(x_{ \pm}(t), t\right) \tag{2.2}
\end{equation*}
$$

With this notation, the compatibility relations (1.23) may be written as ordinary differential equations along each characteristic curve:

$$
\begin{equation*}
\frac{d u_{ \pm}}{d t} \pm \frac{a_{ \pm}}{\rho_{ \pm}} \frac{d \rho_{ \pm}}{d t}=0 \tag{2.3}
\end{equation*}
$$

Thermodynamic closure. To integrate Eq. (2.3), we relate the speed of sound to the density. For a calorically perfect gas, the ideal gas law together with the isentropic condition implies that pressure and density are related by

$$
\begin{equation*}
p=K \rho^{\gamma} \tag{2.4}
\end{equation*}
$$

where $K$ is constant within a region of uniform entropy and $\gamma$ is the ratio of specific heats.
Using the definition of the speed of sound,

$$
\begin{equation*}
a^{2}=\frac{d p}{d \rho} \tag{2.5}
\end{equation*}
$$

Eqs. (2.4)-(2.5) yield

$$
\begin{equation*}
a^{2}=\gamma K \rho^{\gamma-1} . \tag{2.6}
\end{equation*}
$$

Differentiating Eq. (2.6) with respect to $t$ along the characteristic curve gives

$$
\begin{equation*}
\frac{1}{a_{ \pm}} \frac{d a_{ \pm}}{d t}=\frac{\gamma-1}{2} \frac{1}{\rho_{ \pm}} \frac{d \rho_{ \pm}}{d t} . \tag{2.7}
\end{equation*}
$$

Derivation of the invariants. Substituting Eq. (2.7) into Eq. (2.3) eliminates $\rho_{ \pm}$, yielding

$$
\begin{equation*}
\frac{d u_{ \pm}}{d t} \pm \frac{2}{\gamma-1} \frac{d a_{ \pm}}{d t}=0 \tag{2.8}
\end{equation*}
$$

Equation (2.8) may be written as

$$
\begin{equation*}
\frac{d}{d t}\left(u_{ \pm} \pm \frac{2 a_{ \pm}}{\gamma-1}\right)=0 \tag{2.9}
\end{equation*}
$$

so that the quantity in parentheses is constant along the corresponding characteristic curve. We therefore define the Riemann invariants

$$
\begin{equation*}
I_{ \pm}:=u \pm \frac{2 a}{\gamma-1} \tag{2.10}
\end{equation*}
$$

with the properties

$$
\begin{equation*}
\frac{d I_{ \pm}}{d t}=0 \quad \text { along } \quad C_{ \pm} \tag{2.11}
\end{equation*}
$$

Interpretation. Equations (2.10)-(2.11) show that each family of characteristic curves carries a single scalar quantity unchanged through spacetime. The solution at any point is determined by the values of $I_{+}$and $I_{-}$carried along the two characteristics that intersect at that point. In this sense, the Riemann invariants represent the fundamental information propagated by the flow.

The invariants $I_{+}$and $I_{-}$provide a compact description of how information propagates through the flow. To understand how these quantities determine the structure of solutions, it is useful to examine a canonical physical problem in which waves are generated and interact. In the following section, we consider the shock-tube problem, which provides a concrete setting in which the role of the invariants can be clearly interpreted.

### 2.2 The Shock Tube problem and its simple wave region

### 2.2.1 Canonical Example: Expansion in a Shock Tube

A central problem in unsteady compressible flow is the shock tube, in which a diaphragm initially separates two regions of gas at rest with different pressures. When the diaphragm is removed at $t=0$, the initial discontinuity evolves into a structured flow consisting of several distinct features: a left-going expansion wave, a uniform intermediate state (Region 3), a contact surface, and a right-going shock. These structures are illustrated in Fig. 2.1.

This problem is of particular interest because it contains, in a single setting, the fundamental building blocks of compressible wave motion: smooth expansions, uniform regions, and discontinuities.

In this lecture, we focus on the expansion wave, which provides a prototype for a class of smooth solutions.

The expansion fan plays a role closely analogous to that of the centered expansion studied in Module 6. In the steady two-dimensional problem, the flow was required to turn continuously around a corner, and the solution was constructed from a continuum of states organized along characteristic curves. In the present unsteady setting, the initial discontinuity at the diaphragm cannot be sustained, and the flow instead transitions through a continuous family of intermediate states. Each of these states propagates at a different characteristic speed, giving rise to the fan structure.

To understand the organization of the expansion region, we examine the characteristic curves defined by $\frac{d x}{d t}=u \pm a$. In Region 4, where the flow is initially at rest, these reduce to $\frac{d x}{d t}= \pm a_{4}$. The characteristics with $\frac{d x}{d t}=u+a$ propagate from Region 4 into the expansion region. Because Region 4 is uniform, all such curves carry the same value of the invariant $I_{+}$into the fan.

As a result, the invariant $I_{+}$is constant throughout the expansion region. In contrast, the characteristics satisfying $\frac{d x}{d t}=u-a$ form the fan itself. Each such curve corresponds to a different local state, and the flow variables vary continuously across this family, connecting the initial state in Region 4 to the uniform state in Region 3.

This example illustrates a fundamental structure: within the expansion region, the solution is governed by a single invariant inherited from an adjacent uniform state, while variation in the flow occurs across the complementary characteristic family. In the following subsection, we formalize this structure and define the class of solutions for which it holds.

The $x-t$ diagram in Fig. 2.1 makes this structure explicit. The expansion fan occupies a region bounded by characteristic curves satisfying $\frac{d x}{d t}=u-a$, which emanate from the diaphragm rupture. Within this region, the invariant $I_{+}$is constant, inherited from Region 4, while the flow variables vary across the $C_{-}$family. The contact surface and shock, which bound Regions 3 and 2, will be analyzed in a later lecture.

### 2.2.2 Definition and Consequences of Simple-Wave Regions

In general, the invariants $I_{+}$and $I_{-}$are constant only along their respective characteristic curves. A special class of solutions arises when one of these invariants is constant everywhere within a region.

Definition. A simple-wave region is a region of the flow in which one of the Riemann invariants is constant throughout the region. For example, a $C_{+}$simple-wave region is defined by

$$
\begin{equation*}
I_{+}=u+\frac{2 a}{\gamma-1}=I_{+}^{0} \tag{2.12}
\end{equation*}
$$

where $I_{+}^{0}$ is a constant.
Reduction of the solution. Equation (2.12) implies a direct relationship between the flow variables,

$$
\begin{equation*}
u=I_{+}^{0}-\frac{2 a}{\gamma-1} \tag{2.13}
\end{equation*}
$$


![[Pasted image 20260513094921.png|600]]

Figure 2.1: Shock-tube structure and the expansion fan as a simple-wave region. Top: initial diaphragm-separated state. Middle: physical wave pattern shortly after rupture, showing the expansion fan, Region 3, the contact surface, Region 2, and the shock. Bottom: corresponding $x-t$ diagram, drawn with $t$ horizontal so that slopes represent $d x / d t$ directly. For the schematic, we use representative values $u_{4}=0, a_{4}=1, u_{3}=\frac{1}{2}$, and $a_{3}=\frac{3}{4}$, which are consistent with an expansion: the flow accelerates through the fan while the sound speed decreases. The fan is bounded by the $C_{-}$rays satisfying $d x / d t=u-a$, while the invariant $I_{+}$remains constant throughout the fan, inherited from Region 4. The full shock-tube construction, including the contact and shock, will be taken up later.

so that the state of the flow is determined by a single variable. The solution therefore lies along a curve in the $(u, a)$ plane, and variation within the region occurs only through changes in $a$ (or equivalently, in density and pressure).

In this setting, the $C_{+}$characteristics carry the constant value $I_{+}^{0}$ throughout the region, while all variation in the flow is associated with the $C_{-}$family.

### 2.2.3 Expansion and Compression in Simple Waves

We now examine how the structure of the characteristic curves reflects the physical behavior of the flow.

Characteristic slopes. From Eq. (1.16), the slopes of the characteristic curves are given by

$$
\begin{equation*}
\frac{d x}{d t}=u \pm a \tag{2.14}
\end{equation*}
$$

In a $C_{+}$simple-wave region, the relation (2.13) allows these slopes to be expressed entirely in terms of $a$. In particular, the slope of the $C_{-}$characteristics becomes

$$
\begin{equation*}
\frac{d x}{d t}=u-a=I_{+}^{0}-\frac{2 a}{\gamma-1}-a=I_{+}^{0}-\frac{\gamma+1}{\gamma-1} a . \tag{2.15}
\end{equation*}
$$

Variation of characteristic spacing. The behavior of neighboring characteristics is determined by the spatial variation of the slope (2.15). Differentiating with respect to $x$ yields

$$
\begin{equation*}
\frac{\partial}{\partial x}(u-a)=-\frac{\gamma+1}{\gamma-1} \frac{\partial a}{\partial x} . \tag{2.16}
\end{equation*}
$$

The sign of $\partial a / \partial x$ therefore determines whether the characteristics converge or diverge:

- If $\partial a / \partial x<0$, then $\partial(u-a) / \partial x>0$, so the characteristic slopes increase with $x$, and neighboring characteristics diverge. This corresponds to an expansion wave.
- If $\partial a / \partial x>0$, then $\partial(u-a) / \partial x<0$, so the characteristic slopes decrease with $x$, and neighboring characteristics converge. This corresponds to a compression wave.

Physical interpretation. Since the speed of sound satisfies $a^{2} \propto T$, a decrease in $a$ is associated with decreases in temperature, pressure, and density, while an increase in $a$ corresponds to compression of the flow. Thus, the geometric behavior of the characteristics directly reflects the underlying physical process: expansion waves spread smoothly as characteristics diverge, while compression waves lead to the progressive steepening of gradients as characteristics converge.

### 2.3 Outlook

The expansion fan studied in this chapter represents a special class of solutions in which one Riemann invariant is constant throughout a region. Such simple-wave regions arise when the flow is influenced by a single family of characteristic curves carrying information from an adjacent uniform state.

In general, however, both invariants may vary within the flow. This occurs in problems involving interacting waves, such as the full shock-tube solution, where expansion regions, uniform states, and discontinuities must be connected consistently. In these cases, the solution cannot be determined from a single invariant, and instead requires a more general framework that incorporates both characteristic families as well as conservation across discontinuities.

In the next chapter, we develop this framework and apply it to construct solutions to problems involving multiple interacting waves.

# Chapter 3

## Wave Interaction, Discontinuities, and the Shock-Tube Problem

### 3.1 The Shock-Tube Problem and the Limits of Simple Waves

In the previous chapter, we examined simple-wave solutions, in which the flow within a region is governed by a single Riemann invariant that remains constant throughout. While this framework provides a powerful description of smooth expansions, it does not capture the full range of behavior exhibited by compressible flows.

To illustrate this deficiency, we return to the shock-tube problem introduced in Chapter 2. Following the rupture of the diaphragm at $(x, t)=(0,0)$, the flow evolves into a structured configuration consisting of several distinct regions: a left-going expansion fan, a uniform intermediate state (Region 3), a contact surface, a second uniform state (Region 2), and a right-going shock that propagates into the initially undisturbed Region 1.

Our goal is to determine how the flow transitions from the initial states in Regions 4 and 1 to this multi-region structure. From the analysis of Chapter 2, we know that the expansion fan provides a simple-wave region that connects Region 4 to Region 3. In particular, the constancy of the invariant $I_{+}$along $C_{+}$characteristics provides a relation between the state in Region 3 and the initial state in Region 4. This relation constrains ( $u_{3}, a_{3}$ ), but does not by itself fully determine the state in Region 3. The actual state is obtained only after this relation is coupled to the conditions imposed across other regions of the shock tube.

However, the flow in these other regions cannot be computed by the simple-wave framework we established earlier. To see this, consider a region of compression, such as that which develops to the right of the expansion fan. From the results of Chapter 2, the slope of the $C_{-}$characteristics satisfies

$$
\begin{equation*}
\frac{\partial}{\partial x}(u-a)=-\frac{\gamma+1}{\gamma-1} \frac{\partial a}{\partial x} . \tag{3.1}
\end{equation*}
$$

In a compression, the pressure and temperature increase, so that the speed of sound increases and $\partial a / \partial x>0$. Equation (3.1) then implies that $\partial_{x}(u-a)<0$, so that neighboring $C_{-}$characteristics tilt toward one another and eventually intersect.

This intersection signals the breakdown of the smooth solution. Since the invariants carried along different characteristics generally take different values, their intersection would lead to a multi-
valued flow state. The governing equations do not admit such solutions, and the flow instead resolves this inconsistency through the formation of a discontinuity.

The shock tube therefore illustrates a fundamental limitation of the simple-wave framework. The remainder of the flow requires additional tools to handle both discontinuities and the interaction of multiple wave families.

In particular, to proceed from Region 3 to Region 1, we must address two new challenges. First, we must determine how to represent and analyze discontinuities, since the smooth characteristic framework is no longer valid. Second, we must establish how information is transferred across interfaces between regions, so that the solution can be constructed consistently throughout the domain.

In the sections that follow, we develop the tools needed to address these challenges and to complete the construction of the shock-tube solution.

### 3.2 The Contact Surface

We now consider the interface that separates Regions 3 and 2 in the shock-tube solution. Unlike the expansion fan and the shock, which are generated by distinct physical mechanisms, this interface arises as a consequence of the need to connect the states produced by those mechanisms into a single, consistent flow.

Compatibility of the fan and shock. The expansion fan connects Region 4 to Region 3 through a smooth, isentropic process, providing a relation between the state ( $u_{3}, a_{3}$ ) and the initial conditions in Region 4. Independently, the shock connects Region 1 to Region 2 through a compressive, entropyproducing process, determining the state ( $u_{2}, p_{2}, \rho_{2}$ ) from the known conditions in Region 1.

These two processes must be compatible: together, they must produce a physically realizable flow in which the intermediate states meet. In particular, the states in Regions 3 and 2 must match in velocity and pressure so that the composite fan-shock system produces a consistent intermediate flow. The solution therefore selects intermediate states satisfying

$$
\begin{equation*}
u_{2}=u_{3}, \quad p_{2}=p_{3} . \tag{3.2}
\end{equation*}
$$

Entropy mismatch and density discontinuity. While the fan and shock can be arranged to produce matching velocity and pressure, they do so through fundamentally different thermodynamic processes. The expansion fan is isentropic, while the shock involves an increase in entropy. As a result, the states in Regions 3 and 2 generally do not lie on the same thermodynamic path, and there is no reason to expect that their densities will agree. In general,

$$
\begin{equation*}
\rho_{2} \neq \rho_{3} \tag{3.3}
\end{equation*}
$$

The interface between Regions 3 and 2 therefore consists of a discontinuity in density (and entropy) across which velocity and pressure remain continuous. This is the defining feature of a contact surface.

Propagation of the contact. Because the velocity is continuous across the interface, the contact surface moves with the local fluid velocity,

$$
\begin{equation*}
\frac{d x}{d t}=u_{2}=u_{3} . \tag{3.4}
\end{equation*}
$$

Role in the solution. The contact surface serves to transmit the velocity and pressure determined by the expansion fan into Region 2, where the remaining unknown-the density $\rho_{2}$-is determined by the shock relations connecting Region 2 to the known state in Region 1. In this way, the contact provides the link between the smooth expansion and the compressive shock that together define the shock-tube solution.

### 3.3 Shock Waves and Jump Conditions

We now turn to the final element required to complete the shock-tube solution: the compressive discontinuity that connects Region 2 to the initial state in Region 1.

Formation of a shock. As discussed in Section 3.1, regions of compression lead to the convergence of characteristic curves. When these characteristics intersect, the smooth solution breaks down, as different values of the flow variables are brought to the same point in spacetime. The governing equations do not admit multi-valued solutions, and the flow instead resolves this inconsistency through the formation of a discontinuity, or shock.

Conservation across a moving discontinuity. Unlike the expansion fan, which is described by the characteristic relations of Chapter 2, a shock must be analyzed using the integral form of the conservation laws. Consider a control volume that encloses the shock and moves with speed $u_{s}$. Applying conservation of mass and momentum across this moving interface yields the jump conditions

$$
\begin{align*}
{\left[\rho\left(u-u_{s}\right)\right] } & =0,  \tag{3.5}\\
{\left[\rho u\left(u-u_{s}\right)+p\right] } & =0, \tag{3.6}
\end{align*}
$$

where [ • ] denotes the difference between the downstream and upstream states. These relations are known as the Rankine-Hugoniot conditions.

Relation to earlier results. The jump conditions (3.5)-(3.6) are known as the Rankine-Hugoniot conditions, which is the name given to the jump conditions for flows with discontinuities in both steady and unsteady settings. In the present configuration, the discontinuity is time-dependent, and its speed $u_{s}$ must be determined as part of the solution, rather than being fixed by the geometry of the problem.

Application to the shock-tube problem. In the present setting, the upstream state (Region 1) is known from the initial conditions,

$$
\begin{equation*}
u_{1}=0, \quad p_{1}, \rho_{1} \text { given, } \tag{3.7}
\end{equation*}
$$

while the downstream state (Region 2) satisfies

$$
\begin{equation*}
u_{2}=u_{3}, \quad p_{2}=p_{3}, \tag{3.8}
\end{equation*}
$$

as determined by the contact conditions (3.2). The density $\rho_{2}$ and the shock speed $u_{s}$ remain unknown.

Substituting the known quantities into Eqs. (3.5)-(3.6) yields a system of equations that determines $\rho_{2}$ and $u_{s}$. In this way, the shock relations provide the final conditions needed to connect the intermediate state to the initial state in Region 1.

Characteristic structure near the shock. The presence of the shock modifies the propagation of information. Characteristics from Region 2 converge toward the shock, carrying information into it, while characteristics in Region 1 do not propagate back into Region 2. The shock therefore acts as a one-way interface, through which information passes only in the downstream direction. This behavior is consistent with the entropy increase associated with the shock.

Summary. The Rankine-Hugoniot conditions provide a mechanism for coupling the state in Region 2 and the speed of the shock to the post-expansion behavior in Region 3. These collections of unknowns are collectively established from the conditions in the known Regions 1 and 4. These set of relations, coupled together, are required to construct the full shock-tube solution.

### 3.4 Constructing the Shock-Tube Solution

We now summarize how the elements developed in this chapter combine to form a complete solution to the shock-tube problem. The key idea is that the flow is constructed by connecting a sequence of regions, each governed by a different set of relations, in a manner consistent with both the characteristic structure and the conservation laws.

Structure of the solution. The shock-tube flow consists of four distinct components:

- an expansion fan connecting Region 4 to Region 3,
- a contact surface connecting Region 3 to Region 2,
- a shock connecting Region 2 to Region 1,
- and the uniform regions themselves.

Each of these components plays a specific role in transmitting the initial conditions into a consistent flow. The expansion fan provides a relation between Region 4 and Region 3, while the contact surface enforces compatibility between Regions 3 and 2, and the shock supplies the additional relations needed to determine the remaining unknowns by connecting them to the other known Region 1. The full solution is therefore obtained by solving a coupled system that links all regions together.

Information flow. This procedure reflects the way in which information propagates through the flow. The expansion fan transmits information from Region 4 into the interior via the $C_{+}$characteristics, while the contact surface carries this information into Region 2 through continuity of velocity and pressure. The shock then enforces conservation by connecting the resulting state to the known conditions in Region 1. But the information does not flow from one region (say, Region 4) to another. Instead, the Regions 1 and 4 provide the conditions that collectively determine the internal states imposed by the breaking of the diaphragm.

We can put all of this information together to create an updated (and more complex) collection of all the characteristics through the entire shock tube problem.


![[Pasted image 20260513095044.png]]


Outlook. While the structure of the solution is now clear, the practical construction of solutions to general unsteady problems requires a systematic method for propagating information along characteristics and enforcing the governing relations throughout the domain. In the next chapter, we develop such a framework and apply it to the solution of initial-value problems using the method of characteristics.

20CHAPTER 3. WAVE INTERACTION, DISCONTINUITIES, AND THE SHOCK-TUBE PROBLEM

# Chapter 4

## Constructing Solutions to the Shock-Tube Problem

### 4.1 States, Unknowns, and Governing Relations

We now turn from the structural description of the shock-tube solution to its explicit construction. Our goal in this chapter is to determine all flow quantities in each region, using the governing relations developed in the previous chapters.

To begin, we identify what is known, what is unknown, and how the governing equations constrain those unknowns.

Known states and solution structure. The initial conditions specify two uniform states:

$$
\begin{equation*}
\left(u_{4}, p_{4}, \rho_{4}\right), \quad\left(u_{1}, p_{1}, \rho_{1}\right) \tag{4.1}
\end{equation*}
$$

with $u_{4}=u_{1}=0$ in the standard shock-tube configuration.
From Chapter 3, we know that the solution organizes into the sequence
Region $4 \rightarrow$ expansion fan → Region $3 \rightarrow$ contact → Region $2 \rightarrow$ shock → Region 1 .
In this section, we focus on determining the uniform states in Regions 2 and 3. The detailed structure within the expansion fan will be addressed separately.

Unknown states. At first glance, the unknowns are the states in Regions 2 and 3:

$$
\begin{equation*}
\left(u_{2}, p_{2}, \rho_{2}\right), \quad\left(u_{3}, p_{3}, \rho_{3}\right) \tag{4.2}
\end{equation*}
$$

However, the contact conditions reduce the number of independent variables. In particular,

$$
\begin{equation*}
u_{2}=u_{3}=u_{*}, \quad p_{2}=p_{3}=p_{*} \tag{4.3}
\end{equation*}
$$

so that both regions share a common velocity and pressure.
The remaining unknowns are therefore

$$
\begin{equation*}
u_{*}, \quad p_{*}, \quad \rho_{2}, \quad \rho_{3} \tag{4.4}
\end{equation*}
$$

Reduction via thermodynamic relations. The expansion from Region 4 to Region 3 is isentropic, and therefore the thermodynamic variables in Region 3 are not independent. In particular, once the pressure $p_{*}$ is known, the density $\rho_{3}$ and sound speed $a_{3}$ are determined through isentropic relations.

To make this dependence explicit-and to keep the presentation self-contained-we now derive the relevant thermodynamic relations from first principles.

Isentropic relations for a calorically perfect gas. From the homentropic closure introduced in Chapter 1,

$$
\begin{equation*}
d p=a^{2} d \rho \tag{4.5}
\end{equation*}
$$

together with the definition of the speed of sound for a calorically perfect ideal gas,

$$
\begin{equation*}
a^{2}=\gamma \frac{p}{\rho} \tag{4.6}
\end{equation*}
$$

we obtain

$$
\begin{equation*}
\frac{d p}{d \rho}=\gamma \frac{p}{\rho} \tag{4.7}
\end{equation*}
$$

Separating variables yields

$$
\begin{equation*}
\frac{d p}{p}=\gamma \frac{d \rho}{\rho} \tag{4.8}
\end{equation*}
$$

which integrates to

$$
\begin{equation*}
\ln p=\gamma \ln \rho+\ln K \tag{4.9}
\end{equation*}
$$

or equivalently,

$$
\begin{equation*}
p=K \rho^{\gamma} . \tag{4.10}
\end{equation*}
$$

Here $K$ is a constant determined by the entropy of the flow. Within an isentropic region such as the expansion fan, $K$ is constant but need not be evaluated explicitly. In the relations that follow, only ratios of pressure, density, and sound speed appear, so that $K$ cancels identically.

Derived relations. Combining Eq. (4.10) with Eq. (4.6) yields relations between the thermodynamic variables. In particular, between Regions 4 and 3, we obtain

$$
\begin{equation*}
\frac{\rho_{3}}{\rho_{4}}=\left(\frac{p_{*}}{p_{4}}\right)^{1 / \gamma} \tag{4.11}
\end{equation*}
$$

and

$$
\begin{equation*}
\frac{a_{3}}{a_{4}}=\left(\frac{p_{*}}{p_{4}}\right)^{\frac{\gamma-1}{2 \gamma}} \tag{4.12}
\end{equation*}
$$

Summary. The thermodynamic relations show that $\rho_{3}$ and $a_{3}$ are determined once $p_{*}$ is known. The independent unknowns are therefore reduced to

$$
\begin{equation*}
u_{*}, \quad p_{*}, \quad \rho_{2} . \tag{4.13}
\end{equation*}
$$

In the next section, we derive the governing relations that determine these quantities and outline a procedure for solving the resulting system.

### 4.2 Solving for the Uniform States

We now derive the relations needed to determine the unknown quantities

$$
u_{*}, \quad p_{*}, \quad \rho_{2} .
$$

These quantities are obtained by combining the expansion fan relations, the contact conditions, and the shock jump conditions.

Expansion fan relation. We saw earlier that the expansion fan is governed by the Riemann invariant that remains constant along the $C_{+}$characteristics. Applying this invariant between Regions 4 and 3 yields

$$
\begin{equation*}
u_{*}+\frac{2 a_{3}}{\gamma-1}=u_{4}+\frac{2 a_{4}}{\gamma-1} \tag{4.14}
\end{equation*}
$$

Solving for $u_{*}$ gives

$$
\begin{equation*}
u_{*}=u_{4}+\frac{2}{\gamma-1}\left(a_{4}-a_{3}\right) \tag{4.15}
\end{equation*}
$$

Substituting for $a_{3}$ using Eq. (4.12) then yields

$$
\begin{equation*}
u_{*}=u_{4}+\frac{2 a_{4}}{\gamma-1}\left[1-\left(\frac{p_{*}}{p_{4}}\right)^{\frac{\gamma-1}{2 \gamma}}\right] \tag{4.16}
\end{equation*}
$$

This relation expresses the velocity $u_{*}$ in terms of the unknown pressure $p_{*}$.
Shock relation. We now relate $u_{*}$ and $p_{*}$ using the Rankine-Hugoniot conditions (3.5)-(3.6). In the present configuration, the upstream state (Region 1) is known, while the downstream state (Region 2) satisfies

$$
u_{2}=u_{*}, \quad p_{2}=p_{*} .
$$

Eliminating the shock speed $u_{s}$ between Eqs. (3.5)-(3.6), and substituting the known quantities, yields a relation between $u_{*}$ and $p_{*}$. The algebra follows standard steps and is not reproduced in full here; the resulting expression is

$$
\begin{equation*}
u_{*}=u_{1}+\left(p_{*}-p_{1}\right) \sqrt{\frac{2}{(\gamma+1) \rho_{1}} \frac{1}{p_{*}+\frac{\gamma-1}{\gamma+1} p_{1}}} \tag{4.17}
\end{equation*}
$$

Coupled system. Equations (4.16) and (4.17) provide two expressions for the same quantity $u_{*}$. Equating them yields a single nonlinear equation for $p_{*}$,

$$
\begin{equation*}
(4.16)-(4.17)=0, \tag{4.18}
\end{equation*}
$$

which may be solved numerically.
Solution procedure. Equation (4.18) defines a scalar nonlinear equation for $p_{*}$. This equation is solved using a root-finding method, such as Newton iteration, bisection, or standard numerical routines (e.g., scipy.optimize in Python).
Once $p_{*}$ is known, the remaining quantities follow directly:

- $u_{*}$ is obtained from Eq. (4.16),
- $\rho_{3}$ is obtained from Eq. (4.11),
- $a_{3}$ is obtained from Eq. (4.12).

Density behind the shock. The density $\rho_{2}$ is obtained from the Rankine-Hugoniot relations. Combining Eqs. (3.5) and (3.6) yields

$$
\begin{equation*}
\rho_{2}=\rho_{1} \frac{\frac{p_{*}}{p_{1}}+\frac{\gamma-1}{\gamma+1}}{1+\frac{\gamma-1}{\gamma+1} \frac{p_{*}}{p_{1}}} \tag{4.19}
\end{equation*}
$$

Shock speed. Finally, the shock speed $u_{s}$ may be recovered from the mass conservation condition (3.5), which gives

$$
\begin{equation*}
u_{s}=\frac{\rho_{2} u_{*}}{\rho_{2}-\rho_{1}} . \tag{4.20}
\end{equation*}
$$

Algorithmic summary. The procedure for determining the uniform states in Regions 2 and 3 may be summarized as follows:

```
Algorithm 1 Computation of Uniform States in the Shock-Tube Problem
    Given: $\left(u_{4}, p_{4}, \rho_{4}\right)$ and $\left(u_{1}, p_{1}, \rho_{1}\right)$
    Solve for $p_{*}$ :
    Form the nonlinear equation
        $(4.16)-(4.17)=0$
    Solve for $p_{*}$ using a root-finding method
    Compute $u_{*}$ :
    Use Eq. (4.16) to obtain $u_{*}$
    Compute Region 3 state:
    Use Eq. (4.11) to obtain $\rho_{3}$
    Use Eq. (4.12) to obtain $a_{3}$
    Compute Region 2 state:
    Use Eq. (4.19) to obtain $\rho_{2}$
    Compute shock speed:
    Use Eq. (4.20) to obtain $u_{s}$
```

This sequence determines all uniform states in the shock-tube solution. The remaining task is to resolve the continuous variation of the flow within the expansion fan, which we address next.

### 4.3 Resolving the Expansion Fan

In the previous section, we determined the uniform states in Regions 2 and 3. We now complete the solution by resolving the continuous variation of the flow within the expansion fan that connects Regions 4 and 3.

Motivation for a similarity solution. The expansion fan originates at the single point $(x, t)=(0,0)$ and propagates into Region 4. The governing equations admit no intrinsic length or time scale in
this region, and the solution must therefore depend only on the ratio

$$
\begin{equation*}
\xi=\frac{x}{t} \tag{4.21}
\end{equation*}
$$

That is, we seek flow state variables that depend not on ( $x, t$ ) separately but on their ratio defined by $\xi ; u=u(\xi), a=a(\xi)$, etc. This form is consistent with the characteristic structure derived in Chapter 2 and reflects the fact that each point within the fan lies along a straight characteristic ray emanating from the origin.

To make this structure precise, we define a family of curves $C_{\xi}$ parameterized by time as

$$
\begin{equation*}
C_{\xi}: \quad\left(x_{\xi}(t), t\right), \quad x_{\xi}(t)=\xi t \tag{4.22}
\end{equation*}
$$

so that each curve corresponds to a fixed value of $\xi$. Along such a curve, the flow variables remain constant in a self-similar solution.

Characteristic relation. We now compute how $\xi$ evolves along the curve $C_{\xi}$. Differentiating $x_{\xi}(t)=\xi t$ with respect to $t$ gives

$$
\begin{equation*}
\frac{d x_{\xi}}{d t}=\xi \tag{4.23}
\end{equation*}
$$

On the one hand, the self-similar form implies that within the fan the solution is constant along each $C_{\xi}$ curve; i.e., along curves of constant $\xi$. On the other hand, from Chapter 2, the governing equations admit characteristic directions

$$
\frac{d x_{ \pm}}{d t}=u \pm a
$$

Within the expansion fan, the $I_{+}$invariant is constant throughout the region, so that all variation in the solution must arise from moving across the $C_{-}$characteristics. Since the solution is constant at fixed $\xi$, each value of $\xi$ must therefore label a distinct $C_{-}$characteristic, so that

$$
\begin{equation*}
\xi=u-a \tag{4.24}
\end{equation*}
$$

Invariant relation. From Chapter 2, the $C_{+}$invariant remains constant throughout the fan, inherited from Region 4. Thus,

$$
\begin{equation*}
u+\frac{2 a}{\gamma-1}=u_{4}+\frac{2 a_{4}}{\gamma-1} \tag{4.25}
\end{equation*}
$$

Solution within the fan. Equations (4.24) and (4.25) provide two relations for the two unknowns $u$ and $a$ at any point within the fan. Substituting $u=\xi+a$ into Eq. (4.25) yields

$$
\begin{equation*}
\xi+a+\frac{2 a}{\gamma-1}=u_{4}+\frac{2 a_{4}}{\gamma-1} \tag{4.26}
\end{equation*}
$$

Rearranging gives

$$
\begin{equation*}
a\left(1+\frac{2}{\gamma-1}\right)=u_{4}+\frac{2 a_{4}}{\gamma-1}-\xi \tag{4.27}
\end{equation*}
$$

so that

$$
\begin{equation*}
a(\xi)=\frac{\gamma-1}{\gamma+1}\left(u_{4}+\frac{2 a_{4}}{\gamma-1}-\xi\right) . \tag{4.28}
\end{equation*}
$$

The velocity then follows from Eq. (4.24):

$$
\begin{equation*}
u(\xi)=\xi+a(\xi) \tag{4.29}
\end{equation*}
$$

Fan boundaries. The expansion fan is bounded by the extreme $C_{-}$characteristics that originate from Regions 4 and 3. These correspond to

$$
\begin{align*}
\xi_{\text {head }} & =u_{4}-a_{4}  \tag{4.30}\\
\xi_{\text {tail }} & =u_{*}-a_{3} \tag{4.31}
\end{align*}
$$

where $a_{3}$ is obtained from Eq. (4.12).
Complete solution in the fan. The flow within the expansion region is therefore given by the selfsimilar solution

$$
\begin{equation*}
u(x, t)=u(\xi), \quad a(x, t)=a(\xi), \quad \xi=\frac{x}{t} \tag{4.32}
\end{equation*}
$$

with $u(\xi)$ and $a(\xi)$ defined by Eqs. (4.28)-(4.29) for

$$
\xi_{\text {head }} \leq \xi \leq \xi_{\text {tail }} .
$$

Piecewise structure of the solution. Combining the results of Sections 4.2 and 4.3, the full solution may be written in piecewise form as

$$
(u, a)(x, t)= \begin{cases}\left(u_{4}, a_{4}\right), & \frac{x}{t}<u_{4}-a_{4} \\ \left(u\left(\frac{x}{t}\right), a\left(\frac{x}{t}\right)\right), & u_{4}-a_{4} \leq \frac{x}{t} \leq u_{*}-a_{3} \\ \left(u_{*}, a_{3}\right), & u_{*}-a_{3}<\frac{x}{t}<u_{*} \\ \left(u_{*}, a_{2}\right), & u_{*}<\frac{x}{t}<u_{s} \\ \left(u_{1}, a_{1}\right), & \frac{x}{t}>u_{s}\end{cases}
$$

where the locations of the contact and shock are determined from their respective propagation speeds.

Summary. The expansion fan provides a continuous transition between Regions 4 and 3, governed by a self-similar solution in which one invariant remains constant and the other determines the variation of the flow. This completes the construction of the shock-tube solution.

### 4.4 Generalization: Coupling Smooth Regions and Discontinuities

The shock-tube problem provides a canonical example in which a simple-wave region (the expansion fan) is coupled to discontinuities (the contact and shock) and uniform regions. While that solution admits a particularly clean structure, the underlying ideas extend directly to more general unsteady one-dimensional flows, in which smooth regions and discontinuities must be connected in a consistent way.

Propagation in smooth regions. In a general smooth region, neither Riemann invariant is constant throughout the domain. Instead, the solution at a point $P$ is determined by the values of the invariants carried along the two characteristic curves that intersect at $P$.

Let $A$ and $B$ denote the points from which the $C_{+}$and $C_{-}$characteristics passing through $P$ originate. Then

$$
\begin{equation*}
I_{+, P}=I_{+, A}, \quad I_{-, P}=I_{-, B} \tag{4.33}
\end{equation*}
$$

Using the definitions

$$
\begin{equation*}
I_{ \pm}=u \pm \frac{2 a}{\gamma-1} \tag{4.34}
\end{equation*}
$$

the state at $P$ satisfies

$$
\begin{align*}
I_{+, A} & =u_{P}+\frac{2 a_{P}}{\gamma-1}  \tag{4.35}\\
I_{-, B} & =u_{P}-\frac{2 a_{P}}{\gamma-1} \tag{4.36}
\end{align*}
$$

Adding and subtracting these relations yields

$$
\begin{align*}
& u_{P}=\frac{1}{2}\left(I_{+, A}+I_{-, B}\right)  \tag{4.37}\\
& a_{P}=\frac{\gamma-1}{4}\left(I_{+, A}-I_{-, B}\right) \tag{4.38}
\end{align*}
$$

In this way, the solution is propagated through the domain by tracing characteristics and combining the information they carry. To make this process concrete, suppose that the solution is known along an initial curve in the ( $x, t$ ) plane (for example, at $t=0$ ). From each point on this curve, one may trace out the $C_{+}$and $C_{-}$characteristics using the local values of $u$ and $a$.

The intersections of these characteristic curves define new points in the domain at which the solution may be computed. At such an intersection point $P$, one identifies the points $A$ and $B$ from which the $C_{+}$and $C_{-}$characteristics originate, and uses the relations (4.37)-(4.38) to determine the state at $P$.

Once the solution has been computed at a new set of points, these points may in turn be used to generate additional characteristics, allowing the solution to be extended progressively into the domain. In this sense, the method of characteristics constructs the solution by repeatedly seeding characteristics from known data, computing their intersections, and propagating the resulting information forward in spacetime. This procedure is commonly referred to as marching via the method of characteristics, reflecting the step-by-step construction of the solution through characteristic propagation.

Coupling across discontinuities. When a discontinuity is present, this characteristic-based construction must be supplemented by additional constraints. At a contact surface, velocity and pressure remain continuous, while at a shock the Rankine-Hugoniot conditions enforce conservation across the moving interface. These relations connect the states on either side of the discontinuity, but do not, in general, determine the interface location or adjacent states independently.

The key point is that the solution in the smooth region and the conditions at the interface are coupled. The state approaching the interface depends on how information is propagated through the domain, while the interface conditions depend on the state that arrives there.

A coupled viewpoint. To make this coupling concrete, consider a situation in which a smooth region is adjacent to a moving interface, across which the solution is discontinuous. Suppose that the solution is known along a curve in the smooth region and can be propagated toward the interface using the method of characteristics. However, the state at the interface and the interface speed itself are not known a priori.

Let us denote by ( $u_{-}, a_{-}$) the state approaching the interface from the smooth region, obtained by propagating information along characteristics, and by ( $u_{+}, a_{+}, \rho_{+}$) the state immediately across the interface. The interface speed $u_{s}$ is also unknown. Collecting these into a vector of unknowns,

$$
\begin{equation*}
\mathbf{q}=\left(u_{-}, a_{-}, u_{+}, a_{+}, \rho_{+}, u_{s}\right) \tag{4.39}
\end{equation*}
$$

we observe that these quantities are not independent: they must satisfy both the compatibility relations used to propagate ( $u_{-}, a_{-}$) to the interface and the jump conditions that relate the states on either side.

These constraints may be expressed through a residual

$$
\begin{equation*}
R(\mathbf{q})=0 \text {, } \tag{4.40}
\end{equation*}
$$

which measures the inconsistency between the propagated state from the smooth region and the state required by the interface conditions. For example, $R$ may represent the mismatch in the Rankine-Hugoniot relations when evaluated using the incoming state ( $u_{-}, a_{-}$) and a candidate downstream state ( $u_{+}, a_{+}, \rho_{+}$) and interface speed $u_{s}$.

A consistent solution is obtained by adjusting $\mathbf{q}$ so that the state arriving at the interface from the smooth region agrees with the state required by the jump conditions. In practice, one begins with a guess for the interface state and speed, propagates the solution from the known region up to the interface using characteristics, evaluates the residual $R(\mathbf{q})$, and updates the guess until the residual is reduced to zero. In this way, the interface location and adjacent flow states are determined simultaneously as part of a coupled system.

Connection to the shock-tube solution. In the shock-tube problem, this coupling reduces to a single scalar equation for the pressure $p_{*}$, obtained by matching the expansion-fan and shock relations. Because of the special structure of that problem, the solution can be obtained directly without iteration. In more general flows, however, the coupling is not reducible in this way, and the interface location and adjacent states must be determined as part of a coupled system.

Summary. The method of characteristics provides a mechanism for propagating information through smooth regions, while conservation laws govern the behavior at discontinuities. The solution of general unsteady problems requires these elements to be combined so that the flow field and the motion of interfaces are determined simultaneously in a consistent framework.

