


## 1.1 A note on derivative notation

>^2240a8

> [!Question]
> 1. In the "derivative-as-an-operation" viewpoint, what is $\frac{d f}{d x}$ best understood to be?

A. A number that exists only after choosing a specific value of $x$ (for example, $x=2$ ).
B. A new function of $x$ obtained by differentiating $f$ with respect to $x$.
C. The original function $f(x)$ written in a different notation.
D. The operator $\frac{d}{d x}$ by itself, without acting on any function.


> [!Question]
> 2. Let $f(x)=x^2$. Which option correctly represents "differentiate first, then evaluate at $x=2$ "?

A. $\left(\frac{d f}{d x}\right)$
B. $\frac{d f(2)}{d x}$
C. $\frac{d f}{d(2)}$
D. $\left(\frac{d}{d x}\right)(f(2))$



> [!Question]
> 3. Why is the notation $\frac{d f(x)}{d x}$ deliberately avoided in this section?

A. It can be misread as "evaluate $f$ at a particular $x$ first, then differentiate the resulting constant," which would incorrectly suggest zero
B. It is mathematically invalid unless $f$ is linear in $x$
C. It implies differentiating with respect to $f$ rather than with respect to $x$
D. It forces the derivative to be interpreted as a total derivative even for multivariable functions


> [!Question]
> 4. What does the notation $\frac{d f(\cdot)}{d x}$ most directly emphasize?

A. Substitute a particular value into $f$ first, then differentiate the resulting expression
B. Differentiate $f$ with respect to $x$ before substituting any specific value of $x$
C. Treat $f$ as a constant function of $x$ during differentiation
D. Differentiate $f$ with respect to the symbol , not with respect to $x$


> [!Question]
> 5. Which pair of expressions correctly distinguishes "differentiate then evaluate at $x=a$ " from "evaluate then differentiate," in the sense discussed?

A. Differentiate then evaluate: $\left(\frac{d f}{d x}\right)(a)$; Evaluate then differentiate: $\frac{d f(a)}{d x}$
B. Differentiate then evaluate: $\frac{d f(a)}{d x}$; Evaluate then differentiate: $\left(\frac{d f}{d x}\right)(a)$
C. Differentiate then evaluate: $\frac{d f(a)}{d a}$; Evaluate then differentiate: $\frac{d f(\cdot)}{d x}(a)$
D. Differentiate then evaluate: $\frac{d f}{d(a)}$; Evaluate then differentiate: $\left(\frac{d}{d x}\right)(f)$


> [!Question]
> 6. For a multivariable function $f(x, y)$, which option correctly expresses "differentiate with respect to $x$ while holding $y$ fixed," using an equivalent notation from the section?

A. $\frac{\partial f}{\partial x}$
B. $\frac{\partial f(x, \cdot)}{\partial x}$
C. $\frac{\partial f(\cdot, y)}{\partial y}$
D. $\frac{\partial}{\partial x}[f(x, \cdot)]_x(y)$



> [!Question]
> 7. The expression $\frac{\partial}{\partial x}[f(\cdot, y)]_y(x)$ is presented as equivalent to $\frac{\partial f}{\partial x}$. What role does the subscript ${ }_y$ play in this notation?

A. It indicates that the derivative is taken with respect to $y$ instead of $x$
B. It indicates that $y$ is treated as a constant during differentiation with respect to $x$
C. It indicates that $y$ is replaced by $x$ after differentiating
D. It indicates that the derivative is evaluated at $y=x$


> [!Question]
> 8. Which statement best captures why the section recommends making "which variable is held constant" explicit for multivariable derivatives?

A. Because partial derivatives are only defined when all other variables are explicitly set equal to zero
B. Because subtle distinctions about what is held fixed can change the meaning of a derivative, and explicit notation prevents later confusion
C. Because using $\partial$ instead of $d$ automatically forces all other variables to be constant
D. Because total derivatives cannot be evaluated at a point, whereas partial derivatives can




> [!Solution]-
> 1. B
> 2. A
> 3. A
> 4. B
> 5. A
> 6. A
> 7. B
> 8. B




## 1.2 Lagrangian and Eulerian descriptions of motion

