# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INFLATE_SUBJECT_NEW_METADATA = Metadata(
    id="c3ea7e0b28d39449428a797435fdabb03c6243ca.boutiques",
    name="inflate_subject_new",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
InflateSubjectNewParameters = typing.TypedDict('InflateSubjectNewParameters', {
    "__STYX_TYPE__": typing.Literal["inflate_subject_new"],
    "subject_dir": str,
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
        "inflate_subject_new": inflate_subject_new_cargs,
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


class InflateSubjectNewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inflate_subject_new(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def inflate_subject_new_params(
    subject_dir: str,
) -> InflateSubjectNewParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Directory containing the subject data to be inflated.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "inflate_subject_new",
        "subject_dir": subject_dir,
    }
    return params


def inflate_subject_new_cargs(
    params: InflateSubjectNewParameters,
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
    cargs.append("inflate_subject_new")
    cargs.append(params.get("subject_dir"))
    return cargs


def inflate_subject_new_outputs(
    params: InflateSubjectNewParameters,
    execution: Execution,
) -> InflateSubjectNewOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InflateSubjectNewOutputs(
        root=execution.output_file("."),
    )
    return ret


def inflate_subject_new_execute(
    params: InflateSubjectNewParameters,
    execution: Execution,
) -> InflateSubjectNewOutputs:
    """
    Tool to inflate subject surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewOutputs`).
    """
    params = execution.params(params)
    cargs = inflate_subject_new_cargs(params, execution)
    ret = inflate_subject_new_outputs(params, execution)
    execution.run(cargs)
    return ret


def inflate_subject_new(
    subject_dir: str,
    runner: Runner | None = None,
) -> InflateSubjectNewOutputs:
    """
    Tool to inflate subject surfaces.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Directory containing the subject data to be inflated.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InflateSubjectNewOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INFLATE_SUBJECT_NEW_METADATA)
    params = inflate_subject_new_params(subject_dir=subject_dir)
    return inflate_subject_new_execute(params, execution)


__all__ = [
    "INFLATE_SUBJECT_NEW_METADATA",
    "InflateSubjectNewOutputs",
    "InflateSubjectNewParameters",
    "inflate_subject_new",
    "inflate_subject_new_params",
]
