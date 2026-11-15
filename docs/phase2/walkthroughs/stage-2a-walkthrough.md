# Stage 2A Walkthrough: Handoff and Scene Contract Inspection

**Document:** Stage 2A Review Walkthrough  
**Stage:** 2A — Handoff and scene contract  
**Active Repository Root:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`  
**Date:** 2026-11-14  

---

## 1. Overview and Objectives

This walkthrough guides the project owner or reviewer through inspecting the Stage 2A deliverables. Stage 2A converts the Phase 1 sensorimotor handoff and architecture into a formal implementation contract for the 3D Habitat greybox.

Reviewers will verify:
1. Ground-truth auditing of the active repository state and host toolchain.
2. The hierarchical scene graph, entity nomenclature, and camera specifications in `docs/phase2/scene-contract.md`.
3. The strict architectural separation between visitor-operated scientific trials and developer-only asset inspection tools.
4. The dynamic contact event specification, state transition rules, and JSON schema.
5. Rigorous categorization of all spatial and physical quantities as Confirmed, Provisional, or Unresolved.

---

## 2. Prerequisites and Environment

- **Operating System:** Windows 10/11 (PowerShell or Command Prompt).
- **Active Directory:** `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`.
- **Installed Toolchain:** Python 3.14.5 (installed and available on PATH).
- **Environment Note:** Node.js and npm are not currently installed on the host system. No web server or bundling command is assumed to exist.

---

## 3. Step-by-Step Inspection Procedure

### Step 1: Verify Repository and Toolchain Baseline
Open PowerShell in the repository root and inspect the working directory and toolchain status:
```powershell
# 1. Confirm working tree location
Get-Location

# 2. Verify git status
git status

# 3. Check Python and Node.js availability
python --version
Get-Command node -ErrorAction SilentlyContinue
```
**Expected Outcome:**
- Working directory is `C:\Users\abhi0\Desktop\NeuroFly\NeuroFly`.
- Git reports clean tracked tree or shows newly added Phase 2 staging documents in `docs/phase2/`.
- `python --version` returns `Python 3.14.5`.
- Node.js check returns null (confirming Node is not installed and no `npm` commands should be executed).

### Step 2: Inspect the Scene Contract Document
Open and review [scene-contract.md](file:///C:/Users/abhi0/Desktop/NeuroFly/NeuroFly/docs/phase2/scene-contract.md).
Inspect the following sections:
1. **Section 1 (Boundaries):** Verify that connectome data extraction, FAFB v783 root IDs, and neural integration are explicitly excluded.
2. **Section 2 (Repository Audit):** Verify that the audit accurately reflects the absence of `package.json`, empty asset directories, and the proposed smallest implementation path.
3. **Section 3 (Scene Graph):** Confirm the entity tree (`Scene_Root`, `Arena_Floor`, `Stimulus_Patch_Root`, `Fly_Root`, `Head`, `Proboscis_Pivot`, `Contact_Proxy_Labellum`).
4. **Section 4 (Camera System):** Verify definitions for Overview Orbit, Top-Down ($Y = +25\text{ mm}$), Lateral Profile ($X = +20\text{ mm}$), and Macro Contact Close-Up.
5. **Section 5 (Control Bifurcation):** Confirm the strict boundary: visitors manipulate only stimuli and trial triggers; direct joint posing is restricted to the developer inspection panel.
6. **Section 6 (Contact Event Schema):** Inspect the transition-only debouncing requirement and the JSON payload schema.
7. **Section 7 (Categorization Table):** Check that every numerical parameter is tagged as Confirmed, Provisional, or Unresolved, ensuring no provisional value is mischaracterized as biological fact.

---

## 4. Reset and Clean-Up

Because Stage 2A is a contract and architectural specification stage, no transient processes or background servers were spawned. No reset actions are required.

