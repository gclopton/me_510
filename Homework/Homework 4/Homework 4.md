



# Problem 1


##### problem a.i

Let
$$
\beta=\sqrt{1-M_\infty^2},
\qquad M_\infty<1.
$$
Then the PDE becomes
$$
\beta^2\phi_{xx}+\phi_{yy}=0.
$$

For one wall mode
$$
f_k(x)=\sin(kx),
\qquad
f_k'(x)=k\cos(kx),
$$
seek a decaying separated solution of the form
$$
\phi_k(x,y)=A_k e^{-\beta k y}\cos(kx).
$$
Then
$$
\phi_{k,xx}=-k^2A_k e^{-\beta k y}\cos(kx),
\qquad
\phi_{k,yy}=\beta^2k^2A_k e^{-\beta k y}\cos(kx),
$$
so
$$
\beta^2\phi_{k,xx}+\phi_{k,yy}
=
\beta^2\left(-k^2A_k e^{-\beta k y}\cos(kx)\right)
+
\beta^2k^2A_k e^{-\beta k y}\cos(kx)
=
0.
$$
The boundary condition gives
$$
\phi_{k,y}(x,0)
=
-\beta k A_k\cos(kx)
=
U_\infty k\cos(kx),
$$
hence
$$
A_k=-\frac{U_\infty}{\beta}.
$$
Therefore
$$
\phi_k(x,y)=-\frac{U_\infty}{\beta}e^{-\beta k y}\cos(kx).
$$

Since
$$
f(x)=\sin x+\sin 3x+\sin 6x,
$$
the subsonic solution is
$$
\phi_{\text{sub}}(x,y)
=
-\frac{U_\infty}{\beta}
\left(
e^{-\beta y}\cos x
+
e^{-3\beta y}\cos 3x
+
e^{-6\beta y}\cos 6x
\right).
$$


##### problem a.ii

Let
$$
\mu=\sqrt{M_\infty^2-1},
\qquad M_\infty>1.
$$
Then the PDE is
$$
\phi_{yy}-\mu^2\phi_{xx}=0.
$$
Equivalently, with $\eta=\mu y$,
$$
\phi_{\eta\eta}-\phi_{xx}=0.
$$
So the characteristic form is
$$
\phi(x,y)=F(x+\mu y)+G(x-\mu y).
$$
Keeping the downstream-propagating family gives
$$
\phi(x,y)=G(x-\mu y).
$$
Then
$$
\phi_y(x,y)
=
G'(x-\mu y)(-\mu),
$$
so at $y=0$,
$$
\phi_y(x,0)
=
-\mu G'(x)
=
U_\infty f'(x).
$$
Thus
$$
G'(x)=-\frac{U_\infty}{\mu}f'(x),
$$
and we have
$$
G(x)=-\frac{U_\infty}{\mu}f(x)
$$
up to an irrelevant additive constant. Thus
$$
\phi_{\text{sup}}(x,y)
=
-\frac{U_\infty}{\mu}f(x-\mu y).
$$
Since
$$
f(x)=\sin x+\sin 3x+\sin 6x,
$$
the supersonic solution is
$$
\phi_{\text{sup}}(x,y)
=
-\frac{U_\infty}{\mu}
\left[
\sin(x-\mu y)
+
\sin\!\bigl(3(x-\mu y)\bigr)
+
\sin\!\bigl(6(x-\mu y)\bigr)
\right].
$$




> [!warning] Lecture convention mistake
> ChatGPT's diagnosis that $\mu$ should mean the Mach angle is not correct for Lecture 14. In the wavy-wall lecture used for this homework, the lecture explicitly defines
> $$
> \mu=\sqrt{M_\infty^2-1}.
> $$
> With that Lecture 14 definition, the submitted form
> $$
> \phi_{\text{sup}}(x,y)=-\frac{U_\infty}{\mu}f(x-\mu y)
> $$
> satisfies the PDE and the wall boundary condition, and it matches Lecture 14, Eq. (3.10). The only potential ambiguity is that $\mu$ is an overloaded symbol in compressible flow. In later characteristic-flow notation, $\mu$ is often used for the Mach angle, where
> $$
> \sin\mu_{\text{Mach}}=\frac{1}{M_\infty},
> \qquad
> \tan\mu_{\text{Mach}}=\frac{1}{\sqrt{M_\infty^2-1}},
> $$
> but that is not the $\mu$ used in Lecture 14 for this problem. If the grader or rubric reserves $\mu$ for the Mach angle, the same answer should be rewritten with a non-conflicting symbol such as
> $$
> \beta_s=\sqrt{M_\infty^2-1},
> $$
> giving
> $$
> \phi_{\text{sup}}(x,y)=-\frac{U_\infty}{\beta_s}f(x-\beta_s y).
> $$
> For this wall shape, the lecture-consistent answer is therefore
> $$
> \phi_{\text{sup}}(x,y)
> =
> -\frac{U_\infty}{\mu}
> \left[
> \sin(x-\mu y)
> +
> \sin\!\left(3(x-\mu y)\right)
> +
> \sin\!\left(6(x-\mu y)\right)
> \right].
> $$
> Going forward, match the lecture's definitions, symbols, and characteristic variables exactly, and explicitly restate any overloaded symbol before using it in a final boxed answer.



