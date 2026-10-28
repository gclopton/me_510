## CHAPTER 15

## Linear Stability

### 15.0 Introduction

This chapter concerns linear stability, while Chapter 16 will treat nonlinear stability. We begin with a general introduction to linear and nonlinear stability. Unfortunately, there are many different definitions for numerical stability, most of which differ from the definition of physical stability seen in Section 14.1. In particular, unlike physical instability, numerical instability does not necessarily imply sensitivity to small disturbances. Four common definitions of numerical stability are as follows:

- Unbounded Growth A method is unstable if the error grows to infinity as time goes to infinity. In some definitions, the error is required to grow at a certain minimum rate (e.g., exponentially or algebraically). A method that is not unstable is stable.
- Convergence A method is stable if it converges as $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$, assuming only a few basic conditions such as consistency, conservation, and well-posed initial and boundary conditions. Otherwise, a method is unstable. In some definitions, the solution is required not only to converge but also to converge to the solution that satisfies the entropy condition. Somewhat surprisingly, the "unbounded growth" definition and the "convergence" definition are closely related, as discussed in Sections 15.4 and 16.11.
- Physical A method is unstable if it exhibits significant errors created by interactions between various time and space approximations and, in particular, any errors that start small and grow with time. In other words, instability is any significant error beyond that found in the individual component approximations such as the forward-time approximation or the central-space approximation. Conversely, a method is stable when it exhibits only small errors beyond those caused by flaws in the individual component approximations. This definition of numerical instability is the closest in spirit to the definition of physical instability, described in Section 14.1, in that it involves space-time interactions and growth in time. However, unlike true physical instability, this definition of numerical instability does not necessarily require sensitivity to small disturbances.
- Broad A method is unstable if it exhibits large errors that increase with time, or any local errors significantly larger than the average error, most especially oscillatory errors and expansion shocks. Otherwise, a method is stable.

Regardless of definition, spurious oscillations and overshoots are the most common symptoms of numerical instability. Thus, as a unifying principle, this book will discuss stability mainly in terms of spurious oscillations and overshoots. This principle follows the "broad" definition of stability. For example, this principle concerns itself with any significant oscillations, not just unbounded oscillations, contradicting the "unbounded growth" definition of instability. Furthermore, this principle concerns itself with oscillations at ordinary
values of $\Delta x$ and $\Delta t$, rather than oscillations or other types of errors in the limit $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$, contradicting the "convergence" definition of stability. Finally, this principle concerns oscillations regardless of source; oscillations may originate either in the individual space and time approximations or in the interactions between various space and time approximations, contradicting the "physical" definition of instability.

In one natural interpretation, regardless of the definition of stability, stability conditions commonly amount to conditions restricting oscillations. The "unbounded growth" and "convergence" definitions of stability tend to place relatively weak restrictions on oscillations, whereas the "broad" definition tends to place relatively strong restrictions on oscillations. But, in any event, stability analysis most often amounts to oscillation analysis. To distinguish the oscillation aspect of stability from other aspects, some references use terms such as oscillation control or extremum control; this book mostly uses such terms as synonyms for stability.

Although oscillations are the primary symptom of numerical instability, they are also the primary symptom of physical instability, as seen in Section 14.1. By definition, unstable physical systems amplify small disturbances as time progresses, including those introduced by numerical approximations. Then every numerical approximation experiences large errors: The best approximations experience errors characteristic of the physical instability; lesser approximations introduce additional forms of error and instability. How can one distinguish between physical and numerical oscillations without an exact solution? Fortunately, this difficult question does not arise in our applications since, as seen Section 4.11, the unsteady one-dimensional Euler equations and scalar conservation laws are essentially nonoscillatory. In particular, scalar conservation laws neither allow new extrema nor allow existing extrema to grow, so that any oscillations except those found in the initial conditions are purely numerical in origin.

This observation greatly simplifies stability analysis for scalar conservation laws and the one-dimensional Euler equations. Of course, scalar conservation laws and the onedimensional Euler equations are ultimately just first steps towards the multidimensional Euler and Navier-Stokes equations, and any numerical methods based on specific properties of the one-dimensional Euler equations may fail in the extension to the multidimensional Euler and Navier-Stokes equations. In particular, although scalar conservation laws and the one-dimensional Euler equations are always nonoscillatory as described in Section 4.11, the multidimensional Euler and Navier-Stokes equations may be unstable and highly oscillatory as discussed in Section 14.1. However, having said this, by discretizing the nonoscillatory wave/flux terms separately from the oscillatory viscous terms, many numerical methods based on specific properties of scalar conservation laws and the onedimensional Euler equations extend surprisingly well to the multidimensional Euler and Navier-Stokes equations and, in fact, routinely and dramatically outperform methods that are not based on specific properties of scalar conservation laws and the one-dimensional Euler equations.

Numerical errors often mimic physical behaviors - numerical instability mimics physical instability, numerical dissipation mimics physical dissipation, numerical dispersion mimics physical dispersion, and so forth. Distinguishing the physical from the numerical requires a reliable reference standard. One possible reference is experimental results. However, experimental results sometimes contain artifacts of the specific testing conditions, such as disturbances to the flow due to test probes, stings, wall effects in wind tunnels, and so forth. Such artifacts may be difficult to identify and may indicate errors in numerical methods
where none exist. Fortunately, again, the limited scope of this book mostly sidesteps these troubling issues.

Unstable numerical methods are amazingly common. For example, FTCS is highly unstable by any definition, except for a few special and useless cases such as $u_{i}^{0}=$ const. For another historical example, in 1910, Richardson devised one of the first finite-difference methods, a simple linear central-time central-space method approximating the heat equation. Richardson's method is highly unstable, although this was not immediately recognized because the cost of hand calculations prevented anyone from taking more than a few time steps. Instability generally takes time to grow, so that even unstable methods may look fine for the first little while. Sometimes numerical instability has a physical explanation such as, for example, a violation of the CFL condition. Other times there are no specific identifiable factors, either physical or numerical. This is certainly the case for FTCS. Rather than attempting to identify the root causes of instability, this book targets only the symptoms: spurious oscillations and overshoots.

This completes the general introduction to stability. The rest of this chapter specifically concerns stability for linear methods. An equation or numerical approximation is linear if any linear combination of solutions is also a solution. If the governing equations are nonlinear, then any numerical approximation should also be nonlinear. However, the reverse is not necessarily true: Many numerical methods are nonlinear even when the governing equations are linear. Such numerical methods are called inherently nonlinear. All of the methods seen in this book so far are linear when applied to the linear advection equation or a linear system of equations but nonlinear when applied to Burgers' equation or the Euler equations. In other words, none of the methods seen so far are inherently nonlinear. However, most of the modern methods seen in Part V are inherently nonlinear.

