# NeuroFly World and Asset Planner

**Version:** 1.1  
**Prepared:** 1 November 2026  
**Purpose:** Turn the shared 3D NeuroFly Habitat idea into a concrete world layout, asset specification, sourcing plan, and build sequence.

## 1. Recommended concept

Build one compact, persistent 3D world called the **NeuroFly Habitat**. It should feel like a polished indie-game exhibit, while keeping the experiment itself controlled and scientifically legible.

Use a central miniature habitat on a clean laboratory stage. Experiment modes reconfigure that habitat with a selected surface, landmark, odor field, looming object, or other stimulus module. The fly, camera system, controls, neural display, and run history stay consistent. A later mode can have its own visually distinct corner or backdrop when its stimulus needs one, while still using the same world and experiment framework.

This is the best balance for the project because it gives judges one memorable place to explore, lets visitors compare experiments without learning a new interface, and avoids spending early effort on several disconnected scenes. It also makes the scientific comparison fairer: the same fly model, scale, control logic, camera, and record of what happened carry from one mode to another.

### Design decisions to keep

- **The visitor operates an experiment; they do not pilot the fly.** Visitors place or trigger a stimulus. The modeled sensory and neural pathway drives the action. A separate, clearly labeled developer mode can directly pose the body for asset checks.
- **The first playable setup is taste contact to proboscis response.** Build the world around a small controlled food or taste patch, the fly’s contact points, and a clearly visible proboscis response. Confirm the biological cell set and pathway from the chosen connectome and literature before naming any neurons or claiming that a circuit is complete.
- **Keep one source of action.** Stimuli enter the sensory model; neural activity produces motor signals; the body model turns those signals into motion. Animation can make that motion readable, but must not choose the behavior on its own.
- **Make the evidence visible.** Every run should show the stimulus, sensory input, activity in the modeled circuit, motor output, body motion, and a timeline. Label which values come from the data, which are model assumptions, and which are display effects.
- **Add modes as experiment presets, not unrelated minigames.** Each preset defines its starting state, stimulus modules, trial duration, control panel, and measured outcomes.

## 2. World concept and screen composition

### The NeuroFly Habitat

The scene is a clean tabletop or microscope-stage environment with one compact “slice” of fly-scale habitat. Use a restrained, warm palette for the arena and a cooler, precise palette for the laboratory controls. Keep enough natural texture to make the fly’s surroundings feel inhabited, but remove visual clutter that hides the fly or stimulus.

A practical first scene has:

1. **Central arena:** a shallow, softly textured ground surface with room for one fly, a taste patch, and simple approach paths.
2. **Perimeter rail:** a visual boundary that makes the experimental area understandable and keeps future modules neatly framed.
3. **Stimulus station:** a small sugar/taste patch in the first mode, with an optional nearby control marker showing where and when stimulus is active.
4. **Context props:** a few restrained scale cues such as a leaf edge, seed, or lab marker. These are visual framing objects, not unexplained inputs to the model.
5. **Lighting and backdrop:** a broad soft key light, gentle fill, and neutral background that preserve wing, leg, and proboscis contrast.
6. **Scientific overlays:** optional contact point markers, a scale ruler, direction arrows, odor concentration view, and a neural pathway highlight. Each overlay can be turned off.

### Suggested screen layout

- **Main canvas:** the 3D arena occupies most of the display. The fly should remain the visual focus during a run.
- **Top strip:** experiment name, trial number, run/pause/reset, and a clear indication of the current model/data version.
- **Left tool dock:** experiment-specific stimuli and interventions, such as “place taste patch,” “change concentration,” or “start trial.” Disabled tools remain hidden or visibly unavailable.
- **Right readout:** a compact causal chain with sensor input, active modeled neurons or circuit groups, motor command, and current behavior state.
- **Bottom timeline:** stimulus onset, contact, neural activity, action onset, and trial end. Add replay and run comparison after the first loop is reliable.
- **Camera controls:** orbit, pan, zoom, reset view, top view, side view, and fly-eye view. A close-up can show contact and proboscis movement; an overview can show the arena and trajectory.

