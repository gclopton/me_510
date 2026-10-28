# values of the universal gas constant $\bar{R}$ 

$$
\begin{array}{ll}
\bar{R}=8.3143 & \mathrm{~J} / \mathrm{mol}-\mathrm{K} \\
\bar{R}=8314.3 & \mathrm{~J} / \mathrm{kmol}-\mathrm{K} \\
\bar{R}=1545.3 & \mathrm{ft}-\mathrm{lbf} / \mathrm{lbmol}-\mathrm{R} \\
\bar{R}=1.9859 & \mathrm{Btu} / \mathrm{lbmol}-\mathrm{R} \\
\bar{R}=1.9859 & \mathrm{kilocal} / \mathrm{kmol}-\mathrm{K} \\
\bar{R}=0.082056 & \mathrm{~m}^{3}-\mathrm{atm} / \mathrm{kmol}-\mathrm{K}
\end{array}
$$

Dyinamics

## board of advisors, engineering

A. H-S. Ang
Civil Engineering-Systems and Probability
University of Illinois
Donald S. Berry
Northwestern University
Transportation Engineering
James Gere
Stanford University
J. Stuart Hunter
Princeton University
T. William Lambe
R. V. Whitman
Massachusetts Institute of
Technology
Perry L. McCarty
Environmental Engineering
Standford University
Don Phillips
Texas A \& M University
Dale Rudd
University of Wisconsin
Robert Steidel
University of California
Industrial Engineering
Chemical Engineering
Berkeley
R. N. White
Civil Engineering-Structures

# Dighamics <br> Maurice J. Zucrow Joe D. Hoffman 

## School of Mechanical Engineering Purdve University

Copyright © 1976, by John Wiley \& Sons, Inc.
All rights reserved. Published simultaneously in Canada.
No part of this book may be reproduced by any means, nor transmitted, nor translated into a machine language without the written permission of the publisher.

## Library of Congress Cataloging in Publication Data:

Zucrow, Maurice Joseph, 1899-1975.
Gas dynamics.
Includes bibliographical references and index.

1. Gas dynamics. I. Hoffman, Joe D., 1934joint author. II. Title.
QC168.Z8 1976 533′. 2 76-6855
ISBN 0-471-98440-X (v. 1)
Printed in the United States of America

$$
\begin{array}{llllllllll}
10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1
\end{array}
$$

## preface

This book is an introduction to the science of gas dynamics, designed for a first course at the senior or graduate level. It is also written for the practicing engineer and scientist.

The presentation of the subject matter is sufficiently clear so that the student can understand the material without the assistance of an instructor. Therefore, a review of fundamental principles is included, the derivations of equations are presented in detail, and many illustrative examples are worked out completely. Exercise problems are presented at the end of each chapter. Tables of the functions required for solving the illustrative examples and the exercise problems are included in the appendixes.

A background in fluid mechanics and thermodynamics is desirable for the study of gas dynamics. Introductory undergraduate courses in those disciplines are sufficient.

The material in this book is too lengthy to cover completely in a one-semester course; at Purdue University, we discuss in detail the basic concepts presented in each chapter, and the application of those concepts to the flow of a perfect gas. As time permits, real gas effects are discussed, and applications such as nozzles, diffusers, and the like, are presented.

The book is completely self-contained, beginning with a review of fundamental principles (Chapter 1), followed by a detailed derivation of the governing equations of fluid flow (Chapter 2), and an extensive treatment of the classical topics of steady one-dimensional gas dynamics (Chapter 3 to 9). The general features of the steady multidimensional adiabatic flow of an inviscid fluid are discussed (Chapter 10). An introduction to the concept of linearized flow (Chapter 11), the method of characteristics and steady two-dimensional supersonic flow (Chapter 12), and unsteady one-dimensional flow (Chapter 13) are presented. An appendix gives a brief introduction to the concepts of numerical analysis that are employed in the book. Extensive tables are included to aid in working problems.