This chapter concerns stability for linear methods. Although linearity substantially simplifies stability analysis, never assume that the conclusions of linear stability analysis apply to nonlinear methods. At best, nonlinear methods may be approximately locally linearized, so that the results of linear analyses apply approximately and locally. However, many modern methods, especially inherently nonlinear methods, do not allow for local linearizations. As a result, linear stability analysis has increasingly lost ground to nonlinear stability analysis, to the extent that linear stability analysis rarely appears in research papers written after the early 1980s.

## 15.1 von Neumann Analysis

This section describes the most popular type of linear stability analysis, known as von Neumann or Fourier series analysis. As described in the introduction to Chapter 8 of Hirsch (1988), von Neumann developed this technique during World War II at Los Alamos National Labs in New Mexico. The technique was classified until published by others in the open literature just after the war. Although this book will discuss von Neumann analysis specifically in the context of gasdynamics, it is a general technique that applies to all sorts of linear finite-difference approximations.

Since unstable solutions typically oscillate, it makes sense to express the solution as a Fourier series or, in other words, as a sum of oscillatory trigonometric functions, following the philosophy espoused in Example 6.5. Many other subjects use the same strategy: Acoustics, vibrations, and so forth also use Fourier series because periodic and oscillatory behaviors are also expected. By Equation (7.30), the Fourier series for the solution $u\left(x, t^{n}\right)$
on any spatial domain $[a, b]$ is

$$
u\left(x, t^{n}\right)=a_{0}^{n}+\sum_{m=1}^{\infty} a_{m}^{n} \cos \left(2 \pi m \frac{x-a}{b-a}\right)+\sum_{m=1}^{\infty} b_{m}^{n} \sin \left(2 \pi m \frac{x-a}{b-a}\right)
$$

where $a_{m}^{n}$ and $b_{m}^{n}$ are the Fourier series coefficients for $u\left(x, t^{n}\right)$, not to be confused with the limits $a$ and $b$ of the spatial domain. For a discrete solution, sample the Fourier series to obtain

$$
u\left(x_{i}, t^{n}\right)=a_{0}^{n}+\sum_{m=1}^{\infty}\left(a_{m}^{n} \cos 2 \pi m \frac{x_{i}-a}{b-a}+b_{m}^{n} \sin 2 \pi m \frac{x_{i}-a}{b-a}\right) .
$$

Assume evenly space samples $x_{i+1}-x_{i}=\Delta x=$ const. Also assume that the first and last samples are the endpoints of the domain (i.e., $x_{0}=a$ and $x_{N}=b$ ). Then $x_{i}-a=i \Delta x$ and $b-a=N \Delta x$. The sampled Fourier series then becomes

$$
u\left(x_{i}, t^{n}\right)=a_{0}^{n}+\sum_{m=1}^{\infty}\left(a_{m}^{n} \cos 2 \pi m \frac{i}{N}+b_{m}^{n} \sin 2 \pi m \frac{i}{N}\right)
$$

Unfortunately, samples cannot support an infinite range of frequencies and wavelengths. Instead, samples can only support wavelengths of $2 \Delta x$ or longer, as discussed in Section 8.2. Truncate the sampled Fourier series accordingly to find

$$
u\left(x_{i}, t^{n}\right) \approx a_{0}^{n}+\sum_{m=1}^{N / 2}\left(a_{m}^{n} \cos \frac{2 \pi m i}{N}+b_{m}^{n} \sin \frac{2 \pi m i}{N}\right)
$$

which is called a discrete Fourier series. Although this expression allows $2 \Delta x$ - and $3 \Delta x$-waves, the Nyquist sampling theorem says that these waves do not contain useful information about the solution, as discussed in Section 8.2. An equivalent complex expression for a discrete Fourier series is as follows:

$$
u\left(x_{i}, t^{n}\right) \approx \sum_{m=-N / 2}^{N / 2} C_{m}^{n} \exp \left(\frac{2 \pi I m i}{N}\right)
$$

where $I=\sqrt{-1}$. (A more common notation for $\sqrt{-1}$ is $i$ or $j$; however, these can easily be confused with the spatial indices $i$ and $j$.) The complex form simplifies the algebra seen later in the chapter. From elementary complex analysis, Euler's formula is

$$
\text { - } \quad e^{I \theta}=\cos \theta+I \sin \theta \text {. }
$$

Euler's formula yields the following relationships between the coefficients in the real and complex Fourier series:

$$
\begin{aligned}
& C_{0}=a_{0} \\
& C_{m}=\frac{a_{m}-I b_{m}}{2} \\
& C_{-m}=\frac{a_{m}+I b_{m}}{2}
\end{aligned}
$$

In conclusion, any numerical solution can be written in the form of a discrete Fourier series, preferably using complex notation, assuming only that $\Delta x=$ const. and that $u_{i}^{n}$ is periodic or, in other words, $u_{0}^{n}=u_{N}^{n}$.

Example 15.1 Write the solution of FTCS for the linear advection equation in terms of Fourier series coefficients $C_{m}^{n}$. Use these expressions to show that FTCS for the linear advection equation "blows up" in time.

Solution FTCS for the linear advection equation is

$$
u_{i}^{n+1}-u_{i}^{n}+\lambda a \frac{u_{i+1}^{n}-u_{i-1}^{n}}{2}=0
$$

Let

$$
u_{i}^{n}=\sum_{m=-N / 2}^{N / 2} C_{m}^{n} \exp \left(\frac{2 \pi I m i}{N}\right)
$$

Then

$$
u_{i}^{n+1}=\sum_{m=-N / 2}^{N / 2} C_{m}^{n+1} \exp \left(\frac{2 \pi I m i}{N}\right)
$$

and

$$
\begin{aligned}
u_{i \pm 1}^{n} & =\sum_{m=-N / 2}^{N / 2} C_{m}^{n} \exp \left(\frac{2 \pi I m i(i \pm 1)}{N}\right) \\
& =\sum_{m=-N / 2}^{N / 2} C_{m}^{n} \exp \left( \pm \frac{2 \pi I m}{N}\right) \exp \left(\frac{2 \pi I m i}{N}\right)
\end{aligned}
$$

Then FTCS for the linear advection equation becomes

$$
\begin{aligned}
& \sum_{m=-N / 2}^{N / 2}\left[C_{m}^{n+1}-C_{m}^{n}+\frac{\lambda a}{2} C_{m}^{n} \exp \left(\frac{2 \pi I m}{N}\right)\right. \\
& \left.\quad-\frac{\lambda a}{2} C_{m}^{n} \exp \left(-\frac{2 \pi I m}{N}\right)\right] \exp \left(\frac{2 \pi I m i}{N}\right)=0
\end{aligned}
$$

Euler's relation, Equation (15.4), implies

$$
e^{I \theta}-e^{-I \theta}=2 I \sin \theta
$$

Assuming $C_{m}^{n} \neq 0$, then FTCS for the linear advection equation becomes

