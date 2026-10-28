## 1 Why PDEs?

Up to this point in the course, we have taken a deliberately careful route to the governing equations of compressible flow. We began with integral conservation laws for mass, momentum, and energy, expressed over arbitrary control volumes, and emphasized their physical meaning as statements about extensive quantities carried by the fluid. Those laws are exact, global, and conceptually transparent.

This naturally raises a question:
If the integral conservation laws are the physical truth, why do we ever rewrite them as partial differential equations?

The answer is not that PDEs are "more fundamental," but that they allow us to ask different kinds of questions. Writing the governing equations in PDE form exposes the local structure of the flow: how variations in space and time are coupled, how information propagates, and how disturbances interact. It also provides the framework needed for classification (hyperbolic versus elliptic behavior), for analytical tools such as characteristic analysis, and for numerical computation.

In this lecture, our goal is not to derive new physics, but to understand which PDEs we are actually solving, how different forms of the equations encode different physical viewpoints, and why those distinctions matter once smoothness is lost.

## 2 Conservative PDEs as a local restatement of integral conservation

From Lectures $3-4$ and Homework 1, you already know that the integral conservation laws imply the following pointwise equations for inviscid compressible flow:

$$
\begin{gathered}
\partial_{t} \rho+\nabla \cdot(\rho \boldsymbol{u})=0, \\
\partial_{t}(\rho \boldsymbol{u})+\nabla \cdot(\rho \boldsymbol{u} \otimes \boldsymbol{u})=-\nabla p+\rho \boldsymbol{f}, \\
\partial_{t}(\rho E)+\nabla \cdot((\rho E+p) \boldsymbol{u})=\rho \boldsymbol{f} \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h},
\end{gathered}
$$

Some notes on the energy equation. The first two terms on the righthand side are familiar from the integral conservation laws, and represent work due to body forces and heat flux, respectively. Note that we now are also allowing for a volumetric heat transfer term (source/sink), $\dot{q}_{h}$, in the energy equation. This term was omitted in the integral form (but could be added!), and we incorporate it here to allow for slightly more generality. We will refer to these as the conservative form of the governing equations. Remember, as mentioned in the lectures $3-4$ notes, we are dropping the superscript $(\cdot)^{E}$ with the understanding that all quantities are expressed in Eulerian form unless otherwise stated.

These pointwise equations should be understood as a compact rewriting of the integral balance laws you derived earlier (divergence theorem + "holds for all control volumes"). For smooth fields, the conservative PDEs are exactly equivalent to the integral conservation laws. When fields are not smooth, it is the integral statements that remain fundamental; conservative PDEs are then interpreted through those integral balances rather than as classical pointwise differential identities.

## 3 Non-conservative (primitive) form: rewriting in terms of material derivatives

The conservative form is directly tied to conservation, but it is not always the most transparent form for physical interpretation. In particular, it does not explicitly isolate the acceleration of a moving fluid element. When the fields are smooth, we can reorganize the same equations into a material-derivative form that reads like Newton's second law along a particle path.

### 3.1 Primitive form of the governing equations

Assuming sufficient smoothness, the Euler equations may be written in the following nonconservative (primitive) form:

$$
\begin{aligned}
& \frac{D \rho}{D t}+\rho \nabla \cdot \boldsymbol{u}=0 \\
& \rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f} \\
& \rho \frac{D e}{D t}=-p \nabla \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h}
\end{aligned}
$$

Here $\frac{D(\cdot)}{D t}=\partial_{t}(\cdot)+\boldsymbol{u} \cdot \nabla(\cdot)$ is the material derivative you have already come to know and love.

### 3.2 Derivation (momentum): how the material acceleration appears

To illustrate the process, we derive the primitive momentum equation from the conservative momentum equation, highlighting exactly where product rules and continuity enter. The approach for the other governing equations (mass, energy) is entirely analogous.
Start from conservative momentum:

$$
\partial_{t}(\rho \boldsymbol{u})+\nabla \cdot(\rho \boldsymbol{u} \otimes \boldsymbol{u})=-\nabla p+\rho \boldsymbol{f}
$$

Expand the two left-hand terms using product rules:

$$
\partial_{t}(\rho \boldsymbol{u})=\rho \partial_{t} \boldsymbol{u}+\boldsymbol{u} \partial_{t} \rho,
$$

and

$$
\nabla \cdot(\rho \boldsymbol{u} \otimes \boldsymbol{u})=\rho(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}+\boldsymbol{u} \nabla \cdot(\rho \boldsymbol{u}) .
$$

Substituting these expansions yields

$$
\rho \partial_{t} \boldsymbol{u}+\rho(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}+\boldsymbol{u}\left(\partial_{t} \rho+\nabla \cdot(\rho \boldsymbol{u})\right)=-\nabla p+\rho \boldsymbol{f}
$$

