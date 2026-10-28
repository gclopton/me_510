# Module 5: Supersonic flow past a cone 

Andres Goza

April 15, 2026

## Chapter 1

## Problem Formulation and Modeling Structure

### 1.1 Problem statement and physical setting

In this module, we begin our study of supersonic flow over a cone. This problem is a classical one in gas dynamics, but it is also a particularly useful one for us pedagogically: it will force us to combine several ideas developed earlier in the course, including conservation laws, shock conditions, thermodynamic closure, and symmetry-based reduction of the governing equations.

We consider a uniform supersonic freestream impinging on a sharp circular cone whose axis is aligned with the incoming flow. Let the cone half-angle be denoted by $\theta_{c}$. Because the body is axisymmetric, and because the incoming flow is aligned with the cone axis, we expect the resulting flow to inherit that same axisymmetry. A shock forms ahead of the cone, and in the idealized picture we will develop here, that shock is itself conical. We denote its angle by $\theta_{s}$.

At a broad level, the flow field naturally separates into three parts:

- an upstream region, where the flow remains the known uniform freestream,
- a shock surface, across which the flow variables change discontinuously,
- and a downstream region, where the flow is smooth but not yet known.

This decomposition is not just a convenient picture. It already suggests the mathematical structure of the problem we will build in this chapter. Upstream of the shock, the flow state is known. Across the shock, information must be transmitted using conservation laws. Downstream of the shock, we will need governing equations that describe how the flow evolves from the shock to the cone surface.

Throughout this module, we will model the flow as steady, inviscid, and axisymmetric. These assumptions are strong, but they are also well matched to the canonical cone-flow problem we wish to study. Their value is not merely that they simplify the mathematics. More importantly, they isolate the essential gas-dynamic mechanisms we want to understand: how a shock converts a known upstream supersonic state into a compressed downstream state, and how that downstream state then adjusts smoothly to satisfy the cone geometry.

Our goal in this first chapter is therefore not yet to solve the flow. Instead, it is to formulate the problem carefully. We will identify the shock conditions that connect the known upstream region to the unknown downstream region, introduce the geometric structure of the problem, and set the stage for the governing equations that will be developed in the next chapter.

### 1.2 Modeling structure: smooth regions separated by a discontinuity

The physical picture introduced in the previous section suggests a natural way to model the flow. Rather than attempting to describe the entire flow field with a single set of equations everywhere, we instead recognize that the presence of the shock fundamentally changes how the governing laws apply in different regions.

In the upstream and downstream regions, the flow is smooth. In these regions, the differential form of the conservation laws applies, and the flow can be described using the governing equations developed in earlier modules. However, at the shock, the flow variables undergo a finite jump over an infinitesimally thin region. In this case, the differential equations are no longer valid pointwise, and we must return to the underlying integral conservation laws to describe how the flow behaves across the discontinuity.

This leads to a natural decomposition of the problem into two smooth regions separated by an interface. The upstream region is fully known: it is the uniform freestream. The downstream region is smooth but unknown, and must be determined. The shock acts as a transmission mechanism between these two regions. It converts the known upstream state into a downstream state through conservation of mass, momentum, and energy.

From this perspective, the shock plays the role of a boundary for the downstream flow, even though its location and orientation are not known a priori. Once the state immediately behind the shock is determined, it provides the data needed to solve for the flow throughout the downstream region.

This viewpoint reflects a broader modeling principle that will appear repeatedly throughout the course: when discontinuities arise, the governing equations must be interpreted through their integral form, and the resulting jump conditions provide the information needed to couple otherwise smooth regions of the flow.

### 1.3 Jump conditions from integral conservation laws

We now determine how the flow variables change across the shock. As discussed in the previous section, the shock is a surface across which the flow is discontinuous. Because of this, the differential form of the governing equations is not valid at the shock itself. Instead, we return to the integral conservation laws introduced in Module 1 and apply them directly to a control volume that encloses the shock.

## Control-volume formulation

Consider a thin control volume that straddles the shock surface, with its thickness taken to be infinitesimal in the direction normal to the shock. The control surface consists of two faces parallel to the shock (one upstream and one downstream), along with side faces whose contributions vanish in the thin-limit.

We assume that the flow is:

- steady,
- inviscid (no shear stress),
- adiabatic (no heat transfer across the shock).

Let $\boldsymbol{n}$ denote the unit normal vector to the shock, oriented from the upstream state (denoted by subscript 1) toward the downstream state (subscript 2). At each point on the shock, we decompose the velocity into normal and tangential components:

$$
\begin{equation*}
u_{n}=\boldsymbol{u} \cdot \boldsymbol{n}, \quad u_{t}=\boldsymbol{u} \cdot \boldsymbol{t} \tag{1.1}
\end{equation*}
$$

## Mass conservation

Applying conservation of mass to the control volume, and taking the thin-limit, we obtain a balance between the flux entering and leaving the shock:

$$
\begin{equation*}
\rho_{1} u_{n 1}=\rho_{2} u_{n 2} \tag{1.2}
\end{equation*}
$$

This expresses continuity of mass flux across the shock.

## Momentum conservation

Next, we apply conservation of momentum. Because the flow is inviscid, the only surface forces arise from pressure.

Projecting the momentum balance in the normal direction yields

$$
\begin{equation*}
p_{1}+\rho_{1} u_{n 1}^{2}=p_{2}+\rho_{2} u_{n 2^{\prime}}^{2} \tag{1.3}
\end{equation*}
$$

which represents the balance between pressure and normal momentum flux across the shock.
Projecting in the tangential direction gives

$$
\begin{equation*}
\rho_{1} u_{n 1} u_{t 1}=\rho_{2} u_{n 2} u_{t 2} \tag{1.4}
\end{equation*}
$$

Using Eq. (1.2), this reduces to

$$
\begin{equation*}
u_{t 1}=u_{t 2} \tag{1.5}
\end{equation*}
$$

## Energy conservation

Finally, we apply conservation of energy. Under the assumptions of steady, inviscid, and adiabatic flow, the energy balance across the shock yields

$$
\begin{equation*}
h_{1}+\frac{1}{2}\left(u_{n 1}^{2}+u_{t 1}^{2}\right)=h_{2}+\frac{1}{2}\left(u_{n 2}^{2}+u_{t 2}^{2}\right) \tag{1.6}
\end{equation*}
$$

where we have used

