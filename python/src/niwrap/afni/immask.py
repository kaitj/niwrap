# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMMASK_METADATA = Metadata(
    id="86504f652c99d44226f59ecf6081fc213a1b97e4.boutiques",
    name="immask",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImmaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `immask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Masked output image"""


def immask(
    input_image: InputPathType,
    output_image: str,
    threshold: float | None = None,
    mask_image: InputPathType | None = None,
    positive_only: bool = False,
    runner: Runner | None = None,
) -> ImmaskOutputs:
    """
    Masks the input image based on specified criteria and produces the output image.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/immask.html
    
    Args:
        input_image: Input image to be masked.
        output_image: Output image after masking.
        threshold: Threshold value; all pixels with absolute value below this\
            will be set to zero in the output image.
        mask_image: Mask image; only locations that are nonzero in the mask\
            image will be nonzero in the output image.
        positive_only: Use only positive pixels from input image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImmaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMMASK_METADATA)
    cargs = []
    cargs.append("immask")
    if threshold is not None:
        cargs.extend([
            "-thresh",
            str(threshold)
        ])
    if mask_image is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask_image)
        ])
    if positive_only:
        cargs.append("-pos")
    cargs.append(execution.input_file(input_image))
    cargs.append(output_image)
    ret = ImmaskOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMMASK_METADATA",
    "ImmaskOutputs",
    "immask",
]
