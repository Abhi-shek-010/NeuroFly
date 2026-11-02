# NeuroFly Phase 0 Walkthrough and Summary

**Build record date:** 2026-11-01  
**Repository:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Phase status:** Foundation prepared for project-owner review; Phase 0 is not confirmed.  
**Phase 1 status:** On hold pending explicit Phase 0 confirmation.

## 1. Purpose of this record

This document maps the Phase 0 work completed in the repository to the detailed execution guide. It records what was read, what was created, which decisions are only proposals, which scientific or asset items remain unresolved, and what evidence is available for the next review.

Phase 0 is project setup and scope control. It does not implement the connectome pipeline, neural dynamics, fly asset, simulation service, or interactive Habitat. The folder layout is scaffolding. A file or folder being present is not evidence that its later-phase system works.

## 2. Current status at a glance

| Area | State | What that means |
|---|---|---|
| Repository and project records | Prepared | The active repository has the README, source packet, project records, and planned module folders. |
| MVP scope | Written as a proposal | One taste-contact-to-proboscis loop is documented. The project owner has not signed off on it yet. |
| Scientific reference | Candidate recorded | Shiu et al. (2024) is the named feeding-model reference candidate; its methods have not yet been reproduced or fully translated into an assay specification. |
| Dataset | Candidate recorded; compatibility unresolved | FAFB v783 is the candidate snapshot. Stable IDs and compatibility with the reference's earlier snapshot are not verified. Extraction is blocked. |
| Neural model | Deferred | Brian 2 LIF is one candidate if its assumptions match the reference. No engine or parameters have been frozen. |
| Fly asset | Missing or unverified | No fly image/model is in the supplied source folder. A candidate lead is unverified; a small procedural model is the fallback. |
| Runtime and deployment | Proposed | The desktop browser and local-first direction are recorded as proposals. No app runtime or local start command exists. |
| Owner approval | Pending | The confirmation record is blank. The guide requires explicit approval before Phase 1 begins. |

## 3. Working direction established from the plans

### First behavior

The proposed first-release causal loop is:

`physical taste-patch contact -> gustatory input -> selected connectome circuit -> motor output -> proboscis response`

The visitor operates the experiment by setting or activating a stimulus and running a trial. The visitor does not directly pilot the fly during a scientific run. The displayed proboscis action must follow simulation motor output. If the model produces no response, that outcome remains visible and is recorded.

### Research question

The charter carries forward the project plan's question: can a neural model constrained by measured fly connections turn sensory events into coordinated actions that resemble published fly behavior, and do circuit perturbations change those actions in predicted ways?

### Scope boundary

The MVP proposal is limited to taste contact and a feeding-related proboscis response. Walking, food stopping, flight, odor search, visual escape, grooming, associative learning, and whole-brain behavior are deferred. Approach behavior is also outside the first assay unless a later evidence review brings it into scope.

### Evidence boundary

The project is described as a connectome-constrained model of a selected behavior, not as a complete biological fly or whole-brain simulator. The connectome provides structural evidence. Neural dynamics, sensory encoding, motor decoding, and body mechanics are modeled or inferred layers and must be labeled as such.

## 4. Walkthrough of the Phase 0 build

### Step 1 - Open and identify the implementation workspace

**Work performed:**

- Inspected the repository structure and confirmed the active repository root is `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly` (nested within `C:\Users\abhi0\Desktop\NeuroFly`).
- Confirmed that the repository is on local branch `master`, has no commit yet, and has no configured remote.
- Located original source planning documents in their canonical output folders under `C:\Users\abhi0\Documents\Codex\2026-11-01` and preserved them untouched.
- Added a root README recording repository purpose, current phase, scope boundary, source packet location, and the fact that no application run command exists yet.
- Added `.gitignore` entries for Python caches and virtual environments, frontend build output and dependencies, local secrets, logs, and large/raw connectome files. Source plans and decision records are not ignored.

