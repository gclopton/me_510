# Equation Index — Anderson, Chapter 2







# Calorically perfect gas internal energy


> [!question]
> (a) Write the expression for the internal energy per unit mass of a calorically perfect gas.
> (b) What is the central assumption this model makes about the gas, and what does it imply about the relationship between internal energy and temperature?
> (c) Real gases have energy modes (translation, rotation, vibration) that can activate at high temperatures. How does this model treat those modes, and when might that treatment break down?




> [!equation] Calorically perfect gas internal energy
> $$
> e=c_v T
> $$

This equation defines a **Linear Energy Storage Model** for a gas. It assumes that the gas’s capacity to absorb and store internal energy—via molecular translation, rotation, and vibration—remains constant regardless of how hot or cold the gas becomes. Think of the gas as a battery with a **Fixed Storage Capacity** ($c_v$). For every degree you raise the temperature, the internal energy "account" ($e$) increases by exactly the same amount. While real gases have "hidden" energy modes that activate at very high temperatures (vibration), this model treats the gas as having a simple, predictable thermal behavior.

| Expression | Name                            | Description                                                           |
| ---------- | ------------------------------- | --------------------------------------------------------------------- |
| $e$        | Internal energy per unit mass   | Thermodynamic internal energy of the gas (per unit mass).             |
| $c_v T$    | Calorically perfect-gas closure | For constant $c_v$, internal energy varies linearly with temperature. |



# Energy contained inside the control volume


> [!question]
> (a) Write the expression for the total energy contained inside a control volume. Identify the two forms of energy included in the integrand and explain what each represents physically.
> (b) What role does density play in the integrand, and why is it necessary for the integration to work?
> (c) If the properties inside the control volume can be approximated as spatially uniform, what does the integral simplify to?
> (d) Under what physical conditions might you drop the kinetic energy term, and what does the total specific energy reduce to in that case?



> [!equation] Energy contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> $$

This is the instantaneous "snapshot" of all energy currently stored within the fixed spatial boundaries of the control volume. It sums up both the microscopic (thermal) and macroscopic (motion) energy of every fluid particle inside the region.


| **Expression**                                  | **Name**                  | **Description**                                                                                        |
| ----------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------ |
| $\mathscr{V}$                                   | **Control Volume**        | The fixed physical region in space where the energy is being tallied.                                  |
| $\rho$                                          | **Density**               | The "conversion factor" that turns energy-per-mass into energy-per-volume for the spatial integration. |
| $e$                                             | **Internal Energy**       | The microscopic energy stored in the molecular "jiggling" and bonds of the gas.                        |
| $\frac{V^2}{2}$                                 | **Kinetic Energy**        | The macroscopic energy associated with the bulk motion (velocity) of the fluid.                        |
| $e+\frac{V^2}{2}$                               | **Total Specific Energy** | The complete energy "package" carried by a single unit of mass.                                        |
| $\iiint_{\mathscr{V}}\rho(\dots)\,d\mathscr{V}$ | **Total Energy Stored**   | The volume integral that sums the local energy density into a single scalar value (Joules or ft-lb).   |


## Assumptions and Simplifications

1. **Uniform Properties Inside $\mathscr{V}$.** If the properties inside the control volume can be approximated as spatially uniform (a "lumped" model), the integral collapses to a simple product:

$$
\iiint_{\mathcal{Y}} \rho\left(e+\frac{V^2}{2}\right) d \mathscr{V} \approx \rho\left(e+\frac{V^2}{2}\right) \mathscr{V}
$$


This is sometimes useful for filling/emptying tank problems or simplified system models.
2. **Negligible Kinetic Energy.** In problems where the fluid inside the control volume is nearly stationary or moving very slowly (e.g., a pressurized storage tank), the kinetic energy term $V^2 / 2$ may be negligible compared to $e$, reducing the total specific energy to just the internal energy.





# Ideal Gas Linkage Equation (Equation of State)


> [!Question]
> (a) Write the ideal gas equation of state in terms of density and the specific gas constant.
> (b) What is the fundamental role this equation plays in connecting the governing equations of fluid dynamics? Which two sets of properties does it bridge?
> (c) The specific gas constant R is defined in terms of two quantities. What are they, and why does R differ from one gas to another?
> (d) Why must temperature be expressed in absolute units (Kelvin or Rankine) rather than Celsius or Fahrenheit for this equation to work?


> [!equation] Ideal Gas Linkage Equation (Equation of State)
> $$
> p=\rho R T
> $$

This is the Linkage Equation that couples the mechanical properties (pressure/density) to the thermal properties (temperature). It provides the "bridge" that allows the Energy Equation to talk to the Momentum Equation.


| **Expression** | **Name**                  | **Description**                                                                                                            |
| -------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| $p$            | **Static Pressure**       | The normal force per unit area exerted by the molecular collisions of the gas.                                             |
| $\rho$         | **Mass Density**          | The "crowdedness" of the molecules; the amount of matter packed into a unit volume.                                        |
| $R$            | **Specific Gas Constant** | A property-specific constant ($R = \mathcal{R}/M$) that accounts for the molecular weight of the specific gas (e.g., Air). |
| $T$            | **Absolute Temperature**  | The measure of the average kinetic energy of the molecules (must be in Kelvin or Rankine).                                 |
| $\rho R T$     | **State Coupling**        | The mathematical product that defines the internal pressure required to maintain a specific density and temperature.       |




#  Control Volume Power Balance (Eq. 2.12)


> [!question]
> (a) Write the general form of the control volume power balance and identify what each of the three terms represents physically. What kind of quantities are all three terms (i.e., what are their dimensions)?
> (b) If the total power input exceeds the net energy flux leaving the control volume, what must be happening inside the volume?
> (c) What two physical phenomena are excluded from the standard form of this equation due to the inviscid flow assumption? What must be restored if viscous effects matter?
> (d) Under what conditions can you set the net heating power to zero, and what is this assumption called?
> (e) If the flow is steady, which part of the total rate of energy change drops out, and what survives?
> (f) To reduce the steady-flow form down to the familiar thermodynamics equation involving enthalpy, two additional steps are required beyond dropping the time derivative. What are they, and why does enthalpy appear in place of internal energy?


> [!equation] Control Volume Power Balance (Eq. 2.12)
> $$
> B_1+B_2=B_3
> $$

This equation represents the "Global Energy Budget" for a fixed region of space. It states that the total rate at which energy is being supplied to the fluid via heat and work must be perfectly balanced by the rate at which the fluid's total energy changes as it passes through the system. Think of this as a Power Balance. Since all terms are rates (Energy per unit time), this describes the energy "current" flowing in and out of your system. If the energy "pumped in" ($B_1 + B_2$) exceeds the energy "flowing out" (part of $B_3$), then energy must be accumulating inside the volume (the other part of $B_3$).


| **Expression** | **Name**                        | **Description**                                                                                                                        |
| -------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| $B_1$          | **Net Heating Power**           | The total rate of heat transfer (thermal energy) across the boundary into the fluid.                                                   |
| $B_2$          | **Net Mechanical Power**        | The total rate of work being done on the fluid by external forces (pressure, gravity, etc.).                                           |
| $B_3$          | **Total Rate of Energy Change** | The "Net Account Balance"—combines the rate of energy storage within the volume and the net rate of energy flux across the boundaries. |
| $B_1+B_2$      | **Total Power Input**           | The combined "push" of thermal and mechanical energy entering the fluid system from the surroundings.                                  |




## Simplifying Assumptions

1. Inviscid Flow. Eq. 2.20 assumes no viscous stresses act on the control surface. Consequently, there is no work done by viscous shear or normal stresses, and no heat transfer by thermal conduction or diffusion across the boundary. If viscous effects matter (e.g., boundary-layer flows, duct flows with significant friction), the generalized form Eq. 2.20a must be used, which adds the $\dot{W}_{\text {viscous }}$ and full $\dot{Q}$ terms.
2. No Shaft Work. Eq. 2.20 contains no $\dot{W}_{\text {shaft }}$ term. If a rotating shaft crosses the control surface (as in a turbine or compressor), the shaft work term must be restored from Eq. 2.20a.
3. Chemical Energy Treated as Internal Energy. Energy released or absorbed by chemical reactions is not modeled as a separate volumetric heating source in $B_1$. Instead, it is incorporated into the internal energy $e$ of the gas mixture. This is a modeling choice, not a simplification-but it is important to recognize because some treatments of reacting flows handle this differently.

