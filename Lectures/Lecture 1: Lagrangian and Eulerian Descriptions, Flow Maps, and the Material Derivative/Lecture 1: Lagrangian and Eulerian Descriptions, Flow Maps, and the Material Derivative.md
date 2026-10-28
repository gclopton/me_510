


## 1.1 A note on derivative notation

In continuum mechanics and fluid dynamics, it is often most consistent to regard differentiation as an operation that acts on a function and returns a new function. If $f(x)$ is a function, then its derivative with respect to $x$ is written as

$$
\frac{d f}{d x} .
$$

This object is itself a function of $x$. For instance, if $f(x)=x^{2}$, then

$$
\frac{d f}{d x}=2 x .
$$

Both the original function and its derivative can be evaluated at a point. At $x=2$,

$$
f(2)=2^{2}=4, \quad\left(\frac{d f}{d x}\right)(2)=2 \cdot 2=4 .
$$

A notation that is deliberately avoided is

$$
\frac{d f(x)}{d x} .
$$

Written carelessly, this can be misread as "first evaluate $f$ at a particular value of $x$, then differentiate the resulting number with respect to $x$." But once $f$ has been evaluated at a point, the result is a constant, and differentiating a constant with respect to $x$ gives zero. With the same example $f(x)=x^{2}$,

$$
f(2)=4, \quad \frac{d(4)}{d x}=0
$$

To emphasize that the derivative is taken before evaluation, a center-dot can be used when helpful:

$$
\frac{d f(\cdot)}{d x}
$$

which should be read as "differentiate the function $f$ with respect to $x$, without first substituting a particular value."

This bookkeeping becomes especially valuable for multivariable functions. If $f(x, y)$ depends on $x$ and $y$, then a partial derivative with respect to $x$ can be written in several equivalent ways:

$$
\frac{\partial f}{\partial x}, \quad \frac{\partial f(\cdot, y)}{\partial x}, \quad \frac{\partial}{\partial x}[f(\cdot, y)]_{y}(x),
$$

all expressing the same idea: differentiation with respect to $x$ while holding $y$ fixed. As the subject moves into subtle "which-variable-is-held-constant" distinctions, making that choice explicit prevents later confusion.


>[[Chapter 1 Concept Check#^2240a8]]



## 1.2 Lagrangian and Eulerian descriptions of motion

Consider a domain equipped with a single spatial coordinate system $\boldsymbol{x}=[x, y, z]$. Field quantities of interest-density, temperature, velocity, and so on-can be described in two complementary ways.

In a Lagrangian description, attention is restricted to a specific material element as it moves. The element is "tagged" by its initial position at time $t=0$, denoted $\boldsymbol{x}_{0}$. This $\boldsymbol{x}_{0}$ is often called a Lagrangian coordinate, but it is not a second coordinate system; it is
simply the initial location of the chosen material element in the same $\boldsymbol{x}$-space. A Lagrangian field is therefore naturally expressed as

$$
q^{L}\left(\boldsymbol{x}_{0}, t\right),
$$

meaning "the value of $q$ carried by the material element that started at $\boldsymbol{x}_{0}$, observed at time $t$."

In an Eulerian description, attention is instead placed on the field over space at each time. One asks what value the quantity takes at a fixed spatial location $\boldsymbol{x}$ at time $t$, regardless of which material element happens to occupy that location at that instant. An Eulerian field is written as

$$
q^{E}(\boldsymbol{x}, t) .
$$

The contrast becomes sharp for velocity. A Lagrangian question asks: "What is the velocity of the particular material element that was at $\boldsymbol{x}_{0}$ when $t=0$ ?" An Eulerian question asks: "What is the velocity of whichever material element is currently at $\boldsymbol{x}$ ?" Over time, different elements pass through the same Eulerian location, while the Lagrangian description always follows the same element.

Because the independent variables differ, $q^{L}$ and $q^{E}$ are not interchangeable notations for the same function. One does not meaningfully write $q^{L}(\boldsymbol{x}, t)$, because a Lagrangian field is defined on labels $\boldsymbol{x}_{0}$, not on current spatial positions $\boldsymbol{x}$. Maintaining this distinction is essential when differentiating.


>[[Chapter 1 Concept Check#^1a0c71]]






## 1.3 The flow map and the bridge between descriptions

The relationship between the two descriptions is expressed through the flow map $\phi$. The flow map takes the label $\boldsymbol{x}_{0}$ of a material element and returns its current position $\boldsymbol{x}$ at time $t$ :

$$
\boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right) .
$$

When the motion is sufficiently regular, this map is invertible, and the inverse map returns the initial label of the element currently located at $\boldsymbol{x}$ :

$$
\boldsymbol{x}_{0}=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t) .
$$

Using $\boldsymbol{\phi}$ and $\boldsymbol{\phi}^{-1}$, the same physical quantity can be expressed in either representation. The value carried by the element labeled $\boldsymbol{x}_{0}$ at time $t$ equals the Eulerian field evaluated at that element's current location:

$$
q^{L}\left(\boldsymbol{x}_{0}, t\right)=q^{E}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right), t\right) .
$$

