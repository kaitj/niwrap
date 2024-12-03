# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLMATHS_FSL_METADATA = Metadata(
    id="1ba348f3e9fa1acbe3b64d58f1387f609d1c083e.boutiques",
    name="fslmaths.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FslmathsFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmaths_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The resultant output image after applying the specified operations."""


def fslmaths_fsl(
    first_input: InputPathType,
    operations_and_inputs: str,
    output_image: str,
    runner: Runner | None = None,
) -> FslmathsFslOutputs:
    """
    FSLmaths: part of FMRIB Software Library (FSL) for manipulating images via
    various mathematical operations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        first_input: First input image for fslmaths operations.
        operations_and_inputs: Operations and inputs to be applied on the first\
            image.
        output_image: Output image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmathsFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLMATHS_FSL_METADATA)
    cargs = []
    cargs.append("fslmaths")
    cargs.append(execution.input_file(first_input))
    cargs.append(operations_and_inputs)
    cargs.append(output_image)
    ret = FslmathsFslOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_image + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMATHS_FSL_METADATA",
    "FslmathsFslOutputs",
    "fslmaths_fsl",
]