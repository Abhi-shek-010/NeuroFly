# NeuroFly

NeuroFly is a connectome-constrained virtual adult fruit fly in one shared 3D experiment habitat. The first planned experiment follows physical taste contact through gustatory input and a candidate neural circuit to a modeled proboscis response; exact FAFB v783 cell identities and edges remain unverified until Phase 3.

## Project status

- Current phase: Phase 2, Asset triage and Habitat greybox.
- Phase 0 was confirmed by the project owner on 2026-11-01. Phase 1 was confirmed with a scope limitation on 2026-11-14; Phase 2 is approved to begin.
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
- [`docs/assay-and-data-handoff.md`](docs/assay-and-data-handoff.md) - owner-approved provisional assay and dataset handoff; extraction remains blocked until Phase 3 verifies exact cell identities and edges.
- [`docs/architecture.md`](docs/architecture.md) - proposed runtime and deployment boundaries.
- [`docs/decisions.md`](docs/decisions.md) and [`docs/risks.md`](docs/risks.md) - open decisions and risks.
- [`docs/phase0-checklist.md`](docs/phase0-checklist.md) - current evidence and signoff gate.
- [`docs/phase0-walkthrough-and-summary.md`](docs/phase0-walkthrough-and-summary.md) - detailed map of Phase 0 work, evidence, open items, and handoff.

## Local run instructions

There is no runnable application yet. Phase 0 established the project record and repository layout; Phase 2 has not yet produced a runnable application. A local start command will be added when the application runtime is selected and implemented; do not treat this documentation scaffold as a live simulator.

## Next gate

Phase 1 owner approval is recorded in docs/phase1/phase1-open-decisions.md. Phase 2 (asset triage and Habitat greybox) is approved to begin. Exact FAFB v783 cell IDs and pairwise edges remain unresolved and gated on Phase 3; neural integration and cell-level pathway claims must wait for that verification.
