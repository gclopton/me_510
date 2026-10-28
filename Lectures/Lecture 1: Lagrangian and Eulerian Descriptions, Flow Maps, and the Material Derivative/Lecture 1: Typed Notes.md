
## 1 A note about derivative notation

For the exciting discussion we are about to have, I need to make my notation around derivatives clear. In this discussion, we will think of derivatives as functionals. Without getting too bogged down in the details, this interpretation means that a derivative takes in a function and returns a new function.

Mathematically, let's say we have a function $f(x)$. Then we will write the derivative of that function as

$$
\frac{d f}{d x} .
$$

This derivative is itself a function. Like $f$, the derivative can also be evaluated at a point $x$. For example, the function $f(x)=x^{2}$ has a derivative $d f / d x=2 x$. I can evaluate either $f$ or the derivative function $g:=d f / d x$ at $x=2$ to get $f(2)=2^{2}=4$ and $g(2)=2 \times 2=4$.

One thing I will be careful to avoid in the notes below is to write the derivative as

$$
\text { I won't write } \frac{d f(x)}{d x} \text {. }
$$

This notation could be misinterpreted as saying to first evaluate the function $f$ at a specific value of $x$, and then differentiate the result. But once $f$ has been evaluated at a point, it is no longer a function of $x$; differentiating the resulting constant yields zero. For example, for $f(x)=x^{2}$,

$$
f(2)=4 \quad \text { and } \quad \frac{d(4)}{d x}=0
$$

To emphasize that a derivative acts on a function rather than on a value, I will instead use a center dot to indicate functional dependence when helpful. That is, I might write



$$
\text { I will write } \frac{d f(\cdot)}{d x} .
$$

You can take this to mean something like "take the derivative of the function f , without first evaluating it at a particular point."

This center dot notation is especially useful if our function depends on multiple variables. For example, if $f(x, y)$ depends on both $x$ and $y$, then a partial derivative with respect to $x$ may be written as

$$
\text { I will write } \frac{\partial f}{\partial x} \text { or } \frac{\partial f(\cdot, y)}{\partial x} \text { or } \frac{\partial}{\partial x}[f(\cdot, y)]_{y^{\prime}}
$$

with the understanding that $y$ is held fixed.
This may seem pedantic-it's not! This notational bookkeeping is not needed for basic calculus because the order of operations is often clear from context. But down the rabbit holes we are soon to go hunting, the sequence of operations is important and subtle. Keeping careful track of what is being differentiated, and when, will save us from confusion later on. And with that, the game is afoot!

## 2 Lagrangian and Eulerian descriptions

We have a coordinate system $\boldsymbol{x}=[x, y, z]$.

### 2.1 Lagrangian perspective: follow a material element

All quantites (density, temperature, etc) follow a specific material element. We use a marker to define the material element we're focusing on (e.g. $\boldsymbol{x}_{0}$, which could mark the center of mass of the element, expressed in the coordinate system $\boldsymbol{x}$, at time $t=0$ ). The quantity $\boldsymbol{x}_{0}$ is often called the Lagrangian coordinate, but it is not a distinct coordinate system! It is just where the "tagged" fluid element is in the sole coordinate system of the domain.
Generally, a Lagrangian quantity $q^{L}$ is defined as $q^{L}\left(\boldsymbol{x}_{0}, t\right)$. (That is, it depends on the Lagrangian coordinate that "tags" the fluid element, and at the time instance where you are inspecting that chosen fluid particle).

### 2.2 Eulerian perspective: look at the full field at each snapshot

Instead of following distinct fluid elements, we might instead want to look at field variables that probe different quantities (density, temperature, or even velocity) at various points in space.
The difference is most drastically highlighted by looking at the velocity field. Instead of asking: "over time, what is the velocity of this specific fluid element that was at $\boldsymbol{x}_{0}$ when $t=0$ ?", we might instead ask: "what is the velocity of whatever fluid element happens to be at some fixed Eulerian coordinate $\boldsymbol{x}$ ?" Note the difference! The Eulerian approach will generally have a different fluid element inhabit $\boldsymbol{x}$ at the various instances in time, whereas the Lagrangian perspective is always following the same fluid particle.
Generally, an Eulerian quantity $q^{E}$ is defined as $q^{E}(\boldsymbol{x}, t)$. Note our use of the superscript $E$ to distinguish the variable from the Lagrangian variable. This point is key, and a big source of confusion in relating the two perspectives! Let us be clear, one cannot ask for $q^{L}(\boldsymbol{x}, t)$ : Lagrangian quantities take in the reference "Lagrangian coordinate" that tags a fluid element. Likewise, Eulerian quantities must take in a point in the coordinate system without caring where it came from at $t=0$.

### 2.3 Relating Lagrangian and Eulerian perspectives

We can relate the Lagrangian and Eulerian perspectives using the concept of a flow map. The flow map, $\phi$, tells us where the fluid element inhabiting $\boldsymbol{x}_{0}$ at $t=0$ has moved at some later time $t$. Specifically, we say that

$$
x=\phi\left(x_{0}, t\right) .
$$

This flow map is invertible, so that

$$
\boldsymbol{x}_{0}=\phi^{-1}(\boldsymbol{x}, t) .
$$

This flow map lets us relate quantities across the Eulerian and Lagrangian perspectives. We have that

$$
q^{L}\left(\boldsymbol{x}_{0}, t\right)=q^{E}\left(\phi^{-1}\left(\boldsymbol{x}_{0}, t\right), t\right),
$$

and

$$
q^{E}(\boldsymbol{x}, t)=q^{L}(\phi(\boldsymbol{x}, t), t) .
$$

## 3 The material derivative

It will benefit us in the course to perform time derivatives following material elements. We can cast these "Lagrangian" time derivatives in either the Lagrangian perspective (which is most natural), or the Eulerian perspectives.

### 3.1 Lagrangian derivatives in the Lagrangian perspective

The material element that inhabited $\boldsymbol{x}_{0}$ at time $t=0$ can be followed in time to have a new position given by the flow map, $\phi\left(\boldsymbol{x}_{0}, t\right)$. We can get the velocity by differentiating this position with respect to time

$$
\boldsymbol{u}^{L}\left(\boldsymbol{x}_{0}, t\right):=\frac{\partial}{\partial t}\left[\phi\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

Note that I am explicitly mentioning that $\boldsymbol{x}_{0}$ is the variable we are keeping fixed in this differentiation. It is good to be explicit about the variable that is kept constant in this derivatives, as I think we will see when looking at taking derivatives in the Eulerian perspective, a bit later.
Similarly, the acceleration of the fluid element we are following, in the Lagrangian perspective, is

$$
\boldsymbol{a}^{L}\left(\boldsymbol{x}_{0}, t\right):=\frac{\partial}{\partial t}\left[\boldsymbol{u}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)=\frac{\partial^{2}}{\partial t^{2}}\left[\phi\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

More generally, a quantity $q^{L}$ in the Lagrangian perspective can be differentiated, following a fluid element, via

$$
\frac{\partial}{\partial t}\left[\boldsymbol{q}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t) .
$$

### 3.2 Lagrangian derivatives in the Eulerian perspective

We can use the derivatives just established in the Lagrangian perspective to write out the velocity in the Eulerian perspective:

$$
\boldsymbol{u}^{E}(\boldsymbol{x}, t)=\boldsymbol{u}^{L}\left(\phi^{-1}(\boldsymbol{x}, t), t\right)=\left.\frac{\partial}{\partial t}\left[\phi\left(\boldsymbol{x}_{0}, \cdot\right)\right](t)\right|_{\boldsymbol{x}_{0}=\phi^{-1}(\boldsymbol{x}, t)} .
$$

Note the following incredibly subtle point: the dependence of $\phi^{-1}$ on $t$ is not relevant to the derivative, which is only applied to the second argument of $\phi$. The reason for this fact is that we are directly substituting our expression for $\boldsymbol{u}^{L}$, which took a time derivative for a fixed $\boldsymbol{x}_{0}$. After this time derivative is taken, we evaluate the resulting derivative at time $t$ and substitute the identity that $\boldsymbol{x}_{0}=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$.

Let us now consider casting Lagrangian derivatives in the Eulerian perspective. (We will see that the Eulerian velocity field plays a role in these derivatives.) The key point is that we want to ask for the derivative of a quantity associated with whatever fluid element happens to inhabit the $\boldsymbol{x}$ point we have chosen.
As a concrete starting point, let's compute the acceleration of the flow field in an Eulerian perspective. The $i^{\text {th }}$ component of the acceleration vector is

$$
a_{i}^{E}(\boldsymbol{x}, t)=a_{i}^{L}\left(\phi^{-1}(\boldsymbol{x}, t), t\right)=\left.\frac{\partial}{\partial t}\left[u_{i}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right](t)\right|_{\boldsymbol{x}_{0}=\phi^{-1}(\boldsymbol{x}, t)}=\left.\frac{\partial}{\partial t}\left[u_{i}^{E}\left(\phi\left(\boldsymbol{x}_{0}, \cdot\right), \cdot\right)\right](t)\right|_{\boldsymbol{x}_{0}=\phi^{-1}(\boldsymbol{x}, t)} .
$$

The righthand side of this expression is crucial. Mathematically, we see that we must use the chain rule, since the time derivative at fixed $\boldsymbol{x}_{0}$ will affect both arguments of $u_{i}^{E}$. That is, the derivative is affected both because $u_{i}^{E}$ explicitly depends on time, and because the spatial location of the fluid element we are tracking depends on time (these fluid elements are generally moving!). Let us use the chain rule to evaluate this Eulerian form of the acceleration field more explicitly.

The chain rule gives:

$$
\left.\frac{\partial}{\partial t}\left[u_{i}^{E}\left(\phi\left(\boldsymbol{x}_{0}, \cdot\right), \cdot\right)\right](t)\right|_{\boldsymbol{x}_{0}}=\frac{\partial}{\partial t}\left[u_{i}^{E}(\boldsymbol{x}, \cdot)\right]_{\boldsymbol{x}}(t)+\frac{\partial u_{i}^{E}}{\partial x_{j}}(\boldsymbol{x}, t) \frac{\partial}{\partial t}\left[\phi_{j}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t), \quad \boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right) .
$$

Recognize the lastmost term as the velocity written in the Lagrangian perspective:

$$
\frac{\partial}{\partial t}\left[\phi\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)=u_{j}^{L}\left(\boldsymbol{x}_{0}, t\right) .
$$

But this Lagrangian velocity $u_{j}^{L}$ can be expressed as the Eulerian velocity via

$$
u_{j}^{L}\left(\boldsymbol{x}_{0}, t\right)=u_{j}^{E}\left(\phi_{j}\left(\boldsymbol{x}_{0}, t\right), t\right)=u_{j}^{E}(\boldsymbol{x}, t) .
$$

Putting this all together gives us our expression for the Eulerian velocity field:

$$
a_{i}^{E}(\boldsymbol{x}, t)=\left.\frac{\partial}{\partial t}\left[u_{i}^{E}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, \cdot\right), \cdot\right)\right](t)\right|_{\boldsymbol{x}_{0}}=\frac{\partial u_{i}^{E}}{\partial t}(\boldsymbol{x}, t)+u_{j}^{E}(\boldsymbol{x}, t) \frac{\partial u_{i}^{E}}{\partial x_{j}}(\boldsymbol{x}, t), \quad \boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_{0}, t\right) .
$$

