## 1 Conservation laws and extensive quantities

In the previous two lectures, we developed a careful distinction between Eulerian and Lagrangian descriptions of fluid motion and introduced the Reynolds transport theorem (RTT) as the appropriate tool for taking time derivatives of integrals over regions of space. We now use that framework to derive the fundamental conservation laws governing compressible flow.

The governing equations of fluid mechanics are best understood as statements about the evolution of extensive quantities carried by the fluid. An extensive quantity is one whose value depends on the amount of material present. Examples include mass, linear momentum, and energy. These quantities are naturally expressed as integrals over a region of space.

Let $\Omega(t)$ denote a (possibly time-dependent) region of physical space. An extensive quantity associated with the fluid occupying $\Omega(t)$ may be written in the generic form

$$
Q_{\Omega}(t)=\int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V
$$

where $q^{E}(\boldsymbol{x}, t)$ is the Eulerian density (per unit volume) of the quantity. The superscript $E$ emphasizes that this field is expressed in the Eulerian representation, consistent with the notation established previously.

Conservation laws are empirically justified statements about the behavior of such extensive quantities for material systems; i.e. a fixed collections of fluid elements. We accept these laws as true and set as our task to interpret them mathematically for arbitrary control volumes. The Reynolds transport theorem provides exactly this bridge.

Throughout this lecture, we will explicitly retain the distinction between Eulerian and Lagrangian representations. Once the governing equations are established, we will adopt the common convention that all fields are Eulerian unless otherwise stated and drop the superscript $E$.

## 2 Conservation of mass

### 2.1 Total mass in a region

The total mass of fluid occupying the region $\Omega(t)$ is defined as

$$
M_{\Omega}(t)=\int_{\Omega(t)} \rho^{E}(\boldsymbol{x}, t) d V
$$

where $\rho^{E}(\boldsymbol{x}, t)$ is the Eulerian mass density field.

### 2.2 Physical postulate

The conservation of mass is expressed by the following empirical statement:
The total mass of a material system is constant in time.
That is, if $\Omega(t)$ coincides with a material volume moving with the fluid, then $d M_{\Omega} / d t=0$. Our goal is to express this statement in a form that applies to an arbitrary region $\Omega(t)$, which need not be a material volume.

### 2.3 Application of the Reynolds transport theorem

Applying the Reynolds transport theorem to the mass integral gives

$$
\frac{d}{d t} \int_{\Omega(t)} \rho^{E} d V=\int_{\Omega(t)} \partial_{t} \rho^{E} d V+\int_{\partial \Omega(t)} \rho^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S=0
$$

where $\boldsymbol{u}^{E}$ is the Eulerian fluid velocity, $\boldsymbol{w}^{E}$ is the velocity of the control volume boundary, and $\boldsymbol{n}$ is the outward unit normal on $\partial \Omega(t)$.

### 2.4 Interpretation

This equation states that the time rate of change of mass within a fixed region is exactly balanced by the net flux of mass through the boundary. If fluid flows out of the region, the total mass inside decreases; if fluid flows in, it increases. No assumption has been made about incompressibility or steady flow. The result follows directly from the material conservation of mass together with the Reynolds transport theorem.

### 2.5 Remark: Lagrangian density

Although density is most naturally treated as an Eulerian field, it is sometimes useful to consider its representation in Lagrangian (material) coordinates.

Let $\boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right)$ denote the material flow map, and define the Lagrangian density as:

$$
\rho^{L}\left(\boldsymbol{x}_{0}, t\right):=\rho^{E}\left(\phi\left(\boldsymbol{x}_{0}, t\right), t\right) .
$$

Let $\rho_{0}\left(\boldsymbol{x}_{0}\right):=\rho^{E}(\phi(\boldsymbol{x}, 0), 0)$ denote the initial density field, expressed as a function of material labels. Mass conservation for an infinitesimal material volume element implies

$$
\rho^{E}\left(\phi\left(\boldsymbol{x}_{0}, t\right), t\right) J_{\phi}\left(\boldsymbol{x}_{0}, t\right)=\rho_{0}\left(\boldsymbol{x}_{0}\right)
$$

where $J_{\phi}=\operatorname{det}\left(\nabla_{\boldsymbol{x}_{0}} \phi\right)$ is the Jacobian determinant of the flow map. Equivalently,

