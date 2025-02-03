# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MERGELABELS_METADATA = Metadata(
    id="6f1119002868794fb350ad4069f13562cf64aaa1.boutiques",
    name="mri_mergelabels",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriMergelabelsParameters = typing.TypedDict('MriMergelabelsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_mergelabels"],
    "input_labels": list[InputPathType],
    "output_label": str,
    "input_directory": typing.NotRequired[str | None],
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
        "mri_mergelabels": mri_mergelabels_cargs,
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
        "mri_mergelabels": mri_mergelabels_outputs,
    }
    return vt.get(t)


class MriMergelabelsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mergelabels(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    merged_label_file: OutputPathType
    """Merged label output file"""


def mri_mergelabels_params(
    input_labels: list[InputPathType],
    output_label: str,
    input_directory: str | None = None,
) -> MriMergelabelsParameters:
    """
    Build parameters.
    
    Args:
        input_labels: Input label files to be merged.
        output_label: Output file for the merged label.
        input_directory: Directory containing label files to be merged.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_mergelabels",
        "input_labels": input_labels,
        "output_label": output_label,
    }
    if input_directory is not None:
        params["input_directory"] = input_directory
    return params


def mri_mergelabels_cargs(
    params: MriMergelabelsParameters,
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
    cargs.append("mri_mergelabels")
    cargs.extend([
        "-i",
        *[execution.input_file(f) for f in params.get("input_labels")]
    ])
    cargs.extend([
        "-o",
        params.get("output_label")
    ])
    if params.get("input_directory") is not None:
        cargs.extend([
            "-d",
            params.get("input_directory")
        ])
    return cargs


def mri_mergelabels_outputs(
    params: MriMergelabelsParameters,
    execution: Execution,
) -> MriMergelabelsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMergelabelsOutputs(
        root=execution.output_file("."),
        merged_label_file=execution.output_file(params.get("output_label")),
    )
    return ret


def mri_mergelabels_execute(
    params: MriMergelabelsParameters,
    execution: Execution,
) -> MriMergelabelsOutputs:
    """
    A tool to merge two or more label files by concatenating them together.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMergelabelsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_mergelabels_cargs(params, execution)
    ret = mri_mergelabels_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_mergelabels(
    input_labels: list[InputPathType],
    output_label: str,
    input_directory: str | None = None,
    runner: Runner | None = None,
) -> MriMergelabelsOutputs:
    """
    A tool to merge two or more label files by concatenating them together.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_labels: Input label files to be merged.
        output_label: Output file for the merged label.
        input_directory: Directory containing label files to be merged.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMergelabelsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MERGELABELS_METADATA)
    params = mri_mergelabels_params(input_labels=input_labels, output_label=output_label, input_directory=input_directory)
    return mri_mergelabels_execute(params, execution)


__all__ = [
    "MRI_MERGELABELS_METADATA",
    "MriMergelabelsOutputs",
    "mri_mergelabels",
    "mri_mergelabels_params",
]