**Evidence:** [`README.md`](../README.md), [`.gitignore`](../.gitignore), [`docs/phase0-checklist.md`](phase0-checklist.md).

**Status:** Complete for the Phase 0 foundation. The application runtime and local start instructions remain future implementation work.

### Step 2 - Preserve the planning inputs

**Work performed:**

- Copied the complete project plan, revised blueprint, implementation planner, environment/asset planner, and Phase 0 guide into `docs/source-plans/` without editing the original source copies.
- Compared SHA-256 hashes for each original and repository copy, and generated `SHA256SUMS.txt`.
- Added an index (`SOURCE_INDEX.md`) describing each file's title, actual original path, and role.
- Retained the Phase 1 implementation guide placed directly into `docs/source-plans/` as the execution checklist for Phase 1.

**Evidence:** [`docs/source-plans/SOURCE_INDEX.md`](source-plans/SOURCE_INDEX.md), [`docs/source-plans/SHA256SUMS.txt`](source-plans/SHA256SUMS.txt).

**Status:** Complete. The source packet contains all five planning inputs and the Phase 1 guide.

### Step 3 - Prepare the project charter

**Work performed:**

- Recorded the primary research question and first visible behavior.
- Proposed science learners and educators as the primary audience, with judges and technical reviewers as secondary audiences.
- Proposed a browser-based demonstration/exhibit with a desktop recent-laptop target and local exhibit fallback.
- Defined the visitor as experiment operator, not fly pilot.
- Described what a viewer should understand from a baseline and comparison run.
- Recorded no-response as a valid result and preserved the scientific claim boundary.

**Evidence:** [`docs/project-charter.md`](project-charter.md).

**Status:** Prepared for review. The audience, venue, device, browser, and demo context are proposals, not confirmed owner decisions.

### Step 4 - Write the MVP boundary

**Work performed:**

- Chose the taste-contact-to-proboscis path as the proposed single first behavior.
- Kept approach behavior out of the first assay.
- Listed walking, stopping/halting, flight, grooming, odor search, vision, learning, and whole-brain behavior as deferred.
- Stated that patch activation or stimulus choice cannot directly trigger a feeding animation.
- Reserved a possible node-silencing comparison for later evidence review; no neuron or intervention target was selected in Phase 0.
- Required repeatable baseline and intervention trials to share starting pose, contact, and settings, with any changed variable recorded.

**Evidence:** [`docs/project-charter.md`](project-charter.md), [`docs/evidence-and-claims.md`](evidence-and-claims.md), [`docs/assay-and-data-handoff.md`](assay-and-data-handoff.md).

**Status:** Scope is written but not formally frozen until the project owner confirms the Phase 0 gate.

### Step 5 - Establish evidence and claims rules

**Work performed:**

- Defined **Measured**, **Inferred**, **Modeled**, **Predicted**, and **Display-only**.
- Set the claim boundary that NeuroFly models a selected behavior and is not a full biological fly or whole-brain simulator.
- Required scientific body motion to follow model motor output rather than a renderer-selected behavior.
- Required valid contact to depend on geometry and body pose.
- Preserved no-response as an outcome.
- Specified that browser previews, surrogates, physics reference runs, and recorded replays must be labeled separately.
- Listed run-record fields to preserve provenance and comparisons, including scenario, data/graph/model versions, initial pose, stimulus, seed, intervention, time-stamped summaries, outcome, failures, and software build.

**Evidence:** [`docs/evidence-and-claims.md`](evidence-and-claims.md).

**Status:** Recorded as the working standard; owner approval is pending.

### Step 6 - Record the assay and dataset handoff

**Work performed:**