$$
\sum_{m=-N / 2}^{N / 2} C_{m}^{n}\left[\frac{C_{m}^{n+1}}{C_{m}^{n}}-1+I \lambda a \sin \frac{2 \pi m}{N}\right] \exp \left(\frac{2 \pi I m i}{N}\right)=0
$$

This last expression is a linear combination of trigonometric functions $\exp (2 \pi \operatorname{Imi} / N)$, where $m=-N / 2, \ldots, N / 2$. Since these trigonometric functions are linearly independent, the coefficients in the linear combination must equal zero. Then

$$
\frac{C_{m}^{n+1}}{C_{m}^{n}}=1-I \lambda a \sin \frac{2 \pi m}{N}
$$

for all $m$. This last equation is the desired expression for FTCS written in terms of Fourier series coefficients. Again, notice that all we have done so far is to rewrite FTCS.

Let us use this last expression to prove that FTCS blows up. First,

$$
\left|\frac{C_{m}^{n+1}}{C_{m}^{n}}\right|^{2}=\left|1-I \lambda a \sin \frac{2 \pi m}{N}\right|^{2}=1+(\lambda a)^{2} \sin ^{2}\left(\frac{2 \pi m}{N}\right) \geq 1,
$$

where

$$
|\operatorname{Re} z+I \operatorname{Im} z|^{2}=(\operatorname{Re} z)^{2}+(\operatorname{Im} z)^{2}
$$

for any complex number $z$. Then

$$
\left|C_{m}^{n+1}\right|>\left|C_{m}^{n}\right|
$$

for all $m \neq 0$. Thus, except for $C_{0}^{n}$, all of the Fourier series coefficients increase in magnitude as time increases. Thus FTCS for the linear advection equation blows up in time.

The preceding example illustrates a general technique that can be used to analyze the stability of any linear method. However, rather than take the long way around each time, the preceding example suggests several simplifications. First of all, from now on, the principle of superposition will be invoked immediately. Thus, instead of using the entire Fourier series, use only one term in the series:

$$
u_{i}^{n}=C_{m}^{n} \exp \left(\frac{2 \pi I m i}{N}\right),
$$

where $m=-N / 2, \ldots, N / 2$. As a second simplification, consider the following convenient notation:

$$
\quad \phi_{m}=\frac{2 \pi m}{N} .
$$

As a third simplification, the solution of a linear equation can always be written in terms of the ratio $C_{m}^{n+1} / C_{m}^{n}$. For example, Equation (15.6) expresses FTCS in terms of $C_{m}^{n+1} / C_{m}^{n}$. Furthermore, and rather remarkably, the ratio $C_{m}^{n+1} / C_{m}^{n}$ does not depend on $n!$ In other words, each of the Fourier series coefficients changes by exactly the same factor at every time step. This strange property is a direct consequence of linearity. Then, as a convenient notation, let

- $G_{m}=\frac{C_{m}^{n+1}}{C_{m}^{n}}$,
where $G_{m}$ does not have an $n$ superscript, since $G_{m}$ does not depend on the time level $n$. The ratio $G_{m}$ is sometimes called the amplification factor. Then Equation (15.8) becomes

$$
u_{i}^{n}=\frac{C_{m}^{n}}{C_{m}^{n-1}} \cdots \frac{C_{m}^{2}}{C_{m}^{1}} \frac{C_{m}^{1}}{C_{m}^{0}} C_{m}^{0} e^{I \phi_{m} i}
$$

or

$$
u_{i}^{n}=G \cdot G \cdots G \cdot C_{m}^{0} e^{I \phi_{m} i}
$$

or

$$
u_{i}^{n}=G_{m}^{n} C_{m}^{0} e^{I \phi_{m} i},
$$

where $G_{m}^{n}$ means " $G_{m}$ to the power $n$ " as opposed to " $G_{m}$ at time level $n$ " (unlike the other quantities in this chapter). As a fourth simplification, assume that $C_{m}^{0}=1$ in Equation (15.11); any other value except 0 would do just as well and would not affect the final results, but 1 is the most convenient choice. As a final simplification, drop the subscript $m$ in Equation (15.11) to obtain the following final result:

$$
\text { - } \quad u_{i}^{n}=G^{n} e^{I \phi i}
$$

where $G$ is now understood to be a function of $\phi$. The dependencies on $N$ and $m$ have thus been eliminated in favor of a dependence on $\phi$.

This section began assuming nothing more than that the solution could be expressed as a discrete Fourier series, in keeping with the "broad" or "oscillatory" definition of stability. However, the preceding results indicate that the amplitudes of each sinusoid in the discrete Fourier series can only have a very narrow range of behaviors, which inspires a definition for the stability of linear methods along the lines of the "unbounded growth" definition. In particular, suppose a linear method satisfies the CFL condition. Then, by the usual linear definitions, the linear method is linearly stable if $|G|<1$ for all $-\pi \leq \phi \leq \pi$. Similarly, the linear method is neutrally linearly stable if $|G| \leq 1$ for all $-\pi \leq \phi \leq \pi$ and $|G|=1$ for some $-\pi \leq \phi \leq \pi$. Finally, the linear method is linearly unstable if $|G|>1$ for some $-\pi \leq \phi \leq \pi$. These simple definitions of stable, unstable, and neutrally stable are direct consequences of the simple behaviors of linear methods. In particular, for linear methods, the amplitudes of the terms in the discrete Fourier series either grow like $\left|G^{n}\right|$, shrink like $\left|G^{n}\right|$, or remain completely the same.

Von Neumann analysis or Fourier series analysis refers to any linear analysis based on Equation (15.12). As the first priority, von Neumann analysis is used to determine linear stability, as indicated by the magnitude of the amplification factor $|G|=\sqrt{\operatorname{Re}(G)^{2}+\operatorname{Im}(G)^{2}}$. After establishing linear stability, von Neumann analysis may also examine the phase $\tan ^{-1}(\operatorname{Im}(G) / \operatorname{Re}(G))$. Whereas the magnitude indicates the amplitude of each term in the Fourier series, the phase indicates the speed of each term in the Fourier series. In a perfect method, all sinusoids would travel at the same wave speed $a$. However, in real methods, different frequencies travel at different speeds. This causes some frequencies to lag and some frequencies to lead. In the worst case, sinusoids with different frequencies may become completely separated, leading to large spatial oscillations. To introduce some common terminology, frequency-dependent wave speeds cause dispersion. Dispersion can occur physically, but this discussion concerns purely numerical dispersion. Although dispersion never leads linear methods to blow up, large oscillations caused by dispersion may still be considered a form of instability, under the "broad" definition of instability, although it is
certainly not instability under the "unbounded growth" definition most often used in linear analysis. Von Neumann analysis commonly investigates both amplitude and phase, and thus von Neumann analysis commonly investigates both the "unbounded growth" and "broad" definitions of instability, although this chapter is mainly concerned with the "unbounded growth" definition.

