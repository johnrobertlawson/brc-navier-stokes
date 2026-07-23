# Possibility tree

The tree is a falsifiable partition of current routes, not a claim that mathematics has
already supplied a finite exhaustive taxonomy. Any uncovered scenario creates a new
node. The machine-readable version is [`records/routes.json`](records/routes.json).

```text
CLAY
├── R  Prove global regularity
│   ├── R1  Derive a universal critical bound
│   │   ├── R1a  velocity endpoint control
│   │   ├── R1b  vorticity-direction depletion
│   │   ├── R1c  frequency-flux/cascade barrier
│   │   └── R1d  analyticity versus geometric sparseness
│   ├── R2  Minimal-blow-up reduction
│   │   ├── R2a  concentration compactness
│   │   ├── R2b  ancient-solution classification
│   │   └── R2c  backward uniqueness / Liouville rigidity
│   └── R3  Remove assumptions from conditional criteria
│       ├── R3a  point core → arbitrary/multiple cores
│       ├── R3b  imposed direction control → equation-derived control
│       └── R3c  fixed critical profile → general Type-II dynamics
└── B  Prove breakdown
    ├── B1  Unforced smooth-data singularity
    │   ├── B1a  backward self-similar or discretely self-similar
    │   ├── B1b  non-self-similar physical-space concentration
    │   └── B1c  frequency cascade implementing the true nonlinearity
    ├── B2  Smooth-forced Clay construction
    │   ├── B2a  whole-space rapidly decaying force
    │   └── B2b  periodic smooth force
    └── B3  Bridge rough/singular-data mechanisms to Clay data
        ├── B3a  unstable forward self-similar profiles
        ├── B3b  positive-time matching from a smooth prehistory
        └── B3c  certified instability plus exact continuation failure
```

## Classification axes

Every candidate singularity or exclusion theorem must state its cell on each axis.

| Axis | Values initially tracked |
|---|---|
| Domain | \(\mathbb R^3\), \(\mathbb T^3\) |
| Force | zero, smooth allowed force |
| Time rate | Type-I, Type-II, unknown |
| Similarity | continuous, discrete, asymptotic, none |
| Geometry | point, curve/tube, sheet, multi-core, diffuse |
| Scale behavior | single scale, cascade, scale oscillation |
| Location | physical space, frequency space, coupled |
| Symmetry | general, axisymmetric with/without swirl, other |
| Solution class | classical, mild/strong, suitable, Leray–Hopf, weaker |

## Closure rule for a node

A route node closes only by one of these records:

1. **Exclusion theorem:** exact assumptions cover the node and imply regularity.
2. **Reduction theorem:** every object in the node maps into already closed children.
3. **Construction:** an exact example satisfies the node and its terminal Clay
   quantifiers.
4. **Logical redundancy:** the node is proven equivalent to or contained in another
   tracked node.

Numerical absence, physical implausibility, and failure to find an example do not close a
node.

## The three highest-leverage bridges

### Universal logarithmic depletion

Show that the true viscous dynamics force *some* vanishing control of stretching on every
shrinking high-vorticity region. This would turn geometric conditional criteria into a
global argument. The 2607.08866 audit probes one proposed version.

### Minimal-object rigidity

Assume failure, rescale around the most economical concentration, extract a compact
ancient solution, then show energy, pressure, and unique continuation force it to vanish.
The hard step is gaining enough compactness at a supercritical energy level.

The current ROUTE-R3B distance normalization gives a conditional
two-singularity suitable weak-\(L^3\) ancient profile. Local terminal
singular-set finiteness excludes exact continuous and discrete
self-similarity, so the surviving cell is B1b with genuinely
scale-aperiodic physical-space concentration. The subsequent countable
packing theorem permits only finitely many distinct positive limiting
satellite radii in one distance profile and forces every radially ordered
infinite tower to have adjacent-distance ratio liminf zero. The surviving
cell therefore consists of finite or radially collapsed clusters separated
by arbitrarily severe gaps. The next closure test is an inter-satellite
normalization versus packet-to-separation no-neck.

### Singular-to-smooth construction bridge

Certified forward self-similar solutions from singular data provide exact unstable
objects. A breakdown proof would need to connect one to a smooth earlier state—or use an
admissible smooth force—without smuggling the singularity into the initial data or force.

## Adversarial coverage test

For every proposed “complete” argument, construct a survivor table asking whether it
covers:

- multiple concentration centers moving in time;
- anisotropic tubes or sheets rather than balls;
- Type-II rates and oscillatory rescaling;
- energy arriving from far field or distant frequencies;
- vorticity-direction defects at zeros;
- loss of compactness through translation, dilation, or frequency drift;
- the exact endpoint rather than every nearby exponent.

Any “unknown” answer remains an open branch.
