# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SHCONV_METADATA = Metadata(
    id="3c84c5743ea66d880048dc5dc975db440966a75e.boutiques",
    name="shconv",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
ShconvVariousStringParameters = typing.TypedDict('ShconvVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
ShconvVariousFileParameters = typing.TypedDict('ShconvVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
ShconvConfigParameters = typing.TypedDict('ShconvConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
ShconvParameters = typing.TypedDict('ShconvParameters', {
    "__STYX_TYPE__": typing.Literal["shconv"],
    "datatype": typing.NotRequired[str | None],
    "strides": typing.NotRequired[typing.Union[ShconvVariousStringParameters, ShconvVariousFileParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[ShconvConfigParameters] | None],
    "help": bool,
    "version": bool,
    "odf_response": list[str],
    "SH_out": str,
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
        "shconv": shconv_cargs,
        "VariousString": shconv_various_string_cargs,
        "VariousFile": shconv_various_file_cargs,
        "config": shconv_config_cargs,
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
        "shconv": shconv_outputs,
    }.get(t)


def shconv_various_string_params(
    obj: str,
) -> ShconvVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def shconv_various_string_cargs(
    params: ShconvVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def shconv_various_file_params(
    obj: InputPathType,
) -> ShconvVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def shconv_various_file_cargs(
    params: ShconvVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def shconv_config_params(
    key: str,
    value: str,
) -> ShconvConfigParameters:
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


def shconv_config_cargs(
    params: ShconvConfigParameters,
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


class ShconvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `shconv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sh_out: OutputPathType
    """the output spherical harmonics coefficients image."""


def shconv_params(
    odf_response: list[str],
    sh_out: str,
    datatype: str | None = None,
    strides: typing.Union[ShconvVariousStringParameters, ShconvVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[ShconvConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> ShconvParameters:
    """
    Build parameters.
    
    Args:
        odf_response: pairs of input ODF image and corresponding responses.
        sh_out: the output spherical harmonics coefficients image.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
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
        "__STYXTYPE__": "shconv",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "odf_response": odf_response,
        "SH_out": sh_out,
    }
    if datatype is not None:
        params["datatype"] = datatype
    if strides is not None:
        params["strides"] = strides
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def shconv_cargs(
    params: ShconvParameters,
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
    cargs.append("shconv")
    if params.get("datatype") is not None:
        cargs.extend([
            "-datatype",
            params.get("datatype")
        ])
    if params.get("strides") is not None:
        cargs.extend([
            "-strides",
            *dyn_cargs(params.get("strides")["__STYXTYPE__"])(params.get("strides"), execution)
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
    cargs.extend(params.get("odf_response"))
    cargs.append(params.get("SH_out"))
    return cargs


def shconv_outputs(
    params: ShconvParameters,
    execution: Execution,
) -> ShconvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ShconvOutputs(
        root=execution.output_file("."),
        sh_out=execution.output_file(params.get("SH_out")),
    )
    return ret


def shconv_execute(
    params: ShconvParameters,
    execution: Execution,
) -> ShconvOutputs:
    """
    Perform spherical convolution.
    
    Provided with matching pairs of response function and ODF images (containing
    SH coefficients), perform spherical convolution to provide the corresponding
    SH coefficients of the signal.
    
    If multiple pairs of inputs are provided, their contributions will be summed
    into a single output.
    
    If the responses are multi-shell (with one line of coefficients per shell),
    the output will be a 5-dimensional image, with the SH coefficients of the
    signal in each shell stored at different indices along the 5th dimension.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ShconvOutputs`).
    """
    params = execution.params(params)
    cargs = shconv_cargs(params, execution)
    ret = shconv_outputs(params, execution)
    execution.run(cargs)
    return ret


def shconv(
    odf_response: list[str],
    sh_out: str,
    datatype: str | None = None,
    strides: typing.Union[ShconvVariousStringParameters, ShconvVariousFileParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[ShconvConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> ShconvOutputs:
    """
    Perform spherical convolution.
    
    Provided with matching pairs of response function and ODF images (containing
    SH coefficients), perform spherical convolution to provide the corresponding
    SH coefficients of the signal.
    
    If multiple pairs of inputs are provided, their contributions will be summed
    into a single output.
    
    If the responses are multi-shell (with one line of coefficients per shell),
    the output will be a 5-dimensional image, with the SH coefficients of the
    signal in each shell stored at different indices along the 5th dimension.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        odf_response: pairs of input ODF image and corresponding responses.
        sh_out: the output spherical harmonics coefficients image.
        datatype: specify output image data type. Valid choices are: float32,\
            float32le, float32be, float64, float64le, float64be, int64, uint64,\
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,\
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,\
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,\
            int8, uint8, bit.
        strides: specify the strides of the output data in memory; either as a\
            comma-separated list of (signed) integers, or as a template image from\
            which the strides shall be extracted and used. The actual strides\
            produced will depend on whether the output image format can support it.
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
        NamedTuple of outputs (described in `ShconvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SHCONV_METADATA)
    params = shconv_params(datatype=datatype, strides=strides, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, odf_response=odf_response, sh_out=sh_out)
    return shconv_execute(params, execution)


__all__ = [
    "SHCONV_METADATA",
    "ShconvConfigParameters",
    "ShconvOutputs",
    "ShconvParameters",
    "ShconvVariousFileParameters",
    "ShconvVariousStringParameters",
    "shconv",
    "shconv_config_params",
    "shconv_params",
    "shconv_various_file_params",
    "shconv_various_string_params",
]