### Common Additional Simplifications

4. Adiabatic Assumption ( $B_1=0$ ). If the system is insulated or the fluid moves so quickly that heat exchange with the surroundings is negligible, set $B_1=0$. This is common in high-speed nozzle, diffuser, and turbine problems.
5. Steady-Flow Assumption. If the flow is steady, all local time derivatives vanish. The $\partial / \partial t$ volume integral in $B_3$ drops out, and only the surface flux integral survives. This reduces the equation to:

$$
B_1+B_2=\iint_S \rho\left(e+\frac{V^2}{2}\right) \mathbf{V} \cdot d \mathbf{S}
$$

> [!NOTE]
> To reach the familiar Steady-Flow Energy Equation from introductory thermodynamics, two further steps are required beyond just dropping the time derivative:
> (a) The pressure-work surface integral ( $-\iint p \mathbf{V} \cdot d \mathbf{S}$ ) must be combined with the internal energy flux using the enthalpy identity $h=e+p / \rho$. This absorbs the pressure work into the flux term, replacing $e$ with $h$.
> (b) The remaining surface integrals must be evaluated at discrete, one-dimensional inlet and exit stations with uniform properties. Only then does the equation collapse to:
> 
> $$
> \dot{Q}+\dot{W}=\dot{m} \Delta\left(h+\frac{V^2}{2}+g z\right)
> $$
> 
> 
> The appearance of enthalpy $h$ in place of ( $e+p / \rho$ ) is not trivial-it reflects the fact that pressure work on the fluid entering and leaving the control volume has been folded into the energy flux.

6. Negligible Gravitational Potential Energy. In most compressible-flow and aerodynamic applications, the $g z$ term is negligibly small compared to kinetic and thermal energy. It is typically dropped unless the problem involves large elevation changes (e.g., hydraulic systems, atmospheric columns). Note that the SFEE written above includes $g z$ for generality, but Eq. 2.20 as given in the text does not explicitly include it-gravity would enter through the body force term $\rho$ f if relevant.





# Integral continuity equation (Eq. 2.2)

> [!equation] Integral continuity equation (Eq. 2.2)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\, d\mathscr{V}+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}=0
> $$

The net rate of change of mass within a fixed region of space is determined by the balance between internal mass accumulation and the net flow of mass crossing the boundary. This is a mass "budget." Since mass cannot be created or destroyed, any mass exiting the boundary must result in an equal depletion of the mass stored inside.



| **Expression**                                                       | **Name**         | **Description**                                                                                                     |
| -------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| $\rho(\mathbf{V} \cdot d\mathbf{S})$                                 | **Mass Flux**    | The building block of all flux terms; represents mass flow per unit time through an area element.                   |
| $\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\, d\mathscr{V}$ | **Storage Term** | The time-rate of change (accumulation or depletion) of the total mass inventory inside the volume.                  |
| $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$                         | **Net Outflow**  | The total mass crossing the surface. Positive values denote net loss (outflow); negative denotes net gain (inflow). |


## Assumptions and Simplifications

1. **Steady-Flow Assumption.** If the flow is steady, all local time derivatives vanish. The storage term drops out entirely, leaving:

$$
\iint_S \rho \mathbf{V} \cdot d \mathbf{S}=0
$$


This states that the net mass flux across the control surface is exactly zero - what flows in must flow out. For a duct or streamtube with a single inlet (station 1) and a single exit (station 2) with uniform properties at each, this reduces to:

$$
\rho_1 V_1 A_1=\rho_2 V_2 A_2=\dot{m}
$$

2. **Incompressible Flow ( $\rho=$ const).** If the fluid density is constant, $\rho$ factors out of every integral. The steady-flow continuity equation then simplifies to a purely kinematic constraint:

$$
\iint_S \mathbf{V} \cdot d \mathbf{S}=0
$$


For a duct with one inlet and one exit this gives $V_1 A_1=V_2 A_2$.

> [!NOTE]
> Incompressible $\neq$ Steady $>$ Setting $\rho=$ const and assuming steady flow are independent simplifications. An incompressible flow can still be unsteady (e.g., water hammer), in which case the storage term vanishes anyway (since $\partial \rho / \partial t=0$ when $\rho$ is constant), but the velocity field is still time-dependent.


3. **One-Dimensional Uniform Flow at Inlets/Exits.** The integral form requires evaluation over the entire control surface. In practice, the surface is decomposed into solid walls (where $\mathbf{V} \cdot d \mathbf{S}=0$ for impermeable boundaries) and discrete inlet/exit cross-sections where properties are assumed uniform. Only then do the surface integrals collapse to algebraic products like $\rho V A$.



# Generalized Integral Energy Equation (Eq. 2.20a)

> [!equation] Generalized Integral Energy Equation (Eq. 2.20a)
> $$
> \dot{Q}+\dot{W}_{\text {shaft}}+\dot{W}_{\text {viscous}}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> =\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho\left(e+\frac{V^{2}}{2}\right)\, d \mathscr{V}
> +\iint_{S} \rho\left(e+\frac{V^{2}}{2}\right) \mathbf{V} \cdot d \mathbf{S}
> $$

This is the most comprehensive form of the Power Balance for a control volume. It states that the total rate of energy entering the system—via heat, mechanical shafts, friction, and work done by pressure or gravity—must exactly equal the rate at which energy is stored inside the volume plus the net rate at which energy is carried out by the flowing fluid.



| **Expression**                                            | **Name**                   | **Description**                                                                                |
| --------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------- |
| $\dot{Q}$                                                 | **Net Heating Power**      | The rate of heat addition from all external sources (conduction, radiation, etc.).             |
| $\dot{W}_{\text{shaft}} + \dot{W}_{\text{viscous}}$       | **External Work Power**    | Power added via mechanical components (like a turbine shaft) or boundary friction.             |
| $-p(\mathbf{V} \cdot d\mathbf{S})$                        | **Pressure Power**         | The rate of work done on the fluid by pressure forces as it crosses the boundary.              |
| $(\rho\mathbf{f} \cdot \mathbf{V}) d\mathscr{V}$          | **Body Force Power**       | The rate of work done by "action-at-a-distance" forces (like gravity) on the moving fluid.     |
| $\frac{\partial}{\partial t}\iiint \rho E_t d\mathscr{V}$ | **Rate of Energy Storage** | The unsteady accumulation (or depletion) of energy inventory within the volume.                |
| $\iint \rho E_t (\mathbf{V} \cdot d\mathbf{S})$           | **Convective Energy Flux** | The rate at which the fluid "convection" carries its total energy "package" out of the system. |


## Assumptions and Simplifications


1. **Continuum and Local Thermodynamic Equilibrium.** The equation assumes the fluid can be described by continuous field variables ( $p, \rho, T, \mathbf{V}, e$ ) that are well-defined at every point. This fails in highly rarefied flows (high Knudsen number).
2. **No Gravitational Potential Energy as a Separate Storage Term.** Gravity enters only through the body force work term $\rho(\mathbf{f} \cdot \mathbf{V})$, not as a stored potential energy $g z$ in the volume integral. The two formulations are mathematically equivalent (one can be derived from the other), but this form keeps gravity on the "input" side of the balance rather than in the energy "inventory."
3. **Chemical Energy Absorbed into e.** Energy from chemical reactions is part of the internal energy $e$, not a separate source term in $\dot{Q}$. This is a modeling convention consistent with the treatment throughout the text (discussed further in Chapters 16-17).

