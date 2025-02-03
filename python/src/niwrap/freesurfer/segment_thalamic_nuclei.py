# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_THALAMIC_NUCLEI_METADATA = Metadata(
    id="6d4f3bd43ea02912a67101dc7d2bc3abdee4ebd2.boutiques",
    name="SegmentThalamicNuclei",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SegmentThalamicNucleiParameters = typing.TypedDict('SegmentThalamicNucleiParameters', {
    "__STYX_TYPE__": typing.Literal["SegmentThalamicNuclei"],
    "t1_image": InputPathType,
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
        "SegmentThalamicNuclei": segment_thalamic_nuclei_cargs,
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
        "SegmentThalamicNuclei": segment_thalamic_nuclei_outputs,
    }
    return vt.get(t)


class SegmentThalamicNucleiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_thalamic_nuclei(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    seg_output: OutputPathType
    """The output segmentation file of thalamic nuclei."""


def segment_thalamic_nuclei_params(
    t1_image: InputPathType,
    output_dir: str,
) -> SegmentThalamicNucleiParameters:
    """
    Build parameters.
    
    Args:
        t1_image: The T1-weighted image to process.
        output_dir: Directory to store segmentation results.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SegmentThalamicNuclei",
        "t1_image": t1_image,
        "output_dir": output_dir,
    }
    return params


def segment_thalamic_nuclei_cargs(
    params: SegmentThalamicNucleiParameters,
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
    cargs.append("SegmentThalamicNuclei")
    cargs.append(execution.input_file(params.get("t1_image")))
    cargs.append(params.get("output_dir"))
    return cargs


def segment_thalamic_nuclei_outputs(
    params: SegmentThalamicNucleiParameters,
    execution: Execution,
) -> SegmentThalamicNucleiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentThalamicNucleiOutputs(
        root=execution.output_file("."),
        seg_output=execution.output_file(params.get("output_dir") + "/thalamic_nuclei_seg.nii.gz"),
    )
    return ret


def segment_thalamic_nuclei_execute(
    params: SegmentThalamicNucleiParameters,
    execution: Execution,
) -> SegmentThalamicNucleiOutputs:
    """
    A tool for segmenting thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentThalamicNucleiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = segment_thalamic_nuclei_cargs(params, execution)
    ret = segment_thalamic_nuclei_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_thalamic_nuclei(
    t1_image: InputPathType,
    output_dir: str,
    runner: Runner | None = None,
) -> SegmentThalamicNucleiOutputs:
    """
    A tool for segmenting thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_image: The T1-weighted image to process.
        output_dir: Directory to store segmentation results.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentThalamicNucleiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_THALAMIC_NUCLEI_METADATA)
    params = segment_thalamic_nuclei_params(t1_image=t1_image, output_dir=output_dir)
    return segment_thalamic_nuclei_execute(params, execution)


__all__ = [
    "SEGMENT_THALAMIC_NUCLEI_METADATA",
    "SegmentThalamicNucleiOutputs",
    "segment_thalamic_nuclei",
    "segment_thalamic_nuclei_params",
]
