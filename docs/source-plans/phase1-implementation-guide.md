# NeuroFly Phase 1 Implementation Guide

**Phase:** 1 — Assay and circuit evidence  
**Status:** Working guide; Phase 1 remains gated by Phase 0 owner signoff.  
**Active repository:** C:\Users\abhi0\Desktop\NeuroFly\NeuroFly  
**Repository location note:** The current Git project is the nested NeuroFly folder under C:\Users\abhi0\Desktop\NeuroFly. Treat the nested folder as the project root. Update stale path references in the Phase 0 records during the Phase 0 correction work.

## 1. Purpose

Phase 1 turns NeuroFly’s proposed taste-contact experiment into a source-backed, reviewable assay specification. It identifies a candidate gustatory-to-proboscis circuit, records what the connectome and published work support, defines the model assumptions, and states how the first comparison will be judged.

This phase is evidence work. It does not build the data-extraction pipeline, neural engine, body mechanics, fly asset, Habitat interface, or simulation service. The next implementation planner phase is Phase 2, asset triage and Habitat greybox. Connectome data-pipeline implementation is Phase 3 in the detailed planner.

## 2. Phase alignment and entry gate

The source plans number phases differently. The complete project plan calls the data pipeline “Phase 1”; the detailed implementation planner calls Phase 1 “Assay and circuit evidence” and places asset/greybox work in Phase 2 and data-pipeline implementation in Phase 3. This guide follows the detailed implementation planner, which is the active execution sequence for this repository. Record any alternative sequencing as a decision before changing it.

Before starting any Phase 1 work:

- [ ] Correct the Phase 0 source index and source packet as described in Section 3.
- [ ] Update stale references to the project root. The active repository is C:\Users\abhi0\Desktop\NeuroFly\NeuroFly; the outer C:\Users\abhi0\Desktop\NeuroFly folder contains it.
- [ ] Review docs/phase0-checklist.md and record explicit owner confirmation of Phase 0.
- [ ] Confirm the Phase 0 audience, first behavior, deployment assumptions, and proposal statuses are accepted or revised.
- [ ] Confirm the source-plan packet and its checksums are complete for all available source documents.
- [ ] Record the Phase 1 owner and review date in the decision log.

**Stop condition:** If Phase 0 is still blank or unconfirmed, complete the Phase 0 correction work and stop for owner confirmation. Do not begin Phase 1 circuit selection, data acquisition, code, or cell-level public claims while the gate is open.

## 3. Phase 0 corrections to carry into the handoff

The previous review found a source-provenance gap. The current docs/source-plans/SOURCE_INDEX.md points to files directly under C:\Users\abhi0\Desktop\NeuroFly, but that direct location does not contain those plan files. The original files are available in the earlier project output folders, including the revised blueprint that is absent from the current source packet.

Resolve this before treating Phase 0 as complete:

1. Preserve each original source file unchanged.
2. Copy neurofly_revised_blueprint.md from the available original source location into docs/source-plans/.
3. Correct docs/source-plans/SOURCE_INDEX.md so every file names its actual original location and role. Do not use a guessed or parent-folder path.
4. Regenerate docs/source-plans/SHA256SUMS.txt for every source-plan copy, including the revised blueprint.
5. Verify each copied file against its actual original with SHA-256; separately verify each current copy against the manifest.
6. Update README.md, docs/phase0-walkthrough-and-summary.md, and docs/phase0-checklist.md to remove the inaccurate “revised blueprint missing” statement and reflect the moved repository root.
7. Keep the owner-confirmation fields blank until the owner actually reviews and approves Phase 0. Do not turn a documentation correction into implied scientific or owner approval.

Known source locations from the earlier project work include:

- C:\Users\abhi0\Documents\Codex\2026-11-01\hey-ben-i-have-had-a\outputs\neurofly_complete_project_plan.md
- C:\Users\abhi0\Documents\Codex\2026-11-01\hey-ben-i-have-had-a\outputs\neurofly_revised_blueprint.md
- C:\Users\abhi0\Documents\Codex\2026-11-01\hey-ben-i-have-had-a\outputs\neurofly_environment_asset_planner.md
- C:\Users\abhi0\Documents\Codex\2026-11-01\read-and-analyze-the-project-plan\outputs\neurofly_implementation_planner.docx
- C:\Users\abhi0\Documents\Codex\2026-11-01\read-and-analyze-the-project-plan\outputs\neurofly_phase0_execution_guide.docx

If any listed source is unavailable at execution time, search the supplied project sources and adjacent output folder before declaring it missing. Record what was checked. Never reconstruct a source document from memory.