In vector form,

$$
\boldsymbol{a}^{E}(\boldsymbol{x}, t)=\frac{\partial \boldsymbol{u}^{E}}{\partial t}(\boldsymbol{x}, t)+\left[\left(\boldsymbol{u}^{E} \cdot \nabla\right) \boldsymbol{u}^{E}\right](\boldsymbol{x}, t) .
$$

Of course, there is nothing special about the fact that we were taking the Lagrangian derivative of $\boldsymbol{a}^{E}$ (from an Eulerian perspective). We could replace $\boldsymbol{a}^{E}$ with any generic quantity $\boldsymbol{q}^{E}$, and its material derivative would be

$$
\frac{\partial \boldsymbol{q}^{E}}{\partial t}(\boldsymbol{x}, t)+\left[\left(\boldsymbol{u}^{E} \cdot \nabla\right) \boldsymbol{q}^{E}\right](\boldsymbol{x}, t) .
$$

We will generally define the material derivative operator as $D / D t$. Like a general variable $\boldsymbol{q}$, $D / D t$ is a construct that means "time derivative following a fluid particle." While this construct is inherently a Lagrangian quantity, the mathematical representation $D / D t$ of this quantity is agnostic to whether we are working with an Eulerian or Lagrangian representation.

We can cast this material derivative in Lagrangian and Eulerian form as

