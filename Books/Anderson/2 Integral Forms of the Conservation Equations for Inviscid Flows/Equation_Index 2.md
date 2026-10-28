# Equation Index — Anderson, Chapter 2
ME 510




# 1. Kinetic energy per unit mass

> [!question]
>
> (a) Write the expression for kinetic energy per unit mass.
> (b) Why is this a scalar even though velocity is a vector?
> (c) In the total specific energy, what other term is added to this quantity?

> [!equation] Kinetic energy per unit mass
>
> $$
> \frac{V^2}{2}
> $$

This is the macroscopic mechanical energy associated with the bulk motion of a unit mass of fluid. It depends only on the speed magnitude $V$, not the direction of the velocity vector.

| **Expression** | **Name**                  | **Description**                                                  |
| -------------- | ------------------------- | ---------------------------------------------------------------- |
| $V$            | **Speed Magnitude**       | The magnitude of the local velocity vector.                      |
| $\frac{V^2}{2}$ | **Specific Kinetic Energy** | The kinetic energy carried by a unit mass of moving fluid.       |


# 2. Total specific energy

> [!question]
>
> (a) Write the expression for total specific energy in the chapter’s inviscid energy balances.
> (b) What two physical contributions are included in this quantity?
> (c) Why is this called a “specific” energy?

> [!equation] Total specific energy
>
> $$
> e+\frac{V^2}{2}
> $$

This is the total energy carried by a unit mass of fluid when only internal and kinetic energy are being counted. It combines microscopic thermal energy with macroscopic motion energy.

| **Expression**     | **Name**                  | **Description**                                                      |
| ------------------ | ------------------------- | -------------------------------------------------------------------- |
| $e$                | **Internal Energy**       | The microscopic energy stored in the fluid per unit mass.            |
| $\frac{V^2}{2}$    | **Specific Kinetic Energy** | The macroscopic motion energy per unit mass.                         |
| $e+\frac{V^2}{2}$  | **Total Specific Energy** | The complete energy package carried by a unit mass of fluid.         |


# 3. Momentum flux (elemental form)

> [!question]
>
> (a) Write the elemental convective momentum-flux term.
> (b) Which factor gives the mass flow through the surface element?
> (c) Why is the result a vector?

> [!equation] Momentum flux (elemental form)
>
> $$
> (\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}
> $$

This is the momentum per unit time carried through a surface element by the flowing fluid. The scalar mass-flow factor selects how much mass crosses the element, and multiplication by $\mathbf{V}$ attaches the momentum direction.

| **Expression**                                  | **Name**                      | **Description**                                                             |
| ----------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------- |
| $\rho\,\mathbf{V}\cdot d\mathbf{S}$             | **Elemental Mass Flow**       | The signed mass flow rate through the surface element.                      |
| $\mathbf{V}$                                    | **Velocity Vector**           | The momentum direction carried by the crossing fluid.                       |
| $(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}$ | **Elemental Momentum Flux** | The momentum transported through the surface element per unit time.         |


# 4. Body force density

> [!question]
>
> (a) Write the expression for body force density.
> (b) What two quantities are multiplied to form it?
> (c) Why is this a force per unit volume?

> [!equation] Body force density
>
> $$
> \rho\,\mathbf{f}
> $$

This is the local body force acting on a unit volume of fluid. It combines the body force per unit mass with the mass density at the point.

| **Expression**   | **Name**                    | **Description**                                                  |
| ---------------- | --------------------------- | ---------------------------------------------------------------- |
| $\rho$           | **Density**                 | The mass per unit volume of fluid.                               |
| $\mathbf{f}$     | **Body Force per Unit Mass** | The body-force acceleration field, such as gravity.              |
| $\rho\,\mathbf{f}$ | **Body Force Density**    | The net body force exerted on each unit volume of fluid.         |


# 5. Pressure force (elemental form)

> [!question]
>
> (a) Write the elemental pressure-force vector acting on the fluid.
> (b) Why is there a negative sign?
> (c) What role does the area vector play?

> [!equation] Pressure force (elemental form)
>
> $$
> -p\,d\mathbf{S}
> $$

This is the elemental surface force exerted by pressure on the fluid. The minus sign is required because pressure acts inward on the fluid while the area vector $d\mathbf{S}$ points outward by convention.

| **Expression** | **Name**                   | **Description**                                                          |
| -------------- | -------------------------- | ------------------------------------------------------------------------ |
| $p$            | **Pressure**               | The local normal stress acting on the surface element.                   |
| $d\mathbf{S}$  | **Area Vector**            | The oriented surface element pointing outward from the control volume.   |
| $-p\,d\mathbf{S}$ | **Elemental Pressure Force** | The inward pressure force acting on the fluid over that surface patch. |


# 6. Pressure power (elemental form)

> [!question]
>
> (a) Write the elemental pressure-power term.
> (b) How is it related to the elemental pressure force?
> (c) When is this term positive?

> [!equation] Pressure power (elemental form)
>
> $$
> -p\,(\mathbf{V}\cdot d\mathbf{S})
> $$

This is the elemental rate of work done by pressure forces as fluid crosses a surface element. It is the scalar power obtained by projecting the surface-crossing velocity onto the area vector and weighting by pressure.

| **Expression**                  | **Name**                     | **Description**                                                          |
| ------------------------------- | ---------------------------- | ------------------------------------------------------------------------ |
| $\mathbf{V}\cdot d\mathbf{S}$   | **Elemental Volumetric Flow** | The signed volumetric flow rate through the surface element.             |
| $p$                             | **Pressure**                  | The local normal stress driving the work transfer.                       |
| $-p\,(\mathbf{V}\cdot d\mathbf{S})$ | **Elemental Pressure Power** | The rate at which pressure does work on the fluid through that patch.    |


# 7. External work power

> [!question]
>
> (a) Write the chapter’s combined external-work-power term.
> (b) What two contributions are included in it?
> (c) Why is this distinct from pressure work?

> [!equation] External work power
>
> $$
> \dot{W}_{\text{shaft}}+\dot{W}_{\text{viscous}}
> $$

This term groups the non-pressure mechanical power inputs to the control volume. It includes shaft work crossing the boundary and viscous work done by stresses on the boundary.

| **Expression**                           | **Name**               | **Description**                                                        |
| ---------------------------------------- | ---------------------- | ---------------------------------------------------------------------- |
| $\dot{W}_{\text{shaft}}$                 | **Shaft Power**        | Mechanical power transferred by rotating or translating machinery.      |
| $\dot{W}_{\text{viscous}}$               | **Viscous Work Power** | Mechanical power transferred by viscous stresses at the boundary.       |
| $\dot{W}_{\text{shaft}}+\dot{W}_{\text{viscous}}$ | **External Work Power** | The total non-pressure mechanical power added to the control volume. |


