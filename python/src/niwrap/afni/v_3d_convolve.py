# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_CONVOLVE_METADATA = Metadata(
    id="d8440d19a16dca77c6727e625001c56a872d31dc.boutiques",
    name="3dConvolve",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dConvolveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_convolve(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Main output file of 3dConvolve"""


def v_3d_convolve(
    infile: InputPathType,
    outfile: str,
    options: str | None = None,
    runner: Runner | None = None,
) -> V3dConvolveOutputs:
    """
    3dConvolve is no longer supported in AFNI.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dConvolve.html
    
    Args:
        infile: Input file for 3dConvolve.
        outfile: Output file for 3dConvolve.
        options: Additional options for 3dConvolve.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dConvolveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CONVOLVE_METADATA)
    cargs = []
    cargs.append("3dConvolve")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if options is not None:
        cargs.extend([
            "-options",
            options
        ])
    ret = V3dConvolveOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dConvolveOutputs",
    "V_3D_CONVOLVE_METADATA",
    "v_3d_convolve",
]
