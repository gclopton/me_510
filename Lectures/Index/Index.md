# ME 510 Detailed Chapter Index

This index is designed for fast topic lookup without rereading full chapters. Each lecture block lists section-level concepts, key equations, assumptions, and search cues.

## Lecture 1: Lagrangian/Eulerian Descriptions and the Material Derivative
Primary source: [[../Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative|Chapter 1 Notes]]
Companion source: [[../Lecture 1: Lagrangian and Eulerian Descriptions, Flow Maps, and the Material Derivative/Lecture 1: Typed Notes|Typed Lecture 1]]

1. Section 1.1 derivative notation and "differentiate before evaluate."
2. Derivative-as-operator viewpoint; avoids ambiguity of writing `d f(x)/d x`.
3. Center-dot notation `f(.)` to mark functional dependence before substitution.
4. Multivariable derivative bookkeeping and explicit "held constant" variable reminders.
5. Why notation rigor matters for later Eulerian vs Lagrangian derivative manipulations.
6. Section 1.2 Lagrangian vs Eulerian descriptions with one spatial coordinate system `x=[x,y,z]`.
7. Lagrangian field form `q^L(x_0,t)` where `x_0` is the material label (initial position).
8. Eulerian field form `q^E(x,t)` at fixed spatial position regardless of material identity.
9. Velocity interpretation contrast: same particle history vs whoever occupies a point.
10. Non-interchangeability warning: `q^L(x,t)` is conceptually invalid.
11. Section 1.3 flow map bridge.
12. Material flow map `x=phi(x_0,t)` and inverse map `x_0=phi^{-1}(x,t)`.
13. Representation transfer identities `q^L(x_0,t)=q^E(phi(x_0,t),t)` and `q^E(x,t)=q^L(phi^{-1}(x,t),t)`.
14. Invertibility and regularity assumptions behind map-based representation changes.
15. Section 1.4 Lagrangian kinematics and fixed-label differentiation.
16. Lagrangian velocity `u^L(x_0,t)=d/dt[phi(x_0,.)]_{x_0}`.
17. Lagrangian acceleration `a^L(x_0,t)=d/dt[u^L(x_0,.)]_{x_0}=d^2/dt^2[phi(x_0,.)]_{x_0}`.
18. General particle-following derivative for any Lagrangian quantity `q^L`.
19. Explicit reminder that "fixed `x_0`" means follow one tagged material element.
20. Section 1.5 Eulerian velocity and substitution-order subtlety.
21. Eulerian velocity as pullback of Lagrangian velocity: `u^E(x,t)=u^L(phi^{-1}(x,t),t)`.
22. Differentiate first at fixed label, substitute `x_0=phi^{-1}(x,t)` afterward.
23. Distinction between fixed-label differentiation and fixed-space differentiation as source of convective terms.
24. Section 1.6 derivation of Eulerian material derivative form.
25. Start from `a_i^E(x,t)=a_i^L(phi^{-1}(x,t),t)` and rewrite via trajectory composition.
26. Chain-rule split into local and convective contributions.
27. Final component form `a_i^E=partial_t u_i^E + u_j^E partial_{x_j} u_i^E`.
28. Final vector form `a^E=partial_t u^E + (u^E . grad)u^E`.
29. Generalization to arbitrary field `q^E`: `Dq^E/Dt = partial_t q^E + (u^E . grad)q^E`.
30. Physical meaning of terms: local unsteady change plus change from motion through spatial gradients.
31. Section 1.7 material derivative operator as representation-independent physics operator.
32. Lagrangian form `(Dq/Dt)^L = partial_t[q^L(x_0,.)]_{x_0}`.
33. Eulerian form `(Dq/Dt)^E = partial_t q^E + (u^E . grad) q^E`.
34. Purpose: distinguish particle-following derivative from fixed-point time derivative.
35. Section 1.8 synthesis and interpretation.
36. One-operator/two-representations viewpoint.
37. Flow-map-centered consistency framework for moving between representations.
38. Search cues: material derivative, convective acceleration, advective term, fixed label, fixed spatial point, flow map, inverse flow map.

## Lecture 2: Reynolds Transport Theorem and Integral-Level Eulerian/Lagrangian Derivatives
Source: [[../Lecture 2: Reynolds Transport Theorem/Lecture 2: Reynolds Transport Theorem|Lecture 2 Notes]]