# 8. Normal velocity component

> [!question]
>
> (a) Write the expression for the normal component of velocity.
> (b) What angle appears in this definition?
> (c) Why is this quantity central in flux calculations?

> [!equation] Normal velocity component
>
> $$
> V\cos\theta
> $$

This is the component of the velocity magnitude directed normal to a surface. It is the part of the flow that actually crosses the surface and therefore contributes to fluxes.

| **Expression** | **Name**                    | **Description**                                                     |
| -------------- | --------------------------- | ------------------------------------------------------------------- |
| $V$            | **Speed Magnitude**         | The magnitude of the local velocity vector.                         |
| $\theta$       | **Incidence Angle**         | The angle between the velocity vector and the outward surface normal. |
| $V\cos\theta$  | **Normal Velocity Component** | The part of the velocity directed through the surface.             |


# 9. Area vector

> [!question]
>
> (a) Write the definition of the area vector.
> (b) What does the unit normal contribute?
> (c) Why is this notation useful in flux integrals?

> [!equation] Area vector
>
> $$
> d\mathbf{S}=\mathbf{n}\,dS
> $$

This defines the oriented surface element used throughout the integral balances. It combines the scalar area magnitude with the outward unit normal so both size and direction are carried in a single object.

| **Expression**        | **Name**          | **Description**                                                          |
| --------------------- | ----------------- | ------------------------------------------------------------------------ |
| $\mathbf{n}$          | **Unit Normal**   | The outward unit vector normal to the surface element.                   |
| $dS$                  | **Scalar Area**   | The magnitude of the infinitesimal surface patch.                        |
| $d\mathbf{S}$         | **Area Vector**   | The oriented surface element used in surface-force and flux integrals.   |


# 10. Mass flow through an elemental surface (Eq. 2.1)

> [!question]
>
> (a) Write the equivalent forms for elemental mass flow through a surface and explain how they are related.
> (b) What geometric information is built into the vector-flux form?
> (c) How does the sign of this quantity distinguish inflow from outflow?
> (d) Why does only the normal component of velocity contribute?

> [!equation] Mass flow through an elemental surface (Eq. 2.1)
>
> $$
> \dot{m}=\rho(V\cos\theta)\, dS=\rho V_n\, dS=\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

This expression gives the mass flow rate through a differential surface element. The first two forms show that only the velocity component normal to the surface contributes; the final vector-dot-product form packages the same geometry and sign convention compactly.

| **Expression**                | **Name**                      | **Description**                                                                 |
| ----------------------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| $\dot{m}$                     | **Elemental Mass Flow**       | The mass per unit time crossing the differential surface element.               |
| $V\cos\theta$                 | **Normal Velocity Component** | The component of velocity directed normal to the surface.                       |
| $V_n$                         | **Normal Speed**              | A shorthand for the normal velocity component.                                  |
| $d\mathbf{S}=\mathbf{n}\,dS$  | **Area Vector**               | The oriented surface element combining area magnitude and outward normal.        |
| $\rho\,\mathbf{V}\cdot d\mathbf{S}$ | **Vector Flux Form**    | The compact dot-product form with geometry and sign convention built in.         |


# 11. Mechanical power (power projection)

> [!question]
>
> (a) Write the expression for the rate of work done by a force acting on a moving body or fluid element.
> (b) Why does the dot product appear in this expression?
> (c) Under what conditions is the power zero even when a force is present?
> (d) How is this expression used to build the pressure-work and body-force-work terms in the energy equation?

> [!equation] Mechanical power (power projection)
>
> $$
> \dot{W}=\mathbf{F}\cdot\mathbf{V}
> $$

This expression gives the rate at which a force transfers mechanical energy when applied at a point moving with velocity $\mathbf{V}$. The dot product shows that only the component of force aligned with the motion contributes to the power transfer.

| **Expression**             | **Name**             | **Description**                                                          |
| -------------------------- | -------------------- | ------------------------------------------------------------------------ |
| $\dot{W}$                  | **Mechanical Power** | The rate of work or mechanical-energy transfer.                          |
| $\mathbf{F}$               | **Force Vector**     | The applied force doing work on the particle, body, or fluid element.    |
| $\mathbf{V}$               | **Velocity Vector**  | The velocity of the point where the force acts.                          |
| $\mathbf{F}\cdot\mathbf{V}$ | **Power Projection** | The scalar mechanical power from projecting force onto the motion.       |


# 12. Power density

> [!question]
>
> (a) Write the local power-density term associated with body forces.
> (b) Why is this a power per unit volume?
> (c) What does the dot product indicate physically?

> [!equation] Power density
>
> $$
> \rho\,(\mathbf{f}\cdot\mathbf{V})
> $$

This is the local rate of mechanical energy transfer per unit volume due to body forces acting on moving fluid. It is the volumetric form of body-force work rate.

| **Expression**                   | **Name**                | **Description**                                                           |
| -------------------------------- | ----------------------- | ------------------------------------------------------------------------- |
| $\rho$                           | **Density**             | The local mass per unit volume.                                           |
| $\mathbf{f}\cdot\mathbf{V}$      | **Specific Power**      | The rate of body-force work per unit mass.                                |
| $\rho\,(\mathbf{f}\cdot\mathbf{V})$ | **Power Density**    | The body-force power added locally per unit volume of fluid.              |


# 13. Gross momentum thrust

> [!question]
>
> (a) Write the expression for the gross momentum-thrust term in the engine thrust equation.
> (b) What physical process does this term represent?
> (c) Why is this called a momentum thrust?

> [!equation] Gross momentum thrust
>
> $$
> \dot{m}_e V_e
> $$

This is the exhaust-momentum contribution to thrust. It measures the forward reaction force associated with ejecting mass backward at the exit speed $V_e$.

| **Expression** | **Name**                | **Description**                                                  |
| -------------- | ----------------------- | ---------------------------------------------------------------- |
| $\dot{m}_e$    | **Exit Mass Flow Rate** | The rate at which exhaust mass leaves the engine.                |
| $V_e$          | **Exit Velocity**       | The exhaust speed relative to the engine.                        |
| $\dot{m}_e V_e$ | **Gross Momentum Thrust** | The thrust contribution from the outgoing exhaust momentum.   |


# 14. Inlet momentum drag

> [!question]
>
> (a) Write the inlet-momentum-drag term from the air-breathing engine thrust equation.
> (b) Why is this considered a drag penalty?
> (c) What inlet quantities appear in it?