##### problem b

For the specified numerical values
$$
M_{\text{sub}}=0.6,
\qquad
M_{\text{sup}}=2.0,
\qquad
U_\infty=1,
$$
we have
$$
\beta=\sqrt{1-0.6^2}=0.8=\frac45,
\qquad
\mu=\sqrt{2^2-1}=\sqrt3.
$$
So the explicit fields are
$$
\phi_{\text{sub}}(x,y)
=
-\frac54
\left(
e^{-0.8y}\cos x
+
e^{-2.4y}\cos 3x
+
e^{-4.8y}\cos 6x
\right),
$$
and
$$
\phi_{\text{sup}}(x,y)
=
-\frac{1}{\sqrt3}
\left[
\sin(x-\sqrt3\,y)
+
\sin\!\bigl(3x-3\sqrt3\,y\bigr)
+
\sin\!\bigl(6x-6\sqrt3\,y\bigr)
\right].
$$

The subsonic field is a superposition of three exponentially decaying modes. The $k=6$ mode decays fastest, the $k=3$ mode decays next, and the $k=1$ mode persists farthest into the domain. The supersonic field is instead a translated copy of the wall signal, carried along the characteristic direction $x-\sqrt3\,y=\text{const}$.



![[Pasted image 20260421095120.png|800]]




```mathematica
Clear["Global`*"];

Msub = 0.6;
Msup = 2.0;
Uinf = 1.0;

beta = Sqrt[1 - Msub^2];
mu = Sqrt[Msup^2 - 1];

f[x_] := Sin[x] + Sin[3 x] + Sin[6 x];

phiSub1[x_, y_] := -(Uinf/beta) Exp[-beta y] Cos[x];
phiSub3[x_, y_] := -(Uinf/beta) Exp[-3 beta y] Cos[3 x];
phiSub6[x_, y_] := -(Uinf/beta) Exp[-6 beta y] Cos[6 x];
phiSub[x_, y_] := phiSub1[x, y] + phiSub3[x, y] + phiSub6[x, y];

phiSup1[x_, y_] := -(Uinf/mu) Sin[x - mu y];
phiSup3[x_, y_] := -(Uinf/mu) Sin[3 (x - mu y)];
phiSup6[x_, y_] := -(Uinf/mu) Sin[6 (x - mu y)];
phiSup[x_, y_] := phiSup1[x, y] + phiSup3[x, y] + phiSup6[x, y];

xmin = 0;
xmax = 2 Pi;
ymin = 0;
ymax = 2;

xGrid = Subdivide[xmin, xmax, 300];
yGrid = Subdivide[ymin, ymax, 200];

subVals = Flatten@Table[phiSub[x, y], {x, xGrid}, {y, yGrid}];
supVals = Flatten@Table[phiSup[x, y], {x, xGrid}, {y, yGrid}];
commonRange = {Min[Join[subVals, supVals]], Max[Join[subVals, supVals]]};

subPlot =
  ContourPlot[
    phiSub[x, y],
    {x, xmin, xmax}, {y, ymin, ymax},
    Contours -> 25,
    PlotRange -> commonRange,
    ColorFunction -> "SunsetColors",
    PlotLegends -> Automatic,
    FrameLabel -> {"x", "y"},
    PlotLabel -> "Subsonic Potential"
  ];

supPlot =
  ContourPlot[
    phiSup[x, y],
    {x, xmin, xmax}, {y, ymin, ymax},
    Contours -> 25,
    PlotRange -> commonRange,
    ColorFunction -> "SunsetColors",
    PlotLegends -> Automatic,
    FrameLabel -> {"x", "y"},
    PlotLabel -> "Supersonic Potential"
  ];