$$
\rho^{L}\left(\boldsymbol{x}_{0}, t\right)=\frac{\rho_{0}\left(\boldsymbol{x}_{0}\right)}{J_{\phi}\left(\boldsymbol{x}_{0}, t\right)}
$$

This relation shows that, in the Lagrangian description, density is not an independent field: once the initial density and the deformation of material volumes are known, the density at later times is completely determined. Compressibility is therefore encoded entirely in the evolution of the volume Jacobian. Incompressible flow corresponds to the special case $J_{\phi} \equiv 1$.

## 3 Conservation of momentum

### 3.1 Total momentum in a region

The total linear momentum of fluid occupying the region $\Omega(t)$ is defined as

$$
\boldsymbol{P}_{\Omega}(t)=\int_{\Omega(t)} \rho^{E}(\boldsymbol{x}, t) \boldsymbol{u}^{E}(\boldsymbol{x}, t) d V
$$

where $\boldsymbol{u}^{E}(\boldsymbol{x}, t)$ is the Eulerian velocity field. The integrand $\rho^{E} \boldsymbol{u}^{E}$ represents the momentum density (momentum per unit volume).

### 3.2 Physical postulate

The conservation of linear momentum is expressed by Newton's second law, applied to a material system:

The time rate of change of the total momentum of a material system equals the net external force acting on it.
As in the case of mass conservation, this statement applies directly only when $\Omega(t)$ coincides with a material volume. Our goal is to express it in a form that applies to an arbitrary control volume.

### 3.3 Application of the Reynolds transport theorem

Applying the Reynolds transport theorem to the momentum integral yields

$$
\frac{d}{d t} \int_{\Omega(t)} \rho^{E} \boldsymbol{u}^{E} d V=\int_{\Omega(t)} \partial_{t}\left(\rho^{E} \boldsymbol{u}^{E}\right) d V+\int_{\partial \Omega(t)} \rho^{E} \boldsymbol{u}^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S
$$

### 3.4 Forces acting on a fluid

It is important to distinguish between body forces and stresses on physical grounds. Body forces arise from interactions between the fluid and external fields (such as gravity or electromagnetism) and therefore act throughout the volume of a fluid element. In contrast, stresses represent mechanical interactions between neighboring portions of the fluid itself. Such interactions can only be transmitted across interfaces separating adjacent fluid elements and therefore appear as forces acting on surfaces. For this reason, internal mechanical forces in a continuum are necessarily represented as surface forces, described by a traction vector acting on the boundary.

The external forces acting on a fluid volume are thus naturally divided into two categories:

- Body forces, which act throughout the volume (e.g. gravity),
- Surface forces, which act on the boundary $\partial \Omega$ through mechanical contact with the surroundings.

Body forces may be written in the form

$$
\boldsymbol{F}_{\mathrm{body}}=\int_{\Omega} \rho^{E} \boldsymbol{f}^{E} d V
$$

where $\boldsymbol{f}^{E}$ is the body force per unit mass.
Surface forces are represented by the Eulerian traction vector $\boldsymbol{t}^{E}$, defined as the force per unit area acting on the boundary $\partial \Omega(t)$ :

$$
\boldsymbol{F}_{\mathrm{surf}}=\int_{\partial \Omega} \boldsymbol{t}^{E} d S
$$

### 3.5 Inviscid modeling assumption

To describe surface forces in a continuum, it is convenient to introduce the Cauchy stress tensor. The stress tensor $\boldsymbol{\sigma}^{E}(\boldsymbol{x}, t)$ is defined so that the traction (vector force per unit area) acting on a surface with outward unit normal $\boldsymbol{n}$ is given by

$$
\boldsymbol{t}^{E}=\boldsymbol{\sigma}^{E} \boldsymbol{n} .
$$

Physically, $\boldsymbol{\sigma}^{E}$ encodes how neighboring fluid elements exert forces on one another across shared interfaces. If the tractions acting on opposite faces of a fluid element do not exactly balance, the resulting mismatch produces a net force and therefore acceleration of the element.

The stress transmitted across a surface may produce two qualitatively distinct effects on a fluid element. First, it may act to compress or expand the element, changing its volume while preserving its shape. Such an effect must be isotropic, acting equally in all directions, and is therefore represented by a scalar pressure. Second, the stress may act to distort the element at fixed volume, changing its shape through shear or differential stretching. These shape-changing effects depend on the orientation of the surface and are captured by the deviatoric (non-isotropic) part of the stress. This physical distinction motivates the decomposition of the Cauchy stress tensor into an isotropic pressure contribution and a deviatoric contribution associated with viscous effects.

