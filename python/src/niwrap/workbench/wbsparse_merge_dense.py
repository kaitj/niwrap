# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

WBSPARSE_MERGE_DENSE_METADATA = Metadata(
    id="af1749f9ad1bdf4a9e5257d7439ccb891c9cff12.boutiques",
    name="wbsparse-merge-dense",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
WbsparseMergeDenseWbsparseParameters = typing.TypedDict('WbsparseMergeDenseWbsparseParameters', {
    "__STYX_TYPE__": typing.Literal["wbsparse"],
    "wbsparse_in": str,
})
WbsparseMergeDenseParameters = typing.TypedDict('WbsparseMergeDenseParameters', {
    "__STYX_TYPE__": typing.Literal["wbsparse-merge-dense"],
    "direction": str,
    "wbsparse_out": str,
    "wbsparse": typing.NotRequired[list[WbsparseMergeDenseWbsparseParameters] | None],
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
        "wbsparse-merge-dense": wbsparse_merge_dense_cargs,
        "wbsparse": wbsparse_merge_dense_wbsparse_cargs,
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


def wbsparse_merge_dense_wbsparse_params(
    wbsparse_in: str,
) -> WbsparseMergeDenseWbsparseParameters:
    """
    Build parameters.
    
    Args:
        wbsparse_in: a wbsparse file to merge.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wbsparse",
        "wbsparse_in": wbsparse_in,
    }
    return params


def wbsparse_merge_dense_wbsparse_cargs(
    params: WbsparseMergeDenseWbsparseParameters,
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
    cargs.append("-wbsparse")
    cargs.append(params.get("wbsparse_in"))
    return cargs


def wbsparse_merge_dense_params(
    direction: str,
    wbsparse_out: str,
    wbsparse: list[WbsparseMergeDenseWbsparseParameters] | None = None,
) -> WbsparseMergeDenseParameters:
    """
    Build parameters.
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN.
        wbsparse_out: output - the output wbsparse file.
        wbsparse: specify an input wbsparse file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wbsparse-merge-dense",
        "direction": direction,
        "wbsparse_out": wbsparse_out,
    }
    if wbsparse is not None:
        params["wbsparse"] = wbsparse
    return params


def wbsparse_merge_dense_cargs(
    params: WbsparseMergeDenseParameters,
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
    cargs.append("-wbsparse-merge-dense")
    cargs.append(params.get("direction"))
    cargs.append(params.get("wbsparse_out"))
    if params.get("wbsparse") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("wbsparse")] for a in c])
    return cargs


def wbsparse_merge_dense_outputs(
    params: WbsparseMergeDenseParameters,
    execution: Execution,
) -> WbsparseMergeDenseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WbsparseMergeDenseOutputs(
        root=execution.output_file("."),
    )
    return ret


def wbsparse_merge_dense_execute(
    params: WbsparseMergeDenseParameters,
    execution: Execution,
) -> WbsparseMergeDenseOutputs:
    """
    Merge wbsparse files along dense dimension.
    
    The input wbsparse files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WbsparseMergeDenseOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = wbsparse_merge_dense_cargs(params, execution)
    ret = wbsparse_merge_dense_outputs(params, execution)
    execution.run(cargs)
    return ret


def wbsparse_merge_dense(
    direction: str,
    wbsparse_out: str,
    wbsparse: list[WbsparseMergeDenseWbsparseParameters] | None = None,
    runner: Runner | None = None,
) -> WbsparseMergeDenseOutputs:
    """
    Merge wbsparse files along dense dimension.
    
    The input wbsparse files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN.
        wbsparse_out: output - the output wbsparse file.
        wbsparse: specify an input wbsparse file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WbsparseMergeDenseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WBSPARSE_MERGE_DENSE_METADATA)
    params = wbsparse_merge_dense_params(direction=direction, wbsparse_out=wbsparse_out, wbsparse=wbsparse)
    return wbsparse_merge_dense_execute(params, execution)


__all__ = [
    "WBSPARSE_MERGE_DENSE_METADATA",
    "wbsparse_merge_dense",
    "wbsparse_merge_dense_params",
    "wbsparse_merge_dense_wbsparse_params",
]
