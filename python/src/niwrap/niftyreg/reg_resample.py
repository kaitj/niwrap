# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_RESAMPLE_METADATA = Metadata(
    id="50f0da9e2bc6ab8122fa0747723f0f1cd6f03dbc.boutiques",
    name="reg_resample",
    package="niftyreg",
)


class RegResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_resampled_image: OutputPathType
    """File containing the resampled image"""
    output_resampled_blank: OutputPathType
    """File containing the resampled blank grid"""


def reg_resample(
    reference_image: InputPathType,
    floating_image: InputPathType,
    runner: Runner | None = None,
) -> RegResampleOutputs:
    """
    Tool for resampling floating images to the reference image space using different
    transformations.
    
    Author: Marc Modat
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_RESAMPLE_METADATA)
    cargs = []
    cargs.append("reg_resample")
    cargs.extend([
        "-ref",
        execution.input_file(reference_image)
    ])
    cargs.extend([
        "-flo",
        execution.input_file(floating_image)
    ])
    cargs.append("[TRANSFORMATION_OPTION]")
    cargs.append("[OUTPUT_OPTIONS]")
    cargs.append("[INTERPOLATION_OPTIONS]")
    ret = RegResampleOutputs(
        root=execution.output_file("."),
        output_resampled_image=execution.output_file("[RESAMPLED_IMAGE]"),
        output_resampled_blank=execution.output_file("[RESAMPLED_BLANK]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_RESAMPLE_METADATA",
    "RegResampleOutputs",
    "reg_resample",
]