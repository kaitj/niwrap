# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_REPOSITION_SURFACE_METADATA = Metadata(
    id="41b35ee93a58eac699b67d7d488cbcc2df5c677b.boutiques",
    name="mris_reposition_surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisRepositionSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_reposition_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType
    """Output surface file"""


def mris_reposition_surface(
    surf: InputPathType,
    volume: InputPathType,
    points: InputPathType,
    output: str,
    size: float | None = 1,
    sigma: float | None = 2.0,
    iterations: float | None = 1,
    runner: Runner | None = None,
) -> MrisRepositionSurfaceOutputs:
    """
    Reposition a surface based on the given control points (in JSON format).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf: Input surface.
        volume: Input volume.
        points: Input points.
        output: Output surface filename.
        size: Size parameter for repositioning. Default is 1.
        sigma: Sigma. Default is 2.0.
        iterations: Number of iterations. Default is 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRepositionSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REPOSITION_SURFACE_METADATA)
    cargs = []
    cargs.append("mris_reposition_surface")
    cargs.extend([
        "-s",
        execution.input_file(surf)
    ])
    cargs.extend([
        "-v",
        execution.input_file(volume)
    ])
    cargs.extend([
        "-p",
        execution.input_file(points)
    ])
    cargs.extend([
        "-o",
        output
    ])
    if size is not None:
        cargs.extend([
            "-z",
            str(size)
        ])
    if sigma is not None:
        cargs.extend([
            "-g",
            str(sigma)
        ])
    if iterations is not None:
        cargs.extend([
            "-i",
            str(iterations)
        ])
    ret = MrisRepositionSurfaceOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_REPOSITION_SURFACE_METADATA",
    "MrisRepositionSurfaceOutputs",
    "mris_reposition_surface",
]