$$
\begin{equation*}
|\boldsymbol{u}|^{2}=u_{n}^{2}+u_{t}^{2} \tag{1.7}
\end{equation*}
$$

## Thermodynamic closure

To close this system, we adopt the same thermodynamic model used in earlier modules: the flow is a calorically perfect ideal gas, for which

$$
\begin{equation*}
p=\rho R T, \quad h=c_{p} T \tag{1.8}
\end{equation*}
$$

## Summary and interpretation

Collecting Eqs. (1.2)-(1.6), we obtain a set of algebraic relations-the jump conditions-that connect the upstream and downstream states at the shock:

$$
\begin{align*}
\rho_{1} u_{n 1} & =\rho_{2} u_{n 2}  \tag{1.9}\\
p_{1}+\rho_{1} u_{n 1}^{2} & =p_{2}+\rho_{2} u_{n 2^{\prime}}^{2}  \tag{1.10}\\
u_{t 1} & =u_{t 2}  \tag{1.11}\\
h_{1}+\frac{1}{2}\left|\boldsymbol{u}_{1}\right|^{2} & =h_{2}+\frac{1}{2}\left|\boldsymbol{u}_{2}\right|^{2} \tag{1.12}
\end{align*}
$$

These relations show that, for a given upstream state and a specified shock orientation (which determines the normal direction $\boldsymbol{n}$ through Eq. (1.1)), the downstream velocity components, pressure, and density are fully determined. In this way, the shock converts the known upstream flow into a downstream state that will serve as boundary data for the smooth flow region.

### 1.4 Consequences for governing variables

The jump conditions (1.9)-(1.12) relate the upstream and downstream states through the variables

$$
\rho, \quad \boldsymbol{u}, \quad p .
$$

These quantities arise directly from the conservation of mass, momentum, and energy, and therefore carry the physical information that is transmitted across the shock.

This observation has an important consequence for how we formulate the downstream problem. In earlier modules, we often described compressible flow using a scalar velocity potential, which allowed the governing equations to be written in a compact form. However, that formulation is built on the assumption of smooth flow, and expresses the dynamics in terms of a single scalar field.

In the present problem, the situation is fundamentally different. The jump conditions (1.9)-(1.12) are expressed in terms of density, velocity components, and pressure, and do not admit a simple representation in terms of a scalar potential. As a result, it is not natural to formulate the problem using a scalar potential.

Instead, we will work directly with the governing variables ( $\rho, \boldsymbol{u}, p$ ) and derive a differential system that describes how the flow evolves from the shock to the cone surface.

### 1.5 Geometry and coordinate system

To describe the flow field over the cone, it is natural to adopt a coordinate system that reflects the geometry of the problem. Because both the cone and the flow are axisymmetric about a common
axis, we introduce spherical coordinates $(r, \theta, \varphi)$ with the origin located at the cone apex and the polar axis aligned with the freestream direction.

In this coordinate system, the angle $\theta$ is measured from the axis of the cone, so that the cone surface corresponds to a constant value

$$
\begin{equation*}
\theta=\theta_{c} . \tag{1.13}
\end{equation*}
$$

The shock surface, which we idealize as conical, likewise corresponds to

$$
\begin{equation*}
\theta=\theta_{s} . \tag{1.14}
\end{equation*}
$$

Axisymmetry implies that the flow does not depend on the azimuthal coordinate $\varphi$, so that

$$
\begin{equation*}
\frac{\partial}{\partial \varphi}=0 . \tag{1.15}
\end{equation*}
$$

In addition, we assume that the flow has no swirl, so that the velocity has no component in the $\boldsymbol{e}_{\varphi}$ direction. The velocity field can therefore be written as

$$
\begin{equation*}
\boldsymbol{u}=u_{r}(r, \theta) \boldsymbol{e}_{r}+u_{\theta}(r, \theta) \boldsymbol{e}_{\theta} \tag{1.16}
\end{equation*}
$$

This coordinate system and velocity representation will allow us, in the next chapter, to express the governing equations in a form that is well aligned with the conical geometry of the problem.

### 1.6 Conical similarity and dimensional reduction

We now introduce a key simplifying assumption that is specific to this problem and will allow us to reduce the governing equations significantly.

To motivate this assumption, consider the geometric and physical structure of the flow. The cone is a sharp body whose geometry is defined entirely by an angle, and the upstream flow is uniform. Aside from the cone angle $\theta_{c}$, there is no intrinsic length scale in the problem. This suggests that the flow may inherit a form of geometric self-similarity: if we move along a ray emanating from the cone apex, the local flow conditions should remain unchanged.

This observation leads to the conical similarity assumption. We assume that all flow variables depend only on the angular coordinate $\theta$, and not on the radial distance $r$. That is,

$$
\begin{equation*}
u_{r}=u_{r}(\theta), \quad u_{\theta}=u_{\theta}(\theta), \quad p=p(\theta), \quad \rho=\rho(\theta) . \tag{1.17}
\end{equation*}
$$

Under this assumption, the flow is invariant along rays from the apex, and all variation occurs in the angular direction. Physically, this means that the shock and the cone impose a structure on the flow that is preserved at all distances from the apex.

The consequence of this assumption is significant. The governing equations for the smooth downstream region, which are originally partial differential equations in space, reduce to ordinary differential equations in the single variable $\theta$. In other words, the complexity of the problem is reduced from a two-dimensional spatial dependence to a one-dimensional angular dependence.

We emphasize that this reduction has not yet been carried out. In the next chapter, we will express the governing equations in spherical coordinates and apply the conical similarity assumption (1.17) to obtain the resulting system of equations.

### 1.7 Comparison with the wedge problem

Before proceeding to formulate the downstream problem, it is useful to compare the present cone-flow configuration with the two-dimensional wedge problem studied earlier in the course. Although both problems involve supersonic flow and oblique shocks, the structure of their solutions is fundamentally different.

In the wedge problem, the flow is two-dimensional and uniform both upstream and downstream of the shock. The shock produces a sudden change in the flow direction and thermodynamic state, after which the flow remains constant. The requirement that the flow be tangent to the wedge surface is enforced immediately behind the shock. As a result, the shock angle is determined directly from an algebraic relation between the upstream Mach number, the shock angle, and the flow deflection angle.

