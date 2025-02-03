# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIXEL2TSF_METADATA = Metadata(
    id="0bbc1887f97398283810259c9bfc2ba108df6a97.boutiques",
    name="fixel2tsf",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
Fixel2tsfConfigParameters = typing.TypedDict('Fixel2tsfConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
Fixel2tsfParameters = typing.TypedDict('Fixel2tsfParameters', {
    "__STYX_TYPE__": typing.Literal["fixel2tsf"],
    "angle": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Fixel2tsfConfigParameters] | None],
    "help": bool,
    "version": bool,
    "fixel_in": InputPathType,
    "tracks": InputPathType,
    "tsf": str,
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
        "fixel2tsf": fixel2tsf_cargs,
        "config": fixel2tsf_config_cargs,
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
        "fixel2tsf": fixel2tsf_outputs,
    }
    return vt.get(t)


def fixel2tsf_config_params(
    key: str,
    value: str,
) -> Fixel2tsfConfigParameters:
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


def fixel2tsf_config_cargs(
    params: Fixel2tsfConfigParameters,
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


class Fixel2tsfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixel2tsf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tsf: OutputPathType
    """the output track scalar file"""


def fixel2tsf_params(
    fixel_in: InputPathType,
    tracks: InputPathType,
    tsf: str,
    angle: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2tsfConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Fixel2tsfParameters:
    """
    Build parameters.
    
    Args:
        fixel_in: the input fixel data file (within the fixel directory).
        tracks: the input track file.
        tsf: the output track scalar file.
        angle: the max anglular threshold for computing correspondence between\
            a fixel direction and track tangent (default = 45 degrees).
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
        "__STYXTYPE__": "fixel2tsf",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "fixel_in": fixel_in,
        "tracks": tracks,
        "tsf": tsf,
    }
    if angle is not None:
        params["angle"] = angle
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixel2tsf_cargs(
    params: Fixel2tsfParameters,
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
    cargs.append("fixel2tsf")
    if params.get("angle") is not None:
        cargs.extend([
            "-angle",
            str(params.get("angle"))
        ])
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
    cargs.append(execution.input_file(params.get("fixel_in")))
    cargs.append(execution.input_file(params.get("tracks")))
    cargs.append(params.get("tsf"))
    return cargs


def fixel2tsf_outputs(
    params: Fixel2tsfParameters,
    execution: Execution,
) -> Fixel2tsfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fixel2tsfOutputs(
        root=execution.output_file("."),
        tsf=execution.output_file(params.get("tsf")),
    )
    return ret


def fixel2tsf_execute(
    params: Fixel2tsfParameters,
    execution: Execution,
) -> Fixel2tsfOutputs:
    """
    Map fixel values to a track scalar file based on an input tractogram.
    
    This command is useful for visualising all brain fixels (e.g. the output
    from fixelcfestats) in 3D.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fixel2tsfOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fixel2tsf_cargs(params, execution)
    ret = fixel2tsf_outputs(params, execution)
    execution.run(cargs)
    return ret


def fixel2tsf(
    fixel_in: InputPathType,
    tracks: InputPathType,
    tsf: str,
    angle: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fixel2tsfConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Fixel2tsfOutputs:
    """
    Map fixel values to a track scalar file based on an input tractogram.
    
    This command is useful for visualising all brain fixels (e.g. the output
    from fixelcfestats) in 3D.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        fixel_in: the input fixel data file (within the fixel directory).
        tracks: the input track file.
        tsf: the output track scalar file.
        angle: the max anglular threshold for computing correspondence between\
            a fixel direction and track tangent (default = 45 degrees).
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
        NamedTuple of outputs (described in `Fixel2tsfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXEL2TSF_METADATA)
    params = fixel2tsf_params(angle=angle, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, fixel_in=fixel_in, tracks=tracks, tsf=tsf)
    return fixel2tsf_execute(params, execution)


__all__ = [
    "FIXEL2TSF_METADATA",
    "Fixel2tsfOutputs",
    "fixel2tsf",
    "fixel2tsf_config_params",
    "fixel2tsf_params",
]