Conversely, the Eulerian field at a current location $\boldsymbol{x}$ equals the Lagrangian field of the element whose label is $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ :

$$
q^{E}(\boldsymbol{x}, t)=q^{L}\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right)
$$

These identities are conceptually simple but become technically powerful when time derivatives are taken.


>[[Chapter 1 Concept Check#^b95175]]



## 1.4 Lagrangian time derivatives and particle kinematics

Following a material element naturally leads to time derivatives taken at fixed label $\boldsymbol{x}_{0}$. The position of the tagged element is $\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right)$. Its Lagrangian velocity is the time derivative of this trajectory while holding $\boldsymbol{x}_{0}$ fixed:

$$
\boldsymbol{u}^{L}\left(\boldsymbol{x}_{0}, t\right):=\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

This equation says: pick one specific material particle and watch it move; its velocity is the rate at which its position changes in time. Equivalently, it says: The Lagrangian velocity of the material element labeled $x_{0}$ at time $t$ is the time derivative of its motion map $\phi$, evaluated at the same label $x_{0}$. $x_{0}$ is the label (often the reference/initial position) that permanently identifies a particular material element. $\phi\left(x_0, t\right)$ is that element's current position at time $t$. The bracket notation $[\cdot]_{\boldsymbol{x}_0}$ is a reminder that when you differentiate with respect to $t$, you keep $\boldsymbol{x}_0$ fixed-meaning you stay "attached" to the same tagged chunk of material.

The subscript notation emphasizes that the differentiation is performed at fixed $\boldsymbol{x}_{0}$. It distinguishes "time change experienced by the same material element" from "time change at a fixed point in space."

Differentiating once more in time yields the Lagrangian acceleration:

$$
\boldsymbol{a}^{L}\left(\boldsymbol{x}_{0}, t\right):=\frac{\partial}{\partial t}\left[\boldsymbol{u}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)=\frac{\partial^{2}}{\partial t^{2}}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

It says: the Lagrangian acceleration of a tagged material element is the time rate of change of that element's Lagrangian velocity, taken while keeping the label $x_0$ fixed-equivalently, it is the second time derivative of the element's position along its trajectory.

### 1.4.1 Material time derivative (time derivative following a particle)
The acceleration $\boldsymbol{a}^L$ is a special case of a more general idea: once a field is expressed in Lagrangian form, it becomes a time-dependent attribute carried by each labeled material element. It is therefore useful to introduce a single notation for "the time rate of change experienced by the element" that can be applied to any such attribute, not only to the position $\boldsymbol{\phi}$ or the velocity $\boldsymbol{u}^L$.

Let $\boldsymbol{q}^L\left(\boldsymbol{x}_0, t\right)$ denote any Lagrangian quantity attached to the element labeled $\boldsymbol{x}_0$. Examples include scalar fields such as temperature, density, or entropy per unit mass, and vector or tensor fields such as body force per unit mass, stress measures, or internal variables used in constitutive models. For a fixed label $\boldsymbol{x}_0$, the mapping $t \mapsto \boldsymbol{q}^L\left(\boldsymbol{x}_0, t\right)$ is simply the history of that quantity along the element's trajectory. Its time rate of change following the element is defined by differentiating with respect to time while holding $\boldsymbol{x}_0$ fixed:

$$
\frac{\partial}{\partial t}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t) .
$$


