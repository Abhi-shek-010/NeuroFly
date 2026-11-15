# Phase 2 Implementation Guide: NeuroFly Habitat, Fly, and Environment

**Phase:** 2 — Asset triage and Habitat greybox  
**Guide status:** Ready for staged implementation  
**Active repository:** C:\Users\abhi0\Desktop\NeuroFly\NeuroFly  
**Guide owner:** NeuroFly project owner  
**Implementation rule:** Complete and review one stage at a time. Stop at each stage gate until the owner accepts its walkthrough and result record.

## 1. Purpose

Phase 2 creates the first usable NeuroFly Habitat: one compact, persistent 3D experiment world; a temporary procedural fly; a stimulus patch; a visible proboscis joint; and a reliable contact event. The result should be a functional greybox that later phases can connect to the selected neural and body models.

This phase does not establish biological realism, complete fly anatomy, a connectome pathway, neural behavior, or calibrated physics. Keep the scene’s measured inputs, project choices, debug controls, and display effects distinct.

## 2. Phase numbering and entry gate

The source plans use different phase numbers. This repository’s Phase 1 guide names this stage **Phase 2 — Asset triage and Habitat greybox**. Follow that name and sequence in this guide. Do not change the project’s phase numbering while implementing it.

Before implementing Phase 2:

- Confirm the Phase 1 owner gate has been completed and the current Phase 1 handoff names the contact point, visible body action, and unresolved/provisional dimensions.
- Read the current project charter, architecture, asset register, evidence vocabulary, risk register, and source asset planner.
- Confirm the active repository root. Do not initialize another repository or alter Git remotes.
- Inspect the actual frontend and asset folders before choosing file locations or assuming a runtime exists.
- Record the selected browser stack and any remaining owner decision. The architecture proposes React, TypeScript, Vite, and Three.js; use what is already established. If no runtime exists, document the proposed minimal setup in Stage 2A before adding dependencies.

The owner signed off Phase 1 on 2026-11-14 with a scope limitation. Phase 2 may build the Habitat, configurable contact/body proxies, procedural fly, scene, contact-event inspection, and asset triage using provisional dimensions.

Exact FAFB v783 cell IDs and pairwise edges remain unresolved until Phase 3. Do not implement neural integration, present a validated v783 pathway, or treat contact as a scientific neural/motor response in this phase. If a stage depends on any of these unresolved items, document the dependency and stop that work.

## 3. Product and scientific boundaries

Apply these rules in every stage:

1. Build one shared Habitat that later experiment presets can reuse.
2. The visitor operates the experiment by placing or activating stimuli. The visitor does not pilot the fly during a scientific trial.
3. Direct fly posing is available only in a clearly labeled developer/asset inspection mode.
4. The fly mesh is a visual representation. Contact geometry and any later physics body are separate representations with documented mappings.
5. The Phase 2 placeholder is a simplified visual aid. Do not label it as measured anatomy or a validated biomechanical fly.
6. A stimulus or contact event may be logged in Phase 2, but it must not directly create neural activity or trigger a scientific motor response.
7. Keep dimensions, coordinate transforms, and provisional assay values in a small configuration or documented contract. Do not duplicate constants throughout the application.
8. Do not add a new experiment behavior, neural engine, connectome download, or dataset extraction in this phase.
9. Preserve existing working files. Do not replace the project architecture or add packages without documenting why.
10. Do not add automated tests unless requested. Use existing checks when available and perform the manual acceptance walkthrough for the stage being implemented.

## 4. Stage sequence

| Stage | Name | Main result |
|---|---|---|
| 2A | Handoff and scene contract | Phase 1 requirements, repository implementation point, coordinate/scene/body/contact interfaces |
| 2B | World scale and coordinate map | Explicit world units, axes, origin, and configurable scale |
| 2C | Habitat greybox | Arena, perimeter, stimulus patch, lighting, camera views, and reset |
| 2D | Procedural fly placeholder | Simplified, readable body hierarchy with a separate head and proboscis pivot |
| 2E | Contact and body proxies | Geometric contact detector and documented timestamped event |
| 2F | Proboscis articulation and developer controls | Independent movement for inspection, unavailable in scientific trial mode |
| 2G | External asset and rights triage | Recorded keep/reject/defer decision; procedural fallback remains available |
| 2H | Integration review and handoff | Evaluated greybox, evidence packet, known limits, and next-phase handoff |