In contrast, the cone-flow problem is inherently axisymmetric. As discussed in Section 1.17, the geometry admits a conical similarity in which the flow variables depend only on the polar angle $\theta$. However, this does not imply that the downstream flow is uniform. Instead, the flow occupies a continuous region between the shock and the cone surface, and must adjust smoothly throughout this region.

A key consequence of this difference is that the shock does not, in general, produce a flow that immediately satisfies the boundary condition at the cone surface. In particular, the velocity component $u_{\theta}$ is not zero immediately behind the shock. The flow must therefore evolve from its post-shock state at $\theta=\theta_{s}$ (Eq. (1.14)) to satisfy the condition $u_{\theta}\left(\theta_{c}\right)=0$ at the cone surface (Eq. (1.13)).

This behavior can be understood in terms of the additional geometric freedom available in axisymmetric flow. Unlike the two-dimensional wedge, where the flow is constrained to turn within a single plane, the cone geometry allows the flow to redistribute in the circumferential direction. This three-dimensional relaxation reduces the amount of turning required at the shock and distributes it throughout the downstream region.

The consequence is that the cone-flow problem cannot be reduced to an algebraic relation for the shock angle. Instead, the downstream flow must be determined by solving a differential system that governs how the flow evolves from the shock to the cone surface. The shock angle is then determined as part of this solution, rather than specified in advance.

### 1.8 Boundary conditions, domain, and problem structure

We now collect the elements developed in the previous sections to formulate the problem precisely.
The upstream state is known. The freestream conditions specify the velocity, pressure, density, and Mach number ahead of the shock. This provides the initial information from which the rest of the flow must be determined.

The shock acts as a transmission mechanism between the known upstream region and the unknown downstream region. For a given shock angle $\theta_{s}$ (Eq. (1.14)), the jump conditions derived in Section 1.3 determine the downstream state immediately behind the shock.

The downstream flow occupies the region between the shock and the cone surface. In terms of the
angular coordinate, this corresponds to

$$
\begin{equation*}
\theta \in\left[\theta_{c}, \theta_{s}\right] \tag{1.18}
\end{equation*}
$$

Within this region, the flow is smooth and satisfies the assumptions introduced earlier.
At the cone surface, the flow must satisfy a geometric constraint. Because the surface is impermeable, there can be no flow normal to it. In the present coordinate system, this condition takes the form

$$
\begin{equation*}
u_{\theta}\left(\theta_{c}\right)=0 \tag{1.19}
\end{equation*}
$$

At this stage, the unknowns in the problem are the downstream flow field and the shock angle $\theta_{s}$. These quantities are not independent. The shock angle determines the downstream state at $\theta_{s}$ through the jump conditions, while the downstream solution must satisfy the boundary condition (2.51) at the cone surface. The physically relevant solution is obtained when both of these requirements are satisfied simultaneously.

To solve this problem, we require governing equations for the smooth downstream region that describe how the flow evolves from the shock to the cone surface. In Chapter 2, we will formulate and reduce these equations under the assumptions introduced here, leading to the Taylor-Maccoll equation. In Chapter 3, we will use this formulation to determine both the downstream flow and the shock angle, which is not known a priori.

## Chapter 2

## Governing Equations and Reduction to the Taylor-Maccoll System

### 2.1 Governing equations in the smooth downstream region

We now turn to the mathematical description of the flow in the region downstream of the shock. As established in Chapter 1, this region is smooth, and the flow variables vary continuously throughout. As a result, the governing equations may be applied in their differential form.

We model the flow as steady and inviscid, consistent with the assumptions introduced earlier. Under these conditions, the governing equations are the conservation of mass and momentum:

$$
\begin{align*}
\nabla \cdot(\rho \boldsymbol{u}) & =0  \tag{2.1}\\
\rho(\boldsymbol{u} \cdot \nabla) \boldsymbol{u} & =-\nabla p . \tag{2.2}
\end{align*}
$$

These equations apply throughout the smooth region between the shock and the cone surface. In contrast to the shock itself, where discontinuities are present and integral forms must be used, the differential form is valid everywhere in the downstream domain.

To complete the system, we require a thermodynamic model. As in previous modules, we assume that the fluid is a calorically perfect ideal gas. In addition, because the flow downstream of the shock is smooth and adiabatic, it is isentropic. Under these conditions, we make use of the Bernoulli relation derived previously in Module 3b, obtained from the momentum equation together with isentropic thermodynamic relations:

$$
\begin{equation*}
h+\frac{1}{2}|\boldsymbol{u}|^{2}=h_{0} \tag{2.3}
\end{equation*}
$$

where $h_{0}$ is the stagnation enthalpy, which remains constant throughout the smooth downstream region.

Even though we derived Eq. (2.3) using conservation of momentum together with isentropic thermodynamic relations, under the steady, inviscid, isentropic assumptions used here, it is equivalent to the energy equation. We will use this form in what follows.

To relate thermodynamic quantities, we also use the calorically perfect ideal gas relations:

$$
h=c_{p} T, \quad p=\rho R T, \quad \gamma=\frac{c_{p}}{c_{v}}, \quad R=c_{p}-c_{v}
$$

Together, Eqs. (2.1)-(2.30) define the governing system for the smooth downstream flow. In the following sections, we will express these equations in a coordinate system aligned with the cone geometry and systematically reduce them using the assumptions introduced in Chapter 1.

### 2.2 Governing equations in spherical coordinates

To exploit the geometry of the cone-flow problem, we now express the governing equations in the spherical coordinate system ( $r, \theta, \varphi$ ) introduced in Chapter 1. Recall that the velocity field is written as

$$
\begin{equation*}
\boldsymbol{u}=u_{r} \boldsymbol{e}_{r}+u_{\theta} \boldsymbol{e}_{\theta} \tag{2.4}
\end{equation*}
$$

where we have already assumed axisymmetry and no swirl.

## Continuity equation

In spherical coordinates, the continuity equation (2.1) takes the form

$$
\begin{equation*}
\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \rho u_{r}\right)+\frac{1}{r \sin \theta} \frac{\partial}{\partial \theta}\left(\sin \theta \rho u_{\theta}\right)=0 . \tag{2.5}
\end{equation*}
$$

## Momentum equations

The momentum equation (2.2) yields two nontrivial components in the ( $r, \theta$ ) directions.

Radial momentum. The radial component is

