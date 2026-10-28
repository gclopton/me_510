## CHAPTER 14

## Artificial Viscosity

### 14.0 Introduction

It sometimes makes sense to divide numerical approximations into first differences and second differences. For example, Equation (10.17) can be written as

$$
\frac{d f}{d x}\left(x_{i-1}\right)=\frac{f\left(x_{i}\right)-f\left(x_{i-1}\right)}{\Delta x}-\frac{f\left(x_{i+1}\right)-2 f\left(x_{i}\right)+f\left(x_{i-1}\right)}{2 \Delta x}+O\left(\Delta x^{2}\right) .
$$

From one point of view, second differences naturally appear as part of approximations to first derivatives, as in the preceding expression. From another point of view, first differences approximate first derivatives and second differences approximate second derivatives. In our applications, we will often associate first differences with the first derivatives in the Euler equations and scalar conservation laws and second differences with viscous terms in the Navier-Stokes equations. Then the second differences are called artificial viscosity. The term "artificial" reminds us that the second differences in question may not have much to do with physical viscosity. For example, artificial viscosity almost never involves the true coefficient of viscosity. In fact, the true viscosity is typically small in gasdynamics, outside of thin boundary layers coating solid surfaces; this justifies dropping the viscous terms in the first place and means that second differences that truly approximated viscous terms would not have much effect in most of the flow. At best, artificial viscosity has viscous-like effects, but the form and amount of artificial viscosity are chosen on a purely numerical basis.

Many first-derivative approximations also involve higher-order differences; fourth, sixth, and other even-order differences are generally also called artificial viscosity, while third, fifth, and other odd-order differences are generally called artificial dispersion. These higherorder differences are discussed in the next chapter. This chapter concerns only first- and second-order differences.

### 14.1 Physical Viscosity

To help introduce artificial viscosity and its relationship to numerical stability, this section concerns physical viscosity and its relationship to physical stability. The Navier-Stokes equations govern viscous flows. Making standard assumptions such as Stokes' hypothesis and Fourier's law for heat transfer, the conservation form of the NavierStokes equations for one-dimensional compressible flows is

$$
\begin{aligned}
& \frac{\partial \rho}{\partial t}+\frac{\partial(\rho u)}{\partial x}=0 \\
& \frac{\partial(\rho u)}{\partial t}+\frac{\partial}{\partial x}\left(\rho u^{2}+p\right)=\frac{\partial}{\partial x}\left(\frac{4}{3} \mu \frac{\partial u}{\partial x}\right) \\
& \frac{\partial\left(\rho e_{T}\right)}{\partial t}+\frac{\partial}{\partial x}\left(\rho u e_{T}+p u\right)=\frac{\partial}{\partial x}\left(\frac{4}{3} \mu u \frac{\partial u}{\partial x}+k \frac{\partial T}{\partial x}\right)
\end{aligned}
$$

where $\mu \geq 0$ is the coefficient of viscosity and $k \geq 0$ is the coefficient of thermal conductivity. Notice that the left-hand side of the Navier-Stokes equations is exactly the same as the left-hand side of the Euler equations. However, where the Euler equations have zeros on the right-hand side, the Navier-Stokes equations have second derivative terms involving $\mu$ and $k$. The two terms involving $\mu$ are viscosity terms, where viscosity in fluids is the same thing as friction in solids, and the term involving $k$ is a heat conduction term.

Before discussing the relationship between physical viscosity and physical stability, we must first define physical stability. In general, a physical system is stable if the system returns to its original state after any small disturbance. A physical system is neutrally stable if small disturbances cause proportionately small but permanent disturbances. Finally, a physical system is unstable if small disturbances lead to large disturbances. A classic example is a ball on a surface. A ball in a valley is stable - a small disturbance causes the ball to oscillate inside the valley, running up one side of the valley and down the other, until friction damps the motion, and the ball returns to rest. A ball on a perfectly flat surface is neutrally stable - a small disturbance causes the ball to move a small distance. Finally, a ball on a peaked surface is unstable - any small disturbance causes the ball to run down the sides of the peak, gaining speed as it releases its gravitational potential energy, until it comes to rest in some stable, neutrally stable, or even unstable position. As you might expect, friction has a stabilizing effect on the ball, although no amount of friction can stabilize a ball balanced on top of a sharp peak.

