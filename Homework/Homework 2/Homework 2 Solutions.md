
Grady Clopton
ME 510
Homework 2

# Problem 1: Structure and singularity of the quasi-1D $\varepsilon$-system


**Preamble.** In Lectures 5-7, we reformulated the quasi-one-dimensional governing equations as a local linear system relating imposed driving increments (area variation, friction, and heat/work input) to the resulting flow response. The goal of this problem is to examine the structure of that system, understand the origin of the sonic singularity, and connect the algebraic behavior to physical interpretation.

Throughout this problem, assume a calorically perfect ideal gas with constant $\gamma$, and use the local $\varepsilon$-form governing equations:

$$
\begin{aligned}
\varepsilon_\rho+\varepsilon_u+\varepsilon_A & =0, \\
\varepsilon_\rho+2 \varepsilon_u+\varepsilon_A & =-\frac{1}{\gamma M^2} \varepsilon_p-\frac{1}{2} \varepsilon_f, \\
\varepsilon_T+(\gamma-1) M^2 \varepsilon_u-\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0} & =0, \\
\varepsilon_p & =\varepsilon_\rho+\varepsilon_T .
\end{aligned}
$$

> [!question] (a) Casting the governing equations as a linear system
> 
> 
> Identify the driving increments $\varepsilon_{\text {in }}$ and the flow responses $\varepsilon_{\text {out }}$.
> Recast the four governing equations in the schematic matrix form
> 
> $$
> \boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }},
> $$
> 
> clearly indicating how many equations and unknowns are present, which quantities are treated as inputs and which as outputs, how the Mach number enters the system.
> You do not need to write out all entries of $\boldsymbol{A}$ and $\boldsymbol{B}$ explicitly here, but your expressions should make their dependence on $M$ clear.


The local $\varepsilon$-system contains four governing equations but seven fractional increments $\left\{\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T, \varepsilon_A, \varepsilon_f, \varepsilon_{T_0}\right\}$. To make a determinate linear system, three increments are treated as imposed drivers and the remaining four are treated as flow responses. The natural split for quasi-1D flow is

$$
\varepsilon_{\mathrm{in}}=\left[\begin{array}{c}
\varepsilon_A \\
\varepsilon_f \\
\varepsilon_{T_0}
\end{array}\right], \quad \varepsilon_{\mathrm{out}}=\left[\begin{array}{c}
\varepsilon_\rho \\
\varepsilon_u \\
\varepsilon_p \\
\varepsilon_T
\end{array}\right],
$$

so that there are four equations for the four unknown outputs once the three inputs are specified.
Now rewrite each governing equation with all outputs on the left and all inputs on the right.
From continuity,

$$
\varepsilon_\rho+\varepsilon_u+\varepsilon_A=0 \Longrightarrow \varepsilon_\rho+\varepsilon_u=-\varepsilon_A .
$$


From the momentum-type relation,

$$
\varepsilon_\rho+2 \varepsilon_u+\varepsilon_A=-\frac{1}{\gamma M^2} \varepsilon_p-\frac{1}{2} \varepsilon_f
$$

bring $\varepsilon_p$ to the left and $\varepsilon_A$ to the right:

$$
\varepsilon_\rho+2 \varepsilon_u+\frac{1}{\gamma M^2} \varepsilon_p=-\varepsilon_A-\frac{1}{2} \varepsilon_f
$$


From the energy/total-temperature relation,

$$
\varepsilon_T+(\gamma-1) M^2 \varepsilon_u-\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0}=0
$$

move the $\varepsilon_{T_0}$ term to the right:

$$
(\gamma-1) M^2 \varepsilon_u+\varepsilon_T=\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0} .
$$


From the equation of state,

$$
\varepsilon_p=\varepsilon_\rho+\varepsilon_T \quad \Longrightarrow \quad-\varepsilon_\rho+\varepsilon_p-\varepsilon_T=0
$$


Stacking these four linear equations produces the schematic matrix form

$$
\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }}
$$

Each equation contributes one row: the coefficients of $\varepsilon_{\text{out}}=\left[\varepsilon_\rho,\varepsilon_u,\varepsilon_p,\varepsilon_T\right]^T$ populate $\boldsymbol{A}(M)$, and the coefficients of $\varepsilon_{\text{in}}=\left[\varepsilon_A,\varepsilon_f,\varepsilon_{T_0}\right]^T$ on the right-hand side populate $\boldsymbol{B}(M)$. The dimensions are $\boldsymbol{A}(M)\in\mathbb{R}^{4\times 4}$, $\boldsymbol{B}(M)\in\mathbb{R}^{4\times 3}$, $\varepsilon_{\text{out}}\in\mathbb{R}^{4}$, and $\varepsilon_{\text{in}}\in\mathbb{R}^{3}$.


$M$ enters only through the coefficients $\frac{1}{\gamma M^2},(\gamma-1) M^2$, and $1+\frac{\gamma-1}{2} M^2$, i.e., through the linear coupling strength between $\varepsilon_p$ , $\varepsilon_u$, and the imposed $\varepsilon_{T_0}$.




> [!question] (b) Structural singularity at the sonic condition
> 
> 
> **(i)** Write out the mathematical expression $\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }}$, clearly, filling in all details for the symbolic form of all matrices and vectors.
> **(ii)** Construct an explicit nontrivial linear combination of the governing equations that vanishes identically at $M=1$. That is, show that the equations become linearly dependent. Explain what this linear dependence means mathematically for the matrix $A(M)$ at $M=1$.
>**(iii)** In 2-4 sentences, explain the physical meaning of this degeneracy. Why does the sonic condition represent a special point for quasi-1D compressible flow?


## 1.b.i


Using the same ordering as in part (a), the unknown flow-response increments are collected as

$$
\varepsilon_{\text {out }}=\left[\begin{array}{c}
\varepsilon_\rho \\
\varepsilon_u \\
\varepsilon_p \\
\varepsilon_T
\end{array}\right] \text {, }
$$

and the imposed driving increments are collected as

$$
\varepsilon_{\mathrm{in}}=\left[\begin{array}{c}
\varepsilon_A \\
\varepsilon_f \\
\varepsilon_{T_0}
\end{array}\right]
$$


The local $\varepsilon$-system consists of four governing equations but involves seven increments $\left\{\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T, \varepsilon_A, \varepsilon_f, \varepsilon_{T_0}\right\}$. Treating $\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}$ as specified inputs leaves four unknown outputs $\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T$, so the system is square (four equations for four unknowns) once the inputs are prescribed.

Start from the given governing equations:

$$
\begin{gathered}
\varepsilon_\rho+\varepsilon_u+\varepsilon_A=0 \\
\varepsilon_\rho+2 \varepsilon_u+\varepsilon_A=-\frac{1}{\gamma M^2} \varepsilon_p-\frac{1}{2} \varepsilon_f \\
\varepsilon_T+(\gamma-1) M^2 \varepsilon_u-\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0}=0 \\
\varepsilon_p=\varepsilon_\rho+\varepsilon_T
\end{gathered}
$$


