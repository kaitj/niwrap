# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SET_SPACING_METADATA = Metadata(
    id="5a66a083de7d100e80817b6862541b3b2eb2b1ed.boutiques",
    name="SetSpacing",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class SetSpacingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_spacing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """The output image with the specified spacing."""


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
    cargs = []
    cargs.append("SetSpacing")
    cargs.append(str(dimension))
    cargs.append(execution.input_file(input_file))
    cargs.append(output_file)
    cargs.extend(map(str, spacing))
    ret = SetSpacingOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SET_SPACING_METADATA",
    "SetSpacingOutputs",
    "set_spacing",
]
