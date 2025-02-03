# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_APPLY_BIAS_METADATA = Metadata(
    id="b81c79a708e537c2c711365f270f39010a6db69c.boutiques",
    name="mri_apply_bias",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriApplyBiasParameters = typing.TypedDict('MriApplyBiasParameters', {
    "__STYX_TYPE__": typing.Literal["mri_apply_bias"],
    "input_volume": InputPathType,
    "bias_volume": InputPathType,
    "output_volume": str,
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
        "mri_apply_bias": mri_apply_bias_cargs,
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
        "mri_apply_bias": mri_apply_bias_outputs,
    }
    return vt.get(t)


class MriApplyBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_apply_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Output volume after applying bias"""


def mri_apply_bias_params(
    input_volume: InputPathType,
    bias_volume: InputPathType,
    output_volume: str,
) -> MriApplyBiasParameters:
    """
    Build parameters.
    
    Args:
        input_volume: The input volume file.
        bias_volume: The bias volume file.
        output_volume: The output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_apply_bias",
        "input_volume": input_volume,
        "bias_volume": bias_volume,
        "output_volume": output_volume,
    }
    return params


def mri_apply_bias_cargs(
    params: MriApplyBiasParameters,
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
    cargs.append("mri_apply_bias")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(execution.input_file(params.get("bias_volume")))
    cargs.append(params.get("output_volume"))
    return cargs


def mri_apply_bias_outputs(
    params: MriApplyBiasParameters,
    execution: Execution,
) -> MriApplyBiasOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriApplyBiasOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_apply_bias_execute(
    params: MriApplyBiasParameters,
    execution: Execution,
) -> MriApplyBiasOutputs:
    """
    A tool for applying a bias volume to an input volume to produce an output
    volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriApplyBiasOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_apply_bias_cargs(params, execution)
    ret = mri_apply_bias_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_apply_bias(
    input_volume: InputPathType,
    bias_volume: InputPathType,
    output_volume: str,
    runner: Runner | None = None,
) -> MriApplyBiasOutputs:
    """
    A tool for applying a bias volume to an input volume to produce an output
    volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: The input volume file.
        bias_volume: The bias volume file.
        output_volume: The output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriApplyBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_APPLY_BIAS_METADATA)
    params = mri_apply_bias_params(input_volume=input_volume, bias_volume=bias_volume, output_volume=output_volume)
    return mri_apply_bias_execute(params, execution)


__all__ = [
    "MRI_APPLY_BIAS_METADATA",
    "MriApplyBiasOutputs",
    "mri_apply_bias",
    "mri_apply_bias_params",
]