Now invoke continuity in conservative form,

$$
\partial_{t} \rho+\nabla \cdot(\rho \boldsymbol{u})=0
$$

to remove the final term, leaving

$$
\rho\left(\partial_{t} \boldsymbol{u}+(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}\right)=-\nabla p+\rho \boldsymbol{f}
$$

Recognizing the material derivative,

$$
\frac{D \boldsymbol{u}}{D t}=\partial_{t} \boldsymbol{u}+\boldsymbol{u} \cdot \nabla \boldsymbol{u}
$$

we obtain the primitive momentum equation

$$
\rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f}
$$

Interpretation. The conservative momentum equation is already a correct statement of momentum balance, including pressure and body forces. What the primitive form adds is not new physics but a new organization: it rewrites the left-hand side as "mass density × material acceleration," which makes the equation read like Newton's second law along a fluid particle path. That re-organization required product rules and the continuity equation, and therefore relies on smoothness.

## 4 Interpretation of the governing equations at discontinuities

The distinction between conservative and non-conservative forms becomes essential once the flow is no longer smooth; e.g. when shocks are present. The issue is not whether derivatives exist pointwise, but whether the equations retain a clear physical interpretation when smoothness is lost.

### 4.1 Conservative form as a boundary-flux statement

Consider the conservative momentum equation written abstractly as

$$
\partial_{t}(\rho \boldsymbol{u})+\nabla \cdot \mathbf{F}=\rho \boldsymbol{f}, \quad \mathbf{F}:=\rho \boldsymbol{u} \otimes \boldsymbol{u}+p \mathbf{I} .
$$

This equation is designed to mirror the structure of the integral momentum balance. When applied to a control volume $\Omega$, it is interpreted as:

$$
\text { rate of change of momentum inside } \Omega+\text { net flux of } \mathbf{F} \text { across } \partial \Omega=\text { body forces. }
$$

In smooth flows, this interpretation can be justified by applying the divergence theorem to the flux term. However, the crucial point is that this boundary-flux interpretation does not depend on classical differentiability. When discontinuities such as shocks are present, the symbol $\nabla \cdot \mathbf{F}$ is not evaluated pointwise. Instead, it is understood directly through its defining physical meaning: the net flux of momentum carried by $\mathbf{F}$ through the boundary of the control volume.
In this sense, the conservative form provides a direct pathway from the local PDE notation back to the integral conservation law, even when smoothness is lost. The integral balance is the fundamental statement, and the conservative PDE is a compact way of encoding that statement locally.

### 4.2 Why the non-conservative form does not admit the same interpretation

Now consider the primitive (non-conservative) momentum equation,

$$
\rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f}, \quad \frac{D \boldsymbol{u}}{D t}=\partial_{t} \boldsymbol{u}+\boldsymbol{u} \cdot \nabla \boldsymbol{u} .
$$

This equation describes the acceleration of a material fluid element. Its left-hand side is expressed entirely in terms of the motion of individual particles, not in terms of fluxes across surfaces. As a result, there is no immediate way to interpret this equation as a statement about the exchange of momentum between a control volume and its surroundings.

When the fields are smooth, algebraic manipulations reconnect this form to the conservative one, allowing it to inherit a flux interpretation indirectly. But that connection relies on smoothness. Once discontinuities appear, there is no longer a well-defined notion of particle acceleration at the jump, and no direct way to associate the left-hand side with a momentum flux through the boundary of a control volume.

### 4.3 Consequence

The key distinction is therefore interpretive rather than algebraic.
The conservative form is constructed so that, even in the presence of discontinuities, it can be interpreted as a balance between rates of change inside a control volume and fluxes through its boundary, by reverting to its integral meaning. The non-conservative form lacks such a pathway: it encodes smooth-flow particle dynamics, not control-volume transport.

For this reason, conservative form is the appropriate representation of the governing equations whenever shocks or other discontinuities are present, while non-conservative form is best viewed as a smooth-flow convenience that must be used with care.

## 5 Energy equations in multiple forms (with short derivations)

We now record a few standard differential forms of the energy equation. These are not different physical laws; they are different ways of grouping the same conservation statement.

### 5.1 Conservative total-energy form

The conservative energy equation (from Section 1) is

> [!equation]
> 
> $$
> \partial_{t}(\rho E)+\nabla \cdot((\rho E+p) \boldsymbol{u})=\rho \boldsymbol{f} \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h}, \quad E=e+\frac{1}{2}|\boldsymbol{u}|^{2} .
> $$
> 

### 5.2 Primitive internal-energy form

Assume smooth fields and expand the conservative energy equation into a form following the motion of a fluid element.

First expand the flux term:

$$
\nabla \cdot((\rho E+p) \boldsymbol{u})=\nabla \cdot(\rho E \boldsymbol{u})+\nabla \cdot(p \boldsymbol{u}) .
$$