To cast these into the matrix form $\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }}$, each equation is rewritten so that only output increments appear on the left-hand side and only input increments appear on the right-hand side.


From continuity,

$$
\varepsilon_\rho+\varepsilon_u+\varepsilon_A=0 \Longrightarrow \varepsilon_\rho+\varepsilon_u=-\varepsilon_A .
$$


From the momentum-type relation, begin with

$$
\varepsilon_\rho+2 \varepsilon_u+\varepsilon_A=-\frac{1}{\gamma M^2} \varepsilon_p-\frac{1}{2} \varepsilon_f
$$


Add $\frac{1}{\gamma M^2} \varepsilon_p$ to both sides and subtract $\varepsilon_A$ from both sides to obtain

$$
\varepsilon_\rho+2 \varepsilon_u+\frac{1}{\gamma M^2} \varepsilon_p=-\varepsilon_A-\frac{1}{2} \varepsilon_f
$$


From the energy/total-temperature relation, begin with

$$
\varepsilon_T+(\gamma-1) M^2 \varepsilon_u-\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0}=0
$$


Add $\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0}$ to both sides to obtain

$$
(\gamma-1) M^2 \varepsilon_u+\varepsilon_T=\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0}
$$


From the equation of state,

$$
\varepsilon_p=\varepsilon_\rho+\varepsilon_T \Longrightarrow \varepsilon_p-\varepsilon_\rho-\varepsilon_T=0 \Longrightarrow-\varepsilon_\rho+\varepsilon_p-\varepsilon_T=0 \text {. }
$$


These four rearranged equations can be written verbatim as a $4 \times 1$ vector equality:

$$
\left[\begin{array}{c}
\varepsilon_\rho+\varepsilon_u \\
\varepsilon_\rho+2 \varepsilon_u+\frac{1}{\gamma M^2} \varepsilon_p \\
(\gamma-1) M^2 \varepsilon_u+\varepsilon_T \\
-\varepsilon_\rho+\varepsilon_p-\varepsilon_T
\end{array}\right]=\left[\begin{array}{c}
-\varepsilon_A \\
-\varepsilon_A-\frac{1}{2} \varepsilon_f \\
\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0} \\
0
\end{array}\right] .
$$


Now each left-hand-side component is explicitly a linear combination of the output components $\left(\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T\right)$, and each right-hand-side component is explicitly a linear combination of the input components $\left(\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}\right)$. Reading off coefficients in the order $\varepsilon_{\text {out }}=\left[\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T\right]^T$ defines $\boldsymbol{A}(M)$, and reading off coefficients in the order $\varepsilon_{\text {in }}=\left[\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}\right]^T$ defines $\boldsymbol{B}(M)$.

The coefficient extraction is therefore:


$\varepsilon_\rho+\varepsilon_u=-\varepsilon_A \quad \Longrightarrow \quad \Longrightarrow \quad \boldsymbol{A}$ row $1=[1,1,0,0], \quad \boldsymbol{B}$ row $1=[-1,0,0]$,


$\varepsilon_\rho+2 \varepsilon_u+\frac{1}{\gamma M^2} \varepsilon_p=-\varepsilon_A-\frac{1}{2} \varepsilon_f \quad \Longrightarrow \quad \boldsymbol{A}$ row $2=\left[1,2, \frac{1}{\gamma M^2}, 0\right], \quad \boldsymbol{B}$ row $2=\left[-1,-\frac{1}{2}, 0\right]$,


$(\gamma-1) M^2 \varepsilon_u+\varepsilon_T=\left(1+\frac{\gamma-1}{2} M^2\right) \varepsilon_{T_0} \quad \Longrightarrow \quad \boldsymbol{A}$ row $3=\left[0,(\gamma-1) M^2, 0,1\right], \quad \boldsymbol{B}$ row $3=\left[0,0,1+\frac{\gamma-1}{2} M^2\right]$,


$-\varepsilon_p+\varepsilon_p-\varepsilon_T=0 \quad \Longrightarrow \quad \boldsymbol{A}$ row $4=[-1,0,1,-1], \quad \boldsymbol{B}$ row $4=[0,0,0]$.



Thus the matrices are

$$
\boldsymbol{A}(M)=\left[\begin{array}{cccc}
1 & 1 & 0 & 0 \\
1 & 2 & \frac{1}{\gamma M^2} & 0 \\
0 & (\gamma-1) M^2 & 0 & 1 \\
-1 & 0 & 1 & -1
\end{array}\right], \quad \boldsymbol{B}(M)=\left[\begin{array}{ccc}
-1 & 0 & 0 \\
-1 & -\frac{1}{2} & 0 \\
0 & 0 & 1+\frac{\gamma-1}{2} M^2 \\
0 & 0 & 0
\end{array}\right],
$$

so the fully explicit linear system is

$$
\boldsymbol{A}(M) \varepsilon_{\mathrm{out}}=\boldsymbol{B}(M) \varepsilon_{\mathrm{in}}
$$


In terms of dimensions,

$$
\boldsymbol{A}(M) \in \mathbb{R}^{4 \times 4}, \quad \boldsymbol{B}(M) \in \mathbb{R}^{4 \times 3}, \quad \varepsilon_{\text {out }} \in \mathbb{R}^4, \quad \varepsilon_{\text {in }} \in \mathbb{R}^3 .
$$


The Mach number $M$ appears only parametrically through the coefficients $\frac{1}{\gamma M^2},(\gamma-1) M^2$, and $1+ \frac{\gamma-1}{2} M^2$ that enter $\boldsymbol{A}(M)$ and $\boldsymbol{B}(M)$. For a fixed local value of $M$, the system is an algebraic $4 \times 4$ linear system in the four output increments once the three inputs are specified.



## 1.b.ii


Let $\boldsymbol{A}(M) \in \mathbb{R}^{4 \times 4}$ be the left-hand operator matrix in the linear system $\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }}$, using the output ordering $\varepsilon_{\text {out }}=\left[\varepsilon_\rho, \varepsilon_u, \varepsilon_p, \varepsilon_T\right]^T$. Write the rows of $\boldsymbol{A}(M)$ as $\mathbf{r}_1(M), \mathbf{r}_2(M), \mathbf{r}_3(M), \mathbf{r}_4(M)$, so that

$$
\boldsymbol{A}(M)=\left[\begin{array}{l}
\mathbf{r}_1(M) \\
\mathbf{r}_2(M) \\
\mathbf{r}_3(M) \\
\mathbf{r}_4(M)
\end{array}\right], \quad \mathbf{r}_i(M) \in \mathbb{R}^{1 \times 4} .
$$


From the explicit expression for $\boldsymbol{A}(M)$,

$$
\boldsymbol{A}(M)=\left[\begin{array}{cccc}
1 & 1 & 0 & 0 \\
1 & 2 & \frac{1}{\gamma M^2} & 0 \\
0 & (\gamma-1) M^2 & 0 & 1 \\
-1 & 0 & 1 & -1
\end{array}\right],
$$

