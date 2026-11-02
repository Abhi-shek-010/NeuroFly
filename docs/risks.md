# Risk Register

Owner role for the initial register: NeuroFly project owner. The individual name is not yet recorded. Proposed review date: 2026-11-08; confirm or replace.

## Dataset snapshot mismatch

- Likelihood / impact: Medium / High.
- Early signal: reference IDs or annotations do not resolve in FAFB v783, or sources refer to different releases.
- Mitigation: pin the official release and source terms; retain stable IDs and create a documented crosswalk or narrow the comparison.
- Stop condition: no bulk download, extraction, or cell-level claim until compatibility is reviewed.

## Gustatory-to-motor path cannot be traced

- Likelihood / impact: Medium / High.
- Early signal: missing intermediate cells or edges, uncertain annotations, or no source for the motor endpoint.
- Mitigation: record each ID, edge, evidence source, transmitter confidence, and uncertainty; narrow the behavior claim if the path is incomplete.
- Stop condition: do not invent cell identities, label the path complete, or build a named circuit into the interface.

## Renderer or scripted animation chooses the behavior

- Likelihood / impact: Medium / High.
- Early signal: a stimulus click or experiment label triggers proboscis animation without a simulation motor value.
- Mitigation: enforce a one-way display contract from simulation state to renderer; isolate pose tools in developer-only mode.
- Stop condition: no scientific trial or behavior claim until motor output, actuator state, and displayed movement are traceable.

## Modeled behavior is presented as a complete biological fly

- Likelihood / impact: Medium / High.
- Early signal: copy describes full brain simulation or presents modeled dynamics and body rules as measured data.
- Mitigation: use the evidence vocabulary and claim-boundary sentence in README, interface, and demo material.
- Stop condition: revise public copy before release if evidence categories or circuit scope are missing.

## Fly asset rights or rig are unsuitable

- Likelihood / impact: Medium / Medium.
- Early signal: original creator terms cannot be found, redistribution is restricted, or the model lacks a movable proboscis.
- Mitigation: verify the original source and actual file; use an original procedural fallback when unresolved.
- Stop condition: do not bundle an unverified model publicly; do not let an asset search block the labeled placeholder.

## Sensory/contact or body mapping is unsupported

- Likelihood / impact: Medium / High.
- Early signal: stimulus labels directly cause behavior, contact is not pose-dependent, or a motor value does not map to repeatable proboscis motion.
- Mitigation: document contact geometry, encoding assumptions, actuator limits, lag, and calibration before integration.
- Stop condition: no integrated causal claim until the input and output mappings are defined and checked.

## Public deployment or exhibit fallback fails

- Likelihood / impact: Medium / High.
- Early signal: a static host is expected to run the Python service, WebSocket access is unavailable, or venue internet is required.
- Mitigation: keep frontend and simulation service separate; prepare and profile a local fallback on the target laptop before exhibit release.
- Stop condition: do not call the exhibit ready until the selected device and offline path have been exercised.

## Simple baseline succeeds without the intended cause

- Likelihood / impact: Medium / High.
- Early signal: always-respond or sensory-blind baseline meets the same response criterion as the proposed circuit.
- Mitigation: use no-contact, no-sensory, simple-rule, and matched/shuffled controls as appropriate; revise the assay if it does not distinguish causes.
- Stop condition: do not interpret neural activity as causal evidence if the assay passes without the claimed input or circuit.