As one way to view Fourier series analysis, imagine striking a series of tones on a xylophone. The amplitude $C_{m}^{0}$ indicates how loud the note begins; $C_{m}^{0}=0$ corresponds to skipping a note. As the mallet strikes each plate on the xylophone, the tone either dies out, preferably slowly, or resonates and becomes increasingly louder. If one strikes all of the notes simultaneously or in quick succession, the method is said to have low dispersion if far away listeners hear all of the tones simultaneously or in quick succession and high dispersion if far away listeners hear some tones first, well before the others, somewhat like the Doppler effect.

Example 15.2 Use von Neumann analysis to determine the stability of FTFS for the linear advection equation.

Solution FTFS for the linear advection equation is

$$
u_{i}^{n+1}=u_{i}^{n}-\lambda a\left(u_{i+1}^{n}-u_{i}^{n}\right) .
$$

Let $u_{i}^{n}=G^{n} e^{I \phi i}$. Then FTFS for the linear advection equation becomes

$$
G^{n+1} e^{I \phi i}=G^{n} e^{I \phi i}-\lambda a G^{n} e^{I \phi(i+1)}+\lambda a G^{n} e^{I \phi i}
$$

Divide by $G^{n} e^{I \phi i}$ and apply Euler's relation to obtain

$$
G=1-\lambda a e^{I \phi}+\lambda a=1+\lambda a-\lambda a \cos \phi-I \lambda a \sin \phi .
$$

Then

$$
|G|^{2}=(1+\lambda a-\lambda a \cos \phi)^{2}+(\lambda a \sin \phi)^{2}
$$

After some algebraic manipulation, this becomes

$$
|G|^{2}=1+2 \lambda a(1+\lambda a)(1-\cos \phi)
$$

Since $1-\cos \phi \geq 0$ for all $-\pi \leq \phi \leq \pi,|G| \leq 1$ if and only if

$$
2 \lambda a(1+\lambda a) \leq 0,
$$

or equivalently,

$$
-1 \leq \lambda a \leq 0 .
$$

In conclusion, FTFS is linearly stable if $-1 \leq \lambda a \leq 0$. Notice that, in this case, the linear stability condition is the same as the CFL condition.

Example 15.3 Use von Neumann analysis to determine the stability of BTCS for the linear advection equation.

Solution BTCS for the linear advection equation is

$$
u_{i}^{n+1}=u_{i}^{n}-\lambda a \frac{u_{i+1}^{n+1}-u_{i-1}^{n+1}}{2} .
$$

Let $u_{i}^{n}=G^{n} e^{I \phi i}$. Then BTCS for the linear advection equation becomes

$$
G^{n+1} e^{I \phi i}=G^{n} e^{I \phi i}-\frac{\lambda a}{2} G^{n+1} e^{I \phi(i+1)}+\frac{\lambda a}{2} G^{n+1} e^{I \phi(i-1)}
$$

Divide by $G^{n} e^{I \phi i}$ to obtain

$$
G=1-\frac{\lambda a}{2} G e^{I \phi}+\frac{\lambda a}{2} G e^{-I \phi}=1-I \lambda a G \sin \phi
$$

Solve for $G$ to find

$$
G=\frac{1}{1+I \lambda a \sin \phi}
$$

Then

$$
|G|^{2}=G G^{*}=\frac{1}{1+I \lambda a \sin \phi} \frac{1}{1-I \lambda a \sin \phi}=\frac{1}{1+(\lambda a \sin \phi)^{2}}
$$

where the asterisk superscript indicates complex conjugation. By definition:

$$
(\operatorname{Re} z+I \operatorname{Im} z)^{*}=\operatorname{Re} z-I \operatorname{Im} z
$$

for any complex number $z$. Then $|G| \leq 1$ for all $-\pi \leq \phi \leq \pi$ and for all $\lambda a$. Then BTCS is unconditionally stable.

Example 15.4 Show that any method written in artificial viscosity form (14.3) is linearly stable if $(\lambda a)^{2} \leq \lambda \epsilon \leq 1$. This indicates that instability may be caused by either too little or too much artificial viscosity. Assume that both $\epsilon$ and $a$ are constant.

Solution For constant $\epsilon$ and $a$, the artificial viscosity form is

$$
u_{i}^{n+1}=u_{i}^{n}-\frac{\lambda a}{2}\left(u_{i+1}^{n}-u_{i-1}^{n}\right)+\frac{\lambda \epsilon}{2}\left(u_{i+1}^{n}-2 u_{i}^{n}+u_{i-1}^{n}\right),
$$

which allows only methods whose stencils contain the three points $u_{i-1}^{n}, u_{i}^{n}$, and $u_{i+1}^{n}$. This includes FTBS, FTFS, and FTCS applied to the linear advection equation. Let $u_{i}^{n}=G^{n} e^{I \phi i}$. Then

$$
\begin{aligned}
G & =1-\frac{\lambda a}{2}\left(e^{I \phi}-e^{-I \phi}\right)+\frac{\lambda \epsilon}{2}\left(e^{I \phi}-2+e^{-I \phi}\right) \\
& =1-\lambda \epsilon+\lambda \epsilon \cos \phi-I \lambda a \sin \phi
\end{aligned}
$$

and

$$
|G|^{2}=(1-\lambda \epsilon+\lambda \epsilon \cos \phi)^{2}+(\lambda a \sin \phi)^{2}
$$

The rest of this example is an exercise in freshman calculus. The maximum of a smooth function on a closed domain occurs at the endpoints of the domain or where the first derivative equals zero and the second derivative is less than or equal to zero. In this case,
the maximum of $|G|^{2}$ occurs either at $\phi=0$ or the endpoints $\pm \pi$. Notice that $|G|^{2}=1$ when $\phi=0$ regardless of $\epsilon$ or $a$. Then the method is unstable unless all values near $\phi=0$ are less than or equal to one, which implies that $\phi=0$ must be a local maximum regardless of whether or not it is a global maximum. But if $\phi=0$ is a local maximum then the second derivative at $\phi=0$ must be less than or equal to zero, which is true if $(\lambda a)^{2} \leq \lambda \epsilon$. Also, a simple calculation shows that $|G|^{2} \leq 1$ at $\phi= \pm \pi$ if $0 \leq \lambda \epsilon \leq 1$. Combining these two conditions, we see that $(\lambda a)^{2} \leq \lambda \epsilon \leq 1$, implying that all candidate maxima are less than or equal to one, and thus $|G|^{2} \leq 1$; therefore the method is linearly stable.

Unfortunately, von Neumann stability analysis does not work for nonlinear methods. In particular, the principle of superposition no longer applies, so that different frequencies interact nonlinearly, making von Neumann analysis practically impossible. However, suppose that the method is locally linearized. For example, for a scalar conservation law with nonlinear flux function $f(u)$, FTFS is

$$
u_{i}^{n+1}=u_{i}^{n}-\lambda\left(f\left(u_{i+1}^{n}\right)-f\left(u_{i}^{n}\right)\right) .
$$