evaluation at $M=1$ gives

$$
\boldsymbol{A}(1)=\left[\begin{array}{cccc}
1 & 1 & 0 & 0 \\
1 & 2 & \frac{1}{\gamma} & 0 \\
0 & \gamma-1 & 0 & 1 \\
-1 & 0 & 1 & -1
\end{array}\right] .
$$



Accordingly,

$$
\mathbf{r}_1=[1,1,0,0], \quad \mathbf{r}_2=\left[1,2, \frac{1}{\gamma}, 0\right], \quad \mathbf{r}_3=[0, \gamma-1,0,1], \quad \mathbf{r}_4=[-1,0,1,-1],
$$

where $\mathbf{r}_i$ now denotes $\mathbf{r}_i(1)$.
Linear dependence of the governing equations at $M=1$ is equivalent to linear dependence of the row vectors $\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3, \mathbf{r}_4$. An explicit nontrivial linear combination is obtained by forming

$$
(\gamma+1) \mathbf{r}_1-\gamma \mathbf{r}_2+\mathbf{r}_3+\mathbf{r}_4
$$


Substitute the row vectors and combine componentwise:

$$
(\gamma+1) \mathbf{r}_1-\gamma \mathbf{r}_2+\mathbf{r}_3+\mathbf{r}_4=(\gamma+1)[1,1,0,0]-\gamma\left[1,2, \frac{1}{\gamma}, 0\right]+[0, \gamma-1,0,1]+[-1,0,1,-1] .
$$


Collect the four components (corresponding to the $\rho-, u-, p-$, and $T$-columns of $\boldsymbol{A}(1)$ ):
For the $\rho$-component,

$$
(\gamma+1) \cdot 1-\gamma \cdot 1+0+(-1)=(\gamma+1)-\gamma-1=0 .
$$


For the $u$-component,

$$
(\gamma+1) \cdot 1-\gamma \cdot 2+(\gamma-1)+0=(\gamma+1)-2 \gamma+(\gamma-1)=\gamma+1-2 \gamma+\gamma-1=0 .
$$


For the $p$-component,

$$
(\gamma+1) \cdot 0-\gamma \cdot \frac{1}{\gamma}+0+1=0-1+0+1=0 .
$$


For the $T$-component,

$$
(\gamma+1) \cdot 0-\gamma \cdot 0+1+(-1)=0-0+1-1=0 .
$$


All four components are zero, so the full row-vector sum is the zero vector:

$$
(\gamma+1) \mathbf{r}_1-\gamma \mathbf{r}_2+\mathbf{r}_3+\mathbf{r}_4=\mathbf{0}
$$


Because the coefficients $(\gamma+1),-\gamma, 1,1$ are not all zero, this is a nontrivial linear dependence relation among the rows of $\boldsymbol{A}(1)$. Therefore the rows of $\boldsymbol{A}(1)$ do not span $\mathbb{R}^4$, and the row rank satisfies

$$
\operatorname{rank} \boldsymbol{A}(1) \leq 3<4 .
$$


Equivalently, $\boldsymbol{A}(1)$ is not full rank, so it is singular. In particular,

$$
\operatorname{det} \boldsymbol{A}(1)=0,
$$

and $\boldsymbol{A}(1)$ is non-invertible.




## 1.b.iii

At $M=1$, the linearized quasi-1D closure loses an independent constraint because $\boldsymbol{A}(1)$ is singular, so $\boldsymbol{A}(1) \varepsilon_{\text {out }}=\boldsymbol{B}(1) \varepsilon_{\text {in }}$ cannot be solved for $\varepsilon_{\text {out }}$ for an arbitrary choice of imposed drivers $\varepsilon_{\text {in }}= \left[\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}\right]^T$. Solvability requires the right-hand side to lie in the column space of $\boldsymbol{A}(1)$, equivalently that it be orthogonal to every left-null vector $\ell$ satisfying $\ell^T \boldsymbol{A}(1)=0$; using the left-null combination found in (ii), this means $\ell^T \boldsymbol{B}(1) \varepsilon_{\text {in }}=0$ must hold. Physically, the sonic state is a critical point where the flow speed matches the local acoustic speed, so upstream adjustment cannot accommodate arbitrary downstream forcing; the compatibility restriction is the linearized signature of choking. In this sense the "blow-up" of the usual influence-coefficient formulas as $M \rightarrow 1$ reflects not a true divergence of the physics, but the breakdown of the assumption that one may prescribe independent $\varepsilon_A, \varepsilon_f, \varepsilon_{T_0}$ while remaining on a smooth quasi-1D solution branch.





> [!question] (c) Constructing the input-output map
> 
> 
> 
> 
> For $M \neq 1$, the matrix $\boldsymbol{A}(M)$ is invertible, and the governing equations may be written as
> 
> $$
> \varepsilon_{\text {out }}=C(M) \varepsilon_{\text {in }}, \quad C(M)=A(M)^{-1} B(M) .
> $$
> 
> **(i)** Compute the matrix $C(M)$ explicitly. You may perform this computation by hand or using a symbolic algebra package (e.g. Mathematica, SymPy, or similar).
> **(ii)** Use the structure of $C$ to that a sonic singularity appears as a system-level property, rather than a feature of any single governing equation.

## 1.c.i

For $M \neq 1$, the input-output map is defined by

$$
\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}, \quad \boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M),
$$

with the same ordering

$$
\varepsilon_{\text {out }}=\left[\begin{array}{c}
\varepsilon_\rho \\
\varepsilon_u \\
\varepsilon_p \\
\varepsilon_T
\end{array}\right], \quad \varepsilon_{\text {in }}=\left[\begin{array}{c}
\varepsilon_A \\
\varepsilon_f \\
\varepsilon_{T_0}
\end{array}\right] \text {. }
$$


Invertibility is controlled by the determinant of $\boldsymbol{A}(M)$ :

$$
\operatorname{det} \boldsymbol{A}(M)=\frac{1-M^2}{\gamma M^2},
$$

so $\boldsymbol{A}(M)$ is invertible for $M \neq 1$ (and $M \neq 0$, which is excluded in compressible-flow applications of interest). Computing $\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$ gives the explicit $4 \times 3$ matrix

$$
\boldsymbol{C}(M)=\left[\begin{array}{ccc}
\frac{M^2}{1-M^2} & -\frac{\gamma M^2}{2\left(1-M^2\right)} & -\frac{2+(\gamma-1) M^2}{2\left(1-M^2\right)} \\
-\frac{1}{1-M^2} & \frac{\gamma M^2}{2\left(1-M^2\right)} & \frac{2+(\gamma-1) M^2}{2\left(1-M^2\right)} \\
\frac{\gamma M^2}{1-M^2} & -\frac{\gamma M^2\left(1+(\gamma-1) M^2\right)}{2\left(1-M^2\right)} & -\frac{\gamma M^2\left(2+(\gamma-1) M^2\right)}{2\left(1-M^2\right)} \\
\frac{(\gamma-1) M^2}{1-M^2} & -\frac{\gamma(\gamma-1) M^4}{2\left(1-M^2\right)} & \frac{\left(1-\gamma M^2\right)\left(2+(\gamma-1) M^2\right)}{2\left(1-M^2\right)}
\end{array}\right] .
$$