$$
\begin{equation*}
\rho\left(u_{r} \frac{\partial u_{r}}{\partial r}+\frac{u_{\theta}}{r} \frac{\partial u_{r}}{\partial \theta}-\frac{u_{\theta}^{2}}{r}\right)=-\frac{\partial p}{\partial r} . \tag{2.6}
\end{equation*}
$$

The first two terms represent convective acceleration in the radial direction, while the third term arises from the curvature of the coordinate system and corresponds to the effect of polar motion on the radial component of velocity.

Polar momentum. The $\theta$-component is

$$
\begin{equation*}
\rho\left(u_{r} \frac{\partial u_{\theta}}{\partial r}+\frac{u_{\theta}}{r} \frac{\partial u_{\theta}}{\partial \theta}+\frac{u_{r} u_{\theta}}{r}\right)=-\frac{1}{r} \frac{\partial p}{\partial \theta} . \tag{2.7}
\end{equation*}
$$

Here, the additional geometric terms reflect the coupling between radial motion and turning in the polar direction.

## Summary

Equations (2.5), (2.6), and (2.7), together with the Bernoulli relation (2.3), define the governing system for the downstream flow expressed in spherical coordinates.

In the next section, we will apply the conical similarity assumption introduced in Chapter 1 to reduce these equations to a system of ordinary differential equations in the angular coordinate $\theta$.

### 2.3 Application of conical similarity

We now apply the conical similarity assumption introduced in Chapter 1. Recall that, under this assumption, all flow variables depend only on the polar angle $\theta$ :

$$
\begin{equation*}
u_{r}=u_{r}(\theta), \quad u_{\theta}=u_{\theta}(\theta), \quad p=p(\theta), \quad \rho=\rho(\theta) \tag{2.8}
\end{equation*}
$$

This assumption implies that all derivatives with respect to $r$ vanish:

$$
\begin{equation*}
\frac{\partial(\cdot)}{\partial r}=0 . \tag{2.9}
\end{equation*}
$$

We now apply these simplifications to the governing equations derived in the previous section.

## Continuity equation

Substituting Eqs. (2.8) and (2.9) into the continuity equation (2.5), we must take care with the radial derivative. Although $\rho$ and $u_{r}$ are independent of $r$, the factor $r^{2}$ remains, so that

$$
\begin{equation*}
\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \rho u_{r}\right)=\frac{2 \rho u_{r}}{r} . \tag{2.10}
\end{equation*}
$$

The continuity equation therefore becomes

$$
\begin{equation*}
\frac{2 \rho u_{r}}{r}+\frac{1}{r \sin \theta} \frac{d}{d \theta}\left(\sin \theta \rho u_{\theta}\right)=0 . \tag{2.11}
\end{equation*}
$$

Multiplying through by $r$ gives

$$
\begin{equation*}
2 \rho u_{r}+\frac{1}{\sin \theta} \frac{d}{d \theta}\left(\sin \theta \rho u_{\theta}\right)=0 . \tag{2.12}
\end{equation*}
$$

This equation expresses conservation of mass under conical similarity, accounting for both radial transport and geometric spreading in the polar direction.

## Radial momentum equation

Applying the same assumptions to the radial momentum equation (2.6), all derivatives with respect to $r$ vanish, and we obtain

$$
\begin{equation*}
\rho\left(\frac{u_{\theta}}{r} \frac{d u_{r}}{d \theta}-\frac{u_{\theta}^{2}}{r}\right)=0 . \tag{2.13}
\end{equation*}
$$

Multiplying through by $r$ and assuming $\rho \neq 0$, this reduces to

$$
\begin{equation*}
u_{\theta} \frac{d u_{r}}{d \theta}-u_{\theta}^{2}=0 \tag{2.14}
\end{equation*}
$$

For $u_{\theta} \neq 0$, we may divide through by $u_{\theta}$ to obtain

$$
\begin{equation*}
\frac{d u_{r}}{d \theta}=u_{\theta} \tag{2.15}
\end{equation*}
$$

This relation shows that the radial velocity changes with $\theta$ in direct proportion to the polar velocity component.

## Polar momentum equation

Applying the same assumptions to the polar momentum equation (2.7), we obtain

$$
\begin{equation*}
\rho\left(\frac{u_{\theta}}{r} \frac{d u_{\theta}}{d \theta}+\frac{u_{r} u_{\theta}}{r}\right)=-\frac{1}{r} \frac{d p}{d \theta} \tag{2.16}
\end{equation*}
$$

Multiplying through by $r$ and simplifying gives

$$
\begin{equation*}
\rho\left(u_{\theta} \frac{d u_{\theta}}{d \theta}+u_{r} u_{\theta}\right)=-\frac{d p}{d \theta} \tag{2.17}
\end{equation*}
$$

## Summary

Under the conical similarity assumption, the governing equations reduce to the system

$$
\begin{align*}
\frac{d}{d \theta}\left(\sin \theta \rho u_{\theta}\right) & =0  \tag{2.18}\\
\frac{d u_{r}}{d \theta} & =u_{\theta}  \tag{2.19}\\
\rho\left(u_{\theta} \frac{d u_{\theta}}{d \theta}+u_{r} u_{\theta}\right) & =-\frac{d p}{d \theta} \tag{2.20}
\end{align*}
$$

These equations describe the evolution of the flow variables as functions of the angular coordinate $\theta$. In the next section, we will use thermodynamic relations to eliminate $p$ and $\rho$ and obtain a closed system in terms of the velocity components alone.

### 2.4 Governing ODEs in reduced form

The reduced system obtained in the previous section still involves the thermodynamic variables $p(\theta)$ and $\rho(\theta)$ in addition to the velocity components $u_{r}(\theta)$ and $u_{\theta}(\theta)$. Our next goal is to eliminate $p$ and $\rho$ so that the downstream problem is written entirely in terms of the velocity field.

We begin from the Bernoulli relation (2.3),

$$
\begin{equation*}
h+\frac{1}{2}\left(u_{r}^{2}+u_{\theta}^{2}\right)=h_{0} \tag{2.21}
\end{equation*}
$$

Differentiating with respect to $\theta$ gives

$$
\begin{equation*}
\frac{d h}{d \theta}+u_{r} \frac{d u_{r}}{d \theta}+u_{\theta} \frac{d u_{\theta}}{d \theta}=0 \tag{2.22}
\end{equation*}
$$

For isentropic flow, we may relate enthalpy and pressure through

$$
\begin{equation*}
d h=\frac{1}{\rho} d p \tag{2.23}
\end{equation*}
$$

