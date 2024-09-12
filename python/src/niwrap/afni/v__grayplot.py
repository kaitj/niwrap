# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__GRAYPLOT_METADATA = Metadata(
    id="2d8af8df845fbb60cb7c112562424a57ea883df7.boutiques",
    name="@grayplot",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VGrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__grayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    grayplot_img: OutputPathType
    """Output grayplot image"""


def v__grayplot(
    dirname: str,
    allorder: bool = False,
    runner: Runner | None = None,
) -> VGrayplotOutputs:
    """
    Script to read files from an afni_proc.py results directory and produce a
    grayplot from the errts dataset(s), combined with a motion magnitude indicator
    graph.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@grayplot.html
    
    Args:
        dirname: Directory containing afni_proc.py results.
        allorder: Create grayplots for all ordering methods.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GRAYPLOT_METADATA)
    cargs = []
    cargs.append("@grayplot")
    cargs.append(dirname)
    if allorder:
        cargs.append("-ALLorder")
    ret = VGrayplotOutputs(
        root=execution.output_file("."),
        grayplot_img=execution.output_file("Grayplot.errts.*.png"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGrayplotOutputs",
    "V__GRAYPLOT_METADATA",
    "v__grayplot",
]
