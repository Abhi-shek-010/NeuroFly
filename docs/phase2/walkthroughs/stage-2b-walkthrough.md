# Stage 2B Walkthrough: World Scale and Coordinate Map Verification

**Document:** Stage 2B Review Walkthrough  
**Stage:** 2B — World scale and coordinate map  
**Active Repository Root:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Date:** 2026-11-14  

---

## 1. Overview and Objectives

This walkthrough guides the project owner or reviewer through verifying the Stage 2B deliverables:
1. Inspection of the centralized machine-readable spatial configuration in `scenarios/scene_config.json`.
2. Review of the comprehensive spatial coordinate matrix and conversion policies in `docs/phase2/world-coordinate-map.md`.
3. Execution of the programmatic spatial verification engine in `body/scene_coordinate_config.py` using Python 3.14.5.
4. Mathematical verification of proboscis forward kinematics, contact state transitions, and the predeclared negative controls (out-of-reach sucrose patch).

---

## 2. Prerequisites

- **Environment:** Windows 10/11 (PowerShell or Command Prompt).
- **Active Directory:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`.
- **Runtime:** Python 3.14.5 (installed and available on PATH).
- **Required Files on Disk:**
  - `scenarios/scene_config.json`
  - `body/scene_coordinate_config.py`
  - `docs/phase2/world-coordinate-map.md`
  - `docs/phase2/scene-contract.md`

---

## 3. Step-by-Step Verification Procedure

### Step 1: Run the Programmatic Spatial Verification Suite
Execute the verified spatial verification engine from the repository root:
```powershell
python "C:\Users\abhi0\Desktop\NeuroFly\NeuroFly\body\scene_coordinate_config.py"
```

**Expected Console Output:**
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

### Step 2: Inspect Central Spatial Configuration (`scenarios/scene_config.json`)
Open [scene_config.json](file:///C:/Users/abhi0/Desktop/NeuroFly/NeuroFly/scenarios/scene_config.json) and verify:
1. **Coordinate convention:** Right-handed Cartesian with $+Y$ Up, $+Z$ Forward, and $+X$ Right.
2. **Scale factor:** Explicitly declared as `1.0 Three.js World Unit (WU) = 1.0 millimeter (mm)`.
3. **Camera clip planes:** Near clip $0.1\text{ mm}$, far clip $100.0\text{ mm}$ (ratio $1000:1$ preventing depth buffer precision loss).
4. **Entity positions:** Arena floor at $Y = 0.0\text{ mm}$, radius $15.0\text{ mm}$; stimulus patch at $[0, 0, 2.0]\text{ mm}$, radius $1.0\text{ mm}$; fly root at $[0, 0.75, 0.0]\text{ mm}$.
5. **Epistemic labeling:** All parameters correctly tagged as Confirmed, Provisional, or Unresolved.

### Step 3: Inspect World Coordinate Map Document (`docs/phase2/world-coordinate-map.md`)
Open [world-coordinate-map.md](file:///C:/Users/abhi0/Desktop/NeuroFly/NeuroFly/docs/phase2/world-coordinate-map.md) and review:
1. **Section 2:** Axis diagrams and biological anatomical mappings (Dorsal-Ventral, Anterior-Posterior, Medial-Lateral).
2. **Section 3:** Cross-system conversion equations for Three.js, biophysics, micrometers, voxels, and SI meters.
3. **Section 4:** Master coordinate table of named transforms and collision shapes.
4. **Section 5:** Kinematic equations, angle sweep table ($\theta = 0^\circ$ to $45^\circ$), and negative control verification.
5. **Section 6:** Specification of developer scale aids (axes gizmo, metric grid, collider wireframes) and default-hidden enforcement.

---

## 4. Reset and Clean-Up

The verification engine runs statelessly in-memory and writes no disk artifacts or background daemon processes. No cleanup is required.

