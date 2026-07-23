# Research records

These JSON ledgers are the stable interface between prose, proof obligations, and code.

## Record types

- **Source:** exact bibliographic object, version, review status, and last verification.
- **Claim:** one proposition with quantifiers, assumptions, conclusion, provenance, and
  epistemic status.
- **Route:** one branch of the regularity/breakdown possibility tree with a success and
  kill criterion.
- **Experiment:** a falsifiable test with invariants, artifacts, and certificate policy.
- **Obligation:** one independently closable arrow in a paper's proof.

The public type definitions are in
[research-ledgers.schema.json](../../lab/schemas/research-ledgers.schema.json). The
dependency-free validator is **lab/navier_lab/records.py**.

## Status semantics

### Claims

- **established:** supported by a primary peer-reviewed theorem.
- **conditional_preprint:** a conditional theorem stated in a preprint; the record's
  audit field says whether independent checking is pending or complete.
- **preprint_claim:** a preprint's reported result, not yet independently reproduced here.
- **official_status:** time-sensitive status from an official authority.
- **definition:** controlling formulation or convention.
- **open:** an explicit unsolved proposition.

### Obligations

- **open:** no matching proof or counterexample recorded.
- **partially_mechanized:** some algebra is checked, but analytic content remains.
- **verified:** independently checked with matching hypotheses.
- **repaired:** the original step needed a documented correction that now closes.
- **unsupported:** a counterexample or unrepairable gap defeats the stated step.

No status is upgraded by prose alone. Add evidence and rerun **make check**.