In Lagrangian variables this operator is, in substance, an ordinary partial derivative with respect to $t$ at fixed label, but the notation is deliberately explicit because the same physical idea will later be expressed in Eulerian variables, where "following the element" no longer corresponds to holding the spatial coordinate fixed. With this convention, acceleration is recovered immediately by choosing $\boldsymbol{q}^L=\boldsymbol{u}^L$, and the same operator provides, for example, the heating rate of a moving particle when $\boldsymbol{q}^L$ is temperature, or the compressional rate of change when $\boldsymbol{q}^L$ is density.





## 1.5 Eulerian velocity and the subtlety of "what is being differentiated"

An Eulerian velocity field assigns to each current point $\boldsymbol{x}$ and time $t$ the velocity of the element currently there. By definition it is the Lagrangian velocity re-expressed using the inverse flow map:

$$
\boldsymbol{u}^{E}(\boldsymbol{x}, t)=\boldsymbol{u}^{L}\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right)=\left.\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)\right|_{\boldsymbol{x}_{0}=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)} .
$$


It says: to get the Eulerian velocity at a place $\boldsymbol{x}$ and time $\boldsymbol{t}$, first identify which material particle is sitting at $x$ at time $t$, and then read off that particle's Lagrangian velocity at time $t$. More explicitly, the equation is doing two steps:

1.) First, $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ answers the question "which label $\boldsymbol{x}_0$ ends up at the current position $\boldsymbol{x}$ at time $t$ ?" It gives the label of the material element that currently occupies $\boldsymbol{x}$.
2.) Second, $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right)$ gives the velocity of the material element with label $\boldsymbol{x}_0$ at time $t$. Substituting $\boldsymbol{x}_0= \boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ therefore produces the velocity of the element that is presently at $\boldsymbol{x}$.

The last expression is the same statement in "trajectory language": $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is the time derivative of the motion map $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ along a particle path, evaluated for the particular particle whose path passes through $\boldsymbol{x}$ at time $t$.

A subtle but crucial point appears here. The derivative $\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)$ is taken with $\boldsymbol{x}_{0}$ held fixed. Only after that derivative is formed does one substitute $\boldsymbol{x}_{0}=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$. The fact that $\boldsymbol{\phi}^{-1}$ depends on $t$ is irrelevant to the derivative at the moment it is taken, because the differentiation has already been defined as a fixed-label operation.

This distinction is exactly what separates a "time derivative following a particle" from a "time derivative at a fixed spatial location," and it is the origin of the additional convective terms that appear in Eulerian expressions of particle-following time rates of change.




## 1.6 The material derivative in Eulerian form

The objective is now to compute time derivatives that follow a material element, while expressing the result in Eulerian variables ( $\boldsymbol{x}, t$ ). The Eulerian acceleration field provides the canonical example. Componentwise, with Einstein summation over repeated indices, the Eulerian acceleration is the Lagrangian acceleration evaluated for the element currently at $\boldsymbol{x}$ :

$$
a_{i}^{E}(\boldsymbol{x}, t)=a_{i}^{L}\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right) .
$$

