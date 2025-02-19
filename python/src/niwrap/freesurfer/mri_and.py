# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_AND_METADATA = Metadata(
    id="fc9c157fa97aee9cd814998f22d0f65be168bad4.boutiques",
    name="mri_and",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriAndParameters = typing.TypedDict('MriAndParameters', {
    "__STYX_TYPE__": typing.Literal["mri_and"],
    "input_files": list[InputPathType],
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
        "mri_and": mri_and_cargs,
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
    }.get(t)


class MriAndOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_and(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_and_params(
    input_files: list[InputPathType],
) -> MriAndParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input volume files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_and",
        "input_files": input_files,
    }
    return params


def mri_and_cargs(
    params: MriAndParameters,
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
    cargs.append("mri_and")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def mri_and_outputs(
    params: MriAndParameters,
    execution: Execution,
) -> MriAndOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAndOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_and_execute(
    params: MriAndParameters,
    execution: Execution,
) -> MriAndOutputs:
    """
    Performs a logical voxel-wise AND on a series of volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAndOutputs`).
    """
    params = execution.params(params)
    cargs = mri_and_cargs(params, execution)
    ret = mri_and_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_and(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> MriAndOutputs:
    """
    Performs a logical voxel-wise AND on a series of volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input volume files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAndOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_AND_METADATA)
    params = mri_and_params(input_files=input_files)
    return mri_and_execute(params, execution)


__all__ = [
    "MRI_AND_METADATA",
    "MriAndOutputs",
    "MriAndParameters",
    "mri_and",
    "mri_and_params",
]
