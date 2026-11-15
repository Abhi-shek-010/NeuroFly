# Decision Log

Statuses use the Phase 0 guide's terms: **Confirmed**, **Proposed**, **Deferred**, **Rejected**, and **Blocked**. A proposed choice is not a scientific finding or owner signoff.

| Topic | Status | Current position and basis | Next action, owner, review | Block |
|---|---|---|---|---|
| First assay | Confirmed with scope limitation | Taste contact to candidate feeding-related proboscis output; approach remains excluded. The exact FAFB v783 sensory-to-MN9 route is unverified. | Owner accepted the assay/contact-design basis on 2026-11-14; verify IDs and edges in Phase 3. Owner: Abhi. | Habitat work may proceed; neural integration and cell-level pathway claims wait for Phase 3. |
| Dataset snapshot | Confirmed | FlyWire FAFB v783 (Zenodo 10676866) confirmed for MVP brain-only loop; BANC v888 deferred to Phase 10. | Build coordinate/cell-type crosswalk and query tables in Phase 3. Owner: Abhi. | Hard block on bulk download, extraction, or cell naming until Phase 3. |
| Cell-ID source | Proposed; unresolved | Candidate cell classes are documented, but exact FAFB v783 root IDs and pairwise edges are not extracted. Coordinates are supporting localizers, not invariant cross-version mappings. | Query official v783 annotation and connectivity resources in Phase 3; record split/merge ambiguity. Owner: Abhi. | Blocks subgraph extraction, neural integration, and cell-specific claims until Phase 3; does not block Phase 2 Habitat assets. |
| Neural dynamics | Deferred | Brian 2 LIF is a candidate only if it reproduces the reference assumptions; a named rate model is an alternative. | Review the reference equations and choose exactly one engine with units, seed, and parameter record. Owner: simulation workstream. Before Phase 4. | Blocks neural-runtime implementation, not Phase 0 scaffolding. |
| Sensory encoding | Deferred | Taste input must arise from valid patch contact; concentration encoding is not specified. | Define stimulus and receptor mapping from reviewed evidence; document uncertainty. Owner: neuroscience workstream. Before Phase 5. | Blocks sensory integration. |
| Body representation | Proposed | Start stationary or slowly moving with a visible independent proboscis degree of freedom; rendering and physics are separate. | Choose the smallest body/contact model and calibrate extension, hold, retraction, contact, and lag. Owner: body workstream. Before Phase 5. | Blocks integrated body claims. |
| Fly asset | Blocked | No asset is present or verified. Procedural/hand-built rig is the fallback; etainproject model is only an unverified lead. | Inspect source page, license, actual file, rig, and redistribution terms; otherwise make original greybox. Owner: project owner / art workstream. Proposed review 2026-11-08. | Blocks public use of the candidate asset, not placeholder interface work. |
| Software runtime | Proposed | React/TypeScript/Vite/Three.js frontend; Python API, WebSocket snapshots, separate simulation worker. | Confirm the minimal local run path and exact stack before implementation. Owner: project owner / software workstream. At Phase 0 review. | Blocks application-code setup until confirmed. |
| Deployment | Proposed | Develop locally with an offline exhibit fallback; decide public static frontend and separate live service after MVP evidence. | Confirm device, browser, minimum display size, public-hosting intent, and offline requirements. Owner: project owner. At Phase 0 review. | Blocks deployment setup, not research planning. |
| Release scope | Confirmed | One taste-contact-to-proboscis loop; all other behavior modes deferred. | Confirmed by project owner Abhi at Phase 0 gate (2026-11-01). Owner: Abhi. | Phase 1 approved to proceed. |
| Code and data licensing | Deferred | No third-party code/data/assets have been adopted in this repository; source plans are retained as planning inputs. | Record license and attribution per acquired dependency, dataset, and asset before use or publication. Owner: project owner / relevant workstream. Before distribution. | Blocks distribution of uncleared materials. |

## Review convention
## Phase 1 owner decision

Abhi approved Phase 1 with a scope limitation on 2026-11-14 and authorized Phase 2 asset triage and Habitat greybox work. This is owner approval to proceed with the physical Habitat and procedural placeholder. It does not certify the candidate FAFB v783 pathway: exact root IDs, pairwise edges, and subgraph extraction remain Phase 3 work. Phase 0 confirmation dated 2026-11-01 remains intact.


Project owner: Abhi. Phase 0 foundation confirmed on 2026-11-01. Update each row with source/evidence, owner, next action, review date, and explicit block before changing a status to Confirmed.