Equivalently, $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$ means the following four scalar relations hold simultaneously:

$$
\begin{gathered}
\varepsilon_\rho=\frac{M^2}{1-M^2} \varepsilon_A-\frac{\gamma M^2}{2\left(1-M^2\right)} \varepsilon_f-\frac{2+(\gamma-1) M^2}{2\left(1-M^2\right)} \varepsilon_{T_0}, \\
\varepsilon_u=-\frac{1}{1-M^2} \varepsilon_A+\frac{\gamma M^2}{2\left(1-M^2\right)} \varepsilon_f+\frac{2+(\gamma-1) M^2}{2\left(1-M^2\right)} \varepsilon_{T_0}, \\
\varepsilon_p=\frac{\gamma M^2}{1-M^2} \varepsilon_A-\frac{\gamma M^2\left(1+(\gamma-1) M^2\right)}{2\left(1-M^2\right)} \varepsilon_f-\frac{\gamma M^2\left(2+(\gamma-1) M^2\right)}{2\left(1-M^2\right)} \varepsilon_{T_0}, \\
\varepsilon_T=\frac{(\gamma-1) M^2}{1-M^2} \varepsilon_A-\frac{\gamma(\gamma-1) M^4}{2\left(1-M^2\right)} \varepsilon_f+\frac{\left(1-\gamma M^2\right)\left(2+(\gamma-1) M^2\right)}{2\left(1-M^2\right)} \varepsilon_{T_0} .
\end{gathered}
$$


These four equations are exactly the component form of the compact input-output map $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$


## 1.c.ii


The matrix $\boldsymbol{C}(M)$ makes the sonic singularity visible in a way that no single governing equation can. Each of the four original $\varepsilon$-form equations is algebraically well-defined at $M=1$; none of them contains an explicit division by $1-M^2$. The singular behavior appears only after the four equations are taken together as a coupled system and solved for $\varepsilon_{\text {out }}$ in terms of the imposed drivers $\varepsilon_{\text {in }}$. That "solve the system" step is exactly the operation $\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$, and it is at this system level-through the invertibility of $\boldsymbol{A}(M)$-that the sonic condition enters.

This can be stated purely algebraically using the standard identity

$$
\boldsymbol{A}(M)^{-1}=\frac{\operatorname{adj} \boldsymbol{A}(M)}{\operatorname{det} \boldsymbol{A}(M)}, \quad(M \neq 1),
$$

so that

$$
\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)=\frac{\operatorname{adj} \boldsymbol{A}(M) \boldsymbol{B}(M)}{\operatorname{det} \boldsymbol{A}(M)} .
$$


In your computation, the determinant is

$$
\operatorname{det} \boldsymbol{A}(M)=\frac{1-M^2}{\gamma M^2}
$$


The numerator adj $\boldsymbol{A}(M) \boldsymbol{B}(M)$ is built from cofactors of $\boldsymbol{A}(M)$ multiplied by $\boldsymbol{B}(M)$; it is a matrix of rational functions that remains finite as $M \rightarrow 1$. The only factor that must blow up when $M \rightarrow 1$ is therefore the scalar $(\operatorname{det} \boldsymbol{A}(M))^{-1}$, because $\operatorname{det} \boldsymbol{A}(M) \rightarrow 0$. This shows the sonic singularity is not a feature of any single equation, but of the coupled system through the loss of invertibility of $\boldsymbol{A}(M)$.

The explicit structure of $\boldsymbol{C}(M)$ confirms this directly. Every entry of $\boldsymbol{C}(M)$ has the same denominator $1-M^2$; equivalently, the matrix

$$
\left(1-M^2\right) \boldsymbol{C}(M)
$$

has entries that remain finite at $M=1$. Thus the blow-up is a common, global prefactor associated with (det $\boldsymbol{A}(M))^{-1}$, not with any particular row of $\boldsymbol{A}$ or any isolated governing relation. In the language of linear systems, $M=1$ is precisely where the map $\varepsilon_{\text {in }} \mapsto \varepsilon_{\text {out }}$ ceases to be well-defined because $\boldsymbol{A}(1)$ drops rank; attempting to form $\boldsymbol{C}(M)$ forces a division by $\operatorname{det} \boldsymbol{A}(M)$, producing the shared (1-$\left.M^2\right)^{-1}$ singular factor as a system-level property.




> [!question] (d) Interpretation and limits of the framework
> 
> 
> 
> Answer the following conceptual questions ( $2-4$ sentences each):
> **(i)** The governing equations were linearized over a small spatial increment. Why does a singularity nevertheless appear at $M=1$ ?
> **(ii)** What does this breakdown indicate about the validity of the quasi-1D model near the sonic condition?
> **(iii)** Comment on the connection between mathematical singularity and physical limitation in the context of choking.


## 1.d.i

A linearization over a small spatial increment produces a local algebraic relationship among the increments, but it does not remove structural properties of the coefficient matrix that couples those increments. At $M=1$, the coupling matrix $\boldsymbol{A}(1)$ drops rank, so solving for $\varepsilon_{\text {out }}$ requires dividing by $\operatorname{det} \boldsymbol{A}(M) \propto\left(1-M^2\right)$, which is zero at the sonic condition. The singularity therefore reflects a loss of invertibility (a solvability constraint on admissible inputs), not a failure of the "small-step" approximation itself. In other words, even an infinitesimal step inherits the same degeneracy because the sonic point is a characteristic/critical state of the underlying hyperbolic system where the response to forcing cannot be freely specified.

## 1.d.ii

The breakdown indicates that, near $M=1$, the quasi-1D differential framework is no longer able to produce a regular, unique, first-order response to arbitrary geometry/friction/heat inputs, because the closure becomes singular and imposes a compatibility condition instead of a free mapping. In practical terms, the "infinite sensitivities" predicted by $\boldsymbol{C}(M)$ are telling you that the assumptions used to derive the quasi-1D linearized relations-smooth variation, single-valued local state, and a well-posed inputoutput response-stop being valid as the flow approaches choking. Physically, additional effects that were neglected (multi-D adjustment, boundary layers and separation, shocks in supersonic pockets, finiterate/viscous dissipation structure, and/or unsteady behavior) become the mechanisms by which the real flow satisfies the sonic constraint. The model remains useful away from $M=1$, but in a neighborhood of the sonic point it must be supplemented by a throat condition/critical flow analysis rather than treated as a regular perturbation problem.


## 1.d.iii

