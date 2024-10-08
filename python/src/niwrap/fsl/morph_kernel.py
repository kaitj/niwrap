# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_KERNEL_METADATA = Metadata(
    id="5db7dcc534478f0d7a3d9cd9d56ec7cf51322eb3.boutiques",
    name="morph_kernel",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class MorphKernelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_kernel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    morph_kernel_output: OutputPathType
    """Output morphological kernel file"""


def morph_kernel(
    cube_side_length: float,
    sphere_radius: float,
    runner: Runner | None = None,
) -> MorphKernelOutputs:
    """
    Tool to generate morphological kernels.
    
    Author: Author Name
    
    Args:
        cube_side_length: Side length of the cube (e.g., 11).
        sphere_radius: Radius of the sphere (e.g., 5.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphKernelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_KERNEL_METADATA)
    cargs = []
    cargs.append("morph_kernel")
    cargs.append(str(cube_side_length))
    cargs.append(str(sphere_radius))
    ret = MorphKernelOutputs(
        root=execution.output_file("."),
        morph_kernel_output=execution.output_file("sphere[OUTPUT_PREFIX].ker"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MORPH_KERNEL_METADATA",
    "MorphKernelOutputs",
    "morph_kernel",
]
