# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_COMPUTE_BIAS_METADATA = Metadata(
    id="37471e0f282e684b7a904fea88a79fdbc35e80b4.boutiques",
    name="mri_compute_bias",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriComputeBiasParameters = typing.TypedDict('MriComputeBiasParameters', {
    "__STYX_TYPE__": typing.Literal["mri_compute_bias"],
    "subjects": list[str],
    "output_volume": str,
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
        "mri_compute_bias": mri_compute_bias_cargs,
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
        "mri_compute_bias": mri_compute_bias_outputs,
    }.get(t)


class MriComputeBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output volume containing the bias correction result."""


def mri_compute_bias_params(
    subjects: list[str],
    output_volume: str,
) -> MriComputeBiasParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subjects for which bias correction is calculated.
        output_volume: Output volume where the result will be stored.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_compute_bias",
        "subjects": subjects,
        "output_volume": output_volume,
    }
    return params


def mri_compute_bias_cargs(
    params: MriComputeBiasParameters,
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
    cargs.append("mri_compute_bias")
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_compute_bias_outputs(
    params: MriComputeBiasParameters,
    execution: Execution,
) -> MriComputeBiasOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriComputeBiasOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_compute_bias_execute(
    params: MriComputeBiasParameters,
    execution: Execution,
) -> MriComputeBiasOutputs:
    """
    Compute bias correction volumes for the given subjects and outputs the result to
    a specified volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriComputeBiasOutputs`).
    """
    params = execution.params(params)
    cargs = mri_compute_bias_cargs(params, execution)
    ret = mri_compute_bias_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_compute_bias(
    subjects: list[str],
    output_volume: str,
    runner: Runner | None = None,
) -> MriComputeBiasOutputs:
    """
    Compute bias correction volumes for the given subjects and outputs the result to
    a specified volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subjects for which bias correction is calculated.
        output_volume: Output volume where the result will be stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_BIAS_METADATA)
    params = mri_compute_bias_params(subjects=subjects, output_volume=output_volume)
    return mri_compute_bias_execute(params, execution)


__all__ = [
    "MRI_COMPUTE_BIAS_METADATA",
    "MriComputeBiasOutputs",
    "MriComputeBiasParameters",
    "mri_compute_bias",
    "mri_compute_bias_params",
]
