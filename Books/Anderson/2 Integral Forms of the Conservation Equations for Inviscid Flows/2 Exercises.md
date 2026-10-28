# Chapter 2 Exercises

This file collects the exercise callouts from `2 Integral Forms of the Conservation Equations for Inviscid Flows.md`.


# Exercise 2.1 Flow Modeling Approaches and Their Role in Aerodynamic Analysis


> [!exercise] Exercise 2.1 - Flow Modeling Approaches and Their Role in Aerodynamic Analysis
> Consider the general problem of determining the aerodynamic forces, moments, and heat transfer on a body immersed in a fluid flow - for example, a supersonic missile, a submarine, or a tall building in a storm.
> (a) Explain why computing the complete flowfield (i.e., the distributions of $p, p, T, \mathrm{~V}$, etc., at all points in the flow) is a necessary step toward obtaining practical engineering quantities such as lift, drag, and surface heat transfer. In your answer, describe the logical chain from flowfield solution to aerodynamic forces.
> (b) The derivation of the governing equations of fluid motion follows a three-step procedure. State each step clearly, identifying the role of physical laws, flow models, and mathematical extraction.
> (c) Three distinct modeling approaches can be used to derive the equations of fluid motion:
> (i) the finite control volume approach,
> (ii) the infinitesimal fluid element approach, and
> (iii) the molecular (kinetic theory) approach.
> 
> For each approach, briefly describe the model and state whether it leads directly to integral equations, differential equations, or a statistical/kinetic formulation. Also note whether the model can be applied in either a fixed or moving reference frame, and what difference this choice makes.
> (d) Within the finite control volume approach, distinguish between a control volume that is fixed in space and one that moves with the fluid. For the fixed control volume, explain physically why both a surface integral (flux) term and a volume integral (time-rate-ofchange) term appear in the resulting conservation equations. Which of these two formulations is adopted in this chapter, and why might consistency in model choice be important?



## 2.1.a

Computing lift, drag, moments, and surface heat transfer is ultimately a matter of evaluating surface integrals over the body, but the integrands in those surface integrals are not “known” a priori. They are determined by the local state of the fluid in the immediate neighborhood of the surface, which is itself part of the global flowfield. In that sense, the “engineering quantities” are downstream outputs of the flow solution, not independent inputs.

The logical chain is: solve for the flowfield variables (at minimum the spatial distributions of pressure $p(\mathbf{x},t)$, density $\rho(\mathbf{x},t)$, velocity $\mathbf{V}(\mathbf{x},t)$, and temperature $T(\mathbf{x},t)$, together with any constitutive relations such as an equation of state), then restrict those fields to the body surface to obtain the surface loads and heat flux, and finally integrate those surface quantities to obtain the net force, moment, and heat transfer.

More explicitly, the fluid exerts on the body a traction (force per unit area) that depends on the local stress state at the surface. Writing $\mathbf{n}$ for the outward-pointing unit normal on the body surface $S_B$, the surface traction on the body can be written as
$$
\mathbf{t} = -p\,\mathbf{n} + \boldsymbol{\tau}\,\mathbf{n},
$$
where $p$ is the pressure evaluated at the wall and $\boldsymbol{\tau}$ is the viscous stress tensor (whose value at the wall depends on velocity gradients in the near-wall flow). The net aerodynamic force on the body is then obtained by integrating this traction over the entire surface,
$$
\mathbf{F}=\iint_{S_B}\left(-p\,\mathbf{n}+\boldsymbol{\tau}\,\mathbf{n}\right)\,dS,
$$
(plus any body-force contribution if one is being included in the model). Lift and drag are not new physics; they are simply components of $\mathbf{F}$ along prescribed directions (for example, “drag” is the component opposite the free-stream direction and “lift” is the component perpendicular to it in the chosen plane). The aerodynamic moment about a reference point with position vector $\mathbf{r}_0$ is obtained from the same surface traction via
$$
\mathbf{M}_{\mathbf{r}_0}=\iint_{S_B}\left(\mathbf{r}-\mathbf{r}_0\right)\times\left(-p\,\mathbf{n}+\boldsymbol{\tau}\,\mathbf{n}\right)\,dS,
$$
so even the sign and magnitude of the pitching/yawing/rolling moments depend on the detailed spatial distribution of pressure and shear over the body.

Surface heat transfer likewise depends on near-wall information contained in the flowfield. At the wall, the heat flux into the fluid is given (in a Fourier-law description) by
$$
q''=-k\left(\frac{\partial T}{\partial n}\right)_{w},
$$
where $q''$ is the heat transfer rate per unit area, $k$ is the thermal conductivity, and $\partial T/\partial n$ is the temperature gradient normal to the wall (evaluated at the wall). Determining that gradient requires the temperature field in the boundary layer adjacent to the surface, which is again part of the flow solution.

Therefore, without a flowfield solution one cannot determine the surface distributions $p|_{S_B}$, $\boldsymbol{\tau}|_{S_B}$, or $(\partial T/\partial n)_w$, and without those distributions one cannot evaluate the surface integrals that define the net forces, moments, and heat transfer. In inviscid-flow modeling, the same chain remains, but it simplifies because $\boldsymbol{\tau}=\mathbf{0}$, so aerodynamic forces and moments come entirely from the pressure distribution; that pressure distribution is still a global outcome of the flowfield and must be computed.

## 2.1.b

The first step is to state the physical principles that the fluid motion must satisfy. For the “governing equations” of classical fluid mechanics, these are the fundamental balance laws: conservation of mass, Newton’s second law applied to a material amount of fluid (conservation of momentum in the absence of relativistic effects), and the first law of thermodynamics (conservation of energy, including heat and work interactions). These principles are not yet equations for $p(\mathbf{x},t)$, $\rho(\mathbf{x},t)$, $\mathbf{V}(\mathbf{x},t)$, and $T(\mathbf{x},t)$; they are statements about how mass, momentum, and energy of a chosen amount of fluid can change.

The second step is to choose a flow model that makes those physical principles usable. In Anderson’s development, this means selecting the object to which the laws are applied (for example, a finite control volume with a defined control surface, or an infinitesimal fluid element) and adopting the continuum hypothesis so that field variables such as $\rho$, $\mathbf{V}$, $p$, and $T$ are well-defined functions of space and time. This modeling step also includes the mechanical and thermodynamic idealizations that determine what forces and energy-transfer mechanisms are retained (for example, inviscid versus viscous stresses, whether body forces are included, and what form of equation of state and caloric relations are assumed). Step 2 therefore specifies what physics is in the model and what is deliberately neglected.