Here the mathematical singularity and the physical limitation are two views of the same constraint. Mathematically, $\operatorname{det} \boldsymbol{A}(M) \rightarrow 0$ as $M \rightarrow 1$, so the inverse map $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$ ceases to exist unless the imposed drivers satisfy a compatibility condition; the "blow-up" signals that the system cannot accommodate arbitrary forcing with a smooth local response. Physically, choking is exactly that restriction: once the flow reaches the sonic condition at the controlling section (typically the throat), downstream changes or additional driving cannot increase the mass flux, and the flow must instead adjust via non-ideal mechanisms (shocks, separation, multidimensionality, unsteadiness) or by moving the sonic location. The singular coefficients are therefore not predicting an infinite physical response; they are warning that the assumed smooth quasi-1D branch has reached its limit of realizability.



# Problem 2: Global quasi-1D solutions from local $\varepsilon$-relations ( 60 points)

**Preamble.** In Lectures 5-7, we developed a local quasi-one-dimensional framework that relates small imposed driving increments to local flow responses through an algebraic input-output map. In this problem, you will use that local theory to construct a global solution for compressible flow through a variable-area duct, and compare it against a known analytical solution.



> [!question] (a) Analytical reference solution (isentropic nozzle flow)
> 
> **(i)** List what are the assumptions that make the quasi-1D governing equations reduce to the classical isentropic nozzle relation (no need to show the derivation), which can be expressed as an algebraic relation between area ratio $A / A^*$ and Mach number $M$ :
> 
> $$
> \frac{A}{A^*}=\frac{1}{M}\left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2} M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}
> $$
> 
> where $A^*$ denotes the area at which $M=1$.
> **(ii)** Mention one method to solve numerically the isentropic relation above to obtain the analytical Mach number $M_{\text {exact }}(x)$ for a prescribed area profile $A(x)$.

## 2.a.i

To recover the classical isentropic nozzle area-Mach relation from the quasi-1D framework, assume steady quasi-one-dimensional flow in a slowly varying duct so that the state may be represented by cross-section-averaged fields $\rho(x),u(x),p(x),T(x)$ and area $A(x)$, with body forces and potential energy neglected. Impose that the flow is inviscid and adiabatic with no shaft work or heat transfer, so the only "driver" is geometry (equivalently $\varepsilon_f=0$ and $\varepsilon_{T_0}=0$, leaving only area variation). Finally, assume a calorically perfect ideal gas with constant $\gamma$, and require the flow to be isentropic (reversible as well as adiabatic, i.e., no shock/discontinuity or other entropy-producing mechanism), so stagnation quantities are invariant and the quasi-1D relations collapse to an algebraic constraint between $A/A^*$ and $M$.

## 2.a.ii

For a prescribed area profile $A(x)$, compute the local area ratio $R(x)=A(x)/A^*$ and solve the nonlinear scalar equation $f(M;R)=0$ at each $x$, where $f(M;R)=R-\frac{1}{M}\left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2}M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}$. One simple approach is bracketed bisection on the desired branch (e.g., subsonic $M\in(0,1)$ or supersonic $M\in(1,\infty)$ with a practical upper bound), which guarantees convergence because $f(M;R)$ is continuous on the bracket; Newton or secant iterations are also possible if you provide a reasonable initial guess and (for Newton) a derivative or finite-difference slope.





> [!question] (b) Local $\varepsilon$-form for isentropic flow
> 
> 
> For isentropic flow, the only nonzero driving increment is $\varepsilon_A$. Thus,
> 
> $$
> \varepsilon_f=0, \quad \varepsilon_{T_0}=0
> $$
> 
> **(i)** Using the input-output matrix $C(M)$ from Lecture 6, write the local relation between $\varepsilon_u$ and $\varepsilon_A$.
> **(ii)** Explain why this relation depends on the local Mach number $M(x)$, even though the imposed geometric change $\varepsilon_A$ is prescribed.

## 2.b.i

Using the input-output map $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$ with

$$
\varepsilon_{\text {out }}=\left[\begin{array}{c}
\varepsilon_\rho \\
\varepsilon_u \\
\varepsilon_p \\
\varepsilon_T
\end{array}\right], \quad \quad \varepsilon_{\text {in }}=\left[\begin{array}{c}
\varepsilon_A \\
\varepsilon_f \\
\varepsilon_{T_0}
\end{array}\right],
$$

the $\varepsilon_u$ component is obtained by taking the $\varepsilon_u$-row of $\boldsymbol{C}(M)$ :


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



$$
\varepsilon_u=C_{u A}(M) \varepsilon_A+C_{u f}(M) \varepsilon_f+C_{u T_0}(M) \varepsilon_{T_0} .
$$



For isentropic flow, $\varepsilon_f=0$ and $\varepsilon_{T_0}=0$, so this reduces to

$$
\varepsilon_u=C_{u A}(M) \varepsilon_A .
$$


$C_{uA}(M)$ is written explicitly as

$$
\boldsymbol{C}(M)=\left[\begin{array}{ccc}
\frac{M^{2}}{1-M^{2}} & -\frac{\gamma M^{2}}{2\left(1-M^{2}\right)} & -\frac{2+(\gamma-1) M^{2}}{2\left(1-M^{2}\right)} \\
-\frac{1}{1-M^{2}} & \frac{\gamma M^{2}}{2\left(1-M^{2}\right)} & \frac{2+(\gamma-1) M^{2}}{2\left(1-M^{2}\right)} \\
\frac{\gamma M^{2}}{1-M^{2}} & -\frac{\gamma M^{2}\left(1+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)} & -\frac{\gamma M^{2}\left(2+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)} \\
\frac{(\gamma-1) M^{2}}{1-M^{2}} & -\frac{\gamma(\gamma-1) M^{4}}{2\left(1-M^{2}\right)} & \frac{\left(1-\gamma M^{2}\right)\left(2+(\gamma-1) M^{2}\right)}{2\left(1-M^{2}\right)}
\end{array}\right].
$$

From this matrix, we see that $C_{uA}(M)$ is given by.

$$
C_{uA}(M)=-\frac{1}{1-M^2}.
$$

Substituting into $\varepsilon_u=C_{uA}(M)\varepsilon_A$ gives $\varepsilon_u=-\frac{1}{1-M^2}\varepsilon_A$.


## 2.b.ii


Even though $\varepsilon_A$ is prescribed by the duct geometry, the velocity response $\varepsilon_u$ is not determined by kinematics alone; it is determined by the coupled compressible conservation laws (continuity, momentum, energy, and the equation of state) evaluated at the local state. That coupling enters the linearized system through the coefficient matrix $\boldsymbol{A}(M)$, whose entries depend on the local Mach number via factors such as $\frac{1}{\gamma M^2}$ and $(\gamma-1) M^2$, so the inverse map $\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$ necessarily inherits $M$ dependence. Physically, $M(x)$ measures compressibility strength: the same fractional area change produces a different partition between acceleration and thermodynamic adjustment depending on whether the flow is subsonic or supersonic, which is why the coefficient $C_{u A}(M)=-\frac{1}{1-M^2}$ depends on the local value $M(x)$ even for a fixed imposed $\varepsilon_A$.





