# NeuroFly Dataset Release and Identifier Compatibility

**Document:** Phase 1 Dataset Release & ID Strategy  
**Target MVP Release:** FlyWire FAFB (Full Adult Female Brain) v783  
**Reference Model Release:** FlyWire FAFB v630 (used in Shiu et al. 2024)  
**Deferred Locomotion Release:** BANC v888 (Brain and Nerve Cord; reserved for Phase 10)  
**Review Date:** 2026-11-14  
**Status:** FAFB v783 selected for the MVP; exact cell identities and edges remain a Phase 3 gate

---

## 1. Official Dataset Specifications

### 1.1 Canonical Target Release: FlyWire FAFB v783
* **Dataset Name:** FlyWire whole-brain connectome of adult female *Drosophila melanogaster* (FAFB v783).
* **Canonical Archive:** Zenodo DOI [10.5281/zenodo.10676866](https://zenodo.org/records/10676866) (Data release date: 2024-02-15).
* **Online Explorer & Community Annotation Portal:** FlyWire Codex (`codex.flywire.ai`).
* **Primary Literature Citations:**
  * Dorkenwald, S., et al. (2024). *Neuronal wiring diagram of an adult brain.* **Nature**, 634, 124–138. DOI: [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
  * Schlegel, P., et al. (2024). *Whole-brain annotation and multi-connectome cell typing of Drosophila.* **Nature**, 634, 139–152. DOI: [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
* **License & Distribution:** Creative Commons Attribution 4.0 International (CC-BY 4.0). Any derived subgraphs, manifests, or public visualizations must cite the FlyWire consortium and the 2024 Nature papers.
* **Identifier Namespace:** 64-bit integer Root IDs (`root_id`, e.g., starting with `720575940...`), representing dynamic proofread agglomerations in the CAVE (Connectome Annotation Versioning Engine) system. Raw voxel coordinates are specified at $4 \times 4 \times 40\text{ nm}$.

---

## 2. Anatomical Justification: FAFB v783 vs. BANC v888

### 2.1 Why FAFB v783 is Selected for the MVP (Taste to Proboscis)
* **Brain-Only Circuit Topology:** The proboscis extension response (PER) is an anatomically cephalic sensorimotor reflex:
  1. Sugar gustatory receptors on the labellum project axons directly through the labellar nerve into the **subesophageal zone (SEZ)** (gnathal ganglion) in the ventral brain.
  2. Gustatory second-order interneurons and feeding command interneurons (`Fdg`) are entirely contained within the SEZ.
  3. Proboscis motor neurons—specifically **MN9** (rostrum protractor), MN11, and MN12—have their cell bodies, primary dendrites, and motor efferent origins located in the SEZ.
  4. **No ventral nerve cord (VNC) or thoracic circuitry is involved in proboscis extension.**
* **Conclusion:** FAFB v783 contains the complete anatomical sensory, premotor, and motor substrate needed for Sandbox 1.

### 2.2 Role of BANC v888 and Prohibition on Namespace Mixing
* **BANC Scope:** The BANC (Brain and Nerve Cord) v888 dataset reconstructs a continuous female adult brain and ventral nerve cord.
* **When BANC is Required:** BANC is essential when modeling leg motor neurons, thoracic central pattern generators, or descending pathways for walking and halting (Sandbox 2 / Phase 10).
* **Strict Namespace Separation:** BANC v888 utilizes a completely distinct EM segmentation volume and independent root ID namespace. **Under no circumstances will FAFB root IDs and BANC root IDs be combined or cross-referenced without an explicit, documented mapping table.**
* **Open Owner Decision:** If the project owner elects to migrate Sandbox 1 to BANC v888 to ensure seamless anatomical continuity with Phase 10 walking, all Phase 1 cell-edge tracing must be re-executed against the BANC segmentation. The current baseline firmly freezes **FAFB v783** for Phase 1.

---

## 3. Snapshot Crosswalk Strategy: v630 (Shiu) vs. v783 (Canonical)

### 3.1 The Root ID Mutation Challenge
FlyWire root IDs represent proofread states. Between the pre-release v630 freeze (March 2023, used by Shiu et al.) and the canonical v783 public release (February 2024), ongoing proofreading resulted in fragment mergers and split corrections. Consequently, a 64-bit `root_id` from v630 may not map 1:1 to an active `root_id` in v783.

### 3.2 Dual-Release Compatibility in Reference Code
The Shiu et al. repository (`philshiu/Drosophila_brain_model`) explicitly provides dual-release configuration support:
```python
# Shiu et al. configuration pattern:
config = {
    'path_comp': './2023_03_23_completeness_630_final.csv', # v630
    'path_con':  './2023_03_23_connectivity_630_final.parquet', # v630
    # Or swap to v783 files:
    # 'path_comp': './proofread_completeness_v783.csv',
    # 'path_con':  './connectivity_v783.parquet',
}
```

### 3.3 Three-Tier Release-Specific Identity Reconciliation
To make extracted subgraphs auditable and reduce identity errors:
1. **Tier 1: Cell-Type Annotation Key:** Anchor candidate neurons to consensus morphological and functional types curated in Schlegel et al. (2024) (e.g., cell type `MN9`, labellar gustatory receptor neuron classes).
2. **Tier 2: Supporting Morphology and Coordinate Localizers:** Record relevant coordinates or supervoxels as supporting evidence for release-specific re-identification.
   Coordinates do not guarantee a cross-version identity mapping and cannot by themselves resolve a split or merged root. Use an official lineage or mapping resource where available; otherwise re-identify in the selected release and record ambiguity. Stop for unresolved identities.
3. **Tier 3: Release-Specific Graph Query:** In Phase 3, query the canonical v783 annotations and connectivity tables directly. Verify the candidate sensory-to-motor route before freezing any subgraph asset.

---

## 4. Hard Data Rules & Stop Conditions

1. **No Bulk Download in Phase 1:** Phase 1 defines the metadata, candidate cell classes, and extraction specifications. The ~10.6 GB raw Zenodo archive must not be downloaded during this phase.
2. **No Scraped Data:** Bulk data acquisition in Phase 3 will rely exclusively on static Zenodo files or canonical Codex bulk downloads. Dynamic web scraping of the FlyWire 3D viewer is prohibited.
3. **No Namespace Conflation:** FAFB (brain) and BANC (brain + nerve cord) remain strictly separated.
