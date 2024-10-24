# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RELABEL_HYPOINTENSITIES_METADATA = Metadata(
    id="fdccbcea8d0b7d6372e7bb2e7e4ef70fd6f7ab26.boutiques",
    name="mri_relabel_hypointensities",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRelabelHypointensitiesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_relabel_hypointensities(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_aseg_file: OutputPathType
    """The relabeled output aseg file"""


def mri_relabel_hypointensities(
    input_aseg: InputPathType,
    surface_directory: str,
    output_aseg: str,
    runner: Runner | None = None,
) -> MriRelabelHypointensitiesOutputs:
    """
    Tool for relabeling hypointensities in FreeSurfer's aseg files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_aseg: Input aseg file.
        surface_directory: Directory containing surfaces.
        output_aseg: Output aseg file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRelabelHypointensitiesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RELABEL_HYPOINTENSITIES_METADATA)
    cargs = []
    cargs.append("mri_relabel_hypointensities")
    cargs.append(execution.input_file(input_aseg))
    cargs.append(surface_directory)
    cargs.append(output_aseg)
    ret = MriRelabelHypointensitiesOutputs(
        root=execution.output_file("."),
        output_aseg_file=execution.output_file(output_aseg),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RELABEL_HYPOINTENSITIES_METADATA",
    "MriRelabelHypointensitiesOutputs",
    "mri_relabel_hypointensities",
]