_Reduction to the Inviscid Form (Eq. 2.20)_
4. Inviscid Flow → Drop $\dot{W}_{\text {viscous }}$ and Conduction/Diffusion from $\dot{Q}$. If viscous effects are negligible, there is no work done by viscous stresses on the control surface, and heat transfer by conduction and diffusion across the boundary vanishes. The heating term $\dot{Q}$ reduces to just volumetric heating $\iiint \dot{q} \rho d \mathscr{V}$ (radiation only). This yields Eq. 2.20.
5. No Shaft Work → Drop $\dot{W}_{\text {shaft }}$. If no rotating machinery crosses the control surface, this term is zero. Combined with assumption 4, this completes the reduction from Eq. 2.20a to Eq. 2.20.

_Further Common Simplifications (Applied to Either Form)_
6. Adiabatic ( $\dot{Q}=0$ or $B_1=0$ ). If there is no heat transfer of any kind - no radiation, no conduction, no diffusion - the entire heating term drops out. Common in high-speed nozzle and turbine problems where transit time is too short for significant heat exchange.
7. Steady Flow. The $\partial / \partial t$ storage integral vanishes, leaving only flux and work terms. The equation becomes:

$$
\dot{Q}+\dot{W}_{\text {shaft }}+\dot{W}_{\text {viscous }}-\iint_S p \mathbf{V} \cdot d \mathbf{S}+\iiint_{\mathcal{Y}} \rho(\mathbf{f} \cdot \mathbf{V}) d \mathcal{V}=\iint_S \rho\left(e+\frac{V^2}{2}\right) \mathbf{V} \cdot d \mathbf{S}
$$

8.1-D Uniform Inlet/Exit + Enthalpy Substitution. Evaluating the surface integrals at discrete stations with uniform properties, and combining the pressure work integral with the internal energy flux using $h=e+p / \rho$, produces the classical Steady-Flow Energy Equation:

$$
\dot{Q}+\dot{W}_{\text {shaft }}=\dot{m} \Delta\left(h+\frac{V^2}{2}+g z\right)
$$

> [!NOTE]
> The Enthalpy Step Is Not Trivial > The appearance of $h$ in the SFEE is the result of absorbing the pressure-work surface integral into the convective flux. The pressure work $\left(-\iint p \mathbf{V} \cdot d \mathbf{S}\right)$ evaluated at an inlet or exit gives $p V A= p(\dot{m} / \rho)$, which when added to $e \dot{m}$ gives $(e+p / \rho) \dot{m}=h \dot{m}$. This is why enthalpy not internal energy - is the natural energy variable for open systems.

9. **Negligible Gravity ( $g z \approx 0$ ).** In most compressible-flow applications, potential energy changes are tiny compared to kinetic and thermal energy. Dropping $g z$ (or equivalently, setting $\mathbf{f}=0$ ) is standard unless large elevation changes are involved.




# Inviscid Integral Energy Equation (Eq. 2.20)

> [!equation] Inviscid Integral Energy Equation (Eq. 2.20)
> $$
> \iiint_{\mathscr{V}} \dot{q}\, \rho\, d \mathscr{V}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> =\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho\left(e+\frac{V^{2}}{2}\right)\, d \mathscr{V}
> +\iint_{S} \rho\left(e+\frac{V^{2}}{2}\right) \mathbf{V} \cdot d \mathbf{S}
> $$

This equation is the Inviscid Power Balance. It states that for a fluid without friction, the total power added by volumetric heat, pressure work, and body forces must equal the rate at which energy is stored within the volume plus the net rate at which energy is carried away by the flow. This is a simplified version of the First Law of Thermodynamics that ignores "sticky" viscous forces and mechanical shafts. It describes how the energy "inventory" of a fluid changes purely through thermal inputs ($\dot{q}$) and basic mechanical "pushing" (pressure and gravity).


| **Expression**                                            | **Name**                  | **Description**                                                                                                                    |
| --------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| $E_t = e + \frac{V^2}{2}$                                 | **Total Specific Energy** | The complete energy "package" per unit mass, combining microscopic internal energy ($e$) and macroscopic kinetic energy ($V^2/2$). |
| $\iiint_{\mathscr{V}} \dot{q} \rho \, d\mathscr{V}$       | **Volumetric Heating**    | The rate of energy added internally, such as from radiation or chemical heat release.                                              |
| $-p(\mathbf{V} \cdot d\mathbf{S})$                        | **Pressure Power**        | The rate of work done on the fluid by pressure forces as mass crosses the boundaries.                                              |
| $\rho(\mathbf{f} \cdot \mathbf{V})$                       | **Body Force Power**      | The rate of work done by "action-at-a-distance" forces (like gravity) on the moving fluid particles.                               |
| $\frac{\partial}{\partial t}\iiint \rho E_t d\mathscr{V}$ | **Energy Storage**        | The unsteady accumulation (or depletion) of the total energy inventory inside the volume.                                          |
| $\iint \rho E_t (\mathbf{V} \cdot d\mathbf{S})$           | **Energy Flux**           | **Convective Transport:** The rate at which the flow "carries" its total energy package out of the system.                         |


## Assumptions and Simplifications


1. Inviscid Flow. No viscous stresses act on the control surface. This eliminates both the work done by viscous shear/normal stresses $\left(\dot{W}_{\text {viscous }}=0\right)$ and heat transfer by thermal conduction and diffusion across the boundary. The only heating mechanism retained is volumetric heating $\dot{q}$ (e.g., radiation absorption/emission).
2. No Shaft Work. No rotating machinery crosses the control surface ( $\dot{W}_{\text {shaft }}=0$ ). If a turbine or compressor shaft penetrates the boundary, Eq. 2.20a must be used instead.
3. Chemical Energy Absorbed into e. Energy from chemical reactions is not a separate source in the $\dot{q}$ term. It is folded into the internal energy $e$ of the gas mixture - a modeling convention discussed in Chapters 16-17.
4. No Gravitational Potential Energy as Separate Storage. Gravity enters only through the body force work term $\rho(\mathbf{f} \cdot \mathbf{V})$, not as a stored $g z$ term in the volume integral. The two formulations are mathematically equivalent, but this form keeps gravity on the "input" side.

5. Adiabatic $(\vec{q}=0)$. If there is no volumetric heating (no radiation, no internal energy sources), the entire first term drops out. Common in high-speed nozzle and diffuser problems.
6. Steady Flow. The $\partial / \partial t$ storage integral vanishes. Only flux and work terms survive:

$$
\iiint_{\mathcal{Y}} \dot{q} \rho d \mathcal{Y}-\iint_S p \mathbf{V} \cdot d \mathbf{S}+\iiint_{\mathcal{Y}} \rho(\mathbf{f} \cdot \mathbf{V}) d \mathcal{Y}=\iint_S \rho\left(e+\frac{V^2}{2}\right) \mathbf{V} \cdot d \mathbf{S}
$$

7.1-D Uniform Inlet/Exit + Enthalpy Substitution. Evaluating surface integrals at discrete stations with uniform properties and using $h=e+p / \rho$ to absorb the pressure work into the flux gives the inviscid, no-shaft-work form of the SFEE:

$$
\dot{q} \dot{m}=\dot{m} \Delta\left(h+\frac{V^2}{2}\right)
$$

> [!NOTE]
> Why Enthalpy Appears $>$ The pressure work $\left(-\iint p \mathbf{V} \cdot d \mathbf{S}\right)$ evaluated at an inlet or exit yields $p(\dot{m} / \rho)$. Adding this to the internal energy flux em gives $(e+p / \rho) \dot{m}=h \dot{m}$. Enthalpy is therefore the natural energy variable for open systems - it packages internal energy and flow work together.

8. Negligible Body Forces. In most aerodynamic and compressible-flow problems, gravitational work is negligible compared to pressure work and kinetic energy changes. Setting $\mathbf{f}=0$ removes the body force integral entirely.





# Integral momentum equation (inviscid) (Eq. 2.11)

> [!equation] Integral momentum equation (inviscid) (Eq. 2.11)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}
> +\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}
> =\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_{S} p\, d \mathbf{S}
> $$


This is essentially $F = ma$ for a region of space. It says: (Local change in momentum) + (Momentum carried away by the flow) = (The net push from gravity/body forces) + (The net push from pressure). 