1. Section 1 preliminaries: derivative meaning for time-dependent integrals over moving regions.
2. Region map `x=psi(xi,t)` for human-defined domain motion, distinct from material map `phi`.
3. Integral target `I_Omega(t)=int_{Omega(t)} q^E(x,t) dV`.
4. Conceptual split: compare corresponding spatial points vs corresponding material elements.
5. Section 2 Eulerian derivative of moving-domain integral.
6. Change of variables to reference region `Omega_ref` using Jacobian `J_psi=det(grad_xi psi)`.
7. Differentiate at fixed reference coordinate `xi`; product rule on `q^E(psi(xi,t),t) J_psi`.
8. Domain velocity field `w^E(x,t)=partial_t psi|_{xi}`.
9. Chain rule term `partial_t q^E + w^E . grad q^E`.
10. Jacobian transport identity `partial_t J_psi = J_psi div w^E`.
11. Volume-form result `d/dt int_{Omega(t)} q^E dV = int_{Omega(t)} [partial_t q^E + div(q^E w^E)] dV`.
12. Boundary-form result `= int_{Omega(t)} partial_t q^E dV + int_{dOmega(t)} q^E w^E . n dS`.
13. Interpretation: mathematical moving-domain derivative; does not track material transport.
14. Section 3 Lagrangian derivative of integral and RTT derivation.
15. Time-dependent material-label set `P(t)={x_0 : phi(x_0,t) in Omega(t)}`.
16. Material-parameterized integral `I_Omega^{x_0}(t)=int_{P(t)} q^L(x_0,t) J_phi(x_0,t) dV_0`.
17. Differentiate with moving domain in material space; includes volume and boundary contributions.
18. Volume rewrite uses material derivative relation and `partial_t J_phi=J_phi div u^E`.
19. Boundary rewrite introduces relative velocity `(u^E-w^E).n` between fluid and control boundary.
20. Reynolds Transport Theorem result:
21. `d/dt int_{Omega(t)} q^E dV = int_{Omega(t)} partial_t q^E dV + int_{dOmega(t)} q^E (u^E-w^E).n dS`.
22. Special case fixed control volume `w^E=0`: standard advective flux term.
23. Special case material volume `w^E=u^E`: boundary flux term vanishes.
24. Section 4 synthesis and analogy with pointwise derivatives.
25. Parameterization, not operator symbol, determines derivative meaning.
26. Eulerian integral derivative for mathematical domain evolution; Lagrangian integral derivative for conservation statements.
27. Search cues: RTT, moving control volume, control-surface velocity, relative flux, material labels in region, Jacobian transport.

## Lecture 3 and 4: Integral Conservation Laws for Compressible Flow
Source: [[../Lecture 3 and 4: Integral Conservation Laws for Compressible Flow/Lecture 3 and 4: Integral Conservation Laws for Compressible Flow|Lectures 3-4 Notes]]

