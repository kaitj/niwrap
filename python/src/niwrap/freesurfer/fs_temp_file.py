# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FS_TEMP_FILE_METADATA = Metadata(
    id="517fdbcd5c110803a94e295435754191461fd4ee.boutiques",
    name="fs_temp_file",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FsTempFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_temp_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fs_temp_file(
    base_dir_alt: str | None = None,
    suffix_alt: str | None = None,
    scratch: bool = False,
    help_alt: bool = False,
    runner: Runner | None = None,
) -> FsTempFileOutputs:
    """
    Generates and creates an empty temporary file, printing the resulting path to
    stdout.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        base_dir_alt: Manually specify base temporary directory.
        suffix_alt: Optional file suffix.
        scratch: Use /scratch directory if available, but FS_TMPDIR takes\
            priority.
        help_alt: Print help text and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsTempFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_TEMP_FILE_METADATA)
    cargs = []
    cargs.append("fs_temp_file")
    if base_dir_alt is not None:
        cargs.extend([
            "--base",
            base_dir_alt
        ])
    if suffix_alt is not None:
        cargs.extend([
            "--suffix",
            suffix_alt
        ])
    if scratch:
        cargs.append("--scratch")
    if help_alt:
        cargs.append("--help")
    ret = FsTempFileOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FS_TEMP_FILE_METADATA",
    "FsTempFileOutputs",
    "fs_temp_file",
]
