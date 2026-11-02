# Assay and Data Handoff

## First assay

The first assay is physical taste-patch contact followed by a possible feeding-related proboscis response. Approach behavior is out of scope for this MVP. The working hypothesis is that a documented gustatory input, passed through a source-backed selected circuit, can produce a predicted proboscis motor output. The hypothesis remains provisional until the sensory-to-motor path and the reference methods are reviewed.

## Reference candidate

The project plan names Shiu et al. (2024), *Nature*, DOI [10.1038/s41586-024-07763-9](https://doi.org/10.1038/s41586-024-07763-9), as a connectome-based LIF model that studied feeding and grooming. The plan also points to the [reference model repository](https://github.com/philshiu/Drosophila_brain_model). The exact assay, methods, stimulation protocol, output definition, and comparison measure still need review in Phase 1; this record does not claim that NeuroFly has reproduced the study.

## Candidate dataset and stop condition

- Candidate: FlyWire FAFB v783, female adult brain snapshot.
- Status: proposed candidate; exact compatibility with the reference model's earlier FlyWire snapshot is unresolved.
- Identifier namespace and cell crosswalk: not yet confirmed.
- Rule: do not bulk-download, extract, bundle, or name neurons in the interface until Phase 1 verifies the official release, source terms, stable IDs, and any required crosswalk.
- Do not mix FAFB, BANC, or MCNS identifiers without an explicit documented mapping.

The Phase 0 guide reconciles the project plan's early release decision with the implementation planner's separate circuit-evidence phase: Phase 0 records the named reference and candidate release, while Phase 1 owns snapshot compatibility and cell mapping. This is the active handoff rule.

## Phase 1 work required before extraction

1. Review the reference paper and supplementary methods; record the assay, stimulus, modeled circuit, and outcome actually used.
2. Verify the official dataset release, identifier namespace, access terms, citation, and source files.
3. Map candidate sensory, intermediate, and proboscis motor IDs across releases where needed; preserve evidence and uncertainty for every label and edge.
4. Decide whether to reproduce the reference model or narrow the claim to a compatible, source-backed path.
5. Record the exact stimulus-to-sensory mapping, starting pose, contact definition, trial length, reset state, and intervention target before implementation.

## Measures and comparison candidates

Candidate primary measures are response probability, response latency, and extension amplitude or state. Final definitions and thresholds must wait for reference-method review. Candidate controls include no-contact, no-sensory, always-respond, a simple rule, and a shuffled or matched graph where appropriate. The proposed intervention is virtual silencing of a Phase 1-supported node; no cell is selected in Phase 0.

## Ownership

- Owner: NeuroFly project owner; individual name to be recorded.
- Review date: before Phase 1 signoff; 2026-11-08 is proposed for the Phase 0 owner review.
- Stop condition: no data extraction or cell-level claim until dataset compatibility and the sensory-to-output evidence are reviewed.