| Expression | Name | Description |
| --- | --- | --- |
| $\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}$ | Momentum storage term | Unsteady accumulation of momentum inside the control volume. |
| $\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}$ | Momentum flux term | Net convective transport of momentum across the control surface. |
| $\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}$ | Body-force term | Net body force acting on the control-volume fluid. |
| $-\iint_{S} p\, d \mathbf{S}$ | Pressure-force term | Net surface force due to pressure (pressure acts inward, $d\mathbf{S}$ points outward). |



## Assumptions and Simplifications



1. Inviscid Flow. The only surface force retained is pressure. All viscous contributions shear stresses and viscous normal stresses acting on the control surface - are neglected. If friction matters (e.g., boundary layers, duct flows, wakes), the viscous form Eq. 2.11a must be used.
2. Continuum Assumption. The equation treats $\rho, \mathbf{V}$, and $p$ as continuous field variables, requiring that the fluid element is large enough to contain many molecules. This fails in highly rarefied flows (high Knudsen number).

Common Additional Simplifications
3. Steady Flow. The momentum storage term $\partial / \partial t \iiint \rho \mathbf{V} d \mathcal{V}$ vanishes, leaving:

$$
\iint_S(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}=\iiint_{\mathcal{Y}} \rho \mathbf{f} d \mathcal{V}-\iint_{\mathcal{S}} p d \mathbf{S}
$$


This is the form used in the thrust derivation (Section 2.7) and many practical duct/nozzle problems.
4. No Body Forces ( $\mathbf{f}=0$ ). In most aerodynamic applications, gravitational forces on the fluid are negligible compared to pressure forces and momentum fluxes. Dropping the body force integral gives:

$$
\iint_S(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}=-\iint_S p d \mathbf{S}
$$

5.1-D Uniform Inlet/Exit. Decomposing the control surface into impermeable walls ( $\mathbf{V}$. $d \mathbf{S}=0$ ) and discrete stations with uniform $\rho$, $V$, and $p$ converts the surface integrals into algebraic terms. For a single-inlet, single-exit duct (steady, no body forces), the $x$ component becomes:

$$
\dot{m} V_{x, \text { out }}-\dot{m} V_{x, \text { in }}=\left(p_{\text {in }} A_{\text {in }}-p_{\text {out }} A_{\text {out }}\right)_x+F_{\text {surface }, x}
$$

where $F_{\text {surface, } x}$ is the net pressure force from the solid walls - the quantity that becomes the thrust in propulsion applications.


> [!NOTE]
> The integral momentum equation lets you calculate net forces (like engine thrust) without knowing the detailed pressure distribution inside the control volume. The complex internal pressure field is "buried" inside the volume - only conditions at the inlets, exits, and the net wall force appear explicitly. This is the key advantage demonstrated in the thrust derivation of Eq. 2.45.




# Integral momentum equation (with viscous surface force) (Eq. 2.11a)

> [!equation] Integral momentum equation (with viscous surface force) (Eq. 2.11a)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}
> +\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}
> =\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_{S} p\, d \mathbf{S}+\mathbf{F}_{\text{viscous}}
> $$


This is Newton’s Second Law ($F=ma$) applied to a fixed region of fluid. It states that the total external forces acting on the fluid (body forces, pressure, and friction) must equal the rate at which momentum is physically stored within the volume plus the net rate at which momentum is carried across the boundaries by the flow itself.


| **Expression**                                                                   | **Name**                  | **Description**                                                                                                                                           |
| -------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}$ | **Momentum Storage**      | Represents the "local" change in momentum due to unsteady fluctuations (e.g., a starting engine).                                                         |
| $(\rho \mathbf{V} \cdot d \mathbf{S})\mathbf{V}$                                 | **Momentum Flux**         | **Convective Transport:** The rate at which the flow "carries" its own momentum across the surface $S$.                                                   |
| $\rho \mathbf{f}$                                                                | **Body Force Density**    | The "action at a distance" forces (like gravity) acting on every unit of mass inside the volume.                                                          |
| $-p d\mathbf{S}$                                                                 | **Pressure Force**        | The surface force pushing **inward** on the fluid. The negative sign is required because pressure acts against the outward-pointing vector $d\mathbf{S}$. |
| $\mathbf{F}_{\text{viscous}}$                                                    | **Viscous Surface Force** | The net result of internal friction (shear stresses) acting on the boundary; this term is zero in the **inviscid** approximation (Eq. 2.11).              |


## Assumptions and Simplifications


1. No Assumptions on Viscosity—This Is the General Form. Unlike Eq. 2.11, viscous surface forces are explicitly retained through $\mathbf{F}_{\text {viscous }}$, which represents the net integral of shear and viscous normal stresses over the entire control surface. This makes Eq. 2.11a valid for both inviscid and viscous flows.
2. $\mathrm{F}_{\text {viscous }}$ Is a Lumped Term. The viscous contribution appears as a single resultant vector, not as a detailed stress distribution. To evaluate it in practice, you either need the full viscous stress tensor integrated over $S$, or you treat it as an unknown to be determined (e.g., as drag in an external flow problem).
3. Continuum and Local Equilibrium. As with Eq. 2.11, the equation assumes continuous field variables and local thermodynamic equilibrium.

Reduction to the Inviscid Form (Eq. 2.11)
4. Inviscid Approximation → Drop $\mathbf{F}_{\text {viscous. }}$ Setting $\mathbf{F}_{\text {viscous }}=0$ recovers Eq. 2.11 exactly. This is valid when viscous stresses on the control surface are negligible - typically when the surface is placed in regions of irrotational flow away from boundary layers and wakes.

Common Additional Simplifications
5. Steady Flow. The momentum storage term vanishes:

$$
\iint_S(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}=\iiint_{\mathcal{Y}} \rho \mathbf{f} d \mathcal{Y}-\iint_S p d \mathbf{S}+\mathbf{F}_{\text {viscous }}
$$


6. No Body Forces. Dropping $\rho$ f when gravity is negligible.
7.1-D Uniform Inlet/Exit. Same decomposition as for Eq. 2.11, but now the force balance on a duct includes both pressure and viscous wall contributions:

$$
\dot{m}\left(V_{\text {out }}-V_{\text {in }}\right)=\left(p_{\text {in }} A_{\text {in }}-p_{\text {out }} A_{\text {out }}\right)+F_{\text {pressure, walls }}+F_{\text {viscous, walls }}
$$

> [!NOTE]
> When Does $\mathbf{F}_{\text {viscous }}$ Matter? $>$ For external aerodynamics, $\mathbf{F}_{\text {viscous }}$ contributes skin-friction drag. For internal flows (pipes, ducts), it represents frictional pressure losses along the walls. In both cases, it acts to decelerate the flow and dissipate mechanical energy into heat. If you are computing drag on a body using a control volume, you generally *need* this term - it is only safe to drop it when the control surface is entirely in an inviscid region.





# Mass contained inside the control volume

> [!equation] Mass contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\, d\mathscr{V}
> $$

This integral calculates the instantaneous "Mass Inventory" of the fluid currently residing within the fixed boundaries of the control volume. It is the three-dimensional sum of the fluid density across every point in the region. Think of this as the "Scale Weight" of the control volume. If the fluid is compressible, this total mass can change over time as the gas is packed more tightly or thinned out. For an incompressible fluid with a fixed volume, this value remains constant.


| **Expression**                            | **Name**                 | **Description**                                                                                                       |
| ----------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| $\rho$                                    | **Density**              | The local mass per unit volume; determines how much matter exists at a specific point.                                |
| $d\mathscr{V}$                            | **Differential Volume**  | The infinitesimal "building block" of the total volume used for the integration.                                      |
| $\iiint_{\mathscr{V}}\rho\, d\mathscr{V}$ | **Total Mass Inventory** | The volume integral that converts local density into the total scalar amount of mass (kg or slugs) inside the system. |


## Assumptions and Simplifications


# Mass flow through an elemental surface (Eq. 2.1)