- Named Shiu et al. (2024), *Nature*, DOI 10.1038/s41586-024-07763-9, and the associated model repository as the reference candidate identified by the plan.
- Marked the specific assay methods, stimulation protocol, circuit, output definition, and comparison metric for review in Phase 1.
- Recorded FlyWire FAFB v783 as a candidate snapshot, not a locked release.
- Recorded the known concern that the reference code uses an earlier FlyWire snapshot and that a stable ID crosswalk has not been verified.
- Set a stop condition against bulk download, extraction, bundling, neuron naming in the interface, and cell-level claims until official source terms, release compatibility, stable IDs, and crosswalk needs are reviewed.
- Listed response probability, latency, and extension amplitude/state as candidate measures; final definitions and thresholds are pending reference review.
- Listed no-contact, no-sensory, always-respond, simple-rule, and shuffled/matched-graph conditions as candidate controls.
- Left the silencing target unset until Phase 1 provides source-backed evidence.

**Phase alignment:** The complete plan places exact assay and release selection in its Phase 0. The implementation planner places cell/edge tracing in Phase 1. The Phase 0 guide reconciles these: Phase 0 names the reference and candidate release and assigns snapshot/ID compatibility to Phase 1, with extraction held behind that review. This reconciliation is recorded as the handoff rule.

**Evidence:** [`docs/assay-and-data-handoff.md`](assay-and-data-handoff.md), [`docs/decisions.md`](decisions.md).

**Status:** Handoff prepared; exact release, circuit, cell IDs, and methods remain unresolved and block later data extraction and named circuit claims.

### Step 7 - Record the runtime and deployment proposal

**Work performed:**

- Documented the causal state flow from visitor command through contact, sensory input, neural model, motor decoder, body state, and rendered evidence timeline.
- Recorded React, TypeScript, Vite, and Three.js as the candidate frontend stack.
- Recorded Python data preparation and a FastAPI/WebSocket service with a separate simulation worker as candidate backend/runtime shapes.
- Recorded Brian 2 LIF as a candidate only if it matches the reference assumptions; a declared rate model remains an alternative, not a second hidden engine.
- Separated render geometry from physics/body state and actuator mapping.
- Proposed desktop mouse/keyboard on a recent laptop, Chrome or Edge, and local-first development with an offline exhibit fallback.
- Deferred public hosting until the MVP evidence gate; if selected, the static frontend and WebSocket-capable simulation service remain separate.
- Recorded that credentials do not belong in frontend code and raw connectome archives do not belong in the public client bundle.

**Evidence:** [`docs/architecture.md`](architecture.md), [`docs/decisions.md`](decisions.md).

**Status:** Architecture direction is documented, not frozen. No application runtime, simulator, frontend, or executable local command has been built in Phase 0.

### Step 8 - Record the fly asset route

**Work performed:**

- Recorded that the supplied folder contains no verified fly image, model, runtime asset, or rig.
- Carried forward the etainproject CT-scan model lead credited by FruitFly Hub as CC BY 4.0, while marking the original listing, current terms, public redistribution rights, actual file, mesh, and rig as unverified.
- Defined a procedural or hand-built greybox as the fallback, with separate body/head/legs/proboscis pieces and a proboscis pivot/contact proxy.
- Listed intake checks for creator/source, license, redistribution, modification, dimensions/orientation, mesh/materials, skeleton/pivots, proboscis motion, contact proxy, and public credits.
- Kept source files, runtime exports, physics assets, calibration data, and credits in separate planned locations.

**Evidence:** [`docs/asset-register.md`](asset-register.md), [`docs/risks.md`](risks.md).

**Status:** Asset route recorded. No external asset was downloaded, adopted, or cleared for public use.

### Step 9 - Create the planned repository layout

**Work performed:** Created the directories requested by the Phase 0 plans and asset planner. `.gitkeep` files make empty folders visible to Git; they are scaffolding only.