The third step is mathematical extraction: translate the physical balance statements, applied to the chosen model, into explicit integral and/or differential equations for the flowfield variables. For a finite control volume formulation, each balance is written as an “accumulation in the control volume” term plus a “net flux through the control surface” term, equated to the appropriate source terms (body forces, pressure forces, heat addition, and work). A compact template for any extensive property $B$ is
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho b\,d\mathscr{V}+\iint_{S}\rho b\,\mathbf{V}\cdot d\mathbf{S}=\text{(sources of $B$ acting on the control volume)},
$$
where $b$ is the corresponding intensive property per unit mass (so that $B=\iiint_{\mathscr{V}}\rho b\,d\mathscr{V}$). Choosing $b=1$ yields continuity, choosing $b=\mathbf{V}$ together with the appropriate force model yields momentum, and choosing $b=e+V^{2}/2$ together with heat/work models yields energy. If desired, one can then use identities such as the divergence theorem and a limiting process on the control volume to convert these integral statements into differential equations; in any case, the outcome of Step 3 is an explicit set of governing equations (plus constitutive/closure relations) that can be solved for the complete flowfield.

## 2.1.c

(i) In the finite control volume approach, the fluid is modeled as a continuum filling a finite region of space (the control volume) bounded by a closed control surface. One applies the fundamental conservation principles to that finite region, carefully accounting for what crosses the boundary and what accumulates inside. This approach leads naturally and directly to integral equations: the continuity, momentum, and energy equations written as surface and volume integrals over the chosen control surface and control volume. If one wishes, the differential forms can then be obtained as a secondary step by shrinking the control volume to an infinitesimal size and using vector-calculus identities; however, the primary product of the control-volume model is the integral conservation laws.

The control volume may be fixed in space (Eulerian control volume) or it may move and deform with the fluid (a material or Lagrangian control volume). The mathematical difference is that a fixed control volume produces equations with explicit flux terms across the stationary surface (because fluid crosses the boundary), whereas a material control volume eliminates convective flux through the boundary by construction (the boundary is made of the same fluid particles), leaving only time rates of change of the extensive properties of that same material mass. Physically, the choice changes whether the “bookkeeping” of conservation is done by tracking what enters/leaves a region in space (fixed control volume) or by tracking the same fluid as it moves (moving control volume).

(ii) In the infinitesimal fluid element approach, one assumes the continuum model and focuses on an infinitesimally small fluid element (a differential control volume) with dimensions $dx$, $dy$, $dz$. The conservation laws are applied to that differential element and then divided by its volume, followed by the limiting process $dx,dy,dz\to 0$. This approach leads directly to differential equations (partial differential equations) for the field variables, such as the differential continuity equation, the Euler or Navier–Stokes equations (depending on whether viscous stresses are included), and the differential energy equation. The emphasis is on local, pointwise statements: how the variables change at a point in space and time in response to local gradients and sources.

As with the finite control volume, the differential element can be viewed in a fixed spatial frame (Eulerian description) or one can follow a moving element (Lagrangian description). In practice, most “differential form” presentations are written in an Eulerian frame but include material-derivative terms that already encode the option to interpret the equations along a moving fluid particle. The key distinction is again whether one is describing changes at a fixed location or changes experienced by a moving fluid element.

(iii) In the molecular (kinetic theory) approach, the fluid is not taken as a continuum at the outset. Instead, one models the gas as a very large number of molecules whose motion is described statistically (for example, through a molecular velocity distribution function). Conservation laws emerge as moment equations of that distribution, and transport properties such as viscosity and thermal conductivity arise from molecular collisions and mean-free-path effects. The primary output is therefore a statistical/kinetic formulation (e.g., the Boltzmann equation and its moments), from which the familiar continuum equations can be derived in appropriate limits (such as near-equilibrium, small Knudsen number). In this model, the distinction between fixed and moving frames is handled at the level of molecular velocities and distribution functions; the macroscopic conservation laws that are extracted are frame-invariant in content, but the practical form of the equations depends on how one defines macroscopic velocity (mean molecular velocity) relative to the chosen reference frame.

## 2.1.d

In the finite control volume approach, a control volume is a chosen region of space, denoted here by $\mathscr{V}$, bounded by a closed control surface $S$ with outward unit normal $\mathbf{n}$. A control volume that is fixed in space is a stationary region: $\mathscr{V}$ and $S$ do not move, and the fluid with velocity field $\mathbf{V}(\mathbf{x},t)$ can flow into and out of the region across $S$. In contrast, a control volume that moves with the fluid is a material (Lagrangian) volume: the boundary is imagined to move and deform so that it is always made up of the same fluid particles. In that case, no fluid crosses the boundary by construction; the “contents” of the control volume are a fixed mass of fluid that is simply carried along by the motion.

The reason a fixed control volume produces both a surface integral (flux) term and a volume integral (time-rate-of-change) term is that there are two distinct physical mechanisms by which the amount of some conserved quantity inside a *stationary* region can change. First, the amount stored inside the region can change with time because the flow is unsteady; this is an accumulation (or depletion) effect that is captured by a time derivative of a volume integral over $\mathscr{V}$. Second, even if the region itself does not change, the quantity can be carried into or out of the region by the moving fluid crossing the boundary; this transport is a flux effect that is captured by a surface integral over $S$.

For example, for mass conservation in a fixed control volume, the mass inside the region at time $t$ is $\iiint_{\mathscr{V}}\rho\,d\mathscr{V}$, so the unsteady storage term is $\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,d\mathscr{V}$. The net rate at which mass leaves the control volume through the control surface is $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$, where $d\mathbf{S}=\mathbf{n}\,dS$. Conservation of mass then demands that these two effects balance (with sign determined by the outward-normal convention),
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,d\mathscr{V}+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}=0.
$$
If the flow is steady, the stored mass in any fixed region does not change with time, so the volume term vanishes and the remaining statement is that the net mass flux out of the control surface is zero.

If instead one uses a control volume that moves with the fluid, the flux term across the boundary disappears because there is no flow through the moving surface; the conservation statements are written as time rates of change of properties of a fixed material mass. The price one pays is that the boundary motion has to be tracked, which is often inconvenient for engineering applications.