$$
\left(\frac{D \boldsymbol{q}}{D t}\right)^{L}\left(\boldsymbol{x}_{0}, t\right)=\frac{\partial}{\partial t}\left[\boldsymbol{q}^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t),
$$

or

$$
\left(\frac{D \boldsymbol{q}}{D t}\right)^{E}(\boldsymbol{x}, t)=\frac{\partial \boldsymbol{q}^{E}}{\partial t}(\boldsymbol{x}, t)+\left(\boldsymbol{u}^{E} \cdot \nabla\right) \boldsymbol{q}^{E}(\boldsymbol{x}, t),
$$

respectively.

### 3.3 Some synthesis of the material derivative

The material derivative $D / D t$ is a mathematical object that is agnostic to which perspective (Lagrangian versus Eulerian) that it is written in. Physically and mathematically, it expresses the time rate of change of a quantity following a fluid element.

When it takes in a quantity in the Lagrangian perspective, the material derivative reverts to the usual derivative we think of from Newtonian mechanics:

$$
\left(\frac{D q}{D t}\right)^{L}=\frac{\partial}{\partial t}\left[q^{L}\left(\boldsymbol{x}_{0}, \cdot\right)\right]_{\boldsymbol{x}_{0}}(t)
$$

When it is expressed in the Eulerian perspective, the material derivative involves extra terms that depend on spatial gradients the quantity is exposed to as it moves through the flow field:

$$
\left(\frac{D q}{D t}\right)^{E}=\frac{\partial q^{E}}{\partial t}(\boldsymbol{x}, t)+\left[\left(\boldsymbol{u}^{E} \cdot \nabla\right) q^{E}\right](\boldsymbol{x}, t) .
$$

What does the additional term in the Eulerian representation of the material derivative mean? It reflects the fact that, when we track the rate of change of a quantity following a fluid element while expressing that change in a fixed spatial coordinate system, that quantity may change for two distinct reasons. First, it may change explicitly in time. Second, it may change because the fluid element moves through regions of space where the quantity varies, due to spatial gradients sampled along its trajectory. The additional (convective) term in the Eulerian representation accounts precisely for this latter effect.

I hope this presentation has been both challenging and rewarding. Many treatments of the material derivative in an Eulerian setting introduce the final formula without carefully distinguishing between Eulerian and Lagrangian quantities, or without explicitly using the flow map to relate them. In particular, an Eulerian quantity $q^{E}$ and a Lagrangian quantity $q^{L}$ are often treated as interchangeable, even though they are distinct functions defined on different variables. By keeping careful track of these distinctions, and by being explicit about which variables are held fixed when taking derivatives, we have tried to demystify the relationship between Eulerian and Lagrangian representations of physical quantities and their time derivatives.

