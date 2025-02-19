# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SPHERE_SUBJECT_METADATA = Metadata(
    id="1b01c8e4cff0b051c46d47179ad938955066fe57.boutiques",
    name="sphere_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SphereSubjectParameters = typing.TypedDict('SphereSubjectParameters', {
    "__STYX_TYPE__": typing.Literal["sphere_subject"],
    "input_dir": str,
    "output_file": str,
    "license_file": typing.NotRequired[str | None],
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
        "sphere_subject": sphere_subject_cargs,
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
        "sphere_subject": sphere_subject_outputs,
    }.get(t)


class SphereSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sphere_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_result: OutputPathType
    """Output of the sphere_subject execution."""


def sphere_subject_params(
    input_dir: str,
    output_file: str,
    license_file: str | None = "/usr/local/freesurfer/.license",
) -> SphereSubjectParameters:
    """
    Build parameters.
    
    Args:
        input_dir: Input subject directory.
        output_file: Output file for results.
        license_file: Path to FreeSurfer license file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sphere_subject",
        "input_dir": input_dir,
        "output_file": output_file,
    }
    if license_file is not None:
        params["license_file"] = license_file
    return params


def sphere_subject_cargs(
    params: SphereSubjectParameters,
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
    cargs.append("sphere_subject")
    cargs.append(params.get("input_dir"))
    cargs.append(params.get("output_file"))
    if params.get("license_file") is not None:
        cargs.append(params.get("license_file"))
    return cargs


def sphere_subject_outputs(
    params: SphereSubjectParameters,
    execution: Execution,
) -> SphereSubjectOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SphereSubjectOutputs(
        root=execution.output_file("."),
        output_result=execution.output_file(params.get("output_file")),
    )
    return ret


def sphere_subject_execute(
    params: SphereSubjectParameters,
    execution: Execution,
) -> SphereSubjectOutputs:
    """
    A FreeSurfer tool for processing subject data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SphereSubjectOutputs`).
    """
    params = execution.params(params)
    cargs = sphere_subject_cargs(params, execution)
    ret = sphere_subject_outputs(params, execution)
    execution.run(cargs)
    return ret


def sphere_subject(
    input_dir: str,
    output_file: str,
    license_file: str | None = "/usr/local/freesurfer/.license",
    runner: Runner | None = None,
) -> SphereSubjectOutputs:
    """
    A FreeSurfer tool for processing subject data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_dir: Input subject directory.
        output_file: Output file for results.
        license_file: Path to FreeSurfer license file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SphereSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHERE_SUBJECT_METADATA)
    params = sphere_subject_params(input_dir=input_dir, output_file=output_file, license_file=license_file)
    return sphere_subject_execute(params, execution)


__all__ = [
    "SPHERE_SUBJECT_METADATA",
    "SphereSubjectOutputs",
    "SphereSubjectParameters",
    "sphere_subject",
    "sphere_subject_params",
]
