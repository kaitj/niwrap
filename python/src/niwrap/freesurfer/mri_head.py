# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_HEAD_METADATA = Metadata(
    id="fb167e02a7257ba8b9a2343709e24ec6a1664305.boutiques",
    name="mri_head",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriHeadParameters = typing.TypedDict('MriHeadParameters', {
    "__STYX_TYPE__": typing.Literal["mri_head"],
    "identify": bool,
    "read": bool,
    "filename": typing.NotRequired[str | None],
    "question_mark_help": bool,
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
        "mri_head": mri_head_cargs,
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
    vt = {}
    return vt.get(t)


def mri_head_params(
    identify: bool = False,
    read: bool = False,
    filename: str | None = None,
    question_mark_help: bool = False,
) -> MriHeadParameters:
    """
    Build parameters.
    
    Args:
        identify: Identify the MRI file.
        read: Read the MRI file.
        filename: Filename for identification or reading.
        question_mark_help: Display help or usage information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_head",
        "identify": identify,
        "read": read,
        "question_mark_help": question_mark_help,
    }
    if filename is not None:
        params["filename"] = filename
    return params


def mri_head_cargs(
    params: MriHeadParameters,
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
    cargs.append("mri_head")
    if params.get("identify"):
        cargs.append("-identify")
    if params.get("read"):
        cargs.append("-read")
    if params.get("filename") is not None:
        cargs.append(params.get("filename"))
    if params.get("question_mark_help"):
        cargs.append("-?")
    return cargs


def mri_head_outputs(
    params: MriHeadParameters,
    execution: Execution,
) -> MriHeadOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriHeadOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_head_execute(
    params: MriHeadParameters,
    execution: Execution,
) -> MriHeadOutputs:
    """
    No description.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriHeadOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_head_cargs(params, execution)
    ret = mri_head_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_head(
    identify: bool = False,
    read: bool = False,
    filename: str | None = None,
    question_mark_help: bool = False,
    runner: Runner | None = None,
) -> MriHeadOutputs:
    """
    No description.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        identify: Identify the MRI file.
        read: Read the MRI file.
        filename: Filename for identification or reading.
        question_mark_help: Display help or usage information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriHeadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_HEAD_METADATA)
    params = mri_head_params(identify=identify, read=read, filename=filename, question_mark_help=question_mark_help)
    return mri_head_execute(params, execution)


__all__ = [
    "MRI_HEAD_METADATA",
    "mri_head",
    "mri_head_params",
]
