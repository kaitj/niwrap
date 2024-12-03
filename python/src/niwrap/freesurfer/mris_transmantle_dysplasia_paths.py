# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_TRANSMANTLE_DYSPLASIA_PATHS_METADATA = Metadata(
    id="effcf060042c53596ed252e67dbd78f3fd8cbd8e.boutiques",
    name="mris_transmantle_dysplasia_paths",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisTransmantleDysplasiaPathsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_transmantle_dysplasia_paths(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume file"""


def mris_transmantle_dysplasia_paths(
    surface: InputPathType,
    aseg_volume: InputPathType,
    intensity_volume: InputPathType,
    xform: InputPathType,
    output_volume: str,
    filter_: list[float] | None = None,
    noise_sensitivity: bool = False,
    runner: Runner | None = None,
) -> MrisTransmantleDysplasiaPathsOutputs:
    """
    Tool for transmantle dysplasia path computation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Surface file.
        aseg_volume: ASEG volume file.
        intensity_volume: Intensity volume file.
        xform: Transformation file.
        output_volume: Output volume file.
        filter_: Apply specified filter with low and high values (not\
            implemented yet).
        noise_sensitivity: Noise-sensitivity normalize inverse (default=1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisTransmantleDysplasiaPathsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_TRANSMANTLE_DYSPLASIA_PATHS_METADATA)
    cargs = []
    cargs.append("mris_transmantle_dysplasia_paths")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(aseg_volume))
    cargs.append(execution.input_file(intensity_volume))
    cargs.append(execution.input_file(xform))
    cargs.append(output_volume)
    if filter_ is not None:
        cargs.extend([
            "-f",
            *map(str, filter_)
        ])
    if noise_sensitivity:
        cargs.append("-n")
    ret = MrisTransmantleDysplasiaPathsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_TRANSMANTLE_DYSPLASIA_PATHS_METADATA",
    "MrisTransmantleDysplasiaPathsOutputs",
    "mris_transmantle_dysplasia_paths",
]