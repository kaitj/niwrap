# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CALC_GRAD_PERC_DEV_METADATA = Metadata(
    id="41712174e5d5a8cc5a54c8270f4e1d40beda5c6d.boutiques",
    name="calc_grad_perc_dev",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class CalcGradPercDevOutputs(typing.NamedTuple):
    """
    Output object returned when calling `calc_grad_perc_dev(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def calc_grad_perc_dev(
    fullwarp_image: InputPathType,
    out_basename: str,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> CalcGradPercDevOutputs:
    """
    Compute the gradient percent deviation based on a full warp image from
    gradient_unwarp.py.
    
    Author: Mark Jenkinson, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation
    
    Args:
        fullwarp_image: Full warp image from gradient_unwarp.py.
        out_basename: Output basename.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display the help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CalcGradPercDevOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CALC_GRAD_PERC_DEV_METADATA)
    cargs = []
    cargs.append("calc_grad_perc_dev")
    cargs.extend([
        "--fullwarp",
        execution.input_file(fullwarp_image)
    ])
    cargs.extend([
        "-o,--out",
        out_basename
    ])
    if verbose_flag:
        cargs.append("-v,--verbose")
    if help_flag:
        cargs.append("-h,--help")
    ret = CalcGradPercDevOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CALC_GRAD_PERC_DEV_METADATA",
    "CalcGradPercDevOutputs",
    "calc_grad_perc_dev",
]