## 4. Phase 1 objective

Define one bounded, repeatable assay and trace enough source-backed structural evidence to state whether a gustatory-to-proboscis path is supported in the chosen data release.

The working behavior remains:

**valid taste-patch contact -> gustatory input -> selected connectome circuit -> motor output -> possible proboscis response**

A no-response trial is a valid result. A stimulus label must not directly select an animation. The project may narrow the behavior if reference methods or cell evidence do not support the proposed path.

## 5. Targets and required evidence

Phase 1 is complete when the project has:

1. **One assay specification** with a testable question, hypothesis, starting state, contact definition, stimulus, trial duration, reset policy, and expected observation.
2. **One reference-method review** that records the actual published assay, model, stimulation/input, circuit scope, output, and limitations used for comparison.
3. **One dataset decision** naming the exact release and identifier namespace, or a documented compatible alternative. Any cross-release mapping is explicit and evidenced.
4. **One source-backed cell and edge register** for candidate sensory, intermediate, and proboscis motor cells, with stable IDs and uncertainty.
5. **One traceable candidate path** from sensory input to motor output, with each edge labelled by evidence source and confidence. Missing links remain visible.
6. **Explicit mapping hypotheses** for stimulus-to-sensory input and model motor output-to-proboscis action. Evidence and model assumptions are separated.
7. **A predeclared evaluation protocol** with one primary measure, a comparison condition, a candidate intervention effect, and appropriate baseline controls.
8. **A limitations and open-decision list** with owners, next actions, dates, and block effects.
9. **Owner signoff of the Phase 1 evidence gate** before Phase 2 begins.

No target requires a whole-brain circuit or a complete pathway if the evidence does not support one. A narrower, honest assay is a valid Phase 1 outcome.

## 6. Work plan

Complete the steps in order. For each task group, record **Do**, **Check**, and **Confirm** evidence in the Phase 1 files. If a task cannot be completed, write down the evidence gap and its effect on the project; do not replace missing evidence with an assumption.

### P1.0 Verify the entry gate and create the Phase 1 evidence workspace

**Do**

1. Confirm the current repository root is C:\Users\abhi0\Desktop\NeuroFly\NeuroFly.
2. Read applicable AGENTS.md instructions and the Phase 0 checklist.
3. Verify the source-index and checksum corrections are complete.
4. Confirm Phase 0 owner signoff is recorded. If it is not, stop here for confirmation.
5. Create docs/phase1/ for the evidence package.
6. Record the starting repository state and date in docs/phase1/README.md. Do not change Git configuration, initialize a second repository, or create a commit unless separately requested.

**Check**

- The root contains the expected README.md, .git, and docs/.
- The source packet and signoff match the checklist.
- The Phase 1 workspace contains no copied raw connectome archive or unreviewed asset.

**Confirm**

- Record the Phase 0 signoff link, Phase 1 owner, review date, and Phase 1 status as “In progress.”

### P1.1 Make the first question testable

**Do**

1. Copy the approved first-release behavior into docs/phase1/assay-specification.md.
2. Write one question that can be answered by the planned trial.
3. Write one falsifiable hypothesis linking valid contact, gustatory input, circuit response, and a possible proboscis output.
4. List the expected neural and body outputs separately.
5. State what result would count against the hypothesis, including no response or an output that does not differ from the relevant control.
6. Mark every item as measured, inferred, modeled, predicted, or not yet known.

**Check**

- The hypothesis does not assume the sensory-to-motor path exists before it is traced.
- The expected output is not simply copied from the stimulus name.
- A null or contrary result has a place in the specification.

**Confirm**

- The project owner and scientific reviewer can restate the hypothesis in one sentence and identify what evidence would disconfirm it.

### P1.2 Review the published reference and its methods

**Do**

1. Use the selected primary paper, supplementary methods, and reference model repository named in the project plan.
2. Record the full citation, DOI, supplementary file/version, repository URL, and the date reviewed.
3. Extract the assay actually performed: organism or preparation, stimulus, starting condition, trial length, perturbation, measured output, and controls.
4. Record the neural model actually used: circuit scope, data release, neuron/edge selection, dynamics, input encoding, parameters, and output decoder where reported.
5. Separate what the paper measures from what its model assumes.
6. Note any difference between the published feeding/grooming scope and NeuroFly’s narrower taste-contact assay.
7. Record unresolved details as questions for the dataset and cell review.

**Check**

- Each claim has a page, figure, supplement section, code location, or other source locator.
- Do not claim NeuroFly reproduces the reference until the experimental and computational details match.
- If the reference does not support a specific taste-to-proboscis question, revise or narrow the hypothesis.