> [!equation] Inlet momentum drag
>
> $$
> \dot{m}_i V_\infty
> $$

This is the momentum penalty associated with bringing incoming air into the engine. In the full thrust equation it is subtracted, so it reduces the net forward thrust.

| **Expression** | **Name**               | **Description**                                                        |
| -------------- | ---------------------- | ---------------------------------------------------------------------- |
| $\dot{m}_i$    | **Inlet Mass Flow Rate** | The rate at which ambient air enters the engine.                     |
| $V_\infty$     | **Freestream Velocity** | The incoming air speed relative to the engine.                       |
| $\dot{m}_i V_\infty$ | **Inlet Momentum Drag** | The momentum term that opposes the gross exhaust thrust.        |


# 15. Pressure thrust

> [!question]
>
> (a) Write the pressure-thrust term from the engine or rocket thrust equation.
> (b) What pressure difference appears in this expression?
> (c) When does this term vanish?

> [!equation] Pressure thrust
>
> $$
> (p_e-p_\infty)A_e
> $$

This is the thrust contribution caused by a mismatch between exit pressure and ambient pressure. It represents the net force produced when the exhaust pressure pushes on the exit plane area.

| **Expression**       | **Name**             | **Description**                                                       |
| -------------------- | -------------------- | --------------------------------------------------------------------- |
| $p_e-p_\infty$       | **Pressure Difference** | The exit pressure relative to ambient pressure.                    |
| $A_e$                | **Exit Area**        | The nozzle exit area over which the pressure difference acts.         |
| $(p_e-p_\infty)A_e$  | **Pressure Thrust**  | The thrust contribution arising from exit-pressure imbalance.         |


# 16. Heat power density

> [!question]
>
> (a) Write the local volumetric heat-power-density term.
> (b) What two quantities are multiplied to form it?
> (c) Why is this a power per unit volume rather than per unit mass?

> [!equation] Heat power density
>
> $$
> \rho\,\dot{q}
> $$

This is the local rate of thermal energy addition per unit volume. It converts the specific heating rate $\dot{q}$ into a volumetric power density by multiplying by the local mass density.

| **Expression**   | **Name**               | **Description**                                                        |
| ---------------- | ---------------------- | ---------------------------------------------------------------------- |
| $\dot{q}$        | **Specific Heat Addition** | The heat added per unit mass per unit time.                         |
| $\rho$           | **Density**            | The local mass per unit volume.                                        |
| $\rho\,\dot{q}$  | **Heat Power Density** | The thermal power added locally per unit volume of fluid.              |


# 17. Momentum storage inside the control volume (Eq. 2.9)

> [!question]
>
> (a) Write the momentum-storage term for a fixed control volume. Why is this term a vector?
> (b) What does it measure physically, and when is it exactly zero?
> (c) How does this term differ from the momentum-flux term across the control surface?
> (d) In the integral momentum equation, what symbol is commonly used for this term?

> [!equation] Momentum storage inside the control volume (Eq. 2.9)
>
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

This term is the time rate of change of the total momentum presently stored inside the fixed control volume. Because momentum is a vector quantity, the storage term is also a vector. In steady flow this term vanishes; in unsteady flow it measures how the momentum inventory inside the volume is building up or depleting with time. In Eq. 2.9, this term is denoted by $\mathbf{A}_2$.

| **Expression**                                                          | **Name**                  | **Description**                                                                                       |
| ----------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------- |
| $\rho\,\mathbf{V}$                                                      | **Momentum Density**      | The local momentum per unit volume at a point inside the control volume.                              |
| $\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$                   | **Momentum Inventory**    | The total momentum vector of all fluid currently contained in the control volume.                     |
| $\frac{\partial}{\partial t}$                                           | **Storage-Rate Operator** | The time derivative that measures how the stored momentum changes.                                    |
| $\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$ | **Momentum Storage Rate** | The unsteady accumulation or depletion of momentum inside the control volume.                         |
| $\mathbf{A}_2$                                                          | **Momentum-Storage Term** | The standard shorthand used for this contribution in the integral momentum equation.                  |


# 18. Mass contained inside the control volume

> [!question]
>
> (a) Write the expression for the total mass inside a fixed control volume. Explain what the integrand represents physically.
> (b) What happens to this integral if the density is spatially uniform throughout the volume?
> (c) If the fluid is incompressible and the control volume is fixed in space, what can you say about the time derivative of this expression? What does that imply for the continuity equation?
> (d) Where does this expression appear in the governing equations, and what role does it play?

> [!equation] Mass contained inside the control volume
>
> $$
> \iiint_{\mathscr{V}}\rho\, d\mathscr{V}
> $$

This integral gives the instantaneous mass inventory of the fluid currently residing inside the fixed control volume. It sums the local mass density over the entire region, producing the total scalar mass contained in the volume at that instant.

| **Expression**                            | **Name**                 | **Description**                                                                                                       |
| ----------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| $\rho$                                    | **Density**              | The local mass per unit volume at a point in the fluid.                                                               |
| $d\mathscr{V}$                            | **Differential Volume**  | The infinitesimal volume element used to build the full volume integral.                                              |
| $\iiint_{\mathscr{V}}\rho\, d\mathscr{V}$ | **Total Mass Inventory** | The total scalar mass of fluid contained inside the control volume.                                                   |


# 19. Momentum contained inside the control volume

> [!question]
>
> (a) Write the expression for the total momentum inside a fixed control volume. Is the result a scalar or a vector?
> (b) What is the physical meaning of the integrand $\rho\mathbf{V}$, and why is density needed?
> (c) If the properties inside the control volume are spatially uniform, what does this integral simplify to? How does this connect to the familiar point-mass momentum $m\mathbf{V}$?
> (d) Under steady-flow conditions, what happens to the time derivative of this expression, and what does that imply for the momentum equation?

> [!equation] Momentum contained inside the control volume
>
> $$
> \iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

This integral is the total momentum vector of all fluid presently inside the fixed control volume. It sums the local momentum density $\rho\mathbf{V}$ over the whole region, so it is the vector analog of the mass inventory.

| **Expression**                                        | **Name**                     | **Description**                                                                                                                            |
| ----------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| $\rho \mathbf{V}$                                     | **Momentum Density**         | The local momentum per unit volume at a point inside the control volume.                                                                   |
| $d\mathscr{V}$                                        | **Differential Volume**      | The infinitesimal volume element used in the integration.                                                                                  |
| $\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}$ | **Total Momentum Inventory** | The volume integral that converts local momentum density into the total resultant momentum vector for the fluid inside the control volume. |


# 20. Net mass flow into a fixed control volume

