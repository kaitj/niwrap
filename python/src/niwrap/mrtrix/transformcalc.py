# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TRANSFORMCALC_METADATA = Metadata(
    id="21a10a581aef63905bb25a793fa05b7d78555ebc.boutiques",
    name="transformcalc",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
TransformcalcConfigParameters = typing.TypedDict('TransformcalcConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
TransformcalcParameters = typing.TypedDict('TransformcalcParameters', {
    "__STYX_TYPE__": typing.Literal["transformcalc"],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TransformcalcConfigParameters] | None],
    "help": bool,
    "version": bool,
    "inputs": list[str],
    "operation": str,
    "output": str,
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
        "transformcalc": transformcalc_cargs,
        "config": transformcalc_config_cargs,
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
        "transformcalc": transformcalc_outputs,
    }
    return vt.get(t)


def transformcalc_config_params(
    key: str,
    value: str,
) -> TransformcalcConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def transformcalc_config_cargs(
    params: TransformcalcConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class TransformcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `transformcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output transformation matrix."""


def transformcalc_params(
    inputs: list[str],
    operation: str,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TransformcalcConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TransformcalcParameters:
    """
    Build parameters.
    
    Args:
        inputs: the input(s) for the specified operation.
        operation: the operation to perform, one of: invert, half, rigid,\
            header, average, interpolate, decompose, align_vertices_rigid,\
            align_vertices_rigid_scale (see description section for details).
        output: the output transformation matrix.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "transformcalc",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "inputs": inputs,
        "operation": operation,
        "output": output,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def transformcalc_cargs(
    params: TransformcalcParameters,
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
    cargs.append("transformcalc")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.extend(params.get("inputs"))
    cargs.append(params.get("operation"))
    cargs.append(params.get("output"))
    return cargs


def transformcalc_outputs(
    params: TransformcalcParameters,
    execution: Execution,
) -> TransformcalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TransformcalcOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def transformcalc_execute(
    params: TransformcalcParameters,
    execution: Execution,
) -> TransformcalcOutputs:
    """
    Perform calculations on linear transformation matrices.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TransformcalcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = transformcalc_cargs(params, execution)
    ret = transformcalc_outputs(params, execution)
    execution.run(cargs)
    return ret


def transformcalc(
    inputs: list[str],
    operation: str,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TransformcalcConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TransformcalcOutputs:
    """
    Perform calculations on linear transformation matrices.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        inputs: the input(s) for the specified operation.
        operation: the operation to perform, one of: invert, half, rigid,\
            header, average, interpolate, decompose, align_vertices_rigid,\
            align_vertices_rigid_scale (see description section for details).
        output: the output transformation matrix.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TransformcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRANSFORMCALC_METADATA)
    params = transformcalc_params(info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, inputs=inputs, operation=operation, output=output)
    return transformcalc_execute(params, execution)


__all__ = [
    "TRANSFORMCALC_METADATA",
    "TransformcalcOutputs",
    "transformcalc",
    "transformcalc_config_params",
    "transformcalc_params",
]