**Confirm**

- Save docs/phase1/reference-methods-review.md and cite it from the assay specification.

### P1.3 Fix the trial protocol before tracing the path

**Do**

1. Define the initial body pose or stationary starting state.
2. Define the taste-patch location, size, and contact geometry at the level needed for the assay.
3. Define what “valid contact” means and how contact onset will be timestamped.
4. Define the taste condition and concentration or intensity if supported by the reference.
5. If the exact sensory encoding is unknown, specify the unresolved mapping and do not invent receptor firing values.
6. Set the planned trial duration and reset state from the reference or clearly label a project choice.
7. Define how baseline and intervention trials will reuse the same pose, patch, stimulus, seed policy, and timing.
8. Define permitted visitor actions and confirm that scientific trials do not include direct fly posing.

**Check**

- The protocol distinguishes physical contact from stimulus selection.
- Every trial parameter has a source or is labelled a modeled/project choice.
- The same conditions can be repeated for a later comparison.

**Confirm**

- Save the trial protocol in docs/phase1/assay-specification.md; leave unsupported values visibly pending.

### P1.4 Select the release and resolve the identifier question

**Do**

1. Record the dataset candidate, exact release/version, source URL, citation, identifier namespace, and license/access terms.
2. Use official dataset documentation or official data products to confirm how cell IDs and annotations are defined.
3. Compare the reference model’s snapshot with the candidate FAFB v783 release.
4. Identify which IDs are stable, which require a crosswalk, and which annotations are release-specific.
5. Decide among: reproduce on the reference-compatible release; use FAFB v783 with a validated crosswalk; or narrow the comparison to a compatible source-backed path.
6. Record the exact selected release and any crosswalk method in docs/phase1/dataset-release-and-id-compatibility.md.
7. If compatibility remains unknown, assign a specific verification task and keep extraction blocked.

**Check**

- Do not mix FAFB, BANC, MCNS, or other identifier systems without an explicit documented mapping.
- Do not treat a matching cell name as proof that two release IDs refer to the same neuron.
- Confirm license and access terms before downloading or retaining data.

**Confirm**

- The dataset decision is reproducible by another contributor using the recorded source and release identifier.

### P1.5 Locate candidate sensory and motor cells

**Do**

1. Search official connectome annotations, browser views, or static official data products for gustatory sensory candidates relevant to the selected stimulus.
2. Locate candidate intermediate cells only where the source evidence supports their role.
3. Locate candidate proboscis motor outputs from published annotations or validated references.
4. Record each candidate’s stable ID, dataset release, cell type/name, annotation source, query or selection method, and date reviewed.
5. Record neurotransmitter labels and confidence only when the source supplies them; separate observed labels from assumptions.
6. Attach the source and an uncertainty note to every proposed functional label.
7. Keep alternative candidates when evidence is ambiguous; do not choose the one that best fits the expected behavior without evidence.

**Check**

- IDs resolve in the chosen release.
- Candidate names and roles are labelled as measured annotation, inferred role, or unresolved.
- No cell identity is invented or copied across releases without a verified mapping.

**Confirm**

- Save candidate records in docs/phase1/cell-edge-evidence-register.md.

### P1.6 Trace the structural path and record gaps

**Do**

1. Start from the candidate gustatory sensory cell or cells and work toward a candidate proboscis motor output.
2. Record each pre- and postsynaptic stable ID, release, direction, edge evidence source, and connection/synapse statistic used.
3. Note any filtering or threshold rule and why it is used; do not choose a threshold after seeing which pathway looks strongest.
4. Classify each link as measured structural connectivity, inferred biological role, modeled influence, or missing evidence.
5. Record whether intermediate stages are directly supported, inferred from annotations, or omitted by the chosen model.
6. Record alternative paths and disconnected or uncertain steps.
7. Decide whether the evidence supports the original behavior, a narrower circuit claim, or no defensible cell-level claim yet.

**Check**

- Structural connection counts are not described as functional synaptic weights without a justified conversion.
- Direction and source release are clear for each edge.
- A path with missing links is not called complete.

**Confirm**

- A reviewer can follow the evidence from each candidate input to each candidate output and see every uncertainty.

### P1.7 Specify input and output mapping hypotheses

**Do**

1. Write the stimulus-to-sensory mapping in one explicit statement.
2. State which parts are supported by the reference or data and which are modeled.
3. Write the motor-output-to-body-action mapping: output variable, sign/range, extension/hold/retraction interpretation, and expected lag if known.
4. Identify any missing body measurement or calibration that must wait for the body phase.
5. State how no output, conflicting outputs, or an out-of-range value will be represented in the later implementation.
6. Keep display-only effects out of the simulation mapping.