As another simple example of stability, consider a driven damped pendulum. This simple system allows all sorts of strange and complicated behaviors, making it a favorite example in the study of dynamical systems and chaos. Whereas large amounts of damping always stabilize the pendulum's motion, or even prevent the pendulum from moving, small amounts of damping lead to unstable and chaotic behaviors not found in an ideal frictionless pendulum. See Tabor (1989) for more information on the stability of the driven damped pendulum.

Now we turn to the most relevant example - fluid flows. Like any physical system, fluid flows may be stable, neutrally stable, or unstable. Stable flows damp out small disturbances, while unstable flows amplify them. For example, small disturbances in unstable laminar flows lead to oscillatory waves, called Tollmien-Schlichting waves, whose amplitudes grow downstream and with time, ultimately creating first bursts of turbulence and then continuous turbulence, characterized by highly unstable small-scale features. Examples of unstable laminar flows include jets, wakes, shear layers, and boundary layers with adverse pressure gradients.

A classic stability analysis technique called small perturbation analysis leads to Rayleigh's equation in the case of incompressible laminar inviscid flow, to the Orr-Sommerfeld equation in the case of incompressible laminar viscous flow, and to more complicated equations for compressible flows. Small perturbation analysis shows that viscosity has a dramatic effect on the stability of fluid flows, just as in other physical systems. In most cases, viscosity tends to stabilize fluid flows but, like the driven damped pendulum, sometimes small increases in viscosity may actually destabilize fluid flows. See White (1991) for a more thorough introduction to the stability of fluid flows. This completes our necessarily brief introduction to physical viscosity and stability.

### 14.2 Artificial Viscosity Form

Chapter 11 discussed conservation form, and Chapter 13 discussed flux split forms and wave speed split forms. This section introduces a fourth form, artificial viscosity form,
composed of FTCS plus second-order artificial viscosity. Like the flux and wave speed split forms, artificial viscosity form can aid stability analyses.

The Euler equations omit viscosity; however, discretization generally reintroduces viscosity or, more precisely, second-difference terms that have viscous-like effects. Second differences that arise naturally as part of first-derivative approximation are called implicit artificial viscosity. Second differences purposely added to first-derivative approximations are called explicit artificial viscosity. In this context, the term implicit means "hidden and probably unintended" while explicit means "out in the open and intentional." Hopefully, these usages of "implicit" and "explicit" will not cause too much confusion with the earlier usages. This section concerns explicit (second meaning) artificial viscosity in explicit (first meaning) finite-difference approximations.

The viscous terms in the Navier-Stokes equations (14.1) have the following general form:

$$
\frac{\partial}{\partial x}\left(\epsilon \frac{\partial U}{\partial x}\right)
$$

where $\epsilon=\mu, \mu u, k$ and $U=u, T$. Now consider a scalar conservation law,

$$
\frac{\partial u}{\partial t}+\frac{\partial f(u)}{\partial x}=0
$$

Add a viscous-like term to the right-hand side as follows:

$$
\frac{\partial u}{\partial t}+\frac{\partial f(u)}{\partial x}=\frac{\partial}{\partial x}\left(\epsilon(u) \frac{\partial u}{\partial x}\right)
$$

where $\epsilon \geq 0$. Remember that the viscous-like term is added for numerical reasons and generally has no relationship to physical viscosity. As a result, the discretization of the viscous term need not be accurate, provided only that the discretized viscosity term has desirable numerical effects. A conservative forward-time central-space discretization of Equation (14.2) yields

$$
\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}+\frac{f\left(u_{i+1}^{n}\right)-f\left(u_{i-1}^{n}\right)}{2 \Delta x}=\frac{\epsilon_{i+1 / 2}^{n} \frac{u_{i+1}^{n}-u_{i}^{n}}{\Delta x}-\epsilon_{i-1 / 2}^{n} \frac{u_{i}^{n}-u_{i-1}^{n}}{\Delta x}}{\Delta x} .
$$

