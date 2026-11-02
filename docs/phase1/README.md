# NeuroFly Phase 1: Assay and Circuit Evidence

**Phase:** 1 — Assay and circuit evidence  
**Status:** In progress  
**Project Owner:** Abhi  
**Start Date:** 2026-11-01  
**Active Repository Root:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Phase 0 Confirmation Reference:** [`docs/phase0-checklist.md`](../phase0-checklist.md) (Confirmed by Abhi on 2026-11-01)  

---

## 1. Purpose and Boundaries

Phase 1 establishes the scientific, anatomical, and empirical foundations for the first NeuroFly behavioral loop:

$$\text{Physical Taste Contact} \longrightarrow \text{Gustatory Input} \longrightarrow \text{Selected Connectome Circuit} \longrightarrow \text{Motor Output} \longrightarrow \text{Proboscis Extension Response (PER)}$$

This phase is **strictly evidence and specification work**. It does not download or extract bulk connectome datasets, implement neural simulation engines, calibrate body physics, or build web interfaces. Bulk extraction remains blocked until dataset snapshot compatibility and cell mapping are verified.

---

## 2. Evidence Deliverables Index

| Document | Purpose and Scope | Status |
|---|---|:---:|
| [`assay-specification.md`](assay-specification.md) | Testable research question, falsifiable sensorimotor hypothesis, contact geometry, trial protocol, and I/O mapping hypotheses. | Complete |
| [`reference-methods-review.md`](reference-methods-review.md) | Detailed analysis of Shiu et al. (2024) *Nature* methods, Brian 2 LIF model parameters, stimulation protocols, and scope differences. | Complete |
| [`dataset-release-and-id-compatibility.md`](dataset-release-and-id-compatibility.md) | Official FlyWire FAFB v783 dataset release audit, identifier namespace, Zenodo package, and v630-to-v783 crosswalk strategy. | Complete |
| [`cell-edge-evidence-register.md`](cell-edge-evidence-register.md) | Candidate sugar gustatory receptor neurons, intermediate SEZ premotor neurons, and MN9 motor neurons with stable IDs and confidence ratings. | Complete |
| [`evaluation-protocol.md`](evaluation-protocol.md) | Operational definition of the primary response measure, intervention prediction, and baseline controls (no-contact, no-sensory, simple-rule). | Complete |
| [`phase1-open-decisions.md`](phase1-open-decisions.md) | Unresolved questions, risk register updates, workstream ownership, review dates, and Phase 2 handoff requirements. | Complete |

---

## 3. Evidence Vocabulary

NeuroFly enforces strict scientific categorization across all Phase 1 documentation:
* **Measured:** Direct physical or anatomical data from FlyWire FAFB or published experiments (e.g., cell IDs, synapse counts, neuropil coordinates).
* **Inferred:** Biological interpretations supported by indirect evidence or cell typing (e.g., predicted neurotransmitter signs, functional annotations).
* **Modeled:** Mathematical rules or engineering simplifications implemented by NeuroFly (e.g., sensory encoding thresholds, LIF integration equations, motor decoders).
* **Predicted:** Hypothesized outcomes formulated prior to running simulations or inspecting held-out trials (e.g., virtual lesion silencing effects).
* **Display-only:** Visual aids (e.g., arena markers, activity glow, camera framing) that do not influence the simulation physics or neural state.

---

## 4. Phase 1 Exit Gate

Phase 1 is complete when all deliverables above are authored with direct source citations, uncertainty is made explicit, candidate cells and edges are traceable in FAFB v783/v630, and the project owner reviews and approves the Phase 1 signoff record.