**Check**

- No click, patch label, or UI state directly selects a proboscis animation in a scientific trial.
- The output mapping is testable and traceable, even if it remains a hypothesis at this phase.
- Later body calibration can replace the provisional mapping without changing the data provenance.

**Confirm**

- Save the mapping and its evidence status in the assay specification and decision log.

### P1.8 Choose the primary measure and predeclare the comparison

**Do**

1. Review the reference outcome and select one primary response measure.
2. Define the measure operationally. For example, if using latency, define the timestamp origin and what counts as response onset; if using extension, define the output state or threshold.
3. Select any secondary measures and explain why they support the primary one.
4. Define the baseline run and one candidate intervention comparison.
5. Select the intervention target only if the Phase 1 cell/edge evidence supports it. Otherwise leave it unresolved and state what evidence is missing.
6. Write the predicted intervention effect before examining held-out results.
7. State which changes are allowed between paired runs and how all other settings remain fixed.

**Check**

- One metric is primary; several equally primary metrics do not make the result easier to interpret.
- The intervention prediction is timestamped or otherwise recorded before results are reviewed.
- No threshold is chosen solely because it makes the desired intervention appear successful.

**Confirm**

- Save the definitions and prediction in docs/phase1/evaluation-protocol.md.

### P1.9 Specify the controls and comparison logic

**Do**

1. Evaluate whether a no-contact condition tests dependence on physical contact.
2. Evaluate whether a no-sensory condition tests dependence on the input pathway.
3. Include an always-respond control to expose behavior that ignores stimulus or circuit state.
4. Include a simple-rule baseline to test whether a trivial mapping explains the same output.
5. Consider a shuffled or matched-graph comparison if the reference and available data support a fair construction.
6. For every selected control, state the expected result, the interpretation if it passes, and the limitation.
7. Do not include an invalid control merely to complete a checklist; record why it does not apply.

**Check**

- At least one control challenges the claimed sensory cause, and one challenges the claimed circuit contribution.
- Baseline conditions share the same trial setup as the proposed circuit run except for the deliberate change.
- A trivial baseline that matches the proposed circuit result prevents a causal claim until the assay is redesigned.

**Confirm**

- Put the control table in docs/phase1/evaluation-protocol.md.

### P1.10 Review uncertainty, claims, and next-phase dependencies

**Do**

1. Update the decision log with the assay, reference, dataset release, IDs, pathway, intervention, metric, and control decisions.
2. Update the risk register with any newly discovered release, annotation, path, or reference-method risk.
3. Mark unresolved claims and name the evidence needed to resolve each one.
4. Write the narrowest claim supported by the evidence assembled so far.
5. List what Phase 2 needs from this phase: validated contact point, chosen body output, candidate measurement, and any limits on anatomical naming.
6. List what the later Phase 3 data pipeline must not assume: exact release, ID namespace, edge threshold, filters, or transmitter interpretation that are still pending.
7. Review all tables for source links and uncertainty labels.

**Check**

- No unresolved high-impact item is hidden in prose or marked Confirmed by default.
- The README and public-facing language do not overstate cell-level or biological evidence.
- The asset remains a separate task; no unverified model is introduced through the evidence work.

**Confirm**

- Save the open decisions and limitations in docs/phase1/phase1-open-decisions.md.

### P1.11 Hold the Phase 1 review and signoff

**Do**

1. Review every Phase 1 deliverable against Section 5.
2. Ask a second reviewer to follow the proposed path from its cited sources if one is available; if working solo, perform the same source-to-claim check yourself and label it as self-review.
3. Confirm the assay is reproducible from written values and sources.
4. Confirm the selected data release and identifier strategy, or record why the claim was narrowed.
5. Confirm the primary measure, intervention prediction, and control logic were written before evaluation results.
6. Record blockers, owners, and dates.
7. Complete the signoff record below.

**Phase 1 signoff record**

- Phase 0 confirmation reference: ______________________________________
- Phase 1 owner/reviewer: _____________________________________________
- Assay/reference accepted: [ ] Yes  [ ] No
- Dataset release and identifier plan: _________________________________
- Sensory-to-output path status: [ ] Supported  [ ] Narrowed  [ ] Unresolved
- Primary metric and intervention prediction recorded: [ ] Yes  [ ] No
- Open blockers and owners: __________________________________________
- Phase 1 status: [ ] Confirmed  [ ] Rework required
- Approval to begin Phase 2: [ ] Yes, after this signoff  [ ] Hold
- Typed name and date: _______________________________________________

