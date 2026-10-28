# Module 4: Global potential flow and compressible flow past a wavy wall 

Andres Goza

March 26, 2026

## Chapter 1 Globally Linear Potential Flow

### 1.1 From Local Linearization to Global Small-Disturbance Flow

In the previous lecture, we analyzed the compressible potential equation by freezing its coefficients locally about a spacetime point. That analysis revealed a fundamental structural result: the mathematical type of the governing equation (elliptic, hyperbolic, or parabolic) is determined by the local Mach number. Because the coefficients depend on the local velocity and sound speed, the equation may change type from one region of the flow to another.

That level of generality is essential for understanding fully nonlinear compressible flow. However, many flows of practical interest are far simpler in a global sense.

Consider, for example:

- flow past a thin airfoil at small angle of attack,
- flow over a gently undulating surface,
- flow over small geometric imperfections.

In such cases, the velocity field throughout the domain remains close to a uniform state. Physically, we expect

$$
\boldsymbol{u}=(u, v, w)=\left(U_{\infty}, 0,0\right)+\text { small perturbation }
$$

everywhere in the flow. The disturbances induced by the geometry are weak relative to the freestream motion.

This observation motivates a stronger simplification than the one used in the previous lecture. Instead of freezing the coefficients locally about an arbitrary state, we now linearize the governing equations globally about a single uniform base flow. The coefficients of the highest-order derivatives become constant throughout the domain, and the mathematical type of the equation is determined entirely by the freestream Mach number.

Our goals in this chapter are therefore to

- derive the globally linearized compressible potential equation,
- connect the velocity potential to pressure via the pressure coefficient,
- formulate the boundary-value problem for small surface perturbations.


### 1.2 Governing Equation Framework

We begin by recalling the nonlinear compressible potential equation derived in the previous lecture. Under the assumptions of inviscid, isentropic, and irrotational flow, the velocity field may be written as $\boldsymbol{u}=\nabla \phi$ and the governing equation becomes

$$
\begin{equation*}
\phi_{t t}+2 \nabla \phi \cdot \nabla \phi_{t}+(\nabla \phi)^{T}(\nabla \nabla \phi) \nabla \phi-a^{2} \nabla^{2} \phi=0 \tag{1.1}
\end{equation*}
$$

where

$$
\begin{equation*}
a=a(\rho), \quad \rho=\rho(B), \quad B=-\phi_{t}-\frac{1}{2}|\nabla \phi|^{2} . \tag{1.2}
\end{equation*}
$$

Equation (1.1) is exact under the stated assumptions. Its coefficients depend on the solution itself through the velocity and sound speed, making it quasilinear and allowing its type to vary across the flow.

We now restrict attention to steady, two-dimensional flow and develop a global small-disturbance approximation.

### 1.3 Global Linearization About a Uniform Base Flow

For steady flow, $\phi_{t}=0$, and we restrict attention to dependence on $(x, y)$. We introduce a uniform base flow with small perturbations:

$$
\begin{equation*}
u=U_{\infty}+u^{\prime}, \quad v=v^{\prime}, \quad\left|u^{\prime}\right|,\left|v^{\prime}\right| \ll U_{\infty} . \tag{1.3}
\end{equation*}
$$

To leading order, the locally frozen principal part derived previously reduces to

$$
\begin{equation*}
\left(a_{\infty}^{2}-U_{\infty}^{2}\right) \phi_{x x}+a_{\infty}^{2} \phi_{y y}=0 \tag{1.4}
\end{equation*}
$$

Dividing by $a_{\infty}^{2}$ yields the globally linearized compressible small-disturbance potential equation:

$$
\begin{equation*}
\left(1-M_{\infty}^{2}\right) \phi_{x x}+\phi_{y y}=0, \quad M_{\infty}=\frac{U_{\infty}}{a_{\infty}} \tag{1.5}
\end{equation*}
$$

This equation is the central governing equation for the remainder of the module.

Interpretation. Global linearization removes spatial variation in the coefficients of the highest-order derivatives. As a result, the type of the equation is determined everywhere by the freestream Mach number alone.

### 1.4 Classification by Freestream Mach Number

