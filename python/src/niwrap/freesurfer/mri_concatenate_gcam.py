# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CONCATENATE_GCAM_METADATA = Metadata(
    id="f2136516d8c43c1484d6b8f54f1f6627fae4ebe7.boutiques",
    name="mri_concatenate_gcam",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriConcatenateGcamParameters = typing.TypedDict('MriConcatenateGcamParameters', {
    "__STYX_TYPE__": typing.Literal["mri_concatenate_gcam"],
    "inputs": list[InputPathType],
    "output": str,
    "source_image": typing.NotRequired[InputPathType | None],
    "target_image": typing.NotRequired[InputPathType | None],
    "reduce": bool,
    "invert": bool,
    "downsample": bool,
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
        "mri_concatenate_gcam": mri_concatenate_gcam_cargs,
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
        "mri_concatenate_gcam": mri_concatenate_gcam_outputs,
    }
    return vt.get(t)


class MriConcatenateGcamOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concatenate_gcam(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Composite LTA or M3Z transform, depending on input."""


def mri_concatenate_gcam_params(
    inputs: list[InputPathType],
    output: str,
    source_image: InputPathType | None = None,
    target_image: InputPathType | None = None,
    reduce: bool = False,
    invert: bool = False,
    downsample: bool = False,
) -> MriConcatenateGcamParameters:
    """
    Build parameters.
    
    Args:
        inputs: Combination of input LTAs and M3Zs.
        output: Concatenated output transform, saved as an LTA or M3Z depending\
            on the input transforms.
        source_image: Change source image geometry of output M3Z, useful for\
            GCAM inversion if the path of the original source volume changed.
        target_image: Change destination image geometry of output M3Z.
        reduce: Reduce output LTA to single LT.
        invert: Invert the output transform.
        downsample: Downsample output M3Z to spacing of 2; by default, the\
            output spacing is that of the rightmost input M3Z.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_concatenate_gcam",
        "inputs": inputs,
        "output": output,
        "reduce": reduce,
        "invert": invert,
        "downsample": downsample,
    }
    if source_image is not None:
        params["source_image"] = source_image
    if target_image is not None:
        params["target_image"] = target_image
    return params


def mri_concatenate_gcam_cargs(
    params: MriConcatenateGcamParameters,
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
    cargs.append("mri_concatenate_gcam")
    cargs.extend([execution.input_file(f) for f in params.get("inputs")])
    cargs.append(params.get("output"))
    if params.get("source_image") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("source_image"))
        ])
    if params.get("target_image") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("target_image"))
        ])
    if params.get("reduce"):
        cargs.append("-r")
    if params.get("invert"):
        cargs.append("-i")
    if params.get("downsample"):
        cargs.append("-d")
    return cargs


def mri_concatenate_gcam_outputs(
    params: MriConcatenateGcamParameters,
    execution: Execution,
) -> MriConcatenateGcamOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriConcatenateGcamOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output")),
    )
    return ret


def mri_concatenate_gcam_execute(
    params: MriConcatenateGcamParameters,
    execution: Execution,
) -> MriConcatenateGcamOutputs:
    """
    Concatenate a combination of input LTAs (linear transform array) and GCAMs
    (Gaussian classifier atlas, M3Z).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateGcamOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_concatenate_gcam_cargs(params, execution)
    ret = mri_concatenate_gcam_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_concatenate_gcam(
    inputs: list[InputPathType],
    output: str,
    source_image: InputPathType | None = None,
    target_image: InputPathType | None = None,
    reduce: bool = False,
    invert: bool = False,
    downsample: bool = False,
    runner: Runner | None = None,
) -> MriConcatenateGcamOutputs:
    """
    Concatenate a combination of input LTAs (linear transform array) and GCAMs
    (Gaussian classifier atlas, M3Z).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inputs: Combination of input LTAs and M3Zs.
        output: Concatenated output transform, saved as an LTA or M3Z depending\
            on the input transforms.
        source_image: Change source image geometry of output M3Z, useful for\
            GCAM inversion if the path of the original source volume changed.
        target_image: Change destination image geometry of output M3Z.
        reduce: Reduce output LTA to single LT.
        invert: Invert the output transform.
        downsample: Downsample output M3Z to spacing of 2; by default, the\
            output spacing is that of the rightmost input M3Z.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatenateGcamOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCATENATE_GCAM_METADATA)
    params = mri_concatenate_gcam_params(inputs=inputs, output=output, source_image=source_image, target_image=target_image, reduce=reduce, invert=invert, downsample=downsample)
    return mri_concatenate_gcam_execute(params, execution)


__all__ = [
    "MRI_CONCATENATE_GCAM_METADATA",
    "MriConcatenateGcamOutputs",
    "mri_concatenate_gcam",
    "mri_concatenate_gcam_params",
]