Stages 2B–2F are sequential. Stage 2G may be researched after 2A and may proceed alongside the greybox if it does not alter the implementation contract. Stage 2H follows the other work.

## 5. Required evaluation packet for every stage

For each completed stage, create both files:

- Walkthrough: docs/phase2/walkthroughs/stage-2x-walkthrough.md
- Results: docs/phase2/results/stage-2x-results.md

Replace 2x with the stage identifier, such as 2a or 2c. Create the folders when needed.

The walkthrough must tell a reviewer how to open and inspect the result, the exact controls or steps to follow, the expected visible outcome, how to reset, and any prerequisite. Do not invent a run command. Record the actual command only if one exists.

The results file must record:

- Stage name and completion status.
- Short description of what changed and why.
- Files and assets created or changed.
- Exact existing build/run/check commands used, or state that none were available.
- Manual acceptance items checked and their observed outcomes.
- Evidence paths and screenshots, if applicable.
- Known limitations, deviations, and unresolved issues.
- A clear recommendation: complete, rework required, or blocked.
- Confirmation that the next stage has not been started.

Store useful screenshots or captures under docs/phase2/results/media/. Use descriptive names such as stage-2c-habitat-overview.png. Screenshots supplement the walkthrough; they do not replace it. Do not claim a stage passed if the app could not be launched or the relevant behavior could not be observed.

## 6. Stage instructions and copy-ready agent IDE prompts

Run one stage prompt at a time. Attach this guide or ask the IDE agent to read it first. The agent must stop after producing that stage’s evaluation packet and wait for owner review.

### Stage 2A — Handoff and scene contract

**Goal:** Convert the Phase 1 handoff and existing project architecture into an implementation contract for the Habitat.

**Implementation steps:**

1. Inspect the repository and report the actual frontend/runtime state, asset folder state, and any existing scene code.
2. Read Phase 1 assay and handoff records, the architecture, asset register, evidence vocabulary, risk register, and environment asset planner.
3. Extract the agreed or provisional stimulus, contact location, visible body action, arena requirements, camera needs, and owner decisions.
4. Define the world origin, axes, units, fly root, visible body-part names, proboscis pivot, contact proxy, stimulus object, and event interface at a design level.
5. Separate scientific-trial controls from developer-only inspection controls.
6. Record which values are confirmed, provisional, and unresolved. Do not silently promote provisional Phase 1 numbers to measured facts.
7. Decide the smallest implementation location that fits the existing repository. If the app stack is absent or uncertain, record a recommendation and wait at the decision gate before adding dependencies.
8. Create docs/phase2/scene-contract.md and the stage walkthrough/results files.

**Complete when:** The repository entry point and implementation boundary are clear; the contract defines how the scene, fly, stimulus, contact event, and developer controls fit together; every unresolved requirement has an owner action or explicit provisional status.

**Agent IDE prompt:**

> Read docs/phase2/README.md and the current NeuroFly project documents. Implement only Stage 2A. Inspect the repository before choosing files or commands. Write docs/phase2/scene-contract.md with the confirmed, provisional, and unresolved Habitat requirements and the scene/body/contact interface. Do not add dependencies or implementation code if the runtime choice is unresolved. Produce the required Stage 2A walkthrough and results files, including the inspected repository state and any decision needed. Stop after Stage 2A and wait for review.

### Stage 2B — World scale and coordinate map

**Goal:** Make the Habitat’s spatial basis explicit and consistent.

**Implementation steps:**

1. Read the approved scene contract and identify any provisional dimensions.
2. Establish one coordinate convention: up axis, forward direction, world origin, fly facing direction, and units.
3. Put scale and transforms in a central configuration or clearly named module.
4. Define the arena boundary, ground plane, stimulus patch location, fly root, contact point, and proboscis pivot in that convention.
5. Add a development-only scale/axis aid if it helps inspection; keep it hidden from normal presentation.
6. Document coordinate conversion at any rendering boundary. Do not use millimetres as Three.js world units without an explicit conversion policy.
7. Create a compact diagram or table in docs/phase2/world-coordinate-map.md.
8. Produce the Stage 2B walkthrough and results files.