> [!question]
>
> (a) Write the expression for the net mass flow *into* a fixed control volume. Why is a negative sign needed in front of the surface integral?
> (b) If this expression yields a positive value, what is physically happening to the mass inside the control volume?
> (c) How does this expression relate to the storage term in the continuity equation?

> [!equation] Net mass flow into a fixed control volume
>
> $$
> -\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

This surface integral gives the net rate at which mass enters a fixed control volume. With the standard outward-pointing area vector, $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$ represents net outflow. The minus sign reverses that convention so that a positive value corresponds to net inflow, or mass entering faster than it leaves.

| **Expression**                                | **Name**                    | **Description**                                                                                                        |
| --------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| $\rho\,\mathbf{V}\cdot d\mathbf{S}$           | **Differential Mass Flux**  | The elemental mass flow rate through a surface patch; positive for outward flow and negative for inward flow.         |
| $\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$  | **Net Outflow Rate**        | The total mass flow rate leaving the control volume.                                                                   |
| $-\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}$ | **Net Inflow Rate**         | The total mass flow rate entering the control volume, equal to mass in minus mass out.                                |


# 21. Rate of work on the fluid due to pressure forces (Eq. 2.14)

> [!question]
>
> (a) Write the expression for the total rate of work done on the fluid by pressure forces on the control surface. Explain the origin of the negative sign.
> (b) A pressure force acts on a solid, stationary wall of the control volume. Does this pressure force do any work? Why or why not?
> (c) Explain the physical difference between pressure doing work at an inlet (fluid entering) versus at an exit (fluid leaving). Which represents energy added to the system?
> (d) When the surface integrals in the energy equation are evaluated at 1-D uniform stations, the pressure work combines with the internal energy flux to produce enthalpy. Show why.

> [!equation] Rate of work on the fluid due to pressure forces (Eq. 2.14)
>
> $$
> -\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}
> $$

This surface integral gives the net power transferred to the fluid by pressure forces as fluid crosses the control surface. It is not a mass-balance term: the additional factor $p$ converts the volumetric flow rate $\mathbf{V}\cdot d\mathbf{S}$ at each surface element into a rate of pressure work. With the outward-normal convention, inlet contributions are positive and exit contributions are negative.

| **Expression**                              | **Name**                        | **Description**                                                                                             |
| ------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| $p$                                         | **Pressure**                    | The local normal stress exerted by the surrounding fluid on the control surface.                            |
| $\mathbf{V}\cdot d\mathbf{S}$               | **Differential Volumetric Flow** | The signed volumetric flow rate through a surface patch; negative at an inlet and positive at an exit.     |
| $-p\,(\mathbf{V}\cdot d\mathbf{S})$         | **Elemental Pressure Power**    | The differential rate of pressure work done on the fluid through that surface patch.                        |
| $-\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}$ | **Net Pressure-Work Rate**      | The total rate at which pressure forces add mechanical energy to the fluid across the full control surface. |


# 22. Momentum flux across the control surface (Eq. 2.8)

> [!question]
>
> (a) Write the expression for the net momentum flux across a control surface and identify the two factors in the integrand. What does each represent?
> (b) Explain why the momentum flux through a solid, impermeable wall is zero, even though the fluid adjacent to it may be moving fast.
> (c) For a single-inlet, single-exit duct with uniform properties at each station, what does the momentum flux integral simplify to?
> (d) In steady flow, the momentum-storage term vanishes. What does this imply about the relationship between $\mathbf{A}_1$ and the net force on the fluid?
> (e) Is $\mathbf{A}_1$ a force? Explain why or why not, and describe the circumstances under which $\mathbf{A}_1$ numerically equals the net force.

> [!equation] Momentum flux across the control surface (Eq. 2.8)
>
> $$
> \mathbf{A}_1=\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}
> $$

This integral gives the net rate at which momentum is convected across the control surface by the moving fluid. The factor $\rho\,\mathbf{V}\cdot d\mathbf{S}$ selects the mass crossing the surface element, and multiplying by $\mathbf{V}$ converts that mass flow into momentum transport.

| **Expression**                                  | **Name**                         | **Description**                                                                                           |
| ----------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| $\rho \mathbf{V} \cdot d\mathbf{S}$             | **Differential Mass Flow**       | The mass flow rate through a surface element; its sign distinguishes inflow from outflow.                |
| $(\rho \mathbf{V} \cdot d\mathbf{S})\mathbf{V}$ | **Differential Momentum Flux**   | The momentum per unit time transported through a specific surface patch.                                  |
| $\iint_{S} (\dots)$                             | **Net Momentum Flux**            | The surface integral that sums the momentum transport over the entire control surface.                    |
| $\mathbf{A}_1$                                  | **Momentum-Flux Term**           | The standard shorthand for this convective contribution in the integral momentum equation.                |


# 23. Rate of work on the fluid due to body forces (Eq. 2.15)

> [!question]
>
> (a) Write the expression for the total rate of work done on the fluid by body forces throughout a control volume. Identify each factor in the integrand.
> (b) Explain why the dot product $\mathbf{f} \cdot \mathbf{V}$ appears. Under what geometric condition between the force and velocity is no work done?
> (c) If gravity is the only body force and the fluid is flowing horizontally, what is the value of this integral?
> (d) In most aerodynamic applications, this term is neglected. Why?


> [!equation] Rate of work on the fluid due to body forces (Eq. 2.15)
>
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


# 24. Total body force acting on the control volume (Eq. 2.5)

> [!question]
>
> (a) Write the expression for the total body force acting on the fluid inside a control volume. What does the integrand $\rho\mathbf{f}$ represent?
> (b) How does this "action-at-a-distance" force differ from a surface force like pressure?
> (c) If gravity is the only body force, what does $\mathbf{f}$ equal, and what does the integral reduce to for a fluid of uniform density?
> (d) Where does this expression appear in the momentum equation, and on which side (forces or momentum change)?


> [!equation] Total body force acting on the control volume (Eq. 2.5)
>
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


# 25. Energy contained inside the control volume


> [!question]
>
> (a) Write the expression for the total energy contained inside a control volume. Identify the two forms of energy included in the integrand and explain what each represents physically.
> (b) What role does density play in the integrand, and why is it necessary for the integration to work?
> (c) If the properties inside the control volume can be approximated as spatially uniform, what does the integral simplify to?
> (d) Under what physical conditions might you drop the kinetic energy term, and what does the total specific energy reduce to in that case?



> [!equation] Energy contained inside the control volume
>
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


# 26. Time rate of change of energy inside the control volume (Eq. 2.18)