$$
\boldsymbol{\sigma}^{E}=-p^{E} \boldsymbol{I}+\boldsymbol{\tau}^{E},
$$

where $\boldsymbol{\tau}^{E}$ represents viscous stresses. This deviatoric part of the stress tensor represents resistance to relative motion between neighboring fluid elements. When adjacent elements move with different velocities, microscopic momentum exchange through molecular motion produces stresses that oppose velocity gradients. These viscous stresses act to smooth variations in the velocity field and are responsible for dissipation of kinetic energy into internal energy. In a Newtonian fluid, the deviatoric stress depends linearly on the local rate of deformation, providing a simple and widely applicable constitutive model. For a Newtonian compressible fluid, the deviatoric stress tensor is given by

$$
\boldsymbol{\tau}^{E}=\mu\left(\nabla \boldsymbol{u}^{E}+\left(\nabla \boldsymbol{u}^{E}\right)^{T}\right)+\lambda\left(\nabla \cdot \boldsymbol{u}^{E}\right) \boldsymbol{I},
$$

where $\mu$ is the dynamic viscosity and $\lambda$ is the second viscosity coefficient. Under the Stokes hypothesis, $\lambda=-\frac{2}{3} \mu$, and the deviatoric stress becomes

$$
\boldsymbol{\tau}^{E}=\mu\left[\nabla \boldsymbol{u}^{E}+\left(\nabla \boldsymbol{u}^{E}\right)^{T}-\frac{2}{3}\left(\nabla \cdot \boldsymbol{u}^{E}\right) \boldsymbol{I}\right] .
$$

In this course, we focus on inviscid compressible flow and therefore neglect viscous stresses, setting $\boldsymbol{\tau}^{E}=\mathbf{0}$. Under this inviscid assumption, the stress tensor reduces to

$$
\boldsymbol{\sigma}_{\text {inviscid }}^{E}=-p^{E} \boldsymbol{I},
$$

and the corresponding traction becomes

$$
\boldsymbol{t}_{\text {inviscid }}^{E}=-p^{E} \boldsymbol{n} .
$$

The neglect of viscous stresses is a modeling assumption whose validity depends on the physical regime of interest. Viscous stresses arise from velocity gradients and therefore become significant in regions where the flow varies rapidly in space. In compressible flows, such large gradients are typically confined to thin regions such as boundary layers near solid surfaces and the internal structure of shock waves. Outside these localized regions, velocity gradients are modest and viscous stresses are small compared to pressure forces, so that the bulk flow dynamics are accurately described by inviscid equations.

This localization is closely tied to the mathematical character of the inviscid compressible-flow equations. Away from shocks, these equations are hyperbolic, meaning that information propagates along characteristic directions as finite-speed waves. As a result, localized dissipative
mechanisms do not immediately influence the entire flow field. In contrast, incompressible flow is governed by elliptic equations, for which disturbances are felt globally. For this reason, viscous effects in incompressible flow tend to influence the entire domain and cannot usually be neglected, whereas in compressible flow they may often be confined to thin regions without compromising the accuracy of the inviscid description elsewhere.

### 3.6 Integral momentum equation

Combining the Reynolds transport theorem with the force expressions above, the integral momentum equation takes the form

$$
\int_{\Omega(t)} \partial_{t}\left(\rho^{E} \boldsymbol{u}^{E}\right) d V+\int_{\partial \Omega(t)} \rho^{E} \boldsymbol{u}^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S=-\int_{\partial \Omega} p^{E} \boldsymbol{n} d S+\int_{\Omega} \rho^{E} \boldsymbol{f}^{E} d V
$$

This equation expresses the balance of momentum within the control volume: the rate of change of momentum and its advective transport across the boundary are balanced by pressure forces acting on the boundary and body forces acting throughout the volume.

## 4 Conservation of energy

### 4.1 Total energy in a region

Energy is an extensive quantity that accounts for all mechanisms by which a fluid can store and exchange mechanical and thermal effects. For a compressible fluid, the total energy per unit volume consists of three contributions:

- kinetic energy associated with bulk motion,
- internal energy associated with microscopic molecular motion,
- potential energy due to external fields (optional).

