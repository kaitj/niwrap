# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__1D_DIFF_MAG_METADATA = Metadata(
    id="ccbd06979574a6fa073f5c90b06eebc4b39093fe.boutiques",
    name="@1dDiffMag",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dDiffMagOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__1d_diff_mag(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_stdout: OutputPathType
    """The result as a single number displayed on stdout"""


def v__1d_diff_mag(
    infile: InputPathType,
    runner: Runner | None = None,
) -> V1dDiffMagOutputs:
    """
    Computes a magnitude estimate of the first differences of a 1D file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: 1D input file to compute the magnitude estimate of the first\
            differences.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dDiffMagOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__1D_DIFF_MAG_METADATA)
    cargs = []
    cargs.append("@1dDiffMag")
    cargs.append(execution.input_file(infile))
    ret = V1dDiffMagOutputs(
        root=execution.output_file("."),
        result_stdout=execution.output_file("stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dDiffMagOutputs",
    "V__1D_DIFF_MAG_METADATA",
    "v__1d_diff_mag",
]
