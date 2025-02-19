# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRCENTROID_METADATA = Metadata(
    id="d45d49e8b930b948a798b910b254792bd30544a6.boutiques",
    name="mrcentroid",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrcentroidConfigParameters = typing.TypedDict('MrcentroidConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrcentroidParameters = typing.TypedDict('MrcentroidParameters', {
    "__STYX_TYPE__": typing.Literal["mrcentroid"],
    "mask": typing.NotRequired[InputPathType | None],
    "voxelspace": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrcentroidConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": InputPathType,
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
        "mrcentroid": mrcentroid_cargs,
        "config": mrcentroid_config_cargs,
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


def mrcentroid_config_params(
    key: str,
    value: str,
) -> MrcentroidConfigParameters:
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


def mrcentroid_config_cargs(
    params: MrcentroidConfigParameters,
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


class MrcentroidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrcentroid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mrcentroid_params(
    input_: InputPathType,
    mask: InputPathType | None = None,
    voxelspace: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcentroidConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrcentroidParameters:
    """
    Build parameters.
    
    Args:
        input_: the input image.
        mask: only include voxels within a mask in the calculation.
        voxelspace: report image centre of mass in voxel space rather than\
            scanner space.
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
        "__STYXTYPE__": "mrcentroid",
        "voxelspace": voxelspace,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
    }
    if mask is not None:
        params["mask"] = mask
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrcentroid_cargs(
    params: MrcentroidParameters,
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
    cargs.append("mrcentroid")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("voxelspace"):
        cargs.append("-voxelspace")
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
    cargs.append(execution.input_file(params.get("input")))
    return cargs


def mrcentroid_outputs(
    params: MrcentroidParameters,
    execution: Execution,
) -> MrcentroidOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrcentroidOutputs(
        root=execution.output_file("."),
    )
    return ret


def mrcentroid_execute(
    params: MrcentroidParameters,
    execution: Execution,
) -> MrcentroidOutputs:
    """
    Determine the centre of mass / centre of gravity of an image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrcentroidOutputs`).
    """
    params = execution.params(params)
    cargs = mrcentroid_cargs(params, execution)
    ret = mrcentroid_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrcentroid(
    input_: InputPathType,
    mask: InputPathType | None = None,
    voxelspace: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrcentroidConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrcentroidOutputs:
    """
    Determine the centre of mass / centre of gravity of an image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input image.
        mask: only include voxels within a mask in the calculation.
        voxelspace: report image centre of mass in voxel space rather than\
            scanner space.
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
        NamedTuple of outputs (described in `MrcentroidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRCENTROID_METADATA)
    params = mrcentroid_params(mask=mask, voxelspace=voxelspace, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_)
    return mrcentroid_execute(params, execution)


__all__ = [
    "MRCENTROID_METADATA",
    "MrcentroidConfigParameters",
    "MrcentroidOutputs",
    "MrcentroidParameters",
    "mrcentroid",
    "mrcentroid_config_params",
    "mrcentroid_params",
]
