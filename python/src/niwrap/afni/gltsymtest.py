# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GLTSYMTEST_METADATA = Metadata(
    id="332931d9c4a4e4a6d9609bf286d3aa59c1c5917b.boutiques",
    name="GLTsymtest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class GltsymtestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gltsymtest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gltsymtest(
    varlist: str,
    expr: list[str],
    badonly: bool = False,
    runner: Runner | None = None,
) -> GltsymtestOutputs:
    """
    A tool to test the validity of '-gltsym' strings for use with 3dDeconvolve or
    3dREMLfit.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/GLTsymtest.html
    
    Args:
        varlist: A list of allowed variable names in the expression, separated\
            by commas, semicolons, and/or spaces.
        expr: GLT symbolic expression(s), enclosed in quotes.
        badonly: A flag to only output BAD messages rather than all messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GltsymtestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GLTSYMTEST_METADATA)
    cargs = []
    cargs.append("GLTsymtest")
    if badonly:
        cargs.append("-badonly")
    cargs.append(varlist)
    cargs.extend(expr)
    ret = GltsymtestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GLTSYMTEST_METADATA",
    "GltsymtestOutputs",
    "gltsymtest",
]