Equation (1.5) is a linear second-order PDE with constant coefficients. Its type depends only on $M_{\infty}$ :

Subsonic flow ( $M_{\infty}<1$ ). Both coefficients are positive, so the equation is elliptic. Disturbances propagate globally throughout the flow.

Supersonic flow ( $M_{\infty}>1$ ). The coefficient of $\phi_{x x}$ is negative, so the equation is hyperbolic. Disturbances propagate along characteristic directions.

Sonic flow ( $M_{\infty}=1$ ). The equation degenerates and marks the transition between elliptic and hyperbolic behavior.

Thus, within the small-disturbance approximation, compressible flow exhibits a sharp structural transition at Mach 1.

### 1.5 Linearized Pressure Coefficient

We now connect the velocity potential to pressure. For steady, inviscid, isentropic, irrotational flow, the Bernoulli relation gives

$$
\begin{equation*}
\frac{1}{2}|\nabla \phi|^{2}+h(\rho)=\text { constant. } \tag{1.6}
\end{equation*}
$$

Linearizing about the freestream state yields

$$
\begin{equation*}
U_{\infty} u^{\prime}+h^{\prime}=0 \tag{1.7}
\end{equation*}
$$

Using the isentropic thermodynamic identity

$$
\begin{equation*}
d h=\frac{1}{\rho} d p \tag{1.8}
\end{equation*}
$$

we obtain

$$
\begin{equation*}
p^{\prime}=-\rho_{\infty} U_{\infty} u^{\prime} . \tag{1.9}
\end{equation*}
$$

Defining the pressure coefficient

$$
\begin{equation*}
C_{p}=\frac{p-p_{\infty}}{\frac{1}{2} \rho_{\infty} U_{\infty}^{2}} \tag{1.10}
\end{equation*}
$$

we arrive at

$$
\begin{equation*}
C_{p}=-\frac{2}{U_{\infty}} \phi_{x} \tag{1.11}
\end{equation*}
$$

Interpretation. Equation (1.11) shows that once the potential field is known, the pressure distribution follows directly. The scalar potential therefore contains all information needed to compute aerodynamic loads within this approximation.

### 1.6 Boundary Condition for Small Surface Perturbations

To complete the problem formulation, we prescribe a boundary condition along the surface that generates the disturbance. Consider a small-amplitude wall

$$
\begin{equation*}
y=f(x) \tag{1.12}
\end{equation*}
$$

where $\|f\|=\epsilon \ll 1$.

In inviscid flow, the appropriate condition is no penetration:

$$
\begin{equation*}
\boldsymbol{u} \cdot \boldsymbol{n}=0 \tag{1.13}
\end{equation*}
$$

For the surface (1.12), a normal vector is proportional to $\left(-f^{\prime}(x), 1\right)$, so the exact condition becomes

$$
v-u f^{\prime}(x)=0 \quad \text { on } y=f(x)
$$

Linearizing about the undeformed surface and retaining only leading-order terms gives

$$
\begin{equation*}
\phi_{y}(x, 0)=U_{\infty} f^{\prime}(x) \tag{1.14}
\end{equation*}
$$

We therefore obtain the boundary-value problem

$$
\begin{align*}
\left(1-M_{\infty}^{2}\right) \phi_{x x}+\phi_{y y} & =0  \tag{1.15}\\
\phi_{y}(x, 0) & =U_{\infty} f^{\prime}(x)  \tag{1.16}\\
\phi \rightarrow 0 & \text { as } y \rightarrow \infty \tag{1.17}
\end{align*}
$$

All geometric forcing enters through the boundary condition. The governing PDE itself remains homogeneous.

In the next chapter, we solve this problem explicitly and examine how the solution structure depends on the freestream Mach number.

## Chapter 2

## Subsonic Flow Past a Wavy Wall

### 2.1 From Governing Equation to Solution Strategy

We now solve the boundary-value problem formulated at the end of Chapter 1. For subsonic freestream Mach number $M_{\infty}<1$, the governing equation (1.15) is elliptic. Introduce the stretched coordinate

$$
\begin{equation*}
\xi=\sqrt{1-M_{\infty}^{2}} x \tag{2.1}
\end{equation*}
$$

under which (1.15) becomes

