# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


VOLUME_GRADIENT_METADATA = Metadata(
    id="5aedea4c247331f75a9bc89ee3c0a4ea0a69d450",
    name="volume-gradient",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output gradient magnitude volume"""


def volume_gradient(
    volume_in: InputPathType,
    volume_out: InputPathType,
    opt_presmooth_kernel: float | int | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_vectors: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner = None,
) -> VolumeGradientOutputs:
    """
    volume-gradient by Washington University School of Medicin.
    
    GRADIENT OF A VOLUME FILE.
    
    Computes the gradient of the volume by doing linear regressions for each
    voxel, considering only its face neighbors unless too few face neighbors
    exist. The gradient vector is constructed from the partial derivatives of
    the resulting linear function, and the magnitude of this vector is the
    output. If specified, the volume vector output is arranged with the x, y,
    and z components from a subvolume as consecutive subvolumes.
    
    Args:
        volume_in: the input volume
        volume_out: the output gradient magnitude volume
        opt_presmooth_kernel: smooth the volume before computing the gradient:
            the size of the gaussian smoothing kernel in mm, as sigma by default
        opt_roi_roi_volume: select a region of interest to take the gradient of:
            the region to take the gradient within
        opt_vectors: output vectors
        opt_subvolume_subvol: select a single subvolume to take the gradient of:
            the subvolume number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeGradientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-gradient")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(volume_out))
    if opt_presmooth_kernel is not None:
        cargs.extend(["-presmooth", str(opt_presmooth_kernel)])
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_vectors:
        cargs.append("-vectors")
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeGradientOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_GRADIENT_METADATA",
    "VolumeGradientOutputs",
    "volume_gradient",
]