This says that the Eulerian acceleration at the current location $x$ at time $t$ is the acceleration of the specific material particle that happens to be located at $x$ at time $t$. In other words, to find $a_i^E(\boldsymbol{x}, t)$, first identify which particle is at $\boldsymbol{x}$ at time $t$. That particle's label is $\phi^{-1}(x, t)$. Then evaluate the Lagrangian acceleration of that labeled particle at the same time $t$.


> [!goal] Goal of the following derivation
> Compute the material time derivative of the Eulerian velocity field-i.e., the Eulerian acceleration-and express it purely in Eulerian variables ( $\boldsymbol{x}, t$ ).



To expose the Eulerian structure, one rewrites the Lagrangian velocity of a particle as the Eulerian velocity evaluated along the particle's trajectory, then differentiates in time at fixed $\boldsymbol{x}_{0}$ and applies the chain rule.


We start with the definition of the Eulerian acceleration field: evaluate the Lagrangian acceleration of the particle whose label is $\phi^{-1}(\boldsymbol{x}, t)$, i.e., the particle currently located at $\boldsymbol{x}$.

$$
a_i^E(\boldsymbol{x}, t)=a_i^L\left(\phi^{-1}(\boldsymbol{x}, t), t\right)
$$


Use the definition $a_i^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial}{\partial t}\left[u_i^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$ : the time derivative is taken at fixed label $\boldsymbol{x}_0$, and only then do we evaluate at $\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)$.

$$
a_i^E(\boldsymbol{x}, t)=\left.\frac{\partial}{\partial t}\left[u_i^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Rewrite the Lagrangian velocity of the tagged particle as the Eulerian velocity evaluated along that particle's trajectory:

$$
u_i^L\left(\boldsymbol{x}_0, t\right)=u_i^E\left(\phi\left(\boldsymbol{x}_0, t\right), t\right),
$$

which is encoded by the composition $u_i^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right), \cdot\right)$.

$$
a_i^E(\boldsymbol{x}, t)=\left.\frac{\partial}{\partial t}\left[u_i^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right), \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Differentiate this composite with respect to $t$ while holding $\boldsymbol{x}_0$ fixed, using the chain rule. The first term comes from explicit time dependence of $u_i^E$; the second comes from the time dependence of the spatial argument $\phi\left(\boldsymbol{x}_0, t\right)$.

$$
a_i^E(\boldsymbol{x}, t)=\left.\left(\frac{\partial u_i^E}{\partial t}\left(\phi\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial u_i^E}{\partial x_j}\left(\phi\left(\boldsymbol{x}_0, t\right), t\right) \frac{\partial}{\partial t}\left[\phi_j\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Recognize the remaining trajectory derivative as the Lagrangian velocity component:

$$
\begin{gathered}
u_j^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial}{\partial t}\left[\phi_j\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t) . \\
a_i^E(\boldsymbol{x}, t)=\left.\left(\frac{\partial u_i^E}{\partial t}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial u_i^E}{\partial x_j}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right) u_j^L\left(\boldsymbol{x}_0, t\right)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
\end{gathered}
$$


Re-express the Lagrangian velocity in Eulerian form along the same trajectory:

$$
\begin{gathered}
u_j^L\left(\boldsymbol{x}_0, t\right)=u_j^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right) \\
a_i^E(\boldsymbol{x}, t)=\left.\left(\frac{\partial u_i^E}{\partial t}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial u_i^E}{\partial x_j}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right) u_j^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
\end{gathered}
$$


Finally substitute $\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)$. This turns $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ into $\boldsymbol{\boldsymbol { x } _ { 1 }}$, so every evaluation "along the trajectory" becomes evaluation at the Eulerian point $(\boldsymbol{x}, t)$.



> [!equation] Eulerian Representation of the Material Derivative of Velocity
> 
> $$
> a_i^E(\boldsymbol{x}, t)=\frac{\partial u_i^E}{\partial t}(\boldsymbol{x}, t)+u_j^E(\boldsymbol{x}, t) \frac{\partial u_i^E}{\partial x_j}(\boldsymbol{x}, t)
> $$
> 



