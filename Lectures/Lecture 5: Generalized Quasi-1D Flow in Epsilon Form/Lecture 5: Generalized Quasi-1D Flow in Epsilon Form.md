## 1 Setup and $\varepsilon$-notation

We now specialize the integral conservation laws derived in Lectures $3-4$ to a quasi-one-dimensional setting. As before, the philosophy is:

Start from the integral conservation laws, impose modeling assumptions, and then rewrite the resulting relations in a form that exposes physical mechanisms.

Quasi-1D assumptions (steady). We consider flow through a duct whose cross-sectional area varies slowly with the streamwise coordinate $x$. At each station $x$, the flow is represented by cross-section-averaged quantities

$$
\rho(x), \quad u(x), \quad p(x), \quad T(x),
$$

with cross-sectional area $A(x)$. We allow for:

- area variation $A(x)$,
- wall friction,
- heat transfer and shaft work.

Unless stated otherwise, body forces and potential energy are neglected.

Fractional changes. For any scalar quantity $q(x)$, define the fractional change

$$
\varepsilon_{q}:=\frac{d q}{q} .
$$

These quantities represent relative changes between neighboring streamwise stations and provide a natural language for quasi-1D flow analysis.

## 2 Continuity from the integral mass conservation law

We begin from the integral mass conservation law for a fixed control volume:

$$
\begin{equation*}
\int_{\Omega} \partial_{t} \rho d V+\int_{\partial \Omega} \rho \boldsymbol{u} \cdot \boldsymbol{n} d S=0 \tag{1}
\end{equation*}
$$

Steady, quasi-1D specialization. For steady flow, the time-derivative term vanishes. Consider a slender control volume spanning $x$ to $x+d x$. Under the quasi-1D assumption, only the inlet and outlet faces contribute to the surface flux, giving

$$
\left.(\rho u A)\right|_{x+d x}-\left.(\rho u A)\right|_{x}=0
$$

Explicit face expansion. Write the outlet quantity explicitly as

$$
\left.(\rho u A)\right|_{x+d x}=(\rho+d \rho)(u+d u)(A+d A)
$$

Expanding the product,

$$
(\rho+d \rho)(u+d u)(A+d A)=\rho u A+u A d \rho+\rho A d u+\rho u d A+O\left(d^{2}\right)
$$

Retaining only first-order terms and factoring out $\rho u A$,

$$
\left.(\rho u A)\right|_{x+d x} \approx \rho u A\left(1+\frac{d \rho}{\rho}+\frac{d u}{u}+\frac{d A}{A}\right)
$$

Substituting into the flux balance and dividing by $\rho u A$ yields

$$
\begin{equation*}
\varepsilon_{\rho}+\varepsilon_{u}+\varepsilon_{A}=0 \tag{2}
\end{equation*}
$$

## $3 x$-momentum from the integral momentum conservation law

We begin from the integral momentum equation (fixed control volume):

$$
\begin{equation*}
\int_{\Omega} \partial_{t}(\rho \boldsymbol{u}) d V+\int_{\partial \Omega} \rho \boldsymbol{u}(\boldsymbol{u} \cdot \boldsymbol{n}) d S=-\int_{\partial \Omega} p \boldsymbol{n} d S+\int_{\Omega} \rho \boldsymbol{f} d V \tag{3}
\end{equation*}
$$

We neglect body forces, $\boldsymbol{f}=\mathbf{0}$.

Steady, quasi-1D specialization. For steady flow, the unsteady term vanishes. Taking the $x$ component and evaluating inlet/outlet fluxes gives

$$
\left.\left(\rho u^{2} A\right)\right|_{x+d x}-\left.\left(\rho u^{2} A\right)\right|_{x}=\left[-\int_{\partial \Omega} p \boldsymbol{n} d S\right]_{x}+(\text { wall shear })
$$

Explicit face expansion of momentum flux. Write

$$
\left.\left(\rho u^{2} A\right)\right|_{x+d x}=(\rho+d \rho)(u+d u)^{2}(A+d A)
$$

First expand the square and discard second-order terms:

$$
(u+d u)^{2}=u^{2}+2 u d u+(d u)^{2} \approx u^{2}+2 u d u
$$

Substitute this into the product and expand to first order:

$$
(\rho+d \rho)\left(u^{2}+2 u d u\right)(A+d A)=\rho u^{2} A+u^{2} A d \rho+2 \rho u A d u+\rho u^{2} d A+\mathcal{O}\left(d^{2}\right)
$$

Factoring out $\rho u^{2} A$ gives

$$
\left.\left(\rho u^{2} A\right)\right|_{x+d x} \approx \rho u^{2} A\left(1+\frac{d \rho}{\rho}+2 \frac{d u}{u}+\frac{d A}{A}\right)=\rho u^{2} A\left(1+\varepsilon_{\rho}+2 \varepsilon_{u}+\varepsilon_{A}\right)
$$

Dividing by $\rho u^{2} A$, the left-hand side becomes

$$
\varepsilon_{\rho}+2 \varepsilon_{u}+\varepsilon_{A}
$$

## Surface forces in the streamwise direction

Pressure forces on inlet and outlet faces. The inlet face contributes $+p A$ in the $+x$ direction. The outlet face contributes $-(p+d p)(A+d A)$. Expanding to first order,

$$
F_{p, \text { faces }, x} \approx-p A\left(\varepsilon_{p}+\varepsilon_{A}\right) .
$$

Pressure force on the slanted wall. When $A(x)$ varies, the lateral wall is slanted and pressure acting normal to the wall has a streamwise component. Using the geometric identity that the $x$-component of the wall area vector is $-d A$, and approximating the wall pressure by its midpoint value,

$$
p_{w} \approx p+\frac{1}{2} d p
$$

the axial force becomes

