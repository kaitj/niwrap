# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_REORDER_METADATA = Metadata(
    id="c67346c8c77f6b5bb2cc3860f812ce9450fe272f.boutiques",
    name="cifti-reorder",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiReorderParameters = typing.TypedDict('CiftiReorderParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-reorder"],
    "cifti_in": InputPathType,
    "direction": str,
    "reorder_list": str,
    "cifti_out": str,
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
        "cifti-reorder": cifti_reorder_cargs,
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
        "cifti-reorder": cifti_reorder_outputs,
    }
    return vt.get(t)


class CiftiReorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_reorder(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the reordered cifti file"""


def cifti_reorder_params(
    cifti_in: InputPathType,
    direction: str,
    reorder_list: str,
    cifti_out: str,
) -> CiftiReorderParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: input cifti file.
        direction: which dimension to reorder along, ROW or COLUMN.
        reorder_list: a text file containing the desired order transformation.
        cifti_out: the reordered cifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-reorder",
        "cifti_in": cifti_in,
        "direction": direction,
        "reorder_list": reorder_list,
        "cifti_out": cifti_out,
    }
    return params


def cifti_reorder_cargs(
    params: CiftiReorderParameters,
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
    cargs.append("-cifti-reorder")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("direction"))
    cargs.append(params.get("reorder_list"))
    cargs.append(params.get("cifti_out"))
    return cargs


def cifti_reorder_outputs(
    params: CiftiReorderParameters,
    execution: Execution,
) -> CiftiReorderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiReorderOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_reorder_execute(
    params: CiftiReorderParameters,
    execution: Execution,
) -> CiftiReorderOutputs:
    """
    Reorder the parcels or scalar/label maps in a cifti file.
    
    The mapping along the specified direction must be parcels, scalars, or
    labels. For pscalar or ptseries, use COLUMN to reorder the parcels. For
    dlabel, use ROW. The <reorder-list> file must contain 1-based indices
    separated by whitespace (spaces, newlines, tabs, etc), with as many indices
    as <cifti-in> has along the specified dimension. These indices specify which
    current index should end up in that position, for instance, if the current
    order is 'A B C D', and the desired order is 'D A B C', the text file should
    contain '4 1 2 3'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiReorderOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_reorder_cargs(params, execution)
    ret = cifti_reorder_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_reorder(
    cifti_in: InputPathType,
    direction: str,
    reorder_list: str,
    cifti_out: str,
    runner: Runner | None = None,
) -> CiftiReorderOutputs:
    """
    Reorder the parcels or scalar/label maps in a cifti file.
    
    The mapping along the specified direction must be parcels, scalars, or
    labels. For pscalar or ptseries, use COLUMN to reorder the parcels. For
    dlabel, use ROW. The <reorder-list> file must contain 1-based indices
    separated by whitespace (spaces, newlines, tabs, etc), with as many indices
    as <cifti-in> has along the specified dimension. These indices specify which
    current index should end up in that position, for instance, if the current
    order is 'A B C D', and the desired order is 'D A B C', the text file should
    contain '4 1 2 3'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: input cifti file.
        direction: which dimension to reorder along, ROW or COLUMN.
        reorder_list: a text file containing the desired order transformation.
        cifti_out: the reordered cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiReorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_REORDER_METADATA)
    params = cifti_reorder_params(cifti_in=cifti_in, direction=direction, reorder_list=reorder_list, cifti_out=cifti_out)
    return cifti_reorder_execute(params, execution)


__all__ = [
    "CIFTI_REORDER_METADATA",
    "CiftiReorderOutputs",
    "cifti_reorder",
    "cifti_reorder_params",
]