^1a0c71

> [!Question]
> 1. In which description is attention restricted to a specific material element as it moves through space?

A. Eulerian description
B. Lagrangian description
C. Both Eulerian and Lagrangian descriptions
D. Neither description


> [!Question]
> 2. In the Lagrangian description, what does $\boldsymbol{x}_0$ represent, and what is it often called?

A. The current position of a material element at time $t$; often called the Eulerian coordinate (material label)
B. A second, independent coordinate system; often called the Eulerian coordinate (material label)
C. The initial position of a tagged material element at $t=0$; often called a Lagrangian coordinate (material label)
D. The fixed spatial location where measurements are made; often called a Lagrangian coordinate (material label)



> [!Question]
> 3. In which description is attention placed on the field values at fixed spatial locations $\boldsymbol{x}$ as time evolves?

A. Eulerian description
B. Lagrangian description
C. Both descriptions equally
D. Neither description


> [!Question]
> 4. Which question best matches the Lagrangian interpretation of velocity?

A. "What is the velocity of whichever material element is currently at $\boldsymbol{x}$ ?"
B. "What is the velocity of the particular material element that started at $\boldsymbol{x}_0$ when $t=0$ ?"
C. "What is the velocity everywhere in the domain at a fixed time $t$ ?"
D. "What is the velocity averaged over all material elements?"



> [!Question]
> 5. Which question best matches the Eulerian interpretation of velocity?

A. "What is the velocity of the material element that started at $\boldsymbol{x}_0$ at $t=0$, evaluated at time $t$ ?"
B. "What is the velocity at the fixed spatial location $\boldsymbol{x}$ at time $t$, regardless of which material element is there?"
C. "What is the velocity of the material element that is at $\boldsymbol{x}$ at $t=0$, evaluated at time $t$ ?"
D. "What is the velocity at the moving position $\boldsymbol{x}(t)$ of a tagged material element, evaluated at time $t$ ?"


> [!Question]
> 6. Why are $q^L$ and $q^E$ not interchangeable notations for the same function?

A. Because $q^L\left(\boldsymbol{x}_0, t\right)$ and $q^E(\boldsymbol{x}, t)$ are defined on different "spatial" arguments: $q^L$ uses the material label $\boldsymbol{x}_0$ (initial position), whereas $q^E$ uses the current spatial position $\boldsymbol{x}$.
B. Because both fields use the same spatial coordinate system, so swapping $\boldsymbol{x}_0$ and $\boldsymbol{x}$ is always valid as long as $t$ is the same.
C. Because $q^L$ depends on the particle trajectory $\boldsymbol{x}(t)$ while $q^E$ does not depend on time.
D. Because $q^E$ and $q^L$ can only be compared if the material is stationary ( $\boldsymbol{x}=\boldsymbol{x}_0$ for all $t$ ).




> [!solution]-
> **Answers:**
> 1.) B
> 2.) C
> 3.) A
> 4.) B
> 5.) B
> 6.) A


## 1.3 The flow map and the bridge between descriptions

^b95175


> [!Question]
> 1. Which statement correctly defines the flow map $\phi$ for a material motion?

A. $\boldsymbol{\phi}$ takes a current position $\boldsymbol{x}$ and returns the current label $\boldsymbol{x}_0$ at time $t$.
B. $\boldsymbol{\phi}$ takes a label $\boldsymbol{x}_0$ and returns the same label $\boldsymbol{x}_0$ at time $t$.
C. $\boldsymbol{\phi}$ takes a label $\boldsymbol{x}_0$ and returns the current position $\boldsymbol{x}$ at time $t$.
D. $\boldsymbol{\phi}$ takes a time $t$ and returns a mapping $\boldsymbol{x} \mapsto \boldsymbol{x}$ that is independent of $\boldsymbol{x}_0$.


> [!Question]
> 2. Which equation correctly expresses the inverse flow map described in the section?

A. $\boldsymbol{x}=\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right)$
B. $\boldsymbol{x}_0=\boldsymbol{\phi}(\boldsymbol{x}, t)$
C. $\boldsymbol{x}=\boldsymbol{\phi}(\boldsymbol{x}, t)$
D. $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$