$$
F_{p, \text { wall }, x} \approx p_{w} d A \approx p A \varepsilon_{A}
$$

Net pressure force. Combining face and wall contributions,

$$
F_{p, x} \approx-p A \varepsilon_{p}=-A d p .
$$

Wall shear and geometric normalization. The viscous wall shear produces an axial drag proportional to the wetted area. Let $\mathbb{P}(x)$ denote the wetted perimeter. Then

$$
F_{\tau, x}=-\tau_{w} \mathbb{P} d x
$$

In quasi-1D momentum balances, flux terms scale with area $A$ while shear forces scale with perimeter $\mathbb{P}$. To normalize arbitrary cross-sectional geometries to the canonical circular-pipe case, we introduce the hydraulic diameter

$$
D_{h}:=\frac{4 A}{\mathbb{P}}
$$

Defining the Darcy friction factor

$$
f:=\frac{8 \tau_{w}}{\rho u^{2}},
$$

the shear force may be written as

$$
F_{\tau, x}=-\frac{f}{2} \rho u^{2} A \frac{d x}{D_{h}} .
$$

Friction increment. It is convenient to define the friction increment

$$
\varepsilon_{f}:=\frac{f d x}{D_{h}} .
$$

Unlike $\varepsilon_{\rho}$ or $\varepsilon_{u}$, this is not the differential of a state variable; it represents cumulative momentum loss over the distance $d x$.

## Final quasi-1D momentum equation in $\varepsilon$-form

Combining flux and force contributions and dividing by $\rho u^{2} A$ yields

$$
\varepsilon_{\rho}+2 \varepsilon_{u}+\varepsilon_{A}=-\frac{p}{\rho u^{2}} \varepsilon_{p}-\frac{1}{2} \varepsilon_{f}
$$

Using $p=\rho R T$ and $M^{2}=u^{2} /(\gamma R T)$,

$$
\begin{equation*}
\varepsilon_{\rho}+2 \varepsilon_{u}+\varepsilon_{A}=-\frac{1}{\gamma M^{2}} \varepsilon_{p}-\frac{1}{2} \varepsilon_{f} \tag{4}
\end{equation*}
$$

## 4 Energy from the integral energy conservation law

We begin from the steady, inviscid integral energy equation written in enthalpy-flux form (as motivated in Lectures 3-4):

$$
\begin{equation*}
\int_{\partial \Omega} \rho\left(h+\frac{1}{2}|\boldsymbol{u}|^{2}\right) \boldsymbol{u} \cdot \boldsymbol{n} d S=\delta \dot{Q}+\delta \dot{W} \tag{5}
\end{equation*}
$$

where $\delta \dot{Q}$ and $\delta \dot{W}$ are the net heat and shaft work added to the control volume.

Quasi-1D specialization. Evaluating inlet and outlet fluxes,

$$
\left.\dot{m}\left(h+\frac{1}{2} u^{2}\right)\right|_{x+d x}-\left.\dot{m}\left(h+\frac{1}{2} u^{2}\right)\right|_{x}=\delta \dot{Q}+\delta \dot{W} .
$$

Since $\dot{m}$ is constant,

$$
\begin{equation*}
d\left(h+\frac{1}{2} u^{2}\right)=\frac{\delta \dot{Q}+\delta \dot{W}}{\dot{m}} . \tag{6}
\end{equation*}
$$

Stagnation temperature. Define the stagnation enthalpy $h_{0}=h+\frac{1}{2} u^{2}$. For a calorically perfect ideal gas, $h=c_{p} T$, so $h_{0}=c_{p} T_{0}$ and

$$
c_{p} d T_{0}=\frac{\delta \dot{Q}+\delta \dot{W}}{\dot{m}}
$$

Explicit $\varepsilon$-form derivation. Using

$$
T_{0}=T+\frac{u^{2}}{2 c_{p}}
$$

take a differential:

$$
d T_{0}=d T+\frac{u}{c_{p}} d u
$$

Divide by $T_{0}$ and rewrite in fractional form, then introduce $M^{2}=u^{2} /(\gamma R T)$ to obtain

$$
\begin{equation*}
\varepsilon_{T}+(\gamma-1) M^{2} \varepsilon_{u}-\left(1+\frac{\gamma-1}{2} M^{2}\right) \varepsilon_{T_{0}}=0 \tag{7}
\end{equation*}
$$

## 5 Equation of state (closure) and outlook

Starting from the ideal-gas equation of state,

$$
p=\rho R T
$$

evaluate the pressure at $x+d x$ :

$$
p+d p=(\rho+d \rho) R(T+d T)
$$

Expanding to first order,

$$
p+d p=\rho R T+R T d \rho+\rho R d T+\mathcal{O}\left(d^{2}\right)
$$

Dividing by $p=\rho R T$ gives

$$
1+\frac{d p}{p}=1+\frac{d \rho}{\rho}+\frac{d T}{T}
$$

and therefore

$$
\varepsilon_{p}=\varepsilon_{\rho}+\varepsilon_{T} .
$$

Why $\varepsilon$-form? The governing equations have now been rewritten as linear relations between fractional changes. This form:

- isolates the relative influence of different physical mechanisms,
- places geometry, friction, and heat addition on equal footing,
- and enables algebraic solution strategies.

At this stage, all $\varepsilon$ 's are treated symmetrically. In the next lecture, we will distinguish between driving increments (e.g. $\varepsilon_{A}, \varepsilon_{f}, \varepsilon_{T_{0}}$ ) and flow responses (e.g. $\varepsilon_{u}, \varepsilon_{p}, \varepsilon_{\rho}$ ). Rewriting the system in explicit input-output form leads to the influence-coefficient framework, which provides both physical intuition and a practical tool for quasi-1D flow analysis.

