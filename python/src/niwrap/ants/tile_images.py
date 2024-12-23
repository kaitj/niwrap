# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TILE_IMAGES_METADATA = Metadata(
    id="11f704401de392cf34f685f833e7073a2d69b714.boutiques",
    name="TileImages",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class TileImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tile_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tiled_image: OutputPathType
    """The final tiled output image."""


def tile_images(
    image_dimension: int,
    output_image: InputPathType,
    layout: str,
    input_images: list[InputPathType],
    runner: Runner | None = None,
) -> TileImagesOutputs:
    """
    TileImages allows assembling images into a multi-dimensional array, producing a
    single output image. The input images must have a dimension less than or equal
    to the specified output image dimension.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimensionality of the output image.
        output_image: The path for the output tiled image.
        layout: Defines the structure of the tiled output image. The layout\
            dictates the number and arrangement of input images in the output\
            image.
        input_images: Input images to be tiled into the output image. The\
            number of input images should match the layout specification.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TileImagesOutputs`).
    """
    if not (1 <= len(input_images)): 
        raise ValueError(f"Length of 'input_images' must be greater than 1 but was {len(input_images)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(TILE_IMAGES_METADATA)
    cargs = []
    cargs.append("TileImages")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(output_image))
    cargs.append(layout)
    cargs.extend([execution.input_file(f) for f in input_images])
    ret = TileImagesOutputs(
        root=execution.output_file("."),
        tiled_image=execution.output_file(pathlib.Path(output_image).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TILE_IMAGES_METADATA",
    "TileImagesOutputs",
    "tile_images",
]
