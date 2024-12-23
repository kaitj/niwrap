# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_MAT_TABLEIZE_METADATA = Metadata(
    id="5ba44998c47e95e162b9d566a509d5fcbb197e51.boutiques",
    name="fat_mat_tableize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatMatTableizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat_tableize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType
    """Table file usable in AFNI group analysis programs."""
    output_log: OutputPathType
    """Log file reporting inputs, matching, and aspects of creating the table
    file."""


def fat_mat_tableize(
    input_matrices: list[str],
    output_prefix: str,
    input_csv: InputPathType | None = None,
    input_list: InputPathType | None = None,
    parameters: list[str] | None = None,
    version: bool = False,
    date: bool = False,
    help_: bool = False,
    help_short: bool = False,
    help_view: bool = False,
    runner: Runner | None = None,
) -> FatMatTableizeOutputs:
    """
    Make tables for AFNI group analysis programs from 3dNetCorr (*.netcc) and
    3dTrackID (*.grid) outputs, with optional additional subject information from
    CSV files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_matrices: Names of *.netcc or *.grid files with matrices to be\
            used to make table; can be provided using wildcard chars.
        output_prefix: Output basename for the table and log files. Suffix and\
            file extensions will be added for the outputs.
        input_csv: Name of a CSV file to include in the table. The first column\
            must have subject ID labels that match with the input matrix files.
        input_list: File containing paths to subject matrices and optionally\
            CSV IDs for matching.
        parameters: List of matrices to be included in the table, identified by\
            their parameter name.
        version: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        help_short: Display help in terminal (short flag).
        help_view: Display help in a separate text editor.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMatTableizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT_TABLEIZE_METADATA)
    cargs = []
    cargs.append("fat_mat_tableize.py")
    cargs.extend([
        "-in_mat",
        *input_matrices
    ])
    if input_csv is not None:
        cargs.extend([
            "-in_csv",
            execution.input_file(input_csv)
        ])
    if input_list is not None:
        cargs.extend([
            "-in_listfile",
            execution.input_file(input_list)
        ])
    cargs.extend([
        "-prefix",
        output_prefix
    ])
    if parameters is not None:
        cargs.extend([
            "-pars",
            *parameters
        ])
    if version:
        cargs.append("-ver")
    if date:
        cargs.append("-date")
    if help_:
        cargs.append("-help")
    if help_short:
        cargs.append("-h")
    if help_view:
        cargs.append("-hview")
    ret = FatMatTableizeOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(output_prefix + "_tbl.txt"),
        output_log=execution.output_file(output_prefix + "_prep.log"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_MAT_TABLEIZE_METADATA",
    "FatMatTableizeOutputs",
    "fat_mat_tableize",
]