> [!equation] Mass flow through an elemental surface (Eq. 2.1)
> $$
> \dot{m}=\rho(V\cos\theta)\, dS=\rho V_n\, dS=\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

This equation defines the "gatekeeper" of mass transfer. It calculates the rate at which mass crosses a tiny, oriented patch of a surface. The flow rate is determined by the fluid's density and only the portion of the velocity vector that is pushing directly through the surface (the normal component). Think of a window in a windstorm. If the wind blows parallel to the glass, no air enters the room. Only the "normal" component of the wind actually crosses the threshold. The dot product $\mathbf{V} \cdot d\mathbf{S}$ mathematically filters out any "glancing" motion, leaving only the flow that contributes to the mass budget.


| **Expression**                      | **Name**                      | **Description**                                                                                                           |
| ----------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| $\dot{m}$                           | **Elemental Mass Flow**       | The specific "slice" of mass per unit time (e.g., kg/s) crossing the area $dS$.                                           |
| $V \cos\theta$                      | **Normal Velocity Component** | The magnitude of velocity projected onto the surface normal; $\theta$ is the angle between $\mathbf{V}$ and $\mathbf{n}$. |
| $V_n$                               | **Normal Speed**              | A shorthand notation for the velocity component perpendicular to the surface.                                             |
| $d\mathbf{S} = \mathbf{n} dS$       | **Area Vector**               | A vector combining the size of the patch ($dS$) and its orientation in space ($\mathbf{n}$).                              |
| $\rho \mathbf{V} \cdot d\mathbf{S}$ | **Vector Flux Form**          | The most compact representation; the dot product automatically handles the geometry and direction (positive for outflow). |


## Assumptions and Simplifications


# Mechanical power (rate of doing work on a moving body)

> [!equation] Mechanical power (rate of doing work on a moving body)
> $$
> \dot{W}=\mathbf{F}\cdot\mathbf{V}
> $$

This equation defines the rate at which mechanical energy is transferred to a moving body or fluid element by an external force. It states that power is the product of the force and the velocity of the point where that force is applied. Think of this as the "Effective Push." If you push a heavy box but it doesn't move ($V=0$), you are doing zero work. If you push perpendicular to the direction of motion, you are also doing zero work. The dot product $\mathbf{F} \cdot \mathbf{V}$ mathematically extracts only the portion of the force that is actually "driving" or "resisting" the motion.


| **Expression**              | **Name**             | **Description**                                                                               |
| --------------------------- | -------------------- | --------------------------------------------------------------------------------------------- |
| $\dot{W}$                   | **Mechanical Power** | The instantaneous rate of energy transfer (e.g., Watts or ft-lb/s).                           |
| $\mathbf{F}$                | **Force Vector**     | The magnitude and direction of the external push or pull (e.g., pressure or gravity).         |
| $\mathbf{V}$                | **Velocity Vector**  | The speed and direction of the fluid element or surface at the point of application.          |
| $\mathbf{F}\cdot\mathbf{V}$ | **Power Projection** | The scalar result showing that only the force component parallel to the motion performs work. |



## Assumptions and Simplifications


# Momentum contained inside the control volume

> [!equation] Momentum contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

This integral represents the instantaneous Total Momentum Vector of all the fluid currently residing within the fixed boundaries of the control volume. It is the three-dimensional sum of the mass-weighted velocity of every fluid particle in the region. Think of this as the "Net Inertia" of the system. In a steady-state flow, the fluid inside the box might be moving, but the _total_ momentum vector stored in the box doesn't change over time. If the flow is unsteady (like a gust of wind hitting a building), this "Momentum Inventory" fluctuates as the fluid inside speeds up, slows down, or changes direction.


| **Expression**                                        | **Name**                     | **Description**                                                                                                                            |
| ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| $\rho \mathbf{V}$                                     | **Momentum Density**         | The local momentum per unit volume; represents the "pushing power" of the fluid at a specific point.                                       |
| $d\mathscr{V}$                                        | **Differential Volume**      | The infinitesimal "building block" of the total region $\mathscr{V}$ used for the integration.                                             |
| $\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$ | **Total Momentum Inventory** | The volume integral that converts local momentum density into a single resultant vector (e.g., kg·m/s or slug·ft/s) for the entire system. |


## Assumptions and Simplifications



# Momentum flux across the control surface (Eq. 2.8)

> [!equation] Momentum flux across the control surface (Eq. 2.8)
> $$
> \mathbf{A}_1=\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}
> $$


This integral calculates the net rate at which momentum is physically "carried" across the boundaries of the control volume by the moving fluid. It represents the convective transport of momentum—essentially how much "pushing power" enters or leaves the system through the flow itself. Think of the flow as a Conveyor Belt. Each unit of mass crossing the surface is "carrying" its own momentum vector with it. The term in the parentheses $(\rho \mathbf{V} \cdot d\mathbf{S})$ acts as the "Mass Flow Filter," determining how much mass is crossing. This mass is then multiplied by its velocity ($\mathbf{V}$) to find the total momentum transfer. In a jet engine, the fact that the exit momentum flux is much higher than the inlet momentum flux is exactly what generates thrust.


| **Expression**                                  | **Name**                   | **Description**                                                                                                   |
| ----------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| $\rho \mathbf{V} \cdot d\mathbf{S}$             | **Differential Mass Flow** | The amount of mass per unit time crossing the surface element; it determines the "strength" of the conveyor belt. |
| $(\rho \mathbf{V} \cdot d\mathbf{S})\mathbf{V}$ | **Convective Momentum**    | The momentum per unit time being transported through a specific patch of the surface.                             |
| $\iint_{S} (\dots)$                             | **Net Momentum Flux**      | The surface integral that sums all momentum crossing into or out of the volume.                                   |
| $\mathbf{A}_1$                                  | **Convection Term**        | The mathematical shorthand for the total momentum transport used in the momentum balance equation.                |



## Assumptions and Simplifications








# Net mass flow into a fixed control volume

> [!equation] Net mass flow into a fixed control volume
> $$
> -\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

This integral calculates the total rate at which mass is entering a fixed region of space. By placing a negative sign in front of the standard surface integral, we flip the mathematical convention so that a positive result physically represents a **net gain** of mass. This is the "Deposit" side of the mass balance. Because the area vector $d\mathbf{S}$ is defined as pointing **outward**, the standard integral $\iint \rho \mathbf{V} \cdot d\mathbf{S}$ naturally calculates "Net Outflow." To find how much is actually coming _into_ the box to increase the internal inventory, we negate that value.

| Expression | Name | Description |
| --- | --- | --- |
| $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$ | Net outflow rate | Positive when the net flow is outward. |
| $-\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$ | Net inflow rate | Same magnitude with sign flipped to represent inflow. |

| **Expression**                                | **Name**                 | **Description**                                                                                     |
| --------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------- |
| $\rho\,\mathbf{V}\cdot d\mathbf{S}$           | **Differential Outflow** | The infinitesimal mass flow rate through a patch $dS$. Positive if the fluid is leaving the volume. |
| $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$  | **Net Outflow Rate**     | The total "Withdrawal" rate of mass from the control volume.                                        |
| $-\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$ | **Net Inflow Rate**      | The total "Deposit" rate; mathematically equivalent to (Mass In - Mass Out).                        |




# Net rate of energy flow across the control surface (Eq. 2.17)

> [!equation] Net rate of energy flow across the control surface (Eq. 2.17)
> $$
> \iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)
> $$

This integral represents the net rate at which total energy is "carried" across the boundaries of a fixed region by the fluid motion. It is the product of the mass flow rate and the specific total energy (internal plus kinetic) associated with that mass. Think of the flow as a **Thermal Conveyor Belt**. Every gram of fluid crossing the surface carries an energy "package" containing its microscopic heat ($e$) and its macroscopic motion ($V^2/2$). The term $(\rho \mathbf{V} \cdot d\mathbf{S})$ acts as the gatekeeper, determining how much mass crosses, while the $\left(e + \frac{V^2}{2}\right)$ term defines the energy density of that mass.


