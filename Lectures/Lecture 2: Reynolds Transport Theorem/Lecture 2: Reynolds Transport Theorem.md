## 1 Preliminaries: time derivatives of integrals

In the previous lecture, we studied time derivatives of pointwise quantities in a fluid. We saw that the meaning of a time derivative depends on what is held fixed: a spatial location (Eulerian viewpoint) or a material element (Lagrangian viewpoint). This distinction was essential for correctly interpreting unsteady flow phenomena.
In this lecture, we ask the analogous question at the integral level. As fluid mechanicians, we frequently work with integrals of physical quantities-mass, momentum, energy, or passive scalarsover regions of space. These integrals appear naturally in conservation laws, which are inherently dynamic. Our goal is therefore to understand how to take time derivatives of integrals defined over finite regions in a flow.

The subtlety is that there is more than one reasonable notion of a time derivative for such integrals. Just as in the pointwise setting, different notions arise depending on what we choose to hold fixed when differentiating.

### 1.1 A human-defined region of space

Let $\Omega(t) \subset \mathbb{R}^{3}$ be a region of physical space chosen by the observer. To describe its motion, we introduce a reference configuration $\Omega_{\text {ref }} \subset \mathbb{R}^{3}$ and a domain flow map

$$
x=\psi(\xi, t), \quad \xi \in \Omega_{\mathrm{ref}}
$$

so that

$$
\Omega(t)=\left\{\boldsymbol{\psi}(\boldsymbol{\xi}, t): \boldsymbol{\xi} \in \Omega_{\mathrm{ref}}\right\} .
$$

The map $\psi$ describes how the region $\Omega$ moves in time. It is entirely user-defined and need not be related to the fluid motion.

We emphasize that this map is not the material flow map. As in the previous lecture, we reserve the symbol $\phi$ for the material flow map, which describes the motion of fluid elements. Only in the special case where $\Omega(t)$ is a material volume do we have $\boldsymbol{\psi}=\phi$.
Let $q$ be a physical quantity associated with the fluid, with Eulerian representation $q^{E}(\boldsymbol{x}, t)$. The integral of interest is

$$
I_{\Omega}(t):=\int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V
$$

### 1.2 What does it mean to differentiate an integral in time?

At first glance, one might expect there to be a single, unambiguous time derivative of $I_{\Omega}(t)$. However, just as in the pointwise case, different notions of time differentiation arise depending on what is held fixed during the comparison between times.

There are two distinct questions we might ask:

- How does the integral change when $q$ is evaluated at corresponding spatial points in the region $\Omega(t)$ as the region evolves?
- How does the integral change when $q$ is evaluated at corresponding material elements that occupy $\Omega(t)$ as time evolves?

These two questions are not equivalent. They compare different things, and therefore lead to different mathematical results.

This distinction is the exact analog of the Eulerian and Lagrangian time derivatives introduced in the pointwise setting:

- In the Eulerian pointwise derivative, we hold spatial position fixed.
- In the Lagrangian pointwise derivative, we hold material identity fixed.

At the integral level, the same conceptual split occurs.

### 1.3 Two perspectives on time derivatives of integrals

To make this precise, it is helpful to summarize the analogy between pointwise and integral derivatives:

|  | Viewpoint | Pointwise quantity | Integral quantity |
| :--- | :--- | :--- | :--- |
| Eulerian | Hold spatial location fixed | $\left(\frac{\partial}{\partial t}\right)_{\boldsymbol{x}}$ | Compare $q$ at corresponding spatial points in $\Omega(t)$ |
| Lagrangian | Hold material identity fixed | $\left(\frac{\partial}{\partial t}\right)_{\boldsymbol{x}_{0}}$ | Compare $q$ at corresponding material elements occupying $\Omega(t)$ |

In both cases, the distinction does not come from choosing a different symbol for the time derivative. Rather, it comes from how the quantity being differentiated is parameterized. Once the parameterization is fixed, the meaning of the time derivative is determined by which variables are held constant.

### 1.4 Outline of what follows

The remainder of this lecture develops these two notions of time derivatives for integrals.

- In Section 2, we compute the time derivative of $I_{\Omega}(t)$ by comparing values of $q$ at corresponding spatial locations in the evolving region. This calculation answers a purely mathematical question about differentiating an integral over a time-dependent domain. It does not track material transport.
- In Section 3, we compute the time derivative of an integral parameterized by material elements that occupy $\Omega(t)$. This requires introducing a time-dependent subset of material space and leads to the Reynolds transport theorem. This derivative is the appropriate one for conservation laws, which concern the evolution of physical quantities carried by material elements.

