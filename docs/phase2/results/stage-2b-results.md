# Stage 2B Results: World Scale and Coordinate Map

**Document:** Stage 2B Evaluation & Results Record  
**Stage:** 2B — World scale and coordinate map  
**Active Repository Root:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Date:** 2026-11-14  
**Status:** Complete — Recommended for Owner Acceptance  

---

## 1. Summary of Changes

Stage 2B establishes the spatial foundation and coordinate authority for the NeuroFly Habitat in accordance with `docs/phase2/README.md`.

Key accomplishments:
1. **Centralized Spatial Configuration (`scenarios/scene_config.json`):** Created a single source of truth defining world units, right-handed Cartesian axes ($+Y$ up/dorsal, $+Z$ forward/anterior, $+X$ lateral right), the origin at arena center $(0, 0, 0)$, entity bounds, and camera viewports.
2. **Explicit Unit Conversion Policy:** Standardized $1.0\text{ Three.js World Unit (WU)} = 1.0\text{ millimeter (mm)}$, with documented conversions to micrometers ($1000\times$), FAFB EM voxel units ($10^6\times$), and SI meters ($0.001\times$). Optimized depth buffer clipping planes ($0.1\text{ mm}$ near, $100.0\text{ mm}$ far).
3. **Programmatic Spatial & Kinematic Engine (`body/scene_coordinate_config.py`):** Implemented a Python 3 verification engine that loads `scene_config.json`, calculates proboscis forward kinematics, performs geometric overlap testing between the labellar contact proxy and stimulus patch, and validates negative control conditions.
4. **Comprehensive Documentation (`docs/phase2/world-coordinate-map.md`):** Provided mathematical equations, an anatomical axis mapping table, a master entity coordinate matrix, and forward kinematics verification results.
5. **Predeclared Negative Control Verification:** Programmatically verified that placing the stimulus patch at $Z = 3.5\text{ mm}$ ($d > 2.0\text{ mm}$) reliably results in zero contact even at maximum protraction ($\theta = 45^\circ$).

---

## 2. Files Created and Modified

- **Created:**
  - `scenarios/scene_config.json` (Central machine-readable spatial configuration)
  - `body/scene_coordinate_config.py` (Programmatic coordinate transform and validation module)
  - `docs/phase2/world-coordinate-map.md` (World scale and coordinate map specification)
  - `docs/phase2/walkthroughs/stage-2b-walkthrough.md` (Stage 2B inspection walkthrough)
  - `docs/phase2/results/stage-2b-results.md` (This evaluation and results record)
- **Modified:**
  - `docs/phase2/scene-contract.md` (Updated coordinates to reflect verified geometric alignment with `scene_config.json`).

---

## 3. Build, Run, and Verification Commands

The following command was executed to verify the spatial configuration:

```powershell
python "C:\Users\abhi0\Desktop\NeuroFly\NeuroFly\body\scene_coordinate_config.py"
```

**Observed Command Output:**
```
=================================================================
 NeuroFly Stage 2B: Habitat World Scale & Coordinate Map Check   
=================================================================
Loaded configuration from: scene_config.json
Coordinate System   : Right-Handed Cartesian
Axes Convention     : Up=+Y (Dorsal), Forward=+Z (Anterior), Transverse=+X
Scale Policy        : 1.0 Three.js World Unit (WU) = 1.0 millimeter (mm)
Arena Boundary      : Radius = 15.0 mm (Diameter = 30.0 mm)
Stimulus Patch      : Center = [0.0, 0.0, 2.0] mm, Radius = 1.0 mm
Fly Root Resting    : [0.0, 0.75, 0.0] mm, facing +Z
Proboscis Pivot     : [0.0, 0.45, 0.7] mm (world resting)
Contact Proxy       : Radius = 0.15 mm (distal sphere)
-----------------------------------------------------------------
Running Spatial & Kinematic Checks:
[Check 1] Resting Pose (theta = 0.0 deg):
  Proxy Position    : [0.0, 0.35, 0.55] mm
  Contact Active    : False (Expected: False)
  Penetration Depth : -0.3 mm
  Status            : PASS
[Check 2] Intermediate Pose (theta = 20.0 deg):
  Proxy Position    : [0.0, 0.2167, 0.8167] mm
  Contact Active    : False
  Penetration Depth : -0.0333 mm
[Check 3] Max Extension (theta = 45.0 deg):
  Proxy Position    : [0.0, 0.05, 1.15] mm
  Contact Active    : True (Expected: True)
  Penetration Depth : 0.2 mm
  Status            : PASS
[Check 4] Negative Control (Patch at Z = 3.5 mm, theta = 45.0 deg):
  Patch Position    : [0.0, 0.0, 3.5] mm
  Contact Active    : False (Expected: False)
  Status            : PASS
[Check 5] Boundary Containment:
  Fly Root inside Arena  : PASS
  Patch inside Arena     : PASS
  Scale Factor (WU / mm) : 1.0
-----------------------------------------------------------------
Overall Result: ALL CHECKS PASSED (Ready for Stage 2B Gate)
=================================================================
```

