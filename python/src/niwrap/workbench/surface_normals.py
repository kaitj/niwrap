# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_NORMALS_METADATA = Metadata(
    id="bf741b89964614d5dda2065678e1ec762984a361.boutiques",
    name="surface-normals",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceNormalsParameters = typing.TypedDict('SurfaceNormalsParameters', {
    "__STYX_TYPE__": typing.Literal["surface-normals"],
    "surface": InputPathType,
    "metric_out": str,
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
        "surface-normals": surface_normals_cargs,
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
        "surface-normals": surface_normals_outputs,
    }
    return vt.get(t)


class SurfaceNormalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_normals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the normal vectors"""


def surface_normals_params(
    surface: InputPathType,
    metric_out: str,
) -> SurfaceNormalsParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to output the normals of.
        metric_out: the normal vectors.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-normals",
        "surface": surface,
        "metric_out": metric_out,
    }
    return params


def surface_normals_cargs(
    params: SurfaceNormalsParameters,
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
    cargs.append("wb_command")
    cargs.append("-surface-normals")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(params.get("metric_out"))
    return cargs


def surface_normals_outputs(
    params: SurfaceNormalsParameters,
    execution: Execution,
) -> SurfaceNormalsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceNormalsOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def surface_normals_execute(
    params: SurfaceNormalsParameters,
    execution: Execution,
) -> SurfaceNormalsOutputs:
    """
    Output vertex normals as metric file.
    
    Computes the normal vectors of the surface file, and outputs them as a 3
    column metric file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceNormalsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_normals_cargs(params, execution)
    ret = surface_normals_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_normals(
    surface: InputPathType,
    metric_out: str,
    runner: Runner | None = None,
) -> SurfaceNormalsOutputs:
    """
    Output vertex normals as metric file.
    
    Computes the normal vectors of the surface file, and outputs them as a 3
    column metric file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to output the normals of.
        metric_out: the normal vectors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceNormalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_NORMALS_METADATA)
    params = surface_normals_params(surface=surface, metric_out=metric_out)
    return surface_normals_execute(params, execution)


__all__ = [
    "SURFACE_NORMALS_METADATA",
    "SurfaceNormalsOutputs",
    "surface_normals",
    "surface_normals_params",
]
