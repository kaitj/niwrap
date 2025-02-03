# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_THICKNESS_METADATA = Metadata(
    id="1f70790c09e2a07e9627e797f2437c49106bcce2.boutiques",
    name="mris_thickness",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisThicknessParameters = typing.TypedDict('MrisThicknessParameters', {
    "__STYX_TYPE__": typing.Literal["mris_thickness"],
    "subject_name": str,
    "hemi": str,
    "thickness_file": str,
    "max_threshold": typing.NotRequired[float | None],
    "fill_holes": typing.NotRequired[list[str] | None],
    "thickness_from_seg": typing.NotRequired[list[str] | None],
    "vector": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "mris_thickness": mris_thickness_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "mris_thickness": mris_thickness_outputs,
    }
    return vt.get(t)


class MrisThicknessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_thickness_file: OutputPathType
    """Output curvature file containing thickness measurements."""


def mris_thickness_params(
    subject_name: str,
    hemi: str,
    thickness_file: str,
    max_threshold: float | None = None,
    fill_holes: list[str] | None = None,
    thickness_from_seg: list[str] | None = None,
    vector: bool = False,
) -> MrisThicknessParameters:
    """
    Build parameters.
    
    Args:
        subject_name: The subject name for processing.
        hemi: The hemisphere to process (e.g., lh or rh).
        thickness_file: Output file for thickness measurements.
        max_threshold: Use a maximum threshold for thickness (default is 5mm).
        fill_holes: Fill in thickness in holes in the cortex label using\
            fsaverage cortex label.
        thickness_from_seg: Compute thickness from segmentation. Requires the\
            following parameters: surf label, seg.mgz, dmaxmm, ddeltamm, and\
            output.mgz.
        vector: Compute the thickness using a variationally derived vector\
            field.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_thickness",
        "subject_name": subject_name,
        "hemi": hemi,
        "thickness_file": thickness_file,
        "vector": vector,
    }
    if max_threshold is not None:
        params["max_threshold"] = max_threshold
    if fill_holes is not None:
        params["fill_holes"] = fill_holes
    if thickness_from_seg is not None:
        params["thickness_from_seg"] = thickness_from_seg
    return params


def mris_thickness_cargs(
    params: MrisThicknessParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("mris_thickness")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("thickness_file"))
    if params.get("max_threshold") is not None:
        cargs.extend([
            "-max",
            str(params.get("max_threshold"))
        ])
    if params.get("fill_holes") is not None:
        cargs.extend([
            "-fill_holes",
            *params.get("fill_holes")
        ])
    if params.get("thickness_from_seg") is not None:
        cargs.extend([
            "-thickness-from-seg",
            *params.get("thickness_from_seg")
        ])
    if params.get("vector"):
        cargs.append("-vector")
    return cargs


def mris_thickness_outputs(
    params: MrisThicknessParameters,
    execution: Execution,
) -> MrisThicknessOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisThicknessOutputs(
        root=execution.output_file("."),
        output_thickness_file=execution.output_file(params.get("thickness_file")),
    )
    return ret


def mris_thickness_execute(
    params: MrisThicknessParameters,
    execution: Execution,
) -> MrisThicknessOutputs:
    """
    Measures the thickness of the cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_thickness_cargs(params, execution)
    ret = mris_thickness_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_thickness(
    subject_name: str,
    hemi: str,
    thickness_file: str,
    max_threshold: float | None = None,
    fill_holes: list[str] | None = None,
    thickness_from_seg: list[str] | None = None,
    vector: bool = False,
    runner: Runner | None = None,
) -> MrisThicknessOutputs:
    """
    Measures the thickness of the cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: The subject name for processing.
        hemi: The hemisphere to process (e.g., lh or rh).
        thickness_file: Output file for thickness measurements.
        max_threshold: Use a maximum threshold for thickness (default is 5mm).
        fill_holes: Fill in thickness in holes in the cortex label using\
            fsaverage cortex label.
        thickness_from_seg: Compute thickness from segmentation. Requires the\
            following parameters: surf label, seg.mgz, dmaxmm, ddeltamm, and\
            output.mgz.
        vector: Compute the thickness using a variationally derived vector\
            field.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_METADATA)
    params = mris_thickness_params(subject_name=subject_name, hemi=hemi, thickness_file=thickness_file, max_threshold=max_threshold, fill_holes=fill_holes, thickness_from_seg=thickness_from_seg, vector=vector)
    return mris_thickness_execute(params, execution)


__all__ = [
    "MRIS_THICKNESS_METADATA",
    "MrisThicknessOutputs",
    "mris_thickness",
    "mris_thickness_params",
]