> [!question]
>
> (a) Write the expression for the time rate of change of energy inside a control volume. What does it measure physically?
> (b) Under what conditions is this term exactly zero? What type of flow does that correspond to?
> (c) Give a physical example of a transient process where this term would be significant.
> (d) How does this term relate to $B_3$ in the control volume power balance? Is it the whole of $B_3$?


> [!equation] Time rate of change of energy inside the control volume (Eq. 2.18)
>
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> $$

This term represents the unsteady energy-storage rate within the fixed spatial boundaries of the control volume. It tracks how the total energy inventory presently inside the region is accumulating or depleting with time.


| **Expression**                                 | **Name**                  | **Description**                                                                                             |
| ---------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| $\iiint_{\mathscr{V}}\rho E_t \, d\mathscr{V}$ | **Total Stored Energy**   | The instantaneous total energy currently residing inside the volume.                                         |
| $\frac{\partial}{\partial t}(\dots)$           | **Local Time Derivative** | The rate at which the stored energy changes due to unsteadiness.                                             |
| $\rho \left(e+\frac{V^2}{2}\right)$            | **Total Energy Density**  | The local energy per unit volume at each point in the control volume.                                        |


# 27. Net rate of energy flow across the control surface (Eq. 2.17)

> [!question]
>
> (a) Write the net-rate-of-energy-flow term across a control surface in both equivalent forms.
> (b) Why is the total specific energy $e + V^2/2$ rather than just $e$? Under what conditions would the kinetic energy contribution be negligible?
> (c) How do the forms $\rho\left(e+\frac{V^2}{2}\right)\mathbf{V}\cdot d\mathbf{S}$ and $(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)$ express the same physical transport?
> (d) How does the sign convention (outward $d\mathbf{S}$) distinguish energy being carried out of the volume from energy being carried in?

> [!equation] Net rate of energy flow across the control surface (Eq. 2.17)
>
> $$
> \iint_{S}\rho\left(e+\frac{V^2}{2}\right)\mathbf{V}\cdot d\mathbf{S}
> =
> \iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)
> $$

This term is the convective transport of total energy across the control surface. The left form emphasizes the energy-flux vector $\rho\left(e+\frac{V^2}{2}\right)\mathbf{V}$; the right form emphasizes the interpretation “mass flow rate times total specific energy.” They are the same integral written in two equivalent ways.


| **Expression**                                               | **Name**                          | **Description**                                                                                             |
| ------------------------------------------------------------ | --------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| $\rho\left(e+\frac{V^2}{2}\right)\mathbf{V}$                 | **Energy-Flux Vector**            | The vector field representing total energy carried by the moving fluid per unit area per unit time.         |
| $\mathbf{V}\cdot d\mathbf{S}$                                | **Surface-Crossing Factor**       | The geometric factor that extracts the component of the velocity normal to the surface.                     |
| $\rho\,\mathbf{V}\cdot d\mathbf{S}$                          | **Differential Mass Flow**        | The signed mass flow rate through a surface element.                                                        |
| $e+\frac{V^2}{2}$                                            | **Total Specific Energy**         | The energy carried per unit mass of fluid, including both internal and kinetic energy.                      |
| $\iint_{S}\rho\left(e+\frac{V^2}{2}\right)\mathbf{V}\cdot d\mathbf{S}$ | **Net Convective Energy Flow**    | The net rate at which total energy is transported across the full control surface by bulk fluid motion.     |


# 28. Total surface force due to pressure (Eq. 2.6)

> [!question]
>
> (a) Write the expression for the net surface force due to pressure on a control volume. Why is the negative sign necessary?
> (b) If a control volume is immersed in a fluid at uniform pressure $p_\infty$ everywhere on its surface, what is the net pressure force? Explain physically.
> (c) Under what conditions does a net pressure force arise? Relate this to the concept of a pressure gradient.
> (d) How does this term differ from the pressure *work* term $-\iint_S p\,\mathbf{V}\cdot d\mathbf{S}$ that appears in the energy equation?


> [!equation] Total surface force due to pressure (Eq. 2.6)
>
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




# 29. Volumetric heat addition rate (Eq. 2.13)

> [!question]
>
> (a) Write the expression for $B_1$, the volumetric heat addition rate to the fluid inside the control volume. Identify each factor in the integrand.
> (b) What are some physical sources of volumetric heating $\dot{q}$? Why is thermal conduction across the boundary *not* included in this term for the inviscid formulation?
> (c) Under what conditions is it appropriate to set $B_1 = 0$? What is this assumption called?
> (d) In a jet engine combustion chamber, what physical process does $\dot{q}$ primarily represent?


> [!equation] Volumetric heat addition rate (Eq. 2.13)
>
> $$
> B_1=\iiint_{\mathscr{V}}\dot{q}\,\rho\, d\mathscr{V}
> $$

This integral calculates the total rate at which thermal energy is being "pumped" into the fluid throughout the entire interior of the control volume. It sums every individual contribution of heat, whether from a chemical reaction, radiation, or an internal heating element, acting on the mass within the region. Think of this as the **Internal Furnace** of your system. Unlike heat that passes through the walls (surface conduction), this term represents energy that is generated or absorbed "in the bulk." For a combustion chamber in a jet engine, this is the most critical term because it represents the chemical energy of the fuel being converted into the thermal energy that eventually drives the turbine.


|**Expression**|**Name**|**Description**|
|---|---|---|
|$\dot{q}$|**Specific Heat Addition**|The rate of heat energy added per unit mass (e.g., J/kg·s); represents the "intensity" of the heat source.|
|$\rho \dot{q}$|**Heat Power Density**|The heat energy added per unit volume; determines how much "fire" is packed into a specific point in space.|
|$d\mathscr{V}$|**Differential Volume**|The infinitesimal spatial element used to "sweep" through the entire region $\mathscr{V}$.|
|$\iiint_{\mathscr{V}} \dots d\mathscr{V}$|**Total Thermal Power**|The volume integral that tallies every watt of internal heat to find the net heating rate.|
|$B_1$|**Net Heating Term**|The "Thermal Deposit" in your energy budget; this is the primary driver for increasing the fluid's enthalpy.|


# 30. Calorically perfect gas internal energy


> [!question]
>
> (a) Write the expression for the internal energy per unit mass of a calorically perfect gas.
> (b) What is the central assumption this model makes about the gas, and what does it imply about the relationship between internal energy and temperature?
> (c) Real gases have energy modes (translation, rotation, vibration) that can activate at high temperatures. How does this model treat those modes, and when might that treatment break down?




> [!equation] Calorically perfect gas internal energy
>
> $$
> e=c_v T
> $$

