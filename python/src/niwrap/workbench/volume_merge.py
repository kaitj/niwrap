# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


VOLUME_MERGE_METADATA = Metadata(
    id="b6254eb01d66a7787b53b5d1215c803eda9aba4a",
    name="volume-merge",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume file"""


def volume_merge(
    volume_out: InputPathType,
    opt_volume_volume_in: InputPathType | None = None,
    runner: Runner = None,
) -> VolumeMergeOutputs:
    """
    volume-merge by Washington University School of Medicin.
    
    MERGE VOLUME FILES INTO A NEW FILE.
    
    Takes one or more volume files and constructs a new volume file by
    concatenating subvolumes from them. The input volume files must have the
    same volume space.
    
    Example: wb_command -volume-merge out.nii -volume first.nii -subvolume 1
    -volume second.nii
    
    This example would take the first subvolume from first.nii, followed by all
    subvolumes from second.nii, and write these to out.nii.
    
    Args:
        volume_out: the output volume file
        opt_volume_volume_in: specify an input volume file: a volume file to use
            subvolumes from
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-merge")
    cargs.append(execution.input_file(volume_out))
    if opt_volume_volume_in is not None:
        cargs.extend(["-volume", execution.input_file(opt_volume_volume_in)])
    ret = VolumeMergeOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_MERGE_METADATA",
    "VolumeMergeOutputs",
    "volume_merge",
]
