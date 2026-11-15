# Assay and Data Handoff

## First assay

The owner accepted physical taste-patch contact followed by a possible feeding-related proboscis response as the MVP question and Habitat contact-design basis during the Phase 1 signoff on 2026-11-14. The named sensory-to-MN9 route remains a candidate until FAFB v783 identities and edges are verified in Phase 3. Approach behavior is out of scope.

## Reference candidate

The project plan names Shiu et al. (2024), Nature, DOI [10.1038/s41586-024-07763-9](https://doi.org/10.1038/s41586-024-07763-9), as a connectome-based LIF model of feeding and grooming. Phase 1 reviewed the paper and public reference implementation. NeuroFly has not reproduced that model.

## Candidate dataset and stop condition

- Candidate: FlyWire FAFB v783, female adult brain snapshot.
- Status: FAFB v783 is the selected MVP snapshot; exact v783 root IDs and cross-version cell identities remain unresolved.
- Identifier namespace: use FAFB v783 identifiers only. Exact cell identities and a v630-to-v783 mapping are unverified and assigned to Phase 3.
- Rule: do not extract a subgraph, claim a specific v783 cell/pathway, or integrate a neural circuit until Phase 3 resolves the exact identities and edges.
- Do not mix FAFB, BANC, or MCNS identifiers without an explicit documented mapping.

The Phase 0 guide reconciles the project plan's early release decision with the implementation planner's separate circuit-evidence phase: Phase 0 records the named reference and candidate release, while Phase 1 owns snapshot compatibility and cell mapping. This is the active handoff rule.

## Phase 3 work required before extraction

1. Obtain the exact candidate cell identities from the official v783 annotation and mapping resources; record evidence and unresolved split/merge ambiguity.
2. Query release-specific connectivity for each proposed pathway segment and report pairwise synapse counts and threshold sensitivity.
3. Confirm that the extracted candidate route connects sensory input to the chosen motor output in FAFB v783 before freezing a subgraph.
4. Keep FAFB and BANC identifiers separate; use only mappings with explicit provenance.
5. Preserve provisional sensory, motor, and body mappings as modeled assumptions for later calibration; do not infer them from connectome structure alone.

## Measures and comparison candidates

The primary metric, provisional thresholds, candidate controls, and seed-matched intervention comparison are specified in docs/phase1/evaluation-protocol.md. They are evaluation plans, not measured NeuroFly results.

## Ownership

- Owner: NeuroFly project owner; individual name to be recorded.
- Review date: Phase 1 owner decision recorded 2026-11-14.
- Stop condition: no subgraph extraction, neural integration, or specific v783 pathway claim until Phase 3 verifies the exact identities and edges.
