# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_BRAIN_VOLUME_METADATA = Metadata(
    id="2918ea0c5a20422d8241bcf06406d8027e4e4dae.boutiques",
    name="mri_brain_volume",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriBrainVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_brain_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType | None
    """Output file containing brain volume information"""


def mri_brain_volume(
    input_file: InputPathType,
    output_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriBrainVolumeOutputs:
    """
    Tool to calculate brain volume from MRI scans.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input MRI file.
        output_file: Output file for brain volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriBrainVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_BRAIN_VOLUME_METADATA)
    cargs = []
    cargs.append("mri_brain_volume")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_file))
    if output_file is not None:
        cargs.append(execution.input_file(output_file))
    ret = MriBrainVolumeOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(pathlib.Path(output_file).name) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_BRAIN_VOLUME_METADATA",
    "MriBrainVolumeOutputs",
    "mri_brain_volume",
]
