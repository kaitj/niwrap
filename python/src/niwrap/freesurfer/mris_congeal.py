# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_CONGEAL_METADATA = Metadata(
    id="fa0f40776aa3fda2ba4fb3e5ddf05cf95f903e6f.boutiques",
    name="mris_congeal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisCongealOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_congeal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface"""


def mris_congeal(
    input_surface_name: str,
    hemi: str,
    subjects: list[str],
    output_surface_name: str,
    subjects_dir: str | None = None,
    disable_rigid_alignment: bool = False,
    disable_sulc_alignment: bool = False,
    smoothwm_curv: bool = False,
    jacobian_output: str | None = None,
    distance_term: float | None = None,
    manual_label: list[str] | None = None,
    addframe: list[str] | None = None,
    overlay: list[str] | None = None,
    overlay_dir: str | None = None,
    target_subject: bool = False,
    runner: Runner | None = None,
) -> MrisCongealOutputs:
    """
    Program that registers a set of input surfaces together and generates an atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface_name: Input surface name.
        hemi: Hemisphere (hemi).
        subjects: List of subjects.
        output_surface_name: Output surface name.
        subjects_dir: Subjects directory.
        disable_rigid_alignment: Disable initial rigid alignment.
        disable_sulc_alignment: Disable initial sulc alignment.
        smoothwm_curv: Use smoothwm curvature for final alignment.
        jacobian_output: Write-out jacobian overlay data to file.
        distance_term: Specify distance term.
        manual_label: Specify a manual label to align with atlas label.
        addframe: Add frame with specified parameters.
        overlay: Specify overlay surface values and number of averages.
        overlay_dir: Specify overlay directory.
        target_subject: Target specifies a subject's surface, not a template\
            file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCongealOutputs`).
    """
    if manual_label is not None and not (len(manual_label) <= 3): 
        raise ValueError(f"Length of 'manual_label' must be less than 3 but was {len(manual_label)}")
    if addframe is not None and not (len(addframe) <= 4): 
        raise ValueError(f"Length of 'addframe' must be less than 4 but was {len(addframe)}")
    if overlay is not None and not (len(overlay) <= 2): 
        raise ValueError(f"Length of 'overlay' must be less than 2 but was {len(overlay)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CONGEAL_METADATA)
    cargs = []
    cargs.append("mris_congeal")
    cargs.append(input_surface_name)
    cargs.append(hemi)
    cargs.append(" ".join(subjects) + "...")
    cargs.append(output_surface_name)
    if subjects_dir is not None:
        cargs.extend([
            "-SDIR",
            subjects_dir
        ])
    if disable_rigid_alignment:
        cargs.append("-norot")
    if disable_sulc_alignment:
        cargs.append("-nosulc")
    if smoothwm_curv:
        cargs.append("-curv")
    if jacobian_output is not None:
        cargs.extend([
            "-jacobian",
            jacobian_output
        ])
    if distance_term is not None:
        cargs.extend([
            "-dist",
            str(distance_term)
        ])
    if manual_label is not None:
        cargs.extend([
            "-l",
            *manual_label
        ])
    if addframe is not None:
        cargs.extend([
            "-addframe",
            *addframe
        ])
    if overlay is not None:
        cargs.extend([
            "-overlay",
            *overlay
        ])
    if overlay_dir is not None:
        cargs.extend([
            "-overlay-dir",
            overlay_dir
        ])
    if target_subject:
        cargs.append("-1")
    ret = MrisCongealOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(output_surface_name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_CONGEAL_METADATA",
    "MrisCongealOutputs",
    "mris_congeal",
]