> [!Question]
> 3. For a fixed time $t$, what does it mean (here) to say the motion is "sufficiently regular" so that $\boldsymbol{\phi}$ is invertible?

A. Each label $\boldsymbol{x}_0$ corresponds to exactly one current position $\boldsymbol{x}$, and each current position $\boldsymbol{x}$ corresponds to exactly one label $\boldsymbol{x}_0$.
B. The map satisfies $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)=\boldsymbol{x}_0$ for all $\boldsymbol{x}_0$.
C. The map is invertible only at $t=0$, but not for $t>0$.
D. The inverse satisfies $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)=\boldsymbol{x}$ for all $\boldsymbol{x}$.


> [!Question]
> 4. Which expression correctly writes the Eulerian field at ( $\boldsymbol{x}, t$ ) in terms of the Lagrangian field and the inverse flow map?

A. $q^E(\boldsymbol{x}, t)=q^L(\boldsymbol{\phi}(\boldsymbol{x}, t), t)$
B. $q^E(\boldsymbol{x}, t)=q^L\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right)$
C. $q^E(\boldsymbol{x}, t)=q^L\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, 0), t\right)$
D. $q^E(\boldsymbol{x}, t)=q^L(\boldsymbol{x}, t)$


> [!Question]
> 5. Which expression correctly writes the Lagrangian field at ( $\boldsymbol{x}_0, t$ ) in terms of the Eulerian field and the flow map?

A. $q^L\left(\boldsymbol{x}_0, t\right)=q^E\left(\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right), t\right)$
B. $q^L\left(\boldsymbol{x}_0, t\right)=q^E\left(\boldsymbol{x}_0, t\right)$
C. $q^L\left(\boldsymbol{x}_0, t\right)=q^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, 0\right), t\right)$
D. $q^L\left(\boldsymbol{x}_0, t\right)=q^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)$


> [!Question]
> 6. At a given time $t$, what is the meaning of $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ ?

A. The current position of the element that started at $\boldsymbol{x}$ when $t=0$.
B. The time at which the element labeled $\boldsymbol{x}_0$ reaches $\boldsymbol{x}$.
C. The initial label $\boldsymbol{x}_0$ of the material element that is located at $\boldsymbol{x}$ at time $t$.
D. The Eulerian field value $q^E(\boldsymbol{x}, t)$ rewritten with $\boldsymbol{x}_0$ as the independent variable.


> [!Question]
> 7. If $\boldsymbol{\phi}$ is invertible (for fixed $t$ ), which identity must hold for every label $\boldsymbol{x}_0$ ?

A. $\boldsymbol{\phi}^{-1}\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)=\boldsymbol{x}_0$
B. $\boldsymbol{\phi}\left(\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right), t\right)=\boldsymbol{x}_0$
C. $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)=\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right)$
D. $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)=\boldsymbol{x}_0$


> [!Question]
> 8. When taking a time derivative of the identity $q^L\left(\boldsymbol{x}_0, t\right)=q^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)$, which quantity is held fixed on the Lagrangian side by definition?

A. The current position $\boldsymbol{x}$
B. The label $\boldsymbol{x}_0$
C. The flow map $\boldsymbol{\phi}$
D. The Eulerian field $q^E$



> [!Question]
> 9. For a fixed time $t$, which mapping direction matches the "label → current position" viewpoint emphasized for $\phi$ ?

A. $\boldsymbol{x} \mapsto \boldsymbol{x}_0$ via $\boldsymbol{\phi}$
B. $\boldsymbol{x}_0 \mapsto \boldsymbol{x}_0$ via $\boldsymbol{\phi}^{-1}$
C. $\boldsymbol{x}_0 \mapsto \boldsymbol{x}$ via $\boldsymbol{\phi}$
D. $\boldsymbol{x} \mapsto \boldsymbol{x}$ via $\boldsymbol{\phi}^{-1}$


> [!Question]
> 10. What is the most direct reason the identities become technically powerful when time derivatives are taken?

