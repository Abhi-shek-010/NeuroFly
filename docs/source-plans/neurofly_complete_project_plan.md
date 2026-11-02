# NeuroFly: Complete Project Plan

**Plan date:** 1 November 2026  
**Project category:** Connectome-constrained NeuroAI, embodied agent simulation, interactive science demonstration  
**Product form:** One shared 3D NeuroFly Habitat with experiment modes  
**Recommended first behavior:** Taste contact → feeding-related neural activity → proboscis response

## 1. Executive summary

NeuroFly is a virtual adult fruit fly whose selected neural circuits are built from a documented Drosophila connectome. The fly inhabits one interactive 3D world. Visitors change the world with experimental stimuli, watch activity propagate through the selected circuit, and observe the simulated body respond.

Each sandbox is a prepared experiment inside the same world. The fly model, neural engine, sensory rules, body mechanics, and evidence display are shared. A mode selects the starting conditions, active stimuli, circuit view, measurements, and permitted interventions.

The first version should demonstrate a narrow, visible sensorimotor loop: a physical taste encounter produces activity in a documented gustatory pathway, which can drive a modeled feeding motor response. The next experiment adds food-related stopping. Heading, odor search, visual escape, grooming, and associative learning remain staged extensions.

### Core research question

> Can a neural model constrained by measured fly connections turn sensory events into coordinated actions that resemble published fly behavior, and do circuit perturbations change those actions in predicted ways?

### Project promise

Visitors can change what the fly senses, inspect its active neural pathway, and rerun the same experiment after a virtual neural intervention.

### Scientific position

Describe NeuroFly as a **connectome-constrained virtual fly**. A connectome provides structural wiring; neural dynamics, sensory encoders, actuator mappings, and body mechanics add model choices. NeuroFly should show those layers explicitly and test its outputs against published behavior.