The Eulerian acceleration at the spacetime point $(\boldsymbol{x}, t)$-meaning "the acceleration of the particular fluid particle that happens to be located at position $\boldsymbol{x}$ at time $t^{\prime \prime}$-is the total time rate of change of the velocity of that particle, written entirely in terms of the Eulerian velocity field $\boldsymbol{u}^E(\boldsymbol{x}, t)$.

It splits into two physically distinct pieces:
1. $\frac{\partial u_i^E}{\partial t}(\boldsymbol{x}, t)$ is the local (or unsteady) acceleration: how the $i$-th component of the velocity field changes in time at a fixed spatial location $\boldsymbol{x}$. Even if nothing moves through $\boldsymbol{x}$, the field itself could be changing there.
2. $u_j^E(\boldsymbol{x}, t) \frac{\partial u_i^E}{\partial x_j}(\boldsymbol{x}, t)$ is the convective (or advective) acceleration: the change in $u_i$ experienced because the particle is moving through space into regions where the velocity field is different. It is the directional derivative of $u_i$ in the direction of the velocity $\boldsymbol{\boldsymbol { u } _ { \text { ; } } \text { in vector form this is } ( \boldsymbol { u } \cdot \nabla ) \boldsymbol { u } \text { . }}$

So, verbally: a particle's acceleration equals "how the velocity at a point changes with time" plus "how the particle's motion carries it into spatial variations of the velocity field." This is exactly the chain rule applied to $u_i^E(\boldsymbol{x}(t), t)$ along a trajectory $\boldsymbol{x}(t)$ with $\dot{\boldsymbol{x}}(t)=\boldsymbol{u}^E(\boldsymbol{x}(t), t)$.


---


> [!goal] Goal of the following derivation
> Write the Eulerian Representation of the Material Derivative of Velocity in Vector Form




We can write this equation in vector form. We know that 


$$
a_i^E(\boldsymbol{x}, t)=\frac{\partial u_i^E}{\partial t}(\boldsymbol{x}, t)+u_j^E(\boldsymbol{x}, t) \frac{\partial u_i^E}{\partial x_j}(\boldsymbol{x}, t)
$$


The first term is already the $i$-th component of the vector field $\frac{\partial \boldsymbol{u}^E}{\partial t}$, so it can be rewritten using component-extraction brackets.

$$
a_i^E(\boldsymbol{x}, t)=\left[\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)\right]_i+\left[u_j^E(\boldsymbol{x}, t) \frac{\partial u_i^E}{\partial x_j}(\boldsymbol{x}, t)\right]
$$


In the second term, interpret $u_j^E \frac{\partial}{\partial x_j}$ as a first-order differential operator acting on the scalar component $u_i^E$.

$$
a_i^E(\boldsymbol{x}, t)=\left[\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)\right]_i+\left[\left(u_j^E(\boldsymbol{x}, t) \frac{\partial}{\partial x_j}\right) u_i^E(\boldsymbol{x}, t)\right]
$$


Recognize the operator $u_j^E \frac{\partial}{\partial x_j}$ as the directional-derivative operator $\left(\boldsymbol{u}^E \cdot \nabla\right)$.

$$
a_i^E(\boldsymbol{x}, t)=\left[\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)\right]_i+\left[\left(\boldsymbol{u}^E(\boldsymbol{x}, t) \cdot \nabla\right) u_i^E(\boldsymbol{x}, t)\right]
$$


Applying $\left(\boldsymbol{u}^E \cdot \nabla\right)$ to the vector field $\boldsymbol{u}^E$ produces a vector whose $i$-th component is exactly $\left(\boldsymbol{u}^E\right.$. $\nabla) u_i^E$.

