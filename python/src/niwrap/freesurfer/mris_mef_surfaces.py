# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MEF_SURFACES_METADATA = Metadata(
    id="02223303295326924a357b3a06e1f9463f061c83.boutiques",
    name="mris_mef_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMefSurfacesParameters = typing.TypedDict('MrisMefSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_mef_surfaces"],
    "subject_name": str,
    "hemisphere": str,
    "omit_self_intersection": bool,
    "curvature": bool,
    "average_curvature": typing.NotRequired[float | None],
    "white_only": bool,
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
        "mris_mef_surfaces": mris_mef_surfaces_cargs,
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
    vt = {}
    return vt.get(t)


def mris_mef_surfaces_params(
    subject_name: str,
    hemisphere: str,
    omit_self_intersection: bool = False,
    curvature: bool = False,
    average_curvature: float | None = None,
    white_only: bool = False,
) -> MrisMefSurfacesParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere (e.g., left or right).
        omit_self_intersection: Omit self-intersection and only generate\
            gray/white surface.
        curvature: Create curvature and area files from the white matter\
            surface.
        average_curvature: Average curvature values specified number of times,\
            default is 10.
        white_only: Only generate the white matter surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_mef_surfaces",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "omit_self_intersection": omit_self_intersection,
        "curvature": curvature,
        "white_only": white_only,
    }
    if average_curvature is not None:
        params["average_curvature"] = average_curvature
    return params


def mris_mef_surfaces_cargs(
    params: MrisMefSurfacesParameters,
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
    cargs.append("mris_mef_surfaces")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    if params.get("omit_self_intersection"):
        cargs.append("-q")
    if params.get("curvature"):
        cargs.append("-c")
    if params.get("average_curvature") is not None:
        cargs.extend([
            "-a",
            str(params.get("average_curvature"))
        ])
    if params.get("white_only"):
        cargs.append("-whiteonly")
    return cargs


def mris_mef_surfaces_outputs(
    params: MrisMefSurfacesParameters,
    execution: Execution,
) -> MrisMefSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMefSurfacesOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_mef_surfaces_execute(
    params: MrisMefSurfacesParameters,
    execution: Execution,
) -> MrisMefSurfacesOutputs:
    """
    Positions the tessellation of the cortical surface at the white matter surface,
    then the gray matter surface and generates surface files for these surfaces.
    Also generates 'curvature' file for cortical thickness and a surface file
    approximating layer IV of the cortical sheet.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMefSurfacesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_mef_surfaces_cargs(params, execution)
    ret = mris_mef_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_mef_surfaces(
    subject_name: str,
    hemisphere: str,
    omit_self_intersection: bool = False,
    curvature: bool = False,
    average_curvature: float | None = None,
    white_only: bool = False,
    runner: Runner | None = None,
) -> MrisMefSurfacesOutputs:
    """
    Positions the tessellation of the cortical surface at the white matter surface,
    then the gray matter surface and generates surface files for these surfaces.
    Also generates 'curvature' file for cortical thickness and a surface file
    approximating layer IV of the cortical sheet.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        hemisphere: Hemisphere (e.g., left or right).
        omit_self_intersection: Omit self-intersection and only generate\
            gray/white surface.
        curvature: Create curvature and area files from the white matter\
            surface.
        average_curvature: Average curvature values specified number of times,\
            default is 10.
        white_only: Only generate the white matter surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMefSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MEF_SURFACES_METADATA)
    params = mris_mef_surfaces_params(subject_name=subject_name, hemisphere=hemisphere, omit_self_intersection=omit_self_intersection, curvature=curvature, average_curvature=average_curvature, white_only=white_only)
    return mris_mef_surfaces_execute(params, execution)


__all__ = [
    "MRIS_MEF_SURFACES_METADATA",
    "mris_mef_surfaces",
    "mris_mef_surfaces_params",
]