so that Eq. (2.22) becomes

$$
\begin{equation*}
\frac{1}{\rho} \frac{d p}{d \theta}+u_{r} \frac{d u_{r}}{d \theta}+u_{\theta} \frac{d u_{\theta}}{d \theta}=0 \tag{2.24}
\end{equation*}
$$

Using the radial momentum relation derived in the previous section,

$$
\begin{equation*}
\frac{d u_{r}}{d \theta}=u_{\theta} \tag{2.25}
\end{equation*}
$$

Eq. (2.24) becomes

$$
\begin{equation*}
\frac{d p}{d \theta}=-\rho\left(u_{r} u_{\theta}+u_{\theta} \frac{d u_{\theta}}{d \theta}\right) \tag{2.26}
\end{equation*}
$$

This is identical to the reduced polar momentum equation, and therefore confirms that the Bernoulli relation captures the same information as the energy equation in the present setting.

To eliminate $\rho$, we next relate enthalpy to the sound speed. From the calorically perfect ideal-gas relations

$$
\begin{equation*}
p=\rho R T, \quad h=c_{p} T, \quad \gamma=\frac{c_{p}}{c_{v}}, \quad R=c_{p}-c_{v} \tag{2.27}
\end{equation*}
$$

we first compute

$$
\begin{equation*}
R=c_{p}-c_{v}=c_{p}-\frac{c_{p}}{\gamma}=\frac{\gamma-1}{\gamma} c_{p} \tag{2.28}
\end{equation*}
$$

Substituting Eq. (2.28) into $p=\rho R T$ gives

$$
\begin{equation*}
\frac{p}{\rho}=R T=\frac{\gamma-1}{\gamma} c_{p} T=\frac{\gamma-1}{\gamma} h \tag{2.29}
\end{equation*}
$$

and therefore

$$
\begin{equation*}
h=\frac{\gamma}{\gamma-1} \frac{p}{\rho} \tag{2.30}
\end{equation*}
$$

We also recall that, for a calorically perfect ideal gas,

$$
\begin{equation*}
a^{2}=\gamma R T . \tag{2.31}
\end{equation*}
$$

Using $p=\rho R T$, this becomes

$$
\begin{equation*}
a^{2}=\gamma \frac{p}{\rho} \tag{2.32}
\end{equation*}
$$

Combining Eqs. (2.30) and (2.32) gives

$$
\begin{equation*}
h=\frac{a^{2}}{\gamma-1} \tag{2.33}
\end{equation*}
$$

Substituting this into the Bernoulli relation (2.21) gives

$$
\begin{equation*}
\frac{a^{2}}{\gamma-1}+\frac{1}{2}\left(u_{r}^{2}+u_{\theta}^{2}\right)=h_{0} \tag{2.34}
\end{equation*}
$$

or equivalently

$$
\begin{equation*}
a^{2}=(\gamma-1)\left[h_{0}-\frac{1}{2}\left(u_{r}^{2}+u_{\theta}^{2}\right)\right] . \tag{2.35}
\end{equation*}
$$

We now return to the reduced continuity equation. Expanding

$$
\begin{equation*}
2 \rho u_{r}+\frac{1}{\sin \theta} \frac{d}{d \theta}\left(\sin \theta \rho u_{\theta}\right)=0 \tag{2.36}
\end{equation*}
$$

gives

$$
\begin{equation*}
u_{\theta} \frac{d \rho}{d \theta}+\rho \frac{d u_{\theta}}{d \theta}+\rho u_{\theta} \cot \theta+2 \rho u_{r}=0 \tag{2.37}
\end{equation*}
$$

Dividing by $\rho$ yields

$$
\begin{equation*}
u_{\theta} \frac{1}{\rho} \frac{d \rho}{d \theta}+\frac{d u_{\theta}}{d \theta}+u_{\theta} \cot \theta+2 u_{r}=0 \tag{2.38}
\end{equation*}
$$

To eliminate the density derivative, we differentiate Eq. (2.21) in the form

$$
h+\frac{1}{2}\left(u_{r}^{2}+u_{\theta}^{2}\right)=h_{0}
$$

but now use the thermodynamic identity

$$
\begin{equation*}
d h=\frac{a^{2}}{\rho} d \rho \tag{2.39}
\end{equation*}
$$

This gives

$$
\begin{equation*}
a^{2} \frac{1}{\rho} \frac{d \rho}{d \theta}+u_{r} \frac{d u_{r}}{d \theta}+u_{\theta} \frac{d u_{\theta}}{d \theta}=0 \tag{2.40}
\end{equation*}
$$

Using Eq. (2.25), this becomes

$$
\begin{equation*}
a^{2} \frac{1}{\rho} \frac{d \rho}{d \theta}+u_{r} u_{\theta}+u_{\theta} \frac{d u_{\theta}}{d \theta}=0 \tag{2.41}
\end{equation*}
$$

Solving for the density derivative gives

$$
\begin{equation*}
\frac{1}{\rho} \frac{d \rho}{d \theta}=-\frac{u_{\theta}}{a^{2}}\left(u_{r}+\frac{d u_{\theta}}{d \theta}\right) \tag{2.42}
\end{equation*}
$$

Substituting Eq. (2.42) into Eq. (2.38), we obtain

$$
\begin{equation*}
-\frac{u_{\theta}^{2}}{a^{2}}\left(u_{r}+\frac{d u_{\theta}}{d \theta}\right)+\frac{d u_{\theta}}{d \theta}+u_{\theta} \cot \theta+2 u_{r}=0 \tag{2.43}
\end{equation*}
$$

Rearranging gives

$$
\begin{equation*}
\left(1-\frac{u_{\theta}^{2}}{a^{2}}\right) \frac{d u_{\theta}}{d \theta}+u_{\theta} \cot \theta+2 u_{r}-\frac{u_{r} u_{\theta}^{2}}{a^{2}}=0 \tag{2.44}
\end{equation*}
$$

Solving for $d u_{\theta} / d \theta$, we arrive at

$$
\begin{equation*}
\frac{d u_{\theta}}{d \theta}=\frac{u_{r} u_{\theta}^{2}-a^{2}\left(2 u_{r}+u_{\theta} \cot \theta\right)}{a^{2}-u_{\theta}^{2}} \tag{2.45}
\end{equation*}
$$

We have therefore reduced the governing equations to a closed first-order system for the velocity components:

$$
\begin{align*}
\frac{d u_{r}}{d \theta} & =u_{\theta}  \tag{2.46}\\
\frac{d u_{\theta}}{d \theta} & =\frac{u_{r} u_{\theta}^{2}-a^{2}\left(2 u_{r}+u_{\theta} \cot \theta\right)}{a^{2}-u_{\theta}^{2}} \tag{2.47}
\end{align*}
$$

where the sound speed is determined algebraically from

$$
\begin{equation*}
a^{2}=(\gamma-1)\left[h_{0}-\frac{1}{2}\left(u_{r}^{2}+u_{\theta}^{2}\right)\right] . \tag{2.48}
\end{equation*}
$$

Here $h_{0}$ is the stagnation enthalpy, which is determined by the known upstream freestream state and remains constant throughout the flow.
Equations (2.46)-(2.48) are the form of the Taylor-Maccoll system that we will use in Chapter 3.

### 2.5 Structure of the Taylor-Maccoll system

It is useful to pause and examine the structure of this system (2.46)-(2.48) before proceeding further.

## Unknowns and domain

The unknowns are the velocity components $u_{r}(\theta)$ and $u_{\theta}(\theta)$. The flow is defined in the angular interval between the cone surface and the shock,

$$
\begin{equation*}
\theta_{c} \leq \theta \leq \theta_{s} \tag{2.49}
\end{equation*}
$$

where $\theta_{c}$ is the cone half-angle and $\theta_{s}$ is the (as yet unknown) shock angle.

## Nonlinearity and coupling

The system (2.46)-(2.48) is nonlinear. The evolution of $u_{\theta}$ depends on both velocity components as well as on the local sound speed $a$, which itself depends on the velocity magnitude through Eq. (2.48). As a result, the equations are fully coupled and must be solved simultaneously.

## Role of the sound speed

The sound speed is not an independent variable. Instead, it is determined algebraically from the Bernoulli relation through Eq. (2.48). This reflects the fact that the thermodynamic state of the flow is slaved to the velocity field under the assumptions of steady, inviscid, isentropic flow in the smooth downstream region.

## Singular structure

A notable feature of Eq. (2.47) is the denominator $a^{2}-u_{\theta}^{2}$. This term can, in principle, vanish at certain values of $\theta$, leading to a singular behavior in the differential equation. As we will see later, this structure plays an important role in determining physically admissible solutions.

## Interpretation

Taken together, Eqs. (2.46)-(2.48) define a nonlinear dynamical system in the angular variable $\theta$. The shock provides the initial state of this system, and the cone surface imposes a constraint that the solution must satisfy.
In the next section, we will make these ideas precise by formulating the boundary conditions associated with the shock and the cone surface.

### 2.6 Boundary conditions

To complete the mathematical formulation of the problem, we now specify the boundary conditions associated with the shock and the cone surface. These conditions connect the Taylor-Maccoll system derived in §2.4 to the physical structure established in Chapter 1.

## Conditions at the shock

The shock forms the outer boundary of the downstream flow and is located at $\theta=\theta_{s}$. Across the shock, the flow variables satisfy the jump conditions derived in Chapter 1 (see Eqs. (1.2)-(1.6)).

The upstream state is known from the freestream conditions. For a given shock angle $\theta_{s}$, the jump conditions determine the downstream state immediately behind the shock, including the normal and tangential velocity components relative to the shock,

$$
u_{n 2}, \quad u_{t 2}
$$

To use these values as initial conditions for the Taylor-Maccoll system, we express them in the spherical basis. Since the shock is the conical surface $\theta=\theta_{s}$, its tangent direction in the meridional plane is $\boldsymbol{e}_{r}$, while its normal points in the $-\boldsymbol{e}_{\theta}$ direction (from the upstream region into the downstream region). Thus,

$$
\begin{equation*}
u_{r}\left(\theta_{s}\right)=u_{t 2}, \quad u_{\theta}\left(\theta_{s}\right)=-u_{n 2} \tag{2.50}
\end{equation*}
$$

These values serve as the initial conditions for the Taylor-Maccoll system (2.46)-(2.47).

## Condition at the cone surface

At the cone surface $\theta=\theta_{c}$, the flow must satisfy the no-penetration condition. Since the surface is aligned with the radial direction, this requires that

$$
\begin{equation*}
u_{\theta}\left(\theta_{c}\right)=0 \tag{2.51}
\end{equation*}
$$

No additional condition is imposed on the radial velocity $u_{r}$ at the surface.

## Dependence on the shock angle

A key feature of the problem is that the shock angle $\theta_{s}$ is not known a priori. The initial conditions at the shock depend on $\theta_{s}$, and different choices of $\theta_{s}$ will produce different solutions of the Taylor-Maccoll system.

Only for particular values of $\theta_{s}$ will the resulting solution satisfy the cone boundary condition (2.51). Determining this value of $\theta_{s}$ is therefore part of the solution.

## Summary

The Taylor-Maccoll system is to be solved on the interval $\theta_{c} \leq \theta \leq \theta_{s}$, with initial conditions at the shock determined by the jump conditions from Chapter 1 and a boundary condition at the cone surface requiring $u_{\theta}\left(\theta_{c}\right)=0$. The location of the outer boundary $\theta_{s}$ is itself unknown and must be determined as part of the solution.

## Chapter 3

## Solution to the cone-flow problem

### 3.1 Algorithmic overview of the solution procedure

The formulation developed in Chapter 2 reduces the cone-flow problem to a system of ordinary differential equations together with boundary conditions imposed at the shock and at the cone surface. The remaining task is to determine the shock angle $\theta_{s}$ and the corresponding flow field that satisfy these conditions simultaneously.

The structure of the problem suggests a natural solution strategy: for a given candidate shock angle, we compute the post-shock state, integrate the Taylor-Maccoll system toward the cone, and then assess whether the cone boundary condition is satisfied. This leads to an iterative procedure, summarized below.

```
Algorithm 1 Determination of the shock angle and flow field
    Given: freestream state, cone angle $\theta_{c}$
    Choose initial bracket $\left[\theta_{s}^{(a)}, \theta_{s}^{(b)}\right]$
    repeat
        Choose $\theta_{s}$ within the current bracket
        Compute post-shock state at $\theta=\theta_{s}$
        Integrate Taylor-Maccoll system from $\theta_{s}$ to $\theta_{c}$
        Evaluate residual $R\left(\theta_{s}\right)=u_{\theta}\left(\theta_{c}\right)$
        Update bracket based on sign of $R$
    until convergence
    return $\theta_{s}, u_{r}(\theta), u_{\theta}(\theta)$
```