This equation defines a **Linear Energy Storage Model** for a gas. It assumes that the gas’s capacity to absorb and store internal energy—via molecular translation, rotation, and vibration—remains constant regardless of how hot or cold the gas becomes. Think of the gas as a battery with a **Fixed Storage Capacity** ($c_v$). For every degree you raise the temperature, the internal energy "account" ($e$) increases by exactly the same amount. While real gases have "hidden" energy modes that activate at very high temperatures (vibration), this model treats the gas as having a simple, predictable thermal behavior.

| Expression | Name                            | Description                                                           |
| ---------- | ------------------------------- | --------------------------------------------------------------------- |
| $e$        | Internal energy per unit mass   | Thermodynamic internal energy of the gas (per unit mass).             |
| $c_v T$    | Calorically perfect-gas closure | For constant $c_v$, internal energy varies linearly with temperature. |


## Assumptions and Simplifications

1. **Calorically Perfect Gas ($c_v = \text{const}$).** The defining assumption. All molecular energy modes (translation, rotation, vibration) are assumed to contribute a fixed, temperature-independent amount to the heat capacity. This is an excellent approximation for air below roughly 1000 K. Above that threshold, vibrational modes progressively activate, causing $c_v$ to increase with temperature. At that point, the gas is *thermally perfect* ($p = \rho RT$ still holds) but no longer calorically perfect, and $e$ must be computed from $e = \int c_v(T)\, dT$ rather than $c_v T$.
2. **Reference Energy Set to Zero at $T = 0$.** The expression $e = c_v T$ implicitly sets the internal energy datum so that $e = 0$ when $T = 0$. This is a convention, not a physical requirement. In problems involving chemical reactions or multiple species, a different reference state may be needed, and the expression generalizes to $e = c_v (T - T_{\text{ref}}) + e_{\text{ref}}$.
3. **Single-Species or Fixed-Composition Gas.** The value of $c_v$ depends on the molecular weight and degrees of freedom of the gas. If the composition changes (e.g., due to dissociation or combustion), $c_v$ changes as well, and a single constant value no longer applies.

> [!NOTE]
> The companion relation $h = c_p T$ follows from $h = e + p/\rho = c_v T + RT = (c_v + R)T = c_p T$. Both relations share the same assumptions; if one breaks down, so does the other.


# 31. Ideal Gas Linkage Equation (Equation of State)


> [!Question]
>
> (a) Write the ideal gas equation of state in terms of density and the specific gas constant.
> (b) What is the fundamental role this equation plays in connecting the governing equations of fluid dynamics? Which two sets of properties does it bridge?
> (c) The specific gas constant R is defined in terms of two quantities. What are they, and why does R differ from one gas to another?
> (d) Why must temperature be expressed in absolute units (Kelvin or Rankine) rather than Celsius or Fahrenheit for this equation to work?


> [!equation] Ideal Gas Linkage Equation (Equation of State)
>
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


## Assumptions and Simplifications

1. **Molecules Are Point Particles with No Intermolecular Forces.** The ideal gas model assumes that gas molecules occupy negligible volume and exert no attractive or repulsive forces on one another except during brief elastic collisions. This is an excellent approximation when the gas is at low density and high temperature relative to its critical point. It breaks down near condensation, at very high pressures, or at cryogenic temperatures—regimes where real-gas equations of state (e.g., van der Waals, Redlich-Kwong) are needed.
2. **Local Thermodynamic Equilibrium.** The equation assumes that $p$, $\rho$, and $T$ are well-defined at each point, meaning the gas is in local thermodynamic equilibrium. This fails in extreme rarefied flows (high Knudsen number) or in strong non-equilibrium conditions such as the interior of a shock wave at the molecular scale.
3. **Chemically Frozen Composition (Fixed $R$).** The specific gas constant $R = \mathcal{R}/M$ is treated as a constant, which requires the molecular weight $M$ of the gas to be fixed. For air below roughly 2500 K, this is accurate ($R_{\text{air}} \approx 287\;\text{J/(kg·K)}$). At very high temperatures (e.g., hypersonic re-entry), dissociation and ionization change the effective molecular weight, and $R$ becomes a function of temperature and pressure. In such cases $p = \rho RT$ still holds instantaneously, but $R$ must be updated to reflect the local gas composition.
4. **Temperature Must Be Absolute.** $T$ must be in Kelvin or Rankine. Using Celsius or Fahrenheit will produce incorrect results.

> [!NOTE]
> **Thermally Perfect vs. Calorically Perfect.** The ideal gas law $p = \rho RT$ makes the gas *thermally perfect*—it defines the $p$-$\rho$-$T$ relationship. A separate, independent assumption is that the gas is *calorically perfect*, meaning $c_p$ and $c_v$ (and hence $\gamma = c_p/c_v$) are constants independent of temperature. Both assumptions together give a *calorically perfect ideal gas*, the simplest model used extensively in introductory compressible flow. A gas can be thermally perfect without being calorically perfect—this distinction becomes important above roughly 1000 K for air.



# 32. Control Volume Power Balance (Eq. 2.12)


> [!question]
>
> (a) Write the general form of the control volume power balance and identify what each of the three terms represents physically. What kind of quantities are all three terms (i.e., what are their dimensions)?
> (b) If the total power input exceeds the net energy flux leaving the control volume, what must be happening inside the volume?
> (c) What two physical phenomena are excluded from the standard form of this equation due to the inviscid flow assumption? What must be restored if viscous effects matter?
> (d) Under what conditions can you set the net heating power to zero, and what is this assumption called?
> (e) If the flow is steady, which part of the total rate of energy change drops out, and what survives?
> (f) To reduce the steady-flow form down to the familiar thermodynamics equation involving enthalpy, two additional steps are required beyond dropping the time derivative. What are they, and why does enthalpy appear in place of internal energy?


> [!equation] Control Volume Power Balance (Eq. 2.12)
>
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





# 33. Integral continuity equation (Eq. 2.2)

> [!question]
>
> (a) Write the integral form of the continuity equation for a fixed control volume. Identify the two terms and explain what each represents physically.
> (b) Why does the right-hand side equal zero? What physical principle does this reflect?
> (c) The surface integral uses the dot product $\rho\,\mathbf{V}\cdot d\mathbf{S}$. Explain how the sign convention (outward-pointing $d\mathbf{S}$) automatically distinguishes inflow from outflow.
> (d) What happens to the equation under steady-flow conditions? Write the reduced form and explain why it means "what flows in must flow out."
> (e) If the flow is also incompressible ($\rho = \text{const}$), what further simplification occurs? Are "steady" and "incompressible" the same assumption?

> [!equation] Integral continuity equation (Eq. 2.2)
>
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



# 34. Generalized Integral Energy Equation (Eq. 2.20a)