> [!question] (c) Global solution by local marching
> 
> 
> 
> You will now construct a global solution using the local $\varepsilon$-form relations.
> Consider the area distribution
> 
> $$
> A(x)=A^*\left[1+0.2\left(\frac{x}{L}\right)^2\right], \quad x \in[-L, L],
> $$
> 
> with $L=1$ and throat located at $x=0$. Assume a subsonic inlet condition at $x=-L$ with
> 
> $$
> M(-L)=0.5902487609884511 .
> $$
> 
> **(i)** Outline a numerical procedure to march the solution from $x$ to $x+\Delta x$ using the local $\varepsilon$-relations. Your description should clearly indicate:
> - which quantities are updated algebraically,
> - how the Mach number is recomputed at each step,
> - how the influence coefficients are updated.
> 
> Hint: Be aware that $d(\ln (a))=\frac{d a}{a}=\varepsilon_a$, with $a$ being a generic variable. So, for a small increment, we can approximate $\varepsilon_a \approx \frac{\Delta a}{a}$ or $\varepsilon_a \approx \Delta(\ln (a))$. Also, think about a way to relate $\varepsilon_{M^2}$ to $\varepsilon_A$.
> **(ii)** Implement this marching procedure and plot the Mach number distribution $M_{\text {num }}(x)$. Provide this plot by computing the $M_{\text {num }}$ distribution for a $\Delta x$ value for which $M_{\text {num }}$ changes to within, say, $0.1 \%$ over the interval $x \in[-L,-0.25]$.
> **(iii)** Compare your numerical solution to the analytical solution from part (a) on the subsonic branch. To avoid the sonic singularity discussed later, restrict the comparison to the region
> 
> $$
> x \in[-L,-0.25] .
> $$
> 
> 
> On this interval, compute $M_{\text {exact }}(x)$ by solving the area-Mach relation for the subsonic root, and plot
> 
> $$
> \begin{array}{|c|}
> \hline \frac{\left|M_{\text {num }}(x)-M_{\text {exact }}(x)\right|}{\left|M_{\text {exact }}(x)\right|} \\
> \hline
> \end{array}
> $$
> 
> as a function of $x$.




## 2.c.i

Discretize $x \in[-L, L]$ with a uniform step $\Delta x$ and nodes $x_i=-L+i \Delta x$. The geometry is prescribed, so $A_i=A\left(x_i\right)$ is known. Over one step, represent the local area increment using the logarithmic form of the $\varepsilon$-notation:

$$
\varepsilon_{A, i} \approx \Delta(\ln A)=\ln \left(\frac{A_{i+1}}{A_i}\right)
$$

which is consistent with the small-step approximation $\varepsilon_{A, i} \approx\left(A_{i+1}-A_i\right) / A_i$ when $\Delta x$ is small.
In isentropic flow the only nonzero driver is the area increment, so at every station

$$
\varepsilon_{f, i}=0, \quad \varepsilon_{T_0, i}=0
$$


Given the current Mach number $M_i$, evaluate the needed influence coefficients at that station from the input-output map $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$. In particular, the area-only responses are

$$
\varepsilon_{u, i}=C_{u A}\left(M_i\right) \varepsilon_{A, i}, \quad \varepsilon_{T, i}=C_{T A}\left(M_i\right) \varepsilon_{A, i},
$$

and, if desired for tracking additional primitives,

$$
\varepsilon_{\rho, i}=C_{\rho A}\left(M_i\right) \varepsilon_{A, i}, \quad \varepsilon_{p, i}=C_{p A}\left(M_i\right) \varepsilon_{A, i}
$$


For the explicit $\boldsymbol{C}(M)$ from Lecture 6, the two coefficients needed to update $M$ are

$$
C_{u A}(M)=-\frac{1}{1-M^2}, \quad C_{T A}(M)=\frac{(\gamma-1) M^2}{1-M^2}
$$


The $\varepsilon$-responses are then converted into updated state values using the interpretation $\varepsilon_a \approx \Delta(\ln a)$, i.e.

$$
u_{i+1}=u_i e^{\varepsilon_{u, i}}, \quad T_{i+1}=T_i e^{\varepsilon_{T, i}}, \quad p_{i+1}=p_i e^{\varepsilon_{p, i}}, \quad \rho_{i+1}=\rho_i e^{\varepsilon_{\rho, i}}
$$

whenever those variables are being marched. If only the Mach number is required, it is more direct to update $M$ using $M^2=u^2 /(\gamma R T)$, which in $\varepsilon$-form gives

$$
\varepsilon_{M^2}=2 \varepsilon_u-\varepsilon_T
$$


Therefore, in the isentropic area-driven case,

$$
\varepsilon_{M^2, i}=2 \varepsilon_{u, i}-\varepsilon_{T, i}=\left(2 C_{u A}\left(M_i\right)-C_{T A}\left(M_i\right)\right) \varepsilon_{A, i} .
$$


Substituting the explicit $C_{u A}$ and $C_{T A}$ yields the single-step Mach update factor

$$
\varepsilon_{M^2, i}=-\frac{2+(\gamma-1) M_i^2}{1-M_i^2} \varepsilon_{A, i},
$$

and the corresponding multiplicative update is

$$
M_{i+1}^2=M_i^2 e^{\varepsilon_{M^2, i}}, \quad M_{i+1}=\sqrt{M_{i+1}^2} .
$$


Finally, the influence coefficients are updated by re-evaluating them at the new local Mach number: compute $C_{u A}\left(M_{i+1}\right)$ and $C_{T A}\left(M_{i+1}\right)$ (or $\boldsymbol{C}\left(M_{i+1}\right)$ if additional outputs are being tracked), then repeat the same algebra at the next step from $x_{i+1}$ to $x_{i+2}$.



## 2.c.ii




![[Pasted image 20260216235744.png|500]]



## 2.c.iii


On the subsonic isentropic branch, the analytical solution is obtained from the area-Mach relation

$$
\frac{A}{A^*}=\frac{1}{M}\left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2} M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}
$$


For each $x \in[-L,-0.25]$, the geometry prescribes the area ratio

$$
\frac{A(x)}{A^*}=1+0.2\left(\frac{x}{L}\right)^2
$$

so $M_{\text {exact }}(x)$ is defined as the subsonic root $M \in(0,1)$ of the nonlinear equation $F(M ; x)=0$, where

$$
F(M ; x)=\frac{1}{M}\left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2} M^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}-\frac{A(x)}{A^*} .
$$


This root is found numerically at each station (for example by bisection on $(0,1)$ ), and the requested comparison is then the pointwise relative error

$$
\frac{\left|M_{\text {num }}(x)-M_{\text {exact }}(x)\right|}{\left|M_{\text {exact }}(x)\right|}, \quad x \in[-L,-0.25] .
$$