Although these two derivatives act on integrals over the same physical region $\Omega(t)$, they answer different questions and generally produce different results. Distinguishing between them carefully is essential for avoiding confusion when working with unsteady flows.

## 2 Eulerian time derivative of an integral over a moving domain

In this section, we compute the time derivative of

$$
I_{\Omega}(t)=\int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V
$$

in the sense described in Section 1: we compare values $q$ at corresponding spatial locations in the region $\Omega(t)$ as the region evolves in time. This derivative does not track material elements and does not encode conservation; it answers a purely mathematical question about differentiating an integral whose domain depends on time.

### 2.1 Rewriting the integral in reference coordinates

The difficulty in differentiating $I_{\Omega}(t)$ is that the domain of integration depends on time. To handle this, we rewrite the integral using the reference configuration $\Omega_{\text {ref }}$ and the domain flow map

$$
x=\psi(\xi, t), \quad \xi \in \Omega_{\mathrm{ref}}
$$

Using this change of variables, we may write

$$
I_{\Omega}(t)=\int_{\Omega_{\mathrm{ref}}} q^{E}(\psi(\xi, t), t) J_{\psi}(\xi, t) d V_{\xi}
$$

where

$$
J_{\psi}(\xi, t):=\operatorname{det}\left(\nabla_{\xi} \psi(\xi, t)\right)
$$

is the Jacobian determinant associated with the domain map.
This step is purely geometric. We have not changed the meaning of the integral; we have only rewritten it so that the domain of integration is time-independent.

### 2.2 Time differentiation at fixed reference coordinates

Because the integration variable $\boldsymbol{\xi}$ ranges over the fixed region $\Omega_{\text {ref }}$, we may now differentiate under the integral sign. Doing so corresponds to comparing values of the integrand at fixed reference coordinates $\boldsymbol{\xi}$, which in turn correspond to fixed spatial locations as the domain moves.

We obtain

$$
\frac{d}{d t} I_{\Omega}(t)=\int_{\Omega_{\mathrm{ref}}} \frac{\partial}{\partial t}\left[q^{E}(\psi(\boldsymbol{\xi}, \cdot), \cdot) J_{\psi}(\boldsymbol{\xi}, \cdot)\right](t) d V_{\xi}
$$

Applying the product rule yields two contributions:

$$
\int_{\Omega_{\mathrm{ref}}}\left(\frac{\partial}{\partial t}\left[q^{E}(\boldsymbol{\psi}(\boldsymbol{\xi}, \cdot), \cdot)\right](t) J_{\psi}(\boldsymbol{\xi}, t)+q^{E}(\boldsymbol{\psi}(\boldsymbol{\xi}, t), t) \frac{\partial J_{\psi}(\boldsymbol{\xi}, t)}{\partial t}\right) d V_{\xi} .
$$

To proceed, we rewrite both time-derivative terms in a form that can be expressed in spatial variables.

Step 1: chain rule for the field term. Define the domain (Eulerian) velocity field

$$
\boldsymbol{w}^{E}(\boldsymbol{x}, t):=\left.\frac{\partial}{\partial t} \psi(\boldsymbol{\xi}, \cdot)\right|_{\boldsymbol{\xi}}(t), \quad \boldsymbol{x}=\psi(\boldsymbol{\xi}, t) .
$$

Then, by the chain rule,

$$
\frac{\partial}{\partial t}\left[q^{E}(\boldsymbol{\psi}(\boldsymbol{\xi}, \cdot), \cdot)\right](t)=\partial_{t} q^{E}(\boldsymbol{x}, t)+\boldsymbol{w}^{E}(\boldsymbol{x}, t) \cdot \nabla q^{E}(\boldsymbol{x}, t), \quad \boldsymbol{x}=\boldsymbol{\psi}(\boldsymbol{\xi}, t) .
$$

Step 2: time derivative of the Jacobian. We will state, and not derive, the Jacobian transport relation

$$
\frac{\partial J_{\psi}(\boldsymbol{\xi}, t)}{\partial t}=J_{\psi}(\boldsymbol{\xi}, t) \nabla \cdot \boldsymbol{w}^{E}(\boldsymbol{x}, t), \quad \boldsymbol{x}=\boldsymbol{\psi}(\boldsymbol{\xi}, t) .
$$