Use the identity (valid for smooth fields)

$$
\partial_{t}(\rho E)+\nabla \cdot(\rho E \boldsymbol{u})=\rho \frac{D E}{D t},
$$

which follows from product rules together with continuity. Then the energy equation becomes

$$
\rho \frac{D E}{D t}+\nabla \cdot(p \boldsymbol{u})=\rho \boldsymbol{f} \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h} .
$$

Next expand $\nabla \cdot(p \boldsymbol{u})=p \nabla \cdot \boldsymbol{u}+\boldsymbol{u} \cdot \nabla p$ :

$$
\rho \frac{D E}{D t}+p \nabla \cdot \boldsymbol{u}+\boldsymbol{u} \cdot \nabla p=\rho \boldsymbol{f} \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h} .
$$

Now split $E=e+\frac{1}{2}|\boldsymbol{u}|^{2}$ :

$$
\rho \frac{D e}{D t}+\rho \frac{D\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)}{D t}+p \nabla \cdot \boldsymbol{u}+\boldsymbol{u} \cdot \nabla p=\rho \boldsymbol{f} \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h} .
$$

Use $\frac{D\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)}{D t}=\boldsymbol{u} \cdot \frac{D \boldsymbol{u}}{D t}$ and substitute the primitive momentum equation $\rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f}$ dotted with $\boldsymbol{u}$ :

$$
\rho \boldsymbol{u} \cdot \frac{D \boldsymbol{u}}{D t}=-\boldsymbol{u} \cdot \nabla p-\nabla \cdot \boldsymbol{q}_{h}+\rho \boldsymbol{f} \cdot \boldsymbol{u} .
$$

This cancels the $\boldsymbol{u} \cdot \nabla p$ term and the $\rho \boldsymbol{f} \cdot \boldsymbol{u}$ term, leaving


> [!equation] Internal-Energy form of the Energy Equations
> 
> $$
> \rho \frac{D e}{D t}=-p \nabla \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h} .
> $$
> 
> 


This is the primitive internal-energy equation. Take a second to appreciate how this form of the energy equation looks different than the integral variant we encountered in lectures 3-4.

The integral energy equation emphasizes transport. It tracks how energy enters and leaves a control volume through boundary fluxes, and for this reason enthalpy naturally appears as part of the energy flux carried by flowing mass. From this viewpoint, enthalpy packages internal energy together with the pressure work required to displace surrounding fluid as mass crosses a boundary.

In contrast, the primitive internal-energy equation follows a material fluid element. Because the control volume moves with the fluid, there is no advective transport across its "boundary". The equation therefore contains no flux terms. Instead, internal energy is entirely modulated by work and heat transfer mechanisms. The former uses pressure as a way of applying work when the element compresses or expands, and the latter allows for internal energy change under heat transfer.

### 5.3 Enthalpy form

Define enthalpy $h:=e+p / \rho$. Differentiate along a particle path:

$$
\frac{D h}{D t}=\frac{D e}{D t}+\frac{D\left(\frac{p}{\rho}\right)}{D t}=\frac{D e}{D t}+\frac{1}{\rho} \frac{D p}{D t}-\frac{p}{\rho^{2}} \frac{D \rho}{D t}
$$

Multiply by $\rho$ and use continuity in primitive form $\frac{D \rho}{D t}=-\rho \nabla \cdot \boldsymbol{u}$ :

$$
\rho \frac{D h}{D t}=\rho \frac{D e}{D t}+\frac{D p}{D t}+p \nabla \cdot \boldsymbol{u}
$$

Substitute the internal-energy equation $\rho \frac{D e}{D t}=-p \nabla \cdot \boldsymbol{u}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h}$ to obtain

> [!equation] Enthalpy Form of the Energy Equation
> $$
> \rho \frac{D h}{D t}=\frac{D p}{D t}-\nabla \cdot \boldsymbol{q}_{h}+\rho \dot{q}_{h} .
> $$
> 

This form is especially convenient in problems where pressure and enthalpy are more natural state variables than internal energy. This variant of the energy equation represents yet another reorganization of the same physics. Here, enthalpy is treated not as the flux mechanism of transport, but as a primary thermodynamic state variable. Cast in that light, the equation tells us that its evolution along a particle path is governed by pressure changes and heat input.

Please remember that none of these forms represent different laws. They are different lenses on the same conservation principle, each suited to a different physical question: transport across boundaries, or evolution along particle trajectories. Even in the latter, we can ask for transport of distinct variables based on what a given situation calls for, realizing that we are not generating independent governing equations in these reformulations.

## 6 Why conservation laws alone are not enough: thermodynamic closure

The Euler equations for inviscid compressible flow consist of five conservation laws:

