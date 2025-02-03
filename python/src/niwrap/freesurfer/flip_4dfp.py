# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FLIP_4DFP_METADATA = Metadata(
    id="546744c4be37b8dfd459146df7ba1a0232818b0d.boutiques",
    name="flip_4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Flip4dfpParameters = typing.TypedDict('Flip4dfpParameters', {
    "__STYX_TYPE__": typing.Literal["flip_4dfp"],
    "input_image": InputPathType,
    "output_image": typing.NotRequired[str | None],
    "flip_x": bool,
    "flip_y": bool,
    "flip_z": bool,
    "endianness": typing.NotRequired[typing.Literal["b", "l"] | None],
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
        "flip_4dfp": flip_4dfp_cargs,
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
        "flip_4dfp": flip_4dfp_outputs,
    }
    return vt.get(t)


class Flip4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flip_4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    flipped_image: OutputPathType | None
    """Flipped output 4dfp image"""


def flip_4dfp_params(
    input_image: InputPathType,
    output_image: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    endianness: typing.Literal["b", "l"] | None = None,
) -> Flip4dfpParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input 4dfp image file.
        output_image: Output 4dfp image file. Default is input image root with\
            '_flip' suffix.
        flip_x: Flip along x-axis.
        flip_y: Flip along y-axis.
        flip_z: Flip along z-axis.
        endianness: Specify output endianness: 'b' for big endian, 'l' for\
            little endian. Default is input endianness.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "flip_4dfp",
        "input_image": input_image,
        "flip_x": flip_x,
        "flip_y": flip_y,
        "flip_z": flip_z,
    }
    if output_image is not None:
        params["output_image"] = output_image
    if endianness is not None:
        params["endianness"] = endianness
    return params


def flip_4dfp_cargs(
    params: Flip4dfpParameters,
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
    cargs.append("flip_4dfp")
    cargs.append(execution.input_file(params.get("input_image")))
    if params.get("output_image") is not None:
        cargs.append(params.get("output_image"))
    if params.get("flip_x"):
        cargs.append("-x")
    if params.get("flip_y"):
        cargs.append("-y")
    if params.get("flip_z"):
        cargs.append("-z")
    if params.get("endianness") is not None:
        cargs.extend([
            "-@",
            params.get("endianness")
        ])
    return cargs


def flip_4dfp_outputs(
    params: Flip4dfpParameters,
    execution: Execution,
) -> Flip4dfpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Flip4dfpOutputs(
        root=execution.output_file("."),
        flipped_image=execution.output_file(params.get("output_image") + ".4dfp.img") if (params.get("output_image") is not None) else None,
    )
    return ret


def flip_4dfp_execute(
    params: Flip4dfpParameters,
    execution: Execution,
) -> Flip4dfpOutputs:
    """
    A tool to flip 4dfp images along specified axes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Flip4dfpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = flip_4dfp_cargs(params, execution)
    ret = flip_4dfp_outputs(params, execution)
    execution.run(cargs)
    return ret


def flip_4dfp(
    input_image: InputPathType,
    output_image: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    endianness: typing.Literal["b", "l"] | None = None,
    runner: Runner | None = None,
) -> Flip4dfpOutputs:
    """
    A tool to flip 4dfp images along specified axes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input 4dfp image file.
        output_image: Output 4dfp image file. Default is input image root with\
            '_flip' suffix.
        flip_x: Flip along x-axis.
        flip_y: Flip along y-axis.
        flip_z: Flip along z-axis.
        endianness: Specify output endianness: 'b' for big endian, 'l' for\
            little endian. Default is input endianness.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Flip4dfpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIP_4DFP_METADATA)
    params = flip_4dfp_params(input_image=input_image, output_image=output_image, flip_x=flip_x, flip_y=flip_y, flip_z=flip_z, endianness=endianness)
    return flip_4dfp_execute(params, execution)


__all__ = [
    "FLIP_4DFP_METADATA",
    "Flip4dfpOutputs",
    "flip_4dfp",
    "flip_4dfp_params",
]
