# NeuroFly Assay Specification: Taste Contact to Proboscis Response

**Document:** Phase 1 Assay Specification  
**Behavior Scope:** MVP Vertical Slice — Taste contact to proboscis extension response (PER)  
**Status:** Working specification; candidate for Phase 1 signoff  

---

## 1. Testable Research Question & Hypothesis

### 1.1 Core Question
> **Can physical contact with a sucrose stimulus recruit a connectome-derived subesophageal circuit to drive firing in candidate proboscis motor neurons (such as MN9) and produce visible proboscis extension, and does virtual silencing of candidate intermediate nodes significantly attenuate this response?**

### 1.2 Falsifiable Sensorimotor Hypothesis
1. **Primary Sensorimotor Premise:** Physical contact between the fly's gustatory contact proxy (labellar or tarsal sensilla) and a sucrose patch activates modeled sugar-sensing gustatory receptor neurons (GRNs). Synaptic excitation propagating through the connected subesophageal zone (SEZ) circuit drives the firing of proboscis motor neuron MN9 above its baseline threshold.
2. **Causal Intervention Premise:** Virtually silencing identified intermediate interneurons (or the sensory population) in the intact network during sucrose contact will eliminate or significantly delay MN9 motor neuron activation and resulting proboscis extension relative to a seed-matched intact baseline.
3. **Falsification Criteria (What Disconfirms the Hypothesis):**
   * *False Positive / Causality Failure:* Proboscis extension occurs in the absence of valid physical contact (violates contact-dependence).
   * *Sensory Insensitivity:* The motor neuron MN9 fires identically when exposed to non-sugar (e.g., pure water or bitter) stimuli or under a sensory-blind control.
   * *Circuit Disconnection:* Simulation of the extracted connectome subgraph fails to propagate excitation from sugar GRNs to MN9 (resulting in complete motor quiescence under physiological weights).
   * *Perturbation Failure:* Virtual silencing of key bottleneck intermediate nodes produces no significant change in MN9 spike timing or probability compared to the intact circuit.

---

## 2. Evidence Categorization of the Sensorimotor Loop

| Stage | Process | Classification | Biological / Modeling Basis |
|---|---|:---:|---|
| **1. World** | Patch placement, sugar concentration (100 mM sucrose equivalent) | **Modeled** | Standard sucrose concentration used in Drosophila feeding assays (Shiu et al. 2024; Dethier 1976). |
| **2. Contact** | Labellar/tarsal contact proxy intersects patch collision geometry | **Modeled** | Rigid-body sphere-plane collision detection; generates timestamped `ContactEvent`. |
| **3. Sensory Encoding** | `ContactEvent` triggers spike generator in candidate sugar GRNs | **Modeled** | Poisson spike train or step current injection (50–100 Hz equivalent) into identified sugar GRNs. |
| **4. Circuit Wiring** | Synaptic connections between sugar GRNs, SEZ interneurons, and MN9 | **Measured** | Directed synapse counts and topologies from FlyWire FAFB v783 / v630. |
| **5. Neurotransmitters** | Synaptic signs (excitatory vs. inhibitory) | **Inferred** | Machine-learning predicted transmitters (acetylcholine = +, GABA/glutamate = -) from FlyWire annotations. |
| **6. Neural Dynamics** | Membrane potentials, spike thresholds, synaptic currents | **Modeled** | Leaky Integrate-and-Fire (LIF) biophysics with parameters adapted from Shiu et al. (2024). |
| **7. Motor Output** | MN9 spike trains / action potentials | **Predicted** | Model output predicting muscle 9 recruitment. |
| **8. Motor Decoding** | MN9 spike count / frequency converted to rostrum protractor angle | **Modeled** | Leaky integrator / sigmoid actuator mapping: extension angle $\theta(t)$, hold duration, and passive retraction. |
| **9. Visible Action** | Proboscis extension, hold, and retraction | **Modeled / Display** | 3D articulated rig joint rotation driven solely by decoded motor state. |

---

## 3. Standardized Trial Protocol

