# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UNPACKIMADIR_METADATA = Metadata(
    id="6a27f64ee58627da90e1a875d70fa5b839c021e5.boutiques",
    name="unpackimadir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class UnpackimadirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpackimadir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def unpackimadir(
    source_directory: str,
    target_directory: str,
    runner: Runner | None = None,
) -> UnpackimadirOutputs:
    """
    Unpack image directories.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_directory: Source directory containing the images to be unpacked.
        target_directory: Target directory where the unpacked images will be\
            stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackimadirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACKIMADIR_METADATA)
    cargs = []
    cargs.append("unpackimadir")
    cargs.extend([
        "-src",
        source_directory
    ])
    cargs.extend([
        "-targ",
        target_directory
    ])
    ret = UnpackimadirOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UNPACKIMADIR_METADATA",
    "UnpackimadirOutputs",
    "unpackimadir",
]