GraphicsRow[{subPlot, supPlot}, ImageSize -> Large]
```


##### problem c.i

In the subsonic case, the influence of the wall geometry decays with distance from the wall. The explicit solution is
$$
\phi_{\text{sub}}(x,y)
=
-\frac{U_\infty}{\beta}
\left(
e^{-\beta y}\cos x
+
e^{-3\beta y}\cos 3x
+
e^{-6\beta y}\cos 6x
\right),
\qquad
\beta=\sqrt{1-M_\infty^2}.
$$
Each horizontal wavenumber remains present in the solution, but its amplitude is multiplied by an exponential decay factor in $y$.

The key point is that the higher-wavenumber components decay faster. The $k=6$ contribution carries the factor $e^{-6\beta y}$, the $k=3$ contribution carries $e^{-3\beta y}$, and the $k=1$ contribution carries $e^{-\beta y}$. Near the wall, all three modes are visible, so the plot shows finer-scale structure. Farther from the wall, the short-wavelength oscillations diminish first, then the intermediate wavelength weakens, and the longest wavelength persists the farthest. This is exactly what the contour plot shows: the field becomes smoother with increasing $y$, and the large-scale variation dominates in the far field.


##### problem c.ii

In the supersonic case, the disturbance does not fill the domain in the same diffuse way as the subsonic field. Instead, it organizes along specific straight directions. The explicit solution is
$$
\phi_{\text{sup}}(x,y)
=
-\frac{U_\infty}{\mu}f(x-\mu y),
\qquad
\mu=\sqrt{M_\infty^2-1}.
$$
Therefore the phase is constant when
$$
x-\mu y=\text{const}.
$$

These are straight characteristic lines. Solving for $y$ gives
$$
y=\frac{x-\text{const}}{\mu},
$$
so their slope in the $(x,y)$ plane is
$$
\frac{dy}{dx}=\frac{1}{\mu}.
$$
For $M_\infty=2$, we have $\mu=\sqrt{3}$, so
$$
\frac{dy}{dx}=\frac{1}{\sqrt{3}}\approx 0.577.
$$
This agrees with the diagonal band structure in the contour plot. The wall signal is carried into the domain along these characteristic directions rather than decaying away from the wall.


##### problem c.iii

Choose, for example,
$$
y_1=0.1,
\qquad
y_2=0.5,
\qquad
y_3=1.5.
$$
These heights span the near-wall region, an intermediate height, and a far-field height within the plotted domain.

For the subsonic field, define
$$
\phi_1(x,y)=-\frac{U_\infty}{\beta}e^{-\beta y}\cos x,
\qquad
\phi_3(x,y)=-\frac{U_\infty}{\beta}e^{-3\beta y}\cos 3x,
\qquad
\phi_6(x,y)=-\frac{U_\infty}{\beta}e^{-6\beta y}\cos 6x.
$$
Since the norm of each cosine mode over one full period is the same up to its amplitude, the relative contribution is controlled by
$$
e^{-\beta y},\qquad e^{-3\beta y},\qquad e^{-6\beta y}.
$$
With $\beta=0.8$, this gives the approximate subsonic contributions



| $y$ | Contribution $_1$ | Contribution $_3$ | Contribution $_6$ |
| :-- | :---------------- | :---------------- | :---------------- |
| 0.1 | 0.678             | 0.578             | 0.454             |
| 0.5 | 0.905             | 0.407             | 0.123             |
| 1.5 | 0.996             | 0.090             | 0.002             |


So near the wall, all three modes contribute, although $k=1$ is already the largest. By intermediate height, the $k=1$ mode clearly dominates, the $k=3$ mode is secondary, and the $k=6$ mode is small. Far from the wall, the $k=1$ mode overwhelmingly dominates. This happens because the decay rate increases linearly with wavenumber.

For the supersonic field, define
$$
\phi_1(x,y)=-\frac{U_\infty}{\mu}\sin(x-\mu y),
\qquad
\phi_3(x,y)=-\frac{U_\infty}{\mu}\sin\!\bigl(3(x-\mu y)\bigr),
\qquad
\phi_6(x,y)=-\frac{U_\infty}{\mu}\sin\!\bigl(6(x-\mu y)\bigr).
$$
Here there is no exponential decay factor in $y$. Each mode is simply translated in phase as $y$ changes. Therefore the modal contributions do not systematically decrease with height. Over one full period in $x$, each mode has the same norm at every $y$, so the contribution pattern remains essentially unchanged as the disturbance propagates along the characteristic lines.






# Problem 2





##### problem 2.a

Let the wall be parameterized by
$$
\boldsymbol{r}(x)=\bigl(x,\varepsilon f(x)\bigr).
$$
Then
$$
\boldsymbol{r}'(x)=\bigl(1,\varepsilon f'(x)\bigr),
$$
so
$$
ds=\sqrt{1+\varepsilon^2\left(f'(x)\right)^2}\,dx.
$$
Choose the unit normal as
$$
\boldsymbol{n}
=
\frac{\bigl(-\varepsilon f'(x),\,1\bigr)}{\sqrt{1+\varepsilon^2\left(f'(x)\right)^2}},
$$
so that
$$
n_x=-\frac{\varepsilon f'(x)}{\sqrt{1+\varepsilon^2\left(f'(x)\right)^2}}.
$$
Therefore
$$
n_x\,ds
=
-\frac{\varepsilon f'(x)}{\sqrt{1+\varepsilon^2\left(f'(x)\right)^2}}
\sqrt{1+\varepsilon^2\left(f'(x)\right)^2}\,dx
=
-\varepsilon f'(x)\,dx.
$$

Substitute this into the drag expression:
$$
\begin{aligned}
D
&=
\int_{\text{wall}} (p-p_\infty)n_x\,ds\\
&=
\int (p-p_\infty)\bigl(x,\varepsilon f(x)\bigr)\,\bigl(-\varepsilon f'(x)\bigr)\,dx.
\end{aligned}
$$
Now use
$$
C_p=\frac{p-p_\infty}{\frac12\rho_\infty U_\infty^2},
\qquad
p-p_\infty=\frac12\rho_\infty U_\infty^2\,C_p.
$$
Then
$$
\begin{aligned}
D
&=
\frac12\rho_\infty U_\infty^2
\int
C_p\bigl(x,\varepsilon f(x)\bigr)\,\bigl(-\varepsilon f'(x)\bigr)\,dx\\
&\sim
\int
C_p\bigl(x,\varepsilon f(x)\bigr)\,\bigl(-f'(x)\bigr)\,dx,
\end{aligned}
$$
where the omitted overall prefactor includes the constant $\frac12\rho_\infty U_\infty^2\varepsilon$. Thus, up to an overall constant prefactor, the drag has the required form.


##### problem 2.b

Expand the pressure coefficient about the reference line $y=0$:
$$
\begin{aligned}
C_p\bigl(x,\varepsilon f(x)\bigr)
&=
C_p(x,0)
+
\varepsilon f(x)\,C_{p,y}(x,0)
+
O(\varepsilon^2).
\end{aligned}
$$
Since $\varepsilon f(x)=O(\varepsilon)$, this may be written more compactly as
$$
C_p\bigl(x,\varepsilon f(x)\bigr)=C_p(x,0)+O(\varepsilon).
$$

Now substitute this into the drag formula from part (a):
$$
\begin{aligned}
D
&\sim
\int
\left[
C_p(x,0)+O(\varepsilon)
\right]
\bigl(-f'(x)\bigr)\,dx.
\end{aligned}
$$
But the overall prefactor from part (a) already contains one factor of $\varepsilon$, so the leading term in the drag is $O(\varepsilon)$ times
$$
\int C_p(x,0)\bigl(-f'(x)\bigr)\,dx,
$$
while the correction coming from the $O(\varepsilon)$ term in $C_p$ contributes only at the next order. Therefore, to obtain the leading-order drag, it is sufficient to replace $C_p(x,\varepsilon f(x))$ by $C_p(x,0)$.


##### problem 2.c

For the subsonic solution from Problem 1,
$$
\phi_{\text{sub}}(x,y)
=
-\frac{U_\infty}{\beta}
\left(
e^{-\beta y}\cos x
+
e^{-3\beta y}\cos 3x
+
e^{-6\beta y}\cos 6x
\right),
\qquad
\beta=\sqrt{1-M_\infty^2}.
$$
At the wall reference line $y=0$,
$$
\phi_{\text{sub}}(x,0)
=
-\frac{U_\infty}{\beta}\left(\cos x+\cos 3x+\cos 6x\right).
$$
Differentiate:
$$
\phi_{\text{sub},x}(x,0)
=
\frac{U_\infty}{\beta}\left(\sin x+3\sin 3x+6\sin 6x\right).
$$
Hence
$$
C_p(x,0)
=
-\frac{2}{U_\infty}\phi_x(x,0)
=
-\frac{2}{\beta}\left(\sin x+3\sin 3x+6\sin 6x\right).
$$

The leading-order drag is therefore
$$
\begin{aligned}
D
&\sim
\int_0^{2\pi} C_p(x,0)\bigl(-f'(x)\bigr)\,dx\\
&=
\frac{2}{\beta}
\int_0^{2\pi}
\left(\sin x+3\sin 3x+6\sin 6x\right)
\left(\cos x+3\cos 3x+6\cos 6x\right)\,dx.
\end{aligned}
$$
Every term in this integral is of the form
$$
\int_0^{2\pi}\sin(mx)\cos(nx)\,dx,
$$
which is zero over a full period for all integers $m,n$. Hence
$$
D\sim 0.
$$
So the leading-order subsonic drag is zero.


##### problem 2.d

For the supersonic solution from Problem 1,
$$
\phi_{\text{sup}}(x,y)
=
-\frac{U_\infty}{\mu}f(x-\mu y),
\qquad
\mu=\sqrt{M_\infty^2-1}.
$$
Then
$$
\phi_{\text{sup},x}(x,y)
=
-\frac{U_\infty}{\mu}f'(x-\mu y),
$$
so at $y=0$,
$$
\phi_{\text{sup},x}(x,0)
=
-\frac{U_\infty}{\mu}f'(x).
$$
Therefore
$$
C_p(x,0)
=
-\frac{2}{U_\infty}\phi_x(x,0)
=
\frac{2}{\mu}f'(x).
$$

Substitute into the leading-order drag:
$$
\begin{aligned}
D
&\sim
\int_0^{2\pi} C_p(x,0)\bigl(-f'(x)\bigr)\,dx\\
&=
-\frac{2}{\mu}\int_0^{2\pi}\left(f'(x)\right)^2\,dx.
\end{aligned}
$$
Thus the drag is nonzero. The sign depends on the chosen normal-direction convention, but its magnitude is proportional to
$$
\int_0^{2\pi}\left(f'(x)\right)^2\,dx>0.
$$

For the present wall,
$$
f'(x)=\cos x+3\cos 3x+6\cos 6x.
$$
Hence
$$
\begin{aligned}
\int_0^{2\pi}\left(f'(x)\right)^2\,dx
&=
\int_0^{2\pi}
\left(\cos x+3\cos 3x+6\cos 6x\right)^2
dx\\
&=
\int_0^{2\pi}\cos^2x\,dx
+
9\int_0^{2\pi}\cos^2(3x)\,dx
+
36\int_0^{2\pi}\cos^2(6x)\,dx\\
&=
\pi+9\pi+36\pi\\
&=
46\pi,
\end{aligned}
$$
since all cross terms vanish by orthogonality. Therefore
$$
D\sim -\frac{92\pi}{\mu},
$$
up to the overall constant prefactor from part (a). The essential conclusion is that the supersonic drag is nonzero.


##### problem 2.e

In the subsonic case, the governing equation is elliptic, so the disturbance is coupled globally to the wall geometry. That global coupling produces a pressure distribution that is tied to the wall shape itself, and the resulting streamwise pressure contributions cancel over one full period, giving zero leading-order drag. In the supersonic case, the governing equation is hyperbolic, so the disturbance propagates along characteristic directions rather than being globally smoothed. The pressure is then tied to the wall slope instead of the wall displacement, so the drag integral becomes proportional to $\int (f')^2\,dx$, which does not cancel. That is why elliptic structure gives zero leading-order drag here, while hyperbolic structure gives nonzero wave drag.





# Problem 3


##### problem 3.a

The flow must be divided into an upstream region, a shock surface, and a downstream region because the mathematical character of the solution is different in those three places. Upstream of the shock, the state is known: the freestream is uniform, so there is nothing to solve there. At the shock, the flow variables jump discontinuously, so the state cannot be described pointwise by the differential form of the equations. Downstream of the shock, the flow is smooth again, but now unknown, so the differential equations must be solved there subject to the data transmitted through the shock.

The non-conservative differential equations are not valid at the shock because they assume differentiability of the flow variables, while the shock introduces finite jumps over an infinitesimally thin layer. The conservative laws remain valid in an integral sense: if one surrounds the shock by a thin control volume and applies conservation of mass, momentum, and energy to that control volume, the jump conditions follow in the thin-limit. Thus the shock is governed by the integral conservation laws, while the smooth downstream region is governed by the differential equations.


##### problem 3.b

In the wedge problem, the flow downstream of the shock is uniform. The shock turns the incoming flow by exactly the required amount, and the condition that the downstream velocity be tangent to the wedge is enforced immediately behind the shock. Because of that, the shock angle is determined directly from an algebraic relation between the upstream Mach number, the shock angle, and the flow deflection angle.

The cone problem is different because the downstream flow is not uniform. Even after the shock, the flow occupies a whole region between the shock and the cone surface and continues to adjust as a function of position. In particular, the post-shock state does not generally satisfy the cone boundary condition immediately, so one must solve an ODE system that describes how the flow evolves from the shock to the cone surface. The extra geometric freedom of axisymmetric flow is exactly what makes the cone problem a downstream-evolution problem rather than a purely algebraic one.


##### problem 3.c

The jump conditions provide the downstream state immediately behind the shock once the upstream state and the shock orientation are known. More concretely, they determine the downstream pressure, density, and the velocity components normal and tangential to the shock. In that sense, they tell us how the known upstream flow is converted into the initial post-shock state.

However, they do not determine the full downstream flow because they act only locally at the shock. The cone-flow problem still has an entire smooth region between $\theta=\theta_s$ and $\theta=\theta_c$, and the flow in that region must evolve so that the cone-surface condition
$$
u_\theta(\theta_c)=0
$$
is satisfied. The jump conditions give the initial data at the shock, but they do not supply the evolution law through the downstream region. That is why a differential system is still needed.


##### problem 3.d

Conical similarity assumes that the downstream flow is invariant along rays from the cone apex, so the unknowns depend only on the polar angle $\theta$:
$$
u_r=u_r(\theta),
\qquad
u_\theta=u_\theta(\theta),
\qquad
p=p(\theta),
\qquad
\rho=\rho(\theta).
$$
This means that all derivatives with respect to the radial coordinate vanish:
$$
\frac{\partial(\cdot)}{\partial r}=0.
$$

Starting from the steady spherical-coordinate equations, this removes the radial dependence and leaves only $\theta$-derivatives. The continuity and momentum equations therefore reduce from PDEs in $(r,\theta)$ to ODEs in $\theta$. After eliminating $p$ and $\rho$ using the thermodynamic relations and Bernoulli relation, the final Taylor-Maccoll system is
$$
\frac{du_r}{d\theta}=u_\theta,
$$
$$
\frac{du_\theta}{d\theta}
=
\frac{u_ru_\theta^2-a^2\left(2u_r+u_\theta\cot\theta\right)}{a^2-u_\theta^2},
$$
with
$$
a^2=(\gamma-1)\left[h_0-\frac12\left(u_r^2+u_\theta^2\right)\right].
$$
So conical similarity reduces the downstream cone-flow problem to an ODE system in the single variable $\theta$.


##### problem 3.e

The shock angle is determined by an iterative shooting procedure. The key idea is that for each trial value of $\theta_s$, the jump conditions determine a post-shock state, and that post-shock state becomes the initial condition for the Taylor-Maccoll ODE. One then integrates the ODE from the shock inward to the cone surface and checks whether the cone boundary condition is satisfied.

A clean algorithm is:

1. Choose a trial shock angle $\theta_s$.
2. Use the jump conditions to compute the downstream normal and tangential velocity components immediately behind the shock.
3. Convert those components into the spherical variables $u_r(\theta_s)$ and $u_\theta(\theta_s)$.
4. Integrate the Taylor-Maccoll system from $\theta=\theta_s$ down to $\theta=\theta_c$.
5. Evaluate the residual
   $$
   R(\theta_s)=u_\theta(\theta_c).
   $$
6. If $R(\theta_s)=0$ within tolerance, the correct shock angle has been found.
7. Otherwise, update $\theta_s$ using a root-finding method such as bisection and repeat.

The role of the initial guess is to start the root-finding process for $\theta_s$. The downstream solution is computed by integrating the ODE from the shock to the cone. The boundary condition at the cone surface is enforced indirectly by driving the residual $u_\theta(\theta_c)$ to zero. In this way, the shock angle is not prescribed in advance but selected as part of the solution.




# Problem 4


##### problem 4.a

First compute the freestream thermodynamic quantities from the given nondimensional data:
$$
a_\infty^2=\gamma R T_\infty
\quad\Longrightarrow\quad
T_\infty=\frac{a_\infty^2}{\gamma R}
=
\frac{1}{1.4}
=
\frac{5}{7},
$$
$$
\rho_\infty=\frac{p_\infty}{R T_\infty}
=
\frac{1}{1\cdot(5/7)}
=
\frac{7}{5}
=
1.4,
$$
and
$$
U_\infty=M_\infty a_\infty=2.5.
$$
Also,
$$
c_p=\frac{\gamma}{\gamma-1}R=\frac{1.4}{0.4}=3.5,
$$
so the stagnation enthalpy is
$$
h_0=c_pT_\infty+\frac{U_\infty^2}{2}
=
3.5\cdot\frac{5}{7}+\frac{(2.5)^2}{2}
=
2.5+3.125
=
5.625.
$$

The downstream cone flow is then found by combining the shock jump conditions with the Taylor-Maccoll system
$$
\frac{du_r}{d\theta}=u_\theta,
$$
$$
\frac{du_\theta}{d\theta}
=
\frac{u_ru_\theta^2-a^2\left(2u_r+u_\theta\cot\theta\right)}{a^2-u_\theta^2},
$$
$$
a^2=(\gamma-1)\left[h_0-\frac12\left(u_r^2+u_\theta^2\right)\right].
$$
For each trial shock angle $\theta_s$, the oblique-shock relations determine the immediate post-shock state, and that state is used as the initial condition at $\theta=\theta_s$. The correct shock angle is the one for which the integrated solution satisfies
$$
u_\theta(\theta_c)=0
\qquad\text{at}\qquad
\theta_c=10^\circ.
$$

Using this procedure gives
$$
\theta_s \approx 25.288^\circ.
$$
At the shock, the numerical solution starts from approximately
$$
u_r(\theta_s)\approx 2.2604,
\qquad
u_\theta(\theta_s)\approx -0.9583,
\qquad
p(\theta_s)\approx 1.1643.
$$
At the cone surface, the solution reaches
$$
u_r(\theta_c)\approx 2.3941,
\qquad
u_\theta(\theta_c)\approx 0,
\qquad
p(\theta_c)\approx 1.4124.
$$



```python
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

