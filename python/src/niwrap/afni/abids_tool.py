# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ABIDS_TOOL_METADATA = Metadata(
    id="ecdd7e187a3a330cd02d094f809fb0b75a51fe76.boutiques",
    name="abids_tool",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AbidsToolParameters = typing.TypedDict('AbidsToolParameters', {
    "__STYX_TYPE__": typing.Literal["abids_tool"],
    "input_files": list[InputPathType],
    "copy_prefix": typing.NotRequired[list[str] | None],
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
        "abids_tool": abids_tool_cargs,
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


def abids_tool_params(
    input_files: list[InputPathType],
    copy_prefix: list[str] | None = None,
) -> AbidsToolParameters:
    """
    Build parameters.
    
    Args:
        input_files: At least one 3d+time dataset in NIFTI format.
        copy_prefix: Copy both the NIFTI dataset(s) and matching .json file(s)\
            to PREFIX. Must have the same number of prefixes as datasets.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "abids_tool",
        "input_files": input_files,
    }
    if copy_prefix is not None:
        params["copy_prefix"] = copy_prefix
    return params


def abids_tool_cargs(
    params: AbidsToolParameters,
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
    cargs.append("abids_tool.py")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("copy_prefix") is not None:
        cargs.extend([
            "-copy",
            *params.get("copy_prefix")
        ])
    return cargs


def abids_tool_outputs(
    params: AbidsToolParameters,
    execution: Execution,
) -> AbidsToolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AbidsToolOutputs(
        root=execution.output_file("."),
    )
    return ret


def abids_tool_execute(
    params: AbidsToolParameters,
    execution: Execution,
) -> AbidsToolOutputs:
    """
    A tool to work with BIDS formatted datasets created with dcm2niix_afni or
    dcm2niix, mainly to pull information from the matching JSON file and refit the
    input dataset using 3drefit.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AbidsToolOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = abids_tool_cargs(params, execution)
    ret = abids_tool_outputs(params, execution)
    execution.run(cargs)
    return ret


def abids_tool(
    input_files: list[InputPathType],
    copy_prefix: list[str] | None = None,
    runner: Runner | None = None,
) -> AbidsToolOutputs:
    """
    A tool to work with BIDS formatted datasets created with dcm2niix_afni or
    dcm2niix, mainly to pull information from the matching JSON file and refit the
    input dataset using 3drefit.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: At least one 3d+time dataset in NIFTI format.
        copy_prefix: Copy both the NIFTI dataset(s) and matching .json file(s)\
            to PREFIX. Must have the same number of prefixes as datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AbidsToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ABIDS_TOOL_METADATA)
    params = abids_tool_params(input_files=input_files, copy_prefix=copy_prefix)
    return abids_tool_execute(params, execution)


__all__ = [
    "ABIDS_TOOL_METADATA",
    "abids_tool",
    "abids_tool_params",
]