**Complete when:** Another contributor can place the fly, patch, and contact proxy from the document without guessing axes or units; changing a provisional dimension does not require hunting through unrelated rendering code.

**Agent IDE prompt:**

> Read docs/phase2/README.md and docs/phase2/scene-contract.md. Implement only Stage 2B. Establish and document the world origin, axes, units, scale conversion, and named positions for the arena, fly root, stimulus, contact point, and proboscis pivot. Keep provisional values configurable and label them. Add only the minimum scene support needed to show the map. Create the required Stage 2B walkthrough and results files with observed evidence. Do not proceed to Stage 2C.

### Stage 2C — Habitat greybox

**Goal:** Create a clear, compact experiment environment using simple geometry.

**Implementation steps:**

1. Implement the arena floor and visual boundary using the coordinate map.
2. Add a clearly visible stimulus patch with separate visual and interaction representations where appropriate.
3. Use neutral lighting and a restrained backdrop so the fly, patch, and proboscis remain easy to see.
4. Add overview, top, side, and close-up views if supported by the existing interface. Make camera reset predictable.
5. Keep scenery minimal. Any decorative prop must not imply an unmodeled sensory input or physical obstacle.
6. Make the world usable at the target desktop layout. Avoid building later experiment-specific scenery.
7. Add a small readout or debug display for current camera and scene state only if it helps inspection.
8. Capture at least one overview and one contact-region view for the evaluation packet.
9. Produce the Stage 2C walkthrough and results files.

**Complete when:** The fly location, patch boundary, and contact region are visible in the overview and close-up views; camera reset works; the scene can be reset to a documented initial state; visual props do not influence the modeled experiment.

**Agent IDE prompt:**

> Read docs/phase2/README.md, the scene contract, and the world coordinate map. Implement only Stage 2C. Build the simplest readable Habitat greybox with the arena, boundary, stimulus patch, basic lighting, and available camera views. Keep decorative objects out unless they have a documented purpose. Capture overview and close-up evidence. Create the required Stage 2C walkthrough and results files with exact navigation/reset steps and known limitations. Stop before changing the fly model or contact logic.

### Stage 2D — Procedural fly placeholder

**Goal:** Add an original, lightweight fly-like visual model that supports the MVP’s required display.

**Implementation steps:**

1. Inspect existing assets and the asset register before creating duplicates.
2. Use procedural geometry or a small original mesh for the temporary model. Keep it visually cautious and clearly simplified.
3. Build a stable hierarchy with a root, thorax/body, head, abdomen, wings, legs, and proboscis group as needed for the selected view.
4. Give each independently relevant part a clear name. The proboscis must be a child of its own pivot, not merged into the head mesh.
5. Set origin, facing, scale, and pose from the coordinate map.
6. Keep the model source under the appropriate placeholder/source path and the runtime representation under the runtime asset path if the project’s asset conventions support both.
7. Add no biological detail that the project cannot support. Static legs or wings are acceptable for this phase.
8. Record the model as a temporary procedural visual asset in docs/asset-register.md.
9. Capture the fly from overview and macro views. Produce the Stage 2D walkthrough and results files.

**Complete when:** The placeholder is recognizable in the Habitat; it faces the documented direction; its body parts are inspectable in the scene hierarchy; the proboscis can be moved independently by its pivot; it is recorded as a simplified placeholder and not a validated fly model.

**Agent IDE prompt:**

> Read docs/phase2/README.md, the scene contract, coordinate map, and docs/asset-register.md. Implement only Stage 2D. Create a simple procedural fly placeholder with named body groups and an independent proboscis pivot. Match the documented scale, origin, and facing direction. Do not download or copy an external model and do not claim anatomical or biomechanical accuracy. Update the asset register and create the required Stage 2D walkthrough and results files with screenshots and the visible limitations. Stop before implementing contact detection.

### Stage 2E — Contact and body proxies

**Goal:** Represent the contact region independently of the rendered surface and record contact transitions reliably.

**Implementation steps:**