The formulation adopted in this chapter is the fixed finite control volume approach: the remainder of the chapter derives the integral continuity, momentum, and energy equations by applying the physical principles to a stationary control volume with fluid flowing through it. Consistency in model choice matters because the structure and interpretation of the terms depend on whether the boundary is fixed or moving. Mixing a material-volume form for one conservation law with a fixed-control-volume form for another forces you to continually translate between “rate of change following the fluid” and “rate of change in a region of space,” which is exactly where sign errors, missing convective-flux terms, and inconsistent boundary-condition statements tend to appear. Using one control-volume model throughout keeps the bookkeeping uniform: every equation is expressed as “accumulation in $\mathscr{V}$ plus net flux through $S$ equals sources,” so the resulting set of equations closes cleanly on the same set of flowfield variables and is applied with a single, coherent geometric picture.








# Exercise 2.2 Derivation of the Integral Conservation Equations for a Fixed Control Volume

> [!exercise] Exercise 2.2 Derivation of the Integral Conservation Equations for a Fixed Control Volume
> Consider a fixed control volume $\mathscr{V}$ bounded by a closed control surface $S$ immersed in a general fluid flow, as shown in Fig. 2.4. At any point on the surface, let $\mathbf{n}$ be the outwardpointing unit normal, $d \mathbf{S}=\mathbf{n} d S$, and let $\rho$ and $\mathbf{V}$ denote the local density and velocity, respectively.
> (a) Starting from the physical principle that mass can be neither created nor destroyed, show that the mass flow through an elemental surface $d S$ is $\dot{m}=\rho \mathbf{V} \cdot d \mathbf{S}$. Then, by considering the net mass flux through the entire control surface and the time rate of change of mass stored within $\mathscr{V}$, derive the integral form of the continuity equation:
> 
> $$
> \frac{\partial}{\partial t} \iiint_{\mathscr{V}} \rho\, d\mathscr{V}+\iint_S \rho \mathbf{V} \cdot d \mathbf{S}=0
> $$
> 
> 
> Explain why the surface integral alone, without the time-derivative term, is sufficient for steady flows.
> (b) Now consider Newton's second law in the form $d(m \mathbf{V}) / d t=\mathbf{F}$. For the same fixed control volume, identify the two contributions to the total time rate of change of momentum of the fluid flowing through $\mathscr{V}$ : (i) the net flux of momentum across $S$, and (ii) the time rate of change of momentum stored within $\mathscr{V}$. Write expressions for each.
> (c) For an inviscid flow, the forces acting on the fluid in the control volume consist of body forces (with f denoting body force per unit mass) and surface forces due to pressure $p$. Combine your results from part (b) with these force expressions to derive the integral momentum equation:
> 
> $$
> \frac{\partial}{\partial t} \iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}+\iint_S(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}=\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_S p d \mathbf{S}
> $$
> 
> (d) Explain physically why the pressure term carries a negative sign. How would the momentum equation be modified if viscous effects were included? Write the modified equation and identify the additional term.
> (e) Discuss why the continuity and momentum equations together are sufficient for analyzing incompressible flows, but an additional equation (the energy equation) is needed for compressible flows.
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> Mass Can Be Neither Created Nor Destroyed. Let us apply this principle to the model of a fixed control volume in a flow, as illustrated in Fig. 2.4. The volume is $\mathscr{Z}$, and the area of the closed surface is $S$. First, consider point $B$ on the control surface and an elemental area around $B, d S$. Let $\mathbf{n}$ be a unit vector normal to the surface at $B$. Define $d \mathbf{S}=\mathbf{n} d S$. Also, let $\mathbf{V}$ and $\rho$ be the local velocity and density at $B$.

## 2.2.a

Let $dS$ denote an elemental area on the control surface $S$, and let $\mathbf{n}$ be the outward-pointing unit normal at that location. Define the vector area element as $d\mathbf{S}=\mathbf{n}\,dS$. The fluid velocity at the surface element is $\mathbf{V}$, and its component normal to the surface is
$$
V_n=\mathbf{V}\cdot\mathbf{n}.
$$
Over a short time interval $dt$, the fluid that crosses the surface element sweeps out a thin “slug” whose thickness in the normal direction is $V_n\,dt$; hence the volume that crosses is $(V_n\,dt)\,dS$, and the mass that crosses is
$$
dm=\rho\,(V_n\,dt)\,dS.
$$
Dividing by $dt$ gives the mass flow rate through the elemental area,
$$
\dot m=\frac{dm}{dt}=\rho V_n dS=\rho(\mathbf{V}\cdot\mathbf{n})\,dS=\rho\,\mathbf{V}\cdot d\mathbf{S}.
$$
With the outward normal convention, $\dot m>0$ corresponds to outflow and $\dot m<0$ corresponds to inflow; the same formula handles both cases.

Now consider the entire fixed control volume $\mathscr{V}$ bounded by $S$. The total mass contained inside $\mathscr{V}$ at time $t$ is
$$
M(t)=\iiint_{\mathscr{V}}\rho\,d\mathscr{V}.
$$
The net mass flow rate *out* of the control volume through the closed surface is obtained by summing (integrating) the elemental contributions $\rho\,\mathbf{V}\cdot d\mathbf{S}$ over $S$, i.e.
$$
\dot m_{\text{out}}=\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}.
$$
Mass conservation (“mass can be neither created nor destroyed”) for a fixed control volume says that the rate of increase of mass stored inside equals minus the net outflow. Because $\mathscr{V}$ is fixed in space, the time derivative can be taken directly of the volume integral. Writing this as a single explicit chain of equalities,
$$
\begin{aligned}
0
&=\frac{d}{dt}\Big(M(t)\Big)+\dot m_{\text{out}} \\
&=\frac{d}{dt}\left(\iiint_{\mathscr{V}}\rho\,d\mathscr{V}\right)+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S} \\
&=\frac{\partial}{\partial t}\left(\iiint_{\mathscr{V}}\rho\,d\mathscr{V}\right)+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}.
\end{aligned}
$$
Equivalently,
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,d\mathscr{V}+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}=0,
$$
which is the integral (control-volume) form of the continuity equation.

For a steady flow, the density at each fixed point in space does not change with time, so the total mass inside any fixed control volume is constant in time. Hence $\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,d\mathscr{V}=0$, and the continuity equation reduces to
$$
\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}=0,
$$
which states that the net mass flux out of the closed surface vanishes (total outflow equals total inflow).

## 2.2.b

The linear momentum of the fluid contained inside the fixed control volume $\mathscr{V}$ at time $t$ is the volume integral of momentum density:
$$
\mathbf{P}(t)=\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V}.
$$
Hence the time rate of change of momentum stored within $\mathscr{V}$ (the unsteady accumulation term) is
$$
\left(\frac{d\mathbf{P}}{dt}\right)_{\text{stored}}=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V},
$$
where the partial derivative is used because $\mathscr{V}$ is fixed in space.