1. Section 1 framework: extensive quantities `Q_Omega(t)=int_{Omega(t)} q^E dV`.
2. Conservation laws interpreted as material-system statements translated to arbitrary control volumes via RTT.
3. Section 2 conservation of mass.
4. Mass integral `M_Omega=int_{Omega(t)} rho^E dV`.
5. Material-system postulate `dM_Omega/dt=0`.
6. Integral balance from RTT: `int_Omega partial_t rho^E dV + int_{dOmega} rho^E (u^E-w^E).n dS = 0`.
7. Interpretation as storage-plus-net-outflow balance.
8. Lagrangian density relation `rho^L(x_0,t)=rho^E(phi(x_0,t),t)`.
9. Jacobian mass identity `rho^E(phi(x_0,t),t) J_phi(x_0,t)=rho_0(x_0)`.
10. Equivalent density evolution `rho^L=rho_0/J_phi`; incompressible special case `J_phi=1`.
11. Section 3 conservation of momentum.
12. Momentum integral `P_Omega=int_{Omega(t)} rho^E u^E dV`.
13. RTT transport term `int_Omega partial_t(rho^E u^E)dV + int_{dOmega} rho^E u^E (u^E-w^E).n dS`.
14. Force decomposition into body forces and surface tractions.
15. Body force form `F_body=int_Omega rho^E f^E dV`.
16. Traction form `F_surf=int_{dOmega} t^E dS`, with Cauchy relation `t^E=sigma^E n`.
17. Stress decomposition `sigma^E = -p^E I + tau^E`.
18. Newtonian deviatoric model `tau^E = mu(grad u^E + grad u^{E,T}) + lambda(div u^E)I`.
19. Stokes hypothesis `lambda = -2mu/3`.
20. Inviscid assumption `tau^E=0`, so `sigma^E=-p^E I`, `t^E=-p^E n`.
21. Integral momentum equation under inviscid model:
22. `int_Omega partial_t(rho^E u^E)dV + int_{dOmega} rho^E u^E (u^E-w^E).n dS = -int_{dOmega} p^E n dS + int_Omega rho^E f^E dV`.
23. Modeling-scope discussion: viscous effects localized in boundary layers/shocks for many compressible regimes.
24. Section 4 conservation of energy.
25. Total energy integral `E_Omega = int_Omega rho^E(e^E + |u^E|^2/2 + Phi) dV`.
26. First-law postulate: rate of total-energy change equals net work plus net heat input.
27. Surface-work term uses relative velocity `t^E . (u^E-w^E)` for moving control boundaries.
28. Body-work term `int_Omega rho^E f^E . u^E dV`.
29. Heat-flux term `-int_{dOmega} q_h^E . n dS`; Fourier model mention `q_h^E = -k grad T^E`.
30. Inviscid integral energy equation with pressure-work and heat-flux contributions.
31. Section 4.6 enthalpy restructuring.
32. Total specific energy `E^E = e^E + |u^E|^2/2 + Phi`.
33. Enthalpy definition `h^E = e^E + p^E/rho^E`.
34. Flux regrouping to `rho^E(h^E + |u^E|^2/2 + Phi)(u^E-w^E).n`.
35. Physical meaning: enthalpy packages internal energy and flow work.
36. Section 4.7 stagnation quantities.
37. Stagnation enthalpy `h_0 = h^E + |u^E|^2/2`.
38. For calorically perfect ideal gas `h^E=c_p T^E`, `h_0=c_p T_0`, `T_0=T^E+|u^E|^2/(2c_p)`.
39. Isentropic stagnation relations:
40. `p_0/p^E = (T_0/T^E)^{gamma/(gamma-1)}` and `rho_0/rho^E = (T_0/T^E)^{1/(gamma-1)}`.
41. Search cues: traction vs body force, inviscid stress, enthalpy-flux form, stagnation invariants, relative boundary velocity.

## Lecture 5: Generalized Quasi-1D Flow in Epsilon Form
Source: [[../Lecture 5: Generalized Quasi-1D Flow in Epsilon Form/Lecture 5: Generalized Quasi-1D Flow in Epsilon Form|Lecture 5 Notes]]

1. Section 1 setup for steady quasi-1D duct flow with varying area `A(x)`.
2. Cross-section-averaged fields `rho(x), u(x), p(x), T(x)`.
3. Included mechanisms: area variation, wall friction, heat transfer, shaft work.
4. Fractional increment definition `epsilon_q = dq/q`.
5. Section 2 continuity derivation from integral mass conservation.
6. Steady fixed-CV mass equation specialized to slender control slice.
7. First-order expansion of `(rho u A)|_{x+dx}`.
8. Continuity epsilon relation (Eq. 2): `epsilon_rho + epsilon_u + epsilon_A = 0`.
9. Section 3 x-momentum derivation.
10. Start from steady integral momentum equation with body force neglected.
11. First-order expansion of momentum flux `(rho u^2 A)|_{x+dx}` gives `epsilon_rho + 2epsilon_u + epsilon_A` on flux side.
12. Pressure forces split into inlet/outlet face contributions plus slanted-wall contribution.
13. Wall geometry identity converts lateral pressure effect to area-change term.
14. Net pressure force reduces to `-A dp` equivalent to `-(p/(rho u^2)) epsilon_p` after normalization.
15. Wall shear force model `F_tau,x = -tau_w P dx` with wetted perimeter `P`.
16. Hydraulic diameter definition `D_h = 4A/P`.
17. Darcy friction factor definition `f = 8 tau_w/(rho u^2)`.
18. Friction increment definition `epsilon_f = f dx / D_h` (not state-variable differential).
19. Final momentum epsilon relation (Eq. 4):
20. `epsilon_rho + 2epsilon_u + epsilon_A = -(1/(gamma M^2))epsilon_p - (1/2)epsilon_f`.
21. Section 4 energy equation in quasi-1D enthalpy-flux form.
22. Steady equation (Eq. 5): boundary integral of `rho(h+u^2/2) u.n` equals heat/work input rates.
23. Constant mass-flow simplification to Eq. 6: `d(h+u^2/2) = (delta Qdot + delta Wdot)/mdot`.
24. Stagnation temperature relation from calorically perfect gas `h=c_p T`, `h_0=c_p T_0`.
25. Epsilon energy relation (Eq. 7):
26. `epsilon_T + (gamma-1)M^2 epsilon_u - (1 + (gamma-1)M^2/2)epsilon_T0 = 0`.
27. Section 5 equation-of-state closure.
28. From `p=rho R T`, first-order expansion gives `epsilon_p = epsilon_rho + epsilon_T`.
29. Structural outcome: linear local relations in epsilon-space linking state and forcing increments.
30. Search cues: quasi-1D derivation, hydraulic diameter normalization, friction increment, linearized control-volume expansions.

