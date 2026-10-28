# Closed Integral Render Test

This note tests renderer-level macros for closed surface integrals in Obsidian's MathJax renderer.

Macro inline test: $\oiint_S$

Display test:

$$
\oiint_S
$$

Example in a flux expression:

$$
\oiint_S \rho \mathbf{V}\cdot d\mathbf{S}=0
$$

Closed triple-integral test:

$$
\oiiint_V \rho \, d\mathscr{V}
$$

If this renders correctly after reloading Obsidian, we can restore the closed-surface notation in the main equation index using `\oiint` and `\oiiint` directly.