### 3.1 Initial Conditions & Starting State
* **Body State:** Adult fly positioned in a stationary stance on a flat, neutral arena floor ($z = 0$).
* **Proboscis State:** Fully retracted resting pose ($\theta_0 = 0^\circ$).
* **Neural State:** All membrane potentials initialized to resting potential ($V_{\text{rest}} = -55\text{ mV}$), zero synaptic conductances, zero refractory timers.
* **Internal State:** Satiation/hunger multiplier is fixed to a standardized baseline (equivalent to starved/motivated feeding state in Shiu et al. 2024); internal state modulation is held constant for the MVP.

### 3.2 Stimulus & Contact Geometry
* **Stimulus Patch:** Circular surface patch (radius $r = 1.0\text{ mm}$), positioned immediately adjacent to the fly's anterior reach.
* **Contact Boundary:** A localized sphere proxy (radius $0.15\text{ mm}$) at the distal tip of the proboscis/labellum.
* **Valid Contact Definition:** An intersection between the contact proxy and the stimulus patch boundary. Contact onset is recorded as $t_{\text{contact}}$ ($t = 100\text{ ms}$ into a standard trial). Contact offset occurs when the fly body or proboscis moves out of range.

### 3.3 Trial Timing & Replay Rules
* **Trial Duration:** Standardized $500\text{ ms}$ simulation window (5,000 steps at $dt = 0.1\text{ ms}$).
  * $0\text{ ms} \le t < 100\text{ ms}$: Baseline baseline settling / silence window (verifies no spontaneous firing).
  * $100\text{ ms} \le t < 350\text{ ms}$: Stimulus contact window ($250\text{ ms}$ taste exposure).
  * $350\text{ ms} \le t \le 500\text{ ms}$: Post-contact recovery and retraction window.
* **Deterministic Seeds:** Every trial records an integer random seed controlling Poisson sensory spike generation. Seed-matched paired trials guarantee that differences between baseline and intervention runs stem strictly from circuit modifications.

---

## 4. Input and Output Mapping Hypotheses

### 4.1 Stimulus-to-Sensory Mapping
When valid contact is established with a sucrose patch, a constant current or equivalent Poisson input is delivered exclusively to the pre-identified candidate sugar GRNs:
$$I_{\text{inj}, i}(t) = \begin{cases} I_0 \cdot \frac{C}{C + K_d} & \text{if } t_{\text{contact}} \le t < t_{\text{release}} \text{ and } i \in \mathcal{S}_{\text{sugar}} \\ 0 & \text{otherwise} \end{cases}$$
where $I_0 = 15\text{ pA}$, $C = 100\text{ mM}$ sucrose, and $K_d = 20\text{ mM}$ is the half-maximal saturation constant. For bitter stimuli, $I_{\text{inj}} = 0$ for $\mathcal{S}_{\text{sugar}}$, routing instead to bitter GRNs.

### 4.2 Motor-Output-to-Proboscis Actuation
Proboscis extension angle $\theta(t)$ is controlled by the firing rate of proboscis motor neuron MN9, decoded via a first-order leaky accumulator:
$$\tau_m \frac{d A(t)}{dt} = -A(t) + \sum_{k} \delta(t - t_{\text{MN9}, k})$$
$$\theta(t) = \theta_{\text{max}} \cdot \frac{A(t)^n}{A_{50}^n + A(t)^n}$$
where $\theta_{\text{max}} = 45^\circ$, $\tau_m = 50\text{ ms}$ (muscle activation time constant), Hill coefficient $n = 2$, and $A_{50}$ represents the half-maximal spike count threshold. When $A(t) < A_{\text{threshold}}$, $\theta(t) \to 0$ (passive mechanical return to resting pose).

### 4.3 Null and Negative Outcome Representation
If the circuit does not reach the motor firing threshold $A_{\text{threshold}}$, $\theta(t)$ remains $0^\circ$. The simulation marks the trial as `OUTCOME_NO_RESPONSE`. This is rendered as a stationary, retracted proboscis and logged as a valid experimental observation, rather than defaulting to an animation or error state.

