# NeuroFly Phase 1 Evaluation Protocol: Metrics, Intervention, and Controls

**Document:** Phase 1 Quantitative Evaluation Protocol  
**Scope:** Verification rules for the Taste-Contact to Proboscis Extension MVP  
**Status:** Predeclared protocol; candidate for Phase 1 signoff  

---

## 1. Quantitative Performance Measures

### 1.1 Primary Metric: Motor Response Probability ($P_{\text{PER}}$)
* **Definition:** The proportion of valid stimulus contact trials that elicit a functional proboscis motor response:
  $$P_{\text{PER}} = \frac{N_{\text{response}}}{N_{\text{trials}}}$$
* **Operational Response Criterion:** A trial is classified as a positive response ($R = 1$) if and only if:
  1. Proboscis motor neuron **MN9** fires $\ge 5$ action potentials within the stimulus window ($100\text{ ms} \le t \le 350\text{ ms}$).
  2. Decoded extension angle reaches $\theta(t) \ge 20.0^\circ$ prior to trial termination ($t = 500\text{ ms}$).
* **Target Success Threshold:** $P_{\text{PER}} \ge 0.90$ across $N = 50$ randomized, seed-controlled trials with $100\text{ mM}$ sucrose.

### 1.2 Secondary Metrics
* **Response Latency ($\Delta t_{\text{lat}}$):** Time elapsed from physical contact onset ($t_{\text{contact}} = 100\text{ ms}$) to the first action potential in MN9 ($t_{\text{first}}$):
  $$\Delta t_{\text{lat}} = t_{\text{first}} - t_{\text{contact}}$$
  *Biological Expectation:* $15\text{ ms} \le \Delta t_{\text{lat}} \le 60\text{ ms}$ (accounting for synaptic delays across 2–4 synapses in the SEZ).
* **Taste Selectivity Index ($\text{SI}$):**
  $$\text{SI} = P_{\text{PER}}(\text{Sucrose}) - P_{\text{PER}}(\text{Water / Bitter})$$
  *Success Threshold:* $\text{SI} \ge 0.80$ (demonstrates chemical specificity).

---

## 2. Predeclared Virtual Intervention Experiment

### 2.1 Experimental Design
Every evaluation consists of seed-matched paired runs:
1. **Condition A (Intact Baseline):** Intact connectome subgraph, $100\text{ mM}$ sucrose contact, seed $S_k$.
2. **Condition B (Virtual Lesion / Silencing):** Clamping the candidate bottleneck premotor node (`Fdg` / SEZ premotor group) to hyperpolarized resting potential ($V_{\text{clamp}} = -70\text{ mV}$, preventing spike generation), $100\text{ mM}$ sucrose contact, identical seed $S_k$.

### 2.2 Predeclared Falsifiable Prediction
> **Hypothesis:** Under identical initial body pose, contact timing, and stimulus strength, virtual silencing of the intermediate feeding premotor node will produce a statistically significant reduction in proboscis motor recruitment:
> $$P_{\text{PER}}(\text{Silenced}) \le 0.10 \quad \text{vs.} \quad P_{\text{PER}}(\text{Intact}) \ge 0.90$$
> If virtual silencing of the intermediate node fails to significantly attenuate MN9 firing ($P_{\text{PER}} > 0.30$), the hypothesis that this pathway forms a necessary causal bottleneck is rejected, requiring re-tracing of alternative collateral paths.

---

## 3. Negative Controls & Baseline Comparison Suite

To ensure that successful behavior cannot be achieved by trivial, sensory-blind, or spurious mechanisms, every evaluation run must report the following control matrix:

| Control Type | Experimental Manipulation | Expected Outcome | Causal Hypothesis Challenged |
|---|---|---|---|
| **1. No-Contact Control** | Sugar patch placed out of physical reach ($d > 2\text{ mm}$). | $P_{\text{PER}} = 0.00$; zero MN9 spikes. | Verifies behavior depends on true physical contact, ruling out unprovoked spontaneous firing. |
| **2. No-Sensory Control** | Contact occurs, but sensory encoder injection current clamped to zero ($I_{\text{inj}} = 0$). | $P_{\text{PER}} = 0.00$; zero MN9 spikes. | Verifies motor response is driven by sensory input rather than intrinsic network oscillation. |
| **3. Non-Sugar Control** | Contact with pure water ($0\text{ mM}$ sucrose) or bitter deterrent ($10\text{ mM}$ caffeine). | $P_{\text{PER}} \le 0.05$. | Confirms gustatory selectivity; non-target inputs do not activate feeding circuits. |
| **4. Always-Respond Baseline** | Trivial open-loop policy that automatically extends proboscis on every tick. | $P_{\text{PER}} = 1.00$ across all conditions (including no-contact and bitter). | Demonstrates why unconstrained response policies fail biological selectivity requirements. |
| **5. Sensory-Blind Baseline** | Contact triggers fixed motor action via a hardcoded rule without neural propagation. | Identical response latency; no sensitivity to neural silencing. | Establishes the necessity of the connectome simulation: a hardcoded rule cannot reproduce intervention effects. |
| **6. Shuffled-Graph Control** | Degree-matched randomized synaptic connectivity matrix. | Loss of functional signal transmission; $P_{\text{PER}} \approx 0.00$. | Confirms that specific biological wiring (and not merely synaptic density or neuron count) enables propagation. |

---

## 4. Run Record & Evidence Integrity Schema

Every evaluation run will serialize a structured JSON log containing:
* `scenario_id`: `"taste_contact_proboscis_mvp"`
* `dataset_snapshot`: `"FlyWire_FAFB_v783"`
* `subgraph_checksum`: SHA-256 hash of the extracted circuit JSON
* `random_seed`: Integer seed for trial repeatability
* `intervention_target`: Node ID or `"none"`
* `timestamps`: `t_contact`, `t_first_spike_mn9`, `t_max_extension`
* `metrics`: `spike_count_mn9`, `peak_theta_degrees`, `outcome_label`
* `causal_validation_status`: Pass/Fail against control criteria

