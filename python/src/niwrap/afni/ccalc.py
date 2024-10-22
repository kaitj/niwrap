# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CCALC_METADATA = Metadata(
    id="e76d49ddb6fb2569c3e43954471845bd902d1d58.boutiques",
    name="ccalc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class CcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ccalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ccalc(
    expr: str,
    format_: str | None = None,
    runner: Runner | None = None,
) -> CcalcOutputs:
    """
    Command line calculator with formatted output options.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        expr: Evaluate an expression specified on command line, return answer\
            and quit.
        format_: Format output in a nice form. Choose from 'double', 'nice',\
            'int', 'rint', 'cint', 'fint', or custom format string (e.g., %n.mf).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CCALC_METADATA)
    cargs = []
    cargs.append("ccalc")
    if format_ is not None:
        cargs.extend([
            "-form",
            format_
        ])
    cargs.append("-eval")
    cargs.extend([
        "-eval",
        expr
    ])
    ret = CcalcOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CCALC_METADATA",
    "CcalcOutputs",
    "ccalc",
]
