# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_RETINO_MAP_METADATA = Metadata(
    id="0a0bd510fbdb86c742b4ce55d2755f1f8650721e.boutiques",
    name="SurfRetinoMap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfRetinoMapParameters = typing.TypedDict('SurfRetinoMapParameters', {
    "__STYX_TYPE__": typing.Literal["SurfRetinoMap"],
    "surface": str,
    "polar": str,
    "eccentricity": str,
    "prefix": typing.NotRequired[str | None],
    "node_debug": typing.NotRequired[float | None],
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
        "SurfRetinoMap": surf_retino_map_cargs,
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
        "SurfRetinoMap": surf_retino_map_outputs,
    }
    return vt.get(t)


class SurfRetinoMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_retino_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    vfr_output: OutputPathType | None
    """Output Visual Field Ratio (VFR) dataset."""
    threshold_max_output: OutputPathType | None
    """Maximum threshold at each node in the input datasets."""


def surf_retino_map_params(
    surface: str,
    polar: str,
    eccentricity: str,
    prefix: str | None = None,
    node_debug: float | None = None,
) -> SurfRetinoMapParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface on which distances are computed. See 'Specifying input\
            surfaces' section for syntax.
        polar: Retinotopic dataset: polar angle dataset.
        eccentricity: Retinotopic dataset: eccentricity angle dataset.
        prefix: Prefix for output datasets.
        node_debug: Index of node number for which debugging information is\
            output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfRetinoMap",
        "surface": surface,
        "polar": polar,
        "eccentricity": eccentricity,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if node_debug is not None:
        params["node_debug"] = node_debug
    return params


def surf_retino_map_cargs(
    params: SurfRetinoMapParameters,
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
    cargs.append("SurfRetinoMap")
    cargs.append(params.get("surface"))
    cargs.append(params.get("polar"))
    cargs.append(params.get("eccentricity"))
    if params.get("prefix") is not None:
        cargs.extend([
            "--prefix",
            params.get("prefix")
        ])
    if params.get("node_debug") is not None:
        cargs.extend([
            "--node_dbg",
            str(params.get("node_debug"))
        ])
    return cargs


def surf_retino_map_outputs(
    params: SurfRetinoMapParameters,
    execution: Execution,
) -> SurfRetinoMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfRetinoMapOutputs(
        root=execution.output_file("."),
        vfr_output=execution.output_file(params.get("prefix") + "_VFR.nii.gz") if (params.get("prefix") is not None) else None,
        threshold_max_output=execution.output_file(params.get("prefix") + "_threshold_max.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def surf_retino_map_execute(
    params: SurfRetinoMapParameters,
    execution: Execution,
) -> SurfRetinoMapOutputs:
    """
    Tool for retinotopic mapping on cortical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfRetinoMapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surf_retino_map_cargs(params, execution)
    ret = surf_retino_map_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_retino_map(
    surface: str,
    polar: str,
    eccentricity: str,
    prefix: str | None = None,
    node_debug: float | None = None,
    runner: Runner | None = None,
) -> SurfRetinoMapOutputs:
    """
    Tool for retinotopic mapping on cortical surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surface: Surface on which distances are computed. See 'Specifying input\
            surfaces' section for syntax.
        polar: Retinotopic dataset: polar angle dataset.
        eccentricity: Retinotopic dataset: eccentricity angle dataset.
        prefix: Prefix for output datasets.
        node_debug: Index of node number for which debugging information is\
            output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfRetinoMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_RETINO_MAP_METADATA)
    params = surf_retino_map_params(surface=surface, polar=polar, eccentricity=eccentricity, prefix=prefix, node_debug=node_debug)
    return surf_retino_map_execute(params, execution)


__all__ = [
    "SURF_RETINO_MAP_METADATA",
    "SurfRetinoMapOutputs",
    "surf_retino_map",
    "surf_retino_map_params",
]
