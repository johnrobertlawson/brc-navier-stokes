# Proof lab

The lab performs small, auditable jobs. It is not an automatic theorem prover and does
not convert passing unit tests into mathematical truth.

## Current instruments

| Module | What it checks | What it does not check |
|---|---|---|
| **scaling.py** | Exact rational scaling exponents | Existence or regularity estimates |
| **log_chain.py** | Distribution/rearrangement exponent bookkeeping used in the 2607 audit | O'Neil's theorem or its hypotheses |
| **multicore.py** | Exact two-core weak-L(3/2) tail and covering geometry | PDE consistency of the scalar example |
| **anisotropic.py** | Exact one-core anisotropic weak-L(3/2) tail and covering loss | PDE consistency of the scalar example |
| **covering_entropy.py** | Exact weak-L(3/2) cover aggregation and energy-tail exponents | A PDE bound on the cover entropy |
| **perimeter_packing.py** | Exact scaling of divergence-free packets at the entropy threshold | Realisation by one Navier-Stokes evolution |
| **strain.py** | Exact finite-dimensional checks of the Biot-Savart strain contraction | The singular-integral derivation or commutator bounds |
| **records.py** | Schemas, identifiers, dependencies, and cross-record references | Whether a cited theorem is correctly understood |
| **links.py** | Local Markdown targets | External URL availability |
| **math_markup.py** | Balanced, unnested Markdown/LaTeX math delimiters | Whether the mathematics inside them is correct |
| **intervals.py** | Basic outward-rounded decimal interval arithmetic | A spectral or PDE certificate by itself |
| **source_cache.py** | Versioned arXiv fetch, SHA-256, safe extraction | Redistribution permission or proof correctness |
| **paper_build.py** | Repeated TeX compilation, unresolved-reference check, and PDF manifest | Mathematical correctness of the compiled argument |

## Commands

From the repository root:

    make check
    make scaling
    make log-chain
    make multicore
    make anisotropic
    make covering-entropy
    make perimeter-packing
    make strain
    make fetch-2607
    make compile-2607

**make fetch-2607** writes only beneath **lab/cache/**, which is ignored. Its manifest
pins the retrieval URL, UTC time, byte count, SHA-256 digest, and extracted members.
Exact source is cached locally for audit; it is not committed without an affirmative
license check.

## Certificate discipline

A future certified numerical result must separate:

1. candidate-generation code;
2. a deterministic certificate file containing only finite data;
3. a small independent verifier;
4. the analytic theorem explaining why a valid certificate implies the claim.

The candidate generator is allowed to be complicated. The verifier should be small
enough to audit independently and must use directed rounding or exact arithmetic.

## Adding an experiment

Add a record to **dossier/records/experiments.json** before implementation. State the
hypothesis, invariants, success criterion, and what failure would mean. An implemented
experiment must name artifacts that exist, and **make check** enforces those references.
