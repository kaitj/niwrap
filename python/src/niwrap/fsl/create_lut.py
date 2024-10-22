# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CREATE_LUT_METADATA = Metadata(
    id="f5c8f6c368b2d93f8314fb443bdc263294ea4108.boutiques",
    name="create_lut",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class CreateLutOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_lut(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Generated lookup table files"""


def create_lut(
    output_file_root: str,
    runner: Runner | None = None,
) -> CreateLutOutputs:
    """
    A tool to create lookup tables.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_file_root: The root name of the output file to be generated.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateLutOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_LUT_METADATA)
    cargs = []
    cargs.append("create_lut")
    cargs.append(output_file_root)
    ret = CreateLutOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(output_file_root + ".*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CREATE_LUT_METADATA",
    "CreateLutOutputs",
    "create_lut",
]