A. Time derivatives eliminate the need for $\boldsymbol{\phi}^{-1}$ entirely.
B. Time derivatives make $q^L$ and $q^E$ identical functions of $(\boldsymbol{x}, t)$.
C. Time derivatives force $\boldsymbol{\phi}$ to be the identity map $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)=\boldsymbol{x}_0$.
D. Differentiating $q^E\left(\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right), t\right)$ requires accounting for both explicit $t$-dependence and the dependence through the time-varying argument $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$.



> [!Solution]-
> 1. C
> 2. D
> 3. A
> 4. $B$
> 5. D
> 6. C
> 7. A
> 8. $B$
> 9. C
> 10. $D$



## 1.4 Lagrangian time derivatives and particle kinematics


> [!Question]
> 1. In the Lagrangian time derivative, which quantity is held fixed during differentiation with respect to $t$ ?

A. The current spatial position $\boldsymbol{x}$
B. The velocity field $\boldsymbol{u}^L$
C. The time variable $t$
D. The material label $\boldsymbol{x}_0$

> [!Question]
> 2. Which expression correctly defines the Lagrangian velocity of the tagged element?

A. $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial t}[\boldsymbol{\phi}(\cdot, t)]_t\left(\boldsymbol{x}_0\right)$
B. $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial t_{\partial}}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
C. $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial \boldsymbol{x}_0}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_t(t)$
D. $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial t}[\boldsymbol{\phi}(\boldsymbol{x}, \cdot)]_{\boldsymbol{x}}(t)$


> [!Question]
> 3. What does the subscript in $\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$ emphasize?

A. The derivative is evaluated at $t=0$
B. The derivative is taken holding $\phi$ fixed
C. The derivative is taken holding $\boldsymbol{x}_0$ fixed (following the same material element)
D. The derivative is taken holding the current position $\boldsymbol{x}$ fixed (following the same material element)


> [!Question]
> 4. Which expression correctly defines the Lagrangian acceleration $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right)$ ?

A. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial t}\left[\boldsymbol{u}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
B. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial \boldsymbol{x}_0}\left[\boldsymbol{u}^L(\cdot, t)\right]_t\left(\boldsymbol{x}_0\right)$
C. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial}{\partial t}\left[\boldsymbol{u}^L(\boldsymbol{x}, \cdot)\right]_{\boldsymbol{x}}(t)$
D. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right):=\frac{\partial^2}{\partial \boldsymbol{x}_0^2}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_t(t)$


> [!Question]
> 5. Which equation correctly relates Lagrangian acceleration to the flow map $\phi$ ?

A. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial}{\partial \boldsymbol{x}_0}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
B. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial^2}{\partial t^2}[\boldsymbol{\phi}(\cdot, t)]_t\left(\boldsymbol{x}_0\right)$
C. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_t(t)$
D. $\boldsymbol{a}^L\left(\boldsymbol{x}_0, t\right)=\frac{\partial^2}{\partial t^2}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$



> [!Question]
> 6. Which expression best represents the time rate of change "following the material element" for a general Lagrangian quantity $\boldsymbol{q}^L\left(\boldsymbol{x}_0, t\right)$ ?

A. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L(\boldsymbol{x}, \cdot)\right]_{\boldsymbol{x}}(t)$
B. $\frac{\partial}{\partial \boldsymbol{x}_0}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
C. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
D. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L(\cdot, t)\right]_t\left(\boldsymbol{x}_0\right)$


> [!Question]
> 7. The section says the "fixed $\boldsymbol{x}_0$ " subscript is not decorative. What distinction does it enforce?

A. It distinguishes vector fields from scalar fields
B. It distinguishes total derivatives from partial derivatives in multivariable calculus
C. It distinguishes time change experienced by the same moving element from time change at a fixed point in space
D. It distinguishes dependence on $\boldsymbol{x}_0$ from dependence on $t$


> [!Question]
> 8. Which statement is the most accurate paraphrase of the physical meaning of $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right)$ ?

A. The time rate of change of the position of the element labeled $\boldsymbol{x}_0$, observed along its trajectory
B. The time rate of change of the position at a fixed spatial location $\boldsymbol{x}$
C. The spatial rate of change of the trajectory with respect to $\boldsymbol{x}_0$, observed at fixed $t$
D. The time rate of change of the Eulerian field at $\boldsymbol{x}_0$, holding $\boldsymbol{x}_0$ fixed as a point in space


