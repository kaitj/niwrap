# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCREATEHD_METADATA = Metadata(
    id="a1f23fc21d5b4fa921d24d195e31f974c2ac59d1.boutiques",
    name="fslcreatehd",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslcreatehdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcreatehd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_headerfile: OutputPathType
    """Generated NIfTI header file"""


def fslcreatehd(
    xsize: float,
    ysize: float,
    zsize: float,
    tsize: float,
    xvoxsize: float,
    yvoxsize: float,
    zvoxsize: float,
    tr: float,
    xorigin: float,
    yorigin: float,
    zorigin: float,
    datatype: float,
    headername: str,
    nifti_xml_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> FslcreatehdOutputs:
    """
    Tool to create a new NIfTI header.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        xsize: Size of the image in the x dimension.
        ysize: Size of the image in the y dimension.
        zsize: Size of the image in the z dimension.
        tsize: Size of the image in the t dimension (time).
        xvoxsize: Voxel size in the x dimension.
        yvoxsize: Voxel size in the y dimension.
        zvoxsize: Voxel size in the z dimension.
        tr: Repetition time (TR) of the image.
        xorigin: Origin of the image in the x dimension.
        yorigin: Origin of the image in the y dimension.
        zorigin: Origin of the image in the z dimension.
        datatype: Datatype of the image (2=char, 4=short, 8=int, 16=float,\
            64=double).
        headername: Name of the header file to be created.
        nifti_xml_file: NIfTI XML file describing the header configuration\
            (Mutually exclusive with other inputs).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslcreatehdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCREATEHD_METADATA)
    cargs = []
    cargs.append("fslcreatehd")
    cargs.append(str(xsize))
    cargs.append(str(ysize))
    cargs.append(str(zsize))
    cargs.append(str(tsize))
    cargs.append(str(xvoxsize))
    cargs.append(str(yvoxsize))
    cargs.append(str(zvoxsize))
    cargs.append(str(tr))
    cargs.append(str(xorigin))
    cargs.append(str(yorigin))
    cargs.append(str(zorigin))
    cargs.append(str(datatype))
    cargs.append(headername)
    if nifti_xml_file is not None:
        cargs.append(execution.input_file(nifti_xml_file))
    ret = FslcreatehdOutputs(
        root=execution.output_file("."),
        out_headerfile=execution.output_file(headername + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCREATEHD_METADATA",
    "FslcreatehdOutputs",
    "fslcreatehd",
]
