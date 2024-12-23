# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_FLATTEN_METADATA = Metadata(
    id="c7d351c53d00767efc2edd450d96b67b497b34f9.boutiques",
    name="mris_flatten",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisFlattenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_flatten(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_patch_file: OutputPathType
    """Output flattened surface patch"""


def mris_flatten(
    input_patch: InputPathType,
    output_patch: str,
    iterations: float | None = None,
    distances: list[float] | None = None,
    dilations: float | None = None,
    random_seed: float | None = None,
    copy_coords: str | None = None,
    norand: bool = False,
    runner: Runner | None = None,
) -> MrisFlattenOutputs:
    """
    This program will flatten a surface patch.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_patch: Input surface patch.
        output_patch: Output flattened surface patch.
        iterations: Write out the surface every # of iterations.
        distances: Specify size of neighborhood and number of vertices at each\
            distance to be used in the optimization.
        dilations: Specify the number of times to dilate the ripped edges to\
            ensure a clean cut.
        random_seed: Set the random seed to a specific value so that flattening\
            is repeatable.
        copy_coords: Copy xyz coords from surface before flattening.
        norand: Set the random seed to 0 so that flattening is repeatable.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisFlattenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_FLATTEN_METADATA)
    cargs = []
    cargs.append("mris_flatten")
    cargs.append(execution.input_file(input_patch))
    cargs.append(output_patch)
    if iterations is not None:
        cargs.extend([
            "-w",
            str(iterations)
        ])
    if distances is not None:
        cargs.extend([
            "-distances",
            *map(str, distances)
        ])
    if dilations is not None:
        cargs.extend([
            "-dilate",
            str(dilations)
        ])
    if random_seed is not None:
        cargs.extend([
            "-seed",
            str(random_seed)
        ])
    if copy_coords is not None:
        cargs.extend([
            "-copy-coords",
            copy_coords
        ])
    if norand:
        cargs.append("-norand")
    ret = MrisFlattenOutputs(
        root=execution.output_file("."),
        output_patch_file=execution.output_file(output_patch),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_FLATTEN_METADATA",
    "MrisFlattenOutputs",
    "mris_flatten",
]
