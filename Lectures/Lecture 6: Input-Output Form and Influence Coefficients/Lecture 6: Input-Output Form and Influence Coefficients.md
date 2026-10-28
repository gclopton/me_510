## 1 From governing equations to a usable framework

In Lecture 5, we derived a closed set of local quasi-1D relations in $\varepsilon$-form by specializing the integral conservation laws. Today we do no new physics. Instead, we reorganize those relations to answer a different (and more engineering-relevant) question:

If I impose a small geometric change, frictional loss, or heat/work input, how does the flow respond locally?

The central outcome is an input-output map:

[]

$$
(\text { responses })=(\text { Mach-dependent influence coefficients }) \times(\text { drivers })
$$

## 2 Recap: the local $\varepsilon$-system from Lecture 5

We collect the quasi-1D relations (valid locally between $x$ and $x+d x$ ):

$$
\begin{align*}
\varepsilon_{\rho}+\varepsilon_{u}+\varepsilon_{A} & =0  \tag{1}\\
\varepsilon_{\rho}+2 \varepsilon_{u}+\varepsilon_{A} & =-\frac{1}{\gamma M^{2}} \varepsilon_{p}-\frac{1}{2} \varepsilon_{f}  \tag{2}\\
\varepsilon_{T}+(\gamma-1) M^{2} \varepsilon_{u}-\left(1+\frac{\gamma-1}{2} M^{2}\right) \varepsilon_{T_{0}} & =0  \tag{3}\\
\varepsilon_{p} & =\varepsilon_{\rho}+\varepsilon_{T} \tag{4}
\end{align*}
$$

Reminder: what are these $\varepsilon$ 's? Recall $\varepsilon_{q}=d q / q$ for state variables $q \in\left\{\rho, u, p, T, T_{0}, A\right\}$. The friction increment

$$
\varepsilon_{f}:=\frac{f d x}{D_{h}}
$$

is not the differential of a state variable; it measures cumulative momentum loss over the slice of length $d x$.

## 3 Drivers vs. responses: breaking the symmetry on purpose

Mathematically, the local $\varepsilon$-system (1)-(4) treats all fractional changes on equal footing. Each $\varepsilon$ appears as an unknown in a linear algebraic system, and there is no inherent distinction between "inputs" and "outputs."

The problem is that the equations (1)-(4) are not closed: there are four equations for seven unknowns! Fortunately, we can rely on physical intuition to interpret some fractional changes as imposed (inputs), and others as flow responses (outputs) to that stimulus.

A modeling choice. At each streamwise station, some effects are imposed on the flow by design, material properties, or external interaction, while others represent the flow's response. We now make a deliberate modeling choice to reflect this asymmetry.

### 3.1 Driving increments (inputs)

We designate the following quantities as drivers:

$$
\varepsilon_{A}, \quad \varepsilon_{f}, \quad \varepsilon_{T_{0}} .
$$

These increments are not determined by the local fluid state; instead, they are specified externally:

- $\varepsilon_{A}$ represents geometric forcing through area variation,
- $\varepsilon_{f}$ represents frictional forcing due to wall shear,
- $\varepsilon_{T_{0}}$ represents thermal or mechanical forcing through heat transfer or shaft work.

In practice, these quantities are known from geometry, wall properties, or operating conditions.

### 3.2 Flow responses (outputs)

The remaining fractional changes describe how the flow responds locally:

$$
\begin{array}{|llll}
\hline \varepsilon_{u}, & \varepsilon_{p}, & \varepsilon_{\rho}, & \varepsilon_{T} . \\
\hline
\end{array}
$$

These quantities are not prescribed; they are determined by the governing equations once the drivers are specified.

Why this split is useful. This input-output distinction is both required to mathematically close the system, and is essential conceptually. It allows us to reinterpret the quasi-1D governing equations as a local response model:

Given a small imposed change in geometry, friction, or energy input, how does the flow adjust locally?

In the sections that follow, this modeling choice will allow the governing equations to be reorganized into an explicit linear map from driving increments to flow responses, with coefficients that depend only on the local Mach number.

## 4 Algebraic structure: a local linear system parameterized by $M$

With the input-output distinction in place, we now return to the governing $\varepsilon$-system (1)-(4) and reorganize it algebraically.

Our goal in this section is not to solve the equations, but to make their structure explicit.

### 4.1 Collecting the governing equations

We treat the flow responses

$$
\varepsilon_{\mathrm{out}}=\left[\begin{array}{c}
\varepsilon_{\rho} \\
\varepsilon_{u} \\
\varepsilon_{p} \\
\varepsilon_{T}
\end{array}\right]
$$

as unknowns, and the driving increments

$$
\varepsilon_{\mathrm{in}}=\left[\begin{array}{c}
\varepsilon_{A} \\
\varepsilon_{f} \\
\varepsilon_{T_{0}}
\end{array}\right]
$$