- `docs/source-plans/` for the preserved source packet.
- `data_pipeline/` for later retrieval/extraction tooling; extraction remains blocked.
- `subgraphs/` for approved compact graph exports; none are present.
- `simulation/` for the selected neural engine; none is implemented.
- `body/` for contact, body state, actuators, and calibration; none is implemented.
- `frontend/` for the shared Habitat UI; no frontend code is implemented.
- `scenarios/` for future trial presets.
- `evaluation/` for baselines and reports.
- `assets/fly/source/`, `assets/fly/runtime/`, and `assets/fly/physics/` for distinct fly asset roles.
- `assets/world/source/`, `assets/world/runtime/`, `assets/textures/source/`, `assets/ui/`, and `assets/audio/` for world and interface assets.
- `assets/credits/`, `assets/calibration/`, and `assets/evaluation/` for attribution and supporting evidence.
- `deploy/` for future public and offline deployment work.

**Evidence:** [`docs/repository-layout.md`](repository-layout.md).

**Status:** Layout created. Empty folders do not indicate implemented or validated components.

### Step 10 - Create decision and risk registers

**Work performed:**

- Added explicit statuses for the assay, dataset, cell-ID source, neural dynamics, sensory encoding, body representation, fly asset, software runtime, deployment, release scope, and licensing.
- Added next actions, owner roles, review timing, and block effects to the decision log. Named individuals remain to be recorded; 2026-11-08 is a proposed Phase 0 review date, not an agreed deadline.
- Added risk entries for snapshot mismatch, untraceable pathway, renderer/scripted action, biological overclaiming, asset rights/rig, unsupported sensory/body mappings, deployment/offline failure, and simple baselines succeeding without the intended cause.
- Added early signals, mitigations, and stop conditions for the risks.

**Evidence:** [`docs/decisions.md`](decisions.md), [`docs/risks.md`](risks.md).

**Status:** Registers are prepared. Owner identity, calendar date, and approval of proposal statuses remain open.

### Step 11 - Prepare the Phase 0 review gate

**Work performed:**

- Mapped P0.1 through P0.9 to the repository evidence and recorded which items are complete for the foundation versus proposal-only.
- Added review checkboxes for audience, device/browser, offline/public path, scope, architecture, ownership/review date, data stop condition, and asset status.
- Left owner name, review date, confirmation, blockers, Phase 1 decision, and signature blank.
- Set the explicit stop point: no Phase 1 work begins until the project owner records Phase 0 confirmation.

**Evidence:** [`docs/phase0-checklist.md`](phase0-checklist.md).

**Status:** Ready for owner review; not signed off.

## 5. Mapping to the Phase 0 guide's work groups

| Guide group | What the group requires | Work recorded in this repository | Status |
|---|---|---|---|
| A. Open the workspace | Choose root, inspect Git, preserve sources, index files, document purpose/run instructions, ignore generated output/secrets/raw data. | Active root and branch documented; source files (including revised blueprint) copied from Codex output locations and hashed; index added; README and `.gitignore` added. No application run command exists. | Foundation complete. |
| B. Project charter | Audience, setting, question, behavior, visitor controls, learning goal, and success statement. | Charter records all fields, with audience, setting, and device as working proposals. | Prepared; owner review pending. |
| C. MVP boundary | One loop, one visitor stimulus action, candidate intervention, repeatability, valid no-response, explicit exclusions. | Taste contact to proboscis output; no direct piloting; candidate silencing only after Phase 1; no-response preserved; future behavior list documented. | Written; not formally frozen. |
| D. Evidence and claims | Define evidence vocabulary and claim boundary; separate renderer controls; reserve run-record fields. | Definitions and display rules in `evidence-and-claims.md`; run-record fields and renderer boundary recorded. | Prepared. |
| E. Assay and dataset handoff | Name reference and candidate release; state snapshot status; assign mapping; set extraction stop condition and candidate measures. | Shiu et al. (2024) and FAFB v783 recorded as provisional candidates; exact methods/IDs/crosswalk unresolved; candidate metrics and controls listed; extraction blocked. | Handoff prepared; Phase 1 prerequisites unresolved. |
| F. Product and runtime | Device/browser, local/offline behavior, frontend/service shape, state flow, public/local boundary, data/secrets rules. | Proposed desktop/laptop/Chrome-or-Edge target, React/TypeScript/Vite/Three.js, Python API/WebSockets/worker, local fallback, public-hosting deferral, and data boundaries recorded. | Proposal; owner decision pending. |
| G. Fly asset | Record missing status, candidate route, permissions, fallback, owner/date, and asset-independent progress. | Missing/unverified status, unverified candidate lead, procedural fallback, intake checklist, owner role, and proposed review date recorded. | Route prepared; no asset cleared. |
| H. Repository structure | Create docs, data, graph, simulation, body, frontend, scenario, evaluation, assets, and deploy homes. | Required Phase 0 homes plus detailed asset subfolders created and documented. | Complete as scaffolding. |
| I. Decisions and risks | Explicit statuses, rationale, source, owner, next action, date, blocks, and mitigations. | Decision log and risk register created; workstream owner roles and proposed review date recorded. | Prepared; named owner and approval remain open. |
| J. Review and confirmation | Read records from repository, check targets, explain 60-second flow, name scientific status, resolve blockers, sign off. | Records and review checklist are present; Phase 0 gate and Phase 1 stop are explicit. Owner has not supplied confirmation. | Awaiting project-owner review. |

