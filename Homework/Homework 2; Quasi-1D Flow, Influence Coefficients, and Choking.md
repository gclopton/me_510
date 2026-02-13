


**Instructions.** Show your reasoning clearly and keep your notation consistent with the lecture notes. Unless stated otherwise, assume all quantities are smooth enough for the manipulations you perform. You may use any results stated in Lectures 5-7. You are welcome to use symbolic algebra or numerical tools to assist with computations, but you must clearly explain the structure and interpretation of your results.



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





> [!question] (b) Structural singularity at the sonic condition
> 
> 
> **(i)** Write out the mathematical expression $\boldsymbol{A}(M) \varepsilon_{\text {out }}=\boldsymbol{B}(M) \varepsilon_{\text {in }}$, clearly, filling in all details for the symbolic form of all matrices and vectors.
> **(ii)** Construct an explicit nontrivial linear combination of the governing equations that vanishes identically at $M=1$. That is, show that the equations become linearly dependent. Explain what this linear dependence means mathematically for the matrix $A(M)$ at $M=1$.
>**(iii)** In 2-4 sentences, explain the physical meaning of this degeneracy. Why does the sonic condition represent a special point for quasi-1D compressible flow?



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





> [!question] (d) Interpretation and limits of the framework
> 
> 
> 
> Answer the following conceptual questions ( $2-4$ sentences each):
> **(i)** The governing equations were linearized over a small spatial increment. Why does a singularity nevertheless appear at $M=1$ ?
> **(ii)** What does this breakdown indicate about the validity of the quasi-1D model near the sonic condition?
> **(iii)** Comment on the connection between mathematical singularity and physical limitation in the context of choking.






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




> [!question] (e) Physical interpretation
> 
> 
> In 2-4 sentences, summarize what this comparison reveals about:
> - the strengths of the local quasi-1D $\varepsilon$-framework,
> - its limitations near choking,
> - the connection between mathematical singularity and physical behavior.