This important result is one that, for reasons of time, we will not explicitly derive. The derivation is well within your grasp if you are careful with the notation and use concepts we built up to know. But for now, let us take this expression as a fact and focus on its interpretation. The interpretation is most physical when dealing with material elements, so we will focus our understanding on the case when $\boldsymbol{\psi}=\boldsymbol{\phi}$, and $\boldsymbol{w}^{E}=\boldsymbol{u}^{E}$. In this case, the expression states that the local rate of change of volume (relative to the reference configuration) on the lefthand side is governed by the divergence of the Eulerian velocity field. When $\nabla \cdot \boldsymbol{u}^{E}=0$, the local volume is preserved; when $\nabla \cdot \boldsymbol{u}^{E} \neq 0$, the volume changes at a rate proportional both to the divergence and to the current value of the Jacobian (volume change factor) itself. For those that have been told to take at face value that $\nabla \cdot \boldsymbol{u}^{E}$ describes the volume change of fluid elements, you now see the relation that describes why this statement is true!

Combining the two steps. Substituting these identities into the product-rule expression yields

$$
\frac{d}{d t} I_{\Omega}(t)=\int_{\Omega_{\mathrm{ref}}} J_{\psi}(\boldsymbol{\xi}, t)\left[\partial_{t} q^{E}(\boldsymbol{x}, t)+\boldsymbol{w}^{E}(\boldsymbol{x}, t) \cdot \nabla q^{E}(\boldsymbol{x}, t)+q^{E}(\boldsymbol{x}, t) \nabla \cdot \boldsymbol{w}^{E}(\boldsymbol{x}, t)\right]_{\boldsymbol{x}=\boldsymbol{\psi}(\xi, t)} d V_{\xi} .
$$

### 2.3 Returning to spatial variables

We now rewrite the result in terms of the physical coordinates $\boldsymbol{x}$. Using $\boldsymbol{x}=\boldsymbol{\psi}(\boldsymbol{\xi}, t)$ and $d V= J_{\psi} d V_{\xi}$, we obtain

$$
\frac{d}{d t} \int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V=\int_{\Omega(t)}\left[\partial_{t} q^{E}(\boldsymbol{x}, t)+\nabla \cdot\left(q^{E}(\boldsymbol{x}, t) \boldsymbol{w}^{E}(\boldsymbol{x}, t)\right)\right] d V
$$

Finally, applying the divergence theorem gives

$$
\frac{d}{d t} \int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V=\int_{\Omega(t)} \partial_{t} q^{E}(\boldsymbol{x}, t) d V+\int_{\partial \Omega(t)} q^{E}(\boldsymbol{x}, t) \boldsymbol{w}^{E}(\boldsymbol{x}, t) \cdot \boldsymbol{n} d S
$$

### 2.4 Interpretation

This result describes how the integral of a time-dependent field changes when evaluated at corresponding spatial locations in a region that moves in time. The boundary term accounts for the motion of the region itself.

Importantly, this derivative does not track which material elements occupy $\Omega(t)$. If fluid flows into or out of the region, that transport is not accounted for here. For this reason, the result derived in this section is not suitable for expressing conservation laws.

In the next section, we will develop a different time derivative that explicitly tracks material elements occupying $\Omega(t)$. That derivative leads to the Reynolds transport theorem.

## 3 Lagrangian time derivative of an integral: Reynolds transport theorem

In Section 2, we computed the time derivative of

$$
I_{\Omega}(t)=\int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V
$$

by comparing values of $q$ at corresponding spatial locations in the evolving region $\Omega(t)$. That calculation answered a purely mathematical question and made no reference to material transport.

We now turn to a different and more physically meaningful question: How does the integral of $q$ change when we compare values carried by the same material elements as time evolves, even though those elements may enter or leave the region $\Omega(t)$ ?

This question underlies conservation laws and leads to the Reynolds transport theorem.

### 3.1 Why a new parameterization is needed

If $\Omega(t)$ were a material volume, then the same set of fluid elements would occupy the region at all times. In that special case, tracking material elements would be straightforward.

In general, however, $\Omega(t)$ is a human-defined region that does not move with the fluid. As time evolves, fluid elements enter and leave $\Omega(t)$. As a result, there is no fixed subset of material space whose image under the material flow map coincides with $\Omega(t)$ for all times.

To track material elements occupying $\Omega(t)$ at a given time, we must therefore introduce a timedependent subset of material space.

### 3.2 Material elements occupying $\Omega(t)$

Let $\phi\left(x_{0}, t\right)$ denote the material flow map, as in the previous lecture. We define

$$
\mathcal{P}(t):=\left\{\boldsymbol{x}_{0}: \boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right) \in \Omega(t)\right\} .
$$

