


# Problem 1: Centered expansion fan and simple-wave structure


_( 65 points, plus 4 possible extra credit)_



> [!exercise]
> We consider steady, inviscid, supersonic flow undergoing a turning through a corner located at the origin. The upstream flow is uniform, with Mach number $M_1>1$, velocity magnitude $V_1$, and flow angle $\theta_1=0$. The wall turns the flow through a negative angle $\theta_2<0$, generating an expansion.
> 
> 
> 
> 
> 
> ![[Pasted image 20260509005506.png|500]]
> 
> 
> 
> 
> **(a) Characteristic structure**
> 
> Sketch the characteristic families ( $C_{+}$and $C_{-}$) in the following regions:
> (i) upstream of the corner,
> (ii) within the expansion fan,
> (iii) downstream of the fan.
> 
> Clearly indicate which characteristics are straight and which are curved, and explain why.
> 
> 
> **(b) Invariant structure and physical interpretation**
> 
> Using your sketch, argue which characteristic invariant is constant throughout the expansion region.
> 
> Explain:
> (i) why this invariant remains constant globally,
> (ii) what this implies about how the flow variables must vary within the fan.
> 
> 
> **(c) Solution strategy**
> 
> Based on your reasoning above, explain how the flow can be solved within the expansion region.
> 
> Your answer should:
> 
> 
> - describe the role of the constant invariant,
> - identify the independent variable governing the solution,
> - outline the steps needed to compute the flow state.
> 
> You may reference the algorithm provided in the lecture notes.
> 
> 
> 
> **(d) Numerical solution**
> 
> Using the procedure described above, compute the flow state within the expansion fan for
> 
> $$
> M_1=2.4, \quad T_1=300 K, \quad \theta_2=-12^{\circ} .
> $$
> 
> 
> For this computation, you may assume a calorically perfect gas with $\gamma=1.4$ and $R= 287 \mathrm{~J} /(\mathrm{kgK})$. You should choose a consistent normalization for the upstream state (e.g., specify $a_1$ or $T_1$ ) and use the fact that the flow is isentropic within the expansion fan to relate velocity and sound speed through the fan.
> 
> Plot the following as functions of the turning angle:
> 
> $$
> M(\theta), \quad V(\theta), \quad a(\theta) .
> $$
> 
> 
> 
> **(e) Characteristic-based visualization**
> 
> Create an accurate plot for the solution you just obtained (i.e., use code, don't just sketch it) that includes:
> - the wall,
> - representative $C_{+}$and $C_{-}$characteristic families,
> - characteristics upstream, within, and downstream of the fan,
> - one characteristic that originates upstream, propagates through the fan, and continues downstream.
> 
> Clearly distinguish between straight and curved segments.
> 
> 
> **(f) Bonus: flow evolution along a characteristic**
> 
> Color the traced characteristic from part (e) according to the magnitude of the velocity along the curve.
> 
> 








##### problem 1.a

The characteristic directions are

$$
C_{+}:\frac{dy}{dx}=\tan(\theta-\mu),
\qquad
C_{-}:\frac{dy}{dx}=\tan(\theta+\mu),
$$

where

$$
\mu=\sin^{-1}\left(\frac{1}{M}\right).
$$

Upstream of the corner the flow is uniform, so

$$
\theta=\theta_1,
\qquad
M=M_1,
\qquad
\mu=\mu_1=\sin^{-1}\left(\frac{1}{M_1}\right).
$$

Therefore the upstream characteristic slopes are constant:

$$
C_{+}:\frac{dy}{dx}=\tan(\theta_1-\mu_1),
\qquad
C_{-}:\frac{dy}{dx}=\tan(\theta_1+\mu_1).
$$

Since each slope is constant, both upstream characteristic families are straight parallel lines.

Inside the centered expansion fan, the fan itself is made of the $C_{-}$family. Each $C_{-}$characteristic in the fan is a ray from the corner, and its direction is

$$
\alpha=\theta+\mu.
$$

The first ray is attached to the upstream state, so

$$
\alpha_1=\theta_1+\mu_1.
$$

The last ray is attached to the downstream state, so

$$
\alpha_2=\theta_2+\mu_2,
\qquad
\mu_2=\sin^{-1}\left(\frac{1}{M_2}\right).
$$

Thus the $C_{-}$characteristics in the fan are straight rays filling the sector between

$$
y=x\tan(\theta_1+\mu_1)
$$

and

$$
y=x\tan(\theta_2+\mu_2).
$$

The $C_{+}$characteristics behave differently. As a $C_{+}$characteristic enters the fan, the local values of $\theta$ and $M$ change continuously. Since

$$
\frac{dy}{dx}=\tan(\theta-\mu)
$$

and

$$
\mu=\sin^{-1}\left(\frac{1}{M}\right),
$$

the slope of a $C_{+}$characteristic changes continuously while it passes through the fan. Therefore the $C_{+}$characteristics are curved inside the fan.

Downstream of the fan the flow is again uniform, so

$$
\theta=\theta_2,
\qquad
M=M_2,
\qquad
\mu=\mu_2.
$$

The downstream slopes are therefore constant:

$$
C_{+}:\frac{dy}{dx}=\tan(\theta_2-\mu_2),
\qquad
C_{-}:\frac{dy}{dx}=\tan(\theta_2+\mu_2).
$$

Hence both downstream characteristic families are straight parallel lines again.



![[Pasted image 20260509035745.png|500]]



```mathematica title:""
Clear["Global`*"];

gamma = 1.4;
M1 = 2.4;
theta1 = 0;
theta2 = -12 Degree;

nu[M_] :=
  Sqrt[(gamma + 1)/(gamma - 1)]*
    ArcTan[Sqrt[((gamma - 1)/(gamma + 1)) (M^2 - 1)]] -
   ArcTan[Sqrt[M^2 - 1]];

M2 = M /. FindRoot[
    nu[M] == nu[M1] + (theta1 - theta2),
    {M, M1 + 0.5}
    ];

mu[M_] := ArcSin[1/M];

mu1 = mu[M1];
mu2 = mu[M2];

alpha1 = theta1 + mu1;
alpha2 = theta2 + mu2;

beta1 = theta1 - mu1;
beta2 = theta2 - mu2;

thetaGrid = Subdivide[theta2, theta1, 240];
machGrid =
  Table[
   M /. FindRoot[
     nu[M] == nu[M1] - (th - theta1),
     {M, M1}
     ],
   {th, thetaGrid}
   ];
muGrid = mu /@ machGrid;
alphaGrid = thetaGrid + muGrid;

thetaOfAlpha = Interpolation[Transpose[{alphaGrid, thetaGrid}]];
muOfAlpha = Interpolation[Transpose[{alphaGrid, muGrid}]];

mPlusFan[phi_?NumericQ] := Tan[thetaOfAlpha[phi] - muOfAlpha[phi]];

xMin = -2.8;
xMax = 6.6;
yMin = -1.05;
yMax = 2.85;

cMinusColor = RGBColor[0.10, 0.35, 0.75];
cPlusColor = RGBColor[0.80, 0.15, 0.12];
curveHighlightColor = RGBColor[0.95, 0.05, 0.04];

direction[angle_] := {Cos[angle], Sin[angle]};

cPlusCurve[xh_] :=
 Module[
  {phi, x, xSol, fanPts, h, t, start, xWall, finish},
  
  phi[s_] := alpha1 + s (alpha2 - alpha1);
  
  xSol =
   NDSolveValue[
    {
     x'[s] ==
      (alpha2 - alpha1) x[s] Sec[phi[s]]^2/
       (mPlusFan[phi[s]] - Tan[phi[s]]),
     x[0] == xh
     },
    x,
    {s, 0, 1}
    ];
  
  fanPts =
   Table[
    {xSol[s], xSol[s] Tan[phi[s]]},
    {s, 0, 1, 0.025}
    ];
  
  h = First[fanPts];
  t = Last[fanPts];
  
  start = {xMin, h[[2]] + Tan[beta1] (xMin - h[[1]])};
  
  xWall =
   (t[[2]] - Tan[beta2] t[[1]])/
    (Tan[theta2] - Tan[beta2]);
  finish =
   {
    Min[xMax, xWall],
    t[[2]] + Tan[beta2] (Min[xMax, xWall] - t[[1]])
    };
  
  {
   {Dashed, cPlusColor, AbsoluteThickness[2.2], Line[{start, h}]},
   {Dashed, curveHighlightColor, AbsoluteThickness[2.4], Line[fanPts]},
   {Dashed, cPlusColor, AbsoluteThickness[2.2], Line[{t, finish}]}
   }
  ];

wall =
  {
   {Black, AbsoluteThickness[3.5], Line[{{xMin, 0}, {0, 0}}]},
   {Black, AbsoluteThickness[3.5],
    Line[{{0, 0}, {xMax, xMax Tan[theta2]}}]}
   };

fanRays =
  Table[
   {cMinusColor, Thick, Opacity[0.75],
    Line[{{0, 0}, {xMax, xMax Tan[angle]}}]},
   {angle, Subdivide[alpha1, alpha2, 7]}
   ];

fanBoundaries =
  {
   {cMinusColor, AbsoluteThickness[3],
    Line[{{0, 0}, {xMax, xMax Tan[alpha1]}}]},
   {cMinusColor, AbsoluteThickness[3],
    Line[{{0, 0}, {xMax, xMax Tan[alpha2]}}]}
   };

upstreamCMinus =
  Table[
   {Dashed, cMinusColor, Opacity[0.62], Thick,
    Line[{{xMin, Tan[alpha1] xMin + b}, {0, b}}]},
   {b, {0.45, 0.95, 1.45}}
   ];

downstreamCMinus =
  Table[
   With[
    {xStart = -b/(Tan[alpha2] - Tan[theta2])},
    {Dashed, cMinusColor, Opacity[0.62], Thick,
     Line[{{xStart, Tan[theta2] xStart},
       {xMax, Tan[alpha2] xMax + b}}]}
    ],
   {b, {-0.18, -0.42, -0.66}}
   ];

cPlusFamily =
  {
   cPlusCurve[0.70],
   cPlusCurve[1.15],
   cPlusCurve[1.60],
   cPlusCurve[2.05]
   };

Graphics[
 {
  wall,
  fanRays,
  fanBoundaries,
  upstreamCMinus,
  downstreamCMinus,
  cPlusFamily,
  
  Text[Style["upstream: straight C+ and C-", 13], {-1.35, 2.42}],
  Text[Style["fan: straight C- rays, curved C+", 13], {2.85, 0.78}],
  Text[Style["downstream: straight characteristics", 13], {4.75, 0.22}],
  
  Inset[
   LineLegend[
    {cPlusColor, cMinusColor},
    {Subscript[C, "+"], Subscript[C, "-"]},
    LegendLayout -> "Column"
    ],
   Scaled[{0.86, 0.86}]
   ]
  },
 Axes -> True,
 GridLines -> Automatic,
 PlotRange -> {{xMin, xMax}, {yMin, yMax}},
 AspectRatio -> 0.55,
 ImageSize -> Large,
 AxesLabel -> {"x", "y"},
 PlotLabel -> Style["Characteristic structure of a centered expansion fan", 18, Bold]
 ]
```


##### problem 1.b

The compatibility relations for steady two-dimensional supersonic flow give the characteristic invariants

$$
\theta+v(M)=\text{constant along }C_{+},
\qquad
\theta-v(M)=\text{constant along }C_{-},
$$

where $v(M)$ is the Prandtl-Meyer function. These two relations do not mean that both quantities are constant everywhere in the fan. They mean that each quantity is constant only along its own characteristic family.

For the centered expansion fan, the sketch shows that the $C_{+}$characteristics all enter the fan from the upstream uniform region. In that upstream region,

$$
\theta=\theta_1,
\qquad
M=M_1,
$$

so every incoming $C_{+}$characteristic carries the same value of the $C_{+}$invariant:

$$
I_{+}
=
\theta+v(M)
=
\theta_1+v(M_1).
$$

Since $I_{+}$ is constant along each $C_{+}$characteristic, and since all of the $C_{+}$characteristics entering the fan have the same upstream value, the same relation holds throughout the expansion fan:

$$
\boxed{
\theta+v(M)=\theta_1+v(M_1).
}
$$

Thus the invariant that remains constant throughout the expansion region is

$$
\theta+v(M).
$$

The corresponding $C_{-}$invariant,

$$
\theta-v(M),
$$

is still constant along any one $C_{-}$characteristic, but it is not the same from one $C_{-}$ray to the next. This is visible in the centered fan: the $C_{-}$rays all emanate from the corner and fill the fan, with each ray corresponding to a different intermediate state between the upstream and downstream uniform states.

The global invariant relation forces $\theta$ and $M$ to vary together rather than independently. Solving the boxed relation for the flow angle gives

$$
\theta
=
\theta_1+v(M_1)-v(M).
$$

Equivalently,

$$
v(M)
=
v(M_1)-(\theta-\theta_1).
$$

Since the wall turns downward in this problem,

$$
\theta_2<\theta_1,
$$

and therefore inside the fan

$$
\theta-\theta_1<0.
$$

Substituting this sign into the invariant relation gives

$$
v(M)
=
v(M_1)-(\theta-\theta_1)
>
v(M_1).
$$

Because the Prandtl-Meyer function increases with $M$ for supersonic flow, this means

$$
M>M_1
$$

as the flow expands through the fan. Thus the fan is a simple-wave region: the state varies continuously from ray to ray, but all variables are tied to a single parameter, such as $\theta$, $M$, or the ray angle $\alpha=\theta+\mu$. Along each individual $C_{-}$ray the state is fixed, while moving across the fan from the leading ray to the trailing ray changes the Mach number, flow angle, Mach angle, velocity, and thermodynamic state continuously.


##### problem 1.c

The solution inside the expansion fan is simpler than a general two-family characteristic marching problem because the $C_{+}$invariant is fixed globally. From part (b),

$$
\theta+v(M)=\theta_1+v(M_1).
$$

This equation gives one direct relation between the flow angle and the Mach number throughout the fan. Solving for $v(M)$ gives

$$
v(M)
=
v(M_1)-(\theta-\theta_1).
$$

Thus, if a value of $\theta$ is chosen inside the fan, the corresponding Mach number is obtained by solving

$$
v(M)-v(M_1)+(\theta-\theta_1)=0.
$$

Equivalently, the fan can be parameterized by the $C_{-}$ray angle

$$
\alpha=\theta+\mu,
\qquad
\mu=\sin^{-1}\left(\frac{1}{M}\right),
$$

but using $\theta$ is the most direct computational choice because the wall turning angle is prescribed. The independent variable for the fan solution can therefore be taken to be

$$
\theta\in[\theta_2,\theta_1].
$$

For each value of $\theta$, the computation proceeds as follows. First compute the target Prandtl-Meyer value

$$
v_{\text{target}}
=
v(M_1)-(\theta-\theta_1).
$$

Then solve

$$
v(M)=v_{\text{target}}
$$

for the local Mach number $M$. Once $M$ is known, compute the local Mach angle

$$
\mu=\sin^{-1}\left(\frac{1}{M}\right).
$$

The corresponding $C_{-}$ray is then assigned the direction

$$
\alpha=\theta+\mu,
$$

so its equation is

$$
y=x\tan(\alpha).
$$

The state is constant along this ray because the centered expansion fan is self-similar: moving outward from the corner along a fixed ray does not change $\theta$ or $M$. The flow varies only when moving from one ray to another.

After $M$ has been found, the remaining velocity quantities follow from the isentropic energy relation. For a calorically perfect gas,

$$
a^2\left(1+\frac{\gamma-1}{2}M^2\right)=\text{constant}.
$$

The constant is fixed by the upstream state:

$$
a^2\left(1+\frac{\gamma-1}{2}M^2\right)
=
a_1^2\left(1+\frac{\gamma-1}{2}M_1^2\right).
$$

Therefore

$$
a(M)
=
a_1
\sqrt{
\frac{1+\frac{\gamma-1}{2}M_1^2}
{1+\frac{\gamma-1}{2}M^2}
}.
$$

Finally,

$$
V(M)=M\,a(M).
$$

So the full fan solution is obtained by sweeping through the turning angle $\theta$, inverting the Prandtl-Meyer function to find $M(\theta)$, computing $\mu(\theta)$ and the ray angle $\alpha(\theta)$, and then recovering $a(\theta)$ and $V(\theta)$ from the isentropic relation.






##### problem 1.d

For this numerical case, the result from part (c) can be used directly. Since $\theta_1=0$, the fan relation becomes

$$
v(M(\theta))
=
v(M_1)-\theta,
\qquad
-12^\circ\leq \theta\leq 0^\circ.
$$

With $M_1=2.4$, this means the downstream Mach number is determined by the following equation, with the angle converted to radians in the computation:

$$
v(M_2)
=
v(2.4)+12^\circ.
$$

Once $M(\theta)$ is known, the sound speed and velocity magnitude follow from

$$
a(\theta)
=
a_1
\sqrt{
\frac{1+\frac{\gamma-1}{2}M_1^2}
{1+\frac{\gamma-1}{2}M(\theta)^2}
},
\qquad
V(\theta)=M(\theta)a(\theta),
$$

where

$$
a_1=\sqrt{\gamma R T_1}.
$$

Using $\gamma=1.4$, $R=287\ \text{J/(kg K)}$, and $T_1=300\ \text{K}$ gives

$$
\begin{aligned}
M(0^\circ)&=2.40000,
&
M(-12^\circ)&=2.94813,
\\
a(0^\circ)&=347.19\ \text{m/s},
&
a(-12^\circ)&=307.78\ \text{m/s},
\\
V(0^\circ)&=833.25\ \text{m/s},
&
V(-12^\circ)&=907.39\ \text{m/s}.
\end{aligned}
$$

The Mach number and velocity increase through the expansion fan, while the sound speed decreases because the gas expands and cools.



![[Pasted image 20260509061851.png|300]]



![[Pasted image 20260509061904.png|300]]



![[Pasted image 20260509061918.png|300]]



```mathematica title:""
Clear["Global`*"]

gamma = 1.4;
R = 287;
M1 = 2.4;
T1 = 300;
theta1 = 0 Degree;
theta2 = -12 Degree;

a1 = Sqrt[gamma R T1];

nu[M_] := Sqrt[(gamma + 1)/(gamma - 1)]*
    ArcTan[Sqrt[((gamma - 1)/(gamma + 1)) (M^2 - 1)]] -
   ArcTan[Sqrt[M^2 - 1]];

targetNu[theta_] := nu[M1] - (theta - theta1);

mOfTheta[theta_?NumericQ] := mOfTheta[theta] =
  M /. FindRoot[
    nu[M] == targetNu[theta],
    {M, M1, 1.000001, 10}
    ];

aOfM[M_] := a1*
  Sqrt[(1 + ((gamma - 1)/2) M1^2)/(1 + ((gamma - 1)/2) M^2)];

aOfTheta[theta_?NumericQ] := aOfM[mOfTheta[theta]];
speedOfTheta[theta_?NumericQ] := mOfTheta[theta] aOfTheta[theta];

thetaValues = Subdivide[theta2, theta1, 200];

solutionData = Table[
   {theta/Degree, mOfTheta[theta], speedOfTheta[theta], aOfTheta[theta]},
   {theta, thetaValues}
   ];

endpointValues = {
    {"M(0 deg)", M1},
    {"M(-12 deg)", mOfTheta[theta2]},
    {"a(0 deg) (m/s)", a1},
    {"a(-12 deg) (m/s)", aOfTheta[theta2]},
    {"V(0 deg) (m/s)", M1 a1},
    {"V(-12 deg) (m/s)", speedOfTheta[theta2]}
    } // N;

mPlot = ListLinePlot[
   solutionData[[All, {1, 2}]],
   Frame -> True,
   FrameLabel -> {"theta (deg)", "M"},
   PlotStyle -> Directive[Blue, Thick],
   GridLines -> Automatic,
   ImageSize -> Large
   ];

vPlot = ListLinePlot[
   solutionData[[All, {1, 3}]],
   Frame -> True,
   FrameLabel -> {"theta (deg)", "V [m/s]"},
   PlotStyle -> Directive[Red, Thick],
   GridLines -> Automatic,
   ImageSize -> Large
   ];

aPlot = ListLinePlot[
   solutionData[[All, {1, 4}]],
   Frame -> True,
   FrameLabel -> {"theta (deg)", "a [m/s]"},
   PlotStyle -> Directive[Darker[Green], Thick],
   GridLines -> Automatic,
   ImageSize -> Large
   ];

Column[
 {
  Grid[endpointValues, Frame -> All],
  mPlot,
  vPlot,
  aPlot
  }
 ]
```


##### problem 1.e

The characteristic visualization uses the numerical state from part (d). The $C_{-}$characteristics inside the fan are the straight rays

$$
y=x\tan\alpha,
\qquad
\alpha=\theta+\mu,
$$

where $\alpha$ ranges from $\alpha_1=\theta_1+\mu_1$ to $\alpha_2=\theta_2+\mu_2$. A $C_{+}$characteristic passing through the fan is traced by using $\alpha$ as the parameter along the fan. Since the point on the curve lies on one of the $C_{-}$rays,

$$
y=x\tan\alpha.
$$

Along the $C_{+}$curve,

$$
\frac{dy}{dx}=\tan(\theta(\alpha)-\mu(\alpha)).
$$

Differentiating $y=x\tan\alpha$ with respect to $\alpha$ and equating the slope to the local $C_{+}$direction gives

$$
\frac{dx}{d\alpha}
=
\frac{x\sec^2\alpha}
{\tan(\theta(\alpha)-\mu(\alpha))-\tan\alpha}.
$$

This equation is used only inside the fan. Before entering the fan, the traced $C_{+}$characteristic is a straight line with slope $\tan(\theta_1-\mu_1)$. After leaving the fan, it is a straight line with slope $\tan(\theta_2-\mu_2)$.


![[Pasted image 20260509062659.png|500]]


```mathematica title:""
Clear["Global`*"];

gamma = 1.4;
M1 = 2.4;
theta1 = 0 Degree;
theta2 = -12 Degree;

nu[M_] := Sqrt[(gamma + 1)/(gamma - 1)]*
    ArcTan[Sqrt[((gamma - 1)/(gamma + 1)) (M^2 - 1)]] -
   ArcTan[Sqrt[M^2 - 1]];

M2 = M /. FindRoot[
    nu[M] == nu[M1] - (theta2 - theta1),
    {M, M1 + 0.5}
    ];

mu[M_] := ArcSin[1/M];

mu1 = mu[M1];
mu2 = mu[M2];

alpha1 = theta1 + mu1;
alpha2 = theta2 + mu2;
beta1 = theta1 - mu1;
beta2 = theta2 - mu2;

thetaGrid = Subdivide[theta2, theta1, 260];
machGrid =
  Table[
   M /. FindRoot[
     nu[M] == nu[M1] - (theta - theta1),
     {M, M1, 1.000001, 10}
     ],
   {theta, thetaGrid}
   ];

muGrid = mu /@ machGrid;
alphaGrid = thetaGrid + muGrid;

thetaOfAlpha = Interpolation[Transpose[{alphaGrid, thetaGrid}]];
muOfAlpha = Interpolation[Transpose[{alphaGrid, muGrid}]];

cPlusSlopeInFan[alpha_?NumericQ] :=
  Tan[thetaOfAlpha[alpha] - muOfAlpha[alpha]];

xMin = -2.8;
xMax = 6.6;
yMin = -1.05;
yMax = 2.85;

cMinusColor = RGBColor[0.10, 0.35, 0.75];
cPlusColor = RGBColor[0.80, 0.15, 0.12];
traceColor = RGBColor[0.55, 0.00, 0.00];

cPlusCharacteristic[xLead_, straightStyle_, fanStyle_] :=
 Module[
  {alpha, xSol, fanPts, enterPt, exitPt, startPt, xWall, endPt},
  
  alpha[s_] := alpha1 + s (alpha2 - alpha1);
  
  xSol =
   NDSolveValue[
    {
     x'[s] ==
      (alpha2 - alpha1) x[s] Sec[alpha[s]]^2/
       (cPlusSlopeInFan[alpha[s]] - Tan[alpha[s]]),
     x[0] == xLead
     },
    x,
    {s, 0, 1}
    ];
  
  fanPts =
   Table[
    {xSol[s], xSol[s] Tan[alpha[s]]},
    {s, 0, 1, 0.02}
    ];
  
  enterPt = First[fanPts];
  exitPt = Last[fanPts];
  
  startPt =
   {xMin, enterPt[[2]] + Tan[beta1] (xMin - enterPt[[1]])};
  
  xWall =
   (exitPt[[2]] - Tan[beta2] exitPt[[1]])/
    (Tan[theta2] - Tan[beta2]);
  endPt =
   {Min[xMax, xWall],
    exitPt[[2]] + Tan[beta2] (Min[xMax, xWall] - exitPt[[1]])};
  
  {
   Join[straightStyle, {Line[{startPt, enterPt}]}],
   Join[fanStyle, {Line[fanPts]}],
   Join[straightStyle, {Line[{exitPt, endPt}]}]
   }
  ];

wall =
  {
   {Black, AbsoluteThickness[3.5], Line[{{xMin, 0}, {0, 0}}]},
   {Black, AbsoluteThickness[3.5],
    Line[{{0, 0}, {xMax, xMax Tan[theta2]}}]}
   };

fanRays =
  Table[
   {cMinusColor, Opacity[0.70], Thick,
    Line[{{0, 0}, {xMax, xMax Tan[angle]}}]},
   {angle, Subdivide[alpha1, alpha2, 8]}
   ];

fanBoundaries =
  {
   {cMinusColor, AbsoluteThickness[3.2],
    Line[{{0, 0}, {xMax, xMax Tan[alpha1]}}]},
   {cMinusColor, AbsoluteThickness[3.2],
    Line[{{0, 0}, {xMax, xMax Tan[alpha2]}}]}
   };

upstreamCMinus =
  Table[
   {Dashed, cMinusColor, Opacity[0.55], Thick,
    Line[{{xMin, Tan[alpha1] xMin + b}, {0, b}}]},
   {b, {0.45, 0.95, 1.45}}
   ];

downstreamCMinus =
  Table[
   With[
    {xStart = -b/(Tan[alpha2] - Tan[theta2])},
    {Dashed, cMinusColor, Opacity[0.55], Thick,
     Line[{{xStart, Tan[theta2] xStart},
       {xMax, Tan[alpha2] xMax + b}}]}
    ],
   {b, {-0.18, -0.42, -0.66}}
   ];

backgroundCPlus =
  cPlusCharacteristic[
     #,
     {Dashed, cPlusColor, Opacity[0.45], AbsoluteThickness[2]},
     {Dashed, cPlusColor, Opacity[0.45], AbsoluteThickness[2]}
     ] & /@ {0.75, 1.95, 2.35};

tracedCPlus =
  cPlusCharacteristic[
   1.35,
   {Dashed, traceColor, AbsoluteThickness[3.2]},
   {Dashed, traceColor, AbsoluteThickness[3.2]}
   ];

Graphics[
 {
  wall,
  upstreamCMinus,
  downstreamCMinus,
  fanRays,
  fanBoundaries,
  backgroundCPlus,
  tracedCPlus,
  
  Text[Style["upstream: straight characteristics", 12], {-1.45, 2.45}],
  Text[Style["fan: C- rays and curved C+", 12], {2.75, 0.76}],
  Text[Style["downstream: straight characteristics", 12], {4.75, 0.20}],
  
  Inset[
   LineLegend[
    {
     Directive[Dashed, cPlusColor],
     Directive[cMinusColor],
     Directive[Dashed, traceColor, AbsoluteThickness[3]]
     },
    {Subscript[C, "+"], Subscript[C, "-"], Row[{"traced ", Subscript[C, "+"]}]},
    LegendLayout -> "Column"
    ],
   Scaled[{0.84, 0.84}]
   ]
  },
 Axes -> True,
 AxesLabel -> {"x", "y"},
 GridLines -> Automatic,
 PlotRange -> {{xMin, xMax}, {yMin, yMax}},
 AspectRatio -> 0.55,
 ImageSize -> Large,
 PlotLabel ->
  Style["Characteristic visualization for the numerical expansion fan", 18,
   Bold]
 ]
```


##### problem 1.f



The speed is constant on the upstream straight segment, varies through the fan, and is constant again on the downstream straight segment. Inside the fan the local velocity magnitude is determined by the same one-parameter solution used above:

$$
V(\alpha)=M(\alpha)a(\alpha),
\qquad
\alpha=\theta+\mu.
$$

Thus the traced characteristic from part (e) can be divided into short line segments and each segment can be colored according to the local value of $V$.

The following cell uses the geometry already defined in part (e) and replaces the traced characteristic by a velocity-colored version.



![[Pasted image 20260509062623.png|500]]



```mathematica title:""
T1 = 300;
R = 287;

a1 = Sqrt[gamma R T1];
aOfM[M_] := a1*
  Sqrt[(1 + ((gamma - 1)/2) M1^2)/(1 + ((gamma - 1)/2) M^2)];
speedOfM[M_] := M aOfM[M];

machOfAlpha = Interpolation[Transpose[{alphaGrid, machGrid}]];
speedOfAlpha[alpha_?NumericQ] := speedOfM[machOfAlpha[alpha]];

speed1 = speedOfM[M1];
speed2 = speedOfM[M2];

speedColor[V_] := ColorData["Rainbow"][Rescale[V, {speed1, speed2}]];

coloredSegments[pts_, speeds_] :=
  Table[
   {
    speedColor[Mean[speeds[[i ;; i + 1]]]],
    AbsoluteThickness[3.6],
    Line[pts[[i ;; i + 1]]]
    },
   {i, 1, Length[pts] - 1}
   ];

coloredTrace[xLead_] :=
 Module[
  {alpha, xSol, fanPts, fanSpeeds, enterPt, exitPt, startPt,
   xWall, endPt, upstreamPts, upstreamSpeeds, downstreamPts,
   downstreamSpeeds},
  
  alpha[s_] := alpha1 + s (alpha2 - alpha1);
  
  xSol =
   NDSolveValue[
    {
     x'[s] ==
      (alpha2 - alpha1) x[s] Sec[alpha[s]]^2/
       (cPlusSlopeInFan[alpha[s]] - Tan[alpha[s]]),
     x[0] == xLead
     },
    x,
    {s, 0, 1}
    ];
  
  fanPts =
   Table[
    {xSol[s], xSol[s] Tan[alpha[s]]},
    {s, 0, 1, 0.02}
    ];
  fanSpeeds = Table[speedOfAlpha[alpha[s]], {s, 0, 1, 0.02}];
  
  enterPt = First[fanPts];
  exitPt = Last[fanPts];
  
  startPt =
   {xMin, enterPt[[2]] + Tan[beta1] (xMin - enterPt[[1]])};
  
  xWall =
   (exitPt[[2]] - Tan[beta2] exitPt[[1]])/
    (Tan[theta2] - Tan[beta2]);
  endPt =
   {Min[xMax, xWall],
    exitPt[[2]] + Tan[beta2] (Min[xMax, xWall] - exitPt[[1]])};
  
  upstreamPts = {startPt, enterPt};
  upstreamSpeeds = {speed1, speed1};
  
  downstreamPts = {exitPt, endPt};
  downstreamSpeeds = {speed2, speed2};
  
  Join[
   coloredSegments[upstreamPts, upstreamSpeeds],
   coloredSegments[fanPts, fanSpeeds],
   coloredSegments[downstreamPts, downstreamSpeeds]
   ]
  ];

Graphics[
 {
  wall,
  upstreamCMinus,
  downstreamCMinus,
  fanRays,
  fanBoundaries,
  backgroundCPlus,
  coloredTrace[1.35],
  
  Text[Style["velocity increases along the traced C+", 12], {2.95, 0.88}],
  
  Inset[
   BarLegend[
    {speedColor, {speed1, speed2}},
    LegendLabel -> "V [m/s]"
    ],
   Scaled[{0.86, 0.47}]
   ]
  },
 Axes -> True,
 AxesLabel -> {"x", "y"},
 GridLines -> Automatic,
 PlotRange -> {{xMin, xMax}, {yMin, yMax}},
 AspectRatio -> 0.55,
 ImageSize -> Large,
 PlotLabel ->
  Style["Traced characteristic colored by velocity magnitude", 18, Bold]
 ]
```



# Problem 2: Compression, smoothness, and shock formation ( 35 points)




> [!exercise]
> 
> We now consider compressive turning, $\theta_2>\theta_1$, and examine how the characteristic structure differs from the expansion case.
> 
> Figure 1 shows a sharp corner that turns the flow inward at a point, while Fig. 2 shows a smooth wall that gradually compresses the flow. In this problem, you will compare how compression develops in these two settings.
> 
> 
> **(a) Corner compression and immediate breakdown**
> Consider the sharp-corner compression shown in Fig. 1.
> 
> 
> 
> ![[Pasted image 20260509005802.png]]
> 
> 
> (i) Sketch the characteristic families that would arise if one attempted to construct a smooth centered compression analogous to the centered expansion fan.
> 
> 
> (ii) Based on your sketch, explain why this smooth construction breaks down. Your answer should explicitly address what happens to neighboring characteristics and what this implies about the flow state at points where they intersect.
> 
> 
> (iii) What physical structure replaces the invalid smooth solution? Briefly explain your reasoning.
> 
> 
> 
> 
> 
> **(b) Smooth compression and delayed breakdown**
> 
> Now consider the smooth compression geometry shown in Fig. 2.
> (i) Sketch the characteristic families for the smooth compression region. Your sketch should distinguish the family that carries the wall-imposed compression from the family that originates in the upstream uniform flow.
> 
> 
> (ii) Explain why a locally smooth compression can exist in this case, even though the sharpcorner compression fails. Your answer should reference the fact that the turning is distributed over a finite region rather than imposed at a single point.
> 
> 
> (iii) Is this smooth compression region a fully general two-family characteristic marching problem, or does it still have a degenerate/simple-wave structure? Explain. In particular, discuss what happens to the invariant carried by the characteristic family that originates in the upstream uniform flow.
> 
> 
> (iv) Explain why smooth compression waves may nevertheless eventually lead to shock formation. Your answer should describe the role of characteristic convergence and intersection.
> 
> If part of the flow is compressed smoothly while another part undergoes a shock, what qualitative differences would you expect in the downstream states of these regions? Briefly comment on how such differences might affect how the flow can (or cannot) recombine downstream.
> 


##### problem 2.a.i



![[Pasted image 20260509080743.png|500]]


![[Pasted image 20260509080811.png|500]]


The wall turns into the flow, so the compression is carried by the $C_{-}$family for this lower-wall geometry. The relevant characteristic direction is

$$
C_{-}:\frac{dy}{dx}=\tan(\theta+\mu).
$$

If one tries to construct a smooth centered compression analogous to the centered expansion fan, the compression characteristics must crowd together rather than spread apart. In a compression, the flow turns to larger $\theta$ while the Mach number decreases, so $\mu=\sin^{-1}(1/M)$ increases. Thus the $C_{-}$direction

$$
\alpha=\theta+\mu
$$

rotates upward through the attempted compression.


```mathematica title:""
Clear["Global`*"];

theta2 = 12 Degree;

xMin = -2.2;
xMax = 3.6;
yMin = -0.35;
yMax = 1.95;

corner = {0, 0};
failurePoint = {2.0, 1.35};

cMinusColor = RGBColor[0.10, 0.35, 0.75];
cPlusColor = RGBColor[0.80, 0.15, 0.12];

wall =
  {
   {Black, AbsoluteThickness[3.5], Line[{{xMin, 0}, {0, 0}}]},
   {Black, AbsoluteThickness[3.5],
    Line[{{0, 0}, {xMax, xMax Tan[theta2]}}]}
   };

contextCPlus =
  Table[
   {Dashed, cPlusColor, Opacity[0.45], AbsoluteThickness[2],
    Line[{{xMin, -0.45 xMin + b}, {1.15, -0.45 1.15 + b}}]},
   {b, {0.35, 0.82, 1.29}}
   ];

compressionCMinus =
  Map[
   {Dashed, cMinusColor, AbsoluteThickness[2.8], Line[{#, failurePoint}]} &,
   {{0.04, 0.00}, {0.18, 0.03}, {0.32, 0.07}, {0.46, 0.12},
    {0.60, 0.18}}
   ];

Graphics[
 {
  wall,
  contextCPlus,
  compressionCMinus,
  
  Text[Style["attempted C- compression characteristics", 12],
   {1.95, 1.62}],
  Text[Style["first intersection: smooth construction fails", 12],
   {2.25, 1.18}],
  
  Inset[
   LineLegend[
    {
     Directive[Dashed, cPlusColor],
     Directive[Dashed, cMinusColor]
     },
    {Subscript[C, "+"], Subscript[C, "-"]},
    LegendLayout -> "Column"
    ],
   Scaled[{0.84, 0.78}]
   ]
  },
 Axes -> False,
 PlotRange -> {{xMin, xMax}, {yMin, yMax}},
 AspectRatio -> 0.45,
 ImageSize -> Large,
 PlotLabel -> Style["Attempted centered compression", 16, Bold]
 ]
```


##### problem 2.a.ii

The attempted smooth construction breaks down because neighboring compression characteristics intersect. The same simple-wave relation would require

$$
v(M)=v(M_1)-(\theta-\theta_1).
$$

For compression,

$$
\theta-\theta_1>0,
$$

so

$$
v(M)=v(M_1)-(\theta-\theta_1)<v(M_1).
$$

Since $v(M)$ increases with $M$ in supersonic flow, the Mach number decreases through the compression. Then $\mu=\sin^{-1}(1/M)$ increases, so the $C_{-}$directions rotate toward one another. For a smooth distributed compression, this produces convergence over some distance. For a sharp corner, the turning is imposed at a point, so the convergence occurs immediately in the attempted centered construction.

At a characteristic intersection, the smooth construction would assign two different states to the same point. Each neighboring compression characteristic corresponds to a different amount of turning and therefore a different value of $M$, $\mu$, and the associated characteristic invariant. A single smooth flow field cannot have multiple values of the flow variables at one point, so the smooth isentropic characteristic solution is no longer valid.


##### problem 2.a.iii

The invalid smooth centered compression is replaced by a shock. For a moderate sharp compression corner, this is an attached oblique shock issuing from the corner. Across the shock the flow turns abruptly, the Mach number decreases, and the pressure, density, and temperature change discontinuously. This replacement is consistent with the limitation of the smooth characteristic method: once the solution contains a discontinuity, the differential characteristic relations are not enough, and the state change must be determined from the shock jump conditions in conservative form.


##### problem 2.b.i

For a smooth compression wall, the wall-imposed compression is still carried into the flow by the $C_{-}$family. The difference from the sharp corner is that the turning is distributed along the wall. Instead of all compression characteristics being forced from one corner point, neighboring $C_{-}$characteristics originate from different wall locations.

The $C_{+}$characteristics originate in the upstream uniform flow. They carry the upstream invariant into the compression region, while the wall-imposed $C_{-}$family changes from one wall point to the next. The figure shows $C_{-}$characteristics issuing from the smooth wall and converging downstream, while the $C_{+}$family enters from the upstream uniform region.



![[Pasted image 20260509083255.png|500]]


![[Pasted image 20260509083323.png|500]]



```mathematica title:""
Clear["Global`*"];

xMin = -2.4;
xMax = 4.3;
yMin = -0.35;
yMax = 2.35;

cMinusColor = RGBColor[0.10, 0.35, 0.75];
cPlusColor = RGBColor[0.80, 0.15, 0.12];

wallCurve =
  BezierCurve[{{-2.2, 0}, {-0.4, 0}, {1.0, 0.10}, {2.7, 0.62}}];

wall =
  {
   {Black, AbsoluteThickness[3.5], Line[{{xMin, 0}, {-2.2, 0}}]},
   {Black, AbsoluteThickness[3.5], wallCurve},
   {Black, AbsoluteThickness[3.5], Line[{{2.7, 0.62}, {xMax, 1.00}}]}
   };

wallPoints =
  {{-0.10, 0.02}, {0.45, 0.07}, {1.00, 0.17},
   {1.55, 0.32}, {2.10, 0.50}};

convergencePoint = {4.0, 2.45};

wallImposedCMinus =
  Map[
   {Dashed, cMinusColor, AbsoluteThickness[2.6],
      Line[{#, convergencePoint}]} &,
   wallPoints
   ];

upstreamCPlus =
  Table[
   {Dashed, cPlusColor, Opacity[0.55], AbsoluteThickness[2],
    BezierCurve[{{xMin, -0.35 xMin + b}, {-0.2, -0.35 (-0.2) + b},
      {1.2, -0.18 1.2 + b}, {2.9, -0.10 2.9 + b}}]},
   {b, {0.25, 0.70, 1.15, 1.60}}
   ];

Graphics[
 {
  wall,
  upstreamCPlus,
  wallImposedCMinus,
  
  Text[Style["wall-imposed C- compression family", 12], {2.35, 1.55}],
  Text[Style["C+ family from upstream uniform flow", 12], {-0.70, 1.75}],
  Text[Style["smooth wall distributes the turning", 12], {1.35, 0.18}],
  
  Inset[
   LineLegend[
    {
     Directive[Dashed, cPlusColor],
     Directive[Dashed, cMinusColor]
     },
    {Subscript[C, "+"], Subscript[C, "-"]},
    LegendLayout -> "Column"
    ],
   Scaled[{0.84, 0.78}]
   ]
  },
 Axes -> False,
 PlotRange -> {{xMin, xMax}, {yMin, yMax}},
 AspectRatio -> 0.45,
 ImageSize -> Large,
 PlotLabel -> Style["Smooth compression: distributed turning", 16, Bold]
 ]
```


##### problem 2.b.ii

A locally smooth compression can exist because the turning is distributed over a finite wall region. Each wall point imposes only a small change in flow direction, and the corresponding $C_{-}$characteristic enters the flow from a different location. The neighboring compression characteristics are therefore separated initially, so the characteristic construction can remain single-valued near the wall.

This is different from the sharp-corner case, where the entire turn is imposed at one point. At a sharp compression corner, the attempted centered compression forces neighboring compression characteristics to coalesce immediately. For a smooth wall, the same convergence tendency is present, but it is delayed because the boundary data are spread over space rather than concentrated at the corner.


##### problem 2.b.iii

The smooth compression region is not a fully general two-family marching problem, at least before characteristic intersection occurs. It still has simple-wave structure. The $C_{+}$family originates in the upstream uniform flow, where

$$
\theta=\theta_1,
\qquad
M=M_1.
$$

Therefore every incoming $C_{+}$characteristic carries the same invariant:

$$
I_{+}
=
\theta+v(M)
=
\theta_1+v(M_1).
$$

As long as the flow remains smooth, this gives the global relation

$$
\theta+v(M)=\theta_1+v(M_1).
$$

Equivalently,

$$
v(M)=v(M_1)-(\theta-\theta_1).
$$

For compression, $\theta>\theta_1$, so

$$
v(M)<v(M_1).
$$

Since $v(M)$ increases with $M$ for supersonic flow,

$$
M<M_1.
$$

The variation through the compression is supplied by the wall-imposed $C_{-}$family. Different $C_{-}$characteristics correspond to different wall turning angles, so their $I_{-}$values vary from one characteristic to the next. Thus the region is degenerate in the same sense as the expansion fan: one invariant is fixed globally by the upstream uniform flow, while the other family carries the variation imposed by the wall.


##### problem 2.b.iv

Smooth compression waves may still lead to shock formation because the compression characteristics converge. As the flow is compressed, the Mach number decreases and the Mach angle increases. For the wall-imposed $C_{-}$family,

$$
\frac{dy}{dx}=\tan(\theta+\mu),
$$

so the characteristic directions rotate in a way that makes neighboring compression characteristics move toward one another. If they intersect, the smooth characteristic construction attempts to assign more than one state to the same point. That is the same mathematical failure seen in the sharp-corner compression, but it occurs farther downstream rather than immediately at the wall.

Once that intersection occurs, the smooth isentropic solution is no longer valid. The physical flow replaces the multi-valued smooth construction with a shock or a shock-containing structure.


A smoothly compressed region and a shocked region generally do not have the same downstream thermodynamic state. The smooth compression is modeled as isentropic, so it changes the flow through continuous turning and pressure rise without entropy production. A shock, by contrast, is irreversible: entropy increases, total pressure is lost, and the downstream pressure, density, temperature, velocity, and Mach number are determined by jump conditions.

Because the two regions generally leave different entropy levels and different flow states, they cannot simply recombine into one uniform smooth flow without additional adjustment. The recombination would require further waves, shocks, or shear/contact-like structures to reconcile the differences in pressure, flow direction, velocity, and entropy.