- conservation of mass ( 1 equation),
- conservation of linear momentum ( 3 equations),
- conservation of total energy ( 1 equation).

In three spatial dimensions, these provide a total of five partial differential equations.
At first glance, however, the system appears to involve six unknown fields:

$$
\rho, \quad \mathbf{u}, \quad E, \quad p .
$$

Density and total energy are scalar fields, velocity has three components, and pressure appears explicitly in the momentum and energy fluxes.

### 6.1 State variables and dependent variables

In practice, we regard the five conserved quantities

$$
\rho, \quad \rho \mathbf{u}, \quad \rho E
$$

as defining the state of the flow. Equivalently, the state may be expressed in terms of

$$
\rho, \quad \mathbf{u}, \quad E .
$$

Among these variables, at least two are thermodynamic in nature: density $\rho$ and the internal energy component of $E$. The velocity field describes kinematics, while density and internal energy describe the thermodynamic state of the material.

Pressure $p$ appears in the governing equations as a mechanical forcing term. For example, in primitive form,

$$
\rho \frac{D \mathbf{u}}{D t}=-\nabla p+\rho \mathbf{f},
$$

so that $-\nabla p$ acts as a force per unit volume. However, unlike a body force $\mathbf{f}$, pressure is not externally prescribed. It is determined by the thermodynamic state of the fluid itself.

This situation is analogous to viscous stresses in the Navier-Stokes equations: they appear as forces in the momentum balance, yet they are expressible in terms of velocity gradients through a constitutive law. Similarly, pressure is a thermodynamic variable that must be related to the thermodynamic state variables.

### 6.2 The need for a thermodynamic model

For a simple compressible substance, thermodynamics tells us that the state is fully determined by two independent thermodynamic variables. Common choices include $(\rho, e),(\rho, T)$, or $(p, s)$. Consequently, pressure can always be written as a function of two independent thermodynamic variables. We choose to express pressure in terms of whatever thermodynamic variables are a part of our flow state. These state variables almost always involve density and whatever our primary energy variable is. If working with the internal energy form of the energy equation, we would write

$$
p=p(\rho, e)
$$

Providing this relation is what is meant by thermodynamic closure. The conservation laws describe how mass, momentum, and energy are transported and balanced. The thermodynamic model specifies how pressure responds to the thermodynamic state.
In general, this model may consist of a collection of algebraic relations, such as:

- an equation of state (relating $p, \rho$, and $T$ ),
- a caloric relation (relating internal energy to temperature),
- definitions connecting material constants (e.g. $c_{p}-c_{v}=R$ ).

Together, these relations allow pressure to be expressed in terms of the chosen state variables.

### 6.3 Example: calorically perfect ideal gas

Suppose the energy equation is written in terms of internal energy $e$. For a calorically perfect ideal gas, the thermodynamic model consists of:

$$
p=\rho R T, \quad e=c_{v} T, \quad c_{p}-c_{v}=R, \quad \gamma=\frac{c_{p}}{c_{v}} .
$$

Eliminating $T$ from the first two relations gives

$$
p=\rho R\left(\frac{e}{c_{v}}\right)=\rho e \frac{R}{c_{v}}
$$

Using $R=c_{p}-c_{v}$ and $\gamma=c_{p} / c_{v}$, we obtain

$$
\frac{R}{c_{v}}=\gamma-1
$$

and therefore

$$
p=(\gamma-1) \rho e .
$$

Thus, for a calorically perfect ideal gas, pressure is an explicit algebraic function of density and internal energy. In principle, one may substitute this expression directly into the momentum
and energy equations, eliminating $p$ entirely and writing the system solely in terms of the state variables.

In practice, it is often preferable to leave $p$ symbolically in the fluxes and evaluate it from the state at each point. This preserves the structural clarity of the equations and allows the thermodynamic model to be modified independently of the conservation-law framework.

### 6.4 More general thermodynamic models.

For more complex gases, the thermodynamic closure may be more involved. Examples include:

- thermally imperfect gases, where $c_{v}$ depends on temperature and $e=e(T)$ must be inverted numerically,
- real-gas equations of state, where $p=p(\rho, T)$ is nonlinear,
- multi-species or reacting flows, where additional transport equations and composition-dependent thermodynamic relations are required.

In all cases, the structure remains the same:

- conservation laws govern transport and balance,
- thermodynamic relations provide constitutive closure,
- together they determine the evolution of the flow.


## 7 Looking ahead

In this lecture, we have seen that the governing equations of compressible flow admit multiple PDE representations, all descending from the same integral conservation laws. Smoothness allows us to reorganize those equations into intuitive, Newtonian forms, while discontinuities force us to return to the more fundamental flux viewpoint embedded in the integral balances.

In the next lecture, we will build on this foundation to identify quantities that are conserved or transported in special ways, and to understand how thermodynamics shapes the propagation of information in compressible flows.

