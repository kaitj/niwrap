# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_ADD_NEW_TP_METADATA = Metadata(
    id="c092850ac196635799818218f41e6c048de46b98.boutiques",
    name="mri_add_new_tp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriAddNewTpParameters = typing.TypedDict('MriAddNewTpParameters', {
    "__STYX_TYPE__": typing.Literal["mri_add_new_tp"],
    "base_id": str,
    "newtp_id": str,
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
        "mri_add_new_tp": mri_add_new_tp_cargs,
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


def mri_add_new_tp_params(
    base_id: str,
    newtp_id: str,
) -> MriAddNewTpParameters:
    """
    Build parameters.
    
    Args:
        base_id: The ID of the base template.
        newtp_id: The ID of the new time point to be added.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_add_new_tp",
        "base_id": base_id,
        "newtp_id": newtp_id,
    }
    return params


def mri_add_new_tp_cargs(
    params: MriAddNewTpParameters,
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
    cargs.append("mri_add_new_tp")
    cargs.append(params.get("base_id"))
    cargs.append(params.get("newtp_id"))
    return cargs


def mri_add_new_tp_outputs(
    params: MriAddNewTpParameters,
    execution: Execution,
) -> MriAddNewTpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAddNewTpOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_add_new_tp_execute(
    params: MriAddNewTpParameters,
    execution: Execution,
) -> MriAddNewTpOutputs:
    """
    Adds a new time point to the base/template without re-creating the base. Only
    the new time point needs to be run longitudinally.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAddNewTpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_add_new_tp_cargs(params, execution)
    ret = mri_add_new_tp_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_add_new_tp(
    base_id: str,
    newtp_id: str,
    runner: Runner | None = None,
) -> MriAddNewTpOutputs:
    """
    Adds a new time point to the base/template without re-creating the base. Only
    the new time point needs to be run longitudinally.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        base_id: The ID of the base template.
        newtp_id: The ID of the new time point to be added.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAddNewTpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ADD_NEW_TP_METADATA)
    params = mri_add_new_tp_params(base_id=base_id, newtp_id=newtp_id)
    return mri_add_new_tp_execute(params, execution)


__all__ = [
    "MRI_ADD_NEW_TP_METADATA",
    "mri_add_new_tp",
    "mri_add_new_tp_params",
]
