# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DSUM_METADATA = Metadata(
    id="4f283576416dcd71cd46d26b559abcfd886268b8.boutiques",
    name="1dsum",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dsumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dsum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Sum or average of columns in the input files"""


def v_1dsum(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> V1dsumOutputs:
    """
    Sum or average columns of ASCII files with numbers arranged in rows and columns.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dsum.html
    
    Args:
        input_files: Input ASCII files with numbers arranged in rows and\
            columns.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dsumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DSUM_METADATA)
    cargs = []
    cargs.append("1dsum")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V1dsumOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dsumOutputs",
    "V_1DSUM_METADATA",
    "v_1dsum",
]