The second contribution is the net momentum flux across the control surface $S$. The mass flow rate through an elemental area is $d\dot m=\rho\,\mathbf{V}\cdot d\mathbf{S}$ with $d\mathbf{S}=\mathbf{n}\,dS$, so the momentum flow rate (momentum per unit time) carried through that elemental area is
$$
d\dot{\mathbf{P}}_{\text{flux}}=\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}.
$$
Integrating over the closed surface gives the net momentum flux out of the control volume,
$$
\left(\frac{d\mathbf{P}}{dt}\right)_{\text{flux,out}}=\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}.
$$
With the outward-normal convention, inflow portions contribute automatically with $\mathbf{V}\cdot d\mathbf{S}<0$.

Therefore, for a fixed control volume, the total time rate of change of momentum of the fluid “associated with” the flow through $\mathscr{V}$ is represented by the sum of these two contributions:
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V}+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}.
$$

## 2.2.c

For inviscid flow, Newton’s second law for the fluid in the control-volume formulation states that the instantaneous time rate of change of momentum of the fluid “associated with” the fixed control volume equals the net force exerted on that fluid. From part (b), the left-hand side is the sum of the unsteady storage term and the net momentum flux through the control surface:
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V}+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}.
$$

The forces on the fluid in $\mathscr{V}$ consist of (i) body forces and (ii) surface forces. Let $\mathbf{f}$ denote the body force per unit mass (so $\rho\mathbf{f}$ is force per unit volume). Then the total body force acting on the fluid in the volume is
$$
\mathbf{F}_{\text{body}}=\iiint_{\mathscr{V}}\rho\,\mathbf{f}\,d\mathscr{V}.
$$
For inviscid flow, the only surface force is due to pressure. With $d\mathbf{S}=\mathbf{n}\,dS$ defined outward from the control volume, the pressure force on an elemental area is $-p\,d\mathbf{S}$ (pressure acts inward, opposite $d\mathbf{S}$), so the total surface force due to pressure is
$$
\mathbf{F}_{p}=-\iint_{S}p\,d\mathbf{S}.
$$
Hence the net force is $\mathbf{F}=\mathbf{F}_{\text{body}}+\mathbf{F}_{p}$, and assembling the result as an explicit chain gives
$$
\begin{aligned}
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V}+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}
&=\mathbf{F} \\
&=\mathbf{F}_{\text{body}}+\mathbf{F}_{p} \\
&=\iiint_{\mathscr{V}}\rho\,\mathbf{f}\,d\mathscr{V}-\iint_{S}p\,d\mathbf{S}.
\end{aligned}
$$
Equivalently,
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\,d\mathscr{V}+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}
=\iiint_{\mathscr{V}}\rho\,\mathbf{f}\,d\mathscr{V}-\iint_{S}p\,d\mathbf{S},
$$
which is the integral momentum equation for inviscid flow.

## 2.2.d

The pressure term carries a negative sign because of the adopted outward-normal convention for the vector area element $d\mathbf{S}=\mathbf{n}\,dS$. Pressure is a compressive (inward-pointing) normal stress: at a surface element on the control surface, the force exerted on the fluid inside the control volume by the surrounding fluid is directed opposite to $\mathbf{n}$. Hence the elemental pressure force is $d\mathbf{F}_p=-p\,d\mathbf{S}$, and summing over the control surface gives $\mathbf{F}_p=-\iint_{S}p\,d\mathbf{S}$. The minus sign therefore encodes the physical fact that pressure acts inward while $d\mathbf{S}$ points outward.

If viscous effects are included, there is an additional surface force on the control surface due to shear and viscous normal stresses. Denoting this net viscous surface force by $\mathbf{F}_{\text{viscous}}$, the momentum equation becomes
$$
\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}
+\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}
=\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_{S} p\, d \mathbf{S}+\mathbf{F}_{\text{viscous}}.
$$
Here $\mathbf{F}_{\text{viscous}}$ is the additional term: it represents the integral over $S$ of the viscous traction (shear plus viscous normal stress) acting on the fluid at the control surface.

## 2.2.e

For an incompressible flow, the density is constant (or, more precisely, it is treated as constant for the purposes of the analysis), so the mechanical behavior is governed by conservation of mass and conservation of momentum. The continuity equation provides the kinematic constraint on the velocity field (no net volumetric expansion or compression), and the momentum equation relates the acceleration of the fluid to the forces (pressure, body forces, and possibly viscous stresses). In that setting, pressure acts primarily as a Lagrange multiplier that enforces the incompressibility constraint: once suitable boundary conditions are specified, the continuity and momentum equations are sufficient to determine the velocity and pressure fields without separately tracking temperature or internal energy.

For a compressible flow, density is no longer constant; it depends on the thermodynamic state. The continuity and momentum equations alone do not provide enough information to determine the coupled fields $\rho$, $p$, $\mathbf{V}$, and $T$ because a relation between pressure and density requires thermodynamics. In particular, one needs an equation that accounts for how internal energy (and thus temperature) changes due to compression/expansion work and heat transfer. The energy equation supplies this additional constraint by expressing conservation of energy for the flow, and when it is used together with an equation of state (such as $p=\rho R T$ for a perfect gas and appropriate caloric relations), it closes the system. Physically, the key point is that in compressible flow the mechanical motion and the thermodynamic state are inseparable: changes in velocity and pressure can produce significant changes in temperature and density, and those changes feed back into the momentum and continuity equations.





# Exercise 2.3 Derivation of the Integral Energy Equation for a Fixed Control Volume