## 6. Mapping to the numbered P0.1-P0.9 targets

| Target | Evidence | Completion state |
|---|---|---|
| P0.1 Create implementation repository and record root, branch, local instructions | Existing Git root retained; root, `master`, no commit/remote, and absence of an app start command recorded in `README.md` and the checklist. | Done for the foundation. |
| P0.2 Preserve planning documents unchanged | All 5 planning files (including `neurofly_revised_blueprint.md`) plus the Phase 1 implementation guide are present, indexed in `docs/source-plans/SOURCE_INDEX.md`, and hashed in `SHA256SUMS.txt`. | Done. |
| P0.3 Write a one-page charter | Audience proposal, setting, research question, first behavior, visitor role, and success statement in `project-charter.md`. | Prepared; owner review pending. |
| P0.4 Freeze MVP boundary | The single behavior and deferred work are recorded in the charter and handoff. | Proposed; owner must confirm before it is frozen. |
| P0.5 Record public/local, browser, and device target | Desktop browser/recent laptop, Chrome or Edge, local fallback, and public-hosting deferral appear in `architecture.md`. | Recorded as proposals; owner confirmation pending. |
| P0.6 Create decision log | Required scientific, body, asset, runtime, licensing, and release topics have statuses and next steps. | Done for the foundation. |
| P0.7 Create risk register | Eight major risks have signals, mitigation, and stop condition. | Done for the foundation. |
| P0.8 Agree evidence vocabulary | Five evidence terms and product claim boundary are recorded. | Done as a working standard; owner approval pending. |
| P0.9 Create initial folder layout | Planned project and asset folders are present and listed in `repository-layout.md`. | Done as scaffolding. |

## 7. Decisions and open items

### Decisions recorded as proposals

- One shared 3D Habitat; taste contact to proboscis response as the MVP.
- Desktop mouse/keyboard on a recent laptop; Chrome or Edge as the browser candidates.
- Local-first development with an offline exhibit fallback; public deployment deferred until evidence gates pass.
- React/TypeScript/Vite/Three.js frontend and a separate Python/WebSocket simulation service as candidate shape.
- A procedural fly with a separately controlled proboscis as the fallback asset path.
- Shiu et al. (2024) as the reference candidate and FAFB v783 as the dataset candidate.

### Unresolved items with hard or phase-specific blocks