$$
\begin{equation*}
\phi_{\xi \xi}+\phi_{y y}=0 . \tag{2.2}
\end{equation*}
$$

Thus, in subsonic flow, the globally linearized compressible potential equation reduces exactly to Laplace's equation in $(\xi, y)$.

Interpretation. Compressibility does not change the type of the governing equation in subsonic flow. Instead, it rescales the streamwise coordinate. From the standpoint of the solution structure, subsonic compressible flow behaves like incompressible potential flow in a stretched geometry.

### 2.2 Boundary Condition in the Stretched Coordinate

The linearized boundary condition (1.14) may be expressed in terms of the stretched coordinate $\xi$ as

$$
\begin{equation*}
\phi_{y}(\xi, 0)=U_{\infty} \frac{d f}{d x}=U_{\infty} \frac{d f}{d \xi} \frac{d \xi}{d x} \tag{2.3}
\end{equation*}
$$

Using (2.1), we obtain

$$
\begin{equation*}
\phi_{y}(\xi, 0)=U_{\infty} \sqrt{1-M_{\infty}^{2}} f_{\xi}(\xi) \tag{2.4}
\end{equation*}
$$

We therefore seek solutions of Laplace's equation (2.2) satisfying

$$
\begin{align*}
\phi_{y}(\xi, 0) & =U_{\infty} \sqrt{1-M_{\infty}^{2}} f_{\xi}(\xi)  \tag{2.5}\\
\phi & \rightarrow 0 \quad \text { as } y \rightarrow \infty \tag{2.6}
\end{align*}
$$

### 2.3 Fourier Decomposition of the Wall Geometry

Because (2.2) is linear and translation-invariant in $\xi$, it is natural to decompose the wall geometry into Fourier modes. Assume the wall profile is sufficiently smooth and periodic, so that

$$
\begin{equation*}
f(\xi)=a_{0}+\sum_{k>0}\left[a_{k} \cos (k \xi)+b_{k} \sin (k \xi)\right] \tag{2.7}
\end{equation*}
$$

Differentiating gives

$$
\begin{equation*}
f_{\xi}(\xi)=\sum_{k>0}\left[-k a_{k} \sin (k \xi)+k b_{k} \cos (k \xi)\right] \tag{2.8}
\end{equation*}
$$

Substituting (2.8) into (2.5) shows that the boundary forcing at $y=0$ is a superposition of independent wavenumbers. Since (2.2) is linear with constant coefficients, different wavenumbers do not interact. We may therefore solve for each $k$ separately and then superpose the results.

### 2.4 Why the Solution is Oscillatory in $\xi$ and Evanescent in $y$

Before solving, it is worth extracting the key structural message from the PDE.
The boundary condition (2.5) prescribes oscillations in $\xi$ with wavenumber $k$. The PDE (2.2) is translationally invariant in $\xi$ and contains no mechanism to mix or generate new horizontal frequencies. This strongly suggests that each imposed wavenumber $k$ should persist in the interior solution: the flow response should oscillate in $\xi$ with the same $k$, while the $y$-dependence determines how that oscillation extends away from the wall.

We now formalize this using separation of variables for a single wavenumber.

### 2.5 Solution for a Single Wavenumber via Separation of Variables

Consider a single wavenumber component. We seek a separated form

$$
\begin{equation*}
\phi_{k}(\xi, y)=X_{k}(\xi) Y_{k}(y) \tag{2.9}
\end{equation*}
$$

Substituting (2.9) into Laplace's equation (2.2) gives

$$
X_{k}^{\prime \prime}(\xi) Y_{k}(y)+X_{k}(\xi) Y_{k}^{\prime \prime}(y)=0
$$

Dividing by $X_{k} Y_{k}$ yields

$$
\begin{equation*}
\frac{X_{k}^{\prime \prime}}{X_{k}}+\frac{Y_{k}^{\prime \prime}}{Y_{k}}=0 \tag{2.10}
\end{equation*}
$$

The first term depends only on $\xi$ and the second only on $y$, so each must be a constant. Write this constant as $-k^{2}$ :