This method can be locally linearized by replacing the true nonlinear flux function $f(u)$ by the locally linearized flux function $a_{i+1 / 2}^{n} u+$ const., where the slope $a_{i+1 / 2}^{n}$ is some average value of the wave speed $f^{\prime}(u)=a(u)$ for $u$ between $u_{i}^{n}$ and $u_{i+1}^{n}$, such as, for example, $a_{i+1 / 2}^{n}=\left(a\left(u_{i+1}^{n}\right)+a\left(u_{i}^{n}\right)\right) / 2$. After this local linearization, FTFS becomes

$$
u_{i}^{n+1}=u_{i}^{n}-\lambda a_{i+1 / 2}^{n}\left(u_{i+1}^{n}-u_{i}^{n}\right) .
$$

Von Neumann analysis proceeds as before with the result $-1 \leq \lambda a_{i+1 / 2}^{n} \leq 0$. Unfortunately, in general, locally linearized stability is neither necessary nor sufficient for true nonlinear stability. Nonlinear stability is considered in the next chapter.

Von Neumann analysis also applies to linear systems of equations. However, linear scalar analysis usually provides just as much information as linear systems analysis, since the scalar characteristic equations composing a linear system do not interact, and thus von Neumann analysis is rarely conducted on systems. See Section 3.6.2 in Anderson, Tannehill, and Pletcher (1984) for more details.

### 15.2 Alternatives to von Neumann Analysis

Besides linearity, von Neumann analysis requires constant grid spacing $\Delta x$ and periodic solutions. However, there are other linear stability analyses that allow nonconstant grid spacings and nonperiodic solutions. For example, the energy method for linear stability analysis requires that the 2 -norm error $\|e\|_{2}^{2}=\sum\left(u\left(x_{i}, t^{n}\right)-u_{i}^{n}\right)^{2}$ should not increase with $n$. Unfortunately, this is usually extremely difficult to prove, even for relatively simple methods. A more practical alternative is the matrix method for linear stability analysis. Any linear finite-difference method can be written as follows:

$$
u_{i}^{n+1}=\sum_{j=-K}^{K} a_{i j} u_{i+j}^{n} .
$$

An equivalent vector-matrix formulation is

$$
\mathbf{u}^{n+1}=A \mathbf{u}^{n},
$$

where

$$
\mathbf{u}^{n}=\left[u_{0}^{n}\left|u_{1}^{n}\right| \cdots \mid u_{N}^{n}\right]^{T} .
$$

The vector $\mathbf{u}^{n}$ is called the vector of samples. Do not confuse the vector of samples with the vector of conserved quantities. The matrix $A$ is composed of the coefficients $a_{i j}$. For example, in Example 11.4, BTCS was written as $A^{-1} \mathbf{u}^{n+1}=\mathbf{u}^{n}$. Invert to find $\mathbf{u}^{n+1}=A \mathbf{u}^{n}$. Then

$$
\begin{aligned}
\mathbf{u}^{1}= & A \mathbf{u}^{0}, \\
\mathbf{u}^{2}= & A \mathbf{u}^{1}=A^{2} \mathbf{u}^{0}, \\
& \vdots \\
\mathbf{u}^{n}= & A \mathbf{u}^{n-1}=A^{2} \mathbf{u}^{n-2}=\cdots=A^{n} \mathbf{u}^{0} .
\end{aligned}
$$

Suppose that $Q^{-1} A Q=\Lambda$ where $\Lambda$ is a diagonal matrix of the characteristic values $\lambda_{i}$ of $A$, as seen in Section 3.2. Then $Q^{-1} A^{n} Q=\Lambda^{n}$ where $\Lambda^{n}$ is a diagonal matrix of $\lambda_{i}^{n}$, where all the $n$ s in these expressions are exponents and not time indices. Then

$$
Q^{-1} \mathbf{u}^{n}=\Lambda^{n} Q^{-1} \mathbf{u}^{0} .
$$

Notice that $\lambda_{i}^{n}$ either grows rapidly with $n$ if $\lambda_{i}>1$ or shrinks rapidly with $n$ if $\lambda_{i}<1$. Then $\Lambda^{n}$ grows rapidly with $n$ if $\lambda_{i}>1$ for any $i$ and shrinks rapidly with $n$ if $\lambda_{i}<1$ for all $i$. Let the spectral radius $\rho(A)$ be the largest characteristic value of $A$ in absolute value. Assume that the method satisfies the CFL condition. Then using "unbounded growth" definitions as in the last section, a linear method is linearly stable if $\rho(A)<1$, neutrally linearly stable if $\rho(A)=1$, and linearly unstable if $\rho(A)>1$. Unfortunately, finding the spectral radius of $A$ may be difficult. Also notice that, unlike von Neumann analysis, this analysis does not say anything about dispersion and the resulting spurious oscillations, which is an important part of linear stability analysis under the "broad" definition. On the positive side, matrix stability analysis works in cases where Fourier series stability analysis does not. In particular, matrix stability analysis can register the effects of different types of boundary conditions, the number of grid points, and the variable spacing between grid points, all of which radically affect stability, whereas von Neumann analysis is restricted to periodic boundaries and constant grid spacings, as mentioned at the beginning of the chapter. For more on the energy method, the matrix method, and other alternatives to Fourier series analysis see, for example, Chapter 10 of Hirsch (1988). For more on linear stability in the presence of nonperiodic boundaries, see Section 19.1.

### 15.3 Modified Equations

Finite-difference methods solve linear advection equations approximately, but they solve modified linear advection equations exactly. In other words, modified equations choose the questions to fit the answers, just like the television quiz show Jeopardy. Modified equations are best explained by example.

Example 15.5 Find the modified equation for FTCS applied to the linear advection equation.

Solution FTCS for the linear advection equation is

$$
\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}+a \frac{u_{i+1}^{n}-u_{i-1}^{n}}{2 \Delta x}=0 .
$$

By Taylor series we have

$$
\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}=\frac{\partial u}{\partial t}\left(x_{i}, t^{n}\right)+\frac{\Delta t}{2} \frac{\partial^{2} u}{\partial t^{2}}\left(x_{i}, t^{n}\right)+\frac{\Delta t^{2}}{6} \frac{\partial^{3} u}{\partial t^{3}}\left(x_{i}, t^{n}\right)+O\left(\Delta t^{3}\right)
$$

and

$$
\frac{u_{i+1}^{n}-u_{i-1}^{n}}{2 \Delta x}=\frac{\partial u}{\partial x}\left(x_{i}, t^{n}\right)+\frac{\Delta x^{2}}{6} \frac{\partial^{3} u}{\partial x^{3}}\left(x_{i}, t^{n}\right)+O\left(\Delta x^{4}\right)
$$

Then FTCS solves the following partial differential equation exactly:

