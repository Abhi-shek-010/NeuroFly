# NeuroFly Phase 1 Evaluation Protocol: Metrics, Intervention, and Controls

**Document:** Phase 1 Quantitative Evaluation Protocol  
**Scope:** Verification rules for the Taste-Contact to Proboscis Extension MVP  
**Target Release:** FlyWire FAFB v783  
**Review Date:** 2026-11-14  
**Status:** Owner-reviewed; accepted with scope limitation  

---

## 1. Quantitative Performance Measures & Provisional Benchmarks

All quantitative performance thresholds below are **provisional engineering choices** established to evaluate model stability and causality. They are derived from published *Drosophila* feeding literature (Shiu et al. 2024; Dethier 1976) and will be formally calibrated in Phase 5.

### 1.1 Primary Metric: Motor Response Probability ($P_{\text{PER}}$)
* **Mathematical Definition:** The fraction of valid stimulus contact trials that elicit a functional proboscis motor response:
  $$P_{\text{PER}} = \frac{N_{\text{response}}}{N_{\text{trials}}}$$
* **Operational Classification Rule:** A trial is scored as a positive proboscis extension response ($R = 1$) if and only if:
  1. Proboscis motor neuron **MN9** fires $\ge 5$ action potentials within the contact observation window ($100\text{ ms} \le t \le 350\text{ ms}$). *(Provisional firing threshold)*
  2. The decoded proboscis joint angle achieves $\theta(t) \ge 20.0^\circ$ prior to trial termination ($t = 500\text{ ms}$). *(Provisional kinematic threshold)*
* **Provisional Target Cutoff:** $P_{\text{PER}} \ge 0.90$ across $N = 50$ randomized, seed-controlled trials with $100\text{ mM}$ sucrose.
* **Trial Variability:** For binary trial outcomes R_k, report successes/N, the mean p_hat = (sum R_k)/N, sample standard deviation s_R = sqrt(sum((R_k - p_hat)^2)/(N - 1)), and the 95% Wilson score confidence interval. For p_hat = N_response / N and z = 1.96:
  $$\tilde p = \frac{\hat p + z^2/(2N)}{1 + z^2/N}, \qquad h = \frac{z}{1 + z^2/N}\sqrt{\frac{\hat p(1-\hat p)}{N} + \frac{z^2}{4N^2}}, \qquad CI_{95\%} = [\tilde p-h,\tilde p+h].$$
  The target is 50 randomized trials per condition; 30 may be used for exploratory runs. These counts are precision targets, not evidence of adequate statistical power. Report the actual N and do not treat seed variation as independent biological replication.

### 1.2 Secondary Metrics (Provisional Biological Expectations)
* **Response Latency ($\Delta t_{\text{lat}}$):** Time from physical contact onset ($t_{\text{contact}} = 100\text{ ms}$) to the first action potential in MN9 ($t_{\text{first}}$):
  $$\Delta t_{\text{lat}} = t_{\text{first}} - t_{\text{contact}}$$
  *Provisional Biological Estimate:* $15\text{ ms} \le \Delta t_{\text{lat}} \le 60\text{ ms}$, representing estimated conduction and synaptic integration delays across 2–4 synapses in the SEZ.
* **Taste Selectivity Index ($\text{SI}$):**
  $$\text{SI} = P_{\text{PER}}(\text{Sucrose } 100\text{ mM}) - P_{\text{PER}}(\text{Water / Bitter})$$
  *Provisional Target Cutoff:* $\text{SI} \ge 0.80$.

---

## 2. Predeclared Virtual Intervention Experiment

### 2.1 Experimental Protocol
Evaluations are structured as paired, seed-matched comparisons:
1. **Condition A (Intact Baseline):** Intact FAFB v783 connectome subgraph, $100\text{ mM}$ sucrose contact, seed $S_k$.
2. **Condition B (Virtual Lesion / Silenced):** Silenced candidate intermediate premotor node (`Fdg` / SEZ premotor pool), $100\text{ mM}$ sucrose contact, identical seed $S_k$.

### 2.2 Silencing Mechanism & Equivalence Rule
* **Primary Implementation (Shiu-Equivalent):** Outgoing synaptic transmission from the targeted neuron group is zeroed ($W_{ij} = 0$). This matches the reference code implementation in `philshiu/Drosophila_brain_model`.
* **Alternative Modeled Mode (Voltage Clamping):** Membrane potential is clamped to hyperpolarized potential ($V_{\text{clamp}} = -70.0\text{ mV}$).
* **Integrity Mandate:** Evaluation reports must state the active silencing mechanism. Clamping will not be claimed as mathematically identical to Shiu et al.'s synaptic disconnection.