$$
\begin{equation*}
\frac{X_{k}^{\prime \prime}}{X_{k}}=-k^{2}, \quad \frac{Y_{k}^{\prime \prime}}{Y_{k}}=k^{2} \tag{2.11}
\end{equation*}
$$

This choice is not arbitrary: it is fixed by the boundary forcing. The boundary condition contains $\sin (k \xi)$ and $\cos (k \xi)$ at a particular wavenumber $k$, so we must choose the separation constant so that $X_{k}$ admits oscillatory solutions with that same wavenumber.

Equations (2.11) give the ODEs

$$
\begin{equation*}
X_{k}^{\prime \prime}+k^{2} X_{k}=0, \quad Y_{k}^{\prime \prime}-k^{2} Y_{k}=0 \tag{2.12}
\end{equation*}
$$

Thus,

$$
\begin{equation*}
X_{k}(\xi)=A_{k} \cos (k \xi)+B_{k} \sin (k \xi) \tag{2.13}
\end{equation*}
$$

and

$$
\begin{equation*}
Y_{k}(y)=C_{k} e^{k y}+D_{k} e^{-k y} \tag{2.14}
\end{equation*}
$$

The far-field condition (2.6) eliminates the growing exponential, so $C_{k}=0$ and

$$
\begin{equation*}
Y_{k}(y)=D_{k} e^{-k y} \tag{2.15}
\end{equation*}
$$

Interpretation. For each horizontal wavenumber $k$, Laplace's equation preserves the horizontal oscillation and produces an evanescent (exponentially decaying) response away from the boundary. Larger $k$ (shorter wavelengths) decay more rapidly with $y$.

### 2.6 Matching the Boundary Condition and Superposition

From (2.13)-(2.15), the general decaying solution at wavenumber $k$ may be written as

$$
\begin{equation*}
\phi_{k}(\xi, y)=e^{-k y}\left[\alpha_{k} \cos (k \xi)+\beta_{k} \sin (k \xi)\right] \tag{2.16}
\end{equation*}
$$

Differentiating gives

$$
\phi_{k, y}(\xi, 0)=-k\left[\alpha_{k} \cos (k \xi)+\beta_{k} \sin (k \xi)\right]
$$

On the other hand, the boundary forcing at wavenumber $k$ from (2.8) and (2.5) is

$$
\phi_{y}(\xi, 0)=U_{\infty} \sqrt{1-M_{\infty}^{2}}\left[-k a_{k} \sin (k \xi)+k b_{k} \cos (k \xi)\right]
$$

Matching coefficients yields

$$
\alpha_{k}=-U_{\infty} \sqrt{1-M_{\infty}^{2}} b_{k}, \quad \beta_{k}=U_{\infty} \sqrt{1-M_{\infty}^{2}} a_{k}
$$

Therefore,

$$
\begin{equation*}
\phi_{k}(\xi, y)=U_{\infty} \sqrt{1-M_{\infty}^{2}} e^{-k y}\left[a_{k} \sin (k \xi)-b_{k} \cos (k \xi)\right] \tag{2.17}
\end{equation*}
$$

By superposition over all $k>0$,

$$
\begin{equation*}
\phi(\xi, y)=U_{\infty} \sqrt{1-M_{\infty}^{2}} \sum_{k>0} e^{-k y}\left[a_{k} \sin (k \xi)-b_{k} \cos (k \xi)\right] \tag{2.18}
\end{equation*}
$$

### 2.7 Pressure Distribution

The pressure coefficient follows from the linearized relation (1.11):

$$
C_{p}(x, 0)=-\frac{2}{U_{\infty}} \phi_{x}(x, 0)
$$

Using $\xi=\sqrt{1-M_{\infty}^{2}} x$, we have

$$
\begin{equation*}
\partial_{x}=\sqrt{1-M_{\infty}^{2}} \partial_{\xi} \tag{2.19}
\end{equation*}
$$

Evaluate $\phi_{\xi}$ from (2.18) at $y=0$ :

$$
\phi_{\xi}(\xi, 0)=U_{\infty} \sqrt{1-M_{\infty}^{2}} \sum_{k>0} k\left[a_{k} \cos (k \xi)+b_{k} \sin (k \xi)\right]
$$

Therefore,

