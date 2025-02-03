# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKCONVERT_METADATA = Metadata(
    id="e099f163628c4f4e1f744a964fec71d2c4cd255c.boutiques",
    name="tckconvert",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
TckconvertConfigParameters = typing.TypedDict('TckconvertConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
TckconvertVariousStringParameters = typing.TypedDict('TckconvertVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
TckconvertVariousFileParameters = typing.TypedDict('TckconvertVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
TckconvertParameters = typing.TypedDict('TckconvertParameters', {
    "__STYX_TYPE__": typing.Literal["tckconvert"],
    "scanner2voxel": typing.NotRequired[InputPathType | None],
    "scanner2image": typing.NotRequired[InputPathType | None],
    "voxel2scanner": typing.NotRequired[InputPathType | None],
    "image2scanner": typing.NotRequired[InputPathType | None],
    "sides": typing.NotRequired[int | None],
    "increment": typing.NotRequired[int | None],
    "dec": bool,
    "radius": typing.NotRequired[float | None],
    "ascii": bool,
    "binary": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TckconvertConfigParameters] | None],
    "help": bool,
    "version": bool,
    "input": typing.Union[TckconvertVariousStringParameters, TckconvertVariousFileParameters],
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
        "tckconvert": tckconvert_cargs,
        "config": tckconvert_config_cargs,
        "VariousString": tckconvert_various_string_cargs,
        "VariousFile": tckconvert_various_file_cargs,
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
        "tckconvert": tckconvert_outputs,
    }
    return vt.get(t)


def tckconvert_config_params(
    key: str,
    value: str,
) -> TckconvertConfigParameters:
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


def tckconvert_config_cargs(
    params: TckconvertConfigParameters,
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


def tckconvert_various_string_params(
    obj: str,
) -> TckconvertVariousStringParameters:
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


def tckconvert_various_string_cargs(
    params: TckconvertVariousStringParameters,
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


def tckconvert_various_file_params(
    obj: InputPathType,
) -> TckconvertVariousFileParameters:
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


def tckconvert_various_file_cargs(
    params: TckconvertVariousFileParameters,
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


class TckconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track file."""


def tckconvert_params(
    input_: typing.Union[TckconvertVariousStringParameters, TckconvertVariousFileParameters],
    output: str,
    scanner2voxel: InputPathType | None = None,
    scanner2image: InputPathType | None = None,
    voxel2scanner: InputPathType | None = None,
    image2scanner: InputPathType | None = None,
    sides: int | None = None,
    increment: int | None = None,
    dec: bool = False,
    radius: float | None = None,
    ascii_: bool = False,
    binary: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TckconvertParameters:
    """
    Build parameters.
    
    Args:
        input_: the input track file.
        output: the output track file.
        scanner2voxel: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            voxel coordinates.
        scanner2image: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            image coordinates (in mm).
        voxel2scanner: if specified, the properties of this image will be used\
            to convert track point positions from voxel coordinates into real\
            (scanner) coordinates.
        image2scanner: if specified, the properties of this image will be used\
            to convert track point positions from image coordinates (in mm) into\
            real (scanner) coordinates.
        sides: number of sides for streamlines.
        increment: generate streamline points at every (increment) points.
        dec: add DEC as a primvar.
        radius: radius of the streamlines.
        ascii_: write an ASCII VTK file (this is the default).
        binary: write a binary VTK file.
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
        "__STYXTYPE__": "tckconvert",
        "dec": dec,
        "ascii": ascii_,
        "binary": binary,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "input": input_,
        "output": output,
    }
    if scanner2voxel is not None:
        params["scanner2voxel"] = scanner2voxel
    if scanner2image is not None:
        params["scanner2image"] = scanner2image
    if voxel2scanner is not None:
        params["voxel2scanner"] = voxel2scanner
    if image2scanner is not None:
        params["image2scanner"] = image2scanner
    if sides is not None:
        params["sides"] = sides
    if increment is not None:
        params["increment"] = increment
    if radius is not None:
        params["radius"] = radius
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tckconvert_cargs(
    params: TckconvertParameters,
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
    cargs.append("tckconvert")
    if params.get("scanner2voxel") is not None:
        cargs.extend([
            "-scanner2voxel",
            execution.input_file(params.get("scanner2voxel"))
        ])
    if params.get("scanner2image") is not None:
        cargs.extend([
            "-scanner2image",
            execution.input_file(params.get("scanner2image"))
        ])
    if params.get("voxel2scanner") is not None:
        cargs.extend([
            "-voxel2scanner",
            execution.input_file(params.get("voxel2scanner"))
        ])
    if params.get("image2scanner") is not None:
        cargs.extend([
            "-image2scanner",
            execution.input_file(params.get("image2scanner"))
        ])
    if params.get("sides") is not None:
        cargs.extend([
            "-sides",
            str(params.get("sides"))
        ])
    if params.get("increment") is not None:
        cargs.extend([
            "-increment",
            str(params.get("increment"))
        ])
    if params.get("dec"):
        cargs.append("-dec")
    if params.get("radius") is not None:
        cargs.extend([
            "-radius",
            str(params.get("radius"))
        ])
    if params.get("ascii"):
        cargs.append("-ascii")
    if params.get("binary"):
        cargs.append("-binary")
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
    cargs.extend(dyn_cargs(params.get("input")["__STYXTYPE__"])(params.get("input"), execution))
    cargs.append(params.get("output"))
    return cargs


def tckconvert_outputs(
    params: TckconvertParameters,
    execution: Execution,
) -> TckconvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TckconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def tckconvert_execute(
    params: TckconvertParameters,
    execution: Execution,
) -> TckconvertOutputs:
    """
    Convert between different track file formats.
    
    The program currently supports MRtrix .tck files (input/output), ascii text
    files (input/output), VTK polydata files (input/output), and RenderMan RIB
    (export only).
    
    Note that ascii files will be stored with one streamline per numbered file.
    To support this, the command will use the multi-file numbering syntax, where
    square brackets denote the position of the numbering for the files, for
    example:
    
    $ tckconvert input.tck output-'[]'.txt
    
    will produce files named output-0000.txt, output-0001.txt, output-0002.txt,
    ...
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TckconvertOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tckconvert_cargs(params, execution)
    ret = tckconvert_outputs(params, execution)
    execution.run(cargs)
    return ret


def tckconvert(
    input_: typing.Union[TckconvertVariousStringParameters, TckconvertVariousFileParameters],
    output: str,
    scanner2voxel: InputPathType | None = None,
    scanner2image: InputPathType | None = None,
    voxel2scanner: InputPathType | None = None,
    image2scanner: InputPathType | None = None,
    sides: int | None = None,
    increment: int | None = None,
    dec: bool = False,
    radius: float | None = None,
    ascii_: bool = False,
    binary: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckconvertConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckconvertOutputs:
    """
    Convert between different track file formats.
    
    The program currently supports MRtrix .tck files (input/output), ascii text
    files (input/output), VTK polydata files (input/output), and RenderMan RIB
    (export only).
    
    Note that ascii files will be stored with one streamline per numbered file.
    To support this, the command will use the multi-file numbering syntax, where
    square brackets denote the position of the numbering for the files, for
    example:
    
    $ tckconvert input.tck output-'[]'.txt
    
    will produce files named output-0000.txt, output-0001.txt, output-0002.txt,
    ...
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: the input track file.
        output: the output track file.
        scanner2voxel: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            voxel coordinates.
        scanner2image: if specified, the properties of this image will be used\
            to convert track point positions from real (scanner) coordinates into\
            image coordinates (in mm).
        voxel2scanner: if specified, the properties of this image will be used\
            to convert track point positions from voxel coordinates into real\
            (scanner) coordinates.
        image2scanner: if specified, the properties of this image will be used\
            to convert track point positions from image coordinates (in mm) into\
            real (scanner) coordinates.
        sides: number of sides for streamlines.
        increment: generate streamline points at every (increment) points.
        dec: add DEC as a primvar.
        radius: radius of the streamlines.
        ascii_: write an ASCII VTK file (this is the default).
        binary: write a binary VTK file.
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
        NamedTuple of outputs (described in `TckconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKCONVERT_METADATA)
    params = tckconvert_params(scanner2voxel=scanner2voxel, scanner2image=scanner2image, voxel2scanner=voxel2scanner, image2scanner=image2scanner, sides=sides, increment=increment, dec=dec, radius=radius, ascii_=ascii_, binary=binary, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, input_=input_, output=output)
    return tckconvert_execute(params, execution)


__all__ = [
    "TCKCONVERT_METADATA",
    "TckconvertOutputs",
    "tckconvert",
    "tckconvert_config_params",
    "tckconvert_params",
    "tckconvert_various_file_params",
    "tckconvert_various_string_params",
]
