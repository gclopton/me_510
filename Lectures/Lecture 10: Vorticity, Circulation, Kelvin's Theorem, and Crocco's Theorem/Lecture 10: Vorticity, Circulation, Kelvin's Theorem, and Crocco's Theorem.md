In Lectures 8-9, we established the governing equations of inviscid compressible flow in differential form and closed them using thermodynamic relations. That development introduced entropy, the speed of sound, and the Mach number, revealing that thermodynamics does more than supply constitutive information: it constrains the structure of admissible flow fields.

In this lecture, we focus on one particularly important structural feature of fluid motion: vorticity. Our goal is to understand how vorticity evolves in compressible flow, how it is constrained by thermodynamics, and why many high-speed flows are close to irrotational not by assumption, but by physical consequences manifested by the governing equations.
This lecture serves as a bridge. It connects the thermodynamic ideas developed previously to the mathematical simplifications that will be exploited in subsequent lectures, where the Euler equations reduce to scalar partial differential equations whose character depends fundamentally on the Mach number.

## 1 Vorticity, circulation, and geometric meaning

### 1.1 Definition of vorticity

The vorticity of a velocity field $\boldsymbol{u}(\boldsymbol{x}, t)$ is defined as

$$
\omega:=\nabla \times u .
$$

Vorticity is a kinematic quantity that measures the local rotational content of the flow. It characterizes the tendency of fluid elements to undergo rigid-body rotation about their center of mass, distinct from deformation or compression.

While the definition involves a differential operator, its physical meaning is most clearly understood through its relationship to circulation.

### 1.2 Circulation and its relation to vorticity

Let $C$ be a closed curve in space. The circulation of the velocity field around $C$ is defined as

$$
\Gamma:=\oint_{C} u \cdot d \ell
$$

Circulation measures the net tangential motion of the fluid along the curve and provides an integral measure of rotational motion.

The connection between circulation and vorticity follows directly from Stokes' theorem. If $\mathcal{S}$ is any surface bounded by $C$ with outward unit normal $n$, then

$$
\Gamma=\oint_{C} \boldsymbol{u} \cdot d \boldsymbol{\ell}=\int_{\mathcal{S}}(\nabla \times \boldsymbol{u}) \cdot \boldsymbol{n} d S=\int_{\mathcal{S}} \boldsymbol{\omega} \cdot \boldsymbol{n} d S
$$

This relation shows that vorticity may be interpreted as the circulation per unit area in the limit of an infinitesimal surface.

### 1.3 Why circulation is the natural quantity to study

The integral definition of circulation plays a central role in the dynamics of vorticity for two reasons.
First, circulation is defined for any closed curve in space and provides an integral measure of rotational motion associated with the velocity field. When the curve is later chosen to move with the fluid, circulation becomes a natural quantity for studying how rotational motion evolves dynamically along particle paths.

Second, circulation allows vorticity dynamics to be linked directly to the momentum equation through integral statements. As we will see, this perspective leads naturally to Kelvin's circulation theorem, which identifies the precise conditions under which vorticity is conserved or generated in inviscid compressible flow.

In the sections that follow, we will examine how circulation evolves for material loops and how thermodynamic constraints-particularly the role of entropy-enter that evolution.

## 2 Kelvin's circulation theorem

We now ask a precise dynamical question:
How does the circulation around a closed loop of fluid particles evolve in time?
Let $\mathcal{C}(t)$ denote a closed curve that moves with the fluid velocity $\boldsymbol{u}(\boldsymbol{x}, t)$. The circulation around this material loop is

$$
\Gamma(t):=\oint_{C(t)} \boldsymbol{u} \cdot d \boldsymbol{\ell}
$$

Our goal is to compute $\frac{d \Gamma}{d t}$ using the governing equations and to identify the conditions under which circulation is conserved.

### 2.1 Time derivative of circulation for a material loop

The circulation

$$
\Gamma(t):=\oint_{C(t)} \boldsymbol{u} \cdot d \boldsymbol{\ell}
$$

is a line integral over a time-dependent domain: the curve $C(t)$ moves and deforms in time. Therefore, the relevant notion of time derivative is the one emphasized in Lecture 2 for integrals over moving domains: we differentiate by comparing corresponding points on the moving curve itself. (This is not the Reynolds transport theorem; RTT concerns the evolution of integrals representing material content in a region, whereas $\Gamma$ is defined on the curve.)