$$
\phi_{x}(x, 0)=U_{\infty}\left(1-M_{\infty}^{2}\right) \sum_{k>0} k\left[a_{k} \cos (k \xi(x))+b_{k} \sin (k \xi(x))\right]
$$

and the pressure coefficient becomes

$$
\begin{equation*}
C_{p}(x, 0)=-2\left(1-M_{\infty}^{2}\right) \sum_{k>0} k\left[a_{k} \cos (k \xi(x))+b_{k} \sin (k \xi(x))\right], \quad \xi(x)=\sqrt{1-M_{\infty}^{2}} x \tag{2.20}
\end{equation*}
$$

Interpretation. The surface pressure has the same Fourier structure as the wall geometry. Compressibility modifies only the amplitude via the factor $\left(1-M_{\infty}^{2}\right)$, and the stretched coordinate $\xi(x)$ reflects the streamwise rescaling.

### 2.8 Summary

In subsonic small-disturbance flow:

- the governing equation reduces to Laplace's equation in stretched coordinates,
- each horizontal wavenumber persists in the interior solution,
- the vertical dependence is evanescent, with decay rate proportional to the wavenumber,
- compressibility modifies the response through streamwise stretching and amplitude scaling.

In the next chapter, we examine how the structure changes fundamentally in supersonic flow, where the governing equation becomes hyperbolic and solutions develop characteristic directions.

## Chapter 3

### Supersonic Flow Past a Wavy Wall and Wave Drag

We now solve the boundary-value problem from Chapter 1 in the supersonic regime $M_{\infty}>1$. In this case, the governing equation (1.15) is hyperbolic, and the solution structure changes fundamentally: disturbances do not propagate globally, but instead travel along characteristic directions.

### 3.1 Hyperbolic Structure via a Scaling to the Wave Equation

Introduce the Mach-dependent parameter

$$
\begin{equation*}
\mu:=\sqrt{M_{\infty}^{2}-1} \tag{3.1}
\end{equation*}
$$

and define a stretched vertical coordinate

$$
\begin{equation*}
\eta:=y \mu . \tag{3.2}
\end{equation*}
$$

Since $\partial_{y}=\mu \partial_{\eta}$, we have $\phi_{y y}=\mu^{2} \phi_{\eta \eta}$, and substituting into (1.15) gives

$$
\mu^{2} \phi_{\eta \eta}-\mu^{2} \phi_{x x}=0
$$

Multiplying by $1 / \mu^{2}$ yields the canonical wave equation in $(x, \eta)$ :

$$
\begin{equation*}
\phi_{\eta \eta}-\phi_{x x}=0 \tag{3.3}
\end{equation*}
$$

Interpretation. In subsonic flow, the stretched coordinate in Chapter 2 turned the elliptic PDE into Laplace's equation. Here, the corresponding scaling turns the hyperbolic PDE into the wave equation. This makes the notion of propagation directions (characteristics) mathematically precise.

### 3.2 Characteristic Variables and Physical Causality

Equation (3.3) is the standard one-dimensional wave equation (with $\eta$ playing the role of "time"). A key consequence is that the general solution is a superposition of two traveling-wave families:

$$
\begin{equation*}
\phi(x, \eta)=F(x+\eta)+G(x-\eta) \tag{3.4}
\end{equation*}
$$

where $F$ and $G$ are determined by boundary data.
Returning to physical variables using (3.2), define the two characteristic combinations

$$
\begin{equation*}
s_{+}(x, y):=x+y \mu, \quad s_{-}(x, y):=x-y \mu . \tag{3.5}
\end{equation*}
$$

Then (3.4) becomes

$$
\begin{equation*}
\phi(x, y)=F\left(s_{+}(x, y)\right)+G\left(s_{-}(x, y)\right) \tag{3.6}
\end{equation*}
$$

Causality (why we keep only one family). Consider a point $(x, y)$ with $y>0$. Along the line $s_{-}(x, y)=$ const we have $y=1 / \mu(x-$ const $)$, which intersects the wall $y=0$ at the upstream location $x=$ const. Thus the $G\left(s_{-}\right)$family represents information that travels from the wall into the flow in a physically causal manner.