> [!Question]
> 9. Which option correctly matches "differentiate twice in time while following the same tagged element"?

A. $\frac{\partial^2}{\partial t^2}[\boldsymbol{\phi}(\cdot, t)]_t\left(\boldsymbol{x}_0\right)$
B. $\frac{\partial^2}{\partial t^2}[\boldsymbol{\phi}(\boldsymbol{x}, \cdot)]_{\boldsymbol{x}}(t)$
C. $\frac{\partial^2}{\partial t^2}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_t(t)$
D. $\frac{\partial^2}{\partial t^2}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$


> [!Question]
> 10. Which derivative corresponds to "time change at a fixed point in space" (as contrasted with the Lagrangian time change)?

A. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
B. $\frac{\partial}{\partial t}\left[\phi\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$
C. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^E(\boldsymbol{x}, \cdot)\right]_{\boldsymbol{x}}(t)$
D. $\frac{\partial}{\partial t}\left[\boldsymbol{q}^L(\cdot, t)\right]_t\left(\boldsymbol{x}_0\right)$



> [!Solution]-
> 1. D, 2. B, 3. C, 4. A, 5. D, 6. C, 7. C, 8. A, 9. D, 10. C



## 1.5 The material derivative in Eulerian form


> [!question]
> 1. What does the Eulerian velocity $\boldsymbol{u}^E(\boldsymbol{x}, t)$ represent?

A. The velocity of the material element labeled $\boldsymbol{x}_0=\boldsymbol{x}$ at time $t$
B. The velocity of the material element currently located at $\boldsymbol{x}$ at time $t$
C. The time derivative of $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ at fixed $\boldsymbol{x}$
D. The velocity of the material element that will arrive at $\boldsymbol{x}$ at a later time $t+\Delta t$

> [!question]
> 2. Which mapping direction is correct for the flow map and its inverse?

A. $\boldsymbol{\phi}(\boldsymbol{x}, t)$ maps current position $\boldsymbol{x}$ to the label $\boldsymbol{x}_0$, and $\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right)$ maps $\boldsymbol{x}_0$ to $\boldsymbol{x}$
B. $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ maps label $\boldsymbol{x}_0$ to current position $\boldsymbol{x}$, and $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ maps $\boldsymbol{x}$ to $\boldsymbol{x}_0$
C. $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ maps label $\boldsymbol{x}_0$ to current position $\boldsymbol{x}$, and $\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right)$ maps $\boldsymbol{x}_0$ to $\boldsymbol{x}$
D. $\boldsymbol{\phi}(\boldsymbol{x}, t)$ maps current position $\boldsymbol{x}$ to the label $\boldsymbol{x}_0$, and $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ maps $\boldsymbol{x}$ to itself

> [!question]
> 3. Which expression correctly states the definition of Eulerian velocity in terms of the Lagrangian velocity and the inverse flow map?

A. $\boldsymbol{u}^E(\boldsymbol{x}, t)=\boldsymbol{u}^L(\boldsymbol{\phi}(\boldsymbol{x}, t), t)$
B. $\boldsymbol{u}^E(\boldsymbol{x}, t)=\boldsymbol{u}^L\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right)$
C. $\boldsymbol{u}^E(\boldsymbol{x}, t)=\boldsymbol{u}^L\left(\boldsymbol{\phi}^{-1}\left(\boldsymbol{x}_0, t\right), t\right)$ with $\boldsymbol{x}_0=\boldsymbol{x}$
D. $\boldsymbol{u}^E(\boldsymbol{x}, t)=\boldsymbol{u}^L\left(\boldsymbol{x}_0, \boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)\right)$



> [!question]
> 4. In the identity
> 
> $$
> \boldsymbol{u}^E(\boldsymbol{x}, t)=\left.\frac{\partial}{\partial t}\left[\boldsymbol{\phi}\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)\right|_{\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)},
> $$
> 
> which "order of operations" matches the intended meaning?

