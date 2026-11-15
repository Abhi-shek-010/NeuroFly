# NeuroFly Assay Specification: Taste Contact to Proboscis Response

**Document:** Phase 1 Assay Specification  
**Behavior Scope:** MVP Vertical Slice — Taste contact to proboscis extension response (PER)  
**Target Release:** FlyWire FAFB v783  
**Review Date:** 2026-11-14  
**Status:** Owner-approved for planning; specific FAFB v783 circuit remains unverified until Phase 3

---

## 1. Testable Research Question & Sensorimotor Hypothesis

### 1.1 Core Research Question
> **Can physical contact with a sucrose stimulus recruit a candidate SEZ circuit, after its FAFB v783 cell identities and connectivity are verified in Phase 3, to drive candidate proboscis motor-neuron firing and a modeled proboscis response, and does virtual silencing of selected intermediate nodes attenuate that response?**

### 1.2 Falsifiable Sensorimotor Hypothesis
1. **Sensorimotor Transformation Hypothesis:** Physical contact between the fly's labellar contact proxy and a sucrose patch generates simulated sensory drive in candidate sugar gustatory receptor neurons (GRNs). Synaptic excitation propagating through downstream SEZ interneurons drives action potential firing in proboscis motor neuron **MN9** above a baseline threshold.
2. **Causal Perturbation Hypothesis:** Virtually silencing candidate intermediate premotor interneurons (`Fdg` / SEZ premotor group) during sucrose contact will eliminate or significantly attenuate MN9 motor recruitment and resulting proboscis extension relative to an identical seed-matched intact trial.
3. **Falsification Criteria (Observations That Disconfirm the Model):**
   * *Contact Independence (False Positive):* Proboscis extension occurs in the absence of valid physical contact.
   * *Sensory Blindness:* MN9 fires identically when exposed to non-sugar (water, bitter) stimuli or under a sensory-blind control where input current is zeroed.
   * *Circuit Disconnection:* Simulation of the extracted FAFB v783 subgraph fails to propagate excitation from sugar GRNs to MN9 under biophysically plausible synaptic weights.
   * *Intervention Failure:* Virtual silencing of the intermediate premotor node produces no statistically significant difference in MN9 spike timing, spike count, or proboscis extension compared to the intact circuit.

These statements are predeclared hypotheses, not findings. Phase 1 has not verified the named sensory-to-output path or its individual edges in FAFB v783.

---

## 2. Rigorous Categorization of Assay Elements

In accordance with the NeuroFly evidence vocabulary, every element of the sensorimotor loop is classified below:

| Stage | Process / Element | Evidence Classification | Biological & Engineering Status |
|---|---|:---:|---|
| **1. World** | Patch location, sucrose concentration ($100\text{ mM}$ equivalent) | **Modeled** | Standard concentration used in *Drosophila* behavioral feeding assays (Shiu et al. 2024; Dethier 1976). Concentration-response relationship is a provisional model choice. |
| **2. Contact Event** | Spatial intersection between labellar contact proxy and stimulus patch | **Modeled** | Two operational modes: (A) Scripted deterministic contact fixture for regression testing; (B) Dynamic collision detection in the 3D Habitat. |
| **3. Sensory Encoding** | Translation of contact event into GRN electrical excitation | **Modeled** | Provisional uncalibrated model choice: Poisson spike train ($50\text{--}80\text{ Hz}$) or constant depolarizing current injection ($15\text{ pA}$) into candidate sugar GRNs. |
| **4. Circuit Connectivity** | Candidate chemical connections among sugar GRNs, SEZ interneurons, and MN9 | **Proposed / unverified for FAFB v783** | Exact root IDs and pair-specific edges must be queried in Phase 3; do not present the candidate path as measured in v783. |
| **5. Neurotransmitters** | Synaptic signs (excitatory vs. inhibitory) | **Inferred** | Automated per-synapse predictions (Eckstein et al. 2020; Schlegel et al. 2024). Acetylcholine = $+1$; GABA/Glutamate = $-1$. |
| **6. Neural Dynamics** | Membrane potentials, thresholds, synaptic decay | **Modeled** | Leaky Integrate-and-Fire (LIF) dynamics adopting Shiu et al. constants ($v_0 = -52\text{ mV}$, $v_{\text{th}} = -45\text{ mV}$, $t_{\text{ref}} = 2.2\text{ ms}$, $\tau_{\text{syn}} = 5\text{ ms}$). |
| **7. Motor Output** | Action potential trains emitted by motor neuron MN9 | **Predicted** | Model prediction of motor recruitment. |
| **8. Motor Decoding** | Translation of MN9 spikes into joint kinematic command | **Modeled** | Provisional uncalibrated engineering choice: First-order leaky accumulator with muscle time constant $\tau_m = 50\text{ ms}$ driving joint angle $\theta(t)$. |
| **9. Visible Action** | Proboscis rostrum extension, hold, and retraction | **Modeled / Display** | 3D articulated rig joint rotation ($\theta \in [0^\circ, 45^\circ]$). Displayed action is strictly driven by the motor decoder output. |

---

## 3. Standardized Trial Protocol & Contact Definitions