| **Expression**                             | **Name**                   | **Description**                                                                                                |
| ------------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| $\rho \mathbf{V} \cdot d\mathbf{S}$        | **Differential Mass Flow** | The rate of mass transfer through a surface element; dictates the "volume" of energy transport.                |
| $e + \frac{V^2}{2}$                        | **Total Specific Energy**  | The energy "content" per unit mass, including both heat and velocity.                                          |
| $(\rho \mathbf{V} \cdot d\mathbf{S})(E_t)$ | **Convective Energy Flux** | The instantaneous power being physically transported through a specific patch of the surface.                  |
| $\iint_{S} (\dots)$                        | **Net Energy Flux**        | The surface integral summing the energy "deposits" (inflow) and "withdrawals" (outflow) for the entire system. |



# Newton’s second law (constant mass) (Eq. 2.4)

> [!equation] Newton’s second law (constant mass) (Eq. 2.4)
> $$
> \mathbf{F}=m\frac{d\mathbf{V}}{dt}=m\mathbf{a}
> $$

This equation states that the net external force acting on a body of fixed mass is directly proportional to the rate at which its velocity changes over time. In this specific form, the mass is assumed to be an unchanging "lump" of matter. This is the classical "Push-Response" law. It defines how a body reacts to an external influence: the more mass a body has, the more force is required to change its state of motion. In the context of fluid mechanics, this is the foundational principle used to derive the more complex Momentum Equation, which must account for the fact that fluid "mass" is constantly flowing in and out of our region of interest.

| **Expression**           | **Name**                    | **Description**                                                                                     |
| ------------------------ | --------------------------- | --------------------------------------------------------------------------------------------------- |
| $\mathbf{F}$             | **Net Force**               | The vector sum of all external pushes and pulls (pressure, gravity, friction) acting on the mass.   |
| $m$                      | **Fixed Mass**              | The constant quantity of matter being accelerated.                                                  |
| $\frac{d\mathbf{V}}{dt}$ | **Rate of Velocity Change** | The instantaneous change in speed or direction of the mass over time.                               |
| $\mathbf{a}$             | **Acceleration**            | The kinematic result of the applied force; the "response" of the mass to the "push."                |
| $m\mathbf{a}$            | **Inertial Force**          | The product of mass and acceleration, representing the resistance of the body to changes in motion. |


# Newton’s second law (general form) (Eq. 2.3)

> [!equation] Newton’s second law (general form) (Eq. 2.3)
> $$
> \frac{d}{dt}(m\mathbf{V})=\mathbf{F}
> $$

This equation states that the net external force acting on a system is equal to the total time rate of change of its momentum. Unlike the simpler $F=ma$ form, this general version allows for the possibility that both the velocity _and_ the mass of the system can vary with time.

| **Expression**              | **Name**                    | **Description**                                                                                                                        |
| --------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| $m\mathbf{V}$               | **Momentum Vector**         | The "quantity of motion"; a vector combining the mass and its current velocity.                                                        |
| $\frac{d}{dt}(m\mathbf{V})$ | **Rate of Momentum Change** | The instantaneous change in the momentum inventory; mathematically, it expands to $m\frac{d\mathbf{V}}{dt} + \mathbf{V}\frac{dm}{dt}$. |
| $\mathbf{F}$                | **Net Force**               | The total external influence acting on the system from the surroundings.                                                               |




# Rate of work on the fluid due to body forces (Eq. 2.15)

> [!equation] Rate of work on the fluid due to body forces (Eq. 2.15)
> $$
> \iiint_{\mathscr{V}}\rho(\mathbf{f}\cdot\mathbf{V})\, d\mathscr{V}
> $$

This integral calculates the total power supplied to the fluid by "action-at-a-distance" forces, such as gravity or electromagnetism, acting throughout the entire control volume. It sums the rate of work done on every moving fluid particle within the region. Think of this as the Volumetric Power Input. Unlike pressure, which pushes only on the surface, body forces act on the "bulk" of the fluid. This term captures how much energy is being added to (or taken from) the fluid as it moves through a force field. For example, if a fluid is flowing upward against gravity, this term would represent the rate at which kinetic/internal energy is being converted into potential energy (a negative power input).


| **Expression**                              | **Name**                     | **Description**                                                                                  |
| ------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| $\mathbf{f}$                                | **Body Force per Unit Mass** | The local acceleration vector of the force field (e.g., gravity, $\mathbf{g}$).                  |
| $\rho \mathbf{f}$                           | **Force Density**            | The total force acting on a unit volume of fluid at a specific point.                            |
| $\mathbf{f} \cdot \mathbf{V}$               | **Specific Power**           | The rate of work done per unit mass; it is zero if the flow is perpendicular to the force.       |
| $\rho (\mathbf{f} \cdot \mathbf{V})$        | **Power Density**            | The mechanical power generated per unit volume at a specific point in space.                     |
| $\iiint_{\mathscr{V}} (\dots) d\mathscr{V}$ | **Total Body Force Power**   | The volume integral that tallies the power contributions from every point in the control volume. |


# Rate of work on the fluid due to pressure forces (Eq. 2.14)

> [!equation] Rate of work on the fluid due to pressure forces (Eq. 2.14)
> $$
> -\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}
> $$

This integral represents the total power delivered to the fluid by external pressure pushing against the moving boundaries of the control volume. It sums the rate of work done by the surroundings on the fluid at every point where the fluid crosses the control surface. Think of this as Boundary Power. For a fluid to enter or leave the "box," it must push (or be pushed by) the surrounding fluid. If the fluid is moving into the volume, the pressure is doing "positive work" on the system (pushing mass in). If the fluid is moving out, it must do work against the external pressure (pushing mass out), which represents an energy cost to the system. The negative sign is a mathematical correction because pressure pushes inward, while the area vector $d\mathbf{S}$ points outward.



| **Expression**                            | **Name**                     | **Description**                                                                                                    |
| ----------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| $p\,d\mathbf{S}$                          | **Pressure Force Vector**    | The force acting on a surface patch; it carries the magnitude of pressure and the direction of the outward normal. |
| $-p\,d\mathbf{S}$                         | **Inward Pressure Force**    | The actual physical force exerted on the fluid by the surroundings (directed into the volume).                     |
| $\mathbf{V} \cdot d\mathbf{S}$            | **Volumetric Flow Rate**     | The "speed" at which the volume is being swept across the boundary; positive for outflow.                          |
| $-p (\mathbf{V} \cdot d\mathbf{S})$       | **Elemental Pressure Power** | The rate of work done on a single patch of the surface; positive when fluid enters (inflow).                       |
| $-\iint_{S} p\mathbf{V}\cdot d\mathbf{S}$ | **Total Pressure Power**     | The surface integral that calculates the net power "pumped" into the fluid by pressure across the entire boundary. |



# Rocket thrust equation (special case of Eq. 2.45 with $\dot{m}_i=0$)

> [!equation] Rocket thrust equation (special case of Eq. 2.45 with $\dot{m}_i=0$)
> $$
> T=\dot{m}_{e} V_{e}+\left(p_{e}-p_{\infty}\right) A_{e}
> $$


This equation calculates the net force (thrust) generated by a rocket engine. It is composed of two distinct physical contributions: the high-speed "kick" from the mass of the exhaust gas being expelled, and the "push" caused by any difference between the gas pressure at the nozzle exit and the surrounding atmospheric pressure. Unlike a jet engine, a rocket carries all its propellant internally, so there is no "inlet drag" from incoming air. The thrust is purely an **Output Balance**. The first term is the **Momentum Thrust**—the reaction force from throwing mass backward. The second term is the **Pressure Thrust**—an additional boost that occurs if the gas is still "over-pressurized" ($p_e > p_\infty$) as it leaves the nozzle, effectively pushing against the exit area like a piston.


