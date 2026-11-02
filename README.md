# NeuroFly

NeuroFly is a connectome-constrained virtual adult fruit fly in one shared 3D experiment habitat. The first planned experiment follows physical taste contact through gustatory input and a selected neural circuit to a modeled proboscis response.

## Project status

- Current phase: Phase 1, Assay and circuit evidence.
- Phase 0 foundation is confirmed by the project owner (2026-11-01); Phase 1 evidence work is in progress.
- Active repository: `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly` (nested repository root inside `C:\Users\abhi0\Desktop\NeuroFly`).
- Current local branch: `master`. The repository has no commits or configured remote yet.
- Original planning files remain in their respective project output directories under `C:\Users\abhi0\Documents\Codex\2026-11-01`; verified copies and execution guides are in [`docs/source-plans`](docs/source-plans/SOURCE_INDEX.md).

## MVP boundary

The first release is limited to:

`taste-patch contact -> gustatory input -> selected circuit -> motor output -> proboscis response`

The visitor operates the experiment and does not directly pilot the fly during a scientific trial. A run with no proboscis response is a valid result. Walking, food stopping, flight, odor search, vision, grooming, associative learning, and whole-brain claims are deferred.

NeuroFly uses measured connectome structure together with modeled neural dynamics, sensory encoding, motor decoding, and body mechanics. It is not a complete biological fly or whole-brain simulator.

## Source and decision records

- [`docs/project-charter.md`](docs/project-charter.md) - intended visitor, question, and first behavior.
- [`docs/assay-and-data-handoff.md`](docs/assay-and-data-handoff.md) - provisional assay and dataset handoff; extraction remains blocked pending Phase 1 compatibility review.
- [`docs/architecture.md`](docs/architecture.md) - proposed runtime and deployment boundaries.
- [`docs/decisions.md`](docs/decisions.md) and [`docs/risks.md`](docs/risks.md) - open decisions and risks.
- [`docs/phase0-checklist.md`](docs/phase0-checklist.md) - current evidence and signoff gate.
- [`docs/phase0-walkthrough-and-summary.md`](docs/phase0-walkthrough-and-summary.md) - detailed map of Phase 0 work, evidence, open items, and handoff.

## Local run instructions

There is no runnable application yet. Phase 0 currently establishes the project record and repository layout. A local start command will be added when the application runtime is selected and implemented; do not treat this documentation scaffold as a live simulator.

## Next gate

The NeuroFly project owner reviews and records the Phase 0 confirmation in `docs/phase0-checklist.md`. Phase 1 does not start until that confirmation is explicit. Connectome downloads and extraction remain out of scope until the dataset snapshot and identifier mapping are reviewed in Phase 1.
