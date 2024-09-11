# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANALYZE_TRACE_METADATA = Metadata(
    id="ed47a7f83dcf15fced73ccd7d24856d93e3037fb.boutiques",
    name="AnalyzeTrace",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AnalyzeTraceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `analyze_trace(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def analyze_trace(
    runner: Runner | None = None,
) -> AnalyzeTraceOutputs:
    """
    A program to analyze SUMA (and AFNI's perhaps) stack output for functions that
    return with RETURN without bothering to go on the stack.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/AnalyzeTrace.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnalyzeTraceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANALYZE_TRACE_METADATA)
    cargs = []
    cargs.append("AnalyzeTrace")
    cargs.append("[OPTIONAL_PARAMETERS]")
    cargs.append("FILE")
    ret = AnalyzeTraceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANALYZE_TRACE_METADATA",
    "AnalyzeTraceOutputs",
    "analyze_trace",
]