> [!exercise] Exercise 2.3 Derivation of the Integral Energy Equation for a Fixed Control Volume
> Consider the same fixed control volume $\mathscr{V}$ with closed surface $S$ used in the derivations of the continuity and momentum equations (Fig. 2.4). The flow is inviscid, and $\mathbf{V}, \rho, p$ and $e$ denote the local velocity, density, pressure, and internal energy per unit mass, respectively. The body force per unit mass is f , and $\dot{q}$ is the rate of volumetric heat addition per unit mass.
> (a) The first law of thermodynamics states that energy can be neither created nor destroyed. For the fluid flowing through the control volume, this principle can be written as $B_1+ B_2=B_3$, where $B_1$ is the rate of heat added, $B_2$ is the rate of work done on the fluid, and $B_3$ is the rate of change of energy of the fluid. Explain physically what each of these three terms represents.
> (b) Show that the rate of work done on a moving body by a force $\mathbf{F}$ is $\dot{W}=\mathbf{F} \cdot \mathbf{V}$. Using this result, derive expressions for:
> (i) the rate of work done on the fluid by pressure forces acting on the control surface $S$, and
> (ii) the rate of work done on the fluid by body forces acting throughout $\mathscr{V}$.
> 
> Combine these to obtain the total rate of work $B_2$.
> (c) Explain why the total energy per unit mass of the moving fluid is $e+V^2 / 2$ rather than simply $e$. Then, by considering both the net energy flux across the control surface and the time rate of change of energy stored within $\boldsymbol{V}$ (accounting for unsteady effects), derive the expression for $B_3$.
> (d) Combine your results from parts (a)-(c) to derive the integral energy equation for inviscid flow.
> (e) Identify three physical phenomena that are not included in the equation derived in part (d). Write the generalized form of the energy equation that accounts for these additional effects, and explain under what conditions the simpler inviscid form is sufficient.
> (f) Discuss why the energy equation is needed in addition to the continuity and momentum equations for compressible flows, but is not required for incompressible flow analysis.

## 2.3.a

Here $B_1$, $B_2$, and $B_3$ are rates (power-like quantities) that appear when the first law of thermodynamics is applied to the fluid inside a fixed control volume. The term $B_1$ is the rate at which heat is added to the fluid in $\mathscr{V}$ from the surroundings. Physically, this is any energy transfer that is classified as heat rather than work; in the present inviscid control-volume model it is most naturally viewed as volumetric heating within the control volume (for example, absorption or emission of radiation), and it is positive when thermal energy is transferred into the fluid.

The term $B_2$ is the rate of work done on the fluid inside the control volume. In this chapter’s inviscid setting, this work comes from mechanical forces acting on the fluid: pressure forces acting on the control surface and body forces acting throughout the volume. Physically, $B_2$ measures how fast these forces deliver mechanical energy to the fluid (or remove it, if the net work is negative).

The term $B_3$ is the resulting rate of change of the energy of the fluid as it flows through the control volume. Because the control volume is fixed in space, this change has two parts: unsteady accumulation or depletion of energy stored within $\mathscr{V}$ when the local flowfield varies with time, and net convective transport of energy across the control surface as fluid enters and leaves. For a moving fluid, the relevant energy carried with the mass is not just internal energy $e$, but the total energy per unit mass that includes kinetic energy, $e+V^2/2$.

## 2.3.b

Consider first a moving body subjected to a force $\mathbf{F}$. Over an infinitesimal displacement $d\mathbf{r}$, the infinitesimal work done on the body is
$$
dW=\mathbf{F}\cdot d\mathbf{r}.
$$
Dividing by $dt$ and using $d\mathbf{r}/dt=\mathbf{V}$ gives the mechanical power (rate of doing work):
$$
\dot{W}=\frac{dW}{dt}=\mathbf{F}\cdot\frac{d\mathbf{r}}{dt}=\mathbf{F}\cdot\mathbf{V}.
$$

To apply this to the fluid in the fixed control volume, first consider the work rate due to pressure forces on the control surface $S$. With the outward area vector element $d\mathbf{S}=\mathbf{n}\,dS$, the pressure force exerted on the fluid inside the control volume across an elemental area is
$$
d\mathbf{F}_p=-p\,d\mathbf{S}.
$$
The fluid at that surface element has local velocity $\mathbf{V}$, so the rate of work done on the fluid associated with that elemental force is
$$
d\dot{W}_p=d\mathbf{F}_p\cdot\mathbf{V}=(-p\,d\mathbf{S})\cdot\mathbf{V}=-p\,\mathbf{V}\cdot d\mathbf{S}.
$$
Summing over the complete control surface yields the pressure-work contribution to $B_2$:
$$
\dot{W}_p=-\iint_{S}p\,\mathbf{V}\cdot d\mathbf{S}.
$$

Next consider body forces. If $\mathbf{f}$ is the body force per unit mass, then an elemental volume $d\mathscr{V}$ contains mass $\rho\,d\mathscr{V}$ and experiences a body force
$$
d\mathbf{F}_b=\rho\,\mathbf{f}\,d\mathscr{V}.
$$
The corresponding work rate on that elemental volume is
$$
d\dot{W}_b=d\mathbf{F}_b\cdot\mathbf{V}=(\rho\,\mathbf{f}\,d\mathscr{V})\cdot\mathbf{V}=\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}.
$$
Summing over the control volume gives the body-force work rate:
$$
\dot{W}_b=\iiint_{\mathscr{V}}\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}.
$$

Therefore, the total rate of work done on the fluid inside the control volume is the sum of the pressure and body-force contributions,
$$
B_2=\dot{W}_p+\dot{W}_b=-\iint_{S}p\,\mathbf{V}\cdot d\mathbf{S}+\iiint_{\mathscr{V}}\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}.
$$

## 2.3.c

The internal energy $e$ is the energy per unit mass associated with the random microscopic motion and internal degrees of freedom of the molecules. However, the fluid in the control volume is not stationary; it moves with macroscopic velocity $\mathbf{V}$ and therefore possesses macroscopic kinetic energy. For an elemental mass $dm$, the kinetic energy is $(1/2)\,dm\,V^{2}$, where $V^{2}=\mathbf{V}\cdot\mathbf{V}$. Hence the total energy per unit mass carried by the moving fluid is
$$
e+\frac{V^{2}}{2},
$$
not simply $e$.

To construct $B_3$, consider first the net energy carried across the control surface $S$ by mass flow. The elemental mass flow rate across $d\mathbf{S}$ is $\rho\,\mathbf{V}\cdot d\mathbf{S}$, so the associated elemental *energy* flow rate is
$$
d\dot{E}_{\text{flux}}=\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\left(e+\frac{V^{2}}{2}\right).
$$
Summing over the complete control surface gives the net rate of energy flow (net energy flux) across $S$,
$$
\dot{E}_{\text{flux}}=\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\left(e+\frac{V^{2}}{2}\right).
$$

If the flow is unsteady, there is also a time rate of change of the energy stored inside the fixed control volume. The total energy inside $\mathscr{V}$ at time $t$ is
$$
E_{\text{inside}}(t)=\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V},
$$
so the unsteady storage contribution is
$$
\dot{E}_{\text{stored}}=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V}.
$$

