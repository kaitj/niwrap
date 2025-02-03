# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRSTATS_METADATA = Metadata(
    id="ac3503467263b1605cd6395c44e756384ef84457.boutiques",
    name="mrstats",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
MrstatsOutputParameters = typing.TypedDict('MrstatsOutputParameters', {
    "__STYX_TYPE__": typing.Literal["output"],
    "field": str,
})
MrstatsConfigParameters = typing.TypedDict('MrstatsConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
MrstatsParameters = typing.TypedDict('MrstatsParameters', {
    "__STYX_TYPE__": typing.Literal["mrstats"],
    "output": typing.NotRequired[list[MrstatsOutputParameters] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "ignorezero": bool,
    "allvolumes": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[MrstatsConfigParameters] | None],
    "help": bool,
    "version": bool,
    "image": InputPathType,
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
        "mrstats": mrstats_cargs,
        "output": mrstats_output_cargs,
        "config": mrstats_config_cargs,
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


def mrstats_output_params(
    field: str,
) -> MrstatsOutputParameters:
    """
    Build parameters.
    
    Args:
        field: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, std_rv, min, max,\
            count. Useful for use in scripts. Both std options refer to the\
            unbiased (sample) standard deviation. For complex data, min, max and\
            std are calculated separately for real and imaginary parts, std_rv is\
            based on the real valued variance (equals sqrt of sum of variances of\
            imaginary and real parts).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "output",
        "field": field,
    }
    return params


def mrstats_output_cargs(
    params: MrstatsOutputParameters,
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
    cargs.append("-output")
    cargs.append(params.get("field"))
    return cargs


def mrstats_config_params(
    key: str,
    value: str,
) -> MrstatsConfigParameters:
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


def mrstats_config_cargs(
    params: MrstatsConfigParameters,
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


def mrstats_params(
    image: InputPathType,
    output: list[MrstatsOutputParameters] | None = None,
    mask: InputPathType | None = None,
    ignorezero: bool = False,
    allvolumes: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrstatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> MrstatsParameters:
    """
    Build parameters.
    
    Args:
        image: the input image from which statistics will be computed.
        output: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, std_rv, min, max,\
            count. Useful for use in scripts. Both std options refer to the\
            unbiased (sample) standard deviation. For complex data, min, max and\
            std are calculated separately for real and imaginary parts, std_rv is\
            based on the real valued variance (equals sqrt of sum of variances of\
            imaginary and real parts).
        mask: only perform computation within the specified binary mask image.
        ignorezero: ignore zero values during statistics calculation.
        allvolumes: generate statistics across all image volumes, rather than\
            one set of statistics per image volume.
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
        "__STYXTYPE__": "mrstats",
        "ignorezero": ignorezero,
        "allvolumes": allvolumes,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "image": image,
    }
    if output is not None:
        params["output"] = output
    if mask is not None:
        params["mask"] = mask
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def mrstats_cargs(
    params: MrstatsParameters,
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
    cargs.append("mrstats")
    if params.get("output") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("output")] for a in c])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("ignorezero"):
        cargs.append("-ignorezero")
    if params.get("allvolumes"):
        cargs.append("-allvolumes")
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
    cargs.append(execution.input_file(params.get("image")))
    return cargs


def mrstats_outputs(
    params: MrstatsParameters,
    execution: Execution,
) -> MrstatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrstatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mrstats_execute(
    params: MrstatsParameters,
    execution: Execution,
) -> MrstatsOutputs:
    """
    Compute images statistics.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrstatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mrstats_cargs(params, execution)
    ret = mrstats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrstats(
    image: InputPathType,
    output: list[MrstatsOutputParameters] | None = None,
    mask: InputPathType | None = None,
    ignorezero: bool = False,
    allvolumes: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrstatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrstatsOutputs:
    """
    Compute images statistics.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        image: the input image from which statistics will be computed.
        output: output only the field specified. Multiple such options can be\
            supplied if required. Choices are: mean, median, std, std_rv, min, max,\
            count. Useful for use in scripts. Both std options refer to the\
            unbiased (sample) standard deviation. For complex data, min, max and\
            std are calculated separately for real and imaginary parts, std_rv is\
            based on the real valued variance (equals sqrt of sum of variances of\
            imaginary and real parts).
        mask: only perform computation within the specified binary mask image.
        ignorezero: ignore zero values during statistics calculation.
        allvolumes: generate statistics across all image volumes, rather than\
            one set of statistics per image volume.
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
        NamedTuple of outputs (described in `MrstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRSTATS_METADATA)
    params = mrstats_params(output=output, mask=mask, ignorezero=ignorezero, allvolumes=allvolumes, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, image=image)
    return mrstats_execute(params, execution)


__all__ = [
    "MRSTATS_METADATA",
    "mrstats",
    "mrstats_config_params",
    "mrstats_output_params",
    "mrstats_params",
]