| Item | Next evidence/action | Block effect |
|---|---|---|
| Project owner name and explicit Phase 0 approval | Complete the confirmation record in `phase0-checklist.md`. | Phase 1 cannot begin until approved. |
| Primary audience, venue, device, browser, minimum display, offline need, public-hosting intent | Confirm or revise the charter and architecture proposals. | Blocks final product/runtime choices. |
| Reference assay methods and outcome | Read the paper and supplementary methods; write a source-backed assay. | Blocks final metrics, stimulus protocol, and circuit claim. |
| FAFB v783 compatibility with the reference snapshot | Verify official release and IDs; create a deliberate crosswalk or narrow the comparison. | Hard block on bulk download, extraction, and named cell claims. |
| Sensory/intermediate/motor cell IDs and edges | Trace stable IDs and document evidence/uncertainty. | Blocks selected subgraph and intervention target. |
| Neural equation and engine | Compare reference assumptions, then choose one engine and record parameters. | Blocks neural-runtime implementation. |
| Sensory encoder and body actuator map | Define contact, taste mapping, proboscis range/lag, and calibration. | Blocks integrated sensorimotor claims. |
| Fly asset and rights | Inspect the original source and actual model or use an original procedural fallback. | Blocks public use of the candidate asset. |
| Owner/review dates for each workstream | Record named owners and calendar review dates; 2026-11-08 remains proposed. | Blocks accountable phase handoff. |
### Preserved source packet

- `docs/source-plans/neurofly_complete_project_plan.md`
- `docs/source-plans/neurofly_revised_blueprint.md`
- `docs/source-plans/neurofly_implementation_planner.docx`
- `docs/source-plans/neurofly_environment_asset_planner.md`
- `docs/source-plans/neurofly_phase0_execution_guide.docx`
- `docs/source-plans/phase1-implementation-guide.md`
- `docs/source-plans/SOURCE_INDEX.md`
- `docs/source-plans/SHA256SUMS.txt`

### Scaffold folders

`data_pipeline/`, `subgraphs/`, `simulation/`, `body/`, `frontend/`, `scenarios/`, `evaluation/`, `assets/fly/{source,runtime,physics}/`, `assets/world/{source,runtime}/`, `assets/textures/source/`, `assets/ui/`, `assets/audio/`, `assets/credits/`, `assets/calibration/`, `assets/evaluation/`, and `deploy/`.

## 9. Work deliberately not performed in Phase 0

- No connectome archive or subgraph was downloaded, extracted, or bundled.
- No cell IDs, sensory pathway, motor neuron, or intervention target was asserted as verified.
- No Brian 2, rate model, or other neural engine was selected or implemented.
- No taste encoder, proboscis actuator, contact simulation, or body physics was implemented or calibrated.
- No fly asset was downloaded, licensed, rigged, or added.
- No frontend, API, WebSocket service, deployment workflow, or public site was implemented.
- No automated application tests were run because there is no application runtime in this Phase 0 scaffold.
- No Git commit or remote was created.

These limits keep the Phase 0 record aligned with the project evidence gates and prevent scaffolding from being mistaken for a working biological simulation.

## 10. Verification and review notes

- The four copied source files have SHA-256 matches against their originals.
- The current repository state is uncommitted on branch `master`; no remote is configured.
- The DOCX text and tables were extracted for reading. The packaged visual renderer could not run because `soffice.exe` was unavailable, so page layout was not reviewed.
- Application behavior is not verified because no application has been built in Phase 0.
- The proposed owner review date `2026-11-08` is not an agreed deadline; confirm or replace it.

## 11. Phase 0 owner walkthrough and signoff

Before confirming Phase 0, the owner should:

1. Read the charter and decide whether the audience, setting, and first demo target are right.
2. Confirm the taste-contact-to-proboscis scope and deferred behavior list.
3. Review the architecture proposal and select or defer the runtime, browser, hardware class, public-hosting, and offline decisions.
4. Review the Shiu/FAFB handoff and keep extraction blocked until Phase 1 resolves release compatibility and cell mapping.
5. Review the missing asset status and fallback; treat the etainproject lead as unverified.
6. Record a named owner and calendar review date for each remaining decision.
7. Complete the confirmation record in [`phase0-checklist.md`](phase0-checklist.md).

Phase 1 remains on hold until the owner records **Phase 0 confirmed** and explicitly approves the handoff. After that gate, Phase 1 begins with the assay methods and source-backed circuit/ID review; it does not begin with bulk data extraction.