The set $\mathcal{P}(t)$ consists of the material labels of all fluid elements that occupy $\Omega(t)$ at time $t$.
Unlike the reference region used in Section 2, $\mathcal{P}(t)$ is time dependent. This time dependence is unavoidable: it reflects the physical fact that material elements enter and leave the region.

### 3.3 A material-parameterized integral

Using $\mathcal{P}(t)$, we define a new representation of the integral:

$$
I_{\Omega}^{\boldsymbol{x}_{0}}(t):=\int_{\mathcal{P}(t)} q^{L}\left(\boldsymbol{x}_{0}, t\right) J_{\phi}\left(\boldsymbol{x}_{0}, t\right) d V_{0}
$$

where

$$
q^{L}\left(\boldsymbol{x}_{0}, t\right):=q^{E}\left(\phi\left(\boldsymbol{x}_{0}, t\right), t\right), \quad J_{\phi}\left(\boldsymbol{x}_{0}, t\right):=\operatorname{det}\left(\nabla_{\boldsymbol{x}_{0}} \phi\left(\boldsymbol{x}_{0}, t\right)\right) .
$$

This expression represents the same physical quantity as $I_{\Omega}(t)$. The difference lies entirely in how the integral is parameterized:

- the integration variable $\boldsymbol{x}_{0}$ labels material elements,
- the domain of integration $\mathcal{P}(t)$ identifies which material elements are inside $\Omega(t)$ at time $t$.

Because the independent variable is material identity, any time derivative of $I_{\Omega}^{\boldsymbol{x}_{0}}(t)$ must compare values at fixed material labels. This is the integral analog of a Lagrangian time derivative.

### 3.4 Differentiation of the material-parameterized integral

The time derivative of $I_{\Omega}^{\boldsymbol{x}_{0}}(t)$ involves two sources of time dependence:

- the integrand depends on time through $q^{L}$ and $J_{\phi}$,
- the domain of integration $\mathcal{P}(t)$ depends on time.

Mathematically, this is the same problem encountered in Section 2, but now posed in material space. Applying the same differentiation rule to an integral over a moving domain in $\boldsymbol{x}_{0}$-space yields

$$
\frac{d}{d t} I_{\Omega}^{\boldsymbol{x}_{0}}(t)=\int_{\mathcal{P}(t)} \partial_{t}\left(q^{L} J_{\phi}\right)\left(\boldsymbol{x}_{0}, t\right) d V_{0}+\int_{\partial \mathcal{P}(t)} q^{L}\left(\boldsymbol{x}_{0}, t\right) J_{\phi}\left(\boldsymbol{x}_{0}, t\right) \boldsymbol{V}\left(\boldsymbol{x}_{0}, t\right) \cdot \boldsymbol{n}_{0} d S_{0}
$$

where $\boldsymbol{V} \cdot \boldsymbol{n}_{0}$ is the normal velocity of the boundary $\partial \mathcal{P}(t)$ in material space.

### 3.5 Rewriting the volume term in spatial variables

Using the definition of the material derivative,

$$
\partial_{t} q^{L}\left(\boldsymbol{x}_{0}, t\right)=\partial_{t} q^{E}(\boldsymbol{x}, t)+\boldsymbol{u}^{E}(\boldsymbol{x}, t) \cdot \nabla q^{E}(\boldsymbol{x}, t), \quad \boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right),
$$

together with the Jacobian transport identity

$$
\partial_{t} J_{\phi}=J_{\phi} \nabla \cdot \boldsymbol{u}^{E}
$$

we obtain

$$
\partial_{t}\left(q^{L} J_{\phi}\right)=J_{\phi}\left(\partial_{t} q^{E}+\nabla \cdot\left(q^{E} \boldsymbol{u}^{E}\right)\right) \quad \text { evaluated at } \boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right) .
$$

Changing variables from $\boldsymbol{x}_{0}$ to $\boldsymbol{x}$ yields

$$
\int_{\mathcal{P}(t)} \partial_{t}\left(q^{L} J_{\phi}\right) d V_{0}=\int_{\Omega(t)}\left(\partial_{t} q^{E}+\nabla \cdot\left(q^{E} \boldsymbol{u}^{E}\right)\right) d V
$$

### 3.6 Rewriting the boundary term

The boundary $\partial \mathcal{P}(t)$ corresponds to the preimage, under the material flow map, of the boundary $\partial \Omega(t)$. A fluid element lies on $\partial \mathcal{P}(t)$ precisely when it maps to $\partial \Omega(t)$ at time $t$.

A short geometric argument shows that the normal velocity of $\partial \mathcal{P}(t)$ in material space is determined by the relative motion between the fluid and the domain. Specifically,

