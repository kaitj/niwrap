# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_DSET_METADATA = Metadata(
    id="2ab311f33719c698bfe9a89ea408fd9d6da717a0.boutiques",
    name="ConvertDset",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class ConvertDsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_dataset: OutputPathType | None
    """Converted dataset output"""


def convert_dset(
    output_type: list[typing.Literal["niml_asc", "niml_bi", "1D", "1Dp", "1Dpt", "gii", "gii_asc", "gii_b64", "gii_b64gz", "1D_stderr", "1D_stdout", "niml_stderr", "niml_stdout", "1Dp_stdout", "1Dp_stderr", "1Dpt_stdout", "1Dpt_stderr"]],
    input_dataset: InputPathType,
    input_type: typing.Literal["niml", "1D", "dx"] | None = None,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> ConvertDsetOutputs:
    """
    Converts a surface dataset from one format to another.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/ConvertDset.html
    
    Args:
        output_type: Type of output datasets.
        input_dataset: Input dataset to be converted.
        input_type: Type of input datasets.
        output_prefix: Output prefix for dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertDsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_DSET_METADATA)
    cargs = []
    cargs.append("ConvertDset")
    cargs.extend([
        "-o_",
        *output_type
    ])
    cargs.append("-input")
    cargs.extend([
        "-input",
        execution.input_file(input_dataset)
    ])
    if input_type is not None:
        cargs.extend([
            "-i_",
            input_type
        ])
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    cargs.append("[MANDATORY_PARAMS]")
    cargs.append("[OPTIONAL_PARAMS]")
    ret = ConvertDsetOutputs(
        root=execution.output_file("."),
        converted_dataset=execution.output_file(output_prefix) if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_DSET_METADATA",
    "ConvertDsetOutputs",
    "convert_dset",
]