$$
a_i^E(\boldsymbol{x}, t)=\left[\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)\right]_i+\left[\left(\boldsymbol{u}^E(\boldsymbol{x}, t) \cdot \nabla\right) \boldsymbol{u}^E(\boldsymbol{x}, t)\right]_i
$$


Combine the two $i$-th-component expressions into a single $i$-th component of a sum of vectors.

$$
a_i^E(\boldsymbol{x}, t)=\left[\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)+\left(\boldsymbol{u}^E(\boldsymbol{x}, t) \cdot \nabla\right) \boldsymbol{u}^E(\boldsymbol{x}, t)\right]_i
$$


Since this holds for every component $i$, the corresponding vector identity is

$$
\boldsymbol{a}^E(\boldsymbol{x}, t)=\frac{\partial \boldsymbol{u}^E}{\partial t}(\boldsymbol{x}, t)+\left[\left(\boldsymbol{u}^E \cdot \nabla\right) \boldsymbol{u}^E\right](\boldsymbol{x}, t) .
$$


---

This is the prototype for translating a particle-following time derivative into Eulerian language. The starting point, $a_i^E(\boldsymbol{x}, t)=a_i^L\left(\phi^{-1}(\boldsymbol{x}, t), t\right)$, is conceptually Lagrangian: it says "take the time derivative along the motion of a specific material element." In the derivation we showed how to compute that same particle (following rate of change using only Eulerian data; fields defined on space at each time) without explicitly tracking the particle labels.

The resulting formula

$$
a_i^E(\boldsymbol{x}, t)=\frac{\partial u_i^E}{\partial t}(\boldsymbol{x}, t)+u_j^E(\boldsymbol{x}, t) \frac{\partial u_i^E}{\partial x_j}(\boldsymbol{x}, t)
$$

makes the distinction between two sources of change explicit. The term $\partial u_i^E / \partial t$ is the time variation observed at a fixed location, while the term $u_j^E \partial u_i^E / \partial x_j$ accounts for the fact that a moving material element samples different spatial values of the field as it travels. Writing the same result in vector form highlights that the second contribution is a directional derivative along the velocity:

$$
\boldsymbol{a}^E=\frac{\partial \boldsymbol{u}^E}{\partial t}+\left(\boldsymbol{u}^E \cdot \nabla\right) \boldsymbol{u}^E .
$$


The broader accomplishment is the identification of the Eulerian representation of the particle-following time derivative, often written

$$
\frac{D}{D t}=\frac{\partial}{\partial t}+\left(\boldsymbol{u}^E \cdot \nabla\right) .
$$


Once this operator is available, the same translation applies to any Eulerian field $\boldsymbol{q}^E(\boldsymbol{x}, t)$ : the rate of change experienced by a moving material element can be written entirely in Eulerian variables as

$$
\frac{D \boldsymbol{q}^E}{D t}=\frac{\partial \boldsymbol{q}^E}{\partial t}+\left(\boldsymbol{u}^E \cdot \nabla\right) \boldsymbol{q}^E .
$$


So this acceleration derivation establishes the general mechanism by which "follow-the-particle" physics is rewritten as Eulerian field equations.



---




The same mechanism applies to any Eulerian field $\boldsymbol{q}^{E}(\boldsymbol{x}, t)$ whose rate of change is to be taken following a material element. 


$$
\left.\frac{\partial}{\partial t}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Rewrite the Lagrangian field along a trajectory using the flow map: the value carried by the particle labeled $\boldsymbol{x}_0$ at time $t$ equals the Eulerian field evaluated at its current position $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$.

$$
\left.\frac{\partial}{\partial t}\left[\boldsymbol{q}^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right), \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right|_{\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)}
$$


Differentiate the composite $t \mapsto \boldsymbol{q}^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)$ with respect to $t$ while holding $\boldsymbol{x}_0$ fixed, applying the chain rule to account for explicit time dependence and dependence through the spatial argument.