The following code computes $M_{\text {exact }}(x)$ on the same grid as the marched $M_{\text {num }}(x)$ (using $\Delta x=$ 0.003125 from 2.c.ii), and produces the required relative-error plot. As in 2.c.ii, $A^*$ cancels in the ratio $A / A^*$, so it is taken as 1 without loss of generality.


For $\Delta x=0.003125$, the relative error increases as $x$ approaches -0.25 (where the coefficients become more sensitive as $M$ rises toward unity), with a maximum of about $1.78 \times 10^{-3}(\approx 0.178 \%)$ on $x \in[-1,-0.25]$.


![[Pasted image 20260217002127.png|500]]







> [!question] (d) Breakdown near the sonic condition
> 
> 
> 
> **(i)** Repeat part (c)(ii)-(iii) but now march closer to the throat without evaluating exactly at $x=0$. Use the region
> 
> $$
> x \in[-L,-10 \Delta x],
> $$
> 
> 
> Provide all requested plots for both the $\Delta x$ you chose in part (c), and for $\Delta x / 2$.
> 
> 
> **(ii)** Discuss what happens to the numerical solution as $M \rightarrow 1$. Does decreasing $\Delta x$ remove the difficulty near the sonic condition?
> **(iii)** Explain why the analytical solution remains well-defined at the sonic condition, while the local $\varepsilon$-based marching procedure does not. Your answer should explicitly reference the structure of the input-output matrix $C(M)$.



## 2.d.i

Part (c) (ii) is repeated on the shorter interval $x \in[-L,-10 \Delta x]$ by marching the local update

$$
\varepsilon_{A, i}=\ln \left(\frac{A_{i+1}}{A_i}\right), \quad \varepsilon_{M^2, i}=-\frac{2+(\gamma-1) M_i^2}{1-M_i^2} \varepsilon_{A, i}, \quad M_{i+1}^2=M_i^2 e^{\varepsilon_{M^2, i}}, \quad M_{i+1}=\sqrt{M_{i+1}^2},
$$

starting from $M(-L)=0.5902487609884511$ and stopping at $x=-10 \Delta x$ (without evaluating at the throat $x=0$ ). The exact comparison is again formed from the subsonic root of the area-Mach relation at the same grid points, and the plotted error is

$$
\frac{\left|M_{\text {num }}(x)-M_{\text {exact }}(x)\right|}{\left|M_{\text {exact }}(x)\right|} .
$$


For the step size from part (c), $\Delta x=0.003125$, the march ends at $x=-0.03125$ and yields $M_{\text {num }}(-0.03125) \approx 0.97237$ while $M_{\text {exact }}(-0.03125) \approx 0.98476$; the maximum relative error over $[-1,-0.03125]$ is about $1.26 \times 10^{-2}(\approx 1.26 \%)$. 


![[Pasted image 20260217004025.png]]



![[Pasted image 20260217004049.png]]



For the refined step $\Delta x / 2=0.0015625$, the march ends closer to the throat at $x=-0.015625$ and yields $M_{\text {num }}(-0.015625) \approx 0.98172$ while $M_{\text {exact }}(-0.015625) \approx 0.99236$; the maximum relative error over $[-1,-0.015625]$ is about $1.07 \times 10^{-2}(\approx 1.07 \%)$. The corresponding plots are:


![[Pasted image 20260217004225.png]]



![[Pasted image 20260217004236.png]]



In both cases the error remains small far upstream and then grows rapidly as the march approaches the sonic region.



