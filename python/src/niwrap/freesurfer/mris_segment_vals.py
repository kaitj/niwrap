# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SEGMENT_VALS_METADATA = Metadata(
    id="8fb7152be4e370cbcf1d314e781abb1f188e845e.boutiques",
    name="mris_segment_vals",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSegmentValsParameters = typing.TypedDict('MrisSegmentValsParameters', {
    "__STYX_TYPE__": typing.Literal["mris_segment_vals"],
    "input_surface": InputPathType,
    "input_curv_file": InputPathType,
    "output_curv_file": str,
    "threshold": typing.NotRequired[float | None],
    "area_thresh": typing.NotRequired[float | None],
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
        "mris_segment_vals": mris_segment_vals_cargs,
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
        "mris_segment_vals": mris_segment_vals_outputs,
    }
    return vt.get(t)


class MrisSegmentValsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_segment_vals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_curv: OutputPathType
    """Output w/curv file after segmentation"""


def mris_segment_vals_params(
    input_surface: InputPathType,
    input_curv_file: InputPathType,
    output_curv_file: str,
    threshold: float | None = None,
    area_thresh: float | None = None,
) -> MrisSegmentValsParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        input_curv_file: Input w/curv file.
        output_curv_file: Output w/curv file.
        threshold: Threshold for segmentation (default is 0).
        area_thresh: Ignore segments smaller than <area thresh> mm (default 0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_segment_vals",
        "input_surface": input_surface,
        "input_curv_file": input_curv_file,
        "output_curv_file": output_curv_file,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if area_thresh is not None:
        params["area_thresh"] = area_thresh
    return params


def mris_segment_vals_cargs(
    params: MrisSegmentValsParameters,
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
    cargs.append("mris_segment_vals")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("input_curv_file")))
    cargs.append(params.get("output_curv_file"))
    if params.get("threshold") is not None:
        cargs.extend([
            "-T",
            str(params.get("threshold"))
        ])
    if params.get("area_thresh") is not None:
        cargs.extend([
            "-A",
            str(params.get("area_thresh"))
        ])
    return cargs


def mris_segment_vals_outputs(
    params: MrisSegmentValsParameters,
    execution: Execution,
) -> MrisSegmentValsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSegmentValsOutputs(
        root=execution.output_file("."),
        output_curv=execution.output_file(params.get("output_curv_file")),
    )
    return ret


def mris_segment_vals_execute(
    params: MrisSegmentValsParameters,
    execution: Execution,
) -> MrisSegmentValsOutputs:
    """
    This program segments an input val file into connected components.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSegmentValsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_segment_vals_cargs(params, execution)
    ret = mris_segment_vals_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_segment_vals(
    input_surface: InputPathType,
    input_curv_file: InputPathType,
    output_curv_file: str,
    threshold: float | None = None,
    area_thresh: float | None = None,
    runner: Runner | None = None,
) -> MrisSegmentValsOutputs:
    """
    This program segments an input val file into connected components.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        input_curv_file: Input w/curv file.
        output_curv_file: Output w/curv file.
        threshold: Threshold for segmentation (default is 0).
        area_thresh: Ignore segments smaller than <area thresh> mm (default 0).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSegmentValsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SEGMENT_VALS_METADATA)
    params = mris_segment_vals_params(input_surface=input_surface, input_curv_file=input_curv_file, output_curv_file=output_curv_file, threshold=threshold, area_thresh=area_thresh)
    return mris_segment_vals_execute(params, execution)


__all__ = [
    "MRIS_SEGMENT_VALS_METADATA",
    "MrisSegmentValsOutputs",
    "mris_segment_vals",
    "mris_segment_vals_params",
]
