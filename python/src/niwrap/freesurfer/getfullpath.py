# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GETFULLPATH_METADATA = Metadata(
    id="35adb422237513a6ef638025617ac7d09458620d.boutiques",
    name="getfullpath",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GetfullpathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `getfullpath(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def getfullpath(
    filename: str,
    runner: Runner | None = None,
) -> GetfullpathOutputs:
    """
    A utility to retrieve the full path of a specified file or directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        filename: Filename for which to get the full path.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetfullpathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GETFULLPATH_METADATA)
    cargs = []
    cargs.append("getfullpath")
    cargs.append(filename)
    ret = GetfullpathOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GETFULLPATH_METADATA",
    "GetfullpathOutputs",
    "getfullpath",
]