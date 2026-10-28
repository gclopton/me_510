# Equation Index Instructions

This document describes two related tasks for processing textbook chapters:

1. **Tagging principal equations** in the chapter source file with equation callouts
2. **Creating the Equation Index** — a comprehensive reference document for the chapter

Both tasks are described below with formatting rules, examples, and guidance on what constitutes good content.

---

## Part 1: Tagging Principal Equations in the Chapter Source

### Purpose

Go through the chapter's Markdown source file and enclose every principal equation in an Obsidian equation callout. A "principal equation" is one that could reasonably appear in end-of-chapter problems, be referenced in later chapters, or serve as a major result that a student would need to know. Intermediate algebraic steps are *not* tagged unless the intermediate result is itself important (e.g., the Prandtl relation is an intermediate result in deriving the normal shock $M_2$ expression, but it is important enough to tag).

### What qualifies as a principal equation

- Final closed-form results (e.g., the normal shock pressure ratio)
- Governing equations and conservation laws (e.g., continuity, momentum, energy)
- Definitions of important quantities (e.g., total temperature, Mach number)
- Key thermodynamic relations (e.g., isentropic relations, entropy change)
- Important intermediate results that have standalone physical significance (e.g., the Prandtl relation)
- Relations that are tabulated in the appendix (if the textbook tabulates it, it's important)

### What does NOT qualify

- Algebraic manipulation steps that are only used once on the way to a final result
- Numbered equations that are simply rearrangements of the line above
- Equations that restate a result from a previous chapter without modification (unless the chapter re-derives it in a new context)

### Callout format

The equation callout uses Obsidian's `> [!equation]` syntax. The format is:

```markdown
> [!equation] Descriptive title (Eq. X.XX)
> $$
> LaTeX equation here
> $$
```

Rules:

- The title line goes on the same line as `[!equation]`, after a space.
- The title should be a concise, descriptive name followed by the equation number in parentheses.
- The `$$` delimiters and the equation body are all inside the callout (every line starts with `> `).
- There is one blank line after the closing `> $$` before the next paragraph of body text.
- If two closely related equations appear together (e.g., the pressure and density total-to-static ratios), they may share a single callout or have separate callouts — use judgment based on whether they are typically used independently.

### Example

Before (raw chapter text with an important result):

```markdown
Hence, combining Eqs. (3.48) and (3.50), we get

$$
M_{2}^{2}=\frac{1+[(\gamma-1) / 2] M_{1}^{2}}{\gamma M_{1}^{2}-(\gamma-1) / 2}
$$

Equation (3.51) gives the downstream Mach number...
```

After (with equation callout added):

```markdown
Hence, combining Eqs. (3.48) and (3.50), we get

> [!equation] Mach number behind a normal shock (Eq. 3.51)
> $$
> M_{2}^{2}=\frac{1+[(\gamma-1) / 2] M_{1}^{2}}{\gamma M_{1}^{2}-(\gamma-1) / 2}
> $$

Equation (3.51) gives the downstream Mach number...
```

Note that the original `$$...$$` block is replaced by the callout — do not leave a duplicate.

---

## Part 2: Creating the Equation Index

### Purpose

The Equation Index is a standalone reference document that catalogs every important equation, assumption, and building-block expression from a chapter. It is organized so that a student can quickly look up any result, understand what it means physically, see what each symbol represents, and know what assumptions are required.

### File location and naming

Place the file in the chapter's folder:

```
Books/Anderson/<Chapter Folder>/Equation Index.md
```

### Overall structure

The file has two major parts:

1. **Master Reference** — a set of tables at the top that list every entry by category, with entry numbers and equation numbers
2. **Entry sections** — the detailed entries themselves, organized under H1 section headers

The hierarchy is:

- `# Equation Index — Anderson, Chapter N` (document title)
- `## Master Reference` with `### Category Name (N–M)` sub-tables
- `# Section Name` (H1 headers dividing the entries into groups)
- `## N. Entry Title` (H2 headers for each individual entry)

### Master Reference format

The Master Reference contains one table per category. Each table lists the entry number, name, and equation number (or `—` if no equation number).

```markdown
## Master Reference

### Building Blocks (1–20)

| #   | Name                                    | Eq. #    |
| --- | --------------------------------------- | -------- |
| 1   | Speed of sound — general expression     | Eq. 3.17 |
| 2   | Speed of sound for a perfect gas        | Eq. 3.20 |
| ...                                                     |

### Assumptions & Simplifications (21–35)

| #  | Name                          |
| -- | ----------------------------- |
| 21 | Calorically Perfect Gas       |
| 22 | One-Dimensional Flow          |
| ...                              |
```

Assumptions tables omit the Eq. # column since assumptions don't have equation numbers.

### Entry categories

Organize entries into logical groups that reflect the chapter's structure. Typical categories include:

- **Building Blocks** — recurring terms, factors, definitions, and reference quantities that appear inside many of the main results (e.g., speed of sound, Mach number, total conditions, mass flux, impulse function, equation of state, isentropic relations)
- **Assumptions & Simplifications** — the physical assumptions and idealizations that underlie the chapter's results (e.g., calorically perfect gas, steady flow, inviscid, adiabatic, 1-D, constant area)
- **Main equation groups** — organized to mirror the chapter's logical sections (e.g., "Conservation Equations," "Normal Shock Relations," "Rayleigh-Line Flow," "Fanno-Line Flow")

The exact categories and numbering depend on the chapter content. Number entries consecutively across all categories (1, 2, 3, ...).

### Entry format — Equations

Each equation entry has the following components in order:

```markdown
## N. Entry Title (Eq. X.XX)

> [!question]
>
> (a) First study question
> (b) Second study question
> (c) Third study question

> [!equation] Entry Title (Eq. X.XX)
>
> $$ LaTeX equation $$

Description paragraph.

|**Expression**|**Units**|**Base Units**|**Name**|**Description**|
|---|---|---|---|---|
|$symbol$|units|base units|**Name**|Description of this symbol or sub-expression.|
```

#### The question callout

The `> [!question]` callout contains 2–4 study questions that test understanding of the equation. These should:

- Ask the student to recall or write the equation from memory
- Probe the physical meaning (not derivation steps)
- Ask about limiting cases, special values, or physical consequences
- Ask how the equation connects to other results

#### The equation callout

The `> [!equation]` callout contains the equation itself. The title should match the entry title. Use `$$` for display math (on the same line as the equation for single-line equations, or on separate lines for multi-line equations).

Single-line:

```markdown
> [!equation] Entry Title (Eq. X.XX)
>
> $$ \frac{T_o}{T} = 1 + \frac{\gamma - 1}{2}M^2 $$
```

Multi-line (use `\begin{aligned}` for systems of equations):

```markdown
> [!equation] Rayleigh-line flow relations (Eqs. 3.85–3.89)
>
> $$ \begin{aligned}
> \frac{p}{p^{*}} & = \frac{1+\gamma}{1+\gamma M^{2}} \\[6pt]
> \frac{T}{T^{*}} & = M^{2}\left(\frac{1+\gamma}{1+\gamma M^{2}}\right)^{2}
> \end{aligned} $$
```

#### The description paragraph — THIS IS CRITICAL

The description paragraph is the most important part of each entry. It must convey the **physical meaning** of the equation — what it tells you about the physics, what intuition it provides, what trade-offs or constraints it reveals.

**The description is NOT:**

- A derivation ("Setting $q = 0$ in Eq. 3.9 gives...")
- A restatement of where it comes from ("This is derived from the integral momentum equation...")
- A reading of the symbols ("This equation says $T_o/T$ equals one plus...")
- A description of algebraic steps ("Using $c_p = \gamma R/(\gamma-1)$ and substituting...")

**The description IS:**

- An interpretation of what the equation means physically
- An explanation of the intuition behind it — what trade-offs, constraints, or behaviors it captures
- A discussion of what each major term or factor represents in physical terms
- An explanation of limiting cases or surprising behaviors if they illuminate the physics

**Example of a BAD description:**

> Setting $q = 0$ in Eq. 3.9 gives this adiabatic form: the total enthalpy is constant from station to station. This equation applies to normal shocks and to Fanno-line flow. Although derived here for one-dimensional flow, this is actually a general result.

**Example of a GOOD description:**

> This equation asserts that in a steady, adiabatic flow where no mechanical work is performed, the total energy of the fluid — comprising its thermal content and flow work (enthalpy) plus its motion (kinetic energy) — is a conserved quantity. It describes a fundamental trade-off: a fluid element can be "fast and cold" or "slow and hot," but it cannot gain speed without sacrificing thermal energy, nor can it warm up without slowing down, so long as no heat is added or removed. This energy conservation holds across normal shocks, through Fanno-line friction flows, and indeed along any streamline in any steady adiabatic flow regardless of dimensionality. It is the foundation upon which all stagnation properties, nozzle flows, and shock analyses are built.

The good description tells you *what the equation means*, gives you *intuition* about the physics, and explains *why* things behave the way they do. After reading it, you should have a gut-level understanding of the equation, not just a procedural knowledge of where it came from.

#### The expression table

The table breaks down the important symbols, sub-expressions, or terms that appear in the equation. Columns:

| Column | Content |
|---|---|
| **Expression** | The symbol or sub-expression in LaTeX (e.g., `$T_o$`, `$\rho u^2$`, `$\frac{\gamma-1}{2}M^2$`) |
| **Units** | SI units in readable form (e.g., `Pa`, `J/kg`, `m/s`, `—` for dimensionless) |
| **Base Units** | SI base units (e.g., `kg·m⁻¹·s⁻²`, `m²·s⁻²`, `—`) |
| **Name** | Bold name (e.g., `**Static Pressure**`, `**Mach Number**`) |
| **Description** | A concise description of what this quantity represents physically |

Include the most important 2–5 expressions. You do not need to list every symbol — focus on the ones that a student would need to identify or that carry physical meaning beyond their symbol.

### Entry format — Assumptions

Assumption entries have a different structure:

```markdown
## N. Assumption Name

> [!question]
>
> (a) Study question about the assumption
> (b) What terms vanish or simplify?
> (c) When does this assumption break down?

> [!assumption] Assumption Name
>
> Concise statement of the assumption.

**Definition.** Extended explanation of what the assumption means.

**When it is acceptable.** Description of the physical conditions under which this assumption is valid, with specific examples and quantitative guidelines where possible.

**How to recognize when you can apply it.** Practical guidance: what phrases in a problem statement signal this assumption, what to look for, what disqualifies it.
```

### Optional subsections within entries

Some entries benefit from additional subsections. These are H3 headers (since entries are H2):

#### Assumptions and Simplifications (within an equation entry)

If an equation requires specific assumptions beyond what the standalone assumption entries cover, list them:

```markdown
### Assumptions and Simplifications

1. **Steady flow.** The time-derivative (storage) term vanishes.
2. **Inviscid flow.** No viscous shear stress terms.
3. **One-dimensional, constant area.** Properties uniform across each face.
```

#### Simplifications (important special cases)

If an equation has important simplified forms or limiting cases worth highlighting:

```markdown
### Simplifications

| Limit | Value | Physical meaning |
|---|---|---|
| $M_1 = 1$ | $M_2 = 1$ | Infinitely weak shock (Mach wave). |
| $M_1 \to \infty$ | $M_2 \to 0.378$ | Strongest possible shock for air. |
```

Or for reduced/simplified forms of the equation under additional assumptions.

These subsections should only be included where they add genuine value — not for every entry.

### Practical workflow

1. **Read the entire chapter** carefully, identifying every boxed/highlighted equation, every important result, and every assumption used in the derivations.
2. **Catalog the building blocks** — the recurring factors, definitions, and reference quantities that appear throughout the main results.
3. **Catalog the assumptions** — every physical assumption used in the chapter, with enough detail that a student can determine when each one applies.
4. **Organize the main results** into logical groups matching the chapter structure.
5. **Number everything consecutively** across all categories.
6. **Write the Master Reference tables** at the top.
7. **Write each entry**, paying special attention to the description paragraphs — these should convey physical understanding, not derivation history.
8. **Cross-reference** between entries where appropriate (e.g., "See Entry 26 for the adiabatic assumption").

### Quality checklist

Before considering the Equation Index complete, verify:

- [ ] Every principal equation from the chapter is included
- [ ] Every assumption used in the chapter has its own entry
- [ ] Building blocks cover the recurring terms and factors
- [ ] The Master Reference tables accurately list all entries
- [ ] Entry numbering is consecutive with no gaps
- [ ] Every description paragraph focuses on physical meaning, not derivation
- [ ] Expression tables have correct units and base units
- [ ] Study questions probe understanding, not memorization of derivation steps
- [ ] Section headers (H1) match the categories in the Master Reference
- [ ] All entries are H2 headers under their section's H1 header
