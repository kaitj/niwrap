# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_DWI_TO_DT_METADATA = Metadata(
    id="c9b03178bc0b3f7392ffeb60e5d57fcbd0a2ab68.boutiques",
    name="fat_proc_dwi_to_dt",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatProcDwiToDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_dwi_to_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated with the specified prefix."""


def fat_proc_dwi_to_dt(
    in_dwi: InputPathType,
    in_gradmat: InputPathType,
    prefix: str,
    runner: Runner | None = None,
) -> FatProcDwiToDtOutputs:
    """
    This program fits tensors and DT parameters, as well as the uncertainty of DT
    parameters needed for tractography.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_proc_dwi_to_dt.html
    
    Args:
        in_dwi: 4D volume of N DWIs. Required.
        in_gradmat: Input text file of N gradient vectors or bmatrices.
        prefix: Set prefix for output DWI data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcDwiToDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_DWI_TO_DT_METADATA)
    cargs = []
    cargs.append("fat_proc_dwi_to_dt")
    cargs.append("-in_dwi")
    cargs.append(execution.input_file(in_dwi))
    cargs.extend([
        "-in_col_matA | -in_col_matT | -in_col_vec | -in_row_vec",
        execution.input_file(in_gradmat)
    ])
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.append("[OPTIONAL_PARAMETERS]")
    ret = FatProcDwiToDtOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(prefix + "*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_DWI_TO_DT_METADATA",
    "FatProcDwiToDtOutputs",
    "fat_proc_dwi_to_dt",
]