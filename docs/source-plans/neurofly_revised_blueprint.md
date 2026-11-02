# NeuroFly: Revised Project Blueprint

**Revision date:** 1 November 2026
**Project type:** Connectome-constrained NeuroAI and embodied-agent demonstration

## 1. Project framing

NeuroFly is a virtual fly controlled by a neural simulation constrained by a real Drosophila connectome. It is not a complete emulation of a living fly brain. The project uses measured wiring where available, simplified neural dynamics, engineered sensory and motor interfaces, and a simulated body.

The visitor should be able to see which parts come from anatomical data, which parts are modeling choices, and which actions are predictions from the model.

### Central question

Can a neural network constrained by measured fly-brain connections turn sensory events into coordinated actions that resemble published fly behavior, and do connectome-based perturbations change those actions in the predicted way?

## 2. Project goals

### Goal 1: Use a real, versioned connectome

Build each neural circuit from a documented FlyWire release. Keep the release, neuron IDs, annotations, connection threshold, and source references with the simulation so another person can reproduce the graph.

Codex currently lists FAFB v783 for the female adult brain, BANC v888 for the female brain and nerve cord, and MCNS v1.0 for the male brain and nerve cord. Choose one release for each experiment. Do not mix cell IDs from releases unless their mapping has been checked and recorded. Codex notes that IDs and annotations can change across snapshots. [FlyWire Codex FAQ](https://codex.flywire.ai/faq)

### Goal 2: Run a neural model whose assumptions are visible

Represent selected cells and their directed connections as a sparse network. Model neural activity over time and allow it to propagate from sensory to downstream cells. Keep cell-type and transmitter confidence in the data.

Connection counts are anatomical evidence; they are not direct measurements of synaptic current or behavior. Convert them into simulation weights with a documented rule, calibrate where published evidence allows, and show sensitivity when the result depends on an uncertain assumption. A connectome-based LIF model has already been used to make experimentally tested predictions about fly feeding and grooming, so NeuroFly should extend that kind of work with an interactive, embodied, reproducible experience. [Shiu et al., 2024](https://www.nature.com/articles/s41586-024-07763-9)

### Goal 3: Close the loop between the fly, its sensors, and the world

The fly must sense the world from its own position and orientation. Its movements must change what it senses next.

The main loop is:

**environment → sensory receptors → connectome circuit → neural motor output → body movement → changed environment and sensory input**

A visitor should affect the environment, such as placing food or rotating a visual landmark. The visitor should not directly command left, turn, or feed during a normal trial. Direct neuron stimulation is a separate, clearly labeled experiment.

### Goal 4: Reproduce known behavior before claiming new behavior

Each sandbox should have a small behavioral assay, an expected result, measurable outputs, and a published source or dataset for comparison. Start by reproducing one well-documented result. Add a more ambitious task only after the first result is repeatable.

### Goal 5: Make neural interventions causal and interpretable

Let users stimulate or silence selected nodes and edges. The intervention should change the neural simulation itself. The interface should show what was changed, where activity moved, and how the output behavior changed.

Call these virtual stimulation and virtual silencing. They are model experiments. Compare them with biological experiments when suitable evidence exists.

### Goal 6: Make the animal visibly embodied

The fly should have a recognizable body, a position, a heading, contacts with objects, and actions that unfold over time. Each modeled action should be driven by simulated neural output and an explicit actuator model. Body motion should update the sensors and feed back into the neural loop.

## 3. Recommended scope and order

### First public version

Build two reliable demonstrations:

1. **Taste-to-feeding response:** a physical taste encounter activates gustatory neurons and produces a modeled proboscis response.
2. **Feeding-context halt:** a moving fly encounters food, slows or stops through a documented halting circuit, and then responds to taste.

These give visitors a concrete, visible action and let the project demonstrate neural activity, body output, and causal perturbation without pretending to have solved the entire fly.

### Later additions

Add heading, odor-guided search, and visual escape after their sensory-to-motor pathways and output mappings have been traced and benchmarked. Keep grooming and associative learning as research extensions until the first closed-loop behavior is sound.

## 4. Shared simulation design

### 4.1 Data and circuit extraction

For every sandbox, store:

- dataset name and exact version;
- neuron root IDs, cell types, side, and neuropil;
- directed presynaptic and postsynaptic pairs;
- synapse counts and the threshold used to retain edges;
- predicted transmitter types and confidence, plus any verified annotation;
- references for functional roles and known perturbations;
- the rule used to translate anatomical connection counts into model weights.

Use the official downloadable tables and keep the original files' version and attribution. Codex reports different default connection thresholds for different releases: FAFB uses five or more synapses per neuron pair, while BANC uses three or more. Keep this threshold explicit when comparing graphs. [Codex FAQ: connectivity thresholds and downloads](https://codex.flywire.ai/faq)

Display only the selected active circuit in the live graph. A whole-brain force-directed graph would be too dense to explain. Show actual cell IDs and annotated cell types, with a trace of the currently active path.

### 4.2 Neural dynamics

Choose and name one model clearly.

- A **spiking LIF model** tracks membrane state, threshold crossings, spikes, and resets.
- A **leaky rate model** tracks continuous activity values without individual spikes.

Both can be useful simplified models. Do not call a continuous rate equation LIF. For a spike-focused visitor display, a sparse LIF model is a natural first choice if the selected circuit can run smoothly. A rate model is a reasonable fallback if named accurately and evaluated against the same behavior metrics.

Use deterministic random seeds for repeatable trials. If noise is included to represent biological variability, define its range and show repeated trials rather than making each animation arbitrarily different.

### 4.3 Sensory inputs

Convert environmental events into sensory activity using the relevant receptors and stimulus timing.

- Taste should activate gustatory neurons only when the appropriate body part contacts a surface or food.
- Odor should depend on concentration arriving at the antennae over time, including wind and intermittent odor puffs.
- Visual motion should depend on what changes across the fly's visual field, not only on a generic threat flag.

If an early version uses a simplified stimulus, label it as an input approximation.

### 4.4 Body and motor output

Build a small, legible fly body model with at least:

- body position and heading;
- contact points for legs, antennae, and proboscis;
- a proboscis actuator for feeding;
- leg or body actuators for walking, halting, and turning when those circuits are available.

Drive each actuator from selected motor-neuron activity or from a plainly documented decoder. Never teleport the fly to a destination after a sensor fires. Let movement, contact, and inertia produce continuous trajectories. If detailed musculature is outside the first version, say that neural output drives a simplified body actuator.

For brain-only feeding work, FAFB can support the initial taste-to-proboscis experiment. For walking and nerve-cord motor circuits, use an appropriate brain-and-nerve-cord dataset such as BANC v888, and document how its cells and motor outputs were identified. [FlyWire Codex datasets](https://codex.flywire.ai/faq)

### 4.5 What the visitor sees

Keep the arena and activity visualization synchronized. Add a compact evidence legend:

- **Measured anatomy:** connectome edge or cell annotation.
- **Model choice:** dynamics, weight scaling, sensory encoder, or actuator mapping.
- **Model prediction:** activity or action generated in the current trial.
- **Intervention:** virtual stimulation, silencing, or lesion.

When an action occurs, show the path: stimulus, sensory cell, strongest downstream activity, motor output, and body motion. If an expected action fails, show that too.

## 5. Sandboxes

### Sandbox 1 — Taste contact to proboscis response

**Priority:** MVP

**Question:** Does activation of a documented sugar or water taste pathway produce the predicted feeding-related neural output and proboscis response?

**Scene:** The fly is on a simple surface with visible food patches. A taste input occurs only when the proboscis or an appropriate contact point touches the patch. Start with a short assay rather than full food search.

**Working sequence:**

1. The fly's body contacts a sugar, water, or bitter patch.
2. The sensor model activates the corresponding gustatory receptor neurons.
3. Their spikes propagate through the selected connectome subgraph.
4. Feeding-related cells and the relevant proboscis motor neurons become active if the model predicts that response.
5. The motor output drives proboscis extension, a short contact or feeding movement, and retraction.
6. The changed body pose and contact state update the next sensory input.

The FlyWire connectome-based model from Shiu et al. studied gustatory responses and feeding-related motor-neuron predictions, with experimental testing of selected predictions. Use it as a reproduction benchmark, then make NeuroFly distinctive through its closed-loop body, live pathway inspection, and interactive interventions. [Shiu et al., 2024](https://www.nature.com/articles/s41586-024-07763-9)

**Visitor controls:** Place a taste patch, change its stimulus level, or virtually silence a selected sensory or downstream neuron.

**Measure:** Response probability, latency to motor output, motor activity, and whether the proboscis action matches the stimulus condition.

**How to make it feel like a fly:** The fly must physically touch or taste the patch; taste does not activate from a distant mouse click. The proboscis extends only after modeled motor output. Use a measured or literature-grounded action sequence where possible. A recent study reports sequential feeding-related muscle activity coordinated by motor neurons, which can guide a later, more detailed feeding animation. [Motor neurons organize Drosophila feeding sequences](https://www.nature.com/articles/s41593-026-02412-y)

**MVP limit:** This sandbox can begin with a stationary or slowly walking fly. Do not imply that it demonstrates odor search or full locomotor control.

### Sandbox 2 — Food encounter, stopping, and internal state

**Priority:** Core extension of Sandbox 1

**Question:** Can a documented feeding context cause the fly to slow or halt, and does fed-versus-starved state change the response in a way supported by experiments?

**Scene:** The fly walks across a simple floor toward or across food patches. The first version may use a basic arena; add richer body dynamics as nerve-cord motor circuits are integrated.

**Working sequence:**

1. Walking activity drives leg movement.
2. A food encounter changes gustatory activity.
3. Activity reaches identified feeding and halting pathways.
4. Walking commands are reduced or arrested through the modeled halting mechanism.
5. The feeding response proceeds through the proboscis motor circuit.
6. The fly resumes or remains stopped based on modeled circuit activity.

A 2024 study distinguished brain-level walk-OFF halting from nerve-cord braking and found that the halting pathways are context-specific. It also reported stronger responses in a feeding-related halting cell in starved flies than in fed flies. This offers a grounded starting point for an internal-state comparison. [Sapkal et al., 2024](https://www.nature.com/articles/s41586-024-07854-7)

**Fed and starved conditions:** Represent hunger with a state parameter only where a documented pathway supports it. Do not hardcode that starvation cancels bitter avoidance or multiply an arbitrary inhibitory signal unless that rule is labeled as a testable model hypothesis.

**Visitor controls:** Choose a fed or starved starting condition, place food, then virtually silence the documented halting node.

**Measure:** Speed before and after food encounter, stopping-bout duration, time spent near food, and probability of initiating feeding.

**How to make it feel like a fly:** The fly should slow through a continuously changing motor output, not snap into a frozen pose when it reaches a food tile. Separate stopping from proboscis extension because they can be controlled by different pathways.

### Sandbox 3 — Compass and heading maintenance

**Priority:** Core research demo after the feeding loop

**Question:** Does the modeled central-complex circuit maintain and update a heading representation from visual cues and self-motion?

**Scene:** A circular arena with a few stable visual landmarks and an optional wind direction. Let the fly rotate or walk. In one trial, turn off the visual scene after the heading bump is established.

**Working sequence:**

1. Visual landmark input biases the compass network.
2. A localized activity bump represents the fly's current heading.
3. Self-motion signals update the bump as the fly turns.
4. In darkness, the activity persists and changes based on self-motion rather than being held at a fixed visual angle.
5. A steering output may be added only when the relevant goal-to-heading comparison circuit is included.

The fly's EPG heading representation has been studied as a ring-attractor-like activity bump influenced by external cues and self-motion. [Nature Neuroscience, "Multimodal cue integration and learning in a neural representation of head direction"](https://www.nature.com/articles/s41593-024-01823-z)

**Visitor controls:** Rotate a landmark, remove visual cues, or change the direction of a wind cue. Optionally silence selected compass cells.

**Measure:** Heading error, activity-bump stability, and drift during cue loss.

**Important limit:** An EPG heading bump represents heading. It does not alone represent a destination or explain a route around an obstacle. Claim goal-directed steering only after adding and tracing the goal representation and steering pathway. [Converting an allocentric goal into an egocentric steering signal](https://www.nature.com/articles/s41586-023-07006-3)

**How to make it feel like a fly:** The arena must rotate relative to the fly's body, and the body's turns must shift the neural bump. The activity should not be a decorative compass graphic that merely follows a UI heading variable.

### Sandbox 4 — Odor plume search

**Priority:** Stretch goal; high integration effort

**Question:** Can a traced olfactory circuit help the fly search for an odor source under changing plume and wind conditions?

**Scene:** A 2D arena with air flow and visible, intermittent odor puffs. The source is hidden from the simulated fly. The UI may show the plume to the visitor while the fly receives only concentration at its antennae.

**Working sequence:**

1. Airflow carries odor puffs through the arena.
2. The antennae sample concentration as the body moves.
3. Odor receptor neurons encode concentration and timing; include adaptation if supported by the chosen receptor model.
4. Activity propagates through the traced olfactory circuit.
5. Downstream activity changes turning or walking outputs through identified motor pathways.
6. Movement changes the fly's next odor sample.

**Visitor controls:** Shift the odor source, change wind direction, create a sensory blackout, or silence a traced neuron.

**Measure:** Source-finding success, time to source, path efficiency, and response when odor is temporarily lost.

**Data requirement:** Trace the actual sensory-to-motor pathway and validate the receptor and motor mappings before presenting source-finding as connectome-generated. Do not assume a particular receptor directly drives a named turning neuron based only on plausible cell names.

**How to make it feel like a fly:** Use an advected, patchy plume and let the fly sample it as it moves. A smooth radial concentration gradient can remain as a simple comparison condition, but should not be the only input model.

### Sandbox 5 — Visual looming and escape

**Priority:** Stretch goal; add after selecting a validated visual-to-motor pathway

**Question:** Does a looming visual stimulus recruit the expected visual and descending circuits and produce a correctly timed escape action?

**Scene:** A dark arena with a looming object that grows in angular size across the fly's visual field. Let the visitor change its approach direction, speed, and time-to-contact.

**Working sequence:**

1. The visual environment produces changes across the fly's viewing field.
2. The visual sensor model encodes expansion and direction.
3. Activity propagates through the selected visual circuit.
4. Descending and nerve-cord outputs produce an escape action, such as a jump, turn, or rapid walk, according to the circuit and body model chosen.
5. The resulting body movement changes the object's position in the visual field.

**Visitor controls:** Vary the looming object, silence a candidate neuron, or compare left- and right-side stimulation.

**Measure:** Escape probability, latency, direction, and success across different time-to-contact conditions.

**How to make it feel like a fly:** Calculate the stimulus from changing visual angle and body motion. Keep the named neuron pathway provisional until the specific cell identities and motor consequences are traced and supported. Show the selected escape action as a model output, not a canned reaction animation.

### Sandbox 6 — Grooming sequence

**Priority:** Later extension

**Question:** Can mapped mechanosensory input and grooming circuits reproduce the distribution and order of grooming actions?

**Scene:** Dust or tactile stimuli contact different body regions. The fly performs the corresponding cleaning movements.

**Working sequence:**

1. Dust activates the relevant body-part sensory inputs.
2. Activity enters mechanosensory and grooming circuits.
3. Competing grooming outputs change in strength over time.
4. The body performs the selected head, antenna, leg, or body cleaning movement.
5. Cleaning changes the sensory drive from the affected region, which may alter the next action.

Fly grooming has evidence for suppression and priority, but its order can vary and include return-cleaning. Model a distribution of sequences and compare it with observations rather than promising a perfectly fixed queue. [Hampel et al., "A suppression hierarchy among competing motor programs"](https://pmc.ncbi.nlm.nih.gov/articles/PMC4136539/)

**Measure:** Action-order frequencies, bout durations, and transitions between body regions.

### Sandbox 7 — Associative odor learning

**Priority:** Research extension, not part of the first expo build

**Question:** Can a documented mushroom-body circuit change its odor response after pairing with reward or punishment, and does the change generalize appropriately?

**Working sequence:**

1. Present odor patterns to Kenyon cells.
2. Pair one odor with a defined reinforcement input to an identified dopamine pathway.
3. Update only the synapses and plasticity variables supported by the selected learning model.
4. Present the odor alone and measure the change in approach or avoidance.
5. Test retention, reversal, and generalization to a similar odor.

The plasticity rule must be sourced, its parameters documented, and its learned output compared with a published behavioral assay. Do not thin visible edges merely to represent learning; distinguish the anatomical connectome from the model's changing effective weights.

## 6. Evaluation plan for every sandbox

For each sandbox, write a one-page experiment specification before implementation:

1. **Assay:** exact stimulus, starting state, and trial length.
2. **Expected result:** the published or otherwise justified observation.
3. **Neural prediction:** which circuit activity should change and in what direction.
4. **Behavior metrics:** measurable action, latency, probability, or trajectory property.
5. **Intervention:** one stimulation, silencing, or lesion prediction.
6. **Baselines:** a simple controller and a network with shuffled connections or matched random edges.
7. **Repetitions:** enough deterministic-seed trials to show variability and repeatability.
8. **Limitations:** what is simulated, what is measured, and what remains unknown.

The central claim becomes stronger if the connectome-constrained model reproduces known behavior and predicts meaningful intervention effects better than the baselines.

## 7. Booth demonstration flow

1. The visitor chooses a sandbox and sees the modeled fly's current state.
2. The visitor changes the environment, such as placing a taste patch or rotating a landmark.
3. The UI shows the resulting sensory input and active connectome pathway.
4. Neural activity evolves over time and drives a body action.
5. The visitor repeats the same trial after silencing one selected neuron.
6. A comparison panel shows behavior and neural activity for both trials, along with evidence and model-assumption labels.

### Suggested booth explanation

> NeuroFly tests whether measured connections from a fly brain can help explain a real behavior. You can change what the fly senses, follow activity through the modeled circuit, and test how a neural perturbation changes the action. The display also marks which parts are measured anatomy and which parts are simplified model assumptions.

## 8. Build phases and completion gates

### Phase 1 — Freeze the data and trace one circuit

Choose the release, collect the official data products, verify neuron IDs and paths, and create a small reproducible subgraph.

**Gate:** A second person can rebuild the same graph from the documented dataset and extraction rules.

### Phase 2 — Build one neural-to-body loop

Implement the selected neural model, taste input, feeding motor output, and a small fly body with a proboscis actuator.

**Gate:** A sensory event reaches the network and produces or fails to produce a motor action through the documented output path.

### Phase 3 — Reproduce and perturb

Compare the behavior and selected neural outputs with the reference assay. Add virtual stimulation or silencing and the first baseline comparison.

**Gate:** Results are repeatable, measurable, and the intervention changes activity and behavior through the model.

### Phase 4 — Add context and walking halting

Use the nerve-cord dataset and a documented food-related halting pathway. Add fed/starved comparison only where supported by experiment.

**Gate:** Contact-driven walking and stopping work as one closed-loop task, with measured speed and stopping-bout outputs.

### Phase 5 — Add one new sensory behavior at a time

Choose heading, odor, or escape. Trace its inputs and outputs, define its validation task, then add its UI controls.

**Gate:** The new behavior is reproducible and is not driven by a direct scene-to-animation rule.

### Phase 6 — Expo polish

Add pathway highlighting, model/data labels, repeat-trial comparisons, saved experiment presets, and measured performance numbers.

**Gate:** A visitor can run a complete trial and explain the path from stimulus to action.

## 9. Keep out of the first release

Do not promise all seven proposed sandboxes at once. Defer grooming and associative learning until the first sensorimotor loops work. Do not claim a full biological fly, zero assumptions, or zero-shot survival. Use connectome-constrained, model-generated, and predicted where those terms accurately describe the result.

## 10. Source references

- [FlyWire Codex FAQ and dataset releases](https://codex.flywire.ai/faq)
- [Shiu et al., A Drosophila computational brain model reveals sensorimotor processing, Nature (2024)](https://www.nature.com/articles/s41586-024-07763-9)
- [Sapkal et al., Neural circuit mechanisms underlying context-specific halting in Drosophila, Nature (2024)](https://www.nature.com/articles/s41586-024-07854-7)
- [Multimodal cue integration and learning in a neural representation of head direction, Nature Neuroscience (2025)](https://www.nature.com/articles/s41593-024-01823-z)
- [Converting an allocentric goal into an egocentric steering signal, Nature (2024)](https://www.nature.com/articles/s41586-023-07006-3)
- [Hampel et al., A suppression hierarchy among competing motor programs drives sequential grooming in Drosophila](https://pmc.ncbi.nlm.nih.gov/articles/PMC4136539/)
- [Motor neurons organize Drosophila feeding sequences via a disinhibitory cascade, Nature Neuroscience (2026)](https://www.nature.com/articles/s41593-026-02412-y)

