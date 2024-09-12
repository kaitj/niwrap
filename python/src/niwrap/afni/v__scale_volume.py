# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SCALE_VOLUME_METADATA = Metadata(
    id="639e86c7c0bb97fdc4c82b2692a080c0bd9f37fc.boutiques",
    name="@ScaleVolume",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VScaleVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__scale_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output scaled dataset"""


def v__scale_volume(
    runner: Runner | None = None,
) -> VScaleVolumeOutputs:
    """
    A tool to scale the volume of datasets.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ScaleVolume.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VScaleVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SCALE_VOLUME_METADATA)
    cargs = []
    cargs.append("@ScaleVolume")
    cargs.append("<-input")
    cargs.append("DSET>")
    cargs.append("<-prefix")
    cargs.append("PREFIX>")
    cargs.append("[-perc_clip")
    cargs.append("P0")
    cargs.append("P1]")
    cargs.append("[-val_clip")
    cargs.append("V0")
    cargs.append("V1]")
    cargs.append("[-scale_by_mean]")
    cargs.append("[-scale_by_median]")
    cargs.append("[-norm]")
    cargs.append("[-mask")
    cargs.append("MSET]")
    ret = VScaleVolumeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("<-prefix PREFIX>_scaled"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VScaleVolumeOutputs",
    "V__SCALE_VOLUME_METADATA",
    "v__scale_volume",
]
