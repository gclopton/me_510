Grady Clopton
ME 510
Midterm


# Problem 1: Thermodynamic closure and linearized pressure response (20 points)

##### problem 1.a

The thermodynamic definition of the sound speed is
$$
a^{2}:=\left(\frac{\partial p}{\partial \rho}\right)_{s}.
$$
Pressure is the response variable because compressive disturbances act mechanically through pressure forces. In the momentum equation it is $\nabla p$ that produces acceleration. Density is the perturbation variable because compression or expansion of a fluid element is most directly measured by the resulting change in mass per unit volume. Entropy is held fixed because the disturbance is assumed small, fast, and reversible, so heat transfer and irreversible entropy production do not have time to act during the response. Under that locally isentropic restriction, the derivative isolates the intrinsic compressive stiffness of the medium.


##### problem 1.b

Let the equation of state be written locally as $p=p(\rho,s)$, and expand about the uniform reference state $(\rho_*,s_*)$. With
$$
p'=p-p_*, \qquad \rho'=\rho-\rho_*, \qquad s'=s-s_*,
$$
the first-order expansion is
$$
\begin{aligned}
p(\rho,s)
&=p(\rho_*,s_*)+\left.\left(\frac{\partial p}{\partial \rho}\right)_{s}\right|_*(\rho-\rho_*)+\left.\left(\frac{\partial p}{\partial s}\right)_{\rho}\right|_*(s-s_*)+\mathcal{O}\!\left((\rho-\rho_*)^{2},(s-s_*)^{2},(\rho-\rho_*)(s-s_*)\right) \\
&=p_*+\left.\left(\frac{\partial p}{\partial \rho}\right)_{s}\right|_*\rho'+\left.\left(\frac{\partial p}{\partial s}\right)_{\rho}\right|_*s'+\mathcal{O}\!\left((\rho')^{2},(s')^{2},\rho's'\right) \\
&=p_*+\left.\left(\frac{\partial p}{\partial \rho}\right)_{s}\right|_*\rho'+\mathcal{O}\!\left((\rho')^{2}\right) \qquad (\text{use } s'=0 \text{ for a locally isentropic disturbance}) \\
&\approx p_*+\left.\left(\frac{\partial p}{\partial \rho}\right)_{s}\right|_*\rho' \\
p-p_*
&\approx \left.\left(\frac{\partial p}{\partial \rho}\right)_{s}\right|_*\rho' \\
p'
&\approx a_*^{2}\rho'.
\end{aligned}
$$
Thus the quantity being linearized is the thermodynamic pressure function $p(\rho,s)$, the derivative is evaluated at the reference state, and the approximation is justified by two assumptions: the disturbance amplitude is small enough that higher-order terms may be neglected, and the disturbance is locally isentropic so the entropy perturbation vanishes at first order. For a calorically perfect ideal gas, one may also write
$$
a_*^2=\gamma\frac{p_*}{\rho_*}=\gamma R T_*.
$$


##### problem 1.c

The relation
$$
p'=a_*^2\rho'
$$
means that, for a sufficiently small isentropic disturbance, the pressure change is proportional to the density change, with proportionality constant equal to the local compressive stiffness of the medium. A larger $a_*^2$ means that the same fractional compression produces a stronger restoring pressure response. This makes physical sense because an acoustic disturbance is precisely a rapid, weak compression and expansion of fluid elements, so the governing response should be set by the local thermodynamic law relating pressure to density along the appropriate path. That same restoring pressure response is what drives the propagation of sound waves.


##### problem 1.d

The sound speed should be viewed primarily as a material or thermodynamic property, not as a flow property. By definition,
$$
a^{2}=\left(\frac{\partial p}{\partial \rho}\right)_{s},
$$
so it is determined by the equation of state and the local thermodynamic state of the medium. For a calorically perfect ideal gas, for example,
$$
a^{2}=\gamma \frac{p}{\rho}=\gamma R T,
$$
which shows that $a$ depends on the gas state, not on the flow velocity itself. The flow speed becomes important only when compared with $a$, through the Mach number $M=|\mathbf{u}|/a$.






# Problem 2: Interpreting coupled quasi-one-dimensional forcing

##### problem 2.a
For $M<1$, both imposed drivers push the velocity in the same direction. A decrease in area acts like a converging nozzle in subsonic flow, so it accelerates the fluid. Heat addition also accelerates subsonic flow in the quasi-one-dimensional response framework. Therefore the net response is an increase in $u$.

The static pressure $p$ correspondingly decreases. Physically, in subsonic flow both convergence and heat addition drive the state toward higher speed, and that acceleration is accompanied by a drop in static pressure. Thus the two effects reinforce one another for $p$ as well, giving a net pressure decrease.

Area decrease by itself tends to reduce static temperature because part of the fluid enthalpy is converted into kinetic energy as the flow accelerates. For effect of heat addition on the static temperature, if $M<1/\sqrt{\gamma}$, heat addition raises static $T$, so the two effects compete. But if $1/\sqrt{\gamma}<M<1$, heat addition lowers static $T$ because the acceleration induced by the heating is strong enough that the kinetic-energy increase outpaces the thermal rise in the static state. Thus the net sign of the static-temperature change depends not only on the driver strengths but also on where the flow lies within the subsonic regime.

##### problem 2.b

For $M>1$, the sign rules reverse for both geometry and heat addition. A decrease in area now acts to decelerate the flow, and heat addition in supersonic flow also decelerates it. Therefore the two drivers reinforce one another and the net response is a decrease in $u$.

Because the supersonic flow is being slowed, the static pressure rises. Physically, both effects act compressively in the sense that they oppose the supersonic kinetic state and drive part of the kinetic energy back into thermodynamic state variables. Thus the net response is an increase in $p$.

The static temperature also increases. Area decrease in supersonic flow raises $T$ because deceleration converts kinetic energy into internal energy, and heat addition pushes the thermal state upward as well. So unlike the subsonic case, the two drivers reinforce one another for $T$ and produce a clear temperature increase.

##### problem 2.c

The competition is easiest to see by separating acceleration effects from thermodynamic-state effects. Geometric forcing through area decrease changes the flow by redistributing energy between bulk motion and thermodynamic state. In subsonic flow it accelerates the fluid and tends to lower static temperature, whereas in supersonic flow it decelerates the fluid and tends to raise static temperature. Heat addition, by contrast, injects energy directly into the flow and always raises the stagnation thermal state, but its effect on the static variables still depends on Mach number because the added energy can be partitioned between internal and kinetic energy in different ways.

Thus, in subsonic flow the two mechanisms always reinforce one another in velocity, but their interaction in static temperature depends on the Mach number. If $M<1/\sqrt{\gamma}$, heat addition raises static $T$, so it competes with the cooling effect of area decrease; if $1/\sqrt{\gamma}<M<1$, heat addition lowers static $T$, so both effects then push $T$ downward. In supersonic flow they reinforce one another in both velocity response and thermal-state response: both slow the flow and both raise the static temperature. Pressure follows the same broad pattern as the velocity response, decreasing when the subsonic flow is driven to higher speed and increasing when the supersonic flow is driven to lower speed.

##### problem 2.d

The net response cannot be read from any one governing equation because the unknowns are coupled. Continuity ties together density, velocity, and area. Momentum ties velocity and pressure to mechanical forcing. Energy ties velocity and temperature to heat or work input. The equation of state closes the system by relating pressure, density, and temperature. None of these equations by itself determines the sign of every response variable.

For example, heat addition does not affect only temperature. Through the energy equation it changes velocity, and through the equation of state and momentum balance that velocity change feeds back into pressure and density. Likewise area change is not just geometry because it affects the entire thermodynamic state through the coupled system. The input-output quasi-one-dimensional viewpoint is essential precisely because it treats the flow as a single interacting system, so the net local response emerges from all equations acting together rather than from isolated single-equation intuition.



# Problem 3: Linearized acoustic equations from conservation laws

##### problem 3.a
Starting from
$$
\partial_t \rho+\partial_x(\rho u)=0,
$$
substitute
$$
\rho=\rho_*+\rho', \qquad u=u_*+u'.
$$
Then
$$
\begin{aligned}
0
&=\partial_t \rho+\partial_x(\rho u) \\
&=\partial_t(\rho_*+\rho')+\partial_x\!\left[(\rho_*+\rho')(u_*+u')\right] \\
&=\partial_t\rho'+\partial_x\!\left(\rho_*u_*+\rho_*u'+u_*\rho'+\rho'u'\right) \\
&=\partial_t\rho'+\rho_*\partial_xu'+u_*\partial_x\rho'+\partial_x(\rho'u').
\end{aligned}
$$
Since $\rho'u'$ is second order in the disturbance amplitude, discard it in the linearization. Therefore the linearized continuity equation is
$$
\boxed{\partial_t\rho'+u_*\partial_x\rho'+\rho_*\partial_xu'=0.}
$$

##### problem 3.b

Starting from
$$
\partial_t(\rho u)+\partial_x(\rho u^2+p)=0,
$$
substitute
$$
\rho=\rho_*+\rho', \qquad u=u_*+u', \qquad p=p_*+p'.
$$
Then
$$
\begin{aligned}
0
&=\partial_t(\rho u)+\partial_x(\rho u^2+p) \\
&=\partial_t\!\left[(\rho_*+\rho')(u_*+u')\right]+\partial_x\!\left[(\rho_*+\rho')(u_*+u')^2+p_*+p'\right] \\
&=\partial_t\!\left(\rho_*u_*+\rho_*u'+u_*\rho'+\rho'u'\right)+\partial_x\!\left[(\rho_*+\rho')\left(u_*^2+2u_*u'+(u')^2\right)+p_*+p'\right] \\
&\approx \partial_t\!\left(\rho_*u_*+\rho_*u'+u_*\rho'\right)+\partial_x\!\left(\rho_*u_*^2+2\rho_*u_*u'+u_*^2\rho'+p'\right) \\
&=\rho_*\partial_tu'+u_*\partial_t\rho'+2\rho_*u_*\partial_xu'+u_*^2\partial_x\rho'+\partial_xp'.
\end{aligned}
$$
So the linearized momentum equation in conservative perturbation form is
$$
\boxed{\rho_*\partial_tu'+u_*\partial_t\rho'+2\rho_*u_*\partial_xu'+u_*^2\partial_x\rho'+\partial_xp'=0.}
$$
Using the linearized continuity equation from part (a),
$$
u_*\partial_t\rho'+u_*^2\partial_x\rho'+\rho_*u_*\partial_xu'=0,
$$
and subtracting this from the previous equation gives the equivalent form
$$
\boxed{\rho_*\partial_tu'+\rho_*u_*\partial_xu'+\partial_xp'=0,}
$$
or, after dividing by $\rho_*$,
$$
\boxed{\partial_tu'+u_*\partial_xu'+\frac{1}{\rho_*}\partial_xp'=0.}
$$

##### problem 3.c

For a locally isentropic disturbance, the entropy perturbation vanishes to first order, so pressure may be regarded locally as a function of density alone along that thermodynamic path. Linearizing the thermodynamic relation gives
$$
\begin{aligned}
p'
&=p-p_* \\
&\approx \left.\left(\frac{\partial p}{\partial \rho}\right)_s\right|_*(\rho-\rho_*) \\
&=\left.\left(\frac{\partial p}{\partial \rho}\right)_s\right|_*\rho' \\
&=a_*^2\rho'.
\end{aligned}
$$
Thus the closure relation is
$$
\boxed{p'=a_*^2\rho'.}
$$
This is appropriate for small acoustic disturbances because the perturbation is assumed weak enough for a first-order response to dominate and fast enough that heat transfer and irreversible entropy production do not significantly change the entropy during the disturbance.

##### problem 3.d

Substituting
$$
p'=a_*^2\rho'
$$
into the linearized momentum equation gives
$$
\partial_tu'+u_*\partial_xu'+\frac{a_*^2}{\rho_*}\partial_x\rho'=0.
$$
Together with the linearized continuity equation, the coupled perturbation system is
$$
\boxed{
\begin{aligned}
\partial_t\rho'+u_*\partial_x\rho'+\rho_*\partial_xu'&=0, \\
\partial_tu'+u_*\partial_xu'+\frac{a_*^2}{\rho_*}\partial_x\rho'&=0.
\end{aligned}}
$$
Equivalently, with
$$
\mathbf{q}'=\binom{\rho'}{u'},
$$
the system may be written as
$$
\boxed{
\partial_t\mathbf{q}'+
\begin{pmatrix}
u_* & \rho_* \\
\dfrac{a_*^2}{\rho_*} & u_*
\end{pmatrix}
\partial_x\mathbf{q}'=0.}
$$

##### problem 3.e


###### part i

This system already suggests propagating disturbances because the two perturbation variables are dynamically coupled. The continuity equation says that spatial variation of velocity creates density change, while the momentum equation says that spatial variation of pressure, and therefore density through compressibility, creates acceleration. Thus a local compression produces a restoring pressure response, and that pressure response drives motion that can in turn create new compressions and expansions elsewhere. Even before solving the equations, that feedback structure is exactly the signature of wave-like propagation.


###### part ii

Conservation of energy is not needed here because the isentropic assumption removes entropy as an independent thermodynamic variable for the disturbance. In the full compressible-flow system, pressure generally depends on more than one thermodynamic variable, so an additional thermodynamic relation is required to close the equations. Here, however, the disturbance is restricted to an isentropic path, so pressure becomes a function of density alone to first order, which gives
$$
p'=a_*^2\rho'.
$$
That closure relation supplies the missing thermodynamic link directly, so the linearized mass and momentum equations are sufficient to form a closed system for the perturbations.



# Problem 4: Steady 2D potential flow and Mach-number-dependent PDE type


##### problem 4.a
Write
$$
\boldsymbol{u}_*=\binom{u_*}{v_*}, \qquad \left|\boldsymbol{u}_*\right|=\sqrt{u_*^2+v_*^2}.
$$
Assuming $\left|\boldsymbol{u}_*\right|\neq 0$, a unit vector parallel to $\boldsymbol{u}_*$ is
$$
\boxed{\boldsymbol{e}_{\parallel}=\frac{\boldsymbol{u}_*}{|\boldsymbol{u}_*|}=\frac{1}{\sqrt{u_*^2+v_*^2}}\binom{u_*}{v_*}.}
$$
A unit vector perpendicular to $\boldsymbol{u}_*$ is
$$
\boxed{\boldsymbol{e}_{\perp}=\frac{1}{\sqrt{u_*^2+v_*^2}}\binom{-v_*}{u_*}.}
$$
These are orthonormal because
$$
\boldsymbol{e}_{\parallel}\cdot\boldsymbol{e}_{\parallel}=1, \qquad
\boldsymbol{e}_{\perp}\cdot\boldsymbol{e}_{\perp}=1, \qquad
\boldsymbol{e}_{\parallel}\cdot\boldsymbol{e}_{\perp}=0.
$$
If $\boldsymbol{u}_*=\mathbf{0}$, then the matrix is already $a_*^2I$, so any orthonormal basis may be used.

##### problem 4.b

Using
$$
\mathbf{K}_{2D}=a_*^2 I-\boldsymbol{u}_*\boldsymbol{u}_*^T,
$$
act on the parallel direction:
$$
\begin{aligned}
\mathbf{K}_{2D}\boldsymbol{e}_{\parallel}
&=\left(a_*^2 I-\boldsymbol{u}_*\boldsymbol{u}_*^T\right)\boldsymbol{e}_{\parallel} \\
&=a_*^2\boldsymbol{e}_{\parallel}-\boldsymbol{u}_*\left(\boldsymbol{u}_*^T\boldsymbol{e}_{\parallel}\right) \\
&=a_*^2\boldsymbol{e}_{\parallel}-\left|\boldsymbol{u}_*\right|\boldsymbol{u}_* \\
&=a_*^2\boldsymbol{e}_{\parallel}-\left|\boldsymbol{u}_*\right|^2\boldsymbol{e}_{\parallel} \\
&=\left(a_*^2-\left|\boldsymbol{u}_*\right|^2\right)\boldsymbol{e}_{\parallel}.
\end{aligned}
$$
So
$$
\boxed{\lambda_{\parallel}=a_*^2-\left|\boldsymbol{u}_*\right|^2.}
$$
Now act on the perpendicular direction:
$$
\begin{aligned}
\mathbf{K}_{2D}\boldsymbol{e}_{\perp}
&=\left(a_*^2 I-\boldsymbol{u}_*\boldsymbol{u}_*^T\right)\boldsymbol{e}_{\perp} \\
&=a_*^2\boldsymbol{e}_{\perp}-\boldsymbol{u}_*\left(\boldsymbol{u}_*^T\boldsymbol{e}_{\perp}\right) \\
&=a_*^2\boldsymbol{e}_{\perp}-\boldsymbol{u}_*(0) \\
&=a_*^2\boldsymbol{e}_{\perp}.
\end{aligned}
$$
So
$$
\boxed{\lambda_{\perp}=a_*^2.}
$$
Since
$$
M_*=\frac{|\boldsymbol{u}_*|}{a_*},
$$
these may also be written as
$$
\boxed{\lambda_{\parallel}=a_*^2(1-M_*^2), \qquad \lambda_{\perp}=a_*^2.}
$$

##### problem 4.c

Choose the rotated coordinates so that $\xi'$ is aligned with $\boldsymbol{e}_{\parallel}$ and $\zeta'$ is aligned with $\boldsymbol{e}_{\perp}$. Then the principal part becomes
$$
\lambda_{\parallel}\phi_{\xi'\xi'}+\lambda_{\perp}\phi_{\zeta'\zeta'}=0.
$$
Substituting the eigenvalues gives
$$
a_*^2(1-M_*^2)\phi_{\xi'\xi'}+a_*^2\phi_{\zeta'\zeta'}=0.
$$
Since $a_*^2>0$, divide through by $a_*^2$:
$$
(1-M_*^2)\phi_{\xi'\xi'}+\phi_{\zeta'\zeta'}=0.
$$

If $M_*<1$, then $1-M_*^2>0$, so both coefficients have the same sign. The equation is elliptic, and up to an overall nonzero scaling its canonical principal part is
$$
\boxed{(1-M_*^2)\phi_{\xi'\xi'}+\phi_{\zeta'\zeta'}=0.}
$$

If $M_*=1$, then $1-M_*^2=0$, so one second-derivative direction drops out. The equation is parabolic, and with the present coordinate choice the principal part is
$$
\boxed{\phi_{\zeta'\zeta'}=0.}
$$

If $M_*>1$, then $1-M_*^2<0$, so the two coefficients have opposite signs. The equation is hyperbolic, and up to an overall nonzero scaling its canonical principal part is
$$
\boxed{-(M_*^2-1)\phi_{\xi'\xi'}+\phi_{\zeta'\zeta'}=0.}
$$

##### problem 4.d


![[Pasted image 20260407082427.png|700]]


# Problem 5: Synthesis and interpretation

##### problem 5.a
In the incompressible limit, the steady two-dimensional compressible potential equation reduces to Laplace's equation,
$$
\phi_{xx}+\phi_{yy}=0.
$$
This should be interpreted as the limiting case of the subsonic regime in which the Mach number becomes very small. For all $M_*<1$, the steady equation is elliptic, and the incompressible limit is simply the special case where the compressibility correction disappears completely. Thus incompressible potential flow sits inside the elliptic, subsonic branch as its limiting form.

##### problem 5.b

The unsteady one-dimensional compressible potential equation is always hyperbolic because its principal coefficient matrix always has one positive eigenvalue and one negative eigenvalue as long as $a_*>0$. Physically, this means the system always supports finite-speed wave propagation rather than instantaneous global adjustment. In one-dimensional compressible flow, the essential mechanism is the coupling between compression and restoring pressure response, which naturally creates traveling disturbances. Those disturbances move at the acoustic speeds relative to the fluid, so in the laboratory frame the two wave families travel with speeds $u_*+a_*$ and $u_*-a_*$.