In contrast, $s_{+}(x, y)=$ const intersects $y=0$ at $x=$ const $-y \mu$, i.e. information that would have to arrive from downstream to determine the upstream solution. In the usual small-disturbance supersonic setting, we enforce "no upstream influence" and retain only the $s_{-}$family:

$$
\begin{equation*}
\phi(x, y)=G(x-\mu y) \tag{3.7}
\end{equation*}
$$

### 3.3 Determination of the Solution from the Wall Boundary Condition

We now determine $G$ using the linearized no-penetration condition (1.16):

$$
\phi_{y}(x, 0)=U_{\infty} f^{\prime}(x)
$$

Differentiate (3.7). With $s_{-}(x, y)=x-y \mu$, we have $s_{-, y}=-\mu$, so

$$
\phi_{y}(x, y)=G^{\prime}\left(s_{-}\right) s_{-, y}=-\mu G^{\prime}\left(s_{-}\right)
$$

Evaluating at $y=0$ (so $\left.s_{-}=x\right)$ and matching (1.16) yields

$$
\begin{equation*}
-\mu G^{\prime}(x)=U_{\infty} f^{\prime}(x) \quad \Longrightarrow \quad G^{\prime}(x)=-\frac{1}{\mu} U_{\infty} f^{\prime}(x) \tag{3.8}
\end{equation*}
$$

Integrating (and choosing the additive constant so $\phi$ has zero mean, which does not affect velocities) gives

$$
\begin{equation*}
G(x)=-\frac{U_{\infty}}{\mu} f(x) \tag{3.9}
\end{equation*}
$$

Therefore, the supersonic disturbance potential is

$$
\begin{equation*}
\phi(x, y)=-\frac{U_{\infty}}{\mu} f(x-y \mu) \tag{3.10}
\end{equation*}
$$

Interpretation. The wall shape is "imprinted" into the flow and propagates along the lines $x-y / \mu=$ const, i.e. $y=\mu(x-$ const $)$. This is the mathematical origin of Mach-line structure in smalldisturbance supersonic flow.

### 3.4 Supersonic Surface Pressure

The pressure coefficient follows from the globally linearized relation (1.11):

$$
C_{p}(x, y)=-\frac{2}{U_{\infty}} \phi_{x}(x, y)
$$

Differentiate (3.10) with respect to $x$ :

$$
\phi_{x}(x, y)=-\frac{U_{\infty}}{\mu} f^{\prime}(x-y \mu)
$$

so

$$
\begin{equation*}
C_{p}(x, y)=\frac{2}{\mu} f^{\prime}(x-y \mu) . \tag{3.11}
\end{equation*}
$$

In particular, on the reference line $y=0$,

$$
\begin{equation*}
C_{p}(x, 0)=\frac{2}{\mu} f^{\prime}(x) \tag{3.12}
\end{equation*}
$$

This compact result is one of the central structural differences between subsonic and supersonic small-disturbance flow: in the supersonic case, the surface pressure is in phase with the wall slope.

### 3.5 Wave Drag from the Surface Pressure

We now compute the streamwise force induced by the pressure distribution and compare the subsonic and supersonic outcomes.

## Step 1: Pressure is applied on the actual wall

Pressure acts on the physical surface $y=f(x)$ (with $\|f\|=\epsilon \ll 1$ ), not on the reference line $y=0$. We therefore expand the pressure coefficient about $y=0$ :

$$
\begin{equation*}
C_{p}(x, f(x))=C_{p}(x, 0)+f(x) C_{p, y}(x, 0)+O\left(\epsilon^{2}\right) . \tag{3.13}
\end{equation*}
$$

This makes clear why "evaluate at $y=0$ " is only the leading approximation.

## Step 2: Project pressure onto the streamwise direction

The pressure force per unit span acting on a surface element is

$$
d \boldsymbol{F}=-\left(p-p_{\infty}\right) \boldsymbol{n} d s
$$

where $n$ points into the fluid and $d s$ is arclength along the wall. Parameterize the wall by $\boldsymbol{r}(x)=(x, f(x))$. A tangent vector is proportional to $\left(1, f^{\prime}\right)$, so a unit normal may be taken as

