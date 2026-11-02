# NeuroFly Reference Methods Review: Shiu et al. (2024)

**Document:** Phase 1 Literature & Computational Model Review  
**Primary Reference:** Shiu, P. K., Hermundstad, A. M., & Murthy, M. (2024). *A Drosophila computational brain model reveals how neural circuits generate behavior.* **Nature**, 634(8032), 110–119. DOI: [10.1038/s41586-024-07763-9](https://doi.org/10.1038/s41586-024-07763-9)  
**Code Repository:** [github.com/philshiu/Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model)  
**Date Reviewed:** 2026-11-01  

---

## 1. Overview of Published Methods

Shiu et al. constructed a whole-brain computational model of *Drosophila melanogaster* based on the electron microscopy wiring diagram produced by the FlyWire consortium. The study demonstrated that simulating biophysical signal propagation through connectome-constrained wiring predicts functional sensorimotor transformations—specifically identifying feeding-initiation and grooming circuits that were subsequently validated through *in vivo* optogenetics and behavior.

### 1.1 Experimental Preparation & Connectomic Foundation
* **Dataset Used:** FlyWire FAFB (Full Adult Female Brain) version 630 (`2023_03_23_completeness_630_final.csv` and `2023_03_23_connectivity_630_final.parquet`).
* **Graph Scale:** 127,155 modeled neurons and over 50 million predicted chemical synapses.
* **Neurotransmitter Assignment:** Synaptic sign (+ for excitation, - for inhibition) derived from machine learning predictions (Eckstein et al., 2020). Acetylcholine was mapped as excitatory (+1); GABA and Glutamate were mapped as inhibitory (-1). Dopamine, Serotonin, and Octopamine were excluded from fast synaptic transmission or treated as modulatory.

---

## 2. Computational Architecture of the Shiu et al. Model

### 2.1 Neural Dynamics (Brian 2 Simulator)
The model was implemented in Python using the **Brian 2** spiking neural network simulator (`briansimulator.org`). Each neuron $i$ is modeled as a Leaky Integrate-and-Fire (LIF) unit:

$$\tau_m \frac{d V_i(t)}{dt} = (V_{\text{rest}} - V_i(t)) + R_m \cdot I_{\text{syn}, i}(t) + R_m \cdot I_{\text{ext}, i}(t)$$

When $V_i(t) \ge V_{\text{th}}$, a spike is emitted, $V_i$ is clamped to $V_{\text{reset}}$ for refractory period $\tau_{\text{ref}}$, and postsynaptic conductances are updated.

#### Published Biophysical Parameters:
* Membrane time constant: $\tau_m = 10.0\text{ ms}$
* Resting potential: $V_{\text{rest}} = -55.0\text{ mV}$
* Spike threshold: $V_{\text{th}} = -50.0\text{ mV}$
* Reset potential: $V_{\text{reset}} = -55.0\text{ mV}$
* Refractory period: $\tau_{\text{ref}} = 2.0\text{ ms}$
* Integration time step: $dt = 0.1\text{ ms}$
* Synaptic weight scaling: Synaptic efficacy $W_{ij}$ between presynaptic neuron $j$ and postsynaptic neuron $i$ is proportional to the detected EM synapse count $N_{ij}$:
  $$W_{ij} = \text{sign}_j \cdot w_0 \cdot N_{ij}$$
  where $\text{sign}_j \in \{+1, -1\}$ based on predicted transmitter, and $w_0$ is a global synaptic weight scaling coefficient fitted to reproduce physiological post-synaptic potential (PSP) amplitudes (~$0.2\text{ mV}$ per unitary synapse).

---

## 3. Feeding & Proboscis Extension Protocol in the Reference

### 3.1 Sensory Activation (`neu_sugar`)
* The authors isolated candidate sugar-sensing gustatory receptor neurons projecting from the proboscis/labellum to the subesophageal zone (SEZ).
* Sensory stimulation was modeled by driving Poisson spike generators at specified frequencies ($50–100\text{ Hz}$) or constant depolarizing current into `neu_sugar` IDs in the right SEZ.

### 3.2 Circuit Propagation & Motor Prediction
* Injected excitation propagated through polysynaptic SEZ pathways to recruit downstream premotor interneurons and proboscis motor neurons.
* **Target Motor Output:** Proboscis motor neuron **MN9** (muscle 9 motor neuron, rostrum protractor). Muscle 9 contracts to swing the rostrum forward, which is the foundational biomechanical step of the **proboscis extension response (PER)**.
* **In Vivo Validation:** Optogenetic activation (via CsChrimson) of the computational model's predicted intermediate feeding neurons induced robust proboscis extension in live flies, verifying the biological relevance of the predicted path.

---

## 4. Key Differences in NeuroFly's Scope

| Dimension | Shiu et al. (2024) *Nature* | NeuroFly Phase 1 MVP |
|---|---|---|
| **Simulation Scale** | Whole-brain (~127,155 neurons). High compute cluster required. | Compact extracted SEZ subgraph (~50–500 neurons) focused on the gustatory-to-MN9 pathway. |
| **Embodiment & World** | Open-loop, disembodied current injection. No physical body or spatial world. | Embodied in 3D NeuroFly Habitat; physical contact geometry drives sensory injection; motor spikes drive 3D body joints. |
| **Actuation** | Ends at neural prediction (membrane voltage / spike count in MN9). | Decodes MN9 spikes into continuous proboscis rotation, hold, and mechanical retraction. |
| **Connectome Snapshot** | Built on FlyWire v630 (`2023_03_23` freeze). | Targets canonical public FlyWire FAFB v783 with documented crosswalk to v630. |
| **Interactive Latency** | Offline batch simulation (minutes per trial). | Interactive local runtime capable of live session streaming and visitor-controlled intervention replay. |

---

## 5. Methodological Takeaways for NeuroFly Implementation

1. **Adopt LIF Parameters Faithfully:** When implementing the Phase 4 neural engine, use the published parameters ($\tau_m = 10\text{ ms}$, $V_{\text{th}} = -50\text{ mV}$, $V_{\text{rest}} = -55\text{ mV}$, $\tau_{\text{ref}} = 2\text{ ms}$) as the primary baseline before evaluating continuous rate alternatives.
2. **Preserve Linear Synapse-Count Scaling:** Use $W_{ij} \propto N_{ij}$ signed by predicted transmitter, avoiding arbitrary ad-hoc connection weights.
3. **Target MN9 as the Quantitative Endpoint:** Measuring spike count and latency in MN9 aligns NeuroFly's motor readout directly with the primary literature.