### 3.1 Distinction: Scripted Fixtures vs. Habitat Contact Events
To prevent conflating unit-test harnesses with interactive physics, NeuroFly formally defines two contact mechanisms:
* **Scripted Contact Fixture (Benchmarking Mode):** An artificial, deterministic timeline where contact is asserted at exactly $t = 100\text{ ms}$ and held for $250\text{ ms}$ while the fly body is stationary. Used exclusively for automated regression testing, CI validation, and parameter sanity checks.
* **Habitat-Generated Contact Event (Interactive Mode):** A dynamic event emitted by the 3D Habitat spatial engine when the fly's body/labellar collider geometry intersects the stimulus patch boundary in real time.

### 3.2 Standardized Baseline Trial Settings
* **Initial Body Pose:** Adult fly stationary on a flat arena floor ($z = 0$).
* **Proboscis State:** Fully retracted resting pose ($\theta_0 = 0.0^\circ$).
* **Neural State Initialization:** All membrane voltages set to resting potential ($V_i(0) = -52.0\text{ mV}$), zero active synaptic conductances, zero refractory timers.
* **Contact Geometry:** Distal labellar sphere proxy (radius $r_{\text{contact}} = 0.15\text{ mm}$); circular sucrose patch (radius $r_{\text{patch}} = 1.0\text{ mm}$).
* **Trial Timeline ($500\text{ ms}$ total window; $dt = 0.1\text{ ms}$):**
  * $0\text{ ms} \le t < 100\text{ ms}$: Baseline settling window (verifies no spontaneous resting spikes).
  * $100\text{ ms} \le t < 350\text{ ms}$: Contact stimulus window ($250\text{ ms}$ taste exposure).
  * $350\text{ ms} \le t \le 500\text{ ms}$: Post-contact recovery and mechanical retraction window.
* **Accounting for Trial Variability:** Repeated trials vary the integer random seed governing Poisson sensory spike arrival times. Evaluations report mean, standard deviation, and 95% confidence intervals across $N \ge 30$ seeded runs.

---

## 4. Input and Output Mapping Specifications

### 4.1 Stimulus-to-Sensory Mapping (Provisional Model Choice)
When valid contact is established with a sucrose patch, simulated sensory drive is injected into the identified candidate sugar GRNs:
$$I_{\text{inj}, i}(t) = \begin{cases} I_0 \cdot \frac{C}{C + K_d} & \text{if } t_{\text{contact}} \le t < t_{\text{release}} \text{ and } i \in \mathcal{S}_{\text{sugar}} \\ 0 & \text{otherwise} \end{cases}$$
* **Provisional Parameter Values:** $I_0 = 15.0\text{ pA}$ (provisional depolarizing current), $C = 100.0\text{ mM}$ (sucrose concentration), $K_d = 20.0\text{ mM}$ (half-saturation constant). Alternatively, a Poisson spike train with rate $\lambda = 60\text{ Hz} \cdot \frac{C}{C + K_d}$ will be injected.
* **Status:** These values are provisional engineering choices that will be calibrated during Phase 5.

### 4.2 Motor-Output-to-Proboscis Actuation (Provisional Model Choice)
Proboscis extension angle $\theta(t)$ is driven by MN9 spike accumulation:
$$\tau_m \frac{d A(t)}{dt} = -A(t) + \sum_{k} \delta(t - t_{\text{MN9}, k})$$
$$\theta(t) = \theta_{\text{max}} \cdot \frac{A(t)^n}{A_{50}^n + A(t)^n}$$
* **Provisional Parameter Values:** Maximum extension angle $\theta_{\text{max}} = 45.0^\circ$, muscle activation time constant $\tau_m = 50.0\text{ ms}$, Hill coefficient $n = 2$, half-maximal activation $A_{50} = 3\text{ spikes}$.
* **Response Threshold:** A positive extension response is defined as $\theta(t) \ge 20.0^\circ$.
* **Status:** The threshold ($\theta \ge 20^\circ$) and Hill function parameters are uncalibrated modeling assumptions. If biomechanical calibration in Phase 5 indicates a different muscle time constant, these parameters will be updated without modifying connectome provenance.

### 4.3 Null and Negative Outcome Representation
If the operational positive-response rule is not met (MN9 fires at least 5 spikes in the defined window and decoded angle reaches at least 20 degrees before trial end), log OUTCOME_NO_RESPONSE. Subthreshold spikes or angles may still occur. A no-response outcome is valid and is not replaced by an animation.

---

## 5. Intervention Definition and Equivalence Rules

* **Primary Silencing Mechanism (Shiu-Equivalent):** In silico silencing of candidate intermediate neurons (`Fdg` / SEZ premotor pool) will be implemented by **setting all outgoing synaptic weights to zero** ($W_{ij} = 0$). This matches the exact mathematical behavior of `model.py` in the reference repository.
* **Alternative Modeled Mechanism (Voltage Clamping):** Clamping membrane voltage to hyperpolarized potential ($V_{\text{clamp}} = -70.0\text{ mV}$).
* **Documentation Rule:** NeuroFly will explicitly record whether synaptic disconnection or voltage clamping was used in each evaluation run, avoiding claims of equivalence with Shiu et al. unless synaptic zeroing is employed.