### 2.3 Paired Statistical Comparison

For binary response outcomes, compare the seed-matched intact and silenced trials with a two-sided exact McNemar test at alpha = 0.05. Report the two discordant-pair counts and the paired risk difference (silenced minus intact) with a 95% confidence interval from a method appropriate for paired binary data. Do not infer an intervention effect from overlap or non-overlap of separate Wilson intervals. Fifty seed pairs are a planning target; no power claim is made without a prospective power analysis.


### 2.4 Predeclared Falsifiable Prediction
> **Hypothesis:** Under identical initial body pose, contact timing, and stimulus strength, virtual silencing of the intermediate feeding premotor node will produce a statistically significant reduction in proboscis motor recruitment:
> $$P_{\text{PER}}(\text{Silenced}) \le 0.10 \quad \text{vs.} \quad P_{\text{PER}}(\text{Intact}) \ge 0.90$$
> If virtual silencing of the candidate node fails to significantly reduce MN9 firing ($P_{\text{PER}} > 0.30$), the hypothesis that this pathway forms a necessary causal bottleneck is rejected, requiring re-tracing of alternative collateral paths.

---

## 3. Negative Controls & Baseline Comparison Suite

To verify that successful motor execution requires the intended sensory input and connectome wiring, every evaluation run must report against the following control matrix:

| Control Type | Experimental Manipulation | Expected Outcome | Causal Hypothesis Challenged |
|---|---|---|---|
| **1. No-Contact Control** | Sugar patch placed out of physical reach ($d > 2.0\text{ mm}$). | $P_{\text{PER}} = 0.00$; zero MN9 spikes. | Verifies response requires physical contact; rules out spontaneous resting firing. |
| **2. No-Sensory Control** | Contact occurs, but sensory encoder current clamped to zero ($I_{\text{inj}} = 0$). | $P_{\text{PER}} = 0.00$; zero MN9 spikes. | Verifies motor output is driven by gustatory input rather than intrinsic network oscillation. |
| **3. Non-Sugar Control** | Contact with pure water ($0\text{ mM}$ sucrose) or bitter deterrent ($10\text{ mM}$ caffeine). | $P_{\text{PER}} \le 0.05$. | Confirms gustatory selectivity; non-sweet inputs do not trigger the feeding circuit. |
| **4. Always-Respond Baseline** | Trivial open-loop policy that automatically extends proboscis on every tick. | $P_{\text{PER}} = 1.00$ across all conditions (including no-contact and bitter). | Demonstrates why unconstrained response policies fail biological selectivity requirements. |
| **5. Sensory-Blind Baseline** | Contact triggers fixed motor action via a hardcoded rule without neural propagation. | Identical response latency; zero sensitivity to neural silencing. | Establishes the necessity of the connectome simulation: a hardcoded rule cannot reproduce intervention effects. |
| **6. Shuffled-Graph Control** | Degree-matched randomized synaptic connectivity matrix. | Loss of functional signal transmission; $P_{\text{PER}} \approx 0.00$. | Confirms that specific biological wiring (and not merely synaptic density or neuron count) enables propagation. |

---

## 4. Evaluation Testing Harnesses: Scripted vs. Dynamic

* **Scripted Test Harness:** Runs automated suites with fixed $t_{\text{contact}} = 100\text{ ms}$ and fixed contact duration ($250\text{ ms}$). Outputs machine-readable JSON logs for CI.
* **Habitat Interactive Harness:** Executes in the 3D environment where contact onset and duration depend on spatial physics and fly joint configuration.
* **Run Record Schema:** Every test run serializes:
  * `scenario_id`: `"taste_contact_proboscis_mvp"`
  * `dataset_snapshot`: `"FlyWire_FAFB_v783"`
  * `subgraph_checksum`: SHA-256 hash of the extracted circuit JSON
  * `silencing_method`: `"synaptic_zeroing"` or `"voltage_clamp"`
  * `random_seed`: Integer seed for trial repeatability
  * `timestamps`: `t_contact`, `t_first_spike_mn9`, `t_max_extension`
  * `metrics`: `spike_count_mn9`, `peak_theta_degrees`, `outcome_label`
  * `confidence_intervals`: 95% Wilson interval for $P_{\text{PER}}$