$$
\frac{\partial u}{\partial t}+a \frac{\partial u}{\partial x}=-\frac{a \Delta x^{2}}{6} \frac{\partial^{3} u}{\partial x^{3}}-\frac{\Delta t}{2} \frac{\partial^{2} u}{\partial t^{2}}-\frac{\Delta t^{2}}{6} \frac{\partial^{3} u}{\partial t^{3}}+O\left(\Delta x^{4}\right)+O\left(\Delta t^{3}\right)
$$

This is called a modified equation.
To yield useful information, the time derivatives on the right hand of the modified equation must be replaced by spatial derivatives. In particular, it will be shown that

$$
\begin{aligned}
& \frac{\partial^{2} u}{\partial t^{2}}=a^{2} \frac{\partial^{2} u}{\partial x^{2}}+a^{3} \Delta t \frac{\partial^{3} u}{\partial x^{3}}+O\left(\Delta x^{2}\right)+O\left(\Delta t^{2}\right) \\
& \frac{\partial^{3} u}{\partial t^{3}}=-a^{3} \frac{\partial^{3} u}{\partial x^{3}}+O\left(\Delta x^{2}\right)+O(\Delta t)
\end{aligned}
$$

The proof involves repeatedly differentiating the modified equation and substituting the results back into the modified equation or derivatives of the modified equation. This process is sometimes called the Cauchy-Kowalewski procedure. To start with, take the partial derivatives of the modified equation with respect to $x$ and $t$ :

$$
\begin{aligned}
& \frac{\partial^{2} u}{\partial t^{2}}+a \frac{\partial^{2} u}{\partial t \partial x}=-\frac{a \Delta x^{2}}{6} \frac{\partial^{4} u}{\partial t \partial x^{3}}-\frac{\Delta t}{2} \frac{\partial^{3} u}{\partial t^{3}}-\frac{\Delta t^{2}}{6} \frac{\partial^{4} u}{\partial t^{4}}+O\left(\Delta x^{4}\right)+O\left(\Delta t^{3}\right) \\
& \frac{\partial^{2} u}{\partial x \partial t}+a \frac{\partial^{2} u}{\partial x^{2}}=-\frac{a \Delta x^{2}}{6} \frac{\partial^{4} u}{\partial x^{4}}-\frac{\Delta t}{2} \frac{\partial^{3} u}{\partial x \partial t^{2}}-\frac{\Delta t^{2}}{6} \frac{\partial^{4} u}{\partial x \partial t^{3}}+O\left(\Delta x^{4}\right)+O\left(\Delta t^{3}\right)
\end{aligned}
$$

Multiply Equation (15.19) by $a$ and subtract from Equation (15.18) to obtain

$$
\frac{\partial^{2} u}{\partial t^{2}}=a^{2} \frac{\partial^{2} u}{\partial x^{2}}-\frac{\Delta t}{2} \frac{\partial^{3} u}{\partial t^{3}}+\frac{a \Delta t}{2} \frac{\partial^{3} u}{\partial x \partial t^{2}}+O\left(\Delta x^{2}\right)+O\left(\Delta t^{2}\right)
$$

where the several higher-order terms are dropped, since they will not be needed. In Equation (15.20), there is one pure $x$ derivative, one pure $t$ derivative, and one mixed $x-t$ derivative. To eliminate the mixed derivative, take the partial derivative of Equation (15.20) with respect to $x$ to obtain

$$
\frac{\partial^{3} u}{\partial x \partial t^{2}}=a^{2} \frac{\partial^{3} u}{\partial x^{3}}+O(\Delta t)+O\left(\Delta x^{2}\right)
$$

where the higher-order terms are again dropped, since they will not be needed. Substitute Equation (15.21) into Equation (15.20) to get:

$$
\frac{\partial^{2} u}{\partial t^{2}}=a^{2} \frac{\partial^{2} u}{\partial x^{2}}-\frac{\Delta t}{2} \frac{\partial^{3} u}{\partial t^{3}}+\frac{a^{3} \Delta t}{2} \frac{\partial^{3} u}{\partial x^{3}}+O\left(\Delta x^{2}\right)+O\left(\Delta t^{2}\right) .
$$

In Equation (15.22), there is one pure $t$ derivative and two pure $x$ derivatives. To eliminate the $t$ derivative, take the second partial derivative of the modified Equation (15.15) with respect to $t$ to obtain

$$
\frac{\partial^{3} u}{\partial t^{3}}=-a \frac{\partial}{\partial x}\left(\frac{\partial^{2} u}{\partial t^{2}}\right)-\frac{a \Delta x^{2}}{6} \frac{\partial^{4} u}{\partial t^{2} \partial x^{3}}-\frac{\Delta t}{2} \frac{\partial^{4} u}{\partial t^{4}}-\frac{\Delta t^{2}}{6} \frac{\partial^{5} u}{\partial t^{5}}+O\left(\Delta x^{4}\right)+O\left(\Delta t^{3}\right) .
$$

Finally, substitute Equation (15.22) into Equation (15.23) to obtain Equation (15.17), and substitute (15.17) into (15.22) to obtain Equation (15.16).

Now substitute Equations (15.16) and (15.17) into the modified Equation (15.15) to obtain the final result

$$
\frac{\partial u}{\partial t}+a \frac{\partial u}{\partial x}=-\frac{a^{2} \Delta t}{2} \frac{\partial^{2} u}{\partial x^{2}}-\frac{a \Delta x^{2}}{6}\left(1-2(\lambda a)^{2}\right) \frac{\partial^{3} u}{\partial x^{3}}+O\left(\Delta t^{3}\right)+O\left(\Delta x^{3}\right)+O\left(\Delta x^{2} \Delta t\right) .
$$

The right-hand side of the modified equation is written entirely in terms of $x$ derivatives. By the discussion of Section 14.2, the second derivative on the right-hand side is second-order implicit artificial viscosity. Since the coefficient of the second-order artificial viscosity is negative, rather than positive, the artificial viscosity is destabilizing rather than stabilizing, or antidissipative. The third derivative on the right-hand side is third-order implicit artificial dispersion. Whereas artificial dissipation affects the amplitudes of the sinusoids in a Fourier series representation, artificial dispersion affects the speed. Notice that artificial dispersion vanishes for the special CFL numbers $\lambda a= \pm 1 / \sqrt{2}$. The artificial antidissipation never vanishes except in the limit $\Delta t \rightarrow 0$.

Dissipation reduces the amplitudes of sinusoids in a Fourier series. The following derivatives are generally dissipative:

$$
+\frac{\partial^{2} u}{\partial x^{2}},-\frac{\partial^{4} u}{\partial x^{4}},+\frac{\partial^{6} u}{\partial x^{6}},-\frac{\partial^{8} u}{\partial x^{8}}, \ldots .
$$

By contrast, antidissipation increases the amplitudes of sinusoids in a Fourier series. The following derivatives are generally antidissipative:

$$
-\frac{\partial^{2} u}{\partial x^{2}},+\frac{\partial^{4} u}{\partial x^{4}},-\frac{\partial^{6} u}{\partial x^{6}},+\frac{\partial^{8} u}{\partial x^{8}}, \ldots .
$$