> [!question]
>
> (a) Write the generalized integral energy equation (Eq. 2.20a) and identify every term on both sides.
> (b) In what sense is this the "most complete" energy equation in the chapter? What three phenomena does it include that the inviscid form (Eq. 2.20) does not?
> (c) Explain how you reduce Eq. 2.20a to the inviscid form Eq. 2.20. Which terms are dropped and what physical assumptions justify dropping them?
> (d) Starting from the steady-flow version of this equation, describe the two additional steps needed to arrive at the classical Steady-Flow Energy Equation. Why does enthalpy $h$ appear in place of internal energy $e$?
> (e) Under what conditions is the gravitational potential energy term negligible, and when must it be retained?




$$\dot{Q}+\dot{W}_{\text {shaft }}+\dot{W}_{\text {viscous }}-\iint_S p \mathbf{V} \cdot d \mathbf{S}+\iiint_{\mathscr{Y}} \rho(\mathbf{f} \cdot \mathbf{V}) d \mathscr{Y}$$


> [!equation] Generalized Integral Energy Equation (Eq. 2.20a)
>
> $$
> \dot{Q}+\dot{W}_{\text {shaft}}+\dot{W}_{\text {viscous}}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> $$
>
> $$
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




# 35. Inviscid Integral Energy Equation (Eq. 2.20)

> [!question]
>
> (a) Write the inviscid integral energy equation (Eq. 2.20) and identify all terms on both sides.
> (b) What two assumptions are already built into this equation that distinguish it from the generalized form (Eq. 2.20a)?
> (c) The heating term uses $\dot{q}$ (volumetric heating) rather than $\dot{Q}$ (total heat transfer). What is the physical difference, and why does the inviscid form only include $\dot{q}$?
> (d) What does "adiabatic" mean in the context of this equation, and which term vanishes under that assumption?
> (e) Explain why the total specific energy is $e + V^2/2$ rather than just $e$. Under what conditions could you neglect the kinetic energy contribution?



> [!equation] Inviscid Integral Energy Equation (Eq. 2.20)
>
> $$
> \iiint_{\mathscr{V}} \dot{q}\, \rho\, d \mathscr{V}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> $$
>
> $$
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





# 36. Integral momentum equation (inviscid) (Eq. 2.11)

> [!question]
>
> (a) Write the integral momentum equation for an inviscid flow through a fixed control volume. Identify each term by name and physical role.
> (b) Which fundamental law of physics does this equation represent? How does the left-hand side correspond to "rate of change of momentum" and the right-hand side to "net force"?
> (c) What is the key assumption that makes this the *inviscid* form? What additional term would appear if viscous effects were included?
> (d) In the steady-flow, no-body-force case applied to a duct with one inlet and one exit, show how the equation reduces to an algebraic momentum balance. What quantity plays the role of thrust in this reduced form?
> (e) Explain why the integral momentum equation allows you to calculate engine thrust without knowing the detailed pressure distribution inside the engine.

> [!equation] Integral momentum equation (inviscid) (Eq. 2.11)
>
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




# 37. Integral momentum equation (with viscous surface force) (Eq. 2.11a)

> [!question]
>
> (a) Write the integral momentum equation including viscous surface forces (Eq. 2.11a). How does it differ from the inviscid form (Eq. 2.11)?
> (b) What does $\mathbf{F}_{\text{viscous}}$ physically represent, and why is it called a "lumped" term?
> (c) How do you recover the inviscid momentum equation (Eq. 2.11) from this equation? Under what conditions is that reduction valid?
> (d) For an external aerodynamics problem where you want to compute drag on a body using a control volume, why is it generally unsafe to drop $\mathbf{F}_{\text{viscous}}$?
> (e) In the 1-D uniform inlet/exit simplification, how does the algebraic force balance differ from the inviscid version?

> [!equation] Integral momentum equation (with viscous surface force) (Eq. 2.11a)
>
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





# 38. Newton’s second law (constant mass) (Eq. 2.4)

> [!question]
>
> (a) Write Newton's second law for a body of constant mass. What assumption distinguishes this from the more general form (Eq. 2.3)?
> (b) In the context of fluid mechanics, why is this form insufficient on its own for analyzing a control volume? What complication does a flowing fluid introduce that a solid body does not?
> (c) The general form $\frac{d}{dt}(m\mathbf{V}) = \mathbf{F}$ expands via the product rule into two terms. What are they, and which one vanishes under the constant-mass assumption?


> [!equation] Newton’s second law (constant mass) (Eq. 2.4)
>
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


# 39. Newton’s second law (general form) (Eq. 2.3)

> [!question]
>
> (a) Write Newton's second law in its most general form. Why is this form "more general" than $\mathbf{F} = m\mathbf{a}$?
> (b) In the derivation of the integral momentum equation, this general form serves as the starting point. What two contributions to the time rate of change of momentum emerge when this principle is applied to a fixed control volume?
> (c) Give a physical example of a system where the mass changes with time, making the general form necessary instead of $F = ma$.


> [!equation] Newton’s second law (general form) (Eq. 2.3)
>
> $$
> \frac{d}{dt}(m\mathbf{V})=\mathbf{F}
> $$

This equation states that the net external force acting on a system is equal to the total time rate of change of its momentum. Unlike the simpler $F=ma$ form, this general version allows for the possibility that both the velocity _and_ the mass of the system can vary with time.

| **Expression**              | **Name**                    | **Description**                                                                                                                        |
| --------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| $m\mathbf{V}$               | **Momentum Vector**         | The "quantity of motion"; a vector combining the mass and its current velocity.                                                        |
| $\frac{d}{dt}(m\mathbf{V})$ | **Rate of Momentum Change** | The instantaneous change in the momentum inventory; mathematically, it expands to $m\frac{d\mathbf{V}}{dt} + \mathbf{V}\frac{dm}{dt}$. |
| $\mathbf{F}$                | **Net Force**               | The total external influence acting on the system from the surroundings.                                                               |




# 40. Rocket thrust equation (special case of Eq. 2.45 with $\dot{m}_i=0$)

> [!question]
>
> (a) Write the rocket thrust equation. How is it derived as a special case of the general engine thrust equation (Eq. 2.45)?
> (b) Identify the two physical contributions to rocket thrust and explain what each represents.
> (c) What does it mean for a nozzle to be "perfectly expanded"? Which term in the equation vanishes in that case, and what is thrust then equal to?
> (d) How does the equation simplify for operation in the vacuum of space ($p_\infty = 0$)?
> (e) Unlike a jet engine, a rocket has no inlet momentum drag. Why not?


> [!equation] Rocket thrust equation (special case of Eq. 2.45 with $\dot{m}_i=0$)
>
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


