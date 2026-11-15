# NeuroFly Cell and Edge Evidence Register

**Document:** Phase 1 Biological Cell and Synaptic Connectivity Register  
**Circuits in Scope:** Gustatory sensory input, subesophageal zone (SEZ) interneurons, and proboscis motor neuron MN9  
**Target Release:** FlyWire FAFB v783 (with reference mapping to v630)  
**Review Date:** 2026-11-14  
**Status:** Owner-approved with scope limitation; FAFB v783 identities and edges remain unresolved until Phase 3

---

## 1. Candidate Cell Register

The following register identifies candidate cell classes for the taste-contact to proboscis extension loop. No unverified 64-bit root IDs are invented. Individual FAFB v783 root IDs and pair-specific synapse counts remain unresolved for Phase 3. Literature and cell-class evidence below do not establish these identities or edges in the v783 snapshot; this is a candidate register, not a verified v783 subgraph.

| Release | Cell Class / Type Key | Anatomical Neuropil | Proposed Functional Role | Predicted Neurotransmitter & Confidence | Evidence Source | Type-Level Confidence & Rationale | Unresolved Uncertainties |
|---|---|---|---|:---:|---|---|---|
| **FAFB v783** *(Ref: v630 `neu_sugar`)* | `GRN_sugar_labellar` (Sensory class; Gr5a/Gr64 expressing) | Labellar nerve $\to$ SEZ (Gnathal Ganglion) | Primary sweet gustatory reception; responds to sucrose contact | **Acetylcholine** (Excitatory, $+1$); Confidence: **High** (>95% automated prediction) | Shiu et al. (2024); Schlegel et al. (2024); Dethier (1976) | **High at the cell-class level only:** Published anatomy supports the projection; the exact FAFB v783 root identity is not verified. | Exact 64-bit Root IDs in v783 and sensilla-specific receptor tuning pending Phase 3 query against `annotations_v783`. |
| **FAFB v783** *(Ref: v630 G2N pool)* | `G2N` / `SEZ_interneuron_gustatory` | SEZ central neuropil | Second-order gustatory processing; feedforward excitation and local integration | **Acetylcholine** ($+1$) or **GABA** ($-1$); Confidence: **Medium** | Shiu et al. (2024); Bohra et al. (2018); Schlegel et al. (2024) | **Medium at the cell-class level only:** Published analyses motivate this candidate; the exact FAFB v783 identities and edge are unverified. | Specific intermediate interneuron branching and transmitter mixture pending Phase 3 connectivity extraction. |
| **FAFB v783** *(Ref: v630 feeding command)* | `Fdg` / `SEZ_premotor_feeding` | Ventral / lateral SEZ | Command-like premotor interneuron promoting feeding initiation; virtual silencing target | **Acetylcholine** (Excitatory, $+1$); Confidence: **Medium** | Flood et al. (2013); Shiu et al. (2024) | **Medium at the cell-class level only:** Published feeding evidence supports this candidate; the exact FAFB v783 identity and edge remain unresolved. | Exact v630-to-v783 identity and v783 edge query pending Phase 3; coordinates are corroborating localizers only. |
| **FAFB v783** *(Ref: v630 `MN9`)* | `MN9` (Motor Neuron 9 / Rostrum Protractor Motor Neuron) | SEZ $\to$ Rostrum muscle 9 (efferent nerve) | Direct motor drive to rostrum protractor muscle; physical driver of proboscis extension | **Glutamate** (Excitatory at insect NMJ, $+1$); Confidence: **High** | McKellar et al. (2020); Shiu et al. (2024); Schlegel et al. (2024) | **High at the cell-class level only:** Published anatomy supports the motor role; the exact FAFB v783 root identity is unresolved. | Efferent neuromuscular junction (NMJ) biophysics and muscle contraction dynamics are modeled, not measured by EM. |

---

## 2. Candidate Synaptic Pathway Register

The hypothesized causal pathway traces feedforward excitation from peripheral sucrose contact to proboscis motor recruitment:

```
[Physical Contact: Sucrose Patch]
                 │
                 ▼
     [GRN_sugar_labellar]             (Sensory Receptors, SEZ)
                 │
                 ▼ (Direction: Feedforward; Transmitter: Acetylcholine)
     [G2N / SEZ Interneurons]         (Second-Order Gustatory Processors)
                 │
                 ▼ (Direction: Premotor Drive; Transmitter: Acetylcholine)
     [Fdg / SEZ Premotor Pool]        (Feeding Command Hub — Virtual Lesion Target)
                 │
                 ▼ (Candidate motor direction; FAFB v783 extraction pending)
     [MN9 (Motor Neuron 9)]           (Rostrum Protractor Motor Neuron, SEZ)
                 │
                 ▼ (Neuromuscular Junction Drive; Modeled)
     [Muscle 9 (Rostrum Protractor)]  ===>  Proboscis Extension Response (PER)
```

| Pathway Stage | Direction | Presynaptic Group | Postsynaptic Group | Neuropil | Synapse Count & Threshold | Evidence Type | Confidence | Biological Interpretation & Limits |
|---|:---:|---|---|---|---|:---:|:---:|---|
| **Stage 1: Sensory to 2nd Order** | Pre to Post | GRN sugar labellar | G2N SEZ | SEZ / GNG | Not extracted for v783; Nsyn >= 3 is a proposed engineering filter only. | Literature-supported candidate; v783 edge unverified | Not assessed for FAFB v783 | No v783 root IDs or pair-specific counts have been queried; do not describe this as a measured v783 edge. |
| **Stage 2: 2nd Order to Premotor** | Pre to Post | G2N SEZ | Fdg / Premotor | SEZ | Not extracted for v783; Nsyn >= 3 is a proposed engineering filter only. | Literature-supported candidate; v783 edge unverified | Not assessed for FAFB v783 | Published circuit analyses motivate the candidate route, but exact v783 identities, direct edges, and counts remain unverified. |
| **Stage 3: Premotor to Motor** | Pre to Post | Fdg / Premotor | MN9 | SEZ | Not extracted for v783; Nsyn >= 3 is a proposed engineering filter only. | Literature-supported candidate; v783 edge unverified | Not assessed for FAFB v783 | A reference-model result does not verify the corresponding v783 root IDs or pair-specific edge. |
| **Stage 4: Motor $\to$ Muscle** | Pre $\to$ Post | `MN9` | `Muscle 9` | Rostrum (Cephalic) | N/A (Axonal NMJ innervation outside EM brain volume). | **Modeled** | **High** (Anatomy) / **Modeled** (Dynamics) | Peripheral muscle innervation pattern is biologically verified; muscle force and joint rotation are modeled. |

---

## 3. Intervention Candidate Specification

* **Candidate Virtual Silencing Target:** `Fdg` / feeding-initiation premotor interneuron group.
* **Mechanism in Reference Code:** Shiu et al. zero the weights of synapses from the selected neurons, which removes their outgoing transmission. The reference code does not zero incoming synapses or clamp membrane voltage.
* **NeuroFly Implementation Choice:**
  * *Primary Method (Shiu-style):* Zeroing outgoing synaptic conductances from the selected neurons (W_eff = 0).
  * *Alternative Modeled Method:* Sustained hyperpolarizing voltage clamp ($V_{\text{clamp}} = -70\text{ mV}$).
  * *Integrity Rule:* NeuroFly will explicitly state which silencing method is active during an evaluation run, avoiding claims of strict mathematical equivalence unless the synaptic zeroing method is used.
* **Uncertainty & Narrowing Rule:** If the Phase 3 extraction query reveals that feedforward connectivity between G2N, Fdg, and MN9 in FAFB v783 is disynaptic through parallel collateral interneurons rather than a strict single-cell bottleneck, the virtual silencing target will be broadened to the verified premotor pool, or the causal claim will be narrowed accordingly.
