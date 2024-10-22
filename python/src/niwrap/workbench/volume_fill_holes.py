# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_FILL_HOLES_METADATA = Metadata(
    id="278f9aea77ede4c32b8a60e5b93fad04b1fb9ba9.boutiques",
    name="volume-fill-holes",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class VolumeFillHolesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_fill_holes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output ROI volume"""


def volume_fill_holes(
    volume_in: InputPathType,
    volume_out: str,
    runner: Runner | None = None,
) -> VolumeFillHolesOutputs:
    """
    Fill holes in an roi volume.
    
    Finds all face-connected parts that are not included in the ROI, and fills
    all but the largest one with ones.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input ROI volume.
        volume_out: the output ROI volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeFillHolesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_FILL_HOLES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-fill-holes")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    ret = VolumeFillHolesOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(volume_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_FILL_HOLES_METADATA",
    "VolumeFillHolesOutputs",
    "volume_fill_holes",
]
