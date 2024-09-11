# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCOMPLEX_METADATA = Metadata(
    id="04bdecac3ae0becd85cc68c90704b37e0ef54666.boutiques",
    name="fslcomplex",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslcomplexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslcomplex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_output_file: OutputPathType
    """The resulting output file from the specified operation."""


def fslcomplex(
    runner: Runner | None = None,
) -> FslcomplexOutputs:
    """
    Tool for manipulating complex-valued MR data.
    
    Author: FMRIB Analysis Group, Oxford University, UK
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslcomplexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCOMPLEX_METADATA)
    cargs = []
    cargs.append("fslcomplex")
    cargs.append("<outputtype>")
    cargs.append("<input>")
    cargs.append("<output>")
    cargs.append("[startvol")
    cargs.append("[endvol]]")
    ret = FslcomplexOutputs(
        root=execution.output_file("."),
        result_output_file=execution.output_file("[OUTPUT]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCOMPLEX_METADATA",
    "FslcomplexOutputs",
    "fslcomplex",
]