as prescribed inputs.
Equations (1)-(4) may then be written in the matrix form

$$
\begin{equation*}
\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }} \tag{5}
\end{equation*}
$$

where the coefficient matrices depend only on the local Mach number $M$ (and $\gamma$ ).

### 4.2 Explicit form of the coefficient matrices

Writing each governing equation as a row of the system gives

$$
\boldsymbol{A}(M)=\left[\begin{array}{cccc}
1 & 1 & 0 & 0 \\
1 & 2 & \frac{1}{\gamma M^{2}} & 0 \\
0 & (\gamma-1) M^{2} & 0 & 1 \\
-1 & 0 & 1 & -1
\end{array}\right], \quad \boldsymbol{B}(M)=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
-1 & -\frac{1}{2} & 0 \\
0 & 0 & 1+\frac{\gamma-1}{2} M^{2} \\
0 & 0 & 0
\end{array}\right] .
$$

Each row corresponds directly to one of the governing relations:

- Row 1: continuity (1),
- Row 2: $x$-momentum (2),
- Row 3: energy (3),
- Row 4: equation of state (4).

Remark. Nothing new has been introduced here. The matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ are simply a compact restatement of the quasi-1D governing equations derived in Lecture 5.

### 4.3 Structural singularity at the sonic condition

The algebraic system (5) can be solved for the flow responses only if the matrix $\boldsymbol{A}(M)$ is invertible. A direct calculation shows that

$$
\operatorname{det} \boldsymbol{A}(M)=0 \quad \text { when } \quad M=1
$$

Equivalently, at $M=1$ the four governing equations become linearly dependent: at $M=1$ one finds

$$
(\gamma+1) \times(\text { continuity })-\gamma \times(\text { momentum })+(\text { energy })+(\text { equation of state }) \equiv 0 \quad(M=1) .
$$

Thus, at the sonic condition, one of the four equations carries no independent information beyond the other three.

We emphasize that, at this stage, this is simply an algebraic observation. Its physical implications will be discussed in the next lecture.

### 4.4 Interpretation of the matrix form

Equation (5) shows that quasi-1D compressible flow, under the assumptions of the prior lecture, is governed locally by a linear system whose coefficients depend only on the Mach number.

Once the driving increments are specified, the flow responses are determined algebraicallyprovided $M \neq 1$. This observation underlies the influence-coefficient framework developed in the next section.

## 5 The input-output map and influence coefficients

With the driver-response split in place, the local quasi-1D system can now be interpreted as an explicit input-output relation. This is the central structural result of the quasi-1D theory.

### 5.1 Definition of the input-output matrix

For $M \neq 1$, the matrix $\boldsymbol{A}(M)$ is invertible. We therefore define the input-output matrix

$$
\begin{equation*}
\boldsymbol{C}(M):=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M) \tag{6}
\end{equation*}
$$

The governing equations may now be written compactly as

$$
\left[\begin{array}{l}
\varepsilon_{\rho}  \tag{7}\\
\varepsilon_{u} \\
\varepsilon_{p} \\
\varepsilon_{T}
\end{array}\right]=\left[\begin{array}{lll}
C_{\rho A}(M) & C_{\rho f}(M) & C_{\rho T_{0}}(M) \\
C_{u A}(M) & C_{u f}(M) & C_{u T_{0}}(M) \\
C_{p A}(M) & C_{p f}(M) & C_{p T_{0}}(M) \\
C_{T A}(M) & C_{T f}(M) & C_{T T_{0}}(M)
\end{array}\right]\left[\begin{array}{c}
\varepsilon_{A} \\
\varepsilon_{f} \\
\varepsilon_{T_{0}}
\end{array}\right],
$$

where we have detailed the components in $\boldsymbol{C}$ symbolically to make it clear which input coefficient is impacting which output coefficient.

Explicit form of the input-output matrix. Evaluating $\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$ yields

$$
C(M)=\left[\begin{array}{ccc}
\frac{M^{2}}{1-M^{2}} & -\frac{\gamma M^{2}}{2\left(1-M^{2}\right)} & -\frac{2+(\gamma-1) M^{2}}{2\left(1-M^{2}\right)} \\
-\frac{1}{1-M^{2}} & \frac{\gamma M^{2}}{2\left(1-M^{2}\right)} & \frac{2+(\gamma-1) M^{2}}{2\left(1-M^{2}\right)} \\
\frac{\gamma M^{2}}{1-M^{2}} & -\frac{\gamma M^{2}\left(1+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)} & -\frac{\gamma M^{2}\left(2+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)} \\
\frac{(\gamma-1) M^{2}}{1-M^{2}} & -\frac{\gamma(\gamma-1) M^{4}}{2\left(1-M^{2}\right)} & \frac{\left(1-\gamma M^{2}\right)\left(2+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)}
\end{array}\right]
$$

