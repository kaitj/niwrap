# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MORPH_ONLY_SUBJECT_RH_METADATA = Metadata(
    id="cf178313d144b58ca109c79e9c3499855a731ab6.boutiques",
    name="morph_only_subject-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MorphOnlySubjectRhParameters = typing.TypedDict('MorphOnlySubjectRhParameters', {
    "__STYX_TYPE__": typing.Literal["morph_only_subject-rh"],
    "subject_dir": InputPathType,
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
        "morph_only_subject-rh": morph_only_subject_rh_cargs,
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
        "morph_only_subject-rh": morph_only_subject_rh_outputs,
    }.get(t)


class MorphOnlySubjectRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_only_subject_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """The output morphing files for the right hemisphere generated by the
    process."""


def morph_only_subject_rh_params(
    subject_dir: InputPathType,
) -> MorphOnlySubjectRhParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Path to the subject's directory containing the necessary\
            input files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "morph_only_subject-rh",
        "subject_dir": subject_dir,
    }
    return params


def morph_only_subject_rh_cargs(
    params: MorphOnlySubjectRhParameters,
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
    cargs.extend([
        "-rh",
        "morph_only_subject" + execution.input_file(params.get("subject_dir"))
    ])
    return cargs


def morph_only_subject_rh_outputs(
    params: MorphOnlySubjectRhParameters,
    execution: Execution,
) -> MorphOnlySubjectRhOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MorphOnlySubjectRhOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("/usr/local/freesurfer/subjects/" + pathlib.Path(params.get("subject_dir")).name + "/rh.morph"),
    )
    return ret


def morph_only_subject_rh_execute(
    params: MorphOnlySubjectRhParameters,
    execution: Execution,
) -> MorphOnlySubjectRhOutputs:
    """
    This tool processes morph-specific operations for the right hemisphere of the
    brain using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectRhOutputs`).
    """
    params = execution.params(params)
    cargs = morph_only_subject_rh_cargs(params, execution)
    ret = morph_only_subject_rh_outputs(params, execution)
    execution.run(cargs)
    return ret


def morph_only_subject_rh(
    subject_dir: InputPathType,
    runner: Runner | None = None,
) -> MorphOnlySubjectRhOutputs:
    """
    This tool processes morph-specific operations for the right hemisphere of the
    brain using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the subject's directory containing the necessary\
            input files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_ONLY_SUBJECT_RH_METADATA)
    params = morph_only_subject_rh_params(subject_dir=subject_dir)
    return morph_only_subject_rh_execute(params, execution)


__all__ = [
    "MORPH_ONLY_SUBJECT_RH_METADATA",
    "MorphOnlySubjectRhOutputs",
    "MorphOnlySubjectRhParameters",
    "morph_only_subject_rh",
    "morph_only_subject_rh_params",
]