| **Expression**        | **Name**                 | **Description**                                                                                                          |
| --------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| $\dot{m}_e V_e$       | **Momentum Thrust**      | The primary force generated by the time-rate of change of momentum of the exhaust gas.                                   |
| $p_e - p_\infty$      | **Pressure Mismatch**    | The "Gage Pressure" at the exit; the difference between the internal exhaust pressure and the external ambient pressure. |
| $(p_e - p_\infty)A_e$ | **Pressure Thrust**      | The force resulting from the pressure mismatch acting over the entire exit plane area.                                   |
| $A_e$                 | **Exit Area**            | The cross-sectional area of the nozzle at the point where the gas is released into the atmosphere.                       |
| $\dot{m}_e$           | **Propellant Mass Flow** | The rate at which burned fuel and oxidizer are being converted into high-speed exhaust.                                  |



# Time rate of change of energy inside the control volume (Eq. 2.18)

> [!equation] Time rate of change of energy inside the control volume (Eq. 2.18)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> $$

This term represents the Unsteady Energy Storage Rate within the fixed spatial boundaries of the control volume. It tracks how the total "energy inventory"—the sum of all thermal and kinetic energy currently inside the box—is accumulating or depleting at a specific instant in time. Think of this as the Energy Inflation Rate for your system. In a steady-state process (like a jet engine running at a constant cruise speed), this term is zero because the amount of energy inside the engine doesn't change from one second to the next. However, during a transient event (like a rocket ignition or a sudden gust of wind), energy is being "packed" into or "drained" from the volume, and this term captures that time-dependent fluctuation.


| **Expression**                                 | **Name**                  | **Description**                                                                                             |
| ---------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| $\iiint_{\mathscr{V}}\rho E_t \, d\mathscr{V}$ | **Total Stored Energy**   | The instantaneous total energy "account balance" (internal + kinetic) currently residing inside the volume. |
| $\frac{\partial}{\partial t}(\dots)$           | **Local Time Derivative** | The rate at which the stored energy is changing purely due to time-varying flow conditions (unsteadiness).  |
| $\rho (e + \frac{V^2}{2})$                     | **Total Energy Density**  | The local energy per unit volume; determines the "weight" of the energy at each point in the integration.   |



# Total body force acting on the control volume (Eq. 2.5)

> [!equation] Total body force acting on the control volume (Eq. 2.5)
> $$
> \iiint_{\mathscr{V}}\rho\,\mathbf{f}\, d\mathscr{V}
> $$

This integral calculates the total "Action-at-a-Distance" force exerted on the entire mass of fluid currently residing within the control volume. It is the three-dimensional summation of the local force density—determined by the fluid's mass distribution—across the entire region. Unlike pressure or friction, which only "push" on the surface of the fluid, body forces like gravity, magnetism, or electrical fields act on every single molecule throughout the "bulk" of the volume. This term tells you the net result of those fields. If you were holding the control volume like a bucket, this integral would represent the "weight" (if the force is gravity) that you would feel in your hand.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\mathbf{f}$|**Body Force per Unit Mass**|The local acceleration vector of the force field (e.g., gravity, $\mathbf{g}$).|
|$\rho \mathbf{f}$|**Body Force Density**|The "Force per Volume"; represents how much force is applied to a specific point based on how much mass is packed there.|
|$d\mathscr{V}$|**Differential Volume**|The infinitesimal spatial element used to "sweep" through the entire region $\mathscr{V}$.|
|$\iiint_{\mathscr{V}} \dots d\mathscr{V}$|**Net Body Force**|The volume integral that tallies the contributions from every point to find the total resultant vector ($\mathbf{F}_{\text{body}}$).|



# Total force on the control volume (Eq. 2.7)

> [!equation] Total force on the control volume (Eq. 2.7)
> $$
> \mathbf{F}=\iiint_{\mathscr{V}}\rho\,\mathbf{f}\, d\mathscr{V}-\iint_{S}p\, d\mathbf{S}
> $$


This equation defines the Total External Influence acting on a fluid system. It splits the net force into two fundamental categories: forces that act through the "bulk" of the volume (body forces) and forces that "push" across the boundaries (surface pressure). In fluid dynamics, we don't have a single handle to pull on. Instead, we have to account for "Ghostly" forces like gravity that reach into the volume, and "Contact" forces like pressure that squeeze the fluid from the outside. This equation is the mathematical "tally" of those two effects. Note the negative sign on the pressure term: because $d\mathbf{S}$ points outward, but pressure always pushes inward, the sign ensures we are correctly calculating the force acting _on_ the fluid.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\iiint_{\mathscr{V}}\rho\,\mathbf{f}\, d\mathscr{V}$|**Body Force Contribution**|The sum of "action-at-a-distance" forces (like gravity) acting on every unit of mass inside the volume.|
|$-\iint_{S}p\, d\mathbf{S}$|**Pressure Force Contribution**|The net inward "squeeze" from the surrounding fluid acting on the boundary of the control volume.|
|$\mathbf{F}$|**Net External Force**|The total vector sum of all influences; this is the "$\mathbf{F}$" that appears in the general form of Newton's Second Law.|
|$p\, d\mathbf{S}$|**Elemental Pressure Force**|The force on a tiny patch of the surface; the negative sign flips it from the outward normal to the inward push.|



# Total rate of change of energy of the fluid as it flows through the control volume (Eq. 2.19)

> [!equation] Total rate of change of energy of the fluid as it flows through the control volume (Eq. 2.19)
> $$
> B_3=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> +\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)
> $$

This groups the energy “storage” term inside the control volume and the net energy flux through the control surface to form the total rate of energy change for the flowing fluid.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$E_t = e + \frac{V^2}{2}$|**Total Specific Energy**|The complete energy "package" per unit mass (Internal + Kinetic).|
|$\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho E_t\, d\mathscr{V}$|**Energy Storage Rate**|The "Internal Accumulation": how much energy is being banked or drained inside the volume over time.|
|$\iint_{S}(\rho \mathbf{V} \cdot d\mathbf{S}) E_t$|**Net Energy Flux**|The "Convective Export": the rate at which energy is physically shipped out of the system by the moving fluid.|
|$B_3$|**Total Energy-Change Rate**|The combined sum of storage and flux; this is the term that must be balanced by heat and work ($B_1 + B_2$).|


This equation represents the "Net Energy Ledger" for the fluid system. It combines two ways energy can change: by piling up inside the volume (storage) or by being carried across the boundaries by the flow (convection). Together, these terms account for the total rate at which the fluid's energy "account" is fluctuating. Think of this as the Total Power Demand of the fluid. If you want to speed up the flow or heat it up, you have to satisfy both terms. You must provide enough energy to increase the local "inventory" inside your system and enough to cover the energy that the fluid "takes with it" as it exits the boundary. In steady-state engineering, the storage term often vanishes, leaving only the flux term to balance the power inputs.




# Total surface force due to pressure (Eq. 2.6)

> [!equation] Total surface force due to pressure (Eq. 2.6)
> $$
> -\iint_{S}p\, d\mathbf{S}
> $$

This integral calculates the net vector force exerted by the surrounding fluid on the boundaries of a control volume. It sums every individual "push" from pressure across the entire surface to determine if there is a resultant force that would cause the fluid inside to accelerate. Pressure is always a "squeeze" directed inward toward the fluid. Because our mathematical convention is to define the surface area vector $d\mathbf{S}$ as pointing outward, we must apply a negative sign to align the math with the physical reality. If the pressure is uniform all around the volume (like being submerged in a still pool), the integral sums to zero; a net force only appears if the pressure is higher on one side than the other.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$p\, d\mathbf{S}$|**Outward Pressure Vector**|A mathematical construction that points in the direction of the surface normal; it is the opposite of the physical force.|
|$-p\, d\mathbf{S}$|**Inward Pressure Force**|The actual physical "push" exerted by the surroundings on a tiny patch of the fluid boundary.|
|$\iint_{S} (\dots)$|**Surface Tally**|The integral process that "scans" the entire boundary to sum up the individual pressure vectors.|
|$-\iint_{S}p\, d\mathbf{S}$|**Net Pressure Force**|The total resultant force vector ($\mathbf{F}_p$) acting on the fluid due to external pressure.|




# Total time rate of change of momentum (Eq. 2.10)

