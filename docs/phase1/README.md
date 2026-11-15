# NeuroFly Phase 1: Assay and Circuit Evidence

**Phase:** 1 — Assay and circuit evidence  
**Status:** Complete with scope limitation; Phase 2 approved to begin
**Project Owner:** Abhi  
**Start Date:** 2026-11-01  
**Review Date:** 2026-11-14  
**Active Repository Root:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Phase 0 Confirmation Reference:** [`docs/phase0-checklist.md`](../phase0-checklist.md) (Confirmed by Abhi on 2026-11-01)  

---

## 1. Purpose and Boundaries

Phase 1 establishes the scientific, anatomical, and empirical foundations for the first NeuroFly behavioral loop:

$$\text{Physical Taste Contact} \longrightarrow \text{Gustatory Input} \longrightarrow \text{Selected Connectome Circuit} \longrightarrow \text{Motor Output} \longrightarrow \text{Proboscis Extension Response (PER)}$$

This phase is **strictly evidence and specification work**. It does not download or extract bulk connectome datasets, implement neural simulation engines, calibrate body physics, or build web interfaces. Bulk extraction remains blocked until dataset snapshot compatibility and cell mapping are verified in Phase 3.

---

## 2. Evidence Deliverables Index

| Document | Purpose and Scope | Status |
|---|---|:---:|
| [`assay-specification.md`](assay-specification.md) | Testable research question, falsifiable sensorimotor hypothesis, contact geometry (scripted fixtures vs. dynamic Habitat events), trial protocol, and provisional I/O mappings. | Reviewed; accepted with scope limitation |
| [`reference-methods-review.md`](reference-methods-review.md) | Detailed comparison between Shiu et al. (2024) *Nature* reported methods and public reference code (`philshiu/Drosophila_brain_model`), documenting reference LIF settings, including t_mbr, tau, t_rfc, t_dly, and w_syn, synthetic optogenetic defaults, and outgoing synaptic zeroing. | Reviewed; accepted with scope limitation |
| [dataset-release-and-id-compatibility.md](dataset-release-and-id-compatibility.md) | Official FlyWire FAFB v783 release audit, BANC v888 deferral, and release-specific identity reconciliation using coordinates as supporting evidence. | Reviewed; accepted with scope limitation |
| [`cell-edge-evidence-register.md`](cell-edge-evidence-register.md) | Candidate sugar GRNs, G2N interneurons, Fdg command neurons, and MN9 motor neurons with neuropil regions, transmitter predictions, confidence ratings, and explicit unverified ID boundaries. | Reviewed; accepted with scope limitation |
| [`evaluation-protocol.md`](evaluation-protocol.md) | Predeclared primary response metric ($P_{\text{PER}}$), latency expectations, intervention hypothesis (synaptic zeroing), trial variability reporting, and 6 negative control baselines. | Reviewed; accepted with scope limitation |
| [`phase1-open-decisions.md`](phase1-open-decisions.md) | Open decision register, updated risk register, Phase 2 handoff parameters, and Phase 1 signoff gate. | Reviewed; accepted with scope limitation |

---

## 3. Evidence Vocabulary

NeuroFly enforces strict scientific categorization across all Phase 1 documentation:
* **Measured:** Direct physical or anatomical data from FlyWire FAFB or published experiments (e.g., cell types, neuropil coordinates, chemical synapse topology).
* **Inferred:** Biological interpretations supported by indirect evidence or cell typing (e.g., automated transmitter predictions, functional signs).
* **Modeled:** Mathematical rules or engineering simplifications implemented by NeuroFly (e.g., sensory encoding thresholds, LIF integration equations, motor decoders, collision proxies).
* **Predicted:** Hypothesized outcomes formulated prior to running simulations or inspecting held-out trials (e.g., virtual lesion silencing effects).
* **Display-only:** Visual aids (e.g., arena markers, activity glow, camera framing) that do not influence the simulation physics or neural state.

---

## 4. Phase 1 Exit Gate

Phase 1 is confirmed with the owner-approved scope limitation recorded in phase1-open-decisions.md. Phase 2 is authorized for asset triage and Habitat greybox work using provisional, configurable inputs. Exact FAFB v783 root IDs and pairwise edges remain unresolved and must be verified in Phase 3 before neural integration or cell-level pathway claims.
