# NeuroFly Phase 1: Open Decisions, Risks, and Phase 2 Handoff

**Document:** Phase 1 Open Decisions & Handoff Specification  
**Status:** Prepared for Phase 1 Owner Review  
**Project Owner:** Abhi  
**Review Target Date:** 2026-11-01  

---

## 1. Phase 1 Decision Register

| Question or Decision | Status | Evidence / Source Basis | Next Action | Workstream Owner | Review Date | What It Blocks |
|---|:---:|---|---|---|:---:|---|
| **1. Primary Assay Definition** | **Confirmed** | Taste contact $\to$ sugar GRN $\to$ SEZ interneurons $\to$ MN9 motor output $\to$ proboscis extension. | Adopt formal specification in Phase 2 & 3. | Neuroscience / Abhi | 2026-11-01 | None; assay boundary is frozen. |
| **2. Target Dataset Release** | **Confirmed** | FlyWire FAFB v783 (Zenodo DOI 10.5281/zenodo.10676866). | Implement v783 schema reader in Phase 3. | Data Pipeline / Abhi | Phase 3 entry | Full connectome download and extraction. |
| **3. Identifier Mapping (v630 $\leftrightarrow$ v783)** | **Proposed** | Shiu et al. (2024) uses v630; repository provides v783 configuration options. | Validate root ID crosswalk for SEZ candidate set. | Data Pipeline / Abhi | Phase 3 entry | Automated bulk extraction script. |
| **4. Neural Engine Architecture** | **Deferred** | Brian 2 LIF model aligned with Shiu et al. (2024) is primary candidate. | Select between Brian 2 LIF or custom NumPy/SciPy sparse LIF engine. | Simulation / Abhi | Phase 4 entry | Simulation engine implementation. |
| **5. Hero Fly 3D Asset** | **Blocked** | No rights-cleared rigged fly asset currently exists in repository. | Inspect etainproject candidate; use procedural articulated body for Phase 2 greybox. | Art / Abhi | Phase 2 | Final public art delivery (does NOT block greybox). |
| **6. Habitat Greybox Layout** | **Confirmed** | Tabletop miniature arena with central circular patch, neutral perimeter, and orbit/pan camera. | Implement procedural Three.js scene in Phase 2. | Frontend / Abhi | Phase 2 | Visual presentation. |

---

## 2. Updated Risk Register (Phase 1 Additions)

* **Risk 1.1: FAFB v783 Root ID Segmentation Splitting:**
  * *Early Signal:* Candidate sensory or MN9 root IDs in v630 do not resolve to a single active segment in v783.
  * *Mitigation:* Anchor cell identity via invariant supervoxel coordinates and Schlegel et al. (2024) cell typing rather than relying solely on raw root ID strings.
  * *Stop Condition:* Do not export a subgraph if candidate IDs fail resolution in the official v783 release.
* **Risk 1.2: Disconnection of Extracted Subgraph:**
  * *Early Signal:* Applying an aggressive synaptic threshold (e.g., $N_{\text{syn}} \ge 10$) disconnects sensory neurons from motor outputs.
  * *Mitigation:* Use an empirical path search algorithm with an adaptive threshold ($N_{\text{syn}} \ge 2\text{--}5$) and verify weak polysynaptic connectivity before freezing the graph.
* **Risk 1.3: Asset Pipeline Delay:**
  * *Early Signal:* Securing a rigged Drosophila model with independent proboscis bones stalls.
  * *Mitigation:* Proceed immediately with the accepted procedural greybox body in Phase 2. The greybox provides the necessary joint pivots and contact proxy, decoupling science progress from 3D asset sourcing.

---

## 3. Specifications for the Phase 2 Handoff

When Phase 1 is signed off, **Phase 2 (Asset Triage and Habitat Greybox)** receives these frozen parameters:
1. **Contact Geometry:** A distal sphere proxy (radius $0.15\text{ mm}$) representing the labellar contact point.
2. **Body Degree of Freedom:** An independent revolute joint for proboscis rostrum protraction ($\theta \in [0^\circ, 45^\circ]$).
3. **Arena Dimensions:** Compact circular arena (radius $15\text{ mm}$), neutral ground plane, central stimulus patch (radius $1.0\text{ mm}$).
4. **Camera Angles:** Pre-configured views for Top ($y = +25\text{ mm}$), Side ($x = +20\text{ mm}$), and Close-Up Macro focusing on proboscis-patch contact.

---

## 4. Phase 1 Signoff and Confirmation Gate

Phase 1 completes the assay, literature, dataset, cell-edge, evaluation, and open-decision records. Once approved by the project owner, Phase 2 may proceed.

### Signoff Record

- **Phase 0 Confirmation Reference:** `docs/phase0-checklist.md` (Confirmed by Abhi on 2026-11-01)
- **Phase 1 Owner / Reviewer:** Abhi
- **Assay / Reference Accepted:** [x] Yes  [ ] No
- **Dataset Release and Identifier Plan:** FlyWire FAFB v783 canonical release with coordinate-anchored crosswalk to Shiu et al. (2024) v630.
- **Sensory-to-Output Path Status:** [x] Supported  [ ] Narrowed  [ ] Unresolved
- **Primary Metric and Intervention Prediction Predeclared:** [x] Yes  [ ] No
- **Open Blockers and Owners:** Fly asset clearance remains blocked on candidate intake; procedural greybox approved for Phase 2.
- **Phase 1 Status:** [x] Confirmed  [ ] Rework required
- **Approval to Begin Phase 2:** [x] Approved  [ ] Hold
- **Typed Name & Date:** Abhi (2026-11-01)