In our case, $C(t)$ is a material loop, meaning that each point on the curve is a fluid particle and thus moves with the fluid velocity $\boldsymbol{u}$. With that interpretation fixed, an analogue of the moving-domain differentiation rule from Lecture 2 gives the following transport identity:

$$
\frac{d}{d t} \oint_{C(t)} \boldsymbol{u} \cdot d \boldsymbol{\ell}=\oint_{C(t)} \frac{D \boldsymbol{u}}{D t} \cdot d \boldsymbol{\ell}
$$

We will simply use this identity in what follows; a careful derivation is analogous to what we have done in Lecture 2, for 1D line-integrals rather than 3D domain integrals. You may re-visit this derivation in, say, a future homework.

Substituting the primitive momentum equation for inviscid flow,

$$
\rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f}
$$

gives

$$
\frac{d \Gamma}{d t}=\oint_{C(t)}\left(-\frac{1}{\rho} \nabla p+f\right) \cdot d \boldsymbol{l}
$$

### 2.2 Restriction to conservative body forces: physical motivation and consequences

Kelvin's theorem is not intended to describe all possible forcing mechanisms; rather, it isolates a class of flows in which vorticity evolution is governed entirely by internal fluid dynamics and thermodynamics.

In many compressible-flow applications of interest-including atmospheric flows, aerodynamics in uniform gravitational fields, or laboratory-scale gas dynamics-the dominant body forces arise from external fields that act uniformly on fluid elements. Gravity is the canonical example. Such forces do not depend on the velocity, orientation, or deformation of the fluid element, and they do not perform work in a path-dependent way. Physically, they supply or remove energy but do not inject rotational motion into the flow.

This motivates restricting attention to conservative body forces: forces for which the work done on a fluid particle depends only on its position, not on the path taken. Under this assumption, the force per unit mass may be written as the gradient of a scalar potential,

$$
f=-\nabla \Phi
$$

where $\Phi(\boldsymbol{x})$ represents the potential energy per unit mass associated with the external field.
This representation is not a mathematical convenience; it encodes the physical meaning of a conservative force. If the work done by the body force on a fluid particle depends only on the particle's position and not on the path taken to reach it, then the work done between two points must equal the difference of a scalar potential evaluated at those points. In continuum terms, this path independence implies that the force field has no circulatory component: its line integral around any closed curve vanishes.

For smooth fields in a simply connected domain, this condition is equivalent to the force per unit mass being expressible as the gradient of a scalar potential. The scalar $\Phi(\boldsymbol{x})$ therefore represents the potential energy per unit mass associated with the external field, and the force acts to drive fluid particles down gradients of that potential.

The implication for circulation dynamics is immediate. When the momentum equation is integrated around a closed material loop, the contribution of a conservative body force takes the form

$$
\oint_{C(t)} \boldsymbol{f} \cdot d \boldsymbol{\ell}=-\oint_{C(t)} \nabla \Phi \cdot d \boldsymbol{\ell}
$$

Because the line integral of a gradient around any closed curve vanishes, this term contributes nothing to the evolution of circulation. In other words, conservative body forces can redistribute
energy but cannot generate or destroy circulation. Any change in circulation must therefore arise from other mechanisms-such as pressure gradients interacting with density variations or entropy gradients- which will be examined next.

### 2.3 Dealing with the pressure term under isentropic conditions

We now examine the consequences of the isentropic assumption for the pressure term in the circulation equation.

For a simple compressible substance, pressure generally depends on both density and entropy,

$$
p=p(\rho, s) .
$$

If the flow is isentropic, however, entropy is uniform and ceases to be an independent thermodynamic variable. Under this restriction, pressure becomes a single-valued function of density alone:

$$
p=p(\rho) .
$$

This reduction has an important structural consequence for the pressure force. To see it, recall the thermodynamic identity for a simple compressible substance,

$$
T d s=d e+p d\left(\frac{1}{\rho}\right)
$$

Under isentropic conditions ( $d s=0$ ), this reduces to

$$
d e=-p d\left(\frac{1}{\rho}\right)
$$

Now recall the specific enthalpy,

$$
h=e+\frac{p}{\rho},
$$

and take its differential to get

$$
d h=d e+d\left(\frac{p}{\rho}\right)=d e+\frac{1}{\rho} d p-\frac{p}{\rho^{2}} d \rho
$$

Substituting the isentropic relation for de yields a cancellation of the last term, leaving

