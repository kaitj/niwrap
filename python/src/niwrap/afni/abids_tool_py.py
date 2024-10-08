# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ABIDS_TOOL_PY_METADATA = Metadata(
    id="524c7379ac2d0ccd3252afa7fee994de43f217f4.boutiques",
    name="abids_tool.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AbidsToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `abids_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def abids_tool_py(
    input_files: list[InputPathType],
    copy_prefix: list[str] | None = None,
    runner: Runner | None = None,
) -> AbidsToolPyOutputs:
    """
    A tool to work with BIDS formatted datasets created with dcm2niix_afni or
    dcm2niix, mainly to pull information from the matching JSON file and refit the
    input dataset using 3drefit.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/abids_tool.py.html
    
    Args:
        input_files: At least one 3d+time dataset in NIFTI format.
        copy_prefix: Copy both the NIFTI dataset(s) and matching .json file(s)\
            to PREFIX. Must have the same number of prefixes as datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AbidsToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ABIDS_TOOL_PY_METADATA)
    cargs = []
    cargs.append("abids_tool")
    cargs.extend([execution.input_file(f) for f in input_files])
    if copy_prefix is not None:
        cargs.extend([
            "-copy",
            *copy_prefix
        ])
    ret = AbidsToolPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ABIDS_TOOL_PY_METADATA",
    "AbidsToolPyOutputs",
    "abids_tool_py",
]
