"""
NeuroFly Habitat Scene Spatial Configuration and Coordinate Mapping Engine
Phase: 2 — Asset triage and Habitat greybox
Stage: 2B — World scale and coordinate map

Single source of truth for:
- Coordinate axes definitions and unit conversion policies.
- Named entity world positions, bounding geometries, and kinematic hierarchies.
- Forward kinematics for the proboscis rostrum articulation.
- Geometric contact overlap detection between the labellar proxy and stimulus patch.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Vector3:
    x: float
    y: float
    z: float

    def to_list(self) -> List[float]:
        return [self.x, self.y, self.z]

    def __add__(self, other: Vector3) -> Vector3:
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance_to(self, other: Vector3) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

    def planar_distance_to(self, other: Vector3) -> float:
        """Distance in the horizontal XZ ground plane."""
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.z - other.z) ** 2
        )


@dataclass(frozen=True)
class KinematicPose:
    theta_deg: float
    pivot_world_position: Vector3
    proxy_world_position: Vector3
    is_contact_active: bool
    penetration_depth_mm: float
    distance_to_patch_center_mm: float


class SceneCoordinateConfig:
    """Manages spatial transformations, unit conversions, and geometric queries for the NeuroFly Habitat."""

    DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent.parent / "scenarios" / "scene_config.json"

    def __init__(self, config_dict: Dict[str, Any]):
        self.raw_config = config_dict
        
        # Coordinate conventions
        coord = config_dict["coordinate_convention"]
        self.system = coord["system"]
        self.up_axis = coord["up_axis"]
        self.forward_axis = coord["forward_axis"]
        self.transverse_axis = coord["transverse_axis"]
        self.origin = Vector3(*coord["world_origin"])
        
        # Scale and unit conversion policy
        scale = config_dict["scale_and_units"]
        self.unit_symbol = scale["unit_symbol"]
        self.threejs_scale_factor = float(scale["threejs_scale_factor"])
        self.meters_per_wu = float(scale["meters_per_world_unit"])
        self.micrometers_per_wu = float(scale["micrometers_per_world_unit"])
        self.camera_near_clip_mm = float(scale["camera_near_clip_mm"])
        self.camera_far_clip_mm = float(scale["camera_far_clip_mm"])
        
        # Arena
        arena = config_dict["arena"]
        self.arena_radius_mm = float(arena["radius_mm"])
        self.arena_floor_y_mm = float(arena["floor_plane_y_mm"])
        self.perimeter_rail_height_mm = float(arena["perimeter_rail"]["height_mm"])
        
        # Stimulus Patch
        patch = config_dict["stimulus_patch"]
        self.patch_center_mm = Vector3(*patch["center_mm"])
        self.patch_radius_mm = float(patch["radius_mm"])
        self.patch_thickness_mm = float(patch["visual_thickness_mm"])
        self.patch_interaction_height_mm = float(patch["interaction_cylinder_height_mm"])
        self.stimulus_condition = str(patch["condition"])
        
        # Fly Root and Anatomy
        fly = config_dict["fly_spatial_configuration"]
        self.fly_root_resting = Vector3(*fly["resting_position_mm"])
        hierarchy = fly["body_hierarchy"]
        self.head_center_world = Vector3(*hierarchy["head_center_world_mm"])
        
        # Proboscis Pivot
        pivot_cfg = hierarchy["proboscis_pivot"]
        self.proboscis_pivot_resting = Vector3(*pivot_cfg["world_resting_position_mm"])
        self.angle_min_deg = float(pivot_cfg["angle_min_deg"])
        self.angle_max_deg = float(pivot_cfg["angle_max_deg"])
        self.resting_angle_deg = float(pivot_cfg["resting_angle_deg"])
        
        # Contact Proxy (Labellum)
        proxy_cfg = hierarchy["contact_proxy"]
        self.contact_proxy_radius_mm = float(proxy_cfg["radius_mm"])
        self.contact_proxy_resting = Vector3(*proxy_cfg["resting_world_center_mm"])
        self.contact_proxy_max_extended = Vector3(*proxy_cfg["max_extended_world_center_mm"])

    @classmethod
    def load(cls, config_path: Optional[Path] = None) -> SceneCoordinateConfig:
        path = config_path or cls.DEFAULT_CONFIG_PATH
        if not path.is_file():
            raise FileNotFoundError(f"Scene configuration file not found at: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(data)

    # -------------------------------------------------------------------------
    # Unit Conversions
    # -------------------------------------------------------------------------
    def world_to_threejs(self, pos_mm: Vector3) -> Vector3:
        """Converts millimeter world coordinates to Three.js scene units."""
        return Vector3(
            pos_mm.x * self.threejs_scale_factor,
            pos_mm.y * self.threejs_scale_factor,
            pos_mm.z * self.threejs_scale_factor
        )

    def threejs_to_world(self, pos_three: Vector3) -> Vector3:
        """Converts Three.js scene units back to millimeter world coordinates."""
        return Vector3(
            pos_three.x / self.threejs_scale_factor,
            pos_three.y / self.threejs_scale_factor,
            pos_three.z / self.threejs_scale_factor
        )

    def world_to_micrometers(self, pos_mm: Vector3) -> Vector3:
        """Converts millimeter coordinates to micrometers (connectome / cell scale)."""
        return Vector3(
            pos_mm.x * self.micrometers_per_wu,
            pos_mm.y * self.micrometers_per_wu,
            pos_mm.z * self.micrometers_per_wu
        )

    def world_to_si_meters(self, pos_mm: Vector3) -> Vector3:
        """Converts millimeter coordinates to SI standard meters."""
        return Vector3(
            pos_mm.x * self.meters_per_wu,
            pos_mm.y * self.meters_per_wu,
            pos_mm.z * self.meters_per_wu
        )

    # -------------------------------------------------------------------------
    # Forward Kinematics
    # -------------------------------------------------------------------------
    def forward_kinematics(self, theta_deg: float, override_patch_center: Optional[Vector3] = None) -> KinematicPose:
        """
        Computes forward kinematics of the proboscis pivot and distal labellar contact proxy.
        
        Kinematic Model:
        - Input: theta_deg in [angle_min_deg, angle_max_deg] (0.0 to 45.0 degrees).
        - Pivot remains stationary at proboscis_pivot_resting [0.0, 0.45, 0.70].
        - Contact proxy interpolates along the biological protraction trajectory from
          resting [0.0, 0.35, 0.55] to maximum extension [0.0, 0.05, 1.15].
        """
        clamped_theta = max(self.angle_min_deg, min(self.angle_max_deg, float(theta_deg)))
        t = (clamped_theta - self.angle_min_deg) / (self.angle_max_deg - self.angle_min_deg)

        # Smooth parametric interpolation along the protraction arc
        # As proboscis protracts, it extends anteriorly (+Z) and descends towards ground (+Y -> 0)
        proxy_x = 0.0
        proxy_y = self.contact_proxy_resting.y + t * (self.contact_proxy_max_extended.y - self.contact_proxy_resting.y)
        proxy_z = self.contact_proxy_resting.z + t * (self.contact_proxy_max_extended.z - self.contact_proxy_resting.z)
        proxy_pos = Vector3(proxy_x, proxy_y, proxy_z)

        patch_center = override_patch_center or self.patch_center_mm

        # Contact detection against the cylindrical interaction volume of the stimulus patch
        # Patch interaction volume: cylinder centered at patch_center, radius R = 1.0 mm, height H = 0.1 mm [0.0, 0.1]
        planar_dist = proxy_pos.planar_distance_to(patch_center)
        in_planar_patch = planar_dist <= (self.patch_radius_mm + self.contact_proxy_radius_mm)
        
        # Vertical overlap check (ground to top of interaction volume)
        y_bottom = self.arena_floor_y_mm
        y_top = patch_center.y + self.patch_interaction_height_mm
        proxy_bottom = proxy_pos.y - self.contact_proxy_radius_mm
        proxy_top = proxy_pos.y + self.contact_proxy_radius_mm
        vertical_overlap = (proxy_bottom <= y_top) and (proxy_top >= y_bottom)

        is_contact = in_planar_patch and vertical_overlap
        
        # Penetration depth calculation:
        dist_to_center = proxy_pos.distance_to(patch_center)
        if is_contact:
            # Positive penetration depth when intersecting
            vertical_pen = y_top - proxy_bottom
            radial_pen = (self.patch_radius_mm + self.contact_proxy_radius_mm) - planar_dist
            penetration_depth = min(vertical_pen, radial_pen)
        else:
            # Negative separation distance
            radial_sep = planar_dist - (self.patch_radius_mm + self.contact_proxy_radius_mm)
            vertical_sep = proxy_bottom - y_top
            penetration_depth = -max(radial_sep, vertical_sep)

        return KinematicPose(
            theta_deg=clamped_theta,
            pivot_world_position=self.proboscis_pivot_resting,
            proxy_world_position=proxy_pos,
            is_contact_active=is_contact,
            penetration_depth_mm=penetration_depth,
            distance_to_patch_center_mm=dist_to_center
        )

    # -------------------------------------------------------------------------
    # Verification & Self-Test Suite
    # -------------------------------------------------------------------------
    def run_spatial_verification(self) -> Dict[str, Any]:
        """Runs automated spatial verification tests against Stage 2B criteria."""
        results = {}
        
        # Check 1: Resting Stance (theta = 0 deg)
        rest_pose = self.forward_kinematics(0.0)
        results["resting_pose"] = {
            "theta_deg": rest_pose.theta_deg,
            "proxy_position": rest_pose.proxy_world_position.to_list(),
            "is_contact": rest_pose.is_contact_active,
            "penetration_depth_mm": round(rest_pose.penetration_depth_mm, 4),
            "pass_resting_no_contact": not rest_pose.is_contact_active
        }
        
        # Check 2: Intermediate Pose (theta = 20 deg, Phase 1 threshold)
        mid_pose = self.forward_kinematics(20.0)
        results["intermediate_pose"] = {
            "theta_deg": mid_pose.theta_deg,
            "proxy_position": [round(c, 4) for c in mid_pose.proxy_world_position.to_list()],
            "is_contact": mid_pose.is_contact_active,
            "penetration_depth_mm": round(mid_pose.penetration_depth_mm, 4)
        }
        
        # Check 3: Maximum Extension (theta = 45 deg)
        max_pose = self.forward_kinematics(45.0)
        results["max_extension_pose"] = {
            "theta_deg": max_pose.theta_deg,
            "proxy_position": [round(c, 4) for c in max_pose.proxy_world_position.to_list()],
            "is_contact": max_pose.is_contact_active,
            "penetration_depth_mm": round(max_pose.penetration_depth_mm, 4),
            "pass_max_contact_active": max_pose.is_contact_active
        }
        
        # Check 4: Negative Control #1 (Patch placed out of reach at Z = 3.5 mm)
        out_of_reach_center = Vector3(0.0, 0.0, 3.5)
        out_of_reach_pose = self.forward_kinematics(45.0, override_patch_center=out_of_reach_center)
        results["out_of_reach_control"] = {
            "patch_center": out_of_reach_center.to_list(),
            "theta_deg": 45.0,
            "is_contact": out_of_reach_pose.is_contact_active,
            "pass_negative_control": not out_of_reach_pose.is_contact_active
        }
        
        # Check 5: Boundary & Scale Checks
        results["arena_checks"] = {
            "arena_radius_mm": self.arena_radius_mm,
            "fly_within_arena": self.fly_root_resting.planar_distance_to(self.origin) < self.arena_radius_mm,
            "patch_within_arena": self.patch_center_mm.planar_distance_to(self.origin) < self.arena_radius_mm,
            "threejs_scale_ratio": self.threejs_scale_factor
        }
        
        all_passed = (
            results["resting_pose"]["pass_resting_no_contact"] and
            results["max_extension_pose"]["pass_max_contact_active"] and
            results["out_of_reach_control"]["pass_negative_control"] and
            results["arena_checks"]["fly_within_arena"] and
            results["arena_checks"]["patch_within_arena"]
        )
        results["all_checks_passed"] = all_passed
        return results


def main() -> None:
    """CLI execution for verifying Habitat world scale and coordinate transforms."""
    print("=================================================================")
    print(" NeuroFly Stage 2B: Habitat World Scale & Coordinate Map Check   ")
    print("=================================================================")
    
    config = SceneCoordinateConfig.load()
    print(f"Loaded configuration from: {SceneCoordinateConfig.DEFAULT_CONFIG_PATH.name}")
    print(f"Coordinate System   : {config.system}")
    print(f"Axes Convention     : Up={config.up_axis} ({config.raw_config['coordinate_convention']['up_anatomical']}), "
          f"Forward={config.forward_axis} ({config.raw_config['coordinate_convention']['forward_anatomical']}), "
          f"Transverse={config.transverse_axis}")
    print(f"Scale Policy        : {config.raw_config['scale_and_units']['conversion_policy']}")
    print(f"Arena Boundary      : Radius = {config.arena_radius_mm} mm (Diameter = {config.arena_radius_mm * 2} mm)")
    print(f"Stimulus Patch      : Center = {config.patch_center_mm.to_list()} mm, Radius = {config.patch_radius_mm} mm")
    print(f"Fly Root Resting    : {config.fly_root_resting.to_list()} mm, facing {config.raw_config['fly_spatial_configuration']['facing_direction']}")
    print(f"Proboscis Pivot     : {config.proboscis_pivot_resting.to_list()} mm (world resting)")
    print(f"Contact Proxy       : Radius = {config.contact_proxy_radius_mm} mm (distal sphere)")
    print("-----------------------------------------------------------------")
    print("Running Spatial & Kinematic Checks:")
    
    results = config.run_spatial_verification()
    
    rest = results["resting_pose"]
    print(f"[Check 1] Resting Pose (theta = 0.0 deg):")
    print(f"  Proxy Position    : {rest['proxy_position']} mm")
    print(f"  Contact Active    : {rest['is_contact']} (Expected: False)")
    print(f"  Penetration Depth : {rest['penetration_depth_mm']} mm")
    print(f"  Status            : {'PASS' if rest['pass_resting_no_contact'] else 'FAIL'}")
    
    mid = results["intermediate_pose"]
    print(f"[Check 2] Intermediate Pose (theta = 20.0 deg):")
    print(f"  Proxy Position    : {mid['proxy_position']} mm")
    print(f"  Contact Active    : {mid['is_contact']}")
    print(f"  Penetration Depth : {mid['penetration_depth_mm']} mm")
    
    ext = results["max_extension_pose"]
    print(f"[Check 3] Max Extension (theta = 45.0 deg):")
    print(f"  Proxy Position    : {ext['proxy_position']} mm")
    print(f"  Contact Active    : {ext['is_contact']} (Expected: True)")
    print(f"  Penetration Depth : {ext['penetration_depth_mm']} mm")
    print(f"  Status            : {'PASS' if ext['pass_max_contact_active'] else 'FAIL'}")
    
    ctrl = results["out_of_reach_control"]
    print(f"[Check 4] Negative Control (Patch at Z = 3.5 mm, theta = 45.0 deg):")
    print(f"  Patch Position    : {ctrl['patch_center']} mm")
    print(f"  Contact Active    : {ctrl['is_contact']} (Expected: False)")
    print(f"  Status            : {'PASS' if ctrl['pass_negative_control'] else 'FAIL'}")
    
    arena = results["arena_checks"]
    print(f"[Check 5] Boundary Containment:")
    print(f"  Fly Root inside Arena  : {'PASS' if arena['fly_within_arena'] else 'FAIL'}")
    print(f"  Patch inside Arena     : {'PASS' if arena['patch_within_arena'] else 'FAIL'}")
    print(f"  Scale Factor (WU / mm) : {arena['threejs_scale_ratio']}")
    print("-----------------------------------------------------------------")
    overall = "ALL CHECKS PASSED (Ready for Stage 2B Gate)" if results["all_checks_passed"] else "CHECKS FAILED"
    print(f"Overall Result: {overall}")
    print("=================================================================")


if __name__ == "__main__":
    main()
