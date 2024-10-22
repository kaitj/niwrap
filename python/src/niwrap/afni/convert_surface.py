# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_SURFACE_METADATA = Metadata(
    id="0c666db0cc394b6bd84fde9a52f4bed0c71ffdd6.boutiques",
    name="ConvertSurface",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ConvertSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """The converted output surface file."""


def convert_surface(
    input_surface: str,
    output_surface: str,
    surface_volume: str | None = None,
    transform_tlrc: bool = False,
    mni_lpi: bool = False,
    ixmat_1_d: str | None = None,
    native: bool = False,
    runner: Runner | None = None,
) -> ConvertSurfaceOutputs:
    """
    Reads in a surface and writes it out in another format. Only fields pertinent to
    SUMA are preserved.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_surface: Specifies the input surface.
        output_surface: Specifies the output surface.
        surface_volume: Specifies a surface volume.
        transform_tlrc: Apply Talairach transform.
        mni_lpi: Turn AFNI tlrc coordinates (RAI) into MNI coord space in LPI.
        ixmat_1_d: Apply inverse transformation specified in 1D file.
        native: Write the output surface in the coordinate system native to its\
            format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_SURFACE_METADATA)
    cargs = []
    cargs.append("ConvertSurface")
    cargs.extend([
        "-i",
        input_surface
    ])
    cargs.extend([
        "-o",
        output_surface
    ])
    if surface_volume is not None:
        cargs.extend([
            "-sv",
            surface_volume
        ])
    if transform_tlrc:
        cargs.append("-tlrc")
    if mni_lpi:
        cargs.append("-MNI_lpi")
    if ixmat_1_d is not None:
        cargs.extend([
            "-ixmat_1D",
            ixmat_1_d
        ])
    if native:
        cargs.append("-native")
    ret = ConvertSurfaceOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(output_surface),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_SURFACE_METADATA",
    "ConvertSurfaceOutputs",
    "convert_surface",
]
