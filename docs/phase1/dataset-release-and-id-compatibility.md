# NeuroFly Dataset Release and Identifier Compatibility

**Document:** Phase 1 Dataset Release & ID Strategy  
**Target Release:** FlyWire FAFB (Full Adult Female Brain) v783  
**Reference Release:** FlyWire FAFB v630 (used in Shiu et al. 2024)  
**Status:** Canonical release identified; crosswalk strategy defined  

---

## 1. Official Dataset Specifications

### 1.1 Canonical Target Release: FlyWire FAFB v783
* **Title:** FlyWire whole-brain connectome of Drosophila melanogaster (FAFB v783)
* **Canonical Archive:** Zenodo DOI [10.5281/zenodo.10676866](https://zenodo.org/records/10676866)
* **Access Portal:** FlyWire Codex (`codex.flywire.ai`)
* **Primary Citations:**
  * Dorkenwald, S., et al. (2024). *Neuronal wiring diagram of an adult brain.* **Nature**, 634, 124–138. DOI: [10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y)
  * Schlegel, P., et al. (2024). *Whole-brain annotation and multi-connectome cell typing of Drosophila.* **Nature**, 634, 139–152. DOI: [10.1038/s41586-024-07686-5](https://doi.org/10.1038/s41586-024-07686-5)
* **License & Attribution:** Creative Commons Attribution 4.0 International (CC-BY 4.0). Derived subgraphs and public visualizations must cite the FlyWire consortium and the Nature 2024 publications.
* **Identifier Namespace:** 64-bit integer Root IDs (`root_id`, e.g., `7205759406...`), representing agglomerated proofread segmentations in the CAVE (Connectome Annotation Versioning Engine) system. Coordinates are recorded in raw voxel coordinates ($4 \times 4 \times 40\text{ nm}$).

---

## 2. Release Comparison: v630 vs. v783

| Parameter | FlyWire v630 (Shiu et al. 2024) | FlyWire FAFB v783 (NeuroFly Target) | Crosswalk Status |
|---|---|---|---|
| **Freeze Date** | 2023-03-23 | 2024-02-15 (Zenodo release) | Documented change timeline |
| **Proofreading State** | Near-final proofreading freeze | Canonical public release; peer-reviewed freeze | Additional proofreading merges/splits in v783 |
| **Cell Typing** | Early hierarchical type tags | Comprehensive consensus typing (Schlegel et al.) | Cell-type names are standardized in v783 |
| **Neurotransmitter Data** | Eckstein et al. (2020) per-synapse predictions | Updated consensus transmitter assignments | High concordance (>98% on major types) |
| **Shiu et al. Code Support** | Primary development baseline | Supported via config parameter swap in repository | Repo supports both snapshots natively |

---

## 3. Identifier Stability and Crosswalk Strategy

### 3.1 The Root ID Mutation Challenge
In connectomic reconstructions, root IDs change whenever a proofreader performs a merge (joining two segments) or a split (separating falsely merged segments). Consequently, a 64-bit `root_id` from v630 may not map 1:1 to a single `root_id` in v783.

### 3.2 Resolution Methodology
To ensure reproducible extraction and prevent silent identifier corruption, NeuroFly adopts a three-tier crosswalk protocol:
1. **Cell-Type Key Binding:** Neurons of interest (e.g., `MN9`, labellar sugar GRNs, specific SEZ projection interneurons) possess curated morphological and cell-type designations defined by Schlegel et al. (2024). These anatomical classifications remain stable across releases.
2. **Supervoxel Coordinate Anchoring:** Individual proofread segments are composed of invariant $4 \times 4 \times 40\text{ nm}$ supervoxels. When verifying an ID between v630 and v783, the soma coordinate (or primary branch point) serves as the persistent spatial anchor.
3. **Shiu et al. Dual-Release Compatibility:** Because the Shiu et al. (2024) reference codebase explicitly documents compatibility with both v630 and v783 files, NeuroFly will base its Phase 3 extraction pipeline on **FAFB v783**, verifying candidate cell IDs against both the v783 Zenodo tables and the Shiu repository configuration.

---

## 4. Hard Data Rules & Phase Stop Conditions

1. **No Bulk Download in Phase 1:** Phase 1 defines the metadata, identifiers, and extraction rules. Downloading the ~10.6 GB Zenodo raw archive or writing extraction code is deferred to Phase 3.
2. **No Scraped Data:** All data inputs must derive strictly from official static tables (Zenodo or Codex bulk downloads). Dynamic web-scraping of the FlyWire interactive web visualizer is prohibited.
3. **No Cross-Release Mixing:** Under no circumstances will IDs from FAFB (brain) be combined with BANC (brain + nerve cord) or MCNS (male) without an explicit, documented mapping table and version citation.