$$
\boldsymbol{V} \cdot \boldsymbol{n}_{0}=\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} \quad \text { on } \partial \Omega(t),
$$

where $\boldsymbol{w}^{E}$ is the domain velocity introduced in Section 2.
Using this relation and changing variables from material to spatial coordinates yields

$$
\int_{\partial \mathcal{P}(t)} q^{L} J_{\phi} \boldsymbol{V} \cdot \boldsymbol{n}_{0} d S_{0}=\int_{\partial \Omega(t)} q^{E}(\boldsymbol{x}, t)\left(\boldsymbol{u}^{E}(\boldsymbol{x}, t)-\boldsymbol{w}^{E}(\boldsymbol{x}, t)\right) \cdot \boldsymbol{n} d S .
$$

### 3.7 Reynolds transport theorem

Combining the volume and boundary contributions, we obtain the Reynolds transport theorem:

$$
\frac{d}{d t} \int_{\Omega(t)} q^{E}(\boldsymbol{x}, t) d V=\int_{\Omega(t)} \partial_{t} q^{E}(\boldsymbol{x}, t) d V+\int_{\partial \Omega(t)} q^{E}(\boldsymbol{x}, t)\left(\boldsymbol{u}^{E}-\boldsymbol{w}^{E}\right) \cdot \boldsymbol{n} d S
$$

This result gives the time rate of change of the integral of $q$ when values are compared at corresponding material elements. The boundary term accounts for the transport of $q$ into and out of the region due to relative motion between the fluid and the domain.

### 3.8 Special cases

If the region $\Omega(t)$ is fixed in space, then $\boldsymbol{w}^{E}=0$, and the flux term reduces to the familiar advective flux through the boundary.
If the region $\Omega(t)$ moves with the fluid, so that $\boldsymbol{w}^{E}=\boldsymbol{u}^{E}$, the boundary term vanishes. In that case, the time derivative reduces to the integral of the material derivative over the material volume, as expected from conservation laws.

## 4 Synthesis: Eulerian and Lagrangian derivatives at the integral level

We now step back and synthesize the results of Sections 2 and 3. Although both sections addressed time derivatives of integrals over the same physical region $\Omega(t)$, they answered fundamentally different questions. Understanding this distinction is essential for using these results correctly.

### 4.1 Two derivatives, two comparisons

The key idea is that a time derivative always compares values at different times. What distinguishes the two derivatives developed in this lecture is what is held fixed during that comparison.

- In Section 2, we compared values of $q$ at corresponding spatial locations in the region $\Omega(t)$ as the region moves in time. This led to a time derivative that accounts for the motion of the domain itself, but does not track material transport.
- In Section 3, we compared values of $q$ carried by corresponding material elements that occupy $\Omega(t)$ at each instant. This required reparameterizing the integral in terms of material labels and led to the Reynolds transport theorem.

In both cases, the time derivative itself was the ordinary derivative with respect to $t$. The distinction arose entirely from how the integral was parameterized.

### 4.2 Analogy with pointwise Eulerian and Lagrangian derivatives

This structure mirrors exactly what we encountered in the pointwise setting.
At the pointwise level:

- the Eulerian time derivative compares values at fixed spatial positions,
- the Lagrangian (material) time derivative compares values along material trajectories.

At the integral level:

- the Eulerian derivative of an integral compares values at fixed spatial locations within a moving region,
- the Lagrangian derivative of an integral compares values carried by fixed material elements occupying that region.

In neither case is a new differentiation operator required. Instead, Eulerian and Lagrangian derivatives arise because the quantities being differentiated are functions of different independent variables: spatial position or material identity.

### 4.3 Which derivative should be used?

The appropriate derivative depends on the physical question being asked.

- If the goal is to compute the rate of change of an integral as a purely mathematical objectwithout regard to material transport-the Eulerian derivative from Section 2 is appropriate.
- If the goal is to express conservation laws or to track the evolution of quantities carried by the fluid, the Lagrangian derivative from Section 3 must be used. This derivative accounts explicitly for material entering and leaving the region and leads to the Reynolds transport theorem.

Being explicit about which notion of time derivative is intended, and about how integrals are parameterized, removes much of the ambiguity that often surrounds the Reynolds transport theorem in standard presentations.

### 4.4 Final remark

Throughout this lecture, we have emphasized that clarity about Eulerian and Lagrangian viewpoints is not merely a matter of notation. It is a matter of identifying what physical entities are being compared when time derivatives are taken. At both the pointwise and integral levels, this clarity is the key to using time derivatives correctly in fluid mechanics.