gamma = 1.4
R = 1.0
a_inf = 1.0
p_inf = 1.0
M_inf = 2.5
theta_c_deg = 10.0
theta_c = math.radians(theta_c_deg)

u_inf = M_inf * a_inf
T_inf = a_inf**2 / (gamma * R)
rho_inf = p_inf / (R * T_inf)
cp = gamma / (gamma - 1) * R
h0 = cp * T_inf + 0.5 * u_inf**2

def post_shock(theta_s):
    un1 = u_inf * math.sin(theta_s)
    ut1 = u_inf * math.cos(theta_s)
    Mn1 = un1 / a_inf

    rho2_rho1 = ((gamma + 1) * Mn1**2) / ((gamma - 1) * Mn1**2 + 2)
    p2_p1 = 1 + (2 * gamma / (gamma + 1)) * (Mn1**2 - 1)
    T2_T1 = p2_p1 / rho2_rho1
    a2 = a_inf * math.sqrt(T2_T1)

    Mn2_sq = (1 + 0.5 * (gamma - 1) * Mn1**2) / (gamma * Mn1**2 - 0.5 * (gamma - 1))
    Mn2 = math.sqrt(Mn2_sq)

    un2 = Mn2 * a2
    ut2 = ut1

    ur0 = ut2
    uth0 = -un2
    return ur0, uth0