1. Define the labellar/contact proxy in the scene contract and place it using the coordinate map.
2. Add a separate interaction shape for the taste patch.
3. Implement the smallest suitable geometric overlap check for the existing runtime. Do not introduce force-based physics unless already selected and necessary.
4. Emit a timestamped contact-on and contact-off event only when the overlap state changes. Avoid emitting repeated onset events every frame.
5. Include stimulus identity/condition, contact location or proxy identity, trial time, and whether the event came from a manual fixture or geometry check.
6. Provide a development-only debug view to display the interaction shapes. Keep it out of the normal visitor view.
7. Ensure visitor actions operate on the stimulus or trial, not on direct fly motion. If a test fixture moves the patch or fly directly, label the fixture and keep it out of scientific trial mode.
8. Do not connect the event to a sensory neuron or neural model in this stage.
9. Produce the Stage 2E walkthrough and results files, including evidence for onset, sustained contact, release, and reset.

**Complete when:** The proxy and patch interaction boundaries are inspectable; contact onset and offset are recorded once per transition with consistent trial time; reset clears prior contact state; no neural or motor response is triggered by this event in Phase 2.

**Agent IDE prompt:**

> Read docs/phase2/README.md, the scene contract, coordinate map, and the current Phase 2 scene. Implement only Stage 2E. Add a distinct contact proxy and stimulus interaction shape, then record contact onset/offset transitions with trial time and event provenance. Use geometric overlap or the already selected simple interaction method; do not add a new physics engine. Keep debug shapes optional and do not connect contact to neural activity or fly behavior. Create the required Stage 2E walkthrough and results files showing contact onset, continued contact, release, and reset. Stop after Stage 2E.

### Stage 2F — Proboscis articulation and developer controls

**Goal:** Make proboscis movement inspectable without turning direct posing into a scientific-trial input.

**Implementation steps:**

1. Confirm the independent pivot from Stage 2D and its angle/extension convention.
2. Use the Phase 1 handoff’s output range if confirmed. Otherwise keep the range configurable and visibly provisional.
3. Add a developer-only pose control with resting, intermediate, and maximum positions.
4. Verify visually that the head remains still, the proboscis rotates or extends around the correct pivot, and the contact proxy follows the intended contact point.
5. Add a reset-to-rest action. Avoid a hidden automatic animation or any action triggered by stimulus selection.
6. Ensure the pose control is unavailable in visitor scientific-trial mode, or place it in a clearly isolated development panel.
7. Record the render-pivot/contact-proxy relationship and current limits in the scene contract or body mapping note.
8. Produce the Stage 2F walkthrough and results files.

**Complete when:** The proboscis can be inspected across its documented range and reset; the head does not move with it; the proxy remains aligned; developer posing is clearly separated from the experiment flow; no claim is made that a neural output drives the motion yet.

**Agent IDE prompt:**

> Read docs/phase2/README.md, docs/phase2/scene-contract.md, the coordinate map, and the Phase 2 fly implementation. Implement only Stage 2F. Add a clearly labeled developer-only control for the independent proboscis pivot, using confirmed or configurable provisional limits. Keep the contact proxy aligned and provide a reset-to-rest action. Do not add stimulus-triggered animation or claim neural control. Create the required Stage 2F walkthrough and results files with observations at rest, intermediate pose, maximum pose, and reset. Stop after Stage 2F.

### Stage 2G — External asset and rights triage

**Goal:** Decide whether any external model or environment asset is suitable, while keeping the procedural fallback available.

**Implementation steps:**

1. Review the current asset register and original asset planner.
2. Inspect the exact candidate source page and exact license or purchase terms for any asset considered. Record the creator, title, source URL, license name/link, attribution, modification rights, redistribution rights, and review date.
3. Assess whether the actual files provide the scale, orientation, mesh organization, and independent proboscis pivot the MVP needs. A preview image is not proof of rigging or permission.
4. Inspect files already present locally before proposing a new import. Do not overwrite or delete the procedural fallback.
5. Mark each candidate accepted, rejected, or deferred and give the reason. If rights or rig suitability is uncertain, do not place it in the public runtime.
6. Do not download or commit a candidate unless the source and terms are verified and the project owner has approved that asset intake.
7. Produce the Stage 2G walkthrough and results files with the register and evidence links.

**Complete when:** The asset register contains a source-backed decision for each candidate considered; unclear candidates remain excluded; a usable placeholder remains available; attribution and redistribution requirements are visible.

