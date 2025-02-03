# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA = Metadata(
    id="255cbc9bcd0a4cdb77830871dfed14d27befa862.boutiques",
    name="SegmentSubfieldsT1Longitudinal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentSubfieldsT1LongitudinalParameters = typing.TypedDict('SegmentSubfieldsT1LongitudinalParameters', {
    "__STYX_TYPE__": typing.Literal["SegmentSubfieldsT1Longitudinal"],
    "subject_id": str,
    "input_image": InputPathType,
    "output_dir": str,
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
        "SegmentSubfieldsT1Longitudinal": segment_subfields_t1_longitudinal_cargs,
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
        "SegmentSubfieldsT1Longitudinal": segment_subfields_t1_longitudinal_outputs,
    }
    return vt.get(t)


class SegmentSubfieldsT1LongitudinalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subfields_t1_longitudinal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Output file containing the segmented subfields"""


def segment_subfields_t1_longitudinal_params(
    subject_id: str,
    input_image: InputPathType,
    output_dir: str,
) -> SegmentSubfieldsT1LongitudinalParameters:
    """
    Build parameters.
    
    Args:
        subject_id: Subject ID for the longitudinal analysis.
        input_image: Input T1-weighted image.
        output_dir: Directory to save the output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SegmentSubfieldsT1Longitudinal",
        "subject_id": subject_id,
        "input_image": input_image,
        "output_dir": output_dir,
    }
    return params


def segment_subfields_t1_longitudinal_cargs(
    params: SegmentSubfieldsT1LongitudinalParameters,
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
    cargs.append("SegmentSubfieldsT1Longitudinal")
    cargs.append(params.get("subject_id"))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_dir"))
    return cargs


def segment_subfields_t1_longitudinal_outputs(
    params: SegmentSubfieldsT1LongitudinalParameters,
    execution: Execution,
) -> SegmentSubfieldsT1LongitudinalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentSubfieldsT1LongitudinalOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(params.get("output_dir") + "/subfields_segmentation.nii.gz"),
    )
    return ret


def segment_subfields_t1_longitudinal_execute(
    params: SegmentSubfieldsT1LongitudinalParameters,
    execution: Execution,
) -> SegmentSubfieldsT1LongitudinalOutputs:
    """
    FreeSurfer tool for segmenting subfields in longitudinal T1-weighted images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentSubfieldsT1LongitudinalOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_subfields_t1_longitudinal_cargs(params, execution)
    ret = segment_subfields_t1_longitudinal_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_subfields_t1_longitudinal(
    subject_id: str,
    input_image: InputPathType,
    output_dir: str,
    runner: Runner | None = None,
) -> SegmentSubfieldsT1LongitudinalOutputs:
    """
    FreeSurfer tool for segmenting subfields in longitudinal T1-weighted images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID for the longitudinal analysis.
        input_image: Input T1-weighted image.
        output_dir: Directory to save the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubfieldsT1LongitudinalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA)
    params = segment_subfields_t1_longitudinal_params(subject_id=subject_id, input_image=input_image, output_dir=output_dir)
    return segment_subfields_t1_longitudinal_execute(params, execution)


__all__ = [
    "SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA",
    "SegmentSubfieldsT1LongitudinalOutputs",
    "segment_subfields_t1_longitudinal",
    "segment_subfields_t1_longitudinal_params",
]