## Assumptions and Simplifications

1. **No Inlet Flow ($\dot{m}_i = 0$).** This is the defining specialization from the general thrust equation (Eq. 2.45). A rocket carries all propellant internally, so there is no incoming airflow and therefore no ram drag.
2. **Steady Flow.** The momentum equation from which Eq. 2.45 was derived assumes steady conditions—constant $\dot{m}_e$, $V_e$, and $p_e$. During transient phases (ignition, throttling, shutdown), the unsteady storage term must be restored.
3. **Inviscid.** Shear stress on the control surface is neglected. Only pressure forces contribute to thrust. This is the same approximation used in deriving the parent equation (Eq. 2.45).
4. **Uniform Exit Properties.** The exit velocity $V_e$, density $\rho_e$, and pressure $p_e$ are assumed uniform across the exit plane $A_e$. Real nozzles have boundary layers and non-uniform exit profiles, so $V_e$ and $p_e$ represent effective averaged values.
5. **Perfectly Expanded Nozzle ($p_e = p_\infty$).** If the nozzle is designed so that the exit pressure matches the ambient pressure exactly, the pressure thrust term $(p_e - p_\infty)A_e$ vanishes, and thrust reduces to $T = \dot{m}_e V_e$—purely momentum thrust. This is the "design" or "optimally expanded" condition.
6. **Vacuum Operation ($p_\infty = 0$).** In space, the pressure thrust simplifies to $p_e A_e$, giving the maximum possible thrust for a given nozzle: $T = \dot{m}_e V_e + p_e A_e$.


# 41. Total force on the control volume (Eq. 2.7)

> [!question]
>
> (a) Write the expression for the total force on the fluid in a control volume for an inviscid flow (Eq. 2.7). Identify the two contributions.
> (b) Explain the physical meaning of the negative sign on the pressure integral.
> (c) If the pressure is uniform over the entire control surface, what does the pressure integral evaluate to? What does this imply about net thrust from uniform pressure?
> (d) This expression represents the $\mathbf{F}$ in Newton's second law. In the integral momentum equation, what appears on the other side of the equals sign?


> [!equation] Total force on the control volume (Eq. 2.7)
>
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



# 42. Total rate of change of energy of the fluid as it flows through the control volume (Eq. 2.19)

> [!question]
>
> (a) Write the expression for $B_3$, the total rate of change of energy of the fluid flowing through the control volume. Identify the two terms and explain what each represents.
> (b) In steady-state flow, which of the two terms vanishes? What survives?
> (c) Explain the parallel structure between $B_3$ (energy), the momentum equation's left-hand side ($\mathbf{A}_1 + \mathbf{A}_2$), and the continuity equation. What pattern do all three share?


> [!equation] Total rate of change of energy of the fluid as it flows through the control volume (Eq. 2.19)
>
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




# 43. Total time rate of change of momentum (Eq. 2.10)

> [!question]
>
> (a) Write the expression for the total time rate of change of momentum of the fluid flowing through a control volume (Eq. 2.10). Identify $\mathbf{A}_1$ and $\mathbf{A}_2$ and explain the physical mechanism each captures.
> (b) In steady flow, which term vanishes and why? What does this mean about the source of all momentum changes?
> (c) During a transient event like rocket ignition, why is $\mathbf{A}_2$ significant?
> (d) This expression equals $\frac{d}{dt}(m\mathbf{V})$ on the left-hand side of Newton's second law. What appears on the right-hand side in the integral momentum equation?


> [!equation] Total time rate of change of momentum (Eq. 2.10)
>
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


# 44. Total work rate on the fluid (Eq. 2.16)

> [!question]
>
> (a) Write the expression for $B_2$, the total mechanical work rate on the fluid (Eq. 2.16). Identify the two contributions and the physical mechanism behind each.
> (b) Why does the pressure work term carry a negative sign while the body force work term does not?
> (c) Under what conditions would the body force work contribution be negligible compared to the pressure work?
> (d) How does $B_2$ combine with $B_1$ in the control volume power balance?


> [!equation] Total work rate on the fluid (Eq. 2.16)
>
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


# 45. Uninstalled engine thrust equation (Eq. 2.45)

> [!question]
>
> (a) Write the uninstalled engine thrust equation (Eq. 2.45) and identify each term by physical name.
> (b) What is "ram drag" and which term represents it? Why does a faster flight speed increase this penalty?
> (c) Under what nozzle condition does the pressure thrust term $(p_e - p_\infty)A_e$ vanish? What is the thrust then equal to?
> (d) The derivation of this equation uses Newton's third law at a key step. Explain where and why.
> (e) Why is this called the "uninstalled" thrust? What effects are excluded by the assumption of uniform $p_\infty$ on the external surface?
> (f) Explain the fundamental advantage of using the integral momentum equation to compute thrust, rather than integrating the detailed pressure distribution over every internal engine component.


> [!equation] Uninstalled engine thrust equation (Eq. 2.45)
>
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


## Assumptions and Simplifications

1. **Steady Flow.** The derivation uses the steady form of the integral momentum equation (no $\partial/\partial t$ storage term). The engine is assumed to be operating at a fixed condition—constant mass flows, velocities, and pressures at the inlet and exit.
2. **Inviscid.** Shear stress on the control surface is neglected; only pressure forces contribute. This is consistent with the parent momentum equation (Eq. 2.11).
3. **No Body Forces.** Gravitational forces on the fluid inside the engine are neglected.
4. **Uniform Properties at Inlet and Exit.** The velocity, density, and pressure are assumed spatially uniform across both $A_i$ and $A_e$. This is the 1-D uniform-flow assumption that converts surface integrals into algebraic products ($\dot{m}V$, $pA$).
5. **Free-Stream Conditions at the Inlet.** The air entering the engine is assumed to arrive at ambient conditions $V_\infty$, $p_\infty$, and $\rho_\infty$. This is the "on-design" assumption. In off-design flight, a streamtube extending far upstream must be used, though the resulting thrust equation has the same form.
6. **Constant $p_\infty$ on the External Surface (Uninstalled Thrust).** The ambient pressure on the outside of the engine is assumed uniform at $p_\infty$. This neglects aerodynamic interference from the aircraft or nacelle, which is why the result is called the *uninstalled* thrust. Installation effects (inlet distortion, nacelle drag) require separate corrections.
7. **Perfectly Expanded Nozzle ($p_e = p_\infty$).** If the nozzle expands the flow until the exit pressure matches ambient, the pressure thrust term vanishes and $T = \dot{m}_e V_e - \dot{m}_i V_\infty$—thrust is entirely due to the net change in momentum flux.
