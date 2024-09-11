# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CJPEG_METADATA = Metadata(
    id="164adf9df19327dd321b88e1cbb7402d667396ef.boutiques",
    name="cjpeg",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class CjpegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cjpeg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """The output JPEG file"""


def cjpeg(
    outfile: str,
    infile: InputPathType,
    quality: float | None = None,
    grayscale: bool = False,
    optimize: bool = False,
    baseline: bool = False,
    progressive: bool = False,
    runner: Runner | None = None,
) -> CjpegOutputs:
    """
    Compresses an image file to a JPEG file.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/cjpeg.html
    
    Args:
        outfile: Output JPEG file.
        infile: Input image file.
        quality: Quality of JPEG image (0-100).
        grayscale: Create a grayscale JPEG file.
        optimize: Optimize Huffman table.
        baseline: Create a baseline JPEG file.
        progressive: Create a progressive JPEG file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CjpegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CJPEG_METADATA)
    cargs = []
    cargs.append("cjpeg")
    if quality is not None:
        cargs.extend([
            "-quality",
            str(quality)
        ])
    if grayscale:
        cargs.append("-grayscale")
    if optimize:
        cargs.append("-optimize")
    if baseline:
        cargs.append("-baseline")
    if progressive:
        cargs.append("-progressive")
    cargs.append(outfile)
    cargs.append(execution.input_file(infile))
    ret = CjpegOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CJPEG_METADATA",
    "CjpegOutputs",
    "cjpeg",
]