# Initial Architecture and Delivery Boundaries

## Causal data path

`visitor command -> trial coordinator -> contact and sensory input -> selected neural model -> motor decoder -> body state -> timestamped snapshots -> renderer and evidence timeline`

The renderer displays state; it does not select the scientific action. The body pose affects later contact and sensory sampling. Neural processing must run outside the API event loop.

## Proposed components

| Layer | Phase 0 proposal | Boundary and open decision |
|---|---|---|
| Habitat and interface | React, TypeScript, Vite, Three.js | Keep UI state separate from simulation state. Confirm the stack before implementation. |
| Data preparation | Python with tabular inspection tools and NumPy/SciPy sparse structures | Offline, version-pinned pipeline only after Phase 1 fixes the dataset and target path. Do not scrape an interactive explorer or ship the full raw connectome. |
| Session API | FastAPI with WebSockets for scenario commands and compact state snapshots | Candidate shape only. Choose worker/process details when the simulation interface is designed. |
| Neural runtime | One declared engine; Brian 2 LIF is the candidate if it matches the reference assumptions | Equation, units, parameters, and engine remain undecided until reference review. Do not silently run a second hidden model. |
| Body and physics | Visible fly rig plus separately documented body/contact representation | No verified fly asset or proboscis physics model is present. Use a procedural fallback if needed; do not treat a render mesh as validated physics. |
| Run records | Local JSON or CSV for scenario, versions, settings, seed, outputs, outcome, and failures | No accounts or database are needed for the first release. Final schema follows the assay and model decisions. |

## Device and deployment proposal

- First interaction target: desktop mouse and keyboard on a recent laptop.
- Browser proposal: Chrome or Edge; exact supported version and minimum display size are unconfirmed.
- Development path: local first. Keep a local/offline exhibit fallback available.
- Public path: defer the decision to publish until the MVP passes its evidence gate. If published, host the static frontend separately from a WebSocket-capable simulation service; GitHub Pages does not run the Python backend.
- No data download tokens or credentials may be placed in frontend code. Raw connectome archives stay outside the public client bundle and source-control history.

## Phase 0 resolution needed

The project owner should confirm or revise the frontend, service, neural-engine, device, browser, public-hosting, and offline proposals. No application runtime or start command is claimed to exist yet.