Therefore, the total rate of change of energy of the fluid as it flows through the control volume is the sum of these two contributions:
$$
\begin{aligned}
B_3
&=\dot{E}_{\text{stored}}+\dot{E}_{\text{flux}} \\
&=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V}
+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\left(e+\frac{V^{2}}{2}\right).
\end{aligned}
$$

## 2.3.d

From part (a), the first law applied to the fluid in the fixed control volume is $B_1+B_2=B_3$. Using the expressions obtained in parts (b) and (c), we have
$$
\iiint_{\mathscr{V}} \dot{q}\,\rho\,d\mathscr{V}
\;+\;\left(-\iint_{S}p\,\mathbf{V}\cdot d\mathbf{S}+\iiint_{\mathscr{V}}\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}\right)
=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V}
+\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\left(e+\frac{V^{2}}{2}\right).
$$
Collecting terms, the integral energy equation for inviscid flow is
$$
\iiint_{\mathscr{V}} \dot{q}\,\rho\,d\mathscr{V}
-\iint_{S}p\,\mathbf{V}\cdot d\mathbf{S}
+\iiint_{\mathscr{V}}\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}
=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V}
+\iint_{S}\rho\left(e+\frac{V^{2}}{2}\right)\mathbf{V}\cdot d\mathbf{S}.
$$

## 2.3.e

The inviscid integral energy equation derived in part (d) does not include several important mechanisms by which energy can be transferred to/from the fluid in realistic flows. Three such phenomena are:

1. Heat transfer across the control surface by thermal conduction and species diffusion (and, if present, radiation modeled as a surface heat input). In the chapter’s notation, these are bundled into a net heat-addition rate $\dot{Q}$ to the control volume.
2. Shaft work: work done on the fluid by a rotating shaft that crosses the control surface (for example, compressors or turbines), denoted $\dot{W}_{\text{shaft}}$.
3. Work done by viscous stresses on the control surface (viscous dissipation/viscous work at the boundary), denoted $\dot{W}_{\text{viscous}}$.

Including these effects, the generalized integral energy equation takes the form
$$
\dot{Q}+\dot{W}_{\text{shaft}}+\dot{W}_{\text{viscous}}
-\iint_{S}p\,\mathbf{V}\cdot d\mathbf{S}
+\iiint_{\mathscr{V}}\rho\,(\mathbf{f}\cdot\mathbf{V})\,d\mathscr{V}
=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^{2}}{2}\right)\,d\mathscr{V}
+\iint_{S}\rho\left(e+\frac{V^{2}}{2}\right)\mathbf{V}\cdot d\mathbf{S}.
$$

The simpler inviscid form is sufficient when these additional mechanisms are negligible for the situation being modeled: when there is no significant heat transfer through the boundary (adiabatic, negligible conduction/diffusion/radiation), no shaft devices doing work on the fluid within the control volume, and viscous stresses are small enough that viscous work can be neglected (the inviscid approximation).

## 2.3.f

In an incompressible-flow analysis, the density is treated as constant and the primary unknowns of interest are the velocity field $\mathbf{V}(\mathbf{x},t)$ and pressure $p(\mathbf{x},t)$. The continuity equation supplies the kinematic constraint on $\mathbf{V}$, and the momentum equation supplies the dynamical relation that determines $\mathbf{V}$ together with $p$ (with pressure serving to enforce the incompressibility constraint). In this setting, the thermodynamic state does not feed back into the mechanical solution in an essential way: one can often compute the motion without separately determining $T(\mathbf{x},t)$ or $e(\mathbf{x},t)$, and the energy equation is therefore not required to close the mechanical system.

In compressible flow, by contrast, $\rho$ is not prescribed; it varies with the thermodynamic state and couples directly into both the continuity and momentum equations. The unknowns $\rho$, $p$, $\mathbf{V}$, and $T$ (or equivalently $e$) cannot be determined from mass and momentum conservation alone because those two equations do not specify how pressure and density are related, nor how internal energy changes under compression/expansion and heat/work interactions. The energy equation provides the missing statement of conservation of energy needed to determine $e$ (and hence $T$), and when it is combined with an equation of state (for example, $p=\rho R T$ for a perfect gas along with caloric relations linking $e$ and $T$) it supplies the additional closure required to solve for the compressible flowfield. Physically, the key distinction is that in compressible flows the mechanical and thermodynamic behaviors are inseparable: changes in $p$ and $\mathbf{V}$ generally entail significant changes in $T$, $e$, and $\rho$, and those changes in turn alter the forces and accelerations through the conservation laws.






# Exercise 2.4 Determining Thrust of a Jet Propulsion Device Using the Integral Momentum Equation

> [!exercise] Exercise 2.4 Determining Thrust of a Jet Propulsion Device Using the Integral Momentum Equation
> A generic jet propulsion engine can be modeled as a duct through which air enters at the inlet (area $A_i$ ) with free-stream conditions $V_{\infty}, p_{\infty}$, and $\rho_{\infty}$, and exits at the exhaust (area $\left.A_e\right)$ with conditions $V_e, p_e$, and $\rho_e$. The external surface of the engine is assumed to be exposed to a uniform ambient pressure $p_{\infty}$. Shear stress effects are neglected.
> (a) Explain, using the example of an inflated rubber balloon (both with the neck tied shut and with the neck open), why the thrust of any jet propulsion device is fundamentally due to an imbalance in the pressure distribution acting on the engine surfaces. Why does a sealed balloon experience no net thrust, while an open balloon does?
> (b) The net force on the engine is given by the integral of the pressure distribution over all exposed surfaces:
> 
> $$
> T=-\int\left(p_i d S\right)_x-\int\left(p_{\infty} d S\right)_x
> $$
> 
> where the first term accounts for the internal pressure and the second for the external pressure. Show that the contribution from the constant external pressure $p_{\infty}$ simplifies to $p_{\infty}\left(A_i-A_e\right)$, and explain the physical reasoning behind its sign.
> (c) Now consider a control volume drawn just inside the engine duct, with boundaries adjacent to the internal walls and perpendicular cross-sections at the inlet ( $A_i$ ) and exit ( $A_e$ ). Using the steady, inviscid, integral momentum equation (with no body forces):
> 
> $$
> \iint_S(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}=-\iint_S p d \mathbf{S}
> $$
> 
> evaluate both sides of the $x$-component of this equation by considering each segment of the control surface (inlet, exit, and upper/lower walls) separately. Show that the force exerted on the gas by the internal engine surfaces can be expressed in terms of the inlet and exit mass flows, velocities, and pressures.
> (d) Using Newton's third law to relate the force on the gas to the force on the solid engine surface, and combining with your result from part (b), derive the uninstalled engine thrust equation:
> 
> $$
> T=\dot{m}_e V_e-\dot{m}_i V_{\infty}+\left(p_e-p_{\infty}\right) A_e
> $$
> 
> where $\dot{m}_i=\rho_{\infty} V_{\infty} A_i$ and $\dot{m}_e=\rho_e V_e A_e$.
> (e) Interpret each term in the thrust equation physically. Under what condition does the pressure term $\left(p_e-p_{\infty}\right) A_e$ vanish? What does the remaining expression represent in terms of momentum change?
> (f) Discuss the practical advantage of this result. Why is it that the detailed (and potentially very complex) pressure distribution inside the engine does not need to be known in order to calculate the thrust? What property of the integral form of the momentum equation makes this possible?