Each step of this procedure will be developed in detail in the sections that follow. The key point is that the shock angle is not prescribed in advance, but instead emerges as part of the solution through the requirement that the cone boundary condition be satisfied.

### 3.2 Initialization at the shock

The first step in the solution procedure is to determine the flow state immediately downstream of the shock for a given candidate shock angle $\theta_{s}$. This state provides the initial condition required to integrate the Taylor-Maccoll system.

## Given quantities

We assume that the upstream (freestream) state is known. This includes the velocity, pressure, and density of the incoming flow. For a specified value of the shock angle $\theta_{s}$, the orientation of the shock surface is therefore known.

## Application of jump conditions

With the shock orientation specified, the upstream velocity is decomposed into components normal and tangential to the shock using Eq. (1.1). The jump conditions derived in Chapter 1 (Eqs. (1.9)(1.12)) are then applied to determine the downstream state immediately behind the shock.

In particular, these relations provide the downstream normal and tangential velocity components, $u_{n 2}$ and $u_{t 2}$, as functions of the upstream state and the shock angle $\theta_{s}$.

## Projection into spherical coordinates

The Taylor-Maccoll system is expressed in terms of the spherical velocity components $u_{r}$ and $u_{\theta}$. To obtain these from the shock-aligned components, we use the geometric relation derived in Chapter 2 (Eq. (2.50)):

$$
u_{r}\left(\theta_{s}\right)=u_{t 2}, \quad u_{\theta}\left(\theta_{s}\right)=-u_{n 2} .
$$

This transformation converts the downstream velocity into the coordinate system used for the differential equations.

## Initial condition for the Taylor-Maccoll system

The values

$$
u_{r}\left(\theta_{s}\right), \quad u_{\theta}\left(\theta_{s}\right)
$$

obtained above serve as the initial condition for the Taylor-Maccoll system. For each candidate value of $\theta_{s}$, this procedure produces a corresponding initial state from which the downstream solution can be computed.

We emphasize that the initial condition depends parametrically on $\theta_{s}$. Different choices of the shock angle will produce different initial states, and therefore different solutions of the TaylorMaccoll system.

### 3.3 Integration of the Taylor-Maccoll system

Given the initial condition at $\theta=\theta_{s}$ obtained in §3.2, we now integrate the Taylor-Maccoll system inward toward the cone surface.

## Initial value problem

The Taylor-Maccoll equations (Eqs. (2.46)-(2.47)) define a system of first-order ordinary differential equations for the velocity components ( $u_{r}, u_{\theta}$ ) as functions of $\theta$. For a specified shock angle $\theta_{s}$, and corresponding initial condition

$$
u_{r}\left(\theta_{s}\right), \quad u_{\theta}\left(\theta_{s}\right),
$$

the problem is posed as an initial value problem.

## Direction of integration

The integration proceeds from the shock toward the cone surface:

$$
\theta=\theta_{s} \longrightarrow \theta=\theta_{c}
$$

with $\theta$ decreasing. In practice, this is implemented by stepping in $\theta$ using a negative increment $\Delta \theta<0$.

## Evaluation of the right-hand side

At each step of the integration, the derivatives $d u_{r} / d \theta$ and $d u_{\theta} / d \theta$ are evaluated using the TaylorMaccoll equations. This requires computing the sound speed $a^{2}$ from Eq. (2.48) using the current values of $\left(u_{r}, u_{\theta}\right)$.

Thus, at each value of $\theta$, the right-hand side depends only on the current state, and no additional variables are required.

## Numerical integration method

The system may be integrated using a standard explicit method, such as a fourth-order RungeKutta scheme. At each step, the method evaluates the right-hand side of the Taylor-Maccoll equations multiple times to obtain an accurate update of $\left(u_{r}, u_{\theta}\right)$.

The details of the Runge-Kutta method are standard and will not be reproduced here. The key requirement is that the method provides sufficient accuracy in the evolution of $u_{\theta}$, since the cone boundary condition depends directly on its value at $\theta_{c}$.

## Step size considerations

The choice of step size $\Delta \theta$ affects both accuracy and stability of the integration. A step size that is too large may fail to resolve variations in the solution, while a step size that is too small increases computational cost.

In practice:

- a uniform step size may be used for simplicity,
- adaptive step sizing can be advantageous if the solution exhibits rapid variation.

Particular care is required near regions where the denominator in Eq. (2.47) becomes small, since this can lead to rapid changes in the solution.

## Termination of the integration

The integration proceeds until the cone surface is reached at $\theta=\theta_{c}$. At this point, the value of $u_{\theta}\left(\theta_{c}\right)$ is recorded. This value will be used to evaluate the residual in §3.4.

### 3.4 Residual formulation

We define the residual function

$$
\begin{equation*}
R\left(\theta_{s}\right):=u_{\theta}\left(\theta_{c}\right) \tag{3.1}
\end{equation*}
$$

where $u_{\theta}\left(\theta_{c}\right)$ is obtained by:

1. computing the post-shock state for the given $\theta_{s}$ (see §3.2),
2. integrating the Taylor-Maccoll system to $\theta_{c}$ (see§3.3).

## Root-finding problem

The cone-flow problem is thus reduced to finding a value of the shock angle $\theta_{s}$ such that

$$
\begin{equation*}
R\left(\theta_{s}\right)=0 \tag{3.2}
\end{equation*}
$$

This reformulation converts the boundary-value problem into a scalar root-finding problem, which will be solved iteratively in the next section.

### 3.5 Iterative determination of the shock angle

We drive the residual $R\left(\theta_{s}\right)$ to zero using an iterative root-finding procedure.

## Bracketing the solution

A robust approach begins by identifying an interval $\left[\theta_{s}^{(a)}, \theta_{s}^{(b)}\right]$ such that

$$
\begin{equation*}
R\left(\theta_{s}^{(a)}\right) R\left(\theta_{s}^{(b)}\right)<0 \tag{3.3}
\end{equation*}
$$

This condition ensures that a root of $R\left(\theta_{s}\right)$ lies between $\theta_{s}^{(a)}$ and $\theta_{s}^{(b)}$.
In practice, such a bracket may be obtained by evaluating the residual at a sequence of candidate shock angles until a sign change is observed.

