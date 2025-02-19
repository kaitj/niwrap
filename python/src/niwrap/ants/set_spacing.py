# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SET_SPACING_METADATA = Metadata(
    id="5a66a083de7d100e80817b6862541b3b2eb2b1ed.boutiques",
    name="SetSpacing",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SetSpacingParameters = typing.TypedDict('SetSpacingParameters', {
    "__STYX_TYPE__": typing.Literal["SetSpacing"],
    "dimension": int,
    "input_file": InputPathType,
    "output_file": str,
    "spacing": list[float],
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
        "SetSpacing": set_spacing_cargs,
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
        "SetSpacing": set_spacing_outputs,
    }.get(t)


class SetSpacingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_spacing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """The output image with the specified spacing."""


def set_spacing_params(
    dimension: int,
    input_file: InputPathType,
    output_file: str,
    spacing: list[float],
) -> SetSpacingParameters:
    """
    Build parameters.
    
    Args:
        dimension: The dimensionality of the image (e.g., 2 or 3).
        input_file: The input image file in HDR format.
        output_file: The output image file in NII format.
        spacing: Spacing values for each dimension. Requires SpacingX,\
            SpacingY, and optionally SpacingZ.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SetSpacing",
        "dimension": dimension,
        "input_file": input_file,
        "output_file": output_file,
        "spacing": spacing,
    }
    return params


def set_spacing_cargs(
    params: SetSpacingParameters,
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
    cargs.append("SetSpacing")
    cargs.append(str(params.get("dimension")))
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    cargs.extend(map(str, params.get("spacing")))
    return cargs


def set_spacing_outputs(
    params: SetSpacingParameters,
    execution: Execution,
) -> SetSpacingOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SetSpacingOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_file")),
    )
    return ret


def set_spacing_execute(
    params: SetSpacingParameters,
    execution: Execution,
) -> SetSpacingOutputs:
    """
    A tool to set the spacing of an image in each dimension.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SetSpacingOutputs`).
    """
    params = execution.params(params)
    cargs = set_spacing_cargs(params, execution)
    ret = set_spacing_outputs(params, execution)
    execution.run(cargs)
    return ret


def set_spacing(
    dimension: int,
    input_file: InputPathType,
    output_file: str,
    spacing: list[float],
    runner: Runner | None = None,
) -> SetSpacingOutputs:
    """
    A tool to set the spacing of an image in each dimension.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimension: The dimensionality of the image (e.g., 2 or 3).
        input_file: The input image file in HDR format.
        output_file: The output image file in NII format.
        spacing: Spacing values for each dimension. Requires SpacingX,\
            SpacingY, and optionally SpacingZ.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SetSpacingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SET_SPACING_METADATA)
    params = set_spacing_params(dimension=dimension, input_file=input_file, output_file=output_file, spacing=spacing)
    return set_spacing_execute(params, execution)


__all__ = [
    "SET_SPACING_METADATA",
    "SetSpacingOutputs",
    "SetSpacingParameters",
    "set_spacing",
    "set_spacing_params",
]
