# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_GETROW_METADATA = Metadata(
    id="a77775fc37289c2c570d66e31819c1456ad4a367.boutiques",
    name="3dGetrow",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dGetrowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_getrow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output .1D ASCII file"""


def v_3d_getrow(
    xrow: list[int] | None = None,
    yrow: list[int] | None = None,
    zrow: list[int] | None = None,
    input_file: InputPathType | None = None,
    output_file: str | None = None,
    runner: Runner | None = None,
) -> V3dGetrowOutputs:
    """
    Program to extract 1 row from a dataset and write it as a .1D file.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dGetrow.html
    
    Args:
        xrow: Extract row along the x-direction at fixed y-index of j and fixed\
            z-index of k.
        yrow: Extract row along the y-direction at fixed x-index of i and fixed\
            z-index of k.
        zrow: Extract row along the z-direction at fixed x-index of i and fixed\
            y-index of j.
        input_file: Read input from dataset 'ddd' (instead of putting dataset\
            name at end of command line).
        output_file: Filename for output .1D ASCII file will be 'ff' (if 'ff'\
            is '-', then output is to stdout, the default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGetrowOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GETROW_METADATA)
    cargs = []
    cargs.append("3dGetrow")
    if xrow is not None:
        cargs.extend([
            "-xrow",
            *map(str, xrow)
        ])
    if yrow is not None:
        cargs.extend([
            "-yrow",
            *map(str, yrow)
        ])
    if zrow is not None:
        cargs.extend([
            "-zrow",
            *map(str, zrow)
        ])
    if input_file is not None:
        cargs.extend([
            "-input",
            execution.input_file(input_file)
        ])
    if output_file is not None:
        cargs.extend([
            "-output",
            output_file
        ])
    ret = V3dGetrowOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(output_file + ".1D") if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dGetrowOutputs",
    "V_3D_GETROW_METADATA",
    "v_3d_getrow",
]