For convenience, absorb the factor $2 / \Delta x$ into $\epsilon_{i+1 / 2}^{n}$. Then rearranging terms yields the following:

$$
\begin{aligned}
\quad u_{i}^{n+1}= & u_{i}^{n}-\frac{\lambda}{2}\left(f\left(u_{i+1}^{n}\right)-f\left(u_{i-1}^{n}\right)\right) \\
& +\frac{\lambda}{2}\left(\epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right)-\epsilon_{i-1 / 2}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)\right) .
\end{aligned}
$$

This is known as an artificial viscosity form, the terms involving $\epsilon_{i+1 / 2}^{n}$ are called secondorder explicit artificial viscosity, and $\epsilon_{i+1 / 2}^{n}$ is called the coefficient of second-order explicit artificial viscosity. This artificial viscosity form applies equally to scalar and vector conservation laws. For vector conservation laws, the coefficient of viscosity $\epsilon_{i+1 / 2}^{n}$ can be either a scalar or a matrix. Although useful for purposes of introduction, few numerical methods actually derive from equations such as (14.2). Instead, artificial viscosity arises naturally as part of the first-derivative approximations, or gets added after the fact, so that the coefficient of artificial viscosity $\epsilon_{i+1 / 2}^{n}$ generally has no relationship to any $\epsilon(u)$.

Equation (14.3) involves FTCS. Of course, FTCS can be replaced by any other method. For example, suppose the viscous term in Equation (14.2) is discretized as before, while the flux term is discretized using FTFS. Then one obtains

$$
\begin{aligned}
u_{i}^{n+1}= & u_{i}^{n}-\lambda\left(f\left(u_{i+1}^{n}\right)-f\left(u_{i}^{n}\right)\right) \\
& +\frac{\lambda}{2}\left(\epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right)-\epsilon_{i-1 / 2}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)\right) .
\end{aligned}
$$

Besides changing the discretization of the flux term, one could also change the discretization of the viscous term. Despite these myriad of possibilities, this book reserves the phrase "artificial viscosity form" specifically for the traditional equation (14.3).

Artificial viscosity form is related to conservation form by

$$
\hat{f}_{i+1 / 2}^{n}=\frac{1}{2}\left[f\left(u_{i+1}^{n}\right)+f\left(u_{i}^{n}\right)-\epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right)\right] .
$$

Equation (14.4) allows easy transformation from conservation form to artificial viscosity form and vice versa. In fact, for scalar conservation laws, every $\hat{f}_{i+1 / 2}^{n}$ yields a unique $\epsilon_{i+1 / 2}^{n}$ and vice versa. For vector conservation laws, Equation (14.4) may have no solution if $\epsilon_{i+1 / 2}^{n}$ is a scalar or infinitely many solutions if $\epsilon_{i+1 / 2}^{n}$ is a matrix. The solution for matrix coefficients $\epsilon_{i+1 / 2}^{n}$ proceeds as in Section 5.3.

From one point of view, artificial viscosity form is just a variation on the flux-correction form seen in Section 13.3. As seen in Equation (13.5), the flux-correction form is

$$
\hat{f}_{i+1 / 2}^{n}=\hat{f}_{i+1 / 2}^{(1)}+\hat{f}_{i+1 / 2}^{(\mathrm{C})},
$$

where $\hat{f}_{i+1 / 2}^{(1)}$ is the conservative numerical flux of some reference method and $\hat{f}_{i+1 / 2}^{(\mathrm{C})}$ is a flux correction to the reference. Compare this last equation with Equation (14.4) to find the following:

$$
\begin{aligned}
& \hat{f}_{i+1 / 2}^{(1)}=\frac{1}{2}\left(f\left(u_{i+1}^{n}\right)+f\left(u_{i}^{n}\right)\right)=\hat{f}_{i+1 / 2}^{\mathrm{FTCS}}, \\
& \hat{f}_{i+1 / 2}^{(\mathrm{C})}=-\frac{1}{2} \epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right) .
\end{aligned}
$$

