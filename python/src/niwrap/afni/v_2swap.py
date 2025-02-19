# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_2SWAP_METADATA = Metadata(
    id="9a225778ddb446b7e5915ca65f1e69f4a2104017.boutiques",
    name="2swap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V2swapParameters = typing.TypedDict('V2swapParameters', {
    "__STYX_TYPE__": typing.Literal["2swap"],
    "quiet": bool,
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
        "2swap": v_2swap_cargs,
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


class V2swapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_2swap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_2swap_params(
    input_files: list[InputPathType],
    quiet: bool = False,
) -> V2swapParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input files.
        quiet: Work quietly.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "2swap",
        "quiet": quiet,
        "input_files": input_files,
    }
    return params


def v_2swap_cargs(
    params: V2swapParameters,
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
    cargs.append("2swap")
    if params.get("quiet"):
        cargs.append("-q")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def v_2swap_outputs(
    params: V2swapParameters,
    execution: Execution,
) -> V2swapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V2swapOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_2swap_execute(
    params: V2swapParameters,
    execution: Execution,
) -> V2swapOutputs:
    """
    Swaps byte pairs on the files listed.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V2swapOutputs`).
    """
    params = execution.params(params)
    cargs = v_2swap_cargs(params, execution)
    ret = v_2swap_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_2swap(
    input_files: list[InputPathType],
    quiet: bool = False,
    runner: Runner | None = None,
) -> V2swapOutputs:
    """
    Swaps byte pairs on the files listed.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input files.
        quiet: Work quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2swapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_2SWAP_METADATA)
    params = v_2swap_params(quiet=quiet, input_files=input_files)
    return v_2swap_execute(params, execution)


__all__ = [
    "V2swapOutputs",
    "V2swapParameters",
    "V_2SWAP_METADATA",
    "v_2swap",
    "v_2swap_params",
]
