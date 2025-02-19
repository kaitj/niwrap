# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UNPACK_MNC_TCL_METADATA = Metadata(
    id="54eec142d994829a43977ef77cc7f837f8d06635.boutiques",
    name="unpack_mnc.tcl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
UnpackMncTclParameters = typing.TypedDict('UnpackMncTclParameters', {
    "__STYX_TYPE__": typing.Literal["unpack_mnc.tcl"],
    "verbose": bool,
    "output_dir": typing.NotRequired[str | None],
    "input_file": typing.NotRequired[InputPathType | None],
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
        "unpack_mnc.tcl": unpack_mnc_tcl_cargs,
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
        "unpack_mnc.tcl": unpack_mnc_tcl_outputs,
    }.get(t)


class UnpackMncTclOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpack_mnc_tcl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unpacked_file: OutputPathType | None
    """Unpacked output MINC file"""


def unpack_mnc_tcl_params(
    verbose: bool = False,
    output_dir: str | None = None,
    input_file: InputPathType | None = None,
) -> UnpackMncTclParameters:
    """
    Build parameters.
    
    Args:
        verbose: Verbose output messages.
        output_dir: Output directory for unpacked files.
        input_file: Specify a custom input file for unpacking.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "unpack_mnc.tcl",
        "verbose": verbose,
    }
    if output_dir is not None:
        params["output_dir"] = output_dir
    if input_file is not None:
        params["input_file"] = input_file
    return params


def unpack_mnc_tcl_cargs(
    params: UnpackMncTclParameters,
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
    cargs.append("unpack_mnc.tcl")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("output_dir") is not None:
        cargs.extend([
            "-o",
            params.get("output_dir")
        ])
    if params.get("input_file") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("input_file"))
        ])
    return cargs


def unpack_mnc_tcl_outputs(
    params: UnpackMncTclParameters,
    execution: Execution,
) -> UnpackMncTclOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UnpackMncTclOutputs(
        root=execution.output_file("."),
        unpacked_file=execution.output_file(params.get("output_dir") + "/unpacked_data.mnc") if (params.get("output_dir") is not None) else None,
    )
    return ret


def unpack_mnc_tcl_execute(
    params: UnpackMncTclParameters,
    execution: Execution,
) -> UnpackMncTclOutputs:
    """
    A tool for unpacking MINC format images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UnpackMncTclOutputs`).
    """
    params = execution.params(params)
    cargs = unpack_mnc_tcl_cargs(params, execution)
    ret = unpack_mnc_tcl_outputs(params, execution)
    execution.run(cargs)
    return ret


def unpack_mnc_tcl(
    verbose: bool = False,
    output_dir: str | None = None,
    input_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> UnpackMncTclOutputs:
    """
    A tool for unpacking MINC format images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        verbose: Verbose output messages.
        output_dir: Output directory for unpacked files.
        input_file: Specify a custom input file for unpacking.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackMncTclOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACK_MNC_TCL_METADATA)
    params = unpack_mnc_tcl_params(verbose=verbose, output_dir=output_dir, input_file=input_file)
    return unpack_mnc_tcl_execute(params, execution)


__all__ = [
    "UNPACK_MNC_TCL_METADATA",
    "UnpackMncTclOutputs",
    "UnpackMncTclParameters",
    "unpack_mnc_tcl",
    "unpack_mnc_tcl_params",
]
