In the previous lecture, we derived the governing equations of inviscid compressible flow in differential form and discussed how different PDE representations encode different physical viewpoints. We also emphasized that these equations are not complete on their own: to be closed, they require thermodynamic relations connecting pressure, density, and internal energy.

That need for closure is not merely algebraic. Thermodynamics places fundamental constraints on how a fluid can respond to compression, heating, and motion. In this lecture, we introduce entropy as a thermodynamic state variable and examine how it is constrained by the second law. We then use entropy to define the speed of sound, a characteristic response speed of the fluid, and introduce the Mach number as a natural dimensionless parameter.

These quantities will play a central role in characterizing solutions of the governing equations and in motivating simplified models in the lectures that follow.

## 1 The second law of thermodynamics and entropy

### 1.1 Entropy as a thermodynamic state variable

Entropy, denoted $s$, is a ==thermodynamic state variable==. For a simple compressible substance, it may be expressed as a function of other state variables, for example

$$
s=s(\rho, e)
$$

or equivalently as $s(p, \rho)$ or $s(T, \rho)$, depending on the chosen thermodynamic description.
Unlike mass, momentum, or energy, entropy is not generally conserved. Instead, it is constrained by the second law of thermodynamics, which distinguishes between reversible and irreversible processes. This distinction will prove crucial in compressible flow.

### 1.2 The second law of thermodynamics: fundamental statement and balance form

Unlike mass, momentum, and energy, entropy does not satisfy a conservation law. Instead, the second law provides a balance principle with an inequality constraint: entropy may be transported and supplied by heat transfer, and it may also be produced internally by irreversible processes, but it cannot be destroyed.

## Fundamental statement (material system form)

Let $\Omega(t)$ be a material volume moving with the fluid. The second law may be stated as:
The rate of change of the total entropy of a material system equals the entropy supplied by heat transfer plus the entropy produced internally, and the internal production is nonnegative.

Writing total entropy as

$$
S_{\Omega}(t):=\int_{\Omega(t)} \rho s d V
$$

this becomes the integral balance

$$
\frac{d}{d t} \int_{\Omega(t)} \rho s d V=\int_{\Omega(t)} \frac{\rho \dot{q}_{h}}{T} d V-\int_{\partial \Omega(t)} \frac{\boldsymbol{q}_{h} \cdot \boldsymbol{n}}{T} d S+\int_{\Omega(t)} \dot{s}_{\mathrm{irr}} d V
$$

Here:

- $s$ is the specific entropy,
- $\boldsymbol{q}_{h}$ is the heat flux vector,
- $\dot{q}_{h}$ is volumetric heat addition per unit mass (positive or negative),
- $T$ is temperature,
- $\dot{s}_{\text {irr }}$ is the irreversible entropy production rate per unit volume.

**Remark on heat flux versus volumetric heat addition:** The quantities $\boldsymbol{q}_{h}$ and $\dot{q}_{h}$ represent distinct physical mechanisms and should not be conflated. The heat flux $\boldsymbol{q}_{h}$ describes the transport of thermal energy across surfaces due to microscopic motion (e.g. conduction) and is an internal response of the fluid that requires a constitutive law, such as Fourier's law. In contrast, the volumetric heat addition $\dot{q}_{h}$ represents direct energy input or extraction within the fluid volume (e.g. chemical reactions, radiative heating, or imposed source terms) and is typically prescribed as part of the problem setup. These mechanisms may act independently: a flow may exhibit heat conduction with no volumetric heating, volumetric heating with no heat flux, or neither.

The terms in the balance law represent entropy supplied by volumetric heating, entropy supplied by heat flux through the boundary, and entropy produced internally by irreversible processes, respectively. The second-law moreover constrains irreversible processes to have the property

$$
\dot{s}_{\text {irr }} \geq 0 \quad \text { (pointwise). }
$$

## Conservative continuum form (arbitrary control volume)

Now consider an arbitrary control volume $\Omega$. Applying the Reynolds transport theorem to $\int_{\Omega} \rho s d V$ and localizing (as in Lectures 3-4) yields the conservative local entropy balance:

$$
\partial_{t}(\rho s)+\nabla \cdot\left(\rho s \boldsymbol{u}+\frac{\boldsymbol{q}_{h}}{T}\right)=\frac{\rho \dot{q}_{h}}{T}+\dot{s}_{\mathrm{irr}} .
$$

This equation has the same "transport + sources" structure as the other balance laws:

- $\partial_{t}(\rho s)+\nabla \cdot(\rho s \boldsymbol{u})$ represents advective transport of entropy,
- $\nabla \cdot\left(\boldsymbol{q}_{h} / T\right)$ represents entropy transfer due to heat conduction,
- $\rho \dot{q} / T$ represents entropy supplied by volumetric heating or cooling,
- $\dot{s}_{\text {irr }} \geq 0$ represents entropy produced internally.


## Irreversibility made explicit

Since viscous stresses were introduced earlier, it is useful to record a standard representation of the irreversible entropy production:

$$
\dot{\mathrm{s}}_{\text {irr }}=\underbrace{\frac{1}{T} \boldsymbol{\tau}: \nabla \boldsymbol{u}}_{\text {viscous dissipation }}+\underbrace{\boldsymbol{q}_{h} \cdot \nabla\left(\frac{1}{T}\right)}_{\text {thermal diffusion }}+\dot{s}_{\text {other }}, \quad \dot{s}_{\text {other }} \geq 0 .
$$

The term $\dot{s}_{\text {other }}$ represents additional irreversible mechanisms not modeled explicitly here, such as species diffusion, chemical reactions, radiative irreversibility, or phase change; like viscous dissipation and thermal diffusion, all such contributions must be nonnegative to satisfy the second law.

Under standard constitutive assumptions (positive viscosity and Fourier heat conduction with positive thermal conductivity), each contribution is nonnegative, consistent with the second law.

### 1.3 Specialization: inviscid and adiabatic flow

In the inviscid model emphasized in this course, we set $\boldsymbol{\tau}=\mathbf{0}$. If the flow is also adiabatic with no heat conduction and no volumetric heat addition, then

$$
\boldsymbol{\tau}=\mathbf{0}, \quad \boldsymbol{q}_{h}=\mathbf{0}, \quad \dot{q}_{h}=0, \quad \dot{s}_{\mathrm{irr}}=0
$$

Under these assumptions, the entropy balance reduces to

$$
\partial_{t}(\rho s)+\nabla \cdot(\rho s \boldsymbol{u})=0
$$

or equivalently (using continuity),

$$
\frac{D s}{D t}=0 .
$$

Physical meaning. This result does not assert that entropy is universally conserved. It states that, in the idealized limit of inviscid, adiabatic flow with no irreversible mechanisms active, each fluid element carries its entropy unchanged as it moves. When viscosity, heat conduction, or other irreversible processes are present, entropy is produced internally, and the second law requires that this production be nonnegative.

## 2 Speed of sound as a thermodynamic response

### 2.1 A thermodynamic thought experiment

We now introduce the speed of sound by posing a purely thermodynamic question. Consider an infinitesimal compression of a fluid element and ask:

How does the pressure change in response to a small change in density?
To make this question well-defined, we assume:

- the response is fast and sufficiently weak that no entropy-changing mechanisms (heat flux, volumetric heating, or irreversible processes) have time to act, so the thermodynamic response is isentropic,
- the perturbation is small, so the response is linear.

Under these assumptions, the pressure response is characterized by the derivative

$$
\left(\frac{\partial p}{\partial \rho}\right)_{s}
$$

This derivative is a material property: it depends only on the thermodynamic behavior of the fluid, not on its motion.

### 2.2 Why this derivative defines a speed

The physical significance of this derivative becomes apparent from its dimensions. Pressure has units of force per area, while density has units of mass per volume. Their ratio therefore has units

$$
\left[\frac{p}{\rho}\right]=\frac{\text { length }^{2}}{\text { time }^{2}} .
$$

Thus, simply asking how pressure responds to density under fast, reversible compression produces a quantity with the dimensions of a speed squared. This observation is not imposed by dynamics; it emerges directly from thermodynamics.

The derivative $(\partial p / \partial \rho)_{s}$ measures how "stiff" the medium is to compression. That stiffness sets the characteristic speed at which small compressive disturbances propagate through the fluid. For this reason, we define the speed of sound $a$ by

$$
a^{2}:=\left(\frac{\partial p}{\partial \rho}\right)_{s}
$$

### 2.3 Speed of sound for a calorically perfect ideal gas

For a calorically perfect ideal gas, the equation of state is $p=\rho R T$, and isentropic processes satisfy $p \rho^{-\gamma}=$ const, where $\gamma$ is the ratio of specific heats. Differentiating this relation yields

$$
a^{2}=\gamma \frac{p}{\rho}=\gamma R T \text {. }
$$

This expression shows that, for an ideal gas, the speed of sound depends only on the thermodynamic state of the fluid. The assumptions underlying this result-ideal gas behavior and constant specific heats-should be kept in mind when applying it.

## 3 Mach number

Once a characteristic material response speed has been identified, it is natural to compare it to the flow speed. This motivates the definition of the Mach number

$$
M:=\frac{|\boldsymbol{u}|}{a} .
$$

The Mach number measures the competition between two effects: advection of fluid by the flow itself and the ability of the medium to communicate pressure changes through acoustic response. As we will see in subsequent lectures, this competition plays a central role in shaping the behavior and structure of compressible flows.

## 4 Closing remarks

At this point, we have the governing equations of inviscid compressible flow in differential form together with thermodynamic relations that constrain entropy and define a characteristic response speed. These ingredients already tell us something about the character of the equations through the Mach number.

At the same time, the governing equations remain highly coupled and difficult to interpret or solve in general. In the next lecture, we will examine how thermodynamic properties, particularly entropy, interact with the momentum equation to control the generation and transport of vorticity. This analysis will reveal conditions under which the governing equations can be meaningfully simplified, leading to models that are both more interpretable and more tractable.