> [!equation] Total time rate of change of momentum (Eq. 2.10)
> $$
> \frac{d}{dt}(m\mathbf{V})=\mathbf{A}_1+\mathbf{A}_2
> =\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}+\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

This equation defines the total rate at which the "Motion Content" of a fluid system is changing. It accounts for two distinct physical mechanisms: momentum being physically carried across the boundaries by the flowing mass (Flux) and momentum building up or depleting within the fixed region itself (Storage). Think of this as the Momentum Balance Sheet. In a steady-state system, the "Storage" term ($\mathbf{A}_2$) is zero, meaning any change in momentum is purely due to the difference between what flows in and what flows out ($\mathbf{A}_1$). If you are analyzing a transient event—like a rocket engine's initial ignition—the "Storage" term captures how the fluid inside the chamber is accelerating before it even reaches the exit.

|**Expression**|**Name**|**Description**|
|---|---|---|
|$\mathbf{A}_1 = \iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}$|**Momentum Flux**|**Convective Transport:** The rate at which the flow "carries" its own momentum vector across the control surface.|
|$\mathbf{A}_2 = \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$|**Momentum Storage**|**Unsteady Accumulation:** The rate at which the total momentum inventory inside the volume changes over time.|
|$\mathbf{A}_1+\mathbf{A}_2$|**Total Momentum Rate**|The combined result of flux and storage; this represents the "$\frac{d}{dt}(m\mathbf{V})$" used in Newton's Second Law.|
|$\rho \mathbf{V}$|**Momentum Density**|The local momentum per unit volume at any given point within the system.|


# Total work rate on the fluid (Eq. 2.16)

> [!equation] Total work rate on the fluid (Eq. 2.16)
> $$
> B_2=-\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}+\iiint_{\mathscr{V}}\rho(\mathbf{f}\cdot\mathbf{V})\, d\mathscr{V}
> $$

This equation defines the total **Mechanical Power** being transferred from the surroundings into the fluid within the control volume. It sums two distinct modes of work: the "pushing" work done by pressure on the surface of the volume and the "pulling" work done by body forces (like gravity) acting throughout the interior mass. In a closed system, we often think of work as $P \Delta V$. In an open control volume, the fluid is moving across boundaries, so "work" becomes "power" (work per unit time). This equation captures how the environment mechanically "pumps" energy into the fluid. If the fluid is moving in the direction of the force (like falling with gravity or being pushed in by high pressure), $B_2$ is positive, adding energy to the fluid's total budget.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$-\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}$|**Pressure Work Rate**|**Surface Power:** The rate of work done on the fluid by external pressure at the boundary. Positive when fluid is pushed into the volume.|
|$\iiint_{\mathscr{V}}\rho(\mathbf{f}\cdot\mathbf{V})\, d\mathscr{V}$|**Body-Force Work Rate**|**Volumetric Power:** The rate of work done by forces like gravity acting on the bulk of the moving fluid.|
|$B_2$|**Total Work Rate**|The net mechanical power input; this is the term that combines with heat ($B_1$) to balance the energy change ($B_3$).|
|$\rho(\mathbf{f}\cdot\mathbf{V})$|**Power Density**|The mechanical energy added per unit volume per unit time at a specific point inside the system.|


# Uninstalled engine thrust equation (Eq. 2.45)

> [!equation] Uninstalled engine thrust equation (Eq. 2.45)
> $$
> T=\dot{m}_{e} V_{e}-\dot{m}_{i} V_{\infty}+\left(p_{e}-p_{\infty}\right) A_{e}
> $$

This equation defines the net forward force (thrust) produced by an air-breathing engine. It is the result of the "Momentum Balance": the engine takes in air at one speed, accelerates it, and ejects it at a much higher speed. The thrust is the difference between the exit and inlet momentum, plus an additional "push" if the exhaust pressure doesn't perfectly match the outside atmosphere. Think of this as the Net Reaction Force. To get forward thrust, the engine must "throw" mass backward faster than it "caught" it. The term $-\dot{m}_i V_{\infty}$ is effectively a "Ram Drag"—the penalty for scooping up stationary air. The term $\dot{m}_e V_e$ is the "Gross Thrust." If the exit pressure is higher than the ambient air ($p_e > p_{\infty}$), you get a "bonus" force as that high pressure pushes against the nozzle exit area ($A_e$).


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\dot{m}_e V_e$|**Gross Momentum Thrust**|The total force generated by the momentum of the exhaust gas leaving the engine.|
|$\dot{m}_i V_\infty$|**Inlet Momentum Drag**|The "Ram Drag"; the momentum cost of bringing the incoming air into the engine.|
|$(p_e - p_\infty)A_e$|**Pressure Thrust**|The net force caused by the pressure difference between the exhaust gas and the ambient atmosphere.|
|$T$|**Uninstalled Thrust**|The net axial force produced by the engine itself, excluding any aerodynamic interference from the aircraft.|
|$\dot{m}_e$|**Exit Mass Flow**|The total mass leaving ($\dot{m}_{air} + \dot{m}_{fuel}$).|
|$V_e$|**Exit Velocity**|The velocity of the exhaust relative to the engine.|



# Unsteady (transient) momentum term (Eq. 2.9)

> [!equation] Unsteady (transient) momentum term (Eq. 2.9)
> $$
> \mathbf{A}_2=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> =\iiint_{\mathscr{V}}\frac{\partial(\rho\,\mathbf{V})}{\partial t}\, d\mathscr{V}
> $$

This term represents the Internal Momentum Fluctuation. It measures the rate at which the "total pile" of momentum stored inside the fixed boundaries of the control volume is increasing or decreasing at any given moment. Think of this as the Momentum Bank Account. In steady-state flow, the amount of momentum inside the volume is constant, so this term is zero. However, during a transient event—like a rocket engine's startup or a car accelerating—the fluid inside the system is physically speeding up or becoming more dense. This term captures that "acceleration of the fluid within the box" before it even reaches the exit.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$|**Momentum Inventory**|The total quantity of motion (mass $\times$ velocity) currently residing inside the control volume.|
|$\frac{\partial}{\partial t}(\dots)$|**Storage Rate Operator**|The mathematical "clock" that measures how the internal inventory changes over time.|
|$\frac{\partial(\rho\,\mathbf{V})}{\partial t}$|**Local Momentum Change**|The "Integrand Form"; tracks the change in momentum density at every specific point in space.|
|$\mathbf{A}_2$|**Unsteady Shorthand**|The designated symbol for the storage term used in the complete integral momentum balance.|


# Volumetric heat addition rate (Eq. 2.13)

> [!equation] Volumetric heat addition rate (Eq. 2.13)
> $$
> B_1=\iiint_{\mathscr{V}}\dot{q}\,\rho\, d\mathscr{V}
> $$

This integral calculates the total rate at which thermal energy is being "pumped" into the fluid throughout the entire interior of the control volume. It sums every individual contribution of heat—whether from a chemical reaction, radiation, or an internal heating element—acting on the mass within the region. Think of this as the **Internal Furnace** of your system. Unlike heat that passes through the walls (surface conduction), this term represents energy that is generated or absorbed "in the bulk." For a combustion chamber in a jet engine, this is the most critical term because it represents the chemical energy of the fuel being converted into the thermal energy that eventually drives the turbine.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\dot{q}$|**Specific Heat Addition**|The rate of heat energy added per unit mass (e.g., J/kg·s); represents the "intensity" of the heat source.|
|$\rho \dot{q}$|**Heat Power Density**|The heat energy added per unit volume; determines how much "fire" is packed into a specific point in space.|
|$d\mathscr{V}$|**Differential Volume**|The infinitesimal spatial element used to "sweep" through the entire region $\mathscr{V}$.|
|$\iiint_{\mathscr{V}} \dots d\mathscr{V}$|**Total Thermal Power**|The volume integral that tallies every watt of internal heat to find the net heating rate.|
|$B_1$|**Net Heating Term**|The "Thermal Deposit" in your energy budget; this is the primary driver for increasing the fluid's enthalpy.|