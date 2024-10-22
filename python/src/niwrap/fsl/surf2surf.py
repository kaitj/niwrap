# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF2SURF_METADATA = Metadata(
    id="f04d013a8dfed9725f2aa61d23bdd94cecf6db6c.boutiques",
    name="surf2surf",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class Surf2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surf2surf(
    input_surface: InputPathType,
    output_surface: InputPathType,
    input_convention: str | None = None,
    output_convention: str | None = None,
    input_ref_volume: InputPathType | None = None,
    output_ref_volume: InputPathType | None = None,
    transform: InputPathType | None = None,
    output_type: str | None = None,
    output_values: str | None = None,
    runner: Runner | None = None,
) -> Surf2surfOutputs:
    """
    Conversions between surface formats and/or conventions.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_surface: Input surface.
        output_surface: Output surface.
        input_convention: Input convention [default=caret] - only used if\
            output convention is different.
        output_convention: Output convention [default=same as input].
        input_ref_volume: Input reference volume - Must set this if changing\
            conventions.
        output_ref_volume: Output reference volume [default=same as input].
        transform: In-to-out ASCII matrix or out-to-in warpfield\
            [default=identity].
        output_type: Output type: ASCII, VTK, GIFTI_ASCII, GIFTI_BIN,\
            GIFTI_BIN_GZ (default).
        output_values: Set output scalar values (e.g.\
            --values=mysurface.func.gii or --values=1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Surf2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF2SURF_METADATA)
    cargs = []
    cargs.append("surf2surf")
    cargs.append("-i")
    cargs.extend([
        "--surfin",
        execution.input_file(input_surface)
    ])
    cargs.append("-o")
    cargs.extend([
        "--surfout",
        execution.input_file(output_surface)
    ])
    if input_convention is not None:
        cargs.extend([
            "--convin",
            input_convention
        ])
    if output_convention is not None:
        cargs.extend([
            "--convout",
            output_convention
        ])
    if input_ref_volume is not None:
        cargs.extend([
            "--volin",
            execution.input_file(input_ref_volume)
        ])
    if output_ref_volume is not None:
        cargs.extend([
            "--volout",
            execution.input_file(output_ref_volume)
        ])
    if transform is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(transform)
        ])
    if output_type is not None:
        cargs.extend([
            "--outputtype",
            output_type
        ])
    if output_values is not None:
        cargs.extend([
            "--values",
            output_values
        ])
    ret = Surf2surfOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF2SURF_METADATA",
    "Surf2surfOutputs",
    "surf2surf",
]
