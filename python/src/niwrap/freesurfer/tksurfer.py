# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TKSURFER_METADATA = Metadata(
    id="603cb4c673862d6704782330c4df67ab125e67dd.boutiques",
    name="tksurfer",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TksurferParameters = typing.TypedDict('TksurferParameters', {
    "__STYX_TYPE__": typing.Literal["tksurfer"],
    "subject_id": str,
    "hemisphere": str,
    "surface_name": str,
    "options": typing.NotRequired[str | None],
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
        "tksurfer": tksurfer_cargs,
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


def tksurfer_params(
    subject_id: str,
    hemisphere: str,
    surface_name: str,
    options: str | None = None,
) -> TksurferParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject identifier.
        hemisphere: Cortical hemisphere (e.g., lh or rh).
        surface_name: Surface name (e.g., inflated, sphere, white).
        options: Optional flags and parameters.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tksurfer",
        "subject_id": subject_id,
        "hemisphere": hemisphere,
        "surface_name": surface_name,
    }
    if options is not None:
        params["options"] = options
    return params


def tksurfer_cargs(
    params: TksurferParameters,
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
    cargs.append("tksurfer")
    cargs.append(params.get("subject_id"))
    cargs.append(params.get("hemisphere"))
    cargs.append(params.get("surface_name"))
    if params.get("options") is not None:
        cargs.append(params.get("options"))
    return cargs


def tksurfer_outputs(
    params: TksurferParameters,
    execution: Execution,
) -> TksurferOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TksurferOutputs(
        root=execution.output_file("."),
    )
    return ret


def tksurfer_execute(
    params: TksurferParameters,
    execution: Execution,
) -> TksurferOutputs:
    """
    3D visualization tool for cortical surface models (part of FreeSurfer).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TksurferOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tksurfer_cargs(params, execution)
    ret = tksurfer_outputs(params, execution)
    execution.run(cargs)
    return ret


def tksurfer(
    subject_id: str,
    hemisphere: str,
    surface_name: str,
    options: str | None = None,
    runner: Runner | None = None,
) -> TksurferOutputs:
    """
    3D visualization tool for cortical surface models (part of FreeSurfer).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject identifier.
        hemisphere: Cortical hemisphere (e.g., lh or rh).
        surface_name: Surface name (e.g., inflated, sphere, white).
        options: Optional flags and parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TksurferOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKSURFER_METADATA)
    params = tksurfer_params(subject_id=subject_id, hemisphere=hemisphere, surface_name=surface_name, options=options)
    return tksurfer_execute(params, execution)


__all__ = [
    "TKSURFER_METADATA",
    "tksurfer",
    "tksurfer_params",
]
