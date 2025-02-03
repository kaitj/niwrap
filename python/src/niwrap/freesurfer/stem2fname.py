# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STEM2FNAME_METADATA = Metadata(
    id="b941ff1daaefec18565e73dea38778f44521acf7.boutiques",
    name="stem2fname",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Stem2fnameParameters = typing.TypedDict('Stem2fnameParameters', {
    "__STYX_TYPE__": typing.Literal["stem2fname"],
    "stem": str,
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
        "stem2fname": stem2fname_cargs,
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
        "stem2fname": stem2fname_outputs,
    }
    return vt.get(t)


class Stem2fnameOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stem2fname(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Full filename with the detected format. Format could be one of mgh, mgz,
    nii, nii.gz, bhdr, img, or w."""


def stem2fname_params(
    stem: str,
) -> Stem2fnameParameters:
    """
    Build parameters.
    
    Args:
        stem: The stem of the file (without extension).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stem2fname",
        "stem": stem,
    }
    return params


def stem2fname_cargs(
    params: Stem2fnameParameters,
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
    cargs.append("stem2fname")
    cargs.append(params.get("stem"))
    return cargs


def stem2fname_outputs(
    params: Stem2fnameParameters,
    execution: Execution,
) -> Stem2fnameOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Stem2fnameOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("stem") + ".[FORMAT]"),
    )
    return ret


def stem2fname_execute(
    params: Stem2fnameParameters,
    execution: Execution,
) -> Stem2fnameOutputs:
    """
    Determines the full filename with extension for a given file stem by checking
    various formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Stem2fnameOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = stem2fname_cargs(params, execution)
    ret = stem2fname_outputs(params, execution)
    execution.run(cargs)
    return ret


def stem2fname(
    stem: str,
    runner: Runner | None = None,
) -> Stem2fnameOutputs:
    """
    Determines the full filename with extension for a given file stem by checking
    various formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        stem: The stem of the file (without extension).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Stem2fnameOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STEM2FNAME_METADATA)
    params = stem2fname_params(stem=stem)
    return stem2fname_execute(params, execution)


__all__ = [
    "STEM2FNAME_METADATA",
    "Stem2fnameOutputs",
    "stem2fname",
    "stem2fname_params",
]
