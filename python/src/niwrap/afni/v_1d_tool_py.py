# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_TOOL_PY_METADATA = Metadata(
    id="3fa41dd1bca0cd548d36d10ae38dd77cf843863b.boutiques",
    name="1d_tool.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Resulting 1D file"""


def v_1d_tool_py(
    infile: InputPathType,
    write: str | None = None,
    select_cols: str | None = None,
    select_rows: str | None = None,
    select_groups: str | None = None,
    censor_motion: float | None = None,
    pad_into_many_runs: str | None = None,
    set_nruns: float | None = None,
    set_run_lengths: str | None = None,
    show_rows_cols: bool = False,
    transpose: bool = False,
    reverse: bool = False,
    show_max_displace: bool = False,
    runner: Runner | None = None,
) -> V1dToolPyOutputs:
    """
    A tool for manipulating and evaluating 1D files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1d_tool.py.html
    
    Args:
        infile: Input 1D file.
        write: Output file to write results.
        select_cols: Select specific columns.
        select_rows: Select specific rows.
        select_groups: Select columns by group numbers.
        censor_motion: Generate a boolean censor file.
        pad_into_many_runs: Pad a 1D file into many runs.
        set_nruns: Set number of runs.
        set_run_lengths: Set run lengths.
        show_rows_cols: Show the number of rows and columns.
        transpose: Transpose the input matrix.
        reverse: Reverse the data over time.
        show_max_displace: Show the maximum pairwise displacement.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_TOOL_PY_METADATA)
    cargs = []
    cargs.append("1d_tool.py")
    cargs.extend([
        "-infile",
        execution.input_file(infile)
    ])
    if write is not None:
        cargs.extend([
            "-write",
            write
        ])
    if select_cols is not None:
        cargs.extend([
            "-select_cols",
            select_cols
        ])
    if select_rows is not None:
        cargs.extend([
            "-select_rows",
            select_rows
        ])
    if select_groups is not None:
        cargs.extend([
            "-select_groups",
            select_groups
        ])
    if censor_motion is not None:
        cargs.extend([
            "-censor_motion",
            str(censor_motion)
        ])
    if pad_into_many_runs is not None:
        cargs.extend([
            "-pad_into_many_runs",
            pad_into_many_runs
        ])
    if set_nruns is not None:
        cargs.extend([
            "-set_nruns",
            str(set_nruns)
        ])
    if set_run_lengths is not None:
        cargs.extend([
            "-set_run_lengths",
            set_run_lengths
        ])
    if show_rows_cols:
        cargs.append("-show_rows_cols")
    if transpose:
        cargs.append("-transpose")
    if reverse:
        cargs.append("-reverse")
    if show_max_displace:
        cargs.append("-show_max_displace")
    ret = V1dToolPyOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(write) if (write is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dToolPyOutputs",
    "V_1D_TOOL_PY_METADATA",
    "v_1d_tool_py",
]