## 2.4.a

The thrust of a jet propulsion device is fundamentally a *pressure-force* result: the only way the fluid can exert a net force on the solid engine is through stresses on the engine’s surface, and in an inviscid model those stresses reduce to pressure acting normal to the surface. When the pressure distribution over the entire surface is such that the axial components do not cancel, the engine experiences a net axial force (thrust). The “jet momentum” viewpoint is consistent with this, but it is a consequence of the same pressure forces accelerating the fluid; the ultimate agent that pushes on the hardware is the pressure field on the wetted surfaces.

The balloon example makes the cancellation (or lack of it) clear. For a balloon with its neck tied shut, the gas inside the balloon is (to leading order) at a uniform pressure that acts on a closed surface. Pressure always acts normal to the surface, and when it acts over a *closed* surface in a way that has no preferred direction, the vector sum of all those normal forces is zero; there is no unbalanced axial component to produce thrust. Any pressure force on one patch of the balloon is matched by an equal-and-opposite contribution elsewhere on the closed surface, so the net force vanishes.

If the neck is open, the surface on which the internal pressure acts is no longer a purely closed “bag” surface: there is an opening across which the pressure forces do not balance in the same way. Near the neck, the interior pressure acts on the internal walls and on the effective “end area” associated with the opening, while the exterior sees essentially ambient pressure. The result is an unbalanced pressure force directed opposite the exhaust direction: the pressure inside pushes on the fluid and the surrounding surface in such a way that the gas is driven out of the opening, and by Newton’s third law the balloon experiences an equal and opposite reaction. Thus a sealed balloon has no net thrust because its pressure forces balance on a closed surface, whereas an open balloon has thrust because opening the neck creates a pressure-imbalance (and associated momentum flux) that cannot be canceled by pressure forces elsewhere.

## 2.4.b

Because the ambient pressure $p_{\infty}$ is assumed uniform over the entire external surface of the engine, the only way it can contribute a nonzero *net* $x$-force is through the net $x$-projection of the surface on which it acts. For the duct model, that net projection is simply the difference between the inlet and exit cross-sectional areas, because the sidewalls have (to leading order) no net $x$-projected area (their outward normals are predominantly transverse, so their $x$-components cancel around the perimeter).

Let $d\mathbf{S}=\mathbf{n}\,dS$ be the outward area vector of the engine surface on which the external pressure acts. The $x$-component of the external pressure force contribution in the given thrust expression is
$$
T_{\infty}=-\int\left(p_{\infty}\,dS\right)_x=-\iint_{\text{ext}} p_{\infty}\,(\mathbf{n}\cdot\hat{\mathbf{x}})\,dS.
$$
Since $p_{\infty}$ is constant, this becomes
$$
T_{\infty}=-p_{\infty}\iint_{\text{ext}} n_x\,dS,
$$
where $n_x=\mathbf{n}\cdot\hat{\mathbf{x}}$.

For the duct, the external surface contribution reduces to the inlet and exit “end” areas. On the inlet plane (area $A_i$), the outward normal points upstream, so $n_x=-1$ and $n_x\,dS=-\,dA$, giving
$$
T_{\infty,i}=-p_{\infty}\iint_{A_i}(-\,dA)=+p_{\infty}A_i.
$$
On the exit plane (area $A_e$), the outward normal points downstream, so $n_x=+1$ and $n_x\,dS=+\,dA$, giving
$$
T_{\infty,e}=-p_{\infty}\iint_{A_e}(+\,dA)=-p_{\infty}A_e.
$$
Therefore, the net contribution from the constant external pressure is
$$
T_{\infty}=T_{\infty,i}+T_{\infty,e}=p_{\infty}\left(A_i-A_e\right).
$$
The sign has a direct physical interpretation: ambient pressure on the inlet face pushes the engine in the $+x$ direction (because that face’s outward normal points in $-x$), whereas ambient pressure on the exit face pushes in the $-x$ direction. The net effect is proportional to the difference in areas.

## 2.4.c

Take as the control surface $S$ the inlet plane (area $A_i$), the exit plane (area $A_e$), and the internal duct walls. Evaluate the steady, inviscid integral momentum equation with no body forces,
$$
\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)\mathbf{V}=-\iint_{S}p\,d\mathbf{S},
$$
in the axial direction. To match the chapter’s thrust derivation, take the positive $x$ direction to be toward the left (opposite the flow direction in the sketch), so that at the inlet and exit stations
$$
V_x=-V_{\infty}\quad\text{on }A_i,\qquad V_x=-V_e\quad\text{on }A_e,
$$
where $V_{\infty}$ and $V_e$ are the inlet and exit speed magnitudes.

On the inlet plane, $\rho$ and $V_x$ are uniform and $\rho\,\mathbf{V}\cdot d\mathbf{S}=-\rho_{\infty}V_{\infty}\,dA$ (inflow), hence
$$
\iint_{A_i}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)V_x
=\left(-\rho_{\infty}V_{\infty}A_i\right)\left(-V_{\infty}\right)
=\dot{m}_i V_{\infty},
$$
where $\dot{m}_i=\rho_{\infty}V_{\infty}A_i$.

On the exit plane, $\rho$ and $V_x$ are uniform and $\rho\,\mathbf{V}\cdot d\mathbf{S}=+\rho_eV_e\,dA$ (outflow), hence
$$
\iint_{A_e}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)V_x
=\left(\rho_eV_eA_e\right)\left(-V_e\right)
=-\dot{m}_e V_e,
$$
where $\dot{m}_e=\rho_eV_eA_e$.

On the internal walls, $\mathbf{V}\cdot d\mathbf{S}=0$ (no penetration), so the wall contribution to the momentum-flux integral is zero. Therefore, the $x$-component of the left-hand side becomes
$$
\iint_{S}\left(\rho\,\mathbf{V}\cdot d\mathbf{S}\right)V_x=\dot{m}_i V_{\infty}-\dot{m}_e V_e.
$$