A. First substitute $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$, then differentiate in $t$ holding $\boldsymbol{x}$ fixed
B. First substitute $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$, then differentiate in $t$ holding $\boldsymbol{x}_0$ fixed
C. First differentiate in $t$ holding $\boldsymbol{x}_0$ fixed, then substitute $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$
D. First differentiate in $t$ holding $\boldsymbol{x}$ fixed, then substitute $\boldsymbol{x}=\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$


> [!question]
> 5. In $\frac{\partial}{\partial t}\left[\phi\left(\boldsymbol{x}_0, \cdot\right)\right]_{\boldsymbol{x}_0}(t)$, which variable is held fixed by definition during the differentiation?

A. $\boldsymbol{x}$
B. $\boldsymbol{x}_0$
C. Both $\boldsymbol{x}$ and $\boldsymbol{x}_0$
D. Neither $\boldsymbol{x}$ nor $\boldsymbol{x}_0$

> [!question]
> 6. The section claims that the $t$-dependence of $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ is "irrelevant to the derivative at the moment it is taken." Which statement captures that point most accurately?

A. $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ is independent of $t$, so it cannot affect any time derivative
B. The derivative is defined at fixed $\boldsymbol{x}_0$, and $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ is only used after the derivative has already been formed
C. The derivative is defined at fixed $\boldsymbol{x}$, so $\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ is treated as a constant inside it
D. The inverse map appears only as a notational convenience and is not actually used to compute $\boldsymbol{u}^E$



> [!question]
> 7. Which pairing correctly matches the phrase to the "held constant" condition emphasized in the section?

A. "Following a particle" ↔ hold $\boldsymbol{x}$ fixed; "fixed spatial location" ↔ hold $\boldsymbol{x}_0$ fixed
B. "Following a particle" ↔ hold $\boldsymbol{x}_0$ fixed; "fixed spatial location" ↔ hold $\boldsymbol{x}$ fixed
C. "Following a particle" ↔ hold $t$ fixed; "fixed spatial location" ↔ hold $\boldsymbol{x}_0$ fixed
D. "Following a particle" ↔ hold $\boldsymbol{\phi}$ fixed; "fixed spatial location" ↔ hold $\boldsymbol{\phi}^{-1}$ fixed

> [!question]
> 8. The section says the distinction between "differentiate at fixed label" and "differentiate at fixed spatial location" is the origin of additional convective terms in Eulerian formulas for particle-following rates. What feature is being pointed to as the source of those extra terms?

A. The fact that the label $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$ varies with $t$ when $\boldsymbol{x}$ is held fixed
B. The fact that $\boldsymbol{\phi}\left(\boldsymbol{x}_0, t\right)$ is nonlinear in $\boldsymbol{x}_0$ for most motions
C. The fact that $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is defined using an inverse map rather than a forward map
D. The fact that $\boldsymbol{u}^L\left(\boldsymbol{x}_0, t\right)$ is defined as a partial derivative rather than a total derivative

> [!Question]
> 9. Let $g(t)=\boldsymbol{\phi}\left(\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t), t\right)$ for a fixed spatial point $\boldsymbol{x}$. Since $g(t)=\boldsymbol{x}$, one has $\frac{d}{d t} g(t)=\mathbf{0}$. Which statement correctly explains why this does not contradict $\boldsymbol{u}^E(\boldsymbol{x}, t) \neq \mathbf{0}$ in general?

A. $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is defined by differentiating at fixed $\boldsymbol{x}_0$, whereas $\frac{d}{d t} g(t)$ differentiates a composition at fixed $\boldsymbol{x}$
B. $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is defined only for steady flows, whereas $g(t)$ applies only to unsteady flows
C. $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is the derivative of $\boldsymbol{\phi}^{-1}$, whereas $g(t)$ involves the derivative of $\boldsymbol{\phi}$
D. $\boldsymbol{u}^E(\boldsymbol{x}, t)$ is evaluated at $\boldsymbol{x}_0=\boldsymbol{x}$, whereas $g(t)$ uses $\boldsymbol{x}_0=\boldsymbol{\phi}^{-1}(\boldsymbol{x}, t)$

Answers: 1. B, 2. B, 3. B, 4. C, 5. B, 6. B, 7. B, 8. A, 9. A