$$
d h=\frac{1}{\rho} d p
$$

Taking spatial gradients, we obtain the key result

$$
\frac{1}{\rho} \nabla p=\nabla h .
$$

This identity shows that, under isentropic conditions, the pressure force per unit mass is itself a pure gradient. In other words, pressure forces become conservative in exactly the same sense discussed in Section 2.2.

Implication for circulation. Returning to the circulation evolution equation,

$$
\frac{d \Gamma}{d t}=-\oint_{C(t)} \frac{1}{\rho} \nabla p \cdot d \ell
$$

we may now write

$$
\frac{d \Gamma}{d t}=-\oint_{C(t)} \nabla h \cdot d \ell
$$

Because $h$ is a scalar field, the line integral of its gradient around any closed curve vanishes:

$$
\oint_{C(t)} \nabla h \cdot d \ell=0 .
$$

Thus, under the combined assumptions of inviscid flow, conservative body forces, and isentropy, the pressure term-like the body-force term-cannot generate or destroy circulation. Both contributions drop out for the same fundamental reason: they reduce to line integrals of gradients around closed loops.

This completes the circulation balance and sets the stage for Kelvin's circulation theorem.

### 2.4 Kelvin's circulation theorem

We have shown that if:

- the flow is inviscid,
- body forces are conservative,
- the flow is isentropic,
then

$$
\frac{d \Gamma}{d t}=0
$$

This result is known as Kelvin's circulation theorem: the circulation around a closed material loop is conserved in inviscid, isentropic flow with conservative body forces.

### 2.5 Interpretation

Kelvin's theorem is not purely kinematic. It is a dynamical result that rests crucially on thermodynamics. The isentropic constraint reduces the thermodynamic degrees of freedom, causing pressure forces to become conservative and incapable of generating circulation.

This theorem explains why many compressible flows-despite large variations in density and pressure-remain irrotational over substantial regions of the flow. In the next section, we will relax the isentropic assumption and identify the mechanism by which entropy gradients generate vorticity.

## 3 Crocco's theorem: vorticity, entropy, and stagnation enthalpy

Kelvin's circulation theorem showed that, under certain conditions (inviscid flow, conservative body forces, and isentropic motion), circulation around a material loop is conserved. This immediately implies that irrotational flow is preserved in time.

Crocco's theorem generalizes this result. Rather than asking when vorticity is conserved, it asks a deeper question: when and how is vorticity generated in compressible flow? The answer reveals a precise connection between vorticity, entropy gradients, and stagnation enthalpy gradients.

### 3.1 Starting point: the steady inviscid momentum equation

We begin with the inviscid momentum equation written in primitive form:

$$
\rho \frac{D \boldsymbol{u}}{D t}=-\nabla p+\rho \boldsymbol{f}
$$

As in the discussion of Kelvin's theorem, we assume conservative body forces, so that $\boldsymbol{f}=-\nabla \Phi$ for some potential $\Phi(\boldsymbol{x})$. Dividing by $\rho$ gives

$$
\frac{D \boldsymbol{u}}{D t}=-\frac{1}{\rho} \nabla p-\nabla \Phi
$$

We now rewrite the material acceleration using the vector identity

$$
\frac{D \boldsymbol{u}}{D t}=\partial_{t} \boldsymbol{u}+(\boldsymbol{u} \cdot \nabla) \boldsymbol{u}=\partial_{t} \boldsymbol{u}+\nabla\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)-\boldsymbol{u} \times(\nabla \times \boldsymbol{u}) .
$$

Introducing the vorticity $\boldsymbol{\omega}:=\nabla \times \boldsymbol{u}$, we obtain

$$
\partial_{t} \boldsymbol{u}-\boldsymbol{u} \times \boldsymbol{\omega}+\nabla\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)=-\frac{1}{\rho} \nabla p-\nabla \Phi
$$

### 3.2 Introducing stagnation enthalpy

We now use thermodynamics to reorganize the pressure-gradient term. From the Gibbs relation,

$$
d h=T d s+\frac{1}{\rho} d p
$$

which implies, at the level of spatial gradients,

$$
\frac{1}{\rho} \nabla p=\nabla h-T \nabla s
$$

Substituting this into the momentum equation yields

$$
\partial_{t} \boldsymbol{u}-\boldsymbol{u} \times \boldsymbol{\omega}+\nabla\left(\frac{1}{2}|\boldsymbol{u}|^{2}\right)=-\nabla h+T \nabla s-\nabla \Phi .
$$

