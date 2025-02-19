# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FDR_METADATA = Metadata(
    id="c6df1fc3c682e8d10bc8100c6ca38bb1d5015a85.boutiques",
    name="mri_fdr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFdrParameters = typing.TypedDict('MriFdrParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fdr"],
    "input_files": list[str],
    "fdr_value": float,
    "default_frame": typing.NotRequired[int | None],
    "positive_only": bool,
    "negative_only": bool,
    "all_voxels": bool,
    "raw_p_values": bool,
    "threshold_file": typing.NotRequired[str | None],
    "debug": bool,
    "check_options": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mri_fdr": mri_fdr_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "mri_fdr": mri_fdr_outputs,
    }.get(t)


class MriFdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_corrected: OutputPathType
    """Output after applying FDR correction"""
    output_threshold: OutputPathType
    """Threshold written to text file"""


def mri_fdr_params(
    input_files: list[str],
    fdr_value: float,
    default_frame: int | None = None,
    positive_only: bool = False,
    negative_only: bool = False,
    all_voxels: bool = False,
    raw_p_values: bool = False,
    threshold_file: str | None = None,
    debug: bool = False,
    check_options: bool = False,
) -> MriFdrParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input source volume or surface overlay. Specify mask,\
            output, and frame as needed.
        fdr_value: FDR value between 0 and 1, typically .05.
        default_frame: Use input frame when not specifying frame in --i.
        positive_only: Only consider positive voxels.
        negative_only: Only consider negative voxels.
        all_voxels: Consider all voxels regardless of sign (default).
        raw_p_values: Input is raw p-values, not -log10(p).
        threshold_file: Write threshold to text file.
        debug: Turn on debugging.
        check_options: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fdr",
        "input_files": input_files,
        "fdr_value": fdr_value,
        "positive_only": positive_only,
        "negative_only": negative_only,
        "all_voxels": all_voxels,
        "raw_p_values": raw_p_values,
        "debug": debug,
        "check_options": check_options,
    }
    if default_frame is not None:
        params["default_frame"] = default_frame
    if threshold_file is not None:
        params["threshold_file"] = threshold_file
    return params


def mri_fdr_cargs(
    params: MriFdrParameters,
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
    cargs.append("mri_fdr")
    cargs.extend([
        "--i",
        *params.get("input_files")
    ])
    cargs.extend([
        "--fdr",
        str(params.get("fdr_value"))
    ])
    if params.get("default_frame") is not None:
        cargs.extend([
            "--f",
            str(params.get("default_frame"))
        ])
    if params.get("positive_only"):
        cargs.append("--pos")
    if params.get("negative_only"):
        cargs.append("--neg")
    if params.get("all_voxels"):
        cargs.append("--abs")
    if params.get("raw_p_values"):
        cargs.append("--no-log10p")
    if params.get("threshold_file") is not None:
        cargs.extend([
            "--thfile",
            params.get("threshold_file")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("check_options"):
        cargs.append("--checkopts")
    return cargs


def mri_fdr_outputs(
    params: MriFdrParameters,
    execution: Execution,
) -> MriFdrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFdrOutputs(
        root=execution.output_file("."),
        output_corrected=execution.output_file("<output>.mgh"),
        output_threshold=execution.output_file("<output>_threshold.txt"),
    )
    return ret


def mri_fdr_execute(
    params: MriFdrParameters,
    execution: Execution,
) -> MriFdrOutputs:
    """
    A program that performs False Discovery Rate correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFdrOutputs`).
    """
    params = execution.params(params)
    cargs = mri_fdr_cargs(params, execution)
    ret = mri_fdr_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fdr(
    input_files: list[str],
    fdr_value: float,
    default_frame: int | None = None,
    positive_only: bool = False,
    negative_only: bool = False,
    all_voxels: bool = False,
    raw_p_values: bool = False,
    threshold_file: str | None = None,
    debug: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> MriFdrOutputs:
    """
    A program that performs False Discovery Rate correction.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input source volume or surface overlay. Specify mask,\
            output, and frame as needed.
        fdr_value: FDR value between 0 and 1, typically .05.
        default_frame: Use input frame when not specifying frame in --i.
        positive_only: Only consider positive voxels.
        negative_only: Only consider negative voxels.
        all_voxels: Consider all voxels regardless of sign (default).
        raw_p_values: Input is raw p-values, not -log10(p).
        threshold_file: Write threshold to text file.
        debug: Turn on debugging.
        check_options: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FDR_METADATA)
    params = mri_fdr_params(input_files=input_files, fdr_value=fdr_value, default_frame=default_frame, positive_only=positive_only, negative_only=negative_only, all_voxels=all_voxels, raw_p_values=raw_p_values, threshold_file=threshold_file, debug=debug, check_options=check_options)
    return mri_fdr_execute(params, execution)


__all__ = [
    "MRI_FDR_METADATA",
    "MriFdrOutputs",
    "MriFdrParameters",
    "mri_fdr",
    "mri_fdr_params",
]
