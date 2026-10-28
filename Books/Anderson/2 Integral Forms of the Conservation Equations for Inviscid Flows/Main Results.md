# Main Results — Anderson, Chapter 2

For explanations of each equation, see `Equation Index.md`. For symbol meanings and units, see `Symbol Index.md`.

## Continuity (Conservation of Mass)

> [!equation] Mass flow through an elemental surface (Eq. 2.1)
> $$
> \dot{m}=\rho(V\cos\theta)\, dS=\rho V_n\, dS=\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

> [!equation] Net mass flow into a fixed control volume
> $$
> -\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}
> $$

> [!equation] Mass contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\, d\mathscr{V}
> $$

> [!equation] Integral continuity equation (Eq. 2.2)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\, d\mathscr{V}+\iint_{S}\rho\,\mathbf{V}\cdot d\mathbf{S}=0
> $$

## Momentum (Newton’s Second Law)

> [!equation] Newton’s second law (general form) (Eq. 2.3)
> $$
> \frac{d}{dt}(m\mathbf{V})=\mathbf{F}
> $$

> [!equation] Newton’s second law (constant mass) (Eq. 2.4)
> $$
> \mathbf{F}=m\frac{d\mathbf{V}}{dt}=m\mathbf{a}
> $$

> [!equation] Total body force acting on the control volume (Eq. 2.5)
> $$
> \iiint_{\mathscr{V}}\rho\,\mathbf{f}\, d\mathscr{V}
> $$

> [!equation] Total surface force due to pressure (Eq. 2.6)
> $$
> -\iint_{S}p\, d\mathbf{S}
> $$

> [!equation] Total force on the control volume (Eq. 2.7)
> $$
> \mathbf{F}=\iiint_{\mathscr{V}}\rho\,\mathbf{f}\, d\mathscr{V}-\iint_{S}p\, d\mathbf{S}
> $$

> [!equation] Momentum flux across the control surface (Eq. 2.8)
> $$
> \mathbf{A}_1=\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}
> $$

> [!equation] Momentum contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

> [!equation] Unsteady (transient) momentum term (Eq. 2.9)
> $$
> \mathbf{A}_2=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> =\iiint_{\mathscr{V}}\frac{\partial(\rho\,\mathbf{V})}{\partial t}\, d\mathscr{V}
> $$

> [!equation] Total time rate of change of momentum (Eq. 2.10)
> $$
> \frac{d}{dt}(m\mathbf{V})=\mathbf{A}_1+\mathbf{A}_2
> =\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\,\mathbf{V}+\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\,\mathbf{V}\, d\mathscr{V}
> $$

> [!equation] Integral momentum equation (inviscid) (Eq. 2.11)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}
> +\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}
> =\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_{S} p\, d \mathbf{S}
> $$

> [!equation] Integral momentum equation (with viscous surface force) (Eq. 2.11a)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho \mathbf{V}\, d\mathscr{V}
> +\iint_{S}(\rho \mathbf{V} \cdot d \mathbf{S}) \mathbf{V}
> =\iiint_{\mathscr{V}} \rho \mathbf{f}\, d\mathscr{V}-\iint_{S} p\, d \mathbf{S}+\mathbf{F}_{\text{viscous}}
> $$

## Energy (First Law of Thermodynamics)

> [!equation] First law bookkeeping for the control volume (Eq. 2.12)
> $$
> B_1+B_2=B_3
> $$

> [!equation] Volumetric heat addition rate (Eq. 2.13)
> $$
> B_1=\iiint_{\mathscr{V}}\dot{q}\,\rho\, d\mathscr{V}
> $$

> [!equation] Mechanical power (rate of doing work on a moving body)
> $$
> \dot{W}=\mathbf{F}\cdot\mathbf{V}
> $$

> [!equation] Rate of work on the fluid due to pressure forces (Eq. 2.14)
> $$
> -\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}
> $$

> [!equation] Rate of work on the fluid due to body forces (Eq. 2.15)
> $$
> \iiint_{\mathscr{V}}\rho(\mathbf{f}\cdot\mathbf{V})\, d\mathscr{V}
> $$

> [!equation] Total work rate on the fluid (Eq. 2.16)
> $$
> B_2=-\iint_{S} p\,\mathbf{V}\cdot d\mathbf{S}+\iiint_{\mathscr{V}}\rho(\mathbf{f}\cdot\mathbf{V})\, d\mathscr{V}
> $$

> [!equation] Net rate of energy flow across the control surface (Eq. 2.17)
> $$
> \iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)
> $$

> [!equation] Energy contained inside the control volume
> $$
> \iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> $$

> [!equation] Time rate of change of energy inside the control volume (Eq. 2.18)
> $$
> \frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> $$

> [!equation] Total rate of change of energy of the fluid as it flows through the control volume (Eq. 2.19)
> $$
> B_3=\frac{\partial}{\partial t}\iiint_{\mathscr{V}}\rho\left(e+\frac{V^2}{2}\right)\, d\mathscr{V}
> +\iint_{S}(\rho\,\mathbf{V}\cdot d\mathbf{S})\left(e+\frac{V^2}{2}\right)
> $$

> [!equation] Integral energy equation (inviscid) (Eq. 2.20)
> $$
> \iiint_{\mathscr{V}} \dot{q}\, \rho\, d \mathscr{V}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> =\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho\left(e+\frac{V^{2}}{2}\right)\, d \mathscr{V}
> +\iint_{S} \rho\left(e+\frac{V^{2}}{2}\right) \mathbf{V} \cdot d \mathbf{S}
> $$

> [!equation] Integral energy equation (generalized with $\dot{Q}$ and work terms) (Eq. 2.20a)
> $$
> \dot{Q}+\dot{W}_{\text {shaft}}+\dot{W}_{\text {viscous}}
> -\iint_{S} p\, \mathbf{V} \cdot d \mathbf{S}
> +\iiint_{\mathscr{V}} \rho(\mathbf{f} \cdot \mathbf{V})\, d \mathscr{V}
> =\frac{\partial}{\partial t}\iiint_{\mathscr{V}} \rho\left(e+\frac{V^{2}}{2}\right)\, d \mathscr{V}
> +\iint_{S} \rho\left(e+\frac{V^{2}}{2}\right) \mathbf{V} \cdot d \mathbf{S}
> $$

## Application: Jet/Rocket Thrust

> [!equation] Uninstalled engine thrust equation (Eq. 2.45)
> $$
> T=\dot{m}_{e} V_{e}-\dot{m}_{i} V_{\infty}+\left(p_{e}-p_{\infty}\right) A_{e}
> $$

> [!equation] Rocket thrust equation (special case of Eq. 2.45 with $\dot{m}_i=0$)
> $$
> T=\dot{m}_{e} V_{e}+\left(p_{e}-p_{\infty}\right) A_{e}
> $$

## Closure Relations Mentioned in the Chapter

> [!equation] Equation of state (ideal gas)
> $$
> p=\rho R T
> $$

> [!equation] Calorically perfect gas internal energy
> $$
> e=c_v T
> $$