Thus artificial viscosity form is FTCS plus a flux correction, where the flux correction is factored into a coefficient $\epsilon_{i+1 / 2}^{n}$ times a first difference $u_{i+1}^{n}-u_{i}^{n}$. Oftentimes, when a method is written as a flux correction to FTCS, the flux correction includes first-difference factors $u_{i+1}^{n}-u_{i}^{n}$, making the artificial viscosity form especially convenient and natural. Unfortunately, the artificial viscosity form generally involves infinite coefficients when the flux correction does not include first-difference factors $u_{i+1}^{n}-u_{i}^{n}$. In particular, suppose that $u_{i+1}^{n}-u_{i}^{n}=0$. Then if $\epsilon_{i+1 / 2}^{n}$ is finite, the flux correction is zero and the method equals FTCS or, more specifically, $\hat{f}_{i+1 / 2}^{n}=f\left(u_{i}^{n}\right)=f\left(u_{i+1}^{n}\right)$. Otherwise, if the method does not equal FTCS then $\epsilon_{i+1 / 2}^{n}$ is infinite, which is usually the case when the method's stencil contains more than two or three points. Recall that a similar discussion took place in Section 13.5, where the first differences appearing in the wave speed split form also lead to infinite coefficients.

Artificial viscosity forms sometimes suggest alterations and improvements. For example, in one interpretation, the implicit artificial viscosity in FTCS is too small, making FTCS unstable, and adding explicit second-order artificial viscosity with a positive coefficient has a
smoothing and stabilizing effect. In other cases, a numerical method may have too much artificial viscosity, causing smearing or even instability. In this case, adding explicit artificial viscosity with a negative coefficient partially cancels the implicit artificial viscosity, resulting in a sharper, more detailed, and even more stable solution. Second-order artificial viscosity with a positive coefficient is sometimes called artificial dissipation; second-order artificial viscosity with a negative coefficient is sometimes also called artificial antidissipation.

Example 14.1 Write FTFS and FTBS in artificial viscosity form for both vector and scalar conservation laws. Discuss the relationship between stability and the sign of the coefficient of artificial viscosity.

Solution First consider FTFS. By Equation (14.4),

$$
f\left(u_{i+1}^{n}\right)=\frac{1}{2}\left[f\left(u_{i+1}^{n}\right)+f\left(u_{i}^{n}\right)-\epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right)\right] .
$$

For scalar conservation laws, solve for $\epsilon_{i+1 / 2}^{n}$ to find

$$
\epsilon_{i+1 / 2}^{n}=-a_{i+1 / 2}^{n},
$$

where as usual

$$
a_{i+1 / 2}^{n}= \begin{cases}\frac{f\left(u_{i+1}^{n}\right)-f\left(u_{i}^{n}\right)}{u_{i+1}^{n}-u_{i}^{n}} & u_{i+1}^{n} \neq u_{i}^{n}, \\ f^{\prime}\left(u_{i}^{n}\right) & u_{i+1}^{n}=u_{i}^{n} .\end{cases}
$$

Similarly, FTBS yields

$$
\epsilon_{i+1 / 2}^{n}=a_{i+1 / 2}^{n} .
$$

Notice that both coefficients of artificial viscosity are finite. Also notice that FTBS and FTFS are stable when their coefficients of artificial viscosity are positive and unstable when their coefficients of artificial viscosity are negative. Then, from this point of view, a sufficient amount of artificial dissipation can successfully stabilize FTCS.

For vector conservation laws, the previous expressions apply except that $a_{i+1 / 2}^{n}$ is replaced by the Roe-average Jacobian matrix $A_{i+1 / 2}^{n}$ or some other secant plane slope matrix, as described in Section 5.3. Such artificial viscosity successfully stabilizes the method only when all of the characteristic values of $A_{i+1 / 2}^{n}$ are positive and sufficiently large.

There are a number of potential pitfalls with the concept of artificial viscosity. As mentioned before, artificial viscosity may give a false impression of physicality (remember that it is called artificial viscosity for a reason). Furthermore, many people treat artificial viscosity as an afterthought. A typical statement along these lines is as follows: "Standard artificial viscosity was added to the numerical method to reduce spurious oscillations." However, taking the broadest view of artificial viscosity, any method can be written as any other method plus artificial viscosity. Thus, adding artificial viscosity fundamentally alters a method; changing the second differences has almost as much effect as changing the first differences. In some cases, it is more convenient to design or analyze the coefficient of artificial viscosity $\epsilon_{i+1 / 2}^{n}$ rather than the conservative fluxes $\hat{f}_{i+1 / 2}^{n}$, but the one leads to the other, and the design or analysis problem is never trivial either way.