A 2024 connectome-based LIF model studied feeding and grooming. NeuroMechFly v2 provides a separate embodied fly framework with physical interaction, sensory input, and locomotor environments. A preprint posted on 24 October 2026 also describes a brain-and-nerve-cord connectome connected to a simulated body. Treat the preprint as recent related work, not peer-reviewed confirmation. NeuroFly’s contribution should center on a polished shared experiment world, transparent provenance, visitor-controlled interventions, and reproducible comparisons. [Shiu et al., 2024](https://www.nature.com/articles/s41586-024-07763-9), [NeuroMechFly v2](https://www.nature.com/articles/s41592-024-02497-y), [October 2026 preprint](https://arxiv.org/abs/2610.33881)

### Related work: FruitFlyBrain and NeuroFly’s distinction

[FruitFlyBrain](https://github.com/ROHITCRAFTSYT/FruitFlyBrain) is a close related project and a useful engineering reference. Its repository combines connectome analysis, neuron visualization, graph machine learning, and a FlyLab locomotion system. That locomotion system trains a separate small network per skill with Evolution Strategies, then checks candidate controllers in the NeuroMechFly v2 body and MuJoCo physics. Its browser playground presents a 2D canvas surrogate, while MuJoCo films and held-out scores are shown alongside it. The browser model card documents a 17-input, 32-unit, 2-output network with 642 weights per skill and explicitly describes those behavior networks as learned rather than wired from the connectome. Separately, Project 04 uses hemibrain connectivity in a deliberately simple recurrent rate simulation of the central complex. These are valuable but distinct modeling layers. [FlyLab README](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/README.md), [browser playground](https://rohitcraftsyt.github.io/FruitFlyBrain/projects/09_flylab/playground/), [connectome-constrained Project 04](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/04_connectome_neural_network/simulate.py)

NeuroFly’s core question remains different: can a documented gustatory pathway turn contact with a taste stimulus into a feeding-related neural and proboscis response? Its intended contribution combines a visitor-operated 3D experiment world, a connectome-constrained circuit behind the featured behavior, and synchronized sensory, neural, motor, and body evidence. Feeding and proboscis control are not among FruitFlyBrain FlyLab’s seven reported locomotion tasks.

Transfer these engineering patterns selectively:

- **Calibrate the body interface.** Measure how actuator commands affect the chosen body model. For the first response, document proboscis extension, hold, retraction, contact, and lag; for walking, measure forward/lateral/yaw motion and contact.
- **Use a fast surrogate only as a matched preview.** Calibrate it from the reference simulation, compare against held-out time-varying commands, and label it clearly when full physics is not running.
- **Validate in the richer model.** Check any surrogate or learned component against a reference body/physics run.
- **Test whether a task can be solved without its claimed cause.** Run no-sensory, always-act, random, and simple-rule baselines where appropriate. If a sensory-blind policy passes, redesign the assay before claiming that the intended sensory or neural pathway caused the behavior.
- **Hold out conditions and report uncertainty.** Reserve stimulus settings, starts, or arena seeds from parameter tuning. Report trial count, failures, success criteria, and uncertainty alongside headline scores.
- **Test robustness within measured variation.** Once the sensor and body mappings are calibrated, vary plausible sensory noise, contact timing, motor lag, and gait variability within documented ranges. Do not introduce arbitrary randomization and call it biological variability.
- **Publish a realism audit.** Track measured, fitted, simplified, and missing parts; record failures as the model changes. FruitFlyBrain’s audit is a useful example of asking whether a policy truly uses its senses. Its September 2026 findings are historical audit results and should not be assumed to describe the current code without a fresh check. [FruitFlyBrain realism audit](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/09_flylab/REALISM_AUDIT.md)

Do not adopt free-running per-task networks as NeuroFly’s biological brain. Separate task networks are a useful engineering choice in FruitFlyBrain, but NeuroFly’s claimed behavior must remain driven by the documented connectome and shared biological circuit state. Learning methods may support a declared baseline, limited parameter calibration, or a surrogate; they must not silently replace the connectome with an arbitrary policy.

## 2. Project goals

### Goal 1 — Ground the neural graph in a real dataset

Choose a fixed FlyWire snapshot and retain the release, root IDs, annotations, synapse threshold, transmitter predictions, and data citation with every experiment. Keep neural identities tied to the dataset version.

The current Codex FAQ lists FAFB v783 for the female adult brain, BANC v888 for the female brain and nerve cord, and MCNS v1.0 for the male brain and nerve cord. FAFB is a good starting point for comparison with published brain-only work. BANC is the more relevant dataset when a sandbox requires walking and nerve-cord motor circuitry. Do not merge IDs from different releases without documenting how they map. [FlyWire Codex FAQ](https://codex.flywire.ai/faq)

### Goal 2 — Make the neural model reproducible

Select one neural model, state what it simplifies, and version its parameters. The original equation in the first draft is a rate model, not a spiking LIF model. If the exhibit uses spikes, implement and name LIF dynamics accurately; if it uses continuous rates, call it a rate model.

Synapse counts and transmitter predictions should inform the model, but they are not direct measurements of synaptic current or action. Document weight scaling, transmitter assumptions, threshold choices, delays, and uncertainty.

### Goal 3 — Close the sensory-to-body loop

The fly senses from its own position and orientation. Its movements change its next sensory input:

**world → receptors → connectome circuit → motor output → body motion → updated world and sensation**

A visitor changes the environment, such as placing food or rotating a landmark. The visitor does not directly command “turn left” or “feed” during a normal trial. Direct neuron stimulation is a separately labeled intervention.

### Goal 4 — Reproduce a known behavior first

Give each sandbox a published assay or clearly justified behavior target, an expected neural response, measurable outcomes, and a perturbation prediction. Reproduce before extending. Include a simple policy and sensory-blind baseline so the assay demonstrates that the measured input matters.

### Goal 5 — Make interventions informative

Stimulation, silencing, or lesion tools should alter the neural graph or neural state. The interface should reveal the selected intervention, affected connections, subsequent activity, and behavioral difference. Compare with biological evidence when possible.

### Goal 6 — Make the animal visibly embodied

Use a recognizable fly body with position, heading, contact points, and temporally continuous actions. Neural output should drive actuators. The body should affect later sensory input. Simplified biomechanics are acceptable when labeled clearly.

### Goal 7 — Build an exhibit that survives real use

Give visitors a simple path through a trial: choose a scenario, make one change, observe the response, inspect the neural pathway, and compare with an intervention. Include reset, replay, offline fallback, and a clear data/model legend. Keep a browser surrogate and a reference physics run visibly distinct whenever both are used.

### Goal 8 — Demonstrate sensory and circuit causality

For every behavior claim, show that the outcome depends on the intended input and circuit. Compare intact runs with no-sensory, pathway-lesion, shuffled or matched-network, and trivial-action baselines where appropriate. Include held-out trial conditions and report uncertainty rather than only the best run.

## 3. Product concept: one shared 3D NeuroFly Habitat

The recommended experience is one compact world with scenario presets. It should feel like one living subject being tested in different conditions, rather than a collection of unrelated scenes.

**Shared NeuroFly Habitat modes:** feeding; food stopping and state; heading; odor search; visual escape; grooming; associative learning.  
**Shared outputs:** body position and movement; neural activity; motor output; updated sensory input.  
**Shared trial cycle:** the body moves → the environment changes relative to the fly → sensory input updates → the next neural step runs.

### 3.1 What stays the same in every mode

- One fly model with a saved physical state: body pose, position, heading, contact state, and internal condition.
- One environment with configurable floor, food patches, odor, wind, visual landmarks, and approaching objects.
- One neural simulation interface and common intervention controls.
- One evidence legend distinguishing measured anatomy, model assumptions, predictions, and interventions.
- One timeline connecting stimulus, sensory activity, neural activity, motor output, and movement.
- Reset, pause, replay, and side-by-side run comparison.

### 3.2 What a sandbox mode configures

A sandbox loads an experiment preset that specifies:

- starting body pose and environment;
- stimulus types and sensory channels enabled;
- fed/starved or other justified internal state;
- the circuit to trace and display;
- permitted user controls;
- expected outputs and metrics;
- intervention and comparison preset.

Keep a constrained Free Explore mode for visitors after the guided scenarios work. It should allow the same world tools while keeping stimulus-to-sensor rules intact. Simultaneous uncontrolled stimuli should not be the default; they make causal results hard to interpret.

### 3.3 Recommended screen layout

- **Main area:** 3D arena, fly body, relevant food/stimulus objects, and trajectory.
- **Side panel:** current sandbox, stimulus controls, fed/starved state if supported, run/reset controls.
- **Neural panel:** active subgraph only, with actual cell IDs/types and animated activity.
- **Bottom timeline:** stimulus onset → sensory response → circuit response → motor response → body action.
- **Comparison view:** baseline run and intervention run, with synchronized replay.

Use top-down, side, and fly-eye camera options. Make the 3D body and neural panel synchronized so the exhibit explains cause and effect rather than showing unrelated animations.

## 4. How NeuroFly avoids feeling like a scripted image

1. **Inputs follow contact and physics.** Taste happens at a valid body contact; odor depends on what reaches the antennae; looming depends on the visual scene.
2. **Neural activity is the action source.** A motor output drives the proboscis, legs, or turn actuator. The renderer does not independently choose a behavior based on the stimulus label.
3. **Motion is continuous.** Preserve body inertia, contact, turning radius, and action duration. Avoid teleports and instant pose swaps.
4. **The active path is inspectable.** Show which measured cells and edges carried activity, along with the current model weight and annotation.
5. **The display labels uncertainty.** Predicted transmitter, measured connectivity, fitted parameters, and hand-designed sensor/body interfaces have separate labels.
6. **Repeated trials are controlled.** The same initial condition and random seed should replay identically. Additional seeded trials can show bounded biological variability.
7. **Interventions are real model interventions.** Silencing a node changes the network; it does not merely change a prewritten animation.
8. **Failure is visible.** If the model does not produce the expected response, log and show that result rather than forcing the target behavior.
9. **A task must require its claimed cause.** Test whether a trivial action, sensory-blind policy, or unconnected circuit can pass the same success rule. If it can, revise the assay or narrow the claim.
10. **Preview and reference behavior are labeled.** If the browser uses a calibrated surrogate, identify it in the interface and keep its scores separate from full body-physics results.

A useful visitor-facing path is: **place stimulus → watch sensor input → inspect highlighted circuit → observe body action → silence one cell → replay and compare.**

## 5. Experiment sandboxes and target setups

The visitor always uses the same NeuroFly Habitat. A sandbox is an experimental preset that reuses the world, fly, neural engine, and display.

### Sandbox 1 — Taste contact to proboscis response

**Priority:** MVP  
**Question:** Does a documented sugar or water taste pathway produce the predicted feeding-related neural output and proboscis response?

**Target setup:** One fly on a simple arena floor with visible sugar, water, and bitter patches. Taste input occurs only when the proboscis or a relevant contact point touches a patch. Start without a long-range food-search objective.

**Working path:**

1. Body contact exposes taste receptors to a stimulus.
2. The sensory encoder activates the relevant gustatory receptor neurons.
3. Spikes propagate through the selected connectome subgraph.
4. Feeding-related cells and proboscis motor neurons become active if the model predicts that response.
5. The motor output drives proboscis extension, contact/feeding motion, and retraction.
6. Body pose and contact state update the next sensory input.

**Visitor controls:** Place a taste patch, change stimulus strength, reset the fly, or virtually silence a selected sensory or downstream neuron.

**Measure:** Response probability, latency, neural motor output, and stimulus selectivity.

**Evidence and reference:** Shiu et al. studied gustatory responses, feeding-related motor predictions, and experimental testing of selected predictions. Use that work as a reproduction baseline, then differentiate NeuroFly through the shared 3D experiment environment, visitor-controlled perturbations, and transparent provenance. [Shiu et al., Nature (2024)](https://www.nature.com/articles/s41586-024-07763-9)

**Realism rule:** The fly must physically contact the patch; a click does not directly trigger feeding. Proboscis movement follows the modeled motor output. A later version may add a richer feeding action sequence using motor-neuron and muscle evidence. [Motor neurons organize Drosophila feeding sequences (2026)](https://www.nature.com/articles/s41593-026-02412-y)

**MVP limit:** A stationary or slowly moving fly is acceptable while the feeding circuit is isolated. Do not imply this first task proves odor search or full locomotor control.

### Sandbox 2 — Food encounter, stopping, and internal state

**Priority:** First extension of the MVP  
**Question:** Can a food encounter recruit a documented halting pathway, and does a supported fed/starved condition change the response?

**Target setup:** Same arena and fly. The fly walks across simple terrain and contacts a food patch. A scenario control starts it in a fed or starved state.

**Working path:**

1. Walking output drives leg movement.
2. Contact changes gustatory activity.
3. Activity reaches feeding and halting circuits.
4. Halting output reduces walking or turning through motor pathways.
5. Feeding output may activate the proboscis pathway.
6. The model determines whether walking resumes or the fly remains stopped.

A 2024 study reports context-specific mechanisms for halting and found stronger responses in a feeding-related halting neuron in starved flies. It gives a better foundation for this module than a hand-authored hunger multiplier. [Sapkal et al., Nature (2024)](https://www.nature.com/articles/s41586-024-07854-7)

**Visitor controls:** Fed/starved starting condition, food location, and virtual silencing of one documented halting cell.

**Measure:** Speed before/after food contact, stopping-bout duration, time near the patch, and feeding probability.

**Realism rule:** Stopping is a continuous change in motor activity. Keep stopping separate from proboscis extension because evidence indicates distinct pathways contribute to these responses. Represent internal state only through a sourced mechanism; otherwise mark it as a model hypothesis.

### Sandbox 3 — Compass and heading maintenance

**Priority:** Core extension after feeding  
**Question:** Does the modeled central-complex circuit maintain and update a heading representation from visual cues and self-motion?

**Target setup:** Same world, now with a small circular arena and a few stable landmarks. The visitor can rotate the fly, rotate landmarks, or turn off the visual scene.

**Working path:**

1. Visual cues bias the central-complex heading representation.
2. A localized activity bump represents current heading.
3. Self-motion signals shift the bump as the fly turns.
4. During visual blackout, activity persists and updates from self-motion.
5. Steering is added only when the relevant goal-to-heading comparison circuit is included.

Drosophila EPG compass neurons show bump-like activity that tracks heading and responds to both localizing cues and self-motion. [Multimodal cue integration and learning in a neural representation of head direction](https://www.nature.com/articles/s41593-024-01823-z)

**Visitor controls:** Rotate a landmark, remove vision, change wind direction, or silence selected compass cells.

**Measure:** Heading error, activity-bump stability, drift during cue loss, and response to cue rotation.

**Realism rule:** The fly body turn shifts the neural bump, and the bump cannot merely copy a UI heading variable. An EPG heading representation does not by itself encode a destination. Add goal-directed navigation only with a traced goal and steering circuit. [Converting an allocentric goal into an egocentric steering signal](https://www.nature.com/articles/s41586-023-07006-3)

### Sandbox 4 — Odor plume search

**Priority:** Stretch goal; substantial integration effort  
**Question:** Can a traced olfactory circuit help the fly search for an odor source under changing plume and wind conditions?

**Target setup:** Same arena, with airflow and intermittent odor puffs. The visitor can see the odor field, while the fly receives only the concentration reaching its antennae.

**Working path:**

1. Airflow carries odor puffs across the arena.
2. Antennae sample concentration as the body moves.
3. Receptor activity reflects stimulus timing and direction-related cues.
4. Activity propagates through the traced olfactory pathway.
5. Descending output changes walking or turning.
6. Movement changes the next odor sample.

**Visitor controls:** Move the source, turn the wind, create a short odor blackout, or virtually silence a traced cell.

**Measure:** Source-finding rate, time-to-source, path efficiency, and recovery after odor loss.

**Evidence and reference:** Drosophila can use temporal relationships in odor signals across the two antennae to infer odor motion in complex plumes. This supports using dynamic, patchy plumes rather than only a smooth radial gradient. [Odour motion sensing enhances navigation of complex plumes](https://www.nature.com/articles/s41586-022-05423-4)

**Realism rule:** Trace the sensory-to-motor route from the selected dataset. Do not claim that a receptor directly drives a named turn neuron based on a plausible label. The fly must sample the plume while moving; the source position should not be provided directly to the neural model.

### Sandbox 5 — Visual looming and escape

**Priority:** Stretch goal after a visual-to-motor path has been selected  
**Question:** Does an expanding visual object recruit the chosen visual and descending circuit and produce a correctly timed escape response?

**Target setup:** Same arena with a looming object whose angular size grows as it approaches. The visitor can change its approach direction, expansion rate, or time-to-contact.

**Working path:**

1. Visual input changes across the fly's field of view.
2. The visual encoder represents motion and expansion.
3. Activity propagates through the selected visual circuit.
4. Descending and nerve-cord outputs drive the chosen jump, turn, or rapid-walk action.
5. The action changes the object's position in the fly's visual field.

Research on fly looming responses has identified visual feature-detecting neurons and links to the Giant Fiber escape pathway. Trace the specific dataset and motor output selected for NeuroFly before committing to a particular action. [LPLC2 visual feature detection and Giant Fiber escape](https://pmc.ncbi.nlm.nih.gov/articles/PMC7457385/)

**Visitor controls:** Change approach direction/speed, replay the same threat, or virtually silence a candidate neuron.

**Measure:** Escape probability, latency, direction, and response across time-to-contact conditions.

**Realism rule:** Derive the input from changing visual angle and body movement. Do not represent every threat as a generic shadow flag with a scripted reaction.

### Sandbox 6 — Grooming sequence

**Priority:** Later extension  
**Question:** Can mapped mechanosensory inputs and grooming circuits reproduce the order and variability of grooming actions?

**Target setup:** Same fly and world, with virtual dust or touch contacts assigned to different body regions.

**Working path:**

1. Dust activates the relevant body-part sensory inputs.
2. Activity enters mechanosensory and grooming circuits.
3. Competing grooming outputs change over time.
4. Body movements clean the selected region.
5. Cleaning reduces that region's sensory drive and can affect the next action.

Fly grooming shows prioritization and suppression, alongside variable order and return-cleaning. Model action-order distributions and bout durations rather than a perfect deterministic queue. [Hampel et al., sequential grooming hierarchy](https://pmc.ncbi.nlm.nih.gov/articles/PMC4136539/), [Somatotopic grooming pathways](https://doi.org/10.7554/eLife.87602.2)

**Visitor controls:** Dust selected regions, add simultaneous touch, or silence a traced mechanosensory/grooming node.

**Measure:** Action-order frequencies, bout durations, and transitions between body regions.

### Sandbox 7 — Associative odor learning

**Priority:** Research extension; not part of the first expo build  
**Question:** Can a documented mushroom-body model change an odor response after reinforcement, and does learning generalize as expected?

**Target setup:** Same world with two distinguishable odor stimuli, a reward or punishment event, and a pre/post-training comparison.

**Working path:**

1. Odor patterns activate sparse Kenyon-cell populations.
2. Reinforcement activates an identified dopaminergic pathway.
3. A sourced plasticity rule changes effective synaptic strengths in the selected mushroom-body compartment.
4. A later odor-only test measures the changed response.
5. Reversal, retention, and generalization tests probe what the model learned.

Mushroom-body memory models and experiments describe compartment-specific dopamine signals and plasticity at Kenyon-cell-to-output-neuron synapses. Use those findings to define the rule and limits. [Dopamine-mediated interactions between short- and long-term memory dynamics](https://www.nature.com/articles/s41586-024-07819-w), [Dopaminergic mechanisms in reversal learning](https://www.nature.com/articles/s41467-021-21388-w)

**Visitor controls:** Pair an odor with reinforcement, test it, then reverse the pairing.

**Measure:** Acquisition, retention, reversal speed, and generalization to a similar odor.

**Realism rule:** Keep the measured anatomical graph separate from the model's changing effective weights. Do not thin visual edges as a stand-in for learning unless the display clearly labels those as effective-weight changes.

## 6. Shared experiment protocol

Before implementation, write a short specification for each sandbox:

1. Exact starting state, stimulus, and trial duration.
2. Source for the expected behavior and neural response.
3. Cells, edges, transmitter annotations, and dataset release used.
4. Model choices and parameter values.
5. Expected behavioral and neural measurements.
6. One intervention prediction.
7. A simple baseline and a shuffled-connectivity or matched random-network baseline.
8. A sensory-blind or trivial-action baseline that checks whether the task can be solved without the intended input.
9. Held-out conditions or seeds, trial count, success threshold, and the uncertainty summary to report.
10. How repeated trials vary and what the random seed controls.
11. What parts are measured, modeled, or still unknown.

### Cross-sandbox quality gates

- The selected subgraph can be rebuilt from the named release and extraction rules.
- A stimulus reaches the neural model through a documented sensory mapping.
- A motor output drives the visible action through a documented actuator mapping.
- An intervention changes network state and the output follows from the altered model.
- The task is checked against sensory-blind and simple-action baselines; a trivial policy must not satisfy the same success criterion.
- Conditions used for headline evaluation are held out from parameter selection. Report trial count, failures, and uncertainty.
- The result is compared with a published assay or a clear baseline.
- The display and project write-up label limitations directly.
- Target FPS, simulation rate, and latency are measured on named hardware before they are advertised.
- If a browser surrogate is used, compare it with the reference body/neural run on fixed and held-out inputs.

Do not equate 60 FPS rendering with 60 neural updates per second. The renderer can interpolate between neural/body updates if needed, but report the actual simulation update rate.

## 7. Recommended technology stack

The architecture should keep scientific computation, body/environment simulation, and visual presentation separate. The display can run at 60 frames per second while the neural engine publishes state snapshots at its measured update rate.

### 7.1 Front end and 3D world

- **React + TypeScript:** experiment menus, controls, telemetry panels, and shared UI state. [React documentation](https://react.dev/learn)
- **Vite:** local development and static production builds. Its guide supports deployment of a built site to GitHub Pages. [Vite static deployment](https://vite.dev/guide/static-deploy.html)
- **Three.js:** 3D arena, fly rendering, camera modes, food/odor/visual props, trajectories, and neural overlays. [Three.js manual](https://threejs.org/manual/)
- **CSS modules or plain CSS:** layout and visual system. Keep UI state and simulation state separate.
- **WebSocket client:** receive body and neural snapshots; send user stimulus and intervention events.

Use Three.js for visual rendering. Do not build a custom graphics engine. Start with one compact arena, a clear fly silhouette, readable body movement, and close-up views of active neural paths.

### 7.2 Connectome data preparation

- **Python** for offline graph extraction and scientific analysis.
- **Pandas or PyArrow** to inspect downloaded CSV/Parquet/Feather tables.
- **NumPy and SciPy sparse arrays** for numerical arrays and sparse graph operations. SciPy's CSR/CSC formats are designed for sparse arithmetic and vector products. [SciPy sparse arrays](https://docs.scipy.org/doc/scipy/tutorial/sparse.html)
- **NetworkX** only for offline circuit inspection and pathway selection; do not put large graph objects in the hot interactive loop.
- **Versioned subgraph assets:** publish only the selected circuit data required by the demo, with source snapshot and attribution. The full FAFB v783 Zenodo release is about 10.6 GB, so the public app should not bundle the full dataset. [FlyWire Zenodo release](https://zenodo.org/records/10676866)

### 7.3 Neural simulation

- **Brian 2** is the recommended starting point if NeuroFly uses a spiking LIF model. It is a Python spiking-network simulator and is used by the published Drosophila brain model. [Brian 2](https://briansimulator.org/), [Shiu model repository](https://github.com/philshiu/Drosophila_brain_model)
- **SciPy sparse arrays / NumPy** support custom sparse operations, graph transforms, and model-side analysis.
- Begin with one extracted circuit. Increase circuit size only after measuring runtime and checking model stability.
- Keep a documented weight conversion and transmitter-sign policy. Use predicted and verified labels distinctly.
- If the project instead selects a rate model, implement the equation directly with NumPy/SciPy and name it a rate model. Avoid running duplicate Brian and rate engines in the same demo.

The Shiu code repository is valuable for studying and reproducing the reference model. Its default input data are from an earlier FlyWire snapshot, so treat it as a scientific reference and map data versions deliberately instead of assuming it is a drop-in runtime for the latest dataset.

### 7.4 Fly body and environment simulation

**Preferred body/physics resource to evaluate:** FlyGym/NeuroMechFly v2 or the TuragaLab FlyBody model, both based on MuJoCo and intended for fly-body/environment interaction. [FlyGym documentation](https://neuromechfly.org/), [FlyGym repository](https://github.com/NeLy-EPFL/flygym), [FlyBody model and code](https://github.com/TuragaLab/flybody)

Use the body and physics components only where they support NeuroFly's goal. FlyGym includes example controllers and learned models; any reused behavior policy must be disclosed. Connectome-derived motor activity should remain the source of the behavior NeuroFly claims to model.

**Fallback for the first demo:** a simplified articulated 3D fly body whose proboscis or walking actuators respond to selected neural output. Mark unimplemented muscle and sensory mechanics as simplifications. Do not spend the first phase rebuilding detailed biomechanics if a public body model can be adapted.

FlyGym 2.x was rewritten in April 2026, so check compatibility, API, performance, and license before integration. Its maintainers describe CPU/GPU performance figures, but benchmark the exact NeuroFly circuit and exhibit hardware yourself. [FlyGym current documentation](https://neuromechfly.org/)

**Calibration and representation split:** keep the visual Three.js fly and physics body as separate representations connected by a documented body-state mapping. A detailed GLB is a renderer asset; it does not become a validated biomechanical model by being animated. For the proboscis MVP, measure or explicitly parameterize extension, hold, retraction, contact threshold, and motor lag. For later locomotion, sweep actuator commands in the selected physics model and record forward speed, lateral slip, yaw rate, ground contact, and gait variability. Store calibration data with the model version.

**Fast interaction path:** if full physics is too slow for browser interaction, build a reduced surrogate from measured body response. Validate it against held-out time-varying commands and state trajectories, not only steady-state values. Keep benchmark scores from the physics body separate from browser-surrogate scores. A surrogate is a runtime optimization; it is not evidence that the connectome model or body dynamics are biologically complete.

### 7.5 API and real-time link

- **FastAPI + Uvicorn** for session setup, scenario loading, health checks, and run metadata.
- **WebSockets** for live neural/body updates and user intervention messages. [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)
- Keep the neural simulation out of the API event loop. Run it in a worker or dedicated simulation process and publish snapshots to the WebSocket.
- Stream concise state snapshots, not the complete graph or every internal variable.
- Add heartbeat messages, client reconnect, a simulation reset endpoint, and a clear disconnected/replay state.

For the first release, no user accounts or database are required. Save a run locally as JSON/CSV or in session memory with seed, dataset version, stimulus, intervention, and outcome.

## 8. Hosting, deployment, and live-demo setup

### 8.1 Recommended public deployment

**Public web app:** GitHub repository + GitHub Actions + GitHub Pages for the compiled React/Vite frontend.  
**Live simulation service:** Python container on a WebSocket-capable service such as Render.  
**Expo fallback:** run the same container and frontend locally on the demonstration laptop.

For responsiveness, offer two clearly named run modes if needed: **Interactive Preview** for the calibrated browser surrogate and **Reference Run** for the full Python/body-physics path. The reference run can be hosted through the simulation service or run locally at an exhibit. If the hosted physics path is unavailable, show a labeled recorded reference replay beside the live preview rather than presenting the preview as full physics.

GitHub Actions is the build and deployment automation. GitHub Pages serves static files and does not run the Python simulation backend. GitHub's documentation describes Pages as static hosting and says it does not support server-side Python; Vite provides an Actions workflow for deploying its built site. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [Vite deployment guide](https://vite.dev/guide/static-deploy.html)

Render documents Python web services and inbound WebSocket support. Its free web services spin down after 15 minutes without traffic, so a visitor-facing live demo should use a warm service plan or the local expo setup. The WebSocket client still needs reconnect and keepalive handling because service instances can be restarted. [Render web services](https://render.com/docs/web-services), [Render WebSockets](https://render.com/docs/websocket), [Render free service behavior](https://render.com/docs/your-first-deploy)

### 8.2 GitHub Actions responsibilities

Use Actions for repeatable project automation:

- On pull requests: build the frontend, validate data schemas, run Python checks, and run the small deterministic simulation/evaluation suite.
- Check Python/browser parity on fixed example inputs for any shared neural or surrogate equations; record the tolerance used.
- On the default branch: build and publish the static frontend to GitHub Pages.
- For the backend: build the container and deploy through Render's linked-repository deployment or a protected deployment workflow.
- On release tags: publish the documented app version, model version, dataset snapshot, subgraph checksum, and evaluation summary.

Keep secrets and data download tokens out of the frontend and repository. Public asset bundles should contain only approved, cited subgraph files.

### 8.3 Expo reliability plan

- Run the simulation service locally in a container on the expo laptop so the experience does not depend on the venue internet connection.
- Serve the front end locally or use the public Pages site against the local API on the expo network.
- Include a clearly marked recorded replay if the live backend is unavailable. A replay must not be labeled as a live simulation.
- Preload all scenario and graph assets; avoid downloads during the judging demo.
- Provide a one-click reset and three prepared trial presets.
- Include a fixed reference run and a short held-out comparison set so the exhibit can demonstrate both a repeatable example and trial variability.
- Test camera, controls, fonts, and frame/update rate on the actual display and laptop.

### 8.4 Performance rules

- Keep the live graph filtered to the current circuit.
- Use sparse graph data; do not construct a dense full-brain matrix.
- Benchmark neural update rate, body update rate, WebSocket traffic, browser render rate, RAM, and cold start separately.
- State target hardware and circuit size beside any performance number.
- Do not promise sub-2 ms latency or full-brain 60 FPS until measured.

## 9. Resource catalog

This is a curated source map for NeuroFly, grouped by what the project needs. It is not a claim that every source is required on day one; use the starred core resources for the MVP and add the rest with each sandbox.

### 9.1 Connectome data and annotations — core

- **FlyWire Codex:** official browser for cell types, IDs, connectivity, pathways, and downloadable FAFB/BANC data products. Use the static download portal for bulk work; do not scrape the interactive explorer. [Codex and FAQ](https://codex.flywire.ai/faq)
- **FAFB v783 connectivity on Zenodo:** public whole-brain connection tables and root IDs. The complete release is large; extract only selected subgraphs for NeuroFly. [Zenodo dataset](https://zenodo.org/records/10676866)
- **Dorkenwald et al., whole-brain wiring diagram:** background and citation for the adult female brain connectome. [Nature paper](https://www.nature.com/articles/s41586-024-07558-y)
- **Schlegel et al., cell typing and annotations:** background for the FlyWire cell-class/type hierarchy. [Nature paper](https://www.nature.com/articles/s41586-024-07686-5)
- **BANC v888:** use the Codex BANC brain-and-nerve-cord release when the experiment needs walking or nerve-cord outputs. Confirm the selected download's citation and redistribution terms at acquisition. [Codex FAQ](https://codex.flywire.ai/faq)

### 9.2 Neural model and connectome simulation — core

- **Shiu et al., connectome-based feeding/grooming model:** scientific baseline for LIF dynamics, gustatory pathway stimulation, feeding-related motor predictions, and circuit perturbation. [Nature paper](https://www.nature.com/articles/s41586-024-07763-9)
- **Shiu et al. model code:** reference implementation for activation and silencing in a FlyWire-based model. Read the README and record the dataset version and assumptions before adapting it. [GitHub repository](https://github.com/philshiu/Drosophila_brain_model)
- **Brian 2:** Python spiking-network simulator suitable for the LIF route. [Official site](https://briansimulator.org/)
- **SciPy sparse arrays:** efficient sparse arithmetic and vector products for graph-scale operations. [Official tutorial](https://docs.scipy.org/doc/scipy/tutorial/sparse.html)

### 9.3 Body, physics, and embodied simulation — core for 3D locomotion

- **NeuroMechFly v2 / FlyGym:** existing Drosophila body, sensory, environment, and interaction framework. Investigate its scene and physics components before building equivalent mechanics. [Paper](https://www.nature.com/articles/s41592-024-02497-y), [documentation](https://neuromechfly.org/), [GitHub](https://github.com/NeLy-EPFL/flygym)
- **FlyBody:** anatomically detailed MuJoCo fly body and locomotion code. Decide whether to use its mechanics, a simplified body, or a carefully disclosed actuator adapter. [Nature paper](https://www.nature.com/articles/s41586-025-09029-4), [GitHub](https://github.com/TuragaLab/flybody)
- **Mujoco:** the physics foundation used by these body models. Prefer adapting a documented body model over inventing joint geometry and collision behavior.

### 9.4 Behavior and experiment references

- **Feeding and sensorimotor prediction:** Shiu et al., 2024. [Paper](https://www.nature.com/articles/s41586-024-07763-9)
- **Food-related halting and context:** Sapkal et al., 2024. [Paper](https://www.nature.com/articles/s41586-024-07854-7)
- **Heading compass and cue learning:** multimodal cue integration in the Drosophila head-direction network. [Nature Neuroscience paper](https://www.nature.com/articles/s41593-024-01823-z)
- **Heading-to-steering comparison:** circuit that converts an allocentric goal signal into an egocentric steering signal. [Nature paper](https://www.nature.com/articles/s41586-023-07006-3)
- **Odor plume cues:** odor motion and bilateral temporal correlation in naturalistic plume navigation. [Nature paper](https://www.nature.com/articles/s41586-022-05423-4)
- **Visual escape:** looming-feature visual neurons and escape pathway. [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7457385/)
- **Grooming:** hierarchical competition and body-location-specific mechanosensory pathways. [Hampel et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4136539/), [Eichler et al.](https://doi.org/10.7554/eLife.87602.2)
- **Associative memory:** compartmental dopamine signals and mushroom-body plasticity. [Huang et al., Nature (2024)](https://www.nature.com/articles/s41586-024-07819-w)
- **Recent related embodied-connectome work:** October 2026 preprint, not peer reviewed as of this plan date. Read for positioning and comparison, not as settled evidence. [arXiv preprint](https://arxiv.org/abs/2610.33881)

### 9.5 Front-end, build, and hosting references

- **React:** component UI. [Documentation](https://react.dev/learn)
- **Three.js:** 3D web rendering. [Manual](https://threejs.org/manual/)
- **Vite:** development and static build. [GitHub Pages deployment guide](https://vite.dev/guide/static-deploy.html)
- **GitHub Actions and Pages:** build/deploy automation and static site hosting. [GitHub Actions deployment guide](https://docs.github.com/en/get-started/start-your-journey/deploying-your-website-automatically), [Pages limits and supported content](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- **FastAPI WebSockets:** backend session and streaming interface. [Official documentation](https://fastapi.tiangolo.com/advanced/websockets/)
- **Render:** optional Python service host with WebSocket support. [Web services](https://render.com/docs/web-services), [WebSockets](https://render.com/docs/websocket)

### 9.6 Art, 3D assets, and visual research

- Use FlyGym/FlyBody models as a reference or starting asset only after checking the specific model, code, and dataset terms.
- Use Codex's 3D viewer and pathway views to study cell morphology and circuit organization; create simplified, clearly labeled circuit renderings for the exhibit.
- Create original arena props and interface elements. Avoid using screenshots or scientific figures as decorative textures unless the figure's reuse terms permit it.
- Keep a credits file that lists author, source URL, asset license, modified version, and where the asset appears in the application.

### 9.7 Data access, attribution, and responsible publication

- Use the static files and version notes supplied by Codex or the canonical archive rather than automated scraping. [Codex FAQ](https://codex.flywire.ai/faq)
- Record the dataset snapshot and retrieval date in the subgraph manifest.
- Check release-specific licensing and citation requirements before publishing derived graph assets or body models.
- Do not place FlyWire/CAVE credentials or download tokens in frontend code, public repository files, or a Pages deployment.
- Keep raw large connectome data outside the Git repository. Version the extraction script, manifest, selected subgraph, and checksums instead.
- Cite both the dataset and the papers that define cell labels and functional interpretation.

### 9.8 Closely related implementation reference — FruitFlyBrain

- **Repository:** [ROHITCRAFTSYT/FruitFlyBrain](https://github.com/ROHITCRAFTSYT/FruitFlyBrain). Useful for its separated connectome analysis and behavior-control projects, body calibration, lightweight browser surrogate, and public training/evaluation dashboard.
- **Behavior and browser implementation:** [Project 09 FlyLab](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/tree/main/projects/09_flylab). Treat its task-specific learned networks as a locomotion-control reference and baseline, not as a connectome-derived feeding circuit.
- **Connectome rate-model example:** [Project 04 simulation](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/projects/04_connectome_neural_network/simulate.py). Useful for subgraph selection and graph-driven activity visualization; its own code describes the dynamics as deliberately simple and not biophysical.
- **Data provenance:** [dataset notes](https://github.com/ROHITCRAFTSYT/FruitFlyBrain/blob/main/datasets/README.md) distinguish hemibrain connectivity from FlyWire whole-brain annotations and list 3.55 million hemibrain connection rows alongside 14.3 million synapses. NeuroFly should label edge counts and synapse counts separately, freeze its own chosen data release, and avoid mixing identifiers across datasets.
- **Reuse terms:** the repository states its code and documentation are MIT-licensed, connectome datasets are CC BY 4.0, and FlyGym is Apache-2.0. Preserve the correct notice for anything reused and check source terms for each dependency and dataset separately. [Repository license](https://github.com/ROHITCRAFTSYT/FruitFlyBrain#license)

## 10. Build phases and completion gates

### Phase 0 — Lock the first question and data release

Choose the feeding assay, exact dataset release, and expected output. Trace the input and output cells in Codex and decide which paper or experiment will be used as the comparison.

**Complete when:** the team can name the data release, starting stimulus, sensory cells, target motor output, known evidence, and model assumptions.

### Phase 1 — Build the data pipeline

Download the official source files, inspect schema and annotations, extract the selected path and necessary partners, keep provenance and checksums, and export a small sparse subgraph plus manifest.

**Complete when:** the same extraction command can rebuild the subgraph and produce a manifest with cell IDs, version, connection threshold, annotations, and source citations.

### Phase 2 — Build the neural engine

Implement the chosen rate or spiking model for one subgraph. Add stimulus injection, virtual silencing, virtual stimulation, repeatable seeds, and logs.

**Complete when:** fixed input and seed produce repeatable neural outputs, and interventions alter network activity in the expected direction.

### Phase 3 — Build the NeuroFly Habitat and body path

Create the compact 3D arena, visible fly, contact model, camera modes, food objects, reset/replay, and neural activity panel. Decide whether the first version uses a custom lightweight body or FlyGym/FlyBody mechanics. Keep renderer geometry and physics representation distinct and define how body state and actuator outputs map between them. Calibrate the first proboscis response and document missing mechanics.

**Complete when:** the body has stable contacts and continuous movement, the actuator mapping is recorded, and the frontend displays simulation state without changing the action.

### Phase 4 — Complete the taste-to-feeding loop

Connect contact-based taste to the neural circuit and motor output. Drive proboscis movement from the output using a documented extension/hold/retraction mapping. Add the first visitor intervention and synchronized comparison replay.

**Complete when:** a visitor can run the full stimulus → sensory → circuit → motor → body path and repeat it after silencing a selected node; no-contact, no-sensory, and always-respond controls show that the assay depends on the intended causal path.

### Phase 5 — Validate the MVP

Compare neural and behavioral outputs with the reference, plus sensory-blind, simple-rule, always-respond, and shuffled or matched random-network baselines as appropriate. Use held-out stimulus strengths/locations or trial seeds, and vary contact timing, sensor noise, or actuator lag only within stated plausible ranges. Measure response probability, latency, repeatability, uncertainty, surrogate-to-reference agreement, and performance on the target hardware.

**Complete when:** the team reports trial counts, uncertainty, all baseline results, successful and failed cases, model limitations, and avoids unsupported performance or novelty claims.

### Phase 6 — Add food stopping and state

Add walking/halting only after motor pathways and dataset scope are clear. Add fed/starved comparison only where a source supports the mechanism.

**Complete when:** body speed and stopping duration respond continuously to food encounter and intervention.

### Phase 7 — Expand one sandbox at a time

Choose heading, odor, or escape next based on circuit availability and validation quality. Write a separate assay specification for each. Move grooming and associative learning to later work.

**Complete when:** each added mode passes the same provenance, baseline, intervention, repeatability, and body-feedback gates as the MVP.

### Phase 8 — Deploy and prepare for the exhibit

Publish the frontend, deploy or package the backend, prepare offline mode, preload data, and test the full visitor flow on the actual screen and laptop.

**Complete when:** the public site launches, a trial can be reset quickly, the local setup works without venue internet, and the demo can distinguish a live run from a replay.

## 11. Evaluation dashboard

Keep a small dashboard per sandbox with:

- stimulus and starting state;
- dataset version and selected circuit;
- model name and parameter set;
- neural response summary;
- behavior measure;
- baseline result;
- sensory-blind and trivial-policy baseline results;
- intervention result;
- held-out test result, number of trials, failures, and uncertainty interval;
- calibration/surrogate version and reference-physics agreement, where used;
- runtime, memory, render rate, and simulation update rate;
- known limitations.

Suggested measures:

| Sandbox | Core measures |
|---|---|
| Taste-to-feeding | motor response probability, latency, stimulus selectivity |
| Food stopping | speed change, stopping duration, time near food |
| Heading | heading error, bump stability, drift in blackout |
| Odor search | source-finding rate, time-to-source, path efficiency |
| Visual escape | latency, escape direction, success by time-to-contact |
| Grooming | action-order distribution, bout duration, transition frequency |
| Associative learning | acquisition, retention, reversal, stimulus generalization |

The most persuasive project result is not a glowing neural graph. It is a repeatable behavioral result with a measurable connectome-based prediction and a controlled perturbation comparison.

## 12. Suggested repository organization

Keep scientific data processing separate from presentation code:

- **frontend:** React/TypeScript screens, Three.js world, camera, controls, and replay.
- **simulation service:** scenario API, neural runtime, session state, WebSocket snapshots, and health checks.
- **data pipeline:** download notes, schema validation, circuit extraction, version manifests, and checksums.
- **body calibration:** actuator-response maps, render-to-physics mapping, reference traces, and any validated browser surrogate.
- **subgraphs:** only approved compact subgraph assets with source/version manifests.
- **scenarios:** sandbox definitions, initial states, event presets, and expected measures.
- **evaluation:** published assay references, baselines, repeat-trial summaries, and result exports.
- **docs:** model card, data citations, methods, limitation notes, credits, and demo instructions.
- **workflows:** CI and static site/backend deployment configuration.

Never store API tokens or full raw connectome archives in public frontend assets.

## 13. Risks and design rules

| Risk | Design rule |
|---|---|
| The real wiring is mistaken for a full biological brain | Call it connectome-constrained; label modeled dynamics and body interface |
| Behavior is secretly hardcoded in the renderer | Only neural motor output can trigger the displayed action in a neural trial |
| A hand-selected circuit is presented as a whole-brain simulation | State neuron count and circuit scope per sandbox |
| A body controller adds undocumented behavior | Use body mechanics separately from high-level behavior policy; disclose actuator decoders |
| An input mapping invents receptor response | Cite or label the mapping and test sensitivity |
| A display graph becomes decorative noise | Show only the active circuit and link it to the current action |
| The venue network fails | Run the backend locally and preload assets; offer a labeled replay fallback |
| Data terms or cell IDs differ across releases | Freeze the snapshot and record mapping/citation before building |
| Full graph performance is guessed | Benchmark the selected subgraph; do not advertise full-brain timing without measurement |
| A simple policy passes without using the intended stimulus | Add sensory-blind and trivial-action baselines; redesign the stimulus or success rule before interpreting neural activity |
| Browser preview drifts from body physics | Calibrate from the reference body, test held-out command sequences, show separate scores, and keep a Reference Run |
| A trained controller is described as a biological connectome | Keep learned-control baselines separate from the connectome model and label every model layer |
| Render model and physics body diverge | Define a shared state/actuator mapping and compare rendered joints against recorded physics states |

## 14. Presentation outline

### 60-second visitor demonstration

1. Open **Feeding** in the NeuroFly Habitat with the fly in a known starting state.
2. Place a sugar patch in contact range and start the trial.
3. Show the sensory activity and highlight the active connectome pathway.
4. Let neural output drive the proboscis response.
5. Select one candidate neuron for virtual silencing and replay the same trial.
6. Compare neural output and action side by side.
7. Point out which parts come from measured anatomy and which are model assumptions.

### Suggested judge-facing description

> NeuroFly is a connectome-constrained virtual fly in a shared 3D experiment world. Its first experiment follows taste contact through a documented neural pathway to a feeding-related proboscis response. Visitors can change the stimulus, inspect circuit activity, and compare the response with a controlled neural intervention and sensory-blind baselines. The project records which parts come from connectome data, which are model choices, and how the results compare with published behavior.

## 15. Final scope recommendation

The complete vision is a shared, extensible 3D NeuroFly Habitat. The first release should prove the taste-to-feeding loop and one causal intervention. Food-related stopping is the next module. Heading follows once the feeding loop is stable. Odor search and visual escape are stretch modules; grooming and associative learning are later research modules.

Build the world and interfaces so new experiments can be added, but only claim a behavior after tracing its circuit, closing its sensorimotor loop, and comparing its results with evidence.
