# Evidence and Claims Rules

## Evidence vocabulary

- **Measured:** a value or relationship directly present in a named dataset or published experiment, with its source and version recorded.
- **Inferred:** a biological interpretation supported by evidence but not directly established by the selected data.
- **Modeled:** a rule or parameter implemented by NeuroFly, including sensory encoding, neural dynamics, weight conversion, motor decoding, and body mechanics.
- **Predicted:** an expected result written before a comparison or held-out result is inspected.
- **Display-only:** a visual aid such as glow, interpolated animation, or a decorative overlay that does not feed simulation state or determine the fly's action.

## Claim boundary

Use this boundary in project descriptions: **NeuroFly is a connectome-constrained model of a selected behavior, not a complete biological fly or whole-brain simulator.**

The connectome supplies measured structural wiring. It does not by itself provide neural dynamics, synaptic current, receptor responses, a motor decoder, or validated body mechanics. Those parts must be identified as inferred or modeled and supported with methods, calibration, or sensitivity analysis as appropriate.

## Interface and trial rules

1. A scientific trial's visible proboscis action must be driven by the simulation output; a renderer control cannot select the expected response.
2. Contact must depend on body pose and patch geometry. Clicking a patch cannot directly trigger feeding.
3. A no-response outcome is preserved as a valid result.
4. Baseline and intervention trials share the same initial pose, contact, stimulus, seed policy, and trial settings unless the changed variable is explicitly listed.
5. Any browser preview, surrogate, reference physics run, and recorded replay must be labeled separately.
6. Run records should reserve fields for scenario, dataset release, graph checksum, model and parameter versions, pose, stimulus, seed, intervention, time-stamped sensor/circuit/motor/body summaries, outcome, failures, and software build.

## Phase 0 status

These rules are recorded as the working standard. Project-owner approval is still pending.
