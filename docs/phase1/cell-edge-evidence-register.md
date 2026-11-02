# NeuroFly Cell and Edge Evidence Register

**Document:** Phase 1 Biological Cell and Synaptic Connectivity Register  
**Circuits in Scope:** Gustatory sensory input, subesophageal zone (SEZ) premotor interneurons, and proboscis motor neuron MN9  
**Status:** Candidate register compiled from primary literature and FlyWire consensus typing  

---

## 1. Candidate Cell Register

| Release | Cell Type / Label | Anatomical Region | Proposed Functional Role | Predicted Transmitter | Evidence Source | Confidence & Rationale | Known Uncertainties |
|---|---|---|---|:---:|---|---|---|
| **FAFB v783 / v630** | `GRN_sugar_labellar` (population) | Labellar nerve $\to$ SEZ | Primary sugar gustatory sensory input; responds to sucrose contact | Acetylcholine (+1) | Shiu et al. (2024); Schlegel et al. (2024) | **High**: Well-characterized Gr5a/Gr64 expressing sensilla projecting to SEZ. | Exact receptor tuning across individual sensilla variants is simplified to a single sugar class. |
| **FAFB v783 / v630** | `G2N` / `SEZ_interneuron_gustatory` | SEZ (central neuropil) | Second-order gustatory interneuron; relays and integrates sensory excitation | Acetylcholine (+1) or GABA (-1) | Shiu et al. (2024); Bohra et al. (2018) | **Medium-High**: Identified as direct postsynaptic partners of sugar GRNs in FlyWire. | Polysynaptic branching; transmitter prediction confidence varies across individual cells. |
| **FAFB v783 / v630** | `Fdg` / `SEZ_premotor_feeding` | Ventral / lateral SEZ | Command-like premotor interneuron promoting feeding initiation | Acetylcholine (+1) | Flood et al. (2013); Shiu et al. (2024) | **Medium**: Established feeding-regulatory interneurons; strong links to rostrum motor outputs. | Exact individual neuron root ID mapping between v630 and v783 to be extracted in Phase 3. |
| **FAFB v783 / v630** | `MN9` (Motor Neuron 9) | SEZ $\to$ Rostrum muscle 9 | Motor neuron driving rostrum protractor muscle (initiates proboscis extension) | Glutamate (NMJ excitatory) | Shiu et al. (2024); McKellar et al. (2020); Schlegel et al. (2024) | **High**: Classic, anatomically verified proboscis extension motor neuron in EM and light microscopy. | Neuromuscular junction (NMJ) biophysics and muscle activation dynamics are modeled, not measured by EM. |

---

## 2. Candidate Synaptic Path & Connectivity Register

The candidate structural pathway traces feeding initiation from labellar contact to motor actuation:

```
[Sugar Stimulus]
       │
       ▼ (Physical Contact)
[GRN_sugar_labellar]  (Sensory Receptors in SEZ)
       │
       ▼ (Direct & Polysynaptic Excitatory Synapses; Ach)
[G2N / SEZ Interneurons]  (Second-Order Gustatory Processors)
       │
       ▼ (Premotor Excitatory Drive; Ach)
[Fdg / SEZ Premotor Pool]  (Feeding Initiation Command Hub)
       │
       ▼ (Direct Synaptic Input; Measured in Connectome)
[MN9 (Motor Neuron 9)]  (Rostrum Protractor Motor Neuron)
       │
       ▼ (Neuromuscular Glutamatergic Drive)
[Muscle 9 (Rostrum Protractor)]  ===>  Proboscis Extension Response (PER)
```

| Pathway Stage | Presynaptic Group | Postsynaptic Group | Structural Metric | Evidence Type | Confidence | Biological Interpretation & Limits |
|---|---|---|---|:---:|:---:|---|
| **Stage 1: Sensory $\to$ 2nd Order** | `GRN_sugar_labellar` | `G2N_SEZ` | Direct chemical synapses (EM verified) | **Measured** | High | Structural connectivity demonstrates sensory convergence in the SEZ; synaptic weights scaled linearly from synapse count. |
| **Stage 2: 2nd Order $\to$ Premotor** | `G2N_SEZ` | `Fdg / Premotor` | Polysynaptic and direct feedforward synapses | **Measured / Inferred** | Medium-High | Feedforward excitation supported by connectomic path search; some lateral inhibitory interneurons present. |
| **Stage 3: Premotor $\to$ Motor** | `Fdg / Premotor` | `MN9` | Monosynaptic connections onto MN9 dendrites | **Measured** | High | Shiu et al. (2024) identified direct and disynaptic connectivity between feeding interneurons and MN9. |
| **Stage 4: Motor $\to$ Muscle** | `MN9` | `Muscle 9` | Efferent axonal innervation of rostrum protractor | **Modeled** | High (Anatomy) / Modeled (Mechanics) | Innervation pattern is biologically measured (McKellar 2020); motor lag, muscle tension, and joint rotation are modeled. |

---

## 3. Intervention Candidate Selection

* **Candidate Virtual Silencing Target:** `Fdg` / key bottleneck SEZ premotor interneuron group.
* **Biological Rationale:** Previous functional studies (Flood et al. 2013) and computational simulations (Shiu et al. 2024) demonstrate that silencing feeding command interneurons blocks sugar-induced proboscis extension without damaging peripheral sensory reception or baseline motor capacity.
* **NeuroFly Modeling Mechanism:** Setting synaptic transmission efficacy or clamping membrane voltage of the selected intermediate node to $V_{\text{clamp}} = -70\text{ mV}$ during a sugar-contact trial.