**Agent IDE prompt:**

> Read docs/phase2/README.md, docs/asset-register.md, and the original environment asset planner. Implement only Stage 2G. Inspect and document candidate asset provenance, license, redistribution/modification rights, rig structure, scale, and suitability for the independent proboscis pivot. Do not rely on preview images as proof, do not download or commit an asset before its terms are verified and owner approval is recorded, and preserve the procedural fallback. Create the required Stage 2G walkthrough and results files. Stop after the asset decision.

### Stage 2H — Integration review and handoff

**Goal:** Review the Phase 2 Habitat as one coherent, evaluable greybox and prepare the next-phase handoff.

**Implementation steps:**

1. Inspect the complete Phase 2 scene and current repository state.
2. Follow the walkthrough from a clean launch/reset through overview, close-up, stimulus placement/activation, contact inspection, developer-only pose inspection, and reset.
3. Check that visible and interaction representations agree at the contact point and proboscis pivot.
4. Confirm visitor experiment controls do not directly pilot the fly or select the proboscis action.
5. Confirm no connectome data, neural activity, or biological pathway claim has been added to the greybox.
6. Run only existing build/validation commands if available. Record commands and results; do not add tests.
7. List visual and interaction limitations, unresolved owner decisions, and any asset licensing conditions.
8. Update docs/phase2/README.md stage status and repository links. Do not mark Phase 2 complete until the owner reviews this evaluation packet.
9. Produce the Stage 2H walkthrough and results files with screenshots of the overall scene and contact close-up.

**Complete when:** The Habitat opens and resets reliably using the actual project workflow; all prior stage evidence exists; required manual checks are recorded; limitations are explicit; the owner can evaluate the scene from the walkthrough and results packet.

**Agent IDE prompt:**

> Read docs/phase2/README.md and every completed Phase 2 stage result. Implement only Stage 2H integration fixes required to meet the Phase 2 gate. Walk through launch/reset, scene views, stimulus interaction, contact logging, developer-only pose inspection, and reset. Run only existing validation commands and record their actual outcomes. Do not add tests or connect neural behavior. Create the required Stage 2H walkthrough and results files, update the Phase 2 index, list remaining limitations, and stop for owner review.

## 7. Phase 2 completion gate

Phase 2 is ready for owner review when:

- The Habitat has a documented coordinate system and configurable provisional dimensions.
- The arena, stimulus patch, placeholder fly, and intended contact region are visible.
- The procedural model has a separate, inspectable proboscis pivot.
- Contact events can be observed and reset without directly activating neural or motor behavior.
- Scientific-trial controls and developer-only pose controls are clearly separated.
- External assets are either documented and approved or deferred; the procedural fallback remains intact.
- Each completed stage has a walkthrough and results file, with visual evidence where useful.
- The final report states what was observed, what was not verified, and which claims remain out of scope.

After Stage 2H, stop. Do not start the data pipeline, download BANC/FAFB data, implement the neural engine, or claim a completed connectome-driven behavior until the owner reviews the Phase 2 packet and the relevant later-stage plan.

## 8. Overall Phase 2 agent IDE prompt

Use this only to ask an IDE agent to plan or begin Phase 2. For implementation, replace the final instruction with one stage prompt above.

> You are working on NeuroFly in C:\Users\abhi0\Desktop\NeuroFly\NeuroFly. Read this guide, applicable AGENTS.md instructions, the project charter, architecture, Phase 1 handoff, evidence vocabulary, risks, asset register, and original environment asset planner. Confirm the repository root and actual implementation state before making changes. Phase 2 is the shared Habitat greybox and asset stage. Preserve the connectome-constrained virtual fly framing; visitors operate experiments, while direct fly posing is developer-only. Keep the visible mesh separate from contact/physics proxies. Use a simplified procedural placeholder until an external model has verified rights and technical suitability. Keep provisional dimensions configurable. Implement only the explicitly selected Stage 2A–2H; do not continue to the next stage. For that stage, update only necessary project files and produce both docs/phase2/walkthroughs/stage-2x-walkthrough.md and docs/phase2/results/stage-2x-results.md, including observable outcomes and evidence. Run only existing validation commands, add no tests, report limitations honestly, and stop for owner review.