Finally, dispersion affects the speed of sinusoids in a discrete Fourier series, causing them to lead or lag depending on the sign of the coefficient of dispersion and the order of the dispersive derivative. The following derivatives are generally dispersive:

$$
\pm \frac{\partial^{3} u}{\partial x^{3}}, \pm \frac{\partial^{5} u}{\partial x^{5}}, \pm \frac{\partial^{7} u}{\partial x^{7}}, \pm \frac{\partial^{9} u}{\partial x^{9}}, \ldots .
$$

Dispersion can cause different frequencies to separate, resulting in oscillations. Dispersion is especially dramatic near jump discontinuities, where the full range of frequencies occur simultaneously in significant proportions. Explicit artificial dissipation (also known as explicit artificial viscosity) can control or cancel implicit artificial dissipation. Similarly, explicit artificial dispersion can control or cancel implicit artificial dispersion. Artificial dissipation takes the form of even-order differences approximating even-order derivatives. Similarly, artificial dispersion takes the form of odd-order differences approximating oddorder derivatives.

As mentioned at the end of Section 12.1, stability tends to decrease as formal accuracy increases. Modified equations help to justify this observation. Looking at the right-hand side of a modified equation, suppose that the first term is an even derivative, the second term is an odd derivative, the third term is an even derivative, and so forth. Assume that the first term is dissipative and that the method is consequently stable. The first term is the largest source of error, and thus it must be reduced or eliminated to increase the formal order of accuracy. However, if the first term is reduced, the second term will dominate the error. The second term is dispersive and thus the error tends to become oscillatory, especially near jump discontinuities. Furthermore, as the first dissipative term decreases, the scheme's stability becomes heavily influenced by the third term, which may be antidissipative, so that the scheme is unstable. In conclusion, large dissipative terms may be preferable to smaller antidissipative or dispersive terms. Put another way, increasing formal order of accuracy may decrease stability and thus may decrease the overall accuracy.

The right-hand side of a modified equation is sometimes called local truncation error. This definition of the local truncation error is closely related to the definition of the local truncation error seen in Equation (11.53). By either definition, a numerical method is called consistent if the local truncation error goes to zero as $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$, as discussed in Subsection 11.2.2. Notice that this is generally not true if the solution is discontinuous, since the derivatives on the right-hand side of the modified equation will be infinite at jump discontinuities - in other words, numerical methods are generally not consistent for discontinuous solutions. Unfortunately, modified equations are mainly useful for linear methods. The modified equations for nonlinear methods contain nonlinear terms such as $(\partial u / \partial x)^{2}$ and $(\partial u / \partial x)(\partial u / \partial t)$ which have unpredictable effects, unlike the purely dispersive or purely dissipative derivatives seen here.

### 15.4 Convergence and Linear Stability

With some minimal sensible assumptions, linear stability as defined above guarantees convergence to the true solution as $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$, at least for smooth solutions. Assume that the linear approximate equation is consistent with the linear advection equation, in the sense that the local truncation error as defined in Subsection 11.2.2 or as in the previous section goes to zero as $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$. Also, assume that the linear advection equation has well-posed boundary and initial conditions, as discussed in Sections 3.1 and 3.2. Then a consistent linear finite-difference approximation to a well-posed linear problem is convergent if and only if it is linearly stable. Hence, for linear methods, the "unbounded increase" notion of stability is equivalent to the "convergence" notion of stability. This is known as the Lax Equivalence Theorem. Recall that, by one definition, the local truncation error is the error incurred after a single time step. Then a method is consistent if the error incurred after a single time step always goes to zero in the limit of an infinitesimal
time step. The Lax Equivalence Theorem says that if the error goes to zero in the limit of a single infinitesimal time step, then the error goes to zero in the limit of infinitely many infinitesimal time steps if and only if the numerical method is linearly stable. Like so many of the stability properties seen in this chapter, the Lax Equivalence Theorem is a special property of linear methods.

As an often overlooked point, for most numerical methods, the truncation error does not go to zero in the presence of jump discontinuities. In other words, most numerical approximations are not consistent for nonsmooth solutions! Then, in essence, the Lax Equivalence Theorem only applies to smooth solutions - linear stability and convergence are distinct for nonsmooth solutions. Skeptical readers should look ahead to the Lax-Wendroff method, seen in Section 17.2. The Lax-Wendroff method is linearly stable when applied to the linear advection equation. Also, the Lax-Wendroff method is consistent with the linear advection equation for smooth solutions. Then, as expected by the Lax Equivalence Theorem, the Lax-Wendroff method converges to the true solution as $\Delta x \rightarrow 0$ and $\Delta t \rightarrow 0$ for smooth solutions. However, for solutions with jump discontinuities, the Lax-Wendroff method does not converge; for example, in the linear advection of a square wave, oscillations originating on the jump discontinuities spread slowly as time increases, as seen in Figure 17.9.

## References

Anderson, D. A., Tannehill, J. C., and Pletcher, R. H. 1984. Computational Fluid Mechanics and Heat Transfer, New York: Hemisphere, Sections 3.3 and 3.6.
Hirsch, C. 1988. Numerical Computation of Internal and External Flows, Volume 1: Fundamentals of Numerical Discretization, Chichester: Wiley, Chapters 8, 9, and 10.

## Problems

15.1 Apply von Neumann analysis to FTBS for the linear advection equation.
(a) Show that $G=1-\lambda a+\lambda a e^{I \phi}$.
(b) Based on the results of part (a), show that FTBS is linearly stable if $0 \leq \lambda a \leq 1$ and unstable otherwise. How does the linear stability condition compare with the CFL condition?
15.2 Apply von Neumann stability to CTCS for the linear advection equation.
(a) Show that $G=-I \lambda a \sin \phi \pm \sqrt{1-(\lambda a)^{2} \sin ^{2} \phi}$.
(b) Based on the results of part (a), show that CTCS is neutrally linearly stable if $|\lambda a| \leq 1$ and unstable otherwise. How does the linear stability condition compare with the CFL condition?
15.3 Apply von Neumann stability to CTBS for the linear advection equation.
(a) Show that $G=-z \pm \sqrt{z^{2}+1}$, where $z=\lambda a\left(1-e^{-I \phi}\right)$. Hint: The quadratic formula applies to complex numbers.
(b) Based on the results of part (a), show that CTBS is unconditionally linearly unstable. As a hint, multiply the two solutions found in part (a). Use this product to show that one of the two solutions found in part (a) is always greater than or equal to one, while the other is always less than or equal to one.
15.4 Apply von Neumann stability to BTBS for the linear advection equation.
(a) Show that $G=1 /\left(1+\lambda a-\lambda a e^{-l \phi}\right)$.
(b) Based on the results of part (a), show that BTBS is linearly stable for $\lambda a \geq 0$ or $\lambda a \leq-1$. How does the linear stability condition compare with the CFL condition? In particular, what do you think of the negative CFL numbers allowed by the linear stability analysis?
15.5 Apply von Neumann analysis to the following method:

$$
u_{i}^{n+1}=u_{i}^{n}-\frac{\lambda a}{12}\left(u_{i+2}^{n}-8 u_{i+1}^{n}+8 u_{i-1}^{n}-u_{i-2}^{n}\right) .
$$

(a) Show that $G=1-\frac{\lambda a}{3}(4-\cos \phi) \sin \phi l$.
(b) Based on the results of part (a), show that this method is unconditionally linearly unstable.
(c) This method is centered, just like FTCS. Does the wider centered stencil make the method more or less stable relative to FTCS? In other words, is $|G|^{2}$ for this method greater than or less than $|G|^{2}$ for FTCS, as given by Equation (15.7)?
15.6 Consider the following numerical method:

$$
u_{i+1}^{n}=u_{i}^{n}-\lambda\left(\hat{f}_{i+1 / 2}^{n}-\hat{f}_{i-1 / 2}^{n}\right),
$$

where

$$
\hat{f}_{i+1 / 2}^{n}=\frac{1}{2}\left(f\left(u_{i+1}^{n}\right)+f\left(u_{i}^{n}\right)\right)+\frac{1}{2} \delta\left|a_{i+1 / 2}^{n}\right|\left(u_{i+2}^{n}-3 u_{i+1}^{n}+3 u_{i}^{n}-u_{i-1}^{n}\right)
$$

and where $\delta=$ const. and $a_{i+1 / 2}^{n}$ is any average wave speed. Notice that this method is central differences plus fourth-order artificial viscosity; this method will be used in Section 22.3. Perform a von Neumann stability analysis. Write $|G|^{2}$ in the simplest possible form and plot $|G|^{2}$ versus $-\pi \leq \phi \leq \pi$ for
(a) $\lambda a=0.8, \delta=1 / 2$,
(b) $\lambda a=0.8, \delta=1 / 4$,
(c) $\lambda a=0.4, \delta=1 / 2$,
(d) $\lambda a=0.4, \delta=1 / 4$.
15.7 Consider the following numerical method:

$$
u_{i+1}^{n}=u_{i}^{n}-\lambda\left(\hat{f}_{i+1 / 2}^{n}-\hat{f}_{i-1 / 2}^{n}\right),
$$

where

$$
\begin{aligned}
\hat{f}_{i+1 / 2}^{n}= & \frac{1}{2}\left(f\left(u_{i+1}^{n}\right)+f\left(u_{i}^{n}\right)\right) \\
& -\frac{1}{2}\left|a_{i+1 / 2}^{n}\right|\left[\frac{1}{2}\left(u_{i+1}^{n}-u_{i}^{n}\right)-\frac{1}{2} \delta\left(u_{i+2}^{n}-3 u_{i+1}^{n}+3 u_{i}^{n}-u_{i-1}^{n}\right)\right]
\end{aligned}
$$

and where $\delta=$ const. and $a_{i+1 / 2}^{n}$ is any average wave speed. This method is central differences plus second- and fourth-order artificial viscosity; a similar method will be used in Section 22.3. Perform a von Neumann stability analysis. Write $|G|^{2}$ in the simplest possible form and plot $|G|^{2}$ versus $-\pi \leq \phi \leq \pi$ for
(a) $\lambda a=0.8, \delta=1 / 2$,
(b) $\lambda a=0.8, \delta=1 / 4$,
(c) $\lambda a=0.4, \delta=1 / 2$,
(d) $\lambda a=0.4, \delta=1 / 4$.
15.8 Write FTFS for the linear advection equation in artificial viscosity form. Use the results of Example 15.4 to find linear stability bounds on the CFL condition. Do your results agree with those of Example 15.2?
15.9 Consider the Boris and Book first-order upwind method, as described in Problem 11.7. Show that this method is linearly stable for $\lambda|a| \leq \sqrt{3} / 2 \approx 0.866$. You may wish to use the results of Example 15.4.
15.10 Consider the following finite-difference approximation:
$u_{i}^{n+1}=u_{i}^{n}-\lambda u_{i}^{n}\left(u_{i}^{n}-u_{i-1}^{n}\right)$.
What does von Neumann stability analysis say about this method? Be careful.
15.11 Show that FTCS for the linear advection equation is not sensitive to small disturbances, despite the fact that it is highly unstable. More specifically, consider the following linear advection problem on a periodic domain $[-1,1]$ :

$$
\begin{aligned}
& \frac{\partial u}{\partial t}+\frac{\partial u}{\partial x}=0 \\
& u(x, 0)= \begin{cases}1 & |x| \leq 1 / 3 \\
0 & |x|>1 / 3\end{cases}
\end{aligned}
$$

(a) Approximate $u(x, 2)$ using FTCS with 20 cells and $\lambda=\Delta t / \Delta x=0.8$. Verify that your results agree with Figure 11.6.
(b) Perturb your initial conditions using a $2 \Delta x$-wave with an amplitude of 0.1 . That is, alternatively add and subtract 0.1 from the samples in the initial conditions. Make sure that the initial conditions remain periodic. Approximate $u(x, 2)$ using FTCS with 20 cells and $\lambda=\Delta t / \Delta x=0.8$. Compare the results with those of part (a). The initial conditions differ by $10 \%$ in the $\infty$-norm. Do the results for $u(x, 2)$ differ by more or less than $10 \%$ in the $\infty$-norm? That is, have the relative differences grown or shrunk?
(c) Repeat part (b), except this time use a $10 \Delta x$-wave. Is the relative difference in $u(x, 2)$ sensitive to the frequency of the disturbance in the initial conditions?
15.12 Consider the leapfrog method applied to the linear advection equation.
(a) Show that the first term on the right-hand side of the modified equation is

$$
\frac{\partial u}{\partial t}+a \frac{\partial u}{\partial x}=\frac{a \Delta x^{2}}{6}\left((\lambda a)^{2}-1\right) \frac{\partial^{3} u}{\partial t^{3}}+\cdots
$$

What does this indicate about the dissipation, dispersion, and stability of the leapfrog method? Are there any special CFL numbers where the first term on the right-hand side vanishes?
(b) Show that the first two terms on the right-hand side of the modified equation are

$$
\frac{\partial u}{\partial t}+a \frac{\partial u}{\partial x}=\frac{a \Delta x^{2}}{6}\left((\lambda a)^{2}-1\right) \frac{\partial^{3} u}{\partial t^{3}}-\frac{a \Delta x^{4}}{120}\left(9(\lambda a)^{4}-10(\lambda a)^{2}+1\right) \frac{\partial^{5} u}{\partial t^{5}}+\cdots
$$

What do these two terms indicate about the dissipation, dispersion, and stability of the leapfrog method? Are there any special CFL numbers where either or both of the first two terms on the right-hand side vanish?

