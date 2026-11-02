# Repository Layout

Phase 0 creates homes for later work without implying that those components are already implemented.

| Path | Intended contents | Current state |
|---|---|---|
| `docs/` | Charter, scope, evidence rules, decisions, risks, architecture, handoff, and operating notes | Phase 0 records created |
| `docs/phase1/` | Assay specification, reference methods review, dataset release strategy, cell/edge evidence register, evaluation protocol, and open decisions | Phase 1 evidence deliverables complete |
| `docs/source-plans/` | Planning inputs, implementation guides, source index, and checksums | Five planning source files plus Phase 1 guide present |
| `data_pipeline/` | Dataset retrieval notes and later extraction tooling | Scaffold only; extraction blocked |
| `subgraphs/` | Approved compact, version-pinned graph exports | Scaffold only; no graph data |
| `simulation/` | One selected neural model and interventions | Scaffold only; engine deferred |
| `body/` | Contact rules, actuator mapping, body state, and calibration | Scaffold only |
| `frontend/` | Shared Habitat UI and Three.js rendering | Scaffold only; stack proposed |
| `scenarios/` | Trial presets, initial state, and stimulus settings | Scaffold only |
| `evaluation/` | Baselines, held-out trials, and evidence reports | Scaffold only |
| `assets/fly/source/`, `assets/fly/runtime/`, `assets/fly/physics/` | Source, browser runtime, and physics body files stored separately | Empty scaffolds; no asset approved |
| `assets/world/source/`, `assets/world/runtime/`, `assets/textures/source/`, `assets/ui/`, `assets/audio/`, `assets/credits/` | Source/runtime environment media and attribution records | Empty scaffolds |
| `assets/calibration/`, `assets/evaluation/` | Actuator maps, reference traces, and asset-related evaluation material | Empty scaffolds |
| `deploy/` | Frontend/backend hosting and offline exhibit setup | Scaffold only; deployment decision proposed |

Large raw connectome files and unapproved assets must not be placed in the public frontend. See `.gitignore` for local-data exclusions.