---

## 4. Manual Acceptance Checklist & Observed Outcomes

| Acceptance Item | Criteria from Implementation Guide | Observed Outcome | Status |
|---|---|---|:---:|
| **1. Explicit Coordinate Convention** | Define up axis, forward direction, world origin, fly facing, and units. | $+Y$ Up (Dorsal), $+Z$ Forward (Anterior), $+X$ Right (Lateral); Origin at arena floor center $(0,0,0)$; Units: mm. | **PASS** |
| **2. Central Configuration** | Put scale, transforms, and dimensions in a central configuration or module. | Fully declared in `scenarios/scene_config.json` with schema validation and epistemic tagging. | **PASS** |
| **3. Named Entity Placement** | Define arena, floor, patch, fly root, contact proxy, and proboscis pivot. | Complete coordinate matrix documented and mathematically verified without guessing. | **PASS** |
| **4. Scale Conversion Policy** | Document coordinate conversion at any rendering boundary; do not assume units. | Explicit conversion equations defined: $1.0\text{ Three.js WU} = 1.0\text{ mm} = 1000\ \mu\text{m} = 10^{-3}\text{ m}$. | **PASS** |
| **5. Forward Kinematics & Contact** | Verify resting, intermediate, and extended poses; confirm contact state transitions. | Resting ($\theta=0^\circ$) has no contact ($-0.3\text{ mm}$ clearance); Max extension ($\theta=45^\circ$) activates contact ($+0.2\text{ mm}$ penetration). | **PASS** |
| **6. Negative Control Verification** | Verify that patch placed out of reach ($d > 2.0\text{ mm}$) produces zero contact. | Evaluated at $Z = 3.5\text{ mm}$; contact remained False at full extension ($\theta = 45^\circ$). | **PASS** |
| **7. Developer Scale Aids** | Specify scale/axis aids for inspection, hidden from normal presentation. | Specified tri-axis gizmo, metric grid, and collision wireframes with default-hidden flag. | **PASS** |

---

## 5. Known Limitations, Deviations, and Open Decisions

1. **Host Toolchain (Node.js Absence):** Node.js remains uninstalled on the host system. All Stage 2B spatial logic was verified using Python 3.14.5 against the central JSON configuration. When Node.js is provisioned by the project owner, the Three.js scene loader in `frontend/` can parse `scenarios/scene_config.json` directly.
2. **Provisional Anatomy:** The fly body proportions ($2.5\text{ mm}$ length, $1.5\text{ mm}$ stance height) and proboscis kinematics are provisional engineering representations designed to support the 3D greybox, not validated biomechanical fly models.
3. **No External Asset Intake:** External fly models remain unverified and blocked; procedural greybox geometry will be used in Stage 2D.

---

## 6. Verdict and Stage Transition

- **Stage 2B Verdict:** **Complete** — All acceptance criteria verified.
- **Stage Transition Status:** In accordance with the Stage 2B completion gate and the user request ("implement upto phase 2B as mentioned in the file"), **execution is halted at the Stage 2B Gate**.
- **Stage 2C (Habitat greybox) has NOT been started.**