The material in this book closely resembles that in the several books already written about gas dynamics, for example, Zucrow's Aircraft and Missile Propulsion, Volume 1, Thermodynamics of Fluid Flow and Application to Propulsion Engines, and Shapiro's Dynamics and Thermodynamics of Compressible Fluid Flow. The major difference between this book and the existing books is the emphasis on the application of numerical methods for solving real gas dynamic problems.

We believe that the student learns by doing. Consequently, numerous illustrative examples, worked out in complete detail, are presented in each chapter to illustrate the application of the theoretical analysis to real problems.

Because of the inevitable conversion to the international system of units (i.e., the SI system), the illustrative examples and exercise problems employ that system of units.

The tables that are included to aid in working problems include tabulations of the conventional gas dynamic flow functions, the physical properties of the standard atmosphere, and the thermodynamic properties of air. Computer programs are presented for the generation of each of the tables, so the user can construct additional tables if he desires.

The concepts of numerical analysis are introduced briefly. The material includes all of the numerical methods employed in the book: approximation and interpolation, the solution of systems of linear algebraic equations, the solution of nonlinear functions, integration, and the solution of ordinary differential equations. Numerical examples are presented to illustrate these methods.

Volume 1 of this book is based on a combination of Maurice Zucrow's book Aircraft and Missile Propulsion, Volume I, Thermodynamics of Fluid Flow and Application to Propulsion Engines and class notes employed in a gas dynamics course taught at Purdue University over the past 12 years by Joe Hoffman. Many of the figures and several of the illustrative examples in this book are taken from Zucrow's book. The comments of the students at Purdue University who have used Zucrow's book and the class notes were most helpful in the preparation of this book. Two colleagues at Purdue University deserve special acknowledgments for their generous assistance. Professor H. Doyle Thompson contributed ideas, comments, and criticisms during the writing of the book. Professor Peter Liley provided invaluable assistance in obtaining thermodynamic property data. Their generous assistance is greatly appreciated. The excellent work performed by our typist, Miss Cynthia Hoffman, deserves special note.

This book was the joint effort of a teacher and one of his students. For Professor Zucrow, it was a labor of love for his profession, performed after his retirement from Purdue University. For Joe Hoffman, it was an opportunity to work with his teacher, counselor, and friend, Doc Zucrow, in a warm personal relationship that only a few people ever achieve. Doc Zucrow passed away during the final review of the manuscript. He will be missed by his colleagues, students, and friends. This book, on which he worked diligently even on the last day of his life, is a fitting final contribution to his illustrious career.

Joe D. Hoffman
West Lafayette, Indiana, 1976

## contents

1 Review of Fundamental Principles ..... 1
2 Governing Equations for Compressible Fluid Flow ..... 70
3 General Features of the Steady One-Dimensional Flow of a Compressible Fluid ..... 102
4 Steady One-Dimensional Isentropic Flow with Area Change ..... 160
5 Steady One-Dimensional Flow with Friction ..... 243
6 Steady One-Dimensional Flow with Heat Transfer ..... 299
7 Shock Wave ..... 327
8 Expansion Waves ..... 422
9 Mass Addition, Combustion Waves, and Generalized Steady One- Dimensional Flow ..... 461
10 General Features of the Steady Multidimensional Adiabatic Flow of an Inviscid Compressible Fluid ..... 511
11 Introduction to Flow with Small Perturbations ..... 555
12 Introduction to the Method of Characteristics with Application to Steady Two-Dimensional Irrotational Supersonic Flow ..... 580
13 The Method of Characteristics Applied to Unsteady One-Dimensional Homentropic Flow ..... 622
Appendix A
Numerical Analysis ..... 669
Appendix B
The Method of Characteristics in Two Independent Variables ..... 695
Appendix C
Tables ..... 698
Index ..... 761

Dyinamics