This relation is purely algebraic and local: it holds between $x$ and $x+d x$ and contains no spatial derivatives.

### 5.2 Meaning of the influence coefficients

Each entry of $\boldsymbol{C}(M)$ is an influence coefficient. For example, the second row of (7) reads

$$
\varepsilon_{u}=C_{u A}(M) \varepsilon_{A}+C_{u f}(M) \varepsilon_{f}+C_{u T_{0}}(M) \varepsilon_{T_{0}},
$$

where:

- $C_{u A}$ quantifies acceleration due to area change,
- $C_{u f}$ quantifies deceleration due to friction,
- $C_{u T_{0}}$ quantifies acceleration or deceleration due to heat/work input.

Analogous expressions hold for $\varepsilon_{p}, \varepsilon_{\rho}$, and $\varepsilon_{T}$. Thus, each row of $\boldsymbol{C}$ corresponds to one flow response, and each column corresponds to one driving mechanism.

Key structural point. Once $M$ and $\gamma$ are specified, all influence coefficients are known. No further differential equations need to be solved to determine the local flow response.

In what follows, we will focus on interpreting these coefficients and using them to construct solutions. Derived quantities (such as stagnation pressure, entropy, or Mach number change) will be obtained subsequently from the primary variables and are discussed separately.

## 6 Derived quantities and extended influence coefficients

The input-output map (7) provides the local response of the primary flow variables

$$
\left(\varepsilon_{\rho}, \varepsilon_{u}, \varepsilon_{p}, \varepsilon_{T}\right)
$$

to imposed driving increments. Many quantities of engineering interest, however, are not primary variables but are instead functions of these fields.

In this section we show how influence coefficients for such derived quantities follow directly from the primary coefficients, without introducing new governing equations.

### 6.1 Mach number

The Mach number is defined as

$$
M^{2}=\frac{u^{2}}{\gamma R T}
$$

Taking a differential and dividing by $M^{2}$ gives

$$
\varepsilon_{M^{2}}=2 \varepsilon_{u}-\varepsilon_{T} .
$$

Substituting the input-output relations for $\varepsilon_{u}$ and $\varepsilon_{T}$ yields

$$
\varepsilon_{M^{2}}=\left(2 C_{u A}-C_{T A}\right) \varepsilon_{A}+\left(2 C_{u f}-C_{T f}\right) \varepsilon_{f}+\left(2 C_{u T_{0}}-C_{T T_{0}}\right) \varepsilon_{T_{0}} .
$$

Thus, influence coefficients for $M^{2}$ are obtained by simple linear combinations of the primary coefficients.

### 6.2 Stagnation pressure

For an ideal gas undergoing locally isentropic changes, the stagnation pressure satisfies

$$
\frac{p_{0}}{p}=\left(\frac{T_{0}}{T}\right)^{\frac{\gamma}{\gamma-1}}
$$

Taking a differential gives

$$
\varepsilon_{p_{0}}=\varepsilon_{p}+\frac{\gamma}{\gamma-1}\left(\varepsilon_{T_{0}}-\varepsilon_{T}\right)
$$

Substituting the input-output expressions for $\varepsilon_{p}$ and $\varepsilon_{T}$ yields

$$
\varepsilon_{p_{0}}=\left(C_{p A}-\frac{\gamma}{\gamma-1} C_{T A}\right) \varepsilon_{A}+\left(C_{p f}-\frac{\gamma}{\gamma-1} C_{T f}\right) \varepsilon_{f}+\left(C_{p T_{0}}+\frac{\gamma}{\gamma-1}\left(1-C_{T T_{0}}\right)\right) \varepsilon_{T_{0}}
$$

### 6.3 Entropy

For a calorically perfect ideal gas, the differential entropy change satisfies

$$
d s=c_{p} \frac{d T}{T}-R \frac{d p}{p}
$$

Dividing by $c_{p}$ and writing in $\varepsilon$-form gives

$$
\varepsilon_{s}:=\frac{d s}{c_{p}}=\varepsilon_{T}-\frac{\gamma-1}{\gamma} \varepsilon_{p}
$$

Substituting the primary input-output relations yields

$$
\varepsilon_{s}=\left(C_{T A}-\frac{\gamma-1}{\gamma} C_{p A}\right) \varepsilon_{A}+\left(C_{T f}-\frac{\gamma-1}{\gamma} C_{p f}\right) \varepsilon_{f}+\left(C_{T T_{0}}-\frac{\gamma-1}{\gamma} C_{p T_{0}}\right) \varepsilon_{T_{0}} .
$$

Summary. Once the primary influence coefficients are known, influence coefficients for any derived quantity may be obtained by algebraic manipulation alone. No additional conservation laws or differential equations are required.