We now group the gradient terms by defining the stagnation enthalpy

$$
h_{0}:=h+\frac{1}{2}|\boldsymbol{u}|^{2}+\Phi
$$

This stagnation enthalphy will be a useful way to express Crocco's theorem. It is also a variable has important physical meaning. In inviscid flow, pressure forces do not merely "add energy": they redistribute it between thermal (enthalpy) and mechanical (kinetic) forms. Under adiabatic conditions ( $\dot{q}_{h}=0$ ) and conservative body forces ( $f=-\nabla \Phi$ ), one can combine the momentum and energy equations to show that $h_{0}$ is materially conserved:

$$
\frac{D h_{0}}{D t}=0 .
$$

Thus, $h_{0}$ represents the total mechanical-thermal energy carried per unit mass by a fluid element, and it provides a natural scalar whose spatial variations can be directly tied to vorticity through Crocco's theorem.

### 3.3 Crocco's theorem

With the definition of stagnation enthalpy, we arrive at Crocco's theorem

$$
\partial_{t} \boldsymbol{u}-\boldsymbol{u} \times \boldsymbol{\omega}=-\nabla h_{0}+T \nabla s .
$$

It expresses vorticity not as a primitive quantity, but as a consequence of thermodynamic gradients. Vorticity arises when gradients of stagnation enthalpy or entropy are present and misaligned with the velocity field.

### 3.4 Physical interpretation (steady and unsteady viewpoints)

The term $-\partial_{t} u$ represents local (Eulerian) acceleration. In unsteady flows, this acceleration contributes directly to the balance between vorticity and thermodynamic gradients, and it can obscure the purely thermodynamic mechanisms of vorticity generation. For this reason, many discussions of Crocco's theorem focus on the steady case, where

$$
\partial_{t} \boldsymbol{u}=0 \quad \Longrightarrow \quad \boldsymbol{\omega} \times \boldsymbol{u}=\nabla h_{0}-T \nabla s .
$$

We will use this steady form to sharpen physical interpretation; the unsteady term can be restored whenever needed.

Key consequences in steady flow. The steady Crocco relation makes the sources of rotational motion transparent:

- Isentropic and uniform-stagnation-enthalpy flows are irrotational. If $\nabla s=\mathbf{0}$ and $\nabla h_{0}=\mathbf{0}$, then $\boldsymbol{\omega} \times \boldsymbol{u}=\mathbf{0}$. In regions where $\boldsymbol{u} \neq \mathbf{0}$, this forces $\boldsymbol{\omega}=\mathbf{0}$, so the flow is irrotational. This recovers (and strengthens) the insight behind Kelvin's theorem: under sufficiently restrictive conditions, rotational content cannot be created.
- Entropy gradients generate vorticity. When $\nabla s \neq \mathbf{0}$, the term $-T \nabla s$ acts as a direct thermodynamic driver of vorticity. This is one reason shocks, heat addition, and other irreversible processes (which create entropy gradients) are commonly associated with rotational flow features.
- Stagnation-enthalpy gradients generate vorticity. Spatial variations in $h_{0}$ also act as a driver. Physically, if the total mechanical-thermal energy carried by the flow varies from place to place, the momentum balance cannot remain purely potential; rotational motion is induced unless those gradients align in a special way with the velocity field.

Geometric reading. The left-hand side $\boldsymbol{\omega} \times \boldsymbol{u}$ shows that Crocco's theorem constrains only the component of vorticity not parallel to the velocity. Equivalently, it determines how vorticity must orient itself relative to streamlines in the presence of thermodynamic gradients. This viewpoint will be especially useful as we transition to potential-flow models, where $\boldsymbol{\omega}=\mathbf{0}$ allows $\boldsymbol{u}$ to be expressed as the gradient of a scalar potential.

### 3.5 Connection to potential flow

A particularly important consequence follows immediately. If the flow is steady, inviscid, isentropic, and has uniform stagnation enthalpy, then Crocco's theorem implies $\omega=0$. Under these conditions, the velocity field may be written as the gradient of a scalar potential,

$$
\boldsymbol{u}=\nabla \phi,
$$

reducing the Euler equations to a single scalar partial differential equation.
This observation motivates the study of compressible potential flow in the next lecture, where we will see how thermodynamics and Mach number determine the mathematical character of the governing equations.