The total energy of the fluid occupying $\Omega(t)$ is therefore written as

$$
E_{\Omega}(t)=\int_{\Omega(t)} \rho^{E}\left(e^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right) d V
$$

where $e^{E}(\boldsymbol{x}, t)$ is the specific internal energy and $\Phi(\boldsymbol{x})$ is a prescribed potential energy per unit mass (e.g. gravitational potential).

The internal energy represents energy stored in molecular degrees of freedom that are not captured by the bulk velocity $\boldsymbol{u}^{E}$. While the kinetic energy term accounts for the motion of a fluid element as a whole, internal energy accounts for random molecular motion, molecular vibration and rotation, and other microscopic interactions. Changes in internal energy therefore reflect heating, cooling, compression, and expansion of the fluid, rather than macroscopic acceleration.

### 4.2 Physical postulate: the first law of thermodynamics

The conservation of energy is expressed by the first law of thermodynamics:

The time rate of change of total energy of a material system equals the net rate of work done on it plus the net rate of heat added to it.

Our task is to express this statement mathematically for an arbitrary control volume $\Omega(t)$ using the Reynolds transport theorem.

### 4.3 Work and heat transfer mechanisms

Energy may enter or leave a control volume through two distinct mechanisms:

- Mechanical work, performed by body forces and surface tractions,
- Heat transfer, arising from microscopic energy exchange driven by temperature gradients.

Let us consider the rate at which work is done first. We already know the forces that can perform work: those were presented in our development of conservation of momentum. So here is the key question:

Which velocity belongs in the surface-work term? A subtle but important point is that the velocity appearing in the surface-work term must be relative to the control surface motion. Here is a way to intuit that face: The traction $\boldsymbol{t}^{E}$ is the stress force exerted by the surroundings across the control surface. Power can only be transferred to the fluid along the boundaries of $\Omega$ when fluid actually moves relative to that surface. That is, if the boundary moves with the fluid ( $\boldsymbol{w}=\boldsymbol{u}$ ), no fluid mass crosses it, and there should be no flow-work term through that boundary. Using $\boldsymbol{u}$ alone would incorrectly predict nonzero pressure work even for a material surface. Accordingly, the mechanical power input through surface tractions is

$$
\dot{W}_{\text {surf }}=\int_{\partial \Omega(t)} \boldsymbol{t}^{E} \cdot\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) d S
$$

This choice is consistent with the Reynolds transport theorem: when the control surface moves with the fluid ( $\boldsymbol{w}^{E}=\boldsymbol{u}^{E}$ ), no material crosses the boundary, and there is no transport of mechanical energy through that boundary.

In contrast, body forces act throughout the volume and do work directly on the fluid elements, so their power involves the material velocity $\boldsymbol{u}^{E}$ :

$$
\dot{W}_{\mathrm{body}}=\int_{\Omega(t)} \rho^{E} \boldsymbol{f}^{E} \cdot \boldsymbol{u}^{E} d V
$$

Pressure work provides a useful consistency check for this result. For inviscid flow $\boldsymbol{t}^{E}=-p^{E} \boldsymbol{n}$, giving the surface contribution $-\int_{\partial \Omega(t)} p^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S$, which correctly vanishes for a material control surface. Note that this outcome does not mean that pressure is not present in the energy equation when the control volume $\Omega$ is a material volume that moves with the flow. Its effect is latent, and manifests itself directly as changes to the internal energy $e^{E}$ of the system. In fact, manipulating the equations shows that pressure can be viewed as a source term to internal energy, active when the flow undergoes local compression/extension.
Heat transfer is represented by a heat flux vector $\boldsymbol{q}_{h}^{E}$, defined as the rate of thermal energy transfer per unit area. (Note that the heat flux $\boldsymbol{q}_{h}^{E}$ is distinct from $\boldsymbol{q}^{E}$, the variable we use to denote a generic
vector quantity.) Unlike mechanical work, which is associated with forces acting on fluid elements, heat transfer arises from microscopic molecular motion that transports energy across surfaces in response to temperature differences.

The heat flux is not an externally prescribed forcing but a constitutive quantity that depends on the local thermodynamic state of the fluid. Its specific form must therefore be supplied by a constitutive law. The most common model is Fourier's law,

$$
\boldsymbol{q}_{h}^{E}=-k \nabla T^{E},
$$

