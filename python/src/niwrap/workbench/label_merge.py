# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABEL_MERGE_METADATA = Metadata(
    id="23abeff64ad6c7ec293da11e92c329b37b1711f7.boutiques",
    name="label-merge",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
LabelMergeUpToParameters = typing.TypedDict('LabelMergeUpToParameters', {
    "__STYX_TYPE__": typing.Literal["up_to"],
    "last_column": str,
    "opt_reverse": bool,
})
LabelMergeColumnParameters = typing.TypedDict('LabelMergeColumnParameters', {
    "__STYX_TYPE__": typing.Literal["column"],
    "column": str,
    "up_to": typing.NotRequired[LabelMergeUpToParameters | None],
})
LabelMergeLabelParameters = typing.TypedDict('LabelMergeLabelParameters', {
    "__STYX_TYPE__": typing.Literal["label"],
    "label_in": InputPathType,
    "column": typing.NotRequired[list[LabelMergeColumnParameters] | None],
})
LabelMergeParameters = typing.TypedDict('LabelMergeParameters', {
    "__STYX_TYPE__": typing.Literal["label-merge"],
    "label_out": str,
    "label": typing.NotRequired[list[LabelMergeLabelParameters] | None],
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
        "label-merge": label_merge_cargs,
        "label": label_merge_label_cargs,
        "column": label_merge_column_cargs,
        "up_to": label_merge_up_to_cargs,
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
        "label-merge": label_merge_outputs,
    }
    return vt.get(t)


def label_merge_up_to_params(
    last_column: str,
    opt_reverse: bool = False,
) -> LabelMergeUpToParameters:
    """
    Build parameters.
    
    Args:
        last_column: the number or name of the last column to include.
        opt_reverse: use the range in reverse order.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "up_to",
        "last_column": last_column,
        "opt_reverse": opt_reverse,
    }
    return params


def label_merge_up_to_cargs(
    params: LabelMergeUpToParameters,
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
    cargs.append("-up-to")
    cargs.append(params.get("last_column"))
    if params.get("opt_reverse"):
        cargs.append("-reverse")
    return cargs


def label_merge_column_params(
    column: str,
    up_to: LabelMergeUpToParameters | None = None,
) -> LabelMergeColumnParameters:
    """
    Build parameters.
    
    Args:
        column: the column number or name.
        up_to: use an inclusive range of columns.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "column",
        "column": column,
    }
    if up_to is not None:
        params["up_to"] = up_to
    return params


def label_merge_column_cargs(
    params: LabelMergeColumnParameters,
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
    cargs.append("-column")
    cargs.append(params.get("column"))
    if params.get("up_to") is not None:
        cargs.extend(dyn_cargs(params.get("up_to")["__STYXTYPE__"])(params.get("up_to"), execution))
    return cargs


def label_merge_label_params(
    label_in: InputPathType,
    column: list[LabelMergeColumnParameters] | None = None,
) -> LabelMergeLabelParameters:
    """
    Build parameters.
    
    Args:
        label_in: a label file to use columns from.
        column: select a single column to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label",
        "label_in": label_in,
    }
    if column is not None:
        params["column"] = column
    return params


def label_merge_label_cargs(
    params: LabelMergeLabelParameters,
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
    cargs.append("-label")
    cargs.append(execution.input_file(params.get("label_in")))
    if params.get("column") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("column")] for a in c])
    return cargs


class LabelMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label"""


def label_merge_params(
    label_out: str,
    label: list[LabelMergeLabelParameters] | None = None,
) -> LabelMergeParameters:
    """
    Build parameters.
    
    Args:
        label_out: the output label.
        label: specify an input label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-merge",
        "label_out": label_out,
    }
    if label is not None:
        params["label"] = label
    return params


def label_merge_cargs(
    params: LabelMergeParameters,
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
    cargs.append("-label-merge")
    cargs.append(params.get("label_out"))
    if params.get("label") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("label")] for a in c])
    return cargs


def label_merge_outputs(
    params: LabelMergeParameters,
    execution: Execution,
) -> LabelMergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelMergeOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
    )
    return ret


def label_merge_execute(
    params: LabelMergeParameters,
    execution: Execution,
) -> LabelMergeOutputs:
    """
    Merge label files into a new file.
    
    Takes one or more label files and constructs a new label file by
    concatenating columns from them. The input files must have the same number
    of vertices and the same structure.
    
    Example: wb_command -label-merge out.label.gii -label first.label.gii
    -column 1 -label second.label.gii
    
    This example would take the first column from first.label.gii and all
    subvolumes from second.label.gii, and write these to out.label.gii.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelMergeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = label_merge_cargs(params, execution)
    ret = label_merge_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_merge(
    label_out: str,
    label: list[LabelMergeLabelParameters] | None = None,
    runner: Runner | None = None,
) -> LabelMergeOutputs:
    """
    Merge label files into a new file.
    
    Takes one or more label files and constructs a new label file by
    concatenating columns from them. The input files must have the same number
    of vertices and the same structure.
    
    Example: wb_command -label-merge out.label.gii -label first.label.gii
    -column 1 -label second.label.gii
    
    This example would take the first column from first.label.gii and all
    subvolumes from second.label.gii, and write these to out.label.gii.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_out: the output label.
        label: specify an input label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MERGE_METADATA)
    params = label_merge_params(label_out=label_out, label=label)
    return label_merge_execute(params, execution)


__all__ = [
    "LABEL_MERGE_METADATA",
    "LabelMergeOutputs",
    "label_merge",
    "label_merge_column_params",
    "label_merge_label_params",
    "label_merge_params",
    "label_merge_up_to_params",
]
