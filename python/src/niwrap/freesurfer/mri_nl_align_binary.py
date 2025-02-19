# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_NL_ALIGN_BINARY_METADATA = Metadata(
    id="ef5528a0517700c40ec5c8c97d382ea8956dfbf8.boutiques",
    name="mri_nl_align_binary",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNlAlignBinaryParameters = typing.TypedDict('MriNlAlignBinaryParameters', {
    "__STYX_TYPE__": typing.Literal["mri_nl_align_binary"],
    "source_file": InputPathType,
    "target_file": InputPathType,
    "warp_file": str,
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
        "mri_nl_align_binary": mri_nl_align_binary_cargs,
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
        "mri_nl_align_binary": mri_nl_align_binary_outputs,
    }.get(t)


class MriNlAlignBinaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_nl_align_binary(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_warp: OutputPathType
    """Output warp from the alignment process"""


def mri_nl_align_binary_params(
    source_file: InputPathType,
    target_file: InputPathType,
    warp_file: str,
) -> MriNlAlignBinaryParameters:
    """
    Build parameters.
    
    Args:
        source_file: Source image file for alignment.
        target_file: Target image file for alignment.
        warp_file: Output warp file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_nl_align_binary",
        "source_file": source_file,
        "target_file": target_file,
        "warp_file": warp_file,
    }
    return params


def mri_nl_align_binary_cargs(
    params: MriNlAlignBinaryParameters,
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
    cargs.append("mri_nl_align_binary")
    cargs.append(execution.input_file(params.get("source_file")))
    cargs.append(execution.input_file(params.get("target_file")))
    cargs.append(params.get("warp_file"))
    return cargs


def mri_nl_align_binary_outputs(
    params: MriNlAlignBinaryParameters,
    execution: Execution,
) -> MriNlAlignBinaryOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNlAlignBinaryOutputs(
        root=execution.output_file("."),
        output_warp=execution.output_file(params.get("warp_file")),
    )
    return ret


def mri_nl_align_binary_execute(
    params: MriNlAlignBinaryParameters,
    execution: Execution,
) -> MriNlAlignBinaryOutputs:
    """
    Non-linear alignment tool for MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNlAlignBinaryOutputs`).
    """
    params = execution.params(params)
    cargs = mri_nl_align_binary_cargs(params, execution)
    ret = mri_nl_align_binary_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_nl_align_binary(
    source_file: InputPathType,
    target_file: InputPathType,
    warp_file: str,
    runner: Runner | None = None,
) -> MriNlAlignBinaryOutputs:
    """
    Non-linear alignment tool for MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_file: Source image file for alignment.
        target_file: Target image file for alignment.
        warp_file: Output warp file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNlAlignBinaryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NL_ALIGN_BINARY_METADATA)
    params = mri_nl_align_binary_params(source_file=source_file, target_file=target_file, warp_file=warp_file)
    return mri_nl_align_binary_execute(params, execution)


__all__ = [
    "MRI_NL_ALIGN_BINARY_METADATA",
    "MriNlAlignBinaryOutputs",
    "MriNlAlignBinaryParameters",
    "mri_nl_align_binary",
    "mri_nl_align_binary_params",
]
