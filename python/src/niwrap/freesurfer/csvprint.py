# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CSVPRINT_METADATA = Metadata(
    id="88fe426126aea1052da673cfeee9f2078fb01491.boutiques",
    name="csvprint",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class CsvprintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `csvprint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def csvprint(
    infile: InputPathType,
    runner: Runner | None = None,
) -> CsvprintOutputs:
    """
    Command-line tool for printing CSV files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input CSV file to be printed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CsvprintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CSVPRINT_METADATA)
    cargs = []
    cargs.append("csvprint")
    cargs.append(execution.input_file(infile))
    ret = CsvprintOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CSVPRINT_METADATA",
    "CsvprintOutputs",
    "csvprint",
]