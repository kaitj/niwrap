# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_MARRY_METADATA = Metadata(
    id="bf4086d827742de99647b8c529893b01461d76ef.boutiques",
    name="1dMarry",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dMarryParameters = typing.TypedDict('V1dMarryParameters', {
    "__STYX_TYPE__": typing.Literal["1dMarry"],
    "sep": typing.NotRequired[str | None],
    "divorce": bool,
    "files": list[InputPathType],
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
        "1dMarry": v_1d_marry_cargs,
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
        "1dMarry": v_1d_marry_outputs,
    }
    return vt.get(t)


class V1dMarryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_marry(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file when marrying files. This file should be captured using a
    redirection such as '>'."""
    divorcee_a: OutputPathType
    """First output file when divorcing."""
    divorcee_b: OutputPathType
    """Second output file when divorcing."""


def v_1d_marry_params(
    files: list[InputPathType],
    sep: str | None = None,
    divorce: bool = False,
) -> V1dMarryParameters:
    """
    Build parameters.
    
    Args:
        files: Input file(s) to be married or divorced.
        sep: Separator(s) for marrying files. The first character is used as\
            the separator between values 1 and 2, the second character between\
            values 2 and 3, etc.
        divorce: Divorce mode: splits married file into separate files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dMarry",
        "divorce": divorce,
        "files": files,
    }
    if sep is not None:
        params["sep"] = sep
    return params


def v_1d_marry_cargs(
    params: V1dMarryParameters,
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
    cargs.append("1dMarry")
    if params.get("sep") is not None:
        cargs.extend([
            "-sep",
            params.get("sep")
        ])
    if params.get("divorce"):
        cargs.append("-divorce")
    cargs.extend([execution.input_file(f) for f in params.get("files")])
    cargs.append("[FILE2]")
    return cargs


def v_1d_marry_outputs(
    params: V1dMarryParameters,
    execution: Execution,
) -> V1dMarryOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dMarryOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("stdout"),
        divorcee_a=execution.output_file("[FILE2]_A.1D"),
        divorcee_b=execution.output_file("[FILE2]_B.1D"),
    )
    return ret


def v_1d_marry_execute(
    params: V1dMarryParameters,
    execution: Execution,
) -> V1dMarryOutputs:
    """
    Joins together 2 (or more) ragged-right .1D files, for use with 3dDeconvolve
    -stim_times_AM2, or breaks up 1 married file into 2 (or more) single-valued
    files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dMarryOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_1d_marry_cargs(params, execution)
    ret = v_1d_marry_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1d_marry(
    files: list[InputPathType],
    sep: str | None = None,
    divorce: bool = False,
    runner: Runner | None = None,
) -> V1dMarryOutputs:
    """
    Joins together 2 (or more) ragged-right .1D files, for use with 3dDeconvolve
    -stim_times_AM2, or breaks up 1 married file into 2 (or more) single-valued
    files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        files: Input file(s) to be married or divorced.
        sep: Separator(s) for marrying files. The first character is used as\
            the separator between values 1 and 2, the second character between\
            values 2 and 3, etc.
        divorce: Divorce mode: splits married file into separate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dMarryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_MARRY_METADATA)
    params = v_1d_marry_params(sep=sep, divorce=divorce, files=files)
    return v_1d_marry_execute(params, execution)


__all__ = [
    "V1dMarryOutputs",
    "V_1D_MARRY_METADATA",
    "v_1d_marry",
    "v_1d_marry_params",
]
