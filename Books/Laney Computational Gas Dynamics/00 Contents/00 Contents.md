## Contents

Preface ..... X111
Chapter 1 Introduction ..... 1
Part I: Gasdynamics Review ..... 3
Chapter 2 Governing Equations of Gasdynamics ..... 5
2.0 Introduction ..... 5
2.1 The Integral Form of the Euler Equations ..... 5
2.1.1 Conservation of Mass ..... 5
2.1.2 Conservation of Momentum ..... 6
2.1.3 Conservation of Energy ..... 7
2.1.4 Equations of State for a Perfect Gas ..... 8
2.1.5 Entropy and the Second Law of Thermodynamics ..... 10
2.1.6 Vector Notation ..... 12
2.2 The Conservation Form of the Euler Equations ..... 13
2.2.1 Vector and Vector-Matrix Notation ..... 14
2.2.2 Rankine-Hugoniot Relations ..... 15
2.3 The Primitive Variable Form of the Euler Equations ..... 15
2.3.1 Vector-Matrix Notation ..... 16
2.4 Other Forms of the Euler Equations ..... 17
Chapter 3 Waves ..... 21
3.0 Introduction ..... 21
3.1 Waves for a Scalar Model Problem ..... 22
3.2 Waves for a Vector Model Problem ..... 26
3.3 The Characteristic Form of the Euler Equations ..... 28
3.3.1 Examples ..... 33
3.3.2 Physical Interpretation ..... 36
3.4 Simple Waves ..... 37
3.5 Expansion Waves ..... 39
3.6 Compression Waves and Shock Waves ..... 42
3.7 Contact Discontinuities ..... 44
Chapter 4 Scalar Conservation Laws ..... 48
4.0 Introduction ..... 48
4.1 Integral Form ..... 49
4.2 Conservation Form ..... 49
4.3 Characteristic Form ..... 50
4.4 Expansion Waves ..... 51
4.5 Compression Waves and Shock Waves ..... 51
4.6 Contact Discontinuities ..... 52
4.7 Linear Advection Equation ..... 52
4.8 Burgers' Equation ..... 54
4.9 Nonconvex Scalar Conservation Laws ..... 58
4.10 Entropy Conditions ..... 61
4.11 Waveform Preservation, Destruction, and Creation ..... 64
Chapter 5 The Riemann Problem ..... 71
5.0 Introduction ..... 71
5.1 The Riemann Problem for the Euler Equations ..... 72
5.2 The Riemann Problem for Linear Systems of Equations ..... 75
5.3 Three-Wave Linear Approximations - Roe's Approximate Riemann Solver for the Euler Equations ..... 82
5.3.1 Secant Line and Secant Plane Approximations ..... 82
5.3.2 Roe Averages ..... 84
5.3.3 Algorithm ..... 88
5.3.4 Performance ..... 90
5.4 One-Wave Linear Approximations ..... 94
5.5 Other Approximate Riemann Solvers ..... 96
5.6 The Riemann Problem for Scalar Conservation Laws ..... 96
Part II: Computational Review ..... 103
Chapter 6 Numerical Error ..... 105
6.0 Introduction ..... 105
6.1 Norms and Inner Products ..... 105
6.2 Round-Off Error ..... 108
6.3 Discretization Error ..... 110
Chapter 7 Orthogonal Functions ..... 117
7.0 Introduction ..... 117
7.1 Functions as Vectors ..... 118
7.2 Legendre Polynomial Series ..... 120
7.3 Chebyshev Polynomial Series ..... 123
7.4 Fourier Series ..... 126
Chapter 8 Interpolation ..... 132
8.0 Introduction ..... 132
8.1 Polynomial Interpolation ..... 133
8.1.1 Lagrange Form ..... 134
8.1.2 Newton Form ..... 135
8.1.3 Taylor Series Form ..... 138
8.1.4 Accuracy of Polynomial Interpolation ..... 142
8.1.5 Summary of Polynomial Interpolation ..... 145
8.2 Trigonometric Interpolation and the Nyquist Sampling Theorem ..... 145
Chapter 9 Piecewise-Polynomial Reconstruction ..... 150
9.0 Introduction ..... 150
9.1 Piecewise Interpolation-Polynomial Reconstructions ..... 152
9.2 Averaged Interpolation-Polynomial Reconstructions ..... 158
9.3 Reconstruction via the Primitive Function ..... 161
9.4 Reconstructions with Subcell Resolution ..... 167
Chapter 10 Numerical Calculus ..... 172
10.0 Introduction ..... 172
10.1 Numerical Differentiation ..... 172
10.1.1 Linear Approximations ..... 172
10.1.2 Quadratic Approximations ..... 173
10.2 Numerical Integration ..... 175
10.2.1 Constant Approximations ..... 176
10.2.2 Linear Approximations ..... 177
10.3 Runge-Kutta Methods for Solving Ordinary Differential Equations ..... 178
Part III: Basic Principles of Computational Gasdynamics ..... 185
Chapter 11 Conservation and Other Basic Principles ..... 187
11.0 Introduction ..... 187
11.1 Conservative Finite-Volume Methods ..... 187
11.1.1 Forward-Time Methods ..... 193
11.1.2 Backward-Time Methods ..... 196
11.1.3 Central-Time Methods ..... 201
11.2 Conservative Finite-Difference Methods ..... 203
11.2.1 The Method of Lines ..... 205
11.2.2 Formal, Local, and Global Order of Accuracy ..... 206
11.3 Transformation to Conservation Form ..... 208
Chapter 12 The CFL Condition ..... 214
12.0 Introduction ..... 214
12.1 Scalar Conservation Laws ..... 215
12.2 The Euler Equations ..... 219
Chapter 13 Upwind and Adaptive Stencils ..... 222
13.0 Introduction ..... 222
13.1 Scalar Conservation Laws ..... 223
13.2 The Euler Equations ..... 228
13.3 Introduction to Flux Averaging ..... 228
13.4 Introduction to Flux Splitting ..... 231
13.4.1 Flux Split Form ..... 234
13.4.2 Introduction to Flux Reconstruction ..... 237
13.5 Introduction to Wave Speed Splitting ..... 237
13.5.1 Wave Speed Split Form ..... 239
13.6 Introduction to Reconstruction-Evolution Methods ..... 243
Chapter 14 Artificial Viscosity ..... 249
14.0 Introduction ..... 249
14.1 Physical Viscosity ..... 249
14.2 Artificial Viscosity Form ..... 250
Chapter 15 Linear Stability ..... 255
15.0 Introduction ..... 255
15.1 von Neumann Analysis ..... 257
15.2 Alternatives to von Neumann Analysis ..... 264
15.3 Modified Equations ..... 265
15.4 Convergence and Linear Stability ..... 268
Chapter 16 Nonlinear Stability ..... 272
16.0 Introduction ..... 272
16.1 Monotonicity Preservation ..... 276
16.2 Total Variation Diminishing (TVD) ..... 277
16.3 Range Diminishing ..... 282
16.4 Positivity ..... 285
16.5 Upwind Range Condition ..... 289
16.6 Total Variation Bounded (TVB) ..... 292
16.7 Essentially Nonoscillatory (ENO) ..... 293
16.8 Contraction ..... 294
16.9 Monotone Methods ..... 294
16.10 A Summary of Nonlinear Stability Conditions ..... 295
16.11 Stability and Convergence ..... 297
16.12 The Euler Equations ..... 298
16.13 Proofs ..... 299
Part V: Basic Vethods of Computational Gasolynamics ..... 307
Chapter 17 Basic Numerical Methods for Scalar Conservation Laws ..... 309
17.0 Introduction ..... 309
17.1 Lax-Friedrichs Method ..... 312
17.2 Lax-Wendroff Method ..... 316
17.3 First-Order Upwind Methods ..... 323
17.3.1 Godunov's First-Order Upwind Method ..... 325
17.3.2 Roe's First-Order Upwind Method ..... 329
17.3.3 Harten's First-Order Upwind Method ..... 332
17.4 Beam-Warming Second-Order Upwind Method ..... 336
17.5 Fromm's Method ..... 343
Chapter 18 Basic Numerical Methods for the Euler Equations ..... 351
18.0 Introduction ..... 351
18.1 Flux Approach ..... 355
18.1.1 Lax-Friedrichs Method ..... 355
18.1.2 Lax-Wendroff Methods ..... 355
18.2 Wave Approach I: Flux Vector Splitting ..... 362
18.2.1 Steger-Warming Flux Vector Splitting ..... 373
18.2.2 Van Leer Flux Vector Splitting ..... 374
18.2.3 Liou-Steffen Flux Vector Splitting ..... 378
18.2.4 Zha-Bilgen Flux Vector Splitting ..... 379
18.2.5 First-Order Upwind Methods ..... 379
18.2.6 Beam-Warming Second-Order Upwind Method ..... 381
18.3 Wave Approach II: Reconstruction-Evolution ..... 406
18.3.1 Godunov's First-Order Upwind Method ..... 410
18.3.2 Roe's First-Order Upwind Method ..... 410
18.3.3 Harten's First-Order Upwind Method ..... 417
18.3.4 First-Order Upwind Method Based on One-Wave Solver ..... 417
18.3.5 Second- and Higher-Order Accurate Methods ..... 420
Chapter 19 Boundary Treatments ..... 430
19.0 Introduction ..... 430
19.1 Stability ..... 433
19.2 Solid Boundaries ..... 434
19.3 Far-Field Boundaries ..... 441
Part V: Advanced Methods of Computational Gasdynamics ..... 455
Chapter 20 Flux Averaging I: Flux-Limited Methods ..... 459
20.0 Introduction ..... 459
20.1 Van Leer's Flux-Limited Method ..... 463
20.2 Sweby's Flux-Limited Method (TVD) ..... 466
20.2.1 The Linear Advection Equation with $a>0$ ..... 466
20.2.2 The Linear Advection Equation with $a<0$ ..... 472
20.2.3 Nonlinear Scalar Conservation Laws with $a(u)>0$ ..... 473
20.2.4 Nonlinear Scalar Conservation Laws with $a(u)<0$ ..... 474
20.2.5 Nonlinear Scalar Conservation Laws at Sonic Points ..... 475
20.2.6 The Euler Equations ..... 482
20.3 Chakravarthy-Osher Flux-Limited Methods (TVD) ..... 482
20.3.1 A Second-Order Accurate Method: A Semidiscrete Version of Sweby's Flux-Limited Method ..... 485
20.3.2 Another Second-Order Accurate Method ..... 487
20.3.3 Second- and Third-Order Accurate Methods ..... 488
20.3.4 Higher-Order Accurate Methods ..... 490
20.4 Davis-Roe Flux-Limited Method (TVD) ..... 491
20.4.1 Scalar Conservation Laws ..... 491
20.4.2 The Euler Equations ..... 494
20.5 Yee-Roe Flux-Limited Method (TVD) ..... 495
20.5.1 Scalar Conservation Laws ..... 495
20.5.2 The Euler Equations ..... 498
Chapter 21 Flux Averaging I: Flux-Corrected Methods ..... 504
21.0 Introduction ..... 504
21.1 Boris-Book Flux-Corrected Method (FCT) ..... 506
21.2 Zalesak's Flux-Corrected Methods (FCT) ..... 515
21.3 Harten's Flux-Corrected Method (TVD) ..... 517
21.3.1 Scalar Conservation Laws ..... 517
21.3.2 The Euler Equations ..... 521
21.4 Shu-Osher Methods (ENO) ..... 523
Chapter 22 Flux Averaging II: Self-Adjusting Hybrid Methods ..... 541
22.0 Introduction ..... 541
22.1 Harten-Zwas Self-Adjusting Hybrid Method ..... 542
22.2 Harten's Self-Adjusting Hybrid Method ..... 544
22.3 Jameson's Self-Adjusting Hybrid Method ..... 550
22.3.1 Scalar Conservation Laws ..... 550
22.3.2 The Euler Equations ..... 558
Chapter 23 Solution Averaging: Reconstruction-Evolution Methods ..... 565
23.0 Introduction ..... 565
23.1 Van Leer's Reconstruction-Evolution Method (MUSCL) ..... 565
23.1.1 Linear Advection Equation ..... 565
23.1.2 The Lagrange Equations ..... 572
23.2 Colella-Woodward Reconstruction-Evolution Method (PPM) ..... 574
23.3 Anderson-Thomas-Van Leer Reconstruction-Evolution Methods ..... 577
(TVD/MUSCL): Finite-Volume Versions of the Chakravarthy-Osher Flux-Corrected Methods ..... 577
23.3.1 A Second-Order Accurate Method ..... 578
23.3.2 Second- and Third-Order Accurate Methods ..... 579
23.4 Harten-Osher Reconstruction-Evolution Method (UNO) ..... 582
23.4.1 The Linear Advection Equation ..... 582
23.4.2 Nonlinear Scalar Conservation Laws ..... 583
23.4.3 The Euler Equations ..... 585
23.5 Harten-Engquist-Osher-Chakravarthy Reconstruction-Evolution Methods (ENO) ..... 585
23.5.1 Second-Order Accurate Temporal Evolution for Scalar Conservation Laws ..... 587
23.5.2 Third-Order Accurate Temporal Evolution for Scalar Conservation Laws ..... 589
23.5.3 Second-Order Accurate Temporal Evolution for the Euler Equations ..... 591
Chapter 24 A Brief Introduction to Multidimensions ..... 597
24.0 Introduction ..... 597
24.1 Governing Equations ..... 597
24.2 Waves ..... 599
24.3 Conservation and Other Numerical Principles ..... 602
Index ..... 605