$$
\boldsymbol{n}=\frac{\left(-f^{\prime}(x), 1\right)}{\sqrt{1+\left(f^{\prime}(x)\right)^{2}}}, \quad d s=\sqrt{1+\left(f^{\prime}(x)\right)^{2}} d x
$$

Multiplying these yields the useful identity

$$
\begin{equation*}
\boldsymbol{n} d s=\left(-f^{\prime}(x), 1\right) d x \tag{3.14}
\end{equation*}
$$

The streamwise (drag) component is therefore

$$
d D=-\left(p-p_{\infty}\right) n_{x} d s=\left(p-p_{\infty}\right) f^{\prime}(x) d x
$$

Using $p-p_{\infty}=\frac{1}{2} \rho_{\infty} U_{\infty}^{2} C_{p}$, the drag per unit span over one wavelength $L$ is proportional to

$$
\begin{equation*}
D \propto \epsilon \int_{x_{0}}^{x_{0}+L} C_{p}(x, f(x)) f^{\prime}(x) d x \tag{3.15}
\end{equation*}
$$

where $x_{0}$ is arbitrary due to periodicity.

## Step 3: Leading-order drag and why it differs by regime

Substitute the wall expansion (3.13) into (3.15):

$$
\begin{equation*}
D \propto \epsilon \int_{x_{0}}^{x_{0}+L} C_{p}(x, 0) f^{\prime}(x) d x+O\left(\epsilon^{2}\right) \tag{3.16}
\end{equation*}
$$

Thus the leading-order contribution is controlled by $C_{p}(x, 0)$, and the key question becomes: how does $C_{p}(x, 0)$ relate to the wall shape $f$ ?

Subsonic case (leading-order cancellation). From Chapter 2, the subsonic surface pressure on $y=0$ is given by (2.20). For a single physical wavenumber component, that result implies that $C_{p}(x, 0)$ is in phase with $f(x)$ (it is proportional to the wall shape, up to Mach-dependent amplitude and coordinate stretching). As a consequence, the leading-order drag term becomes proportional to

$$
D \propto \int_{x_{0}}^{x_{0}+L} f(x) f^{\prime}(x) d x=\frac{1}{2} \int_{x_{0}}^{x_{0}+L} \frac{d}{d x}\left(f(x)^{2}\right) d x=0
$$

so the $O(\epsilon)$ term in (3.16) cancels for a periodic wall. Subsonic drag therefore enters only at higher order in $\epsilon$ within this model.

Supersonic case (nonzero wave drag). In supersonic flow we found the surface pressure (3.12) was proportional to $f^{\prime}(x)$. Substituting this into the leading-order term in (3.16) gives

$$
D \propto \int_{x_{0}}^{x_{0}+L}\left(f^{\prime}(x)\right) f^{\prime}(x) d x=\int_{x_{0}}^{x_{0}+L}\left(f^{\prime}(x)\right)^{2} d x
$$

Thus

$$
\begin{equation*}
D \propto \int_{x_{0}}^{x_{0}+L}\left(f^{\prime}(x)\right)^{2} d x>0, \quad\left(M_{\infty}>1\right) \tag{3.17}
\end{equation*}
$$

which is the classical wave drag result: in the supersonic regime, pressure is in phase with slope, so pressure forces have a systematic streamwise component that does not cancel over a wavelength.

Interpretation. The contrast is geometric and phase-based:

- In subsonic flow (elliptic), the pressure distribution is essentially tied to the wall shape, producing cancellations in $\int C_{p} f^{\prime} d x$ over a period.
- In supersonic flow (hyperbolic), the pressure is tied to the wall slope and propagates along characteristics, yielding $\int\left(f^{\prime}\right)^{2} d x$ and a net positive drag.


### 3.6 Summary

In supersonic small-disturbance flow:

- the governing PDE (1.15) reduces to the wave equation under the scaling (3.2),
- solutions decompose into characteristic families (3.6), and causality selects the downstreampropagating family (3.7),
- the wall geometry imprints into the flow as (3.10),
- the surface pressure satisfies $C_{p}(x, 0)=2 / \mu f^{\prime}(x)$ (3.12), leading to the nonzero wave-drag scaling (3.17).