$$
\left.\left(\frac{\partial \boldsymbol{q}^E}{\partial t}\left(\phi\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial \boldsymbol{q}^E}{\partial x_j}\left(\phi\left(\boldsymbol{x}_0, t\right), t\right) \frac{\partial}{\partial t}\left[\phi_j\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Recognize the remaining trajectory derivative as the $j$-th component of the Lagrangian velocity of the tagged particle.

$$
\left.\left(\frac{\partial \boldsymbol{q}^E}{\partial t}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial \boldsymbol{q}^E}{\partial x_j}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right) u_j^L\left(\boldsymbol{x}_0, t\right)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Re-express the Lagrangian velocity along the same trajectory in Eulerian form, replacing $u_j^L\left(\boldsymbol{x}_0, t\right)$ by $u_j^E\left(\phi\left(\boldsymbol{x}_0, t\right), t\right)$.

$$
\left.\left(\frac{\partial \boldsymbol{q}^E}{\partial t}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)+\frac{\partial \boldsymbol{q}^E}{\partial x_j}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right) u_j^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)\right)\right|_{\boldsymbol{x}_0=\phi^{-1}(\boldsymbol{x}, t)}
$$


Now evaluate at $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$, so $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)=\boldsymbol{x}$, converting "along the trajectory" evaluations into evaluations at ( $\boldsymbol{x}, t$ ).

$$
\frac{\partial \boldsymbol{q}^E}{\partial t}(\boldsymbol{x}, t)+u_j^E(\boldsymbol{x}, t) \frac{\partial \boldsymbol{q}^E}{\partial x_j}(\boldsymbol{x}, t)
$$

Recognize the index form $u_j^E \partial / \partial x_j$ as the directional-derivative operator $\left(\boldsymbol{u}^E \cdot \nabla\right)$ acting on the field $\boldsymbol{q}^E$.


$$
\frac{\partial \boldsymbol{q}^{E}}{\partial t}(\boldsymbol{x}, t)+\left[\left(\boldsymbol{u}^{E} \cdot \nabla\right) \boldsymbol{q}^{E}\right](\boldsymbol{x}, t) .
$$

This expression is the time rate of change of $\boldsymbol{q}^E$ experienced by a material element as it moves with the flow, expressed using Eulerian variables.

The first term $\frac{\partial \boldsymbol{q}^E}{\partial t}(\boldsymbol{x}, t)$ is the local time change you would measure at a fixed spatial location $\boldsymbol{x}$. The second term $\left[\left(\boldsymbol{u}^E \cdot \nabla\right) \boldsymbol{q}^E\right](\boldsymbol{x}, t)$ is the convective (advective) change caused by the element moving with velocity $\boldsymbol{u}^E$ through spatial variations of $\boldsymbol{q}^E$. Together, they give the particle-following (material) derivative of $\boldsymbol{q}$ evaluated at the particle currently at $\boldsymbol{x}$ at time $t$.


This derivation generalizes the acceleration calculation into a reusable rule for translating "time change experienced by a moving material element" into Eulerian variables. The quantity $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$ is inherently Lagrangian because it differentiates while holding the particle label $\boldsymbol{x}_0$ fixed, i.e., it follows the same material element through time. By rewriting $\boldsymbol{q}^L\left(\boldsymbol{x}_0, t\right)$ as the Eulerian field evaluated along the trajectory $\boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ and applying the chain rule, the particle-following derivative becomes an operator acting on Eulerian fields: a local time derivative plus a convective correction. The final result,

$$
\frac{\partial \boldsymbol{q}^E}{\partial t}+\left(\boldsymbol{u}^E \cdot \nabla\right) \boldsymbol{q}^E,
$$

provides a purely Eulerian formula for a fundamentally Lagrangian concept. It isolates the two sources of change seen by a moving particle-explicit time variation at a point and variation encountered by moving through spatial gradients-and it furnishes the standard "material derivative" operator that can be applied to any transported field (temperature, concentration, momentum, and so on) without re-deriving the chain rule each time.





## 1.7 The material derivative operator $D / D t$


The operator $D / D t$ is introduced because continuum mechanics constantly needs to express laws that are naturally stated for a moving material element while working with fields that are most conveniently described in space. Newtonian mechanics is written for particles: force equals mass times the time rate of change of momentum of the same piece of matter. In a continuum, the "same piece of matter" is a fluid particle or material element, so the relevant time derivative is the one taken while following that element. Writing that operation repeatedly as "differentiate at fixed $\boldsymbol{x}_0$ " in a Lagrangian setting, or as $\partial / \partial t+ \left(\boldsymbol{u}^E \cdot \nabla\right)$ in an Eulerian setting, quickly becomes cumbersome and obscures the fact that the physical operation is the same in both descriptions. Introducing $D / D t$ names the operation once and for all: it is the time derivative evaluated along a material trajectory.

This notation does more than shorten formulas. It cleanly separates two ideas that are otherwise easy to conflate: a time derivative taken at a fixed location in space and a time derivative taken along the motion of matter. In Eulerian form, these differ by the convective contribution, so without a dedicated symbol it is easy to lose track of which derivative a balance law requires. By reserving $D / D t$ for the particle-following derivative, statements like "a scalar is conserved along particle paths" become representationindependent: one can write $D q / D t=0$ without committing to Lagrangian or Eulerian variables, and then expand it as needed depending on the chosen description. This is exactly the role $D / D t$ will play in transport and balance laws: it is the common operator that lets particle-based physics be written compactly while still being computable from Eulerian fields when required.


In a Lagrangian description, it reduces to the fixed-label time derivative:

$$
\left(\frac{D \boldsymbol{q}}{D t}\right)^{L}\left(\boldsymbol{x}_{0}, t\right)=\frac{\partial}{\partial t}\left[\boldsymbol{q}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

This says that the material (particle-following) time derivative of $\boldsymbol{q}$ in the Lagrangian description is the ordinary time derivative of $\boldsymbol{q}^L$ taken while holding the particle label $\boldsymbol{x}_0$ fixed.

In an Eulerian description, it takes the familiar advective form:

$$
\left(\frac{D \boldsymbol{q}}{D t}\right)^{E}(\boldsymbol{x}, t)=\frac{\partial \boldsymbol{q}^{E}}{\partial t}(\boldsymbol{x}, t)+\left(\boldsymbol{u}^{E} \cdot \nabla\right) \boldsymbol{q}^{E}(\boldsymbol{x}, t) .
$$

It says: the material (particle-following) time derivative of $\boldsymbol{q}$, expressed in Eulerian variables, equals the local time change of the Eulerian field at a fixed point $\boldsymbol{x}$ plus the change produced by being carried through space by the flow.



### 1.8 Summary and interpretive synthesis

A single spatial coordinate system $\boldsymbol{x}$ supports two distinct representations of continuum motion. The Lagrangian description labels material elements by their initial positions $\boldsymbol{x}_{0}$ and follows them through time, while the Eulerian description fixes attention on spatial locations $\boldsymbol{x}$ and records the field values of whichever elements occupy those locations at each time. The flow map $\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right)$ and its inverse $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ provide the bridge between these representations, allowing physical quantities to be consistently translated between label space and current configuration space.

Within this framework, the material derivative $D / D t$ is the natural derivative "experienced" by a moving material element. In Lagrangian form it is simply a partial time derivative at fixed label. In Eulerian form it becomes the sum of a local time derivative and a convective derivative, reflecting how a particle's motion through a spatially varying field contributes to the particle-following rate of change. Keeping careful track of which variables are held fixed, and distinguishing the functions $q^{L}\left(\boldsymbol{x}_{0}, t\right)$ and $q^{E}(\boldsymbol{x}, t)$ rather than conflating them, removes much of the mystery that often surrounds the Eulerian form of the material derivative.


