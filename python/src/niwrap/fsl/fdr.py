# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FDR_METADATA = Metadata(
    id="2a1c4a9f5cb4a550c5161a4d2b7bef57ce14f259.boutiques",
    name="fdr",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_adjusted: OutputPathType | None
    """Output FDR-adjusted p-values image"""
    output_thresholded: OutputPathType
    """Thresholded output p-value image"""
    output_order: OutputPathType
    """Output order values image"""


def fdr(
    infile: InputPathType,
    maskfile: InputPathType | None = None,
    qvalue: float | None = None,
    adjustedimage: str | None = None,
    othresh_flag: bool = False,
    order_flag: bool = False,
    oneminusp_flag: bool = False,
    positive_corr_flag: bool = False,
    independent_flag: bool = False,
    conservative_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FdrOutputs:
    """
    False Discovery Rate (FDR) correction tool from FSL.
    
    Author: University of Oxford (Mark Jenkinson)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input p-value image file.
        maskfile: Mask image file.
        qvalue: Q-value (FDR) threshold.
        adjustedimage: Output image with FDR-adjusted p-values.
        othresh_flag: Output a thresholded p-value image.
        order_flag: Output image of order values.
        oneminusp_flag: Treat input as 1-p (also save output like this).
        positive_corr_flag: Use FDR correction factor that assumes positive\
            correlation.
        independent_flag: Use FDR correction factor that assumes independence.
        conservative_flag: Use conservative FDR correction factor (allows for\
            any correlation).
        debug_flag: Switch on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FDR_METADATA)
    cargs = []
    cargs.append("fdr")
    cargs.append("-i")
    cargs.extend([
        "-i",
        execution.input_file(infile)
    ])
    if maskfile is not None:
        cargs.extend([
            "-m",
            execution.input_file(maskfile)
        ])
    if qvalue is not None:
        cargs.extend([
            "-q",
            str(qvalue)
        ])
    if adjustedimage is not None:
        cargs.extend([
            "-a",
            adjustedimage
        ])
    if othresh_flag:
        cargs.append("--othresh")
    if order_flag:
        cargs.append("--order")
    if oneminusp_flag:
        cargs.append("--oneminusp")
    if positive_corr_flag:
        cargs.append("--positivecorr")
    if independent_flag:
        cargs.append("--independent")
    if conservative_flag:
        cargs.append("--conservative")
    if debug_flag:
        cargs.append("--debug")
    if verbose_flag:
        cargs.append("-v")
    ret = FdrOutputs(
        root=execution.output_file("."),
        output_adjusted=execution.output_file(adjustedimage + ".nii.gz") if (adjustedimage is not None) else None,
        output_thresholded=execution.output_file(pathlib.Path(infile).name + "_thr.nii.gz"),
        output_order=execution.output_file(pathlib.Path(infile).name + "_order.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FDR_METADATA",
    "FdrOutputs",
    "fdr",
]