```Python
import numpy as np
import math
import matplotlib.pyplot as plt

# -------------------------
# Problem data
# -------------------------
gamma = 1.4
L = 1.0
M_inlet = 0.5902487609884511

# Base interval for part (c)
x_start_c, x_end_c = -L, -0.25

def A_over_Astar(x):
    # A(x)/A* with L=1; A* cancels in ratios, so no need to specify A*
    return 1.0 + 0.2*(x/L)**2

# -------------------------
# Local-ε marching for M(x)
# -------------------------
def march_M(x0, x1, dx, M0, gamma=gamma):
    n = int(round((x1 - x0)/dx))
    x = np.linspace(x0, x1, n + 1)
    A = A_over_Astar(x)

    M = np.empty_like(x)
    M2 = M0**2
    M[0] = M0

    for i in range(n):
        eps_A = math.log(A[i+1]/A[i])
        eps_M2 = - (2.0 + (gamma - 1.0)*M2) / (1.0 - M2) * eps_A
        M2 = M2 * math.exp(eps_M2)
        M[i+1] = math.sqrt(M2)

    return x, M

def max_rel_diff_coarse_vs_fine(dx, x0, x1):
    x_c, M_c = march_M(x0, x1, dx, M_inlet, gamma)
    x_f, M_f = march_M(x0, x1, dx/2, M_inlet, gamma)
    # Fine grid contains coarse nodes exactly for these dx choices
    M_f_on_c = M_f[::2]
    rel = np.abs(M_c - M_f_on_c) / np.abs(M_f_on_c)
    return rel.max()

# -------------------------
# Exact subsonic solution from area–Mach relation
# -------------------------
def area_mach_ratio(M, gamma=gamma):
    term = (2.0/(gamma + 1.0)) * (1.0 + (gamma - 1.0)/2.0 * M**2)
    expo = (gamma + 1.0) / (2.0*(gamma - 1.0))
    return (1.0/M) * (term**expo)

def subsonic_mach_from_area_ratio(Ar, gamma=gamma, tol=1e-12, maxit=250):
    # Solve area_mach_ratio(M)=Ar for M in (0,1) by bisection
    lo, hi = 1e-12, 1.0 - 1e-12
    for _ in range(maxit):
        mid = 0.5*(lo + hi)
        f_mid = area_mach_ratio(mid, gamma) - Ar
        if abs(f_mid) < tol:
            return mid
        # For Ar>=1 on the subsonic branch: f(lo)>0 and f(hi)<=0
        if f_mid > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol*max(1.0, mid):
            return 0.5*(lo + hi)
    return 0.5*(lo + hi)

def M_exact_on_grid(x):
    Ar = A_over_Astar(x)
    return np.array([subsonic_mach_from_area_ratio(a, gamma=gamma) for a in Ar])

# ============================================================
# Part (c): choose dx on [-1, -0.25], plot M_num and rel error
# ============================================================
dx = 0.05
for _ in range(12):
    err = max_rel_diff_coarse_vs_fine(dx, x_start_c, x_end_c)
    if err <= 1e-3:
        break
    dx /= 2.0

dx_selected = dx
print("Selected dx for part (c) =", dx_selected)
print("Max relative change vs dx/2 on [-1, -0.25] =", err)

x_c, M_num_c = march_M(x_start_c, x_end_c, dx_selected, M_inlet, gamma)
M_exact_c = M_exact_on_grid(x_c)
rel_err_c = np.abs(M_num_c - M_exact_c) / np.abs(M_exact_c)

plt.figure()
plt.plot(x_c, M_num_c)
plt.xlabel("x")
plt.ylabel("M_num(x)")
plt.title(f"Part (c): M_num on [-1, -0.25] (Δx={dx_selected:g})")
plt.grid(True)
plt.savefig("c_M_num.png", dpi=200, bbox_inches="tight")
plt.show()

plt.figure()
plt.plot(x_c, rel_err_c)
plt.xlabel("x")
plt.ylabel(r"$|M_{\mathrm{num}}-M_{\mathrm{exact}}|/|M_{\mathrm{exact}}|$")
plt.title(f"Part (c): Relative error on [-1, -0.25] (Δx={dx_selected:g})")
plt.grid(True)
plt.savefig("c_rel_error.png", dpi=200, bbox_inches="tight")
plt.show()

# ============================================================
# Part (d): march closer to throat on [-1, -10Δx] for dx and dx/2
# ============================================================
dx1 = dx_selected
dx2 = dx_selected / 2.0

x_end_d1 = -10.0*dx1
x_end_d2 = -10.0*dx2

# dx1 case
x_d1, M_num_d1 = march_M(-L, x_end_d1, dx1, M_inlet, gamma)
M_exact_d1 = M_exact_on_grid(x_d1)
rel_err_d1 = np.abs(M_num_d1 - M_exact_d1) / np.abs(M_exact_d1)

plt.figure()
plt.plot(x_d1, M_num_d1)
plt.xlabel("x")
plt.ylabel("M_num(x)")
plt.title(f"Part (d): M_num on [-1, -10Δx] (Δx={dx1:g})")
plt.grid(True)
plt.savefig("d_M_num_dx.png", dpi=200, bbox_inches="tight")
plt.show()

plt.figure()
plt.plot(x_d1, rel_err_d1)
plt.xlabel("x")
plt.ylabel(r"$|M_{\mathrm{num}}-M_{\mathrm{exact}}|/|M_{\mathrm{exact}}|$")
plt.title(f"Part (d): Relative error on [-1, -10Δx] (Δx={dx1:g})")
plt.grid(True)
plt.savefig("d_rel_error_dx.png", dpi=200, bbox_inches="tight")
plt.show()

# dx2 case
x_d2, M_num_d2 = march_M(-L, x_end_d2, dx2, M_inlet, gamma)
M_exact_d2 = M_exact_on_grid(x_d2)
rel_err_d2 = np.abs(M_num_d2 - M_exact_d2) / np.abs(M_exact_d2)

plt.figure()
plt.plot(x_d2, M_num_d2)
plt.xlabel("x")
plt.ylabel("M_num(x)")
plt.title(f"Part (d): M_num on [-1, -10Δx] (Δx={dx2:g})")
plt.grid(True)
plt.savefig("d_M_num_dx_over2.png", dpi=200, bbox_inches="tight")
plt.show()

plt.figure()
plt.plot(x_d2, rel_err_d2)
plt.xlabel("x")
plt.ylabel(r"$|M_{\mathrm{num}}-M_{\mathrm{exact}}|/|M_{\mathrm{exact}}|$")
plt.title(f"Part (d): Relative error on [-1, -10Δx] (Δx={dx2:g})")
plt.grid(True)
plt.savefig("d_rel_error_dx_over2.png", dpi=200, bbox_inches="tight")
plt.show()

# Quick summaries at the end points (optional but handy)
print("\nPart (d) endpoint summaries:")
print(f"Δx={dx1:g}, x_end={x_end_d1:g}, M_num={M_num_d1[-1]:.6f}, M_exact={M_exact_d1[-1]:.6f}, max rel err={rel_err_d1.max():.6e}")
print(f"Δx={dx2:g}, x_end={x_end_d2:g}, M_num={M_num_d2[-1]:.6f}, M_exact={M_exact_d2[-1]:.6f}, max rel err={rel_err_d2.max():.6e}")

```


## 2.d.ii

As $M \rightarrow 1$, the marching update becomes extremely sensitive because the local input-output coefficients (and, in particular, the area-to-velocity and area-to-temperature couplings) scale like ( 1 -$\left.M^2\right)^{-1}$. This means that a geometrically small $\varepsilon_A=\Delta(\ln A)$ produces an $O\left(\varepsilon_A /\left(1-M^2\right)\right)$ change in the flow increments, so the problem becomes stiff and any local discretization error is strongly amplified as the throat is approached. Decreasing $\Delta x$ reduces $\varepsilon_A$ and does improve the result modestly, but it does not remove the underlying difficulty: the conditioning of the update still deteriorates as $1-M^2$ shrinks, so the step size required for stable, accurate marching collapses as one tries to march arbitrarily close to the sonic point.


## 2.d.iii


The analytical solution remains well-defined at the sonic condition because it is posed implicitly through the finite area-Mach relation $A / A^*=f(M)$, for which $f(1)=1$ and the subsonic branch approaches $M \rightarrow 1$ smoothly as $A / A^* \rightarrow 1$. By contrast, the local $\varepsilon$-marching procedure requires the explicit inputoutput map $\varepsilon_{\text {out }}=\boldsymbol{C}(M) \varepsilon_{\text {in }}$ with $\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$, and the structure of $\boldsymbol{C}(M)$ contains a common denominator $1-M^2$ (equivalently $\boldsymbol{C}(M) \propto 1 / \operatorname{det} \boldsymbol{A}(M)$ with $\operatorname{det} \boldsymbol{A}(M) \propto 1-M^2$ ). Thus, as $M \rightarrow 1$, the explicit increment map becomes ill-conditioned and the marching update involves multiplying a small $\varepsilon_A$ by a coefficient that diverges like $\left(1-M^2\right)^{-1}$, so the procedure loses numerical robustness even though the underlying implicit algebraic relation defining $M$ from $A / A^*$ remains perfectly meaningful at $M=1$.




> [!question] (e) Physical interpretation
> 
> 
> In 2-4 sentences, summarize what this comparison reveals about:
> - the strengths of the local quasi-1D $\varepsilon$-framework,
> - its limitations near choking,
> - the connection between mathematical singularity and physical behavior.



The local quasi-1D $\varepsilon$-framework is powerful because it converts the coupled conservation laws into a compact input-output map, allowing efficient marching that reproduces the subsonic isentropic solution accurately when $M$ stays bounded away from unity. Its limitation near choking is structural: the influence coefficients in $\boldsymbol{C}(M)=\boldsymbol{A}(M)^{-1} \boldsymbol{B}(M)$ scale like $\left(1-M^2\right)^{-1}$, so the marching update becomes illconditioned and increasingly sensitive as $M \rightarrow 1$, even though the underlying isentropic area-Mach relation remains well-defined. The mathematical singularity therefore signals not a physical divergence, but a loss of regularity of the explicit incremental response map at the sonic state, reflecting the physical constraint that the flow cannot accommodate arbitrary forcing and instead approaches the choking condition.