where $k$ is the thermal conductivity and $T^{E}$ is the temperature field. This relation expresses the empirical observation that thermal energy flows from regions of higher temperature to lower temperature.

Fourier's law is accurate for a wide range of engineering flows but rests on the assumption that heat flux responds instantaneously to local temperature gradients. In regimes involving very rapid transients, very small length scales, or rarefied gases, this assumption may break down, and alternative constitutive models introducing finite thermal relaxation times or higher-order effects are sometimes employed. Such models play a role in specialized applications but are beyond the scope of this course.

In what follows, we retain the heat flux term in the energy balance without committing to a particular constitutive law. Depending on the physical regime of interest, heat transfer may be neglected (e.g. adiabatic flow), or an appropriate constitutive relation may be specified as needed.

The net heat input to the control volume is therefore

$$
-\int_{\partial \Omega} \boldsymbol{q}_{h}^{E} \cdot \boldsymbol{n} d S
$$

### 4.4 Application of the Reynolds transport theorem

Applying the Reynolds transport theorem to the total energy integral yields

$$
\frac{d E_{\Omega}}{d t}=\int_{\Omega} \partial_{t}\left[\rho^{E}\left(e^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)\right] d V+\int_{\partial \Omega} \rho^{E}\left(e^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S
$$

Equating this rate of change to the sum of mechanical work and heat transfer gives the integral energy balance.

### 4.5 Inviscid energy equation

Under the inviscid assumption, the traction reduces to $\boldsymbol{t}^{E}=-p^{E} \boldsymbol{n}$. Neglecting viscous dissipation, the integral energy equation becomes

$$
\begin{gathered}
\int_{\Omega(t)} \partial_{t}\left[\rho^{E}\left(e^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)\right] d V+\int_{\partial \Omega(t)} \rho^{E}\left(e^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S=\int_{\Omega(t)} \rho^{E} \boldsymbol{f}^{E} \cdot \boldsymbol{u}^{E} d V \\
-\int_{\partial \Omega(t)} p^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S-\int_{\partial \Omega(t)} \boldsymbol{q}_{h}^{E} \cdot \boldsymbol{n} d S
\end{gathered}
$$

This equation expresses conservation of total energy for an arbitrary control volume, accounting for work done by pressure and body forces and for heat transfer.

### 4.6 Enthalpy and its physical meaning

In this and the next subsection, we discuss quantities provided in the Reference document, motivated using the conservation laws just derived. Hopefully that gives you a fresh lens within which to view and understand these concepts.

To streamline our notation, define the total specific energy

$$
E^{E}:=e^{E}+\frac{1}{2}\left|u^{E}\right|^{2}+\Phi .
$$

Under the inviscid assumption $\boldsymbol{t}^{E}=-p^{E} \boldsymbol{n}$, the integral energy balance may be written as

$$
\begin{aligned}
\frac{d}{d t} \int_{\Omega} \rho^{E} E^{E} d V+\int_{\partial \Omega} \rho^{E} E^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S= & \int_{\Omega} \rho^{E} \boldsymbol{f}^{E} \cdot \boldsymbol{u}^{E} d V \\
& -\int_{\partial \Omega} p^{E}\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S-\int_{\partial \Omega} \boldsymbol{q}_{h}^{E} \cdot \boldsymbol{n} d S
\end{aligned}
$$

The two boundary terms involving $\boldsymbol{u}^{E} \cdot \boldsymbol{n}$ may be combined by moving the pressure-work term to the left-hand side:

$$
\frac{d}{d t} \int_{\Omega} \rho^{E} E^{E} d V+\int_{\partial \Omega}\left(\rho^{E} E^{E}+p^{E}\right)\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S=\int_{\Omega} \rho^{E} \boldsymbol{f}^{E} \cdot \boldsymbol{u}^{E} d V-\int_{\partial \Omega} \boldsymbol{q}_{h}^{E} \cdot \boldsymbol{n} d S
$$

This regrouping motivates defining the specific enthalpy

$$
h^{E}:=e^{E}+\frac{p^{E}}{\rho^{E}}
$$

Indeed, since $\rho^{E} E^{E}+p^{E}=\rho^{E}\left(h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)$, the energy equation takes the compact enthalpy-flux form

$$
\frac{d}{d t} \int_{\Omega} \rho^{E} E^{E} d V+\int_{\partial \Omega} \rho^{E}\left(h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi\right)\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S=\int_{\Omega} \rho^{E} \boldsymbol{f}^{E} \cdot \boldsymbol{u}^{E} d V-\int_{\partial \Omega} \boldsymbol{q}_{h}^{E} \cdot \boldsymbol{n} d S
$$

Physical interpretation. The definition $h^{E}=e^{E}+p^{E} / \rho^{E}$ is not merely algebraic. When mass crosses a control surface, the fluid transports internal energy $e^{E}$, but it must also perform pressure ("flow") work to push surrounding fluid as it enters or exits. This result is tied to the following physical fact: pressure work can only occur when fluid mass crosses a surface, in exactly the same way that energy flux (provided by the Reynolds transport theorem) can only occur when fluid moves through a surface. Enthalpy packages these spiritually similar contributions into a single per-mass quantity that is naturally transported by the flow.

### 4.7 Stagnation quantities

The enthalpy-flux form of the energy equation highlights a particularly important combination of variables:

$$
h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}+\Phi .
$$

This combination represents the total energy transported per unit mass by the flow. Under certain common idealizations, it becomes a conserved quantity and therefore deserves special attention.

### 4.7.1 Motivation

Consider a flow satisfying the following assumptions:

- steady,
- inviscid,
- adiabatic,
- no body-force work (and hence $\Phi \equiv 0$ ).

Under these conditions, the enthalpy-flux form of the energy equation reduces to the statement that the net flux of $\rho^{E}\left(h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}\right)$ through the boundary of a fixed control volume is zero. At the same time, conservation of mass implies that the net flux of $\rho^{E} \boldsymbol{u}^{E}$ through the boundary is also zero.

