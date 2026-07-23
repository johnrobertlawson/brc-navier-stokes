# The exact Clay target

## Governing system

For velocity \(u:\mathbb R^3\times[0,\infty)\to\mathbb R^3\), pressure \(p\), viscosity
\(\nu>0\), and force \(f\),

\[
\partial_t u +(u\cdot\nabla)u=\nu\Delta u-\nabla p+f,
\qquad \nabla\cdot u=0,
\qquad u(\cdot,0)=u_0.
\]

Charles Fefferman's [official problem description][official] asks for a proof of **one**
of four statements. The paraphrases below are routing aids; the official text controls.

## The four terminal alternatives

| ID | Domain | Force | Required conclusion |
|---|---|---|---|
| A | \(\mathbb R^3\) | \(f=0\) | Every smooth, divergence-free, rapidly decaying \(u_0\) has a global smooth physically reasonable solution. |
| B | \(\mathbb T^3=\mathbb R^3/\mathbb Z^3\) | \(f=0\) | Every smooth periodic divergence-free \(u_0\) has a global smooth periodic solution. |
| C | \(\mathbb R^3\) | Smooth, rapidly decaying \(f\) allowed | Exhibit admissible smooth \(u_0,f\) for which no global smooth physically reasonable solution exists. |
| D | \(\mathbb T^3\) | Smooth spatially periodic \(f\), rapidly decaying in time | Exhibit admissible smooth periodic \(u_0,f\) for which no global smooth periodic solution exists. |

Here “rapidly decaying” is quantitative. In the whole-space alternatives, every spatial
derivative of \(u_0\) decays faster than any power, and every space-time derivative of
\(f\) decays faster than any power of \(1+|x|+t\). In the periodic forced alternative,
every derivative of \(f\) decays faster than any power of \(1+t\). These are the
official conditions (4), (5), (8), and (9), not optional modelling preferences.

For A and B the initial data may be arbitrarily large. Small-data or short-time results
are not enough. For C and D, nonuniqueness of rough weak solutions is not by itself the
required breakdown: the construction must meet the official smoothness, domain, force,
and solution requirements.

## Solution classes must not be conflated

| Class | Rough meaning | Why it matters here |
|---|---|---|
| Classical/smooth | All derivatives needed by the equation exist pointwise. | This is the prize-level regularity target. |
| Strong/mild | Enough critical-space regularity for local well-posedness and smoothing. | Such a solution is unique while it exists in the strong class. |
| Leray–Hopf weak | Distributional solution with global energy control. | Global existence is known; global smoothness and general uniqueness are separate questions. |
| Suitable weak | A weak solution satisfying a local energy inequality. | Partial-regularity theory applies, but a tiny singular set is not the same as no singular set. |

## A claim-to-prize checklist

Before calling any result a solution, answer all of these explicitly:

1. Which alternative—A, B, C, or D—does it prove?
2. Is the domain exact?
3. Are the initial data smooth, divergence-free, and decaying/periodic as required?
4. Is the force exactly zero where required, or smooth and admissible where allowed?
5. Is the conclusion global classical smoothness or its genuine impossibility?
6. Are all constants uniform up to the alleged terminal time?
7. Is every computer-assisted step accompanied by a checkable certificate?

Even a correct proof has a separate recognition path. Clay does not accept direct
submissions; its [rules][rules] require a qualifying publication, at least two years, and
general acceptance by the global mathematics community.

[official]: https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf
[rules]: https://www.claymath.org/millennium-problems/rules/