## Lecture 6: Input-Output Form and Influence Coefficients
Source: [[../Lecture 6: Input-Output Form and Influence Coefficients/Lecture 6: Input-Output Form and Influence Coefficients|Lecture 6 Notes]]

1. Section 1 objective: reorganize Lecture 5 equations into engineering response map.
2. Section 2 recap of four governing epsilon equations (continuity, momentum, energy, EOS).
3. Driver-response modeling choice to close underdetermined 4-equation/7-unknown local system.
4. Section 3.1 input vector choice:
5. `epsilon_A` (geometry forcing), `epsilon_f` (friction forcing), `epsilon_T0` (heat/work forcing).
6. Section 3.2 output vector choice:
7. `epsilon_u, epsilon_p, epsilon_rho, epsilon_T` as local flow responses.
8. Section 4 matrix structure `A(M) epsilon_out = B(M) epsilon_in`.
9. Explicit `A(M)` rows map directly to continuity, momentum, energy, EOS.
10. Explicit `B(M)` rows encode where each driver appears in governing equations.
11. Sonic structural singularity: `det A(M)=0` at `M=1`.
12. Linear dependence identity at `M=1`:
13. `(gamma+1)*continuity - gamma*momentum + energy + EOS = 0`.
14. Interpretation: sonic condition as algebraic degeneracy of local linear closure.
15. Section 5 influence-coefficient map for `M!=1`.
16. Define `C(M)=A(M)^{-1}B(M)`.
17. Response form `epsilon_out = C(M) epsilon_in`.
18. Entries `C_{ij}` interpreted as local sensitivities of each response to each driver.
19. Explicit closed-form coefficients all contain denominator `(1-M^2)`.
20. Example velocity equation:
21. `epsilon_u = C_{uA} epsilon_A + C_{uf} epsilon_f + C_{uT0} epsilon_T0`.
22. Section 6 derived quantities from primary coefficients.
23. Mach-number change: `epsilon_{M^2}=2epsilon_u-epsilon_T`; coefficients are linear combinations of primary `C` entries.
24. Stagnation-pressure increment (locally isentropic): `epsilon_{p0}=epsilon_p + gamma/(gamma-1)(epsilon_T0-epsilon_T)`.
25. Entropy increment for ideal gas: `epsilon_s = epsilon_T - (gamma-1)/gamma epsilon_p`.
26. Core point: no extra conservation equations needed for derived-variable sensitivities.
27. Search cues: influence matrix, driver/output split, sonic matrix singularity, derived influence coefficients.

## Lecture 7: Interpretation of Influence Coefficients and Global Marching
Source: [[../Lecture 7: Interpretation of Influence Coefficients and Global Marching/Lecture 7: Interpretation of Influence Coefficients and Global Marching|Lecture 7 Notes]]

1. Section 1 interpretation scope: `epsilon_out = C(M) epsilon_in` as local sensitivity model, not new physics.
2. Coefficient meaning by entry: response sign, response magnitude, Mach dependence.
3. Linearization scope: valid over small streamwise increments.
4. Section 2 single-driver interpretation.
5. Area-only forcing: `epsilon_u = C_{uA} epsilon_A`, `C_{uA}=-1/(1-M^2)`.
6. Subsonic `M<1`: area increase decelerates; area decrease accelerates.
7. Supersonic `M>1`: area increase accelerates; area decrease decelerates.
8. Friction-only forcing: `epsilon_u=C_{uf} epsilon_f`, `C_{uf}=gamma M^2/[2(1-M^2)]`.
9. Subsonic: friction accelerates; supersonic: friction decelerates.
10. Heat/work-only forcing: `epsilon_u=C_{uT0} epsilon_T0`, `C_{uT0}=[2+(gamma-1)M^2]/[2(1-M^2)]`.
11. Subsonic heat addition accelerates; supersonic heat addition decelerates.
12. Unifying structural factor across responses: denominator `(1-M^2)`.
13. Section 3 sonic condition and choking origin.
14. As `M -> 1`, coefficients diverge; local smooth-response model breaks down.
15. Interpretation framed as incompatibility of subsonic and supersonic response rules at the sonic limit.
16. Section 4 global solution construction from local algebraic map.
17. Frozen-coefficient assumption over small `dx`: `C(M(x))` treated constant on each step.
18. Marching cycle: evaluate `M`, build `C(M)`, apply drivers, compute `epsilon` responses, update state.
19. Exponential update relation from `dq/q = epsilon_q`:
20. `q(x+dx)=q(x) exp(epsilon_q)`.
21. Perspective: assemble global behavior from repeated local algebraic updates.
22. Section 4.3 limits: near sonic conditions, shocks, or strongly nonlinear/large-step variation.
23. Section 5 model validity assumptions: quasi-1D, steady local behavior, smoothness, no discontinuities, small increments.
24. Non-captured physics: shock dynamics, multidimensional effects, transient behavior.
25. Search cues: frozen-coefficient marching, choking indicator via coefficient blow-up, subsonic/supersonic sign reversal.

## Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure
Source: [[../Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure/Lecture 8: PDE Conservation Laws, Primitive Forms, and Thermodynamic Closure|Lecture 8 Notes]]

1. Section 1 motivation for PDE form: local structure, propagation, classification, and numerics.
2. Section 2 conservative PDE forms (inviscid compressible flow):
3. Mass: `partial_t rho + div(rho u)=0`.
4. Momentum: `partial_t(rho u)+div(rho u tensor u) = -grad p + rho f`.
5. Energy: `partial_t(rho E)+div((rho E + p)u)=rho f.u - div q_h + rho qdot_h`.
6. Conservative form as local encoding of integral conservation laws.
7. Smooth-vs-nonsmooth distinction: integral law remains fundamental at discontinuities.
8. Section 3 primitive/non-conservative forms via material derivative.
9. Mass primitive: `D rho/Dt + rho div u = 0`.
10. Momentum primitive: `rho D u/Dt = -grad p + rho f`.
11. Internal-energy primitive: `rho D e/Dt = -p div u - div q_h + rho qdot_h`.
12. Material derivative definition `D()/Dt = partial_t() + u.grad()`.
13. Momentum derivation pathway: expand conservative form with product rules, then cancel using continuity.
14. Interpretation: primitive form reorganizes physics into particle-acceleration form; not new law.
15. Section 4 discontinuity interpretation.
16. Conservative form retains boundary-flux meaning via integral balances when shocks exist.
17. Primitive form lacks direct control-volume flux interpretation at jumps due to smoothness reliance.
18. Practical rule: use conservative form for shock/discontinuous solutions.
19. Section 5 energy equations in multiple equivalent organizations.
20. Conservative total-energy equation retained as transport-flux form.
21. Derive primitive internal-energy form through expansion, continuity, and momentum substitution/cancellation.
22. Enthalpy form derivation:
23. `h=e+p/rho`, then `rho Dh/Dt = Dp/Dt - div q_h + rho qdot_h`.
24. Conceptual split: transport-across-boundary view vs along-particle evolution view.
25. Section 6 thermodynamic closure necessity.
26. Euler equations provide 5 conservation PDEs; pressure requires constitutive relation from thermodynamic model.
27. Closure example with internal-energy state variable: `p=p(rho,e)`.
28. Calorically perfect ideal-gas closure chain:
29. `p=rho R T`, `e=c_v T`, `gamma=c_p/c_v`, `c_p-c_v=R`, leading to `p=(gamma-1)rho e`.
30. More general closure contexts: thermally imperfect gases, real-gas EOS, reacting/multispecies systems.
31. Structural principle: conservation equations + thermodynamic closure together determine evolution.
32. Search cues: conservative vs primitive PDE, shock-consistent formulation, internal-energy equation derivation, thermodynamic closure.

## Fast Cross-Chapter Lookup Anchors

1. Eulerian vs Lagrangian derivative meaning: Lecture 1 and Lecture 2.
2. Reynolds transport theorem derivation and control-volume velocity term `(u-w).n`: Lecture 2.
3. Integral mass/momentum/energy balances for arbitrary moving control volumes: Lecture 3 and 4.
4. Enthalpy and stagnation-property derivations: Lecture 3 and 4.
5. Quasi-1D epsilon equations from integral laws: Lecture 5.
6. Influence-coefficient matrix and sonic singularity: Lecture 6.
7. Physical sign interpretation and marching strategy: Lecture 7.
8. Conservative PDE form vs primitive form at discontinuities: Lecture 8.
9. Thermodynamic closure and ideal-gas reduction `p=(gamma-1)rho e`: Lecture 8.