Taken together, these two facts imply that, for flow entering and leaving the control volume, the quantity

$$
h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2}
$$

is the same at inlet and outlet. In other words, in steady, adiabatic, inviscid flow, changes in flow speed are accompanied by compensating changes in thermodynamic state so that this combination remains invariant. This observation motivates the definition of stagnation quantities.

### 4.7.2 Stagnation enthalpy

The stagnation enthalpy is defined as

$$
h_{0}:=h^{E}+\frac{1}{2}\left|\boldsymbol{u}^{E}\right|^{2} \text {. }
$$

Physically, $h_{0}$ represents the specific enthalpy the fluid would attain if it were brought to rest adiabatically and without losses. Under the assumptions listed above, $h_{0}$ is conserved along the flow. For this reason, stagnation enthalpy serves as a convenient invariant in many compressible-flow analyses and provides a velocity-independent measure of the energetic state of the fluid.

### 4.7.3 Stagnation temperature for an ideal gas

For a calorically perfect ideal gas, the specific enthalpy is related to temperature by

$$
h^{E}=c_{p} T^{E},
$$

where $c_{p}$ is the constant-pressure specific heat. (We emphasize that this relation relies on an ideal-gas model with constant specific heats and is valid only over temperature ranges where such an approximation is appropriate.) Using this relation, the stagnation enthalpy may be written as

$$
h_{0}=c_{p} T_{0}
$$

which motivates the definition of the stagnation temperature

$$
T_{0}:=T^{E}+\frac{\left|\boldsymbol{u}^{E}\right|^{2}}{2 c_{p}} .
$$

Thus, in steady, adiabatic, inviscid ideal-gas flow, the stagnation temperature is conserved. Kinetic energy changes associated with acceleration or deceleration of the flow are exactly balanced by corresponding changes in temperature.

### 4.7.4 Stagnation pressure and density

If, in addition, the flow is isentropic (reversible and adiabatic), the stagnation pressure $p_{0}$ and stagnation density $\rho_{0}$ are defined as the pressure and density associated with the stagnation state. For a calorically perfect ideal gas, the isentropic relations give

$$
\frac{p_{0}}{p^{E}}=\left(\frac{T_{0}}{T^{E}}\right)^{\frac{\gamma}{\gamma-1}}, \quad \frac{\rho_{0}}{\rho^{E}}=\left(\frac{T_{0}}{T^{E}}\right)^{\frac{1}{\gamma-1}},
$$

where $\gamma$ is the ratio of specific heats.
Stagnation properties provide a compact and physically meaningful way to characterize compressible flows. They will appear repeatedly in our analysis of one-dimensional flow, nozzles, and wave phenomena, where many problems reduce to tracking how the flow redistributes energy between kinetic and thermodynamic forms while preserving these invariants.