## Bisection method

Given a bracket satisfying Eq. (3.3), the root may be determined using the bisection method. At iteration $k$, let the current bracket be $\left[\theta_{s}^{(a)}, \theta_{s}^{(b)}\right]$. Define the midpoint

$$
\begin{equation*}
\theta_{s}^{(m)}=\frac{1}{2}\left(\theta_{s}^{(a)}+\theta_{s}^{(b)}\right) \tag{3.4}
\end{equation*}
$$

The residual $R\left(\theta_{s}^{(m)}\right)$ is evaluated by:

1. computing the post-shock state (see §3.2),
2. integrating the Taylor-Maccoll system to $\theta_{c}$ (see §3.3),
3. evaluating $u_{\theta}\left(\theta_{c}\right)$ (see §3.4).

The bracket is then updated according to the sign of the residual:

- If $R\left(\theta_{s}^{(a)}\right) R\left(\theta_{s}^{(m)}\right)<0$, set $\theta_{s}^{(b)} \leftarrow \theta_{s}^{(m)}$.
- Otherwise, set $\theta_{s}^{(a)} \leftarrow \theta_{s}^{(m)}$.

This procedure is repeated, shrinking the bracket at each step, until convergence is achieved.

## Convergence criteria

The iteration may be terminated when either of the following conditions is satisfied:

$$
\begin{align*}
\left|R\left(\theta_{s}^{(m)}\right)\right| & <\varepsilon,  \tag{3.5}\\
\left|\theta_{s}^{(b)}-\theta_{s}^{(a)}\right| & <\varepsilon . \tag{3.6}
\end{align*}
$$

Here, $\varepsilon$ is a prescribed tolerance.

## Remarks on alternative methods

Other root-finding methods, such as the secant or Newton methods, may also be used. These methods can converge more rapidly, but generally require more careful initialization or additional information. The bisection method provides a simple and robust baseline that is sufficient for the present problem.

## Summary

The determination of the shock angle $\theta_{s}$ proceeds by combining:

- the initialization at the shock (Chapter 1 and §3.2),
- the integration of the Taylor-Maccoll system (§3.3),
- and the evaluation of the residual (§3.4),
within an iterative root-finding procedure.
The converged value of $\theta_{s}$ yields a solution that satisfies both the governing equations and the boundary condition at the cone surface.


### 3.6 Failure modes and existence of solutions

The solution procedure described in §3.5 assumes that a value of the shock angle $\theta_{s}$ exists for which the residual $R\left(\theta_{s}\right)$ vanishes. In practice, this is not always the case.

This becomes apparent directly in the algorithm. Several distinct failure modes may be encountered:
(i) Failure to reach the cone surface. For some choices of $\theta_{s}$, the integration of the Taylor-Maccoll system may terminate before $\theta=\theta_{c}$ is reached. This typically occurs when the solution develops very large gradients or becomes undefined, preventing continuation of the integration.
(ii) Approach to a singular state. The Taylor-Maccoll system contains the factor $a^{2}-u_{\theta}^{2}$ in the denominator of Eq. (2.47). If this quantity approaches zero during the integration, the solution exhibits singular behavior, and the numerical integration becomes unstable or fails.
(iii) Absence of a sign change in the residual. Even when the integration proceeds smoothly to $\theta=\theta_{c}$, it may not be possible to identify a bracket $\left[\theta_{s}^{(a)}, \theta_{s}^{(b)}\right]$ for which $R\left(\theta_{s}^{(a)}\right)$ and $R\left(\theta_{s}^{(b)}\right)$ have opposite signs. In this case, the bisection method cannot be applied, and no root of $R\left(\theta_{s}\right)$ is found within the admissible range of shock angles.

These behaviors indicate that no value of $\theta_{s}$ produces a solution that simultaneously satisfies the Taylor-Maccoll system and the cone boundary condition.

Interpretation. When these failure modes occur, the assumed flow structure-an attached conical shock with a smooth downstream adjustment to the cone surface-is not physically realizable for the specified freestream conditions and cone angle. In such cases, the flow instead exhibits a different structure, typically involving a detached shock that is not captured by the present formulation. Physically, this detachment might occur because an attached conical shock must deflect the incoming flow just enough so that the downstream velocity can adjust smoothly and become tangent to the cone surface. As the cone angle increases (or the upstream Mach number decreases), the required turning becomes stronger. Beyond a certain point, no oblique shock can produce a downstream state compatible with this smooth adjustment: the flow cannot remain attached while satisfying both the shock relations and the cone boundary condition. The flow then reorganizes into a different structure, typically involving a detached shock that stands off from the cone and allows a more gradual adjustment of the flow.

Thus, the existence of a solution to the Taylor-Maccoll problem is not guaranteed, but depends on the compatibility between the governing equations, the boundary conditions, and the geometry of the cone.

### 3.7 Summary and conceptual interpretation of the module

In this module, we have developed a complete framework for analyzing compressible flow over a cone. The problem was formulated by decomposing the flow into upstream, shock, and downstream regions, with the shock providing the mechanism by which information from the known upstream state is transmitted into the downstream flow.

Within the downstream region, the assumptions of steady, inviscid, axisymmetric flow lead to the Taylor-Maccoll system, a set of ordinary differential equations governing the evolution of the velocity components as functions of the polar angle. This reduction from a multidimensional flow problem to a one-dimensional dynamical system reflects the strong geometric constraint imposed by the conical configuration.

The solution of this system requires combining three elements: the jump conditions at the shock, which determine the initial state of the downstream flow; the differential equations, which describe how the flow evolves toward the cone; and the boundary condition at the cone surface, which imposes a global constraint on the solution. The shock angle is not specified in advance, but is instead determined as part of the solution by enforcing consistency between these elements.

This structure distinguishes the cone-flow problem from the wedge problem considered previously. In the wedge case, the governing relations reduce to algebraic equations that directly determine the shock angle. In contrast, the cone problem requires solving a differential system whose solution selects the shock angle through a global condition.

Finally, the analysis reveals that a solution does not always exist for arbitrary combinations of cone angle and freestream conditions. When the required flow turning exceeds what can be achieved by an attached shock, the assumed flow structure breaks down, and a detached shock forms instead. In this way, the governing equations themselves encode both the existence and the limitations of the conical flow solution.

