# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FILMBABESCRIPT_METADATA = Metadata(
    id="9ab884875e83253614c3c611f6bada1f6ecbb988.boutiques",
    name="filmbabescript",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FilmbabescriptOutputs(typing.NamedTuple):
    """
    Output object returned when calling `filmbabescript(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def filmbabescript(
    feat_dir: str,
    flobs_dir: str,
    runner: Runner | None = None,
) -> FilmbabescriptOutputs:
    """
    A tool/script for processing FEAT directories and FLOBs directories.
    
    Author: Author Unknown
    
    URL: URL not provided
    
    Args:
        feat_dir: Input FEAT directory.
        flobs_dir: Input FLOBs directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FilmbabescriptOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILMBABESCRIPT_METADATA)
    cargs = []
    cargs.append("filmbabescript")
    cargs.append(feat_dir)
    cargs.append(flobs_dir)
    ret = FilmbabescriptOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILMBABESCRIPT_METADATA",
    "FilmbabescriptOutputs",
    "filmbabescript",
]