Desktop mouse/keyboard interaction should work first. Touch controls can follow once the desktop layout is stable. Keep critical controls as real interface components rather than painting labels into textures, so they remain readable, accessible, and easy to revise.

### Run flow

Visitor chooses an experiment preset  
→ the world loads its specified initial state  
→ visitor applies the stimulus  
→ sensory input is calculated from the stimulus and contact/position  
→ the neural model updates  
→ the motor interface produces body commands  
→ the body visibly moves  
→ the timeline and result panel record the event.

If any link is missing, display the run as an animation or plumbing prototype rather than as a neural behavior result.

## 3. Experiment modules and what each requires

| Module | World pieces | Visitor action | Fly response to show | Evidence to record |
|---|---|---|---|---|
| **1. Taste contact and proboscis response — MVP** | Neutral ground, patch with clear boundary, contact marker, optional sugar/bitter condition selector | Place or activate a taste patch, then run a trial | Approach/contact is a separately validated phase; the MVP response is driven extension, hold, or retraction of the proboscis where supported by the model | Contact time, taste input, modeled circuit trace, motor command, proboscis angle/state, response latency |
| **2. Food encounter and stopping** | Food object/patch, approach path, simple locomotion region | Place food or vary its state | Stop or slow, investigate, feed, depart, as supported by the motor pathway | Position/speed, contact, feeding state, timing, internal-state assumptions |
| **3. Heading and landmark use** | High-contrast landmark(s), compass ring, controllable orientation, optional light cue | Rotate or move a landmark | Turn or maintain heading only when the selected circuit and body interface support the behavior | Landmark angle, orientation error, neural trace, turn command, heading over time |
| **4. Odor-guided search** | Odor source, visible plume overlay, configurable airflow arrows, bounded arena | Move the source or alter wind/odor settings | Search turns and progress depend on modeled olfactory input and the selected locomotor controller | Odor field at fly, wind, trajectory, sensor input, turn/speed outputs |
| **5. Looming visual stimulus and escape** | Approaching disk or shadow card, safe test lane, speed control | Set looming size/speed and start the trial | An escape-like motor response, only after the mapped visual input and body controller are connected | Stimulus expansion, visual input, neural activity, escape latency and trajectory |
| **6. Grooming sequence** | Simple stationary perch/ground, close camera, optional dust marker | Apply a light grooming trigger if supported by the model | Grooming limb sequence from a motor command or a validated body controller | Trigger, active neural groups, limb sequence, timing |
| **7. Associative odor learning — later research goal** | Two odor sources, configurable paired/unpaired cue timing, trial/recovery controls | Select a training protocol and run repeated trials | A change in modeled response after training, only if the plasticity mechanism is explicitly implemented and evaluated | Trial-by-trial response, pairing schedule, model state changes, controls and replicates |

The world can present all of these as future presets, but the first implementation should complete one causal loop before building all the scenery. The full-project plan identifies taste-to-feeding as the first vertical slice and adds other modes incrementally.

## 4. Asset specification

### A. Hero fly model — critical path

The attached image shows a detailed textured fly model preview and an export menu. It does not reveal whether the exported model has a skeleton, meaningful joint pivots, or usable animations. Those need to be confirmed from the actual downloaded file.

