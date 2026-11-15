# NeuroFly Phase 1: Open Decisions, Risks, and Phase 2 Handoff

**Document:** Phase 1 Open Decisions & Handoff Specification  
**Status:** Confirmed with scope limitation; Phase 2 approved to begin
**Project Owner:** Abhi  
**Review Date:** 2026-11-14  

---

## 1. Phase 1 Decision Register

| Question or Decision | Status | Evidence / Source Basis | Next Action | Workstream Owner | Review Timing | What It Blocks |
|---|:---:|---|---|---|:---:|---|
| **1. Primary Assay Definition** | **Confirmed with scope limitation** | The owner accepts taste-contact-to-proboscis response as the MVP question and contact-design basis. The sensory-to-MN9 route remains a candidate, not a verified FAFB v783 path. | Use the provisional contact contract for Habitat work; verify exact identities and edges before neural integration. | Neuroscience / Abhi | Phase 3 verification | Does not block Habitat greybox; blocks cell-level pathway claims and neural integration. |
| **2. Target Dataset Release** | **Confirmed** | FlyWire FAFB v783 (Zenodo DOI: [10.5281/zenodo.10676866](https://zenodo.org/records/10676866)). Complete cephalic SEZ circuitry present. | Implement v783 schema reader in Phase 3. | Data Pipeline / Abhi | Phase 3 entry | Full connectome download and extraction. |
| **3. BANC v888 vs. FAFB v783** | **Confirmed** | BANC v888 deferred to Phase 10 (locomotion/halting). FAFB v783 retained for MVP brain-only loop; no ID mixing permitted. | Retain FAFB v783 for Phase 1–9. | Data Pipeline / Abhi | Phase 1 signoff | Any multi-region dataset integration. |
| **4. Identifier Mapping (v630 to v783)** | **Proposed; unresolved** | Candidate cell classes are literature-supported; exact FAFB v783 root IDs and pairwise edge counts have not been extracted. Coordinates are supporting localizers, not invariant cross-version keys. | Use available official mappings or release-specific re-identification, then query v783 annotations and edges in Phase 3. | Data Pipeline / Abhi | Phase 3 | Blocks subgraph extraction, cell-specific claims, and neural integration; does not block Habitat assets. |
| **5. Neural Engine Architecture** | **Deferred** | Brian 2 LIF model aligned with Shiu et al. biophysical constants ($v_0=-52\text{ mV}, v_{\text{th}}=-45\text{ mV}$) is primary candidate. | Select between Brian 2 LIF or custom NumPy/SciPy sparse LIF engine. | Simulation / Abhi | Phase 4 entry | Simulation engine implementation. |
| **6. Hero Fly 3D Asset** | **Blocked** | No rights-cleared rigged fly asset exists in repository. Etainproject CT-scan lead remains unverified. | Procedural articulated greybox approved as Phase 2 functional fallback. | Art / Abhi | Phase 2 | Final public art delivery (does NOT block greybox). |
| **7. Habitat Greybox Layout** | **Approved for provisional Phase 2 build** | Owner authorizes the shared Habitat greybox using configurable starting dimensions; these are engineering placeholders, not biological measurements. | Centralize values in the Stage 2A scene contract and adjust them as needed for a usable greybox. | Frontend / Abhi | Phase 2 | No calibrated geometry claim; Phase 2 may proceed. |

---

## 2. Updated Risk Register (Phase 1 Additions)

* **Risk 1.1: FAFB v783 Root ID Segmentation Splitting:**
  * *Early Signal:* Candidate root IDs from earlier literature fail to resolve to active FAFB v783 segments or map ambiguously.
  * *Mitigation:* Prefer official lineage or mapping resources where available. Use morphology, cell type, and coordinates as corroborating evidence, then perform release-specific identity and graph queries. Record split/merge ambiguity and do not force a one-to-one crosswalk.
  * *Stop Condition:* Do not export a subgraph if candidate IDs fail resolution in the official v783 release.
* **Risk 1.2: Disconnection of Extracted Subgraph:**
  * *Early Signal:* Applying an overly strict synaptic threshold ($N_{\text{syn}} \ge 10$) disconnects sensory neurons from MN9 motor output.
  * *Mitigation:* Use an empirical path search algorithm with an adaptive threshold ($N_{\text{syn}} \ge 2\text{--}5$) and verify weak polysynaptic connectivity before freezing the graph.
* **Risk 1.3: Asset Pipeline Dependency Delay:**
  * *Early Signal:* Sourcing or rigging an external Drosophila 3D model stalls.
  * *Mitigation:* Decouple functional progress by proceeding with the procedural articulated greybox in Phase 2. The greybox provides the necessary joint pivots and contact proxy for testing the loop.

---

## 3. Specifications for Phase 2 Handoff

The following values are configurable greybox starting points approved for Phase 2. They are not biological measurements or calibrated contact/body values. Stage 2A must centralize them in the scene contract.

The owner-approved Phase 2 handoff uses the following configurable, provisional scene inputs:
1. **Contact Geometry:** A distal sphere proxy (radius $0.15\text{ mm}$) representing the labellar contact point.
2. **Body Degree of Freedom:** An independent revolute joint for proboscis rostrum protraction ($\theta \in [0.0^\circ, 45.0^\circ]$).
3. **Arena Dimensions:** Compact circular arena (radius $15.0\text{ mm}$), neutral ground plane, central stimulus patch (radius $1.0\text{ mm}$).
4. **Camera Angles:** Pre-configured views for Top ($y = +25\text{ mm}$), Side ($x = +20\text{ mm}$), and Close-Up Macro focusing on proboscis-patch contact.

---

## 4. Phase 1 Owner Decision and Confirmation Gate

### Owner decision recorded 2026-11-14

I, Abhi, as project owner, approve completion of Phase 1 with the explicit scope limitation below and authorize Phase 2 to begin.

- **Phase 0 foundation:** Preserved as confirmed by Abhi on 2026-11-01; see the Phase 0 checklist.
- **Assay / reference accepted:** Yes, as the project question, provisional assay specification, and Habitat contact-design basis. This does not claim that NeuroFly reproduced the reference model.
- **Dataset release:** FAFB v783 is the selected MVP snapshot. BANC v888 remains deferred for the later locomotion scope.
- **Primary metric and intervention:** Predeclared for later evaluation; numerical thresholds and biological input/body mappings remain provisional.
- **Sensory-to-output path status:** Narrowed. Candidate cell classes and literature routes are recorded, but exact FAFB v783 root IDs, pairwise edge counts, and the complete path remain unresolved for Phase 3.
- **Phase 1 status:** Confirmed with scope limitation. The unresolved v783 identities and edges are an explicit Phase 3 handoff, not a claim that the path has been verified.
- **Approval to begin Phase 2:** Approved for asset triage and Habitat greybox work, including the procedural fly, configurable contact/body proxies, scene, and contact-event inspection.
- **Restrictions carried forward:** Do not implement neural integration, claim a validated FAFB v783 pathway, present candidate cell identities as verified v783 cells, or treat contact as a neural/motor response until Phase 3 resolves the relevant IDs and edges.
- **Open blockers and owners:** Exact v783 identity and edge extraction — Phase 3 / Abhi; motor and sensory calibration — Phase 5 / relevant workstream; rights-cleared hero fly asset — asset workstream. The procedural greybox is authorized as the Phase 2 fallback.
- **Owner authorization record:** Abhi gave explicit written approval in the Codex conversation on 2026-11-14. This entry records that authorization; it does not claim an external or handwritten signature.
- **Date:** 2026-11-14
- **Next gate:** Complete Phase 2 stages one at a time and submit each walkthrough/results packet for owner review.
