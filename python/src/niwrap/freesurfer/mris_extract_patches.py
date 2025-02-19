# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_EXTRACT_PATCHES_METADATA = Metadata(
    id="4b1b272c0e5d898fdbf11dee43aa5f15d5fc44a4.boutiques",
    name="mris_extract_patches",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisExtractPatchesParameters = typing.TypedDict('MrisExtractPatchesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_extract_patches"],
    "subject": str,
    "output_dir": str,
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
        "mris_extract_patches": mris_extract_patches_cargs,
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


class MrisExtractPatchesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_extract_patches(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_extract_patches_params(
    subject: str,
    output_dir: str,
) -> MrisExtractPatchesParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject from which patches are to be extracted.
        output_dir: Output directory where patches will be saved.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_extract_patches",
        "subject": subject,
        "output_dir": output_dir,
    }
    return params


def mris_extract_patches_cargs(
    params: MrisExtractPatchesParameters,
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
    cargs.append("mris_extract_patches")
    cargs.append(params.get("subject"))
    cargs.append(params.get("output_dir"))
    return cargs


def mris_extract_patches_outputs(
    params: MrisExtractPatchesParameters,
    execution: Execution,
) -> MrisExtractPatchesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisExtractPatchesOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_extract_patches_execute(
    params: MrisExtractPatchesParameters,
    execution: Execution,
) -> MrisExtractPatchesOutputs:
    """
    A tool for extracting patches from brain surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisExtractPatchesOutputs`).
    """
    params = execution.params(params)
    cargs = mris_extract_patches_cargs(params, execution)
    ret = mris_extract_patches_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_extract_patches(
    subject: str,
    output_dir: str,
    runner: Runner | None = None,
) -> MrisExtractPatchesOutputs:
    """
    A tool for extracting patches from brain surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject from which patches are to be extracted.
        output_dir: Output directory where patches will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisExtractPatchesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_EXTRACT_PATCHES_METADATA)
    params = mris_extract_patches_params(subject=subject, output_dir=output_dir)
    return mris_extract_patches_execute(params, execution)


__all__ = [
    "MRIS_EXTRACT_PATCHES_METADATA",
    "MrisExtractPatchesOutputs",
    "MrisExtractPatchesParameters",
    "mris_extract_patches",
    "mris_extract_patches_params",
]