**Preferred web runtime file:** GLB, the binary form of glTF. Khronos describes glTF as a runtime 3D asset format, and Three.js provides a GLTFLoader that loads glTF/GLB scenes and exposes animations. This aligns with the planned Three.js browser world. [Khronos glTF specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html), [Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html), [Three.js model-loading guide](https://threejs.org/manual/pages/loading-3d-models.html)

**Ask the model creator for:**

- A GLB export with materials and textures included.
- The editable source file, preferably Blender (.blend), if they are willing to share it.
- A note on whether the model is rigged, whether it includes animations, and which body parts/bones are separate.
- The exact license or purchase terms and the original model page.
- A screenshot of the rig or a short turntable clip if the model page does not make its structure clear.

**Anatomy and motion structure to inspect:**

- Body groups: head, thorax, abdomen, left/right wings, antennae, proboscis, and six legs.
- Skeleton or pivot groups with clear root, head, thorax, abdomen, wing, antenna, proboscis, and leg-joint names.
- Leg pivots that allow visible stance, swing, and contact. The first sandbox especially needs feet/tarsi and proboscis contact to be legible.
- Proboscis geometry that can extend/retract or rotate without deforming the whole head.
- Wing geometry that can be animated or held still. Do not imply flight until flight dynamics and its neural/body control are in scope.
- UVs and physically based materials that retain the fly’s silhouette under the target lighting.
- Correct outward normals, no hidden missing textures, and a useful model origin at the body root.

If the model has no rig, it can still be useful for a turntable, an initial scene, or a static reference. It cannot by itself support convincing neural-driven leg or proboscis movement. In that case ask for a rigged export, rig it in Blender, or use a simpler custom model for the MVP while preserving the detailed model for the exhibit’s close-up view.

**Important:** an attractive animation supplied with an asset is not evidence that the modeled circuit produced that action. The animation can be used as an art reference or for a loading/idle presentation; experiment motion must be driven by model outputs.

### B. Shared environment pieces

| Asset group | Needed for | Suggested starting approach | Runtime form |
|---|---|---|---|
| Arena ground and perimeter | Establishes one contained, repeatable experiment space | Simple custom mesh with one or two materials; use modest texture detail | GLB or procedural geometry |
| Taste/food patches | Defines the first stimulus and later food encounter | Custom mesh/material variants for conditions; expose stimulus state in data, not just color | GLB or procedural geometry plus app state |
| Odor source and plume | Odor search | Source prop plus plume visualization generated from the model’s odor field; arrows are a separate wind display | GLB source, procedural shader/particles for field |
| Visual landmarks | Heading experiments | Simple distinctive shapes with controllable rotation/position | GLB or procedural geometry |
| Looming card/object | Escape experiment | A simple plane/disc that can move toward the fly according to trial parameters | Procedural geometry |
| Perch/leaf/obstacles | Grooming and locomotion | A few high-contrast props with collision/contact markers only when their physical effect is modeled | GLB or procedural geometry |
| Stage, backdrop, lab frame | Makes the exhibit look finished | Mostly static; avoid competing with the animal | GLB or procedural geometry |
| Contact and scale markers | Scientific clarity | UI overlays or thin lines generated from known scene positions | SVG/canvas overlay or procedural lines |

Use procedural geometry for basic surfaces, patches, arrows, and looming shapes if that makes the experiment easier to control. The more important task is a reliable stimulus and contact model, not a high-detail sugar grain.

### C. Visual science overlays

These are dynamic explanatory layers rather than decorative art assets:

- **Trajectory trace:** the fly’s measured body-root path with a time scrubber.
- **Sensor/contact markers:** show when and where the modeled input is sampled.
- **Odor concentration field:** a labeled heatmap or particles driven by the same field used by the neural model.
- **Neural pathway view:** highlight only the selected circuit, with data version and scope stated.
- **Motor output indicator:** a small chart, vector, or joint-state panel linked to the body controller.
- **Trial timeline:** cues, contact, response onset, and end state share one time base.
- **State badges:** “simulated,” “recorded reference,” “visualization,” and “debug” should be visually distinct.

Avoid decorative glowing nerve lines unless they map to actual selected nodes/edges and their activity. A glowing pathway should be a view into the selected circuit, not a decorative claim of full-brain activity.

### D. Interface and sound assets

- Build the control dock, readouts, plot, timeline, and settings as application UI. Use original vector icons or a consistent open-licensed icon set.
- Supply logos and illustrations as SVG or transparent PNG; keep text and labels as live text.
- Make interaction states clear: idle, selected, active, unavailable, recording, and error.
- Optional audio: a quiet room tone and subtle response cues can add polish, but do not use sound as a hidden substitute for a visible model state. The entire demo should work muted.
- Any font, icon, sound, or illustration used in a public build needs a recorded source and license.

### E. Physics and calibration artifacts

Plan for two separate fly representations if the project uses a detailed body-physics model:

- **Visible fly:** the GLB rig used by Three.js for the public 3D world and close camera views.
- **Physics fly:** the body, joint, contact, and environment representation used by MuJoCo/FlyGym or another selected physics system. It may use its own model files and is not automatically a browser GLB.
- **Mapping record:** a documented table linking physics body state and actuator outputs to visible GLB joints. Keep names, units, coordinate axes, scale, and sign conventions explicit.

NeuroMechFly/FlyGym is a strong locomotion and contact reference, but the first taste response needs proboscis extension, hold, retraction, and contact. Confirm those actuators exist before relying on that body; plan a small custom extension if they do not.

Treat these simulation artifacts as versioned project assets alongside the models:

- Proboscis motor-output-to-angle/extension curve, lag, contact threshold, and return behavior for the first experiment.
- For later walking, a measured actuator grid for forward speed, lateral slip, yaw, ground contact, and gait variability.
- Reference traces from the full physics run and fixed examples for checking browser output.
- If needed, a compact surrogate lookup/model calibrated from those traces, with its validity range and version.
- Held-out trial seeds and baseline outcomes for no-sensory, no-contact, always-respond, and simple-rule controls.
- Documented ranges for measured sensory noise, contact timing, actuator lag, and gait variability used in robustness checks.

Store curves and mappings in a documented table or structured format such as JSON, CSV, or NPZ. Preserve source, units, model version, calibration method, and provenance. Label the browser surrogate as **Interactive Preview** and physics results as **Reference Run**; report their scores separately.

## 5. What the export options in the image are for

- **GLB:** recommended first choice for this Three.js web project. It packages a glTF scene into one binary file and can carry meshes, materials, textures, a rig, and animation data.
- **FBX:** useful as a DCC interchange file when the creator’s animation or rigging pipeline uses it. If it is what the creator offers, import it into Blender, inspect it, then export a tested GLB for the web runtime.
- **OBJ:** suitable mainly for static mesh exchange. It is not the format to request for a rigged, animated fly.
- **USD:** useful in some advanced content-creation pipelines and scene interchange. It is not the simplest first runtime asset for this planned browser app.
- **STL and 3MF:** primarily for 3D printing. They do not preserve the game-ready material, rig, and animation setup needed here.

The screenshot’s highlighted GLB option is therefore the right export button to try first. Keep the editable source and any original texture files too. If the resulting GLB is static or missing materials, the original source can help repair it.

## 6. Asset sourcing plan

### Preferred starting sources

- **Your fly model:** use the page or store from which the pictured model comes. Verify that you can use the actual model file in a public browser project, not only view or print it. The visible export menu does not tell us its license or whether the file includes a rig.
- **FruitFlyBrain as an engineering reference:** study its body calibration, browser surrogate, held-out evaluations, and realism audit. Its public playground is a 2D canvas surrogate, useful for control/readout ideas but not a ready-made 3D scene or art asset. Its locomotion system uses the NeuroMechFly v2 body with MuJoCo/FlyGym; treat that as a physics/code reference rather than assuming it is a ready-to-drop-in GLB or a gustatory/proboscis asset. [Project 09 README](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/README.md), [browser playground](https://rohitcraftsyt.github.io/FruitFlyBrain/projects/09_flylab/playground/), [realism audit](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/REALISM_AUDIT.md)
- **Poly Haven:** useful for background HDRIs, textures, and general props. Its current license page states that its assets are shared under CC0. [Poly Haven license](https://polyhaven.com/license)
- **Kenney:** useful for placeholder props, buttons, cursor prompts, and some UI/game assets. Kenney’s support page says game assets on its asset pages are public domain/CC0; still retain the specific pack’s license file. [Kenney support and license guidance](https://kenney.nl/support)
- **Sketchfab:** useful for discovering or buying specialized insect/food/environment models. Check the exact asset’s license and the permitted use in a public browser app; the platform’s license agreement includes restrictions against making licensed material available as a standalone downloadable asset. [Sketchfab license agreement](https://sketchfab.com/licenses)
- **Original assets:** best for the signature fly, scientific overlays, project mark, and distinctive interface. These assets will make the exhibit feel like NeuroFly rather than a collection of stock packs.

Prefer CC0 or commissioned assets when possible for files that must ship with the public app. Keep attribution-required assets in an attribution list and add readable credits to the project. “Free download” is not the same as a license to publish in a public app.

### Sourcing rules

1. Save the asset’s source page, creator name, license name, and license URL at acquisition.
2. Keep the source download unchanged in an archive; work on a duplicate.
3. Check whether redistribution, modification, and public web embedding are allowed.
4. Do not commit a paid asset or a high-resolution source file into a public repository unless its license allows that distribution.
5. If a model license allows use in a rendered project but restricts extraction or standalone redistribution, assess whether shipping the GLB in a public web app is allowed before using it.
6. Use original or explicitly reusable models for any asset whose rights are uncertain.
7. Ask me to inspect the model page and files before we commit to an asset pipeline.

## 7. File formats and project organization

| Content | Authoring/source file | Web/runtime file |
|---|---|---|
| Fly model | Blender file or licensed creator source | GLB |
| Modular environment props | Blender file or original source format | GLB, or generated procedural geometry |
| PBR texture maps | PNG/TIFF source maps | Optimized image format supported by the app; consider KTX2 after a tested loader path |
| UI icons and logos | SVG source | SVG or raster PNG where appropriate |
| UI layout and screens | Figma/design source, if used | React/CSS components |
| Short sound effects | WAV source | compressed web audio format chosen during implementation |
| Neural and behavior data | CSV/Parquet/JSON plus provenance | compact, versioned JSON/binary data selected by the runtime architecture |
| Body calibration and render-to-physics mapping | CSV/JSON/NPZ plus units, version, and provenance | compact calibration data consumed by the simulator/renderer |
| Surrogate reference vectors and held-out trial seeds | JSON/CSV/NPZ plus expected outputs and split description | small fixtures for parity and reproducibility checks |
| Credits and rights | source URLs, licenses, receipts/permissions | machine-readable manifest plus visible Credits page |

Suggested logical asset areas:

- assets/fly/source
- assets/fly/runtime
- assets/fly/physics
- assets/calibration
- assets/evaluation
- assets/world/source
- assets/world/runtime
- assets/textures/source
- assets/ui
- assets/audio
- assets/credits

The source and runtime folders are conceptual organization; actual repository paths can be adapted to the implementation plan. Keep the runtime build lean and preserve original source files outside the public web bundle when their license or size makes that appropriate.

## 8. Starter quality and performance targets

These are initial working targets, not measured guarantees. Profile a real representative scene before publishing a frame-rate promise.

- Fly: one hero model, moderate mesh density, one or two 2K texture sets to begin; use 4K only if a close-up proves the detail is needed.
- Static scene: reuse materials and meshes; avoid large numbers of individually animated props.
- Effects: keep odor, activity, and trajectory views opt-in; provide a simpler reduced-motion/reduced-detail mode.
- Delivery: keep the first downloadable scene as small as practical; compress textures/geometry only after verifying the model still loads and looks correct on the intended browser.
- Performance target: smooth interaction on an ordinary recent laptop, then check a lower-power device. Record browser, device class, load time, and frame rate for the demo setup.
- Accessibility: allow pause, reset, keyboard operation for main actions, adequate text contrast, and reduced motion.

## 9. Build sequence and acceptance checks

### Stage 1 — Greybox the arena

Use simple geometry and a placeholder fly. Implement orbit/zoom, run controls, stimulus position, and a visible trajectory.

**Accept when:** a visitor can identify the fly, stimulus, active mode, and run state without explanation; the scene loads reliably and reset returns it to the same initial conditions.

### Stage 2 — Import and inspect the hero fly

Load the GLB in the actual Three.js page. Check size, orientation, materials, textures, pivot, skeleton, and animation list. Keep a static thumbnail/model viewer as a fallback while the rig is being prepared.

**Accept when:** the fly faces the expected direction, stays framed at the expected scale, has no missing textures, and all required joints/contact parts can be located. Document any missing rig features.

### Stage 3 — Connect control to body

Drive a small number of visible joint states from a test motor command. Use an explicit debug panel so art/rig issues can be isolated from the neural model.

**Accept when:** a displayed motor value produces a repeatable and reversible corresponding joint movement, the actuator mapping is recorded, and no hidden animation selects the action.

### Stage 4 — Build the taste-contact module

Add the patch, contact sensing, taste condition control, trial timeline, and first verified pathway. Keep approach behavior out of scope if it is not yet generated by the model; provide a clear start position so the first experiment can focus on the response.

**Accept when:** a run shows stimulus timing, sensor input, circuit activity, motor command, and proboscis/body response on one time base. No-contact, no-sensory, always-respond, and intervention controls establish whether the intended causal path matters.

### Stage 5 — Add replay and comparison

Save experiment settings and version identifiers so the user can reproduce a run. Add a baseline-versus-intervention comparison.

**Accept when:** the same saved run can be replayed, and comparisons show which parameters changed.

### Stage 6 — Add modes one at a time

Reuse the same arena and interface. Add a new prop only with its sensory field, model input, body response, and evidence display specified.

**Accept when:** each new module has its own experiment definition and passes the same reset, reproducibility, provenance, and causal-link checks as the MVP.

## 10. Asset intake checklist for anything you send

For each asset, send any combination of:

- Direct source page or creator name.
- Downloaded file(s), if the license permits sharing them here.
- Format, such as GLB, FBX, OBJ, blend, SVG, PNG, or WAV.
- License text or a screenshot/link to its license.
- What you want it to do in the scene.
- For models: whether it is rigged, animated, textured, and which components must move.
- For templates: whether it is inspiration, editable design source, or a finished UI.
- Any restrictions, attribution text, purchase proof, or creator instructions.

For the pictured fly, the most useful next handoff is the **GLB file plus the original model/source page and license**. If the GLB has no skeleton, provide the editable source or request a rigged version. I can then check its structure and tell you whether it is ready for the MVP, needs cleanup, or should be reserved for a static close-up.

## 11. Project continuity and how to start 

Suggested project instruction:

> We are building NeuroFly, an interactive browser-based fly connectome exhibit. Preserve the decisions in the project plan and decision log. The product is one shared 3D NeuroFly Habitat with modular experiment presets, starting with taste contact to proboscis response. Keep the visitor in the role of experiment operator, not fly pilot. Be explicit about which pathways, neurons, outputs, and behaviors are verified, modeled, visualized, or still future work. Do not claim the whole biological brain is simulated. Keep connectome dynamics separate from learned-control baselines. Before adding a visual or behavior, state what stimulus drives it, what neural/body model drives it, and what evidence the interface will show. Label browser previews and reference physics runs separately. Use the asset planner and record source, license, format, rig/animation state, and intended use for every external asset.

## 12. References

- [ChatGPT Projects and chats](https://learn.chatgpt.com/docs/projects)
- [FruitFlyBrain Project 09 README](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/README.md)
- [FruitFlyBrain browser playground](https://rohitcraftsyt.github.io/FruitFlyBrain/projects/09_flylab/playground/)
- [FruitFlyBrain realism audit](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/REALISM_AUDIT.md)
- [FruitFlyBrain dataset provenance](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/datasets/README.md)
- [Khronos glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
- [Three.js GLTFLoader documentation](https://threejs.org/docs/pages/GLTFLoader.html)
- [Three.js loading 3D models guide](https://threejs.org/manual/pages/loading-3d-models.html)
- [Blender glTF import/export manual](https://docs.blender.org/manual/en/4.0/addons/import_export/scene_gltf2.html)
- [Poly Haven license](https://polyhaven.com/license)
- [Kenney support and asset licensing](https://kenney.nl/support)
- [Sketchfab license agreement](https://sketchfab.com/licenses)
- [NeuroFly complete project plan](neurofly_complete_project_plan.md)