def rhs(theta, y):
    ur, uth = y
    a2 = (gamma - 1) * (h0 - 0.5 * (ur**2 + uth**2))
    dur = uth
    duth = (ur * uth**2 - a2 * (2 * ur + uth / math.tan(theta))) / (a2 - uth**2)
    return [dur, duth]

def integrate(theta_s):
    ur0, uth0 = post_shock(theta_s)
    return solve_ivp(
        rhs,
        (theta_s, theta_c),
        [ur0, uth0],
        rtol=1e-10,
        atol=1e-12,
        max_step=1e-3
    )

def residual(theta_s):
    sol = integrate(theta_s)
    return sol.y[1, -1]

theta_s = brentq(
    residual,
    math.radians(25.2),
    math.radians(25.3),
    xtol=1e-14,
    rtol=1e-12
)

sol = integrate(theta_s)
theta_deg = np.degrees(sol.t)
ur = sol.y[0]
uth = sol.y[1]
a2 = (gamma - 1) * (h0 - 0.5 * (ur**2 + uth**2))
T = a2 / (gamma * R)
p = p_inf * (T / T_inf)**(gamma / (gamma - 1))

print(f"theta_s = {math.degrees(theta_s):.12f} deg")

plt.figure(figsize=(8, 4.8))
plt.plot(theta_deg, ur, label=r"$u_r(\theta)$", linewidth=2)
plt.plot(theta_deg, uth, label=r"$u_\theta(\theta)$", linewidth=2)
plt.plot(theta_deg, p, label=r"$p(\theta)$", linewidth=2)
plt.xlabel(r"$\theta$ (deg)")
plt.ylabel("value")
plt.title("Supersonic Cone-Flow Solution")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("/Users/gradyclopton/ObsidianVaults/me_510/Homework/Homework 4/images/problem4_cone_solution.png", dpi=200)
plt.show()
```




![[images/problem4_cone_solution.png|800]]


##### problem 4.b.i

The flow begins at the shock with a nonzero inward polar velocity component, so the post-shock state is not yet tangent to the cone. As the solution is integrated from $\theta=\theta_s$ down to $\theta=\theta_c$, the Taylor-Maccoll system continuously adjusts the velocity components. In the computed solution, $u_\theta$ rises from a negative value at the shock to essentially zero at the cone, while $u_r$ increases slightly. Over the same interval, the pressure increases from about $1.164$ just behind the shock to about $1.412$ at the cone surface.


##### problem 4.b.ii

The cone boundary condition is not satisfied immediately behind the shock because the shock relations only enforce conservation across the shock, not tangency to the cone surface. The jump conditions determine the local post-shock state once the shock angle is chosen, but that state generally still has
$$
u_\theta(\theta_s)\neq 0.
$$
For the present case, the computed post-shock value is approximately $u_\theta(\theta_s)\approx -0.958$, so the flow is still turning after it passes through the shock. The downstream ODE is needed to carry that state to the cone surface and complete the adjustment.


##### problem 4.b.iii

The ODE supplies the downstream evolution law that the jump conditions alone do not provide. The jump conditions determine only the state immediately behind the shock, which is local information at $\theta=\theta_s$. The Taylor-Maccoll system then propagates that state through the whole region
$$
\theta_c\leq \theta\leq \theta_s
$$
and tells us whether the resulting solution reaches the cone with
$$
u_\theta(\theta_c)=0.
$$
Without the ODE, there is no way to connect the local post-shock state to the global cone-surface requirement.


##### problem 4.c

One major distinction is that the cone-flow problem is a shock-fitting problem, whereas the wavy-wall problem is a direct boundary-value problem. In cone flow, the shock location is not known in advance, so the solution must determine $\theta_s$ as part of the computation. In the wavy-wall problem, the boundary geometry is prescribed from the start, and the field is solved directly in the region above that boundary. Mathematically, this means cone flow includes a free-boundary aspect, while the wavy-wall problem does not.

A second distinction is that the cone problem is governed downstream by a nonlinear ODE system, while the wavy-wall problem is governed by a linear scalar PDE. In cone flow, the unknowns $u_r(\theta)$ and $u_\theta(\theta)$ are coupled nonlinearly through the sound speed and the geometry of spherical coordinates. In the wavy-wall problem, once the Mach-number regime is fixed, the governing equation is linear and admits superposition. Physically, the cone problem is therefore a nonlinear downstream-adjustment problem, while the wavy-wall problem is a small-disturbance propagation problem.

A third distinction is that the cone-flow solution is selected by a global compatibility condition, whereas the wavy-wall solution is available in explicit closed form. In the cone problem, one must guess a shock angle, integrate the ODE, and check whether the cone boundary condition is satisfied. In the wavy-wall problem, the subsonic field is built from exponentially decaying Fourier modes, and the supersonic field is an explicit characteristic transport of the wall signal. So the cone problem requires an iterative shooting/root-finding procedure, while the wavy-wall problem can be written down directly once the boundary forcing is known.
