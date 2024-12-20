# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SBTIV_METADATA = Metadata(
    id="f635fd3b0d71913a55d64eab8618d5ffd1066300.boutiques",
    name="sbtiv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SbtivOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sbtiv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Intracranial stats output file."""


def sbtiv(
    input_file: InputPathType,
    output_file: str | None = None,
    labels_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> SbtivOutputs:
    """
    Tool to calculate the total intracranial volume of a subject by summing
    individual volumes computed by samseg.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Volume stats input file.
        output_file: Intracranial stats output file.
        labels_file: File containing a list of intracranial structure\
            labelnames to include in the calculation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SbtivOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SBTIV_METADATA)
    cargs = []
    cargs.append("sbtiv")
    cargs.append(execution.input_file(input_file))
    if output_file is not None:
        cargs.extend([
            "-o",
            output_file
        ])
    if labels_file is not None:
        cargs.extend([
            "-l",
            execution.input_file(labels_file)
        ])
    ret = SbtivOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(output_file) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SBTIV_METADATA",
    "SbtivOutputs",
    "sbtiv",
]
