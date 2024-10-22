# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_SCHURPROD_METADATA = Metadata(
    id="ca12ec7f7f8174a7f7db38c0f340010b291391dc.boutiques",
    name="fsl_schurprod",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslSchurprodOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_schurprod(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix_product: OutputPathType
    """Generated matrix product output file"""


def fsl_schurprod(
    input_file: InputPathType,
    design_file: InputPathType,
    output_file: str,
    regression_flag: bool = False,
    index: float | None = None,
    mask_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslSchurprodOutputs:
    """
    Generates element-wise matrix products or product of matrices against vectors
    from 4D data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file name (4D image file).
        design_file: ASCII text matrix of time series to be correlated.
        output_file: Output file base name.
        regression_flag: Use regression rather than correlation.
        index: Index of column in the design to be used for matrix product\
            calculation.
        mask_file: Mask image file name.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSchurprodOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SCHURPROD_METADATA)
    cargs = []
    cargs.append("fsl_schurprod")
    cargs.append("-i")
    cargs.append(execution.input_file(input_file))
    cargs.append("-d")
    cargs.append(execution.input_file(design_file))
    cargs.append("-o")
    cargs.append(output_file)
    if regression_flag:
        cargs.append("-r")
    if index is not None:
        cargs.extend([
            "-i",
            str(index)
        ])
    if mask_file is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask_file)
        ])
    if verbose_flag:
        cargs.append("-v")
    if help_flag:
        cargs.append("-h")
    ret = FslSchurprodOutputs(
        root=execution.output_file("."),
        output_matrix_product=execution.output_file(output_file + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_SCHURPROD_METADATA",
    "FslSchurprodOutputs",
    "fsl_schurprod",
]
