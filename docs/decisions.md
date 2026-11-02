# Decision Log

Statuses use the Phase 0 guide's terms: **Confirmed**, **Proposed**, **Deferred**, **Rejected**, and **Blocked**. A proposed choice is not a scientific finding or owner signoff.

| Topic | Status | Current position and basis | Next action, owner, review | Block |
|---|---|---|---|---|
| First assay | Proposed | Physical taste contact to feeding-related proboscis output; approach is excluded. | Review Shiu et al. (2024) methods and write exact assay. Owner: project owner / neuroscience workstream. By Phase 1 signoff; target 2026-11-08 proposed. | Blocks cell selection and assay claims. |
| Dataset snapshot | Proposed | FAFB v783 is a candidate; compatibility with the earlier reference snapshot is unresolved. | Verify official release and source terms; create an explicit crosswalk or narrow the comparison. Owner: project owner / data workstream. Before any extraction. | Hard block on bulk download, extraction, or cell naming. |
| Cell-ID source | Blocked | No sensory, intermediate, or proboscis motor IDs have been verified for NeuroFly. | Trace and document stable IDs and evidence in Phase 1. Owner: neuroscience/data workstream; individual to be recorded. | Hard block on named pathway claims and subgraph extraction. |
| Neural dynamics | Deferred | Brian 2 LIF is a candidate only if it reproduces the reference assumptions; a named rate model is an alternative. | Review the reference equations and choose exactly one engine with units, seed, and parameter record. Owner: simulation workstream. Before Phase 4. | Blocks neural-runtime implementation, not Phase 0 scaffolding. |
| Sensory encoding | Deferred | Taste input must arise from valid patch contact; concentration encoding is not specified. | Define stimulus and receptor mapping from reviewed evidence; document uncertainty. Owner: neuroscience workstream. Before Phase 5. | Blocks sensory integration. |
| Body representation | Proposed | Start stationary or slowly moving with a visible independent proboscis degree of freedom; rendering and physics are separate. | Choose the smallest body/contact model and calibrate extension, hold, retraction, contact, and lag. Owner: body workstream. Before Phase 5. | Blocks integrated body claims. |
| Fly asset | Blocked | No asset is present or verified. Procedural/hand-built rig is the fallback; etainproject model is only an unverified lead. | Inspect source page, license, actual file, rig, and redistribution terms; otherwise make original greybox. Owner: project owner / art workstream. Proposed review 2026-11-08. | Blocks public use of the candidate asset, not placeholder interface work. |
| Software runtime | Proposed | React/TypeScript/Vite/Three.js frontend; Python API, WebSocket snapshots, separate simulation worker. | Confirm the minimal local run path and exact stack before implementation. Owner: project owner / software workstream. At Phase 0 review. | Blocks application-code setup until confirmed. |
| Deployment | Proposed | Develop locally with an offline exhibit fallback; decide public static frontend and separate live service after MVP evidence. | Confirm device, browser, minimum display size, public-hosting intent, and offline requirements. Owner: project owner. At Phase 0 review. | Blocks deployment setup, not research planning. |
| Release scope | Confirmed | One taste-contact-to-proboscis loop; all other behavior modes deferred. | Confirmed by project owner Abhi at Phase 0 gate (2026-11-01). Owner: Abhi. | Phase 1 approved to proceed. |
| Code and data licensing | Deferred | No third-party code/data/assets have been adopted in this repository; source plans are retained as planning inputs. | Record license and attribution per acquired dependency, dataset, and asset before use or publication. Owner: project owner / relevant workstream. Before distribution. | Blocks distribution of uncleared materials. |

## Review convention

Project owner: Abhi. Phase 0 foundation confirmed on 2026-11-01. Update each row with source/evidence, owner, next action, review date, and explicit block before changing a status to Confirmed.
