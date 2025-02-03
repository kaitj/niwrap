# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_REDUCE_METADATA = Metadata(
    id="cf6964a089f9810b1107cc8ec31b854f370cd7e4.boutiques",
    name="mri_reduce",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriReduceParameters = typing.TypedDict('MriReduceParameters', {
    "__STYX_TYPE__": typing.Literal["mri_reduce"],
    "input_file": InputPathType,
    "output_file": str,
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
        "mri_reduce": mri_reduce_cargs,
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
        "mri_reduce": mri_reduce_outputs,
    }
    return vt.get(t)


class MriReduceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_reduce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reduced_output: OutputPathType
    """Reduced MRI file output"""


def mri_reduce_params(
    input_file: InputPathType,
    output_file: str,
) -> MriReduceParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input MRI file.
        output_file: Output filename for the reduced MRI file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_reduce",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def mri_reduce_cargs(
    params: MriReduceParameters,
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
    cargs.append("mri_reduce")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def mri_reduce_outputs(
    params: MriReduceParameters,
    execution: Execution,
) -> MriReduceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriReduceOutputs(
        root=execution.output_file("."),
        reduced_output=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_reduce_execute(
    params: MriReduceParameters,
    execution: Execution,
) -> MriReduceOutputs:
    """
    A tool to reduce MRI file dimensions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriReduceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_reduce_cargs(params, execution)
    ret = mri_reduce_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_reduce(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> MriReduceOutputs:
    """
    A tool to reduce MRI file dimensions.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input MRI file.
        output_file: Output filename for the reduced MRI file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriReduceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_REDUCE_METADATA)
    params = mri_reduce_params(input_file=input_file, output_file=output_file)
    return mri_reduce_execute(params, execution)


__all__ = [
    "MRI_REDUCE_METADATA",
    "MriReduceOutputs",
    "mri_reduce",
    "mri_reduce_params",
]