For the pressure term, decompose the right-hand side integral into inlet, exit, and wall contributions. The inlet and exit plane contributions are
$$
\int_{A_i}(p\,dS)_x=p_{\infty}A_i,\qquad \int_{A_e}(p\,dS)_x=-p_eA_e,
$$
and the remaining contribution is due to the distributed internal pressure $p_i$ acting on the gas because of the equal and opposite reaction on the solid interior surface. Denote
$$
\left[-\int\left(p_i\,dS\right)_x\right]\equiv\text{(force on the gas due to the solid interior surface)}.
$$
Then the $x$-momentum balance yields
$$
\dot{m}_i V_{\infty}-\dot{m}_e V_e=-p_{\infty}A_i+p_eA_e+\left[-\int\left(p_i\,dS\right)_x\right],
$$
so the force exerted on the gas by the internal engine surfaces can be written as
$$
\left[-\int\left(p_i\,dS\right)_x\right]=\dot{m}_i V_{\infty}-\dot{m}_e V_e+p_{\infty}A_i-p_eA_e.
$$

## 2.4.d

From part (b), the uninstalled engine thrust is the net pressure force on the solid engine surfaces, written as
$$
T=\left[-\int\left(p_i\,dS\right)_x\right]_{\text{force on the solid surface due to the gas}}+p_{\infty}\left(A_i-A_e\right).
$$
From part (c), the bracketed quantity for the force on the gas due to the solid surface is
$$
\left[-\int\left(p_i\,dS\right)_x\right]_{\text{force on the gas due to the solid surface}}
=\dot{m}_i V_{\infty}-\dot{m}_e V_e+p_{\infty}A_i-p_eA_e.
$$
By Newton’s third law, the force on the solid surface due to the gas is equal and opposite, hence
$$
\left[-\int\left(p_i\,dS\right)_x\right]_{\text{force on the solid surface due to the gas}}
=-\left[-\int\left(p_i\,dS\right)_x\right]_{\text{force on the gas due to the solid surface}}
=\dot{m}_e V_e-\dot{m}_i V_{\infty}+p_eA_e-p_{\infty}A_i.
$$
Substituting this into the thrust expression and simplifying gives the uninstalled thrust equation:
$$
\begin{aligned}
T
&=\left(\dot{m}_e V_e-\dot{m}_i V_{\infty}+p_eA_e-p_{\infty}A_i\right)+p_{\infty}\left(A_i-A_e\right) \\
&=\dot{m}_e V_e-\dot{m}_i V_{\infty}+p_eA_e-p_{\infty}A_e \\
&=\dot{m}_e V_e-\dot{m}_i V_{\infty}+\left(p_e-p_{\infty}\right)A_e.
\end{aligned}
$$

## 2.4.f

The practical advantage of the thrust result is that it converts an essentially impossible “surface-load bookkeeping” problem into a small set of measurable inlet/exit quantities. In principle, thrust is obtained by integrating the pressure distribution over all exposed internal and external engine surfaces. In practice, the detailed internal pressure field $p_i(\mathbf{x})$ can be extremely complicated, and even if it were known locally it would still have to be integrated over a complex three-dimensional geometry to obtain the net axial force. The integral momentum equation bypasses that difficulty: it states a global balance between the net surface forces on the control volume and the net rate at which axial momentum is carried into and out of the control volume by the flow.

When a control surface is chosen to cut the flow at a few stations (inlet and exit) and to coincide with impermeable walls elsewhere, the momentum-flux integral depends only on the fluxes through the inlet and exit planes (the wall flux is zero because $\mathbf{V}\cdot d\mathbf{S}=0$ on a solid boundary). The only remaining appearance of the complicated wall-pressure distribution is through its net integral, i.e., a single resultant force. That resultant can then be eliminated in favor of inlet/exit momentum fluxes and the simple pressure forces on the inlet and exit planes. In this way, the detailed pressure distribution inside the engine is “buried” inside the control volume: its effect on thrust enters only through a single net force that the momentum balance allows you to compute without resolving the distribution.

This is the key property of the integral form of the momentum equation: it is a conservation law written in global (integral) form, relating net forces to net momentum fluxes across a closed surface. Therefore, once the inlet and exit conditions (mass flow rates and velocities) and the exit pressure relative to ambient are known, the thrust follows directly, without needing the detailed internal pressure distribution point-by-point.






# Exercise 2.5

> [!exercise] Exercise 2.5
> Consider a turbojet-powered airplane flying at a velocity of $300 \mathrm{~m} / \mathrm{s}$ at an altitude of 10 km , where the free-stream pressure and density are $2.65 \times 10^{4} \mathrm{~N} / \mathrm{m}^{2}$ and $0.414 \mathrm{~kg} / \mathrm{m}^{3}$, respectively. The turbojet engine has inlet and exit areas of $2 \mathrm{~m}^{2}$ and $1 \mathrm{~m}^{2}$, respectively. The velocity and pressure of the exhaust gas are $500 \mathrm{~m} / \mathrm{s}$ and $2.3 \times 10^{4} \mathrm{~N} / \mathrm{m}^{2}$ respectively. The fuel-toair mass ratio is 0.05 . Calculate the thrust of the engine.

## 2.5

Use the uninstalled engine thrust equation derived in Exercise 2.4,
$$
T=\dot{m}_e V_e-\dot{m}_i V_{\infty}+\left(p_e-p_{\infty}\right)A_e.
$$
The inlet mass flow rate is
$$
\dot{m}_i=\rho_{\infty}V_{\infty}A_i=(0.414)(300)(2)=248.4\ \mathrm{kg/s}.
$$
With fuel-to-air ratio $f/a=0.05$, the exit mass flow rate is
$$
\dot{m}_e=(1+f/a)\dot{m}_i=1.05(248.4)=260.82\ \mathrm{kg/s}.
$$
Therefore,
$$
\begin{aligned}
T
&=\dot{m}_e V_e-\dot{m}_i V_{\infty}+\left(p_e-p_{\infty}\right)A_e \\
&=(260.82)(500)-(248.4)(300)+\left(2.3\times 10^{4}-2.65\times 10^{4}\right)(1) \\
&=130410-74520-3500 \\
&=52390\ \mathrm{N}.
\end{aligned}
$$
Thus, the thrust is $T\approx 5.24\times 10^{4}\ \mathrm{N}$.