## References

Tabor, M. 1989. Chaos and Integrability in Nonlinear Dynamics: An Introduction, New York: Wiley. White, F. M. 1991. Viscous Fluid Flow, 2nd ed., New York: McGraw-Hill, Chapter 5.

## Problems

14.1 Consider the following numerical approximation to a scalar conservation law:
$u_{i}^{n+1}=u_{i}^{n}-\frac{\lambda}{2}\left(3 f\left(u_{i}^{n}\right)-4 f\left(u_{i-1}^{n}\right)+f\left(u_{i-2}^{n}\right)\right)$.
(a) Write this method in standard artificial viscosity form. That is, write the method as FTCS plus second-order artificial viscosity.
(b) Write this method as FTBS plus second-order artificial viscosity. Does the method have more or less artificial viscosity than FTBS? In particular, for $a>0$, show that the method has more artificial viscosity than FTBS at maxima and minima and less artificial viscosity than FTBS in monotone regions.
14.2 Consider the following numerical approximation to a scalar conservation law:
$u_{i}^{n+1}=u_{i}^{n}+\frac{\lambda}{12}\left(f\left(u_{i+2}^{n}\right)-8 f\left(u_{i+1}^{n}\right)+8 f\left(u_{i-1}^{n}\right)-f\left(u_{i-2}^{n}\right)\right)$.
Write this method in standard artificial viscosity form.
14.3 This problem concerns the relationship between artificial viscosity form and wave speed split form.
(a) Find an expression for $\epsilon_{i+1 / 2}^{n}$ in terms of $C_{i+1 / 2}^{+}, C_{i+1 / 2}^{-}$, and $g_{i}^{n}$. Specifically, suppose a conservative numerical method is written in wave speed split form as follows:
$u_{i}^{n+1}=u_{i}^{n}+C_{i+1 / 2}^{+}\left(u_{i+1}^{n}-u_{i}^{n}\right)-C_{i-1 / 2}^{-}\left(u_{i}^{n}-u_{i-1}^{n}\right)$
such that
$\left(C_{i+1 / 2}^{-}-C_{i+1 / 2}^{+}\right)\left(u_{i+1}^{n}-u_{i}^{n}\right)=\lambda\left(g_{i+1}^{n}-g_{i}^{n}\right)$.
Then show that the method can be written in the following form:
$u_{i}^{n+1}=u_{i}^{n}-\frac{\lambda}{2}\left(g_{i+1}^{n}-g_{i-1}^{n}\right)+\frac{1}{2} \lambda \epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right)-\frac{1}{2} \lambda \epsilon_{i-1 / 2}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)$,
where
$\lambda \epsilon_{i+1 / 2}^{n}=C_{i+1 / 2}^{+}+C_{i+1 / 2}^{-}$.
If $g_{i}^{n}=f\left(u_{i}^{n}\right)$ then

$$
\begin{aligned}
u_{i}^{n+1}= & u_{i}^{n}-\frac{\lambda}{2}\left(f\left(u_{i+1}^{n}\right)-f\left(u_{i-1}^{n}\right)\right)+\frac{1}{2} \lambda \epsilon_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right) \\
& -\frac{1}{2} \lambda \epsilon_{i-1 / 2}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)
\end{aligned}
$$

which is the standard artificial viscosity form.
(b) Reverse the results found in part (a) to find expressions for $C_{i+1 / 2}^{+}$and $C_{i+1 / 2}^{-}$in terms of $\epsilon_{i+1 / 2}^{n}$ and $g_{i}^{n}$.
14.4 By examining conservative numerical flux, argue that second-order artificial viscosity transfers conserved quantities from cells that have more to cells that have less. Like Robin Hood, it takes from the rich and gives to the poor.

