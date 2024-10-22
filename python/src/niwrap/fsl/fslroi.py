# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLROI_METADATA = Metadata(
    id="00e29bb44c1bad43dabef44ccab4fb8493d655dc.boutiques",
    name="fslroi",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslroiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslroi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the extracted ROI"""


def fslroi(
    infile: InputPathType,
    outfile: str,
    xmin: float | None = None,
    xsize: float | None = None,
    ymin: float | None = None,
    ysize: float | None = None,
    zmin: float | None = None,
    zsize: float | None = None,
    tmin: float | None = None,
    tsize: float | None = None,
    runner: Runner | None = None,
) -> FslroiOutputs:
    """
    Extracts a region of interest (ROI) from an image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input image file.
        outfile: Output image file.
        xmin: Minimum X coordinate for ROI (indexing starts at 0).
        xsize: Size of the ROI in X direction.
        ymin: Minimum Y coordinate for ROI (indexing starts at 0).
        ysize: Size of the ROI in Y direction.
        zmin: Minimum Z coordinate for ROI (indexing starts at 0).
        zsize: Size of the ROI in Z direction.
        tmin: Minimum T coordinate for ROI (indexing starts at 0).
        tsize: Size of the ROI in T direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslroiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLROI_METADATA)
    cargs = []
    cargs.append("fslroi")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if xmin is not None:
        cargs.append(str(xmin))
    if xsize is not None:
        cargs.append(str(xsize))
    if ymin is not None:
        cargs.append(str(ymin))
    if ysize is not None:
        cargs.append(str(ysize))
    if zmin is not None:
        cargs.append(str(zmin))
    if zsize is not None:
        cargs.append(str(zsize))
    if tmin is not None:
        cargs.append(str(tmin))
    if tsize is not None:
        cargs.append(str(tsize))
    ret = FslroiOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLROI_METADATA",
    "FslroiOutputs",
    "fslroi",
]
