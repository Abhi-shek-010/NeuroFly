# NeuroFly Reference Methods Review: Shiu et al. (2024)

**Document:** Phase 1 Literature & Computational Model Review  
**Primary Reference:** Shiu, P. K., Sterne, G. R., Spiller, N., et al. (2024). *A Drosophila computational brain model reveals sensorimotor processing.* **Nature**, 634, 210–219. DOI: [10.1038/s41586-024-07763-9](https://doi.org/10.1038/s41586-024-07763-9)
**Reference Codebase:** [github.com/philshiu/Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model) (`model.py`, `example.ipynb`, `utils.py`)  
**Review Date:** 2026-11-14  
**Status:** Owner-reviewed; corrected reference facts and scope-limited

---

## 1. Executive Summary & Citation Trace

Shiu et al. (2024) developed a whole-brain, leaky integrate-and-fire (LIF) computational model of the adult female *Drosophila melanogaster* brain based on the FlyWire electron microscopy (EM) connectome. The study simulated signal propagation from sensory inputs through the central brain and subesophageal zone (SEZ) to predict downstream motor outputs, with a primary focus on feeding initiation (proboscis extension) and grooming.

This review systematically compares what is published in the **Nature paper and supplementary information** against the author's **public reference implementation** (`philshiu/Drosophila_brain_model`). Modeling assumptions and software defaults in the reference codebase are explicitly distinguished from empirical biological measurements.

---

## 2. Direct Comparison: Published Paper vs. Reference Repository

The following matrix documents the exact parameters, equations, and mechanisms in both sources:

| Component / Parameter | Published Paper & Supplement (Shiu et al. 2024) | Reference Code (`philshiu/Drosophila_brain_model`) | NeuroFly Analysis & Distinction |
|---|---|---|---|
| **Underlying Connectome Snapshot** | FlyWire FAFB v630 freeze (`2023_03_23` release; 127,155 neurons, ~53 million chemical synapses). | Default paths point to `2023_03_23_completeness_630_final.csv` and `2023_03_23_connectivity_630_final.parquet`. Configuration dictionary permits swapping to v783 files. | **Measured Connectome**: v630 was the pre-release proofreading freeze. Public canonical release is v783 (Zenodo 10676866). Root IDs differ between snapshots due to continued proofreading. |
| **Simulator Platform** | Brian 2 simulator (Python / C++ code generation). | Brian 2 (`brian2`), configured with C++ standalone/weave acceleration where available. | **Implementation**: NeuroFly will evaluate Brian 2 or equivalent sparse matrix operations in Python for Phase 4. |
| **Resting Membrane Potential ($v_0$)** | $-52\text{ mV}$ (phenomenological parameter inherited from *Drosophila* modeling literature, Kakaria & de Bivort 2017). | `default_params['v_0'] = -52 * mV` in `model.py`. | **Modeled Parameter**: Not a cell-specific patch-clamp measurement. Uniform across all 127k modeled neurons. |
| **Reset Potential ($v_{\text{rst}}$)** | $-52\text{ mV}$ (voltage clamped to resting baseline immediately following an action potential). | `default_params['v_rst'] = -52 * mV` in `model.py`. | **Modeled Parameter**: Standard integrate-and-fire reset rule. |
| **Spike Threshold ($v_{\text{th}}$)** | $-45\text{ mV}$ ($7\text{ mV}$ depolarization above rest required for action potential generation). | `default_params['v_th'] = -45 * mV` in `model.py`. | **Modeled Parameter**: Fixed global threshold across all non-sensory neuron classes. |
| **Membrane Time Constant (t_mbr)** | 20 ms. | default_params key t_mbr = 20 ms in model.py. | **Modeled Parameter**: Uniform model setting; not a cell-specific patch-clamp value. |
| **Refractory Period (t_ref)** | 2.2 ms absolute refractory duration after threshold crossing. | default_params key t_rfc = 2.2 ms in model.py. | **Modeled Parameter**: The code key is t_rfc; this is a model setting, not a cell-specific measurement. |
| **Synaptic Decay Constant (tau)** | 5.0 ms exponential synaptic decay time constant. | default_params key tau = 5 ms in model.py. | **Modeled Dynamics**: The reference code key is tau, not tau_syn. |
| **Synaptic Transmission Delay (t_dly)** | 1.8 ms. | default_params key t_dly = 1.8 ms in model.py. | **Modeled Parameter**: Reference-model delay; retain as a software/model assumption if adopting this implementation. |
| **Synaptic Weight Scaling (W_ij)** | The model weight combines synapse count, presynaptic sign, and Wsyn. Wsyn = 0.275 mV is the model free parameter selected so 100 Hz sugar GRN activation produced roughly 80% of maximal MN9 firing in the published model. | default_params key w_syn = 0.275 mV in model.py; the code applies synapse count and presynaptic sign. | **Modeled Transformation**: 0.275 mV is not a directly measured unitary EPSP. The fitted scale and linear synapse-count rule are modeling choices. |
| **Neurotransmitter Assignment** | Eckstein et al. (2020) per-synapse automated predictions. Acetylcholine $\to$ excitatory (+1); GABA and Glutamate $\to$ inhibitory (-1). Biogenic amines excluded from fast transmission. | Annotations table provides transmitter probabilities; sign applied as $+1$ or $-1$ based on dominant prediction. | **Inferred Biology**: Over 95% classification confidence for cholinergic/GABAergic/glutamatergic cells, but functional sign remains a computational inference. |
| **Sensory Drive / Activation** | In silico activation of sugar-sensing gustatory receptor neurons (`neu_sugar`) in the SEZ via independent Poisson spike trains. In vivo validation via optogenetics (CsChrimson). | `default_params['r_poi'] = 150 * Hz` in `model.py`. Optional secondary drive `r_poi2 = 0 * Hz`. Duration `t_run = 1000 * ms`. | **Software Default vs. Biology**: `150 Hz` in the code is a synthetic optogenetic stimulation rate, **not** a measurement of physiological GRN firing during natural feeding contact. |
| **Circuit Silencing Mechanism** | Candidate neurons are silenced in silico to evaluate downstream model output; the paper compares predictions with experimental inhibition. | The reference silence function sets weights of synapses from selected neurons to zero, removing their outgoing transmission. | **NeuroFly Implementation Distinction**: This is outgoing synaptic zeroing, not incoming-and-outgoing disconnection, membrane hyperpolarization, or voltage clamping. |
| **Target Motor Endpoint** | Motor Neuron 9 (**MN9**), the rostrum protractor motor neuron innervating Muscle 9 of the proboscis. Firing of MN9 corresponds to feeding initiation / proboscis extension response (PER). | Firing rates and spike counts of MN9 are recorded across runs to predict proboscis extension probability. | **Measured Anatomy / Modeled Motor**: MN9 anatomy is EM-measured; translation of MN9 spike rate into physical joint angles is modeled in NeuroFly. |

---

## 3. Feeding Circuitry and Sensorimotor Scope

### 3.1 The Published Feeding Pathway
Shiu et al. demonstrated that optogenetic stimulation of sweet-sensing gustatory receptor neurons projecting from the labellum to the SEZ activates a polysynaptic feeding circuit:
1. **Sensory Reception:** Sugar-sensing GRNs project via the labellar nerve into the SEZ.
2. **Second-Order Interneurons:** Local SEZ interneurons (including G2Ns and command-like interneurons such as `Fdg`) integrate gustatory drive.
3. **Motor Recruitment:** SEZ interneurons converge on proboscis motor neurons, notably **MN9** (rostrum protractor), driving rostrum extension.
4. **Validation:** Optogenetic activation of predicted intermediate interneurons in vivo elicited robust proboscis extension in food-deprived flies, confirming the functional role of the connectome pathway.

### 3.2 Critical Scope Differences for NeuroFly

1. **Whole-Brain vs. Extracted Subgraph:**
   * *Shiu et al.:* Simulates all 127,155 neurons across the entire brain simultaneously on multi-core compute clusters.
   * *NeuroFly:* Extracts a compact, verified SEZ gustatory-to-motor subgraph (~tens to hundreds of neurons) to achieve low-latency interactive simulation in a browser session worker.
2. **Embodied Sensorimotor Feedback vs. Open-Loop Injection:**
   * *Shiu et al.:* Disembodied simulation. Stimulation is an artificial Poisson spike train directly injected into selected neuron IDs without physical space or body geometry.
   * *NeuroFly:* Embodied in the 3D NeuroFly Habitat. Spatial collision between the fly's body/labellar proxy and an arena sucrose patch triggers sensory encoding; motor neuron output drives continuous 3D proboscis joint kinematics, updating subsequent contact.
3. **Actuation & Biomechanics:**
   * *Shiu et al.:* Simulation terminates at motor neuron spike predictions (membrane potential and spike counts of MN9).
   * *NeuroFly:* Implements an explicit, calibrated motor decoder mapping MN9 spike accumulation to continuous joint angles (extension, hold, and mechanical retraction).
4. **Connectome Snapshot Baseline:**
   * *Shiu et al.:* Based on pre-release FlyWire v630.
   * *NeuroFly:* Targets canonical FlyWire FAFB v783 (Zenodo 10676866); Phase 3 must perform release-specific identity reconciliation, with coordinates used only as supporting evidence.

---

## 4. Methodological Guidelines for NeuroFly Phase 2–4

1. **Reference Parameter Integrity:** If NeuroFly adopts a Shiu-style LIF model, record the reference settings as model defaults: v_0 = -52 mV, v_rst = -52 mV, v_th = -45 mV, t_mbr = 20 ms, tau = 5 ms, t_rfc = 2.2 ms, t_dly = 1.8 ms, and w_syn = 0.275 mV. These are model parameters, not all biological measurements.
2. **Distinguish Natural Contact from Optogenetic Drive:** The code default r_poi = 150 Hz is a synthetic Poisson stimulation setting, not a measured natural-contact firing rate. NeuroFly must not claim a physiological contact rate until its sensory encoding is calibrated in Phase 5.
3. **Model Silencing via Outgoing Synaptic Zeroing:** To match the reference code mechanism, NeuroFly may zero outgoing synaptic weights from the target group. Record this exact operation; voltage clamping is a separate modeled intervention.