**Exit gate:** Phase 1 is confirmed only when the assay and evidence package are source-backed, uncertainties and model choices are visible, any unresolved path has led to a narrower claim or explicit rework decision, and the project owner approves the handoff. Do not begin Phase 2 automatically.

## 7. Evidence vocabulary and confidence rules

Use the project’s existing terms consistently:

- **Measured:** directly present in a named dataset or published experiment, with release and source recorded.
- **Inferred:** an interpretation supported by evidence but not directly established by the selected data.
- **Modeled:** a rule or parameter NeuroFly implements, including sensory encoding, neural dynamics, edge-weight conversion, motor decoding, and body mechanics.
- **Predicted:** an expected comparison result written before the comparison is inspected.
- **Display-only:** a visual effect that does not feed simulation state or determine the action.

For each cell, edge, and mapping, record a confidence label such as high, medium, low, or unresolved, plus a short reason. Confidence is a summary of evidence quality, not a substitute for citations. Do not turn a structural edge into a causal functional claim without a model and evaluation that support that interpretation.

## 8. Required Phase 1 files

Create and maintain these files under docs/phase1/:

| File | Contents |
|---|---|
| README.md | Phase 1 status, owner, date, link to Phase 0 signoff, and index of evidence files. |
| assay-specification.md | Testable question, hypothesis, stimulus, contact definition, trial state, expected outputs, and mappings. |
| reference-methods-review.md | Paper and supplement methods, reference code details, outcome, limitations, and NeuroFly differences. |
| dataset-release-and-id-compatibility.md | Official release, identifier namespace, access/license, reference snapshot comparison, and crosswalk decision. |
| cell-edge-evidence-register.md | Candidate sensory/intermediate/motor cells, directed edges, stable IDs, source evidence, confidence, and unknowns. |
| evaluation-protocol.md | Primary metric, paired comparison, intervention prediction, controls, and decision rules. |
| phase1-open-decisions.md | Unresolved questions, risks, owners, next actions, dates, and block effects. |

Do not add raw connectome archives, large data dumps, unverified assets, or API credentials to this evidence folder.

## 9. Suggested record templates

### Cell evidence row

| Release | Stable ID | Proposed role | Annotation/name source | Evidence type | Confidence and reason | Unknowns |
|---|---|---|---|---|---|---|

### Edge evidence row

| Release | Pre ID | Post ID | Structural statistic/source | Filter or threshold | Evidence type | Confidence | Interpretation limits |
|---|---|---|---|---|---|---|---|

### Decision/open-question row

| Question or decision | Current status | Evidence/source | Next action | Owner | Review date | What it blocks |
|---|---|---|---|---|---|---|

### Trial protocol row

| Field | Value | Source or status | Repeat/reset rule |
|---|---|---|---|
| Starting pose |  |  |  |
| Patch location and geometry |  |  |  |
| Valid-contact definition |  |  |  |
| Taste condition/intensity |  |  |  |
| Sensory-input mapping |  |  |  |
| Trial duration |  |  |  |
| Reset state |  |  |  |
| Primary response measure |  |  |  |
| Intervention |  |  |  |

## 10. Items that remain outside Phase 1

- Bulk connectome download, extraction scripts, and compact subgraph generation.
- Neural-engine selection and implementation.
- Sensory encoder code, body actuator calibration, and contact simulation.
- Fly asset search, licensing, rigging, and Habitat greybox.
- Frontend, service, WebSocket, deployment, and live simulation work.
- Public cell names or pathway claims unsupported by the evidence register.
- A whole-brain, complete-fly, or production-validity claim.

These remain later work or explicit project decisions. Phase 1 may create a source-backed evidence record and narrow the scientific question; it does not claim that NeuroFly already simulates the published behavior.

## 11. Source documents

Use the corrected source packet and current project records. The current packet should include the complete project plan, revised blueprint, implementation planner, environment/asset planner, and Phase 0 execution guide.

- ../source-plans/neurofly_complete_project_plan.md
- ../source-plans/neurofly_revised_blueprint.md
- ../source-plans/neurofly_implementation_planner.docx
- ../source-plans/neurofly_environment_asset_planner.md
- ../source-plans/neurofly_phase0_execution_guide.docx
- ../phase0-checklist.md
- ../phase0-walkthrough-and-summary.md
- ../assay-and-data-handoff.md
- ../evidence-and-claims.md
- ../decisions.md
- ../risks.md

**Stop point:** This guide prepares Phase 1. It does not confirm Phase 0, authorize bulk data acquisition, or start Phase 2. Record each owner gate before proceeding.

