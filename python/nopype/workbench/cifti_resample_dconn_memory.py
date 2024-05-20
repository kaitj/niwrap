# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_RESAMPLE_DCONN_MEMORY_METADATA = Metadata(
    id="2635443003d4c7ffad7b01916e6ac9cb5cf08e92",
    name="cifti-resample-dconn-memory",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiResampleDconnMemoryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_resample_dconn_memory(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_resample_dconn_memory(
    runner: Runner,
    cifti_in: InputPathType,
    cifti_template: InputPathType,
    template_direction: str,
    surface_method: str,
    volume_method: str,
    cifti_out: InputPathType,
    opt_surface_largest: bool = False,
    opt_volume_predilate_dilate_mm: float | int | None = None,
    opt_surface_postdilate_dilate_mm: float | int | None = None,
    opt_affine_affine_file: str | None = None,
    opt_warpfield_warpfield: str | None = None,
) -> CiftiResampleDconnMemoryOutputs:
    """
    USE LOTS OF MEMORY TO RESAMPLE DCONN.
    
    This command does the same thing as running -cifti-resample twice, but uses
    memory up to approximately 2x the size that the intermediate file would be.
    This is because the intermediate dconn is kept in memory, rather than
    written to disk, and the components before and after resampling/dilation
    have to be in memory at the same time during the relevant computation. The
    <template-direction> argument should usually be COLUMN, as dtseries,
    dscalar, and dlabel all have brainordinates on that direction. If spheres
    are not specified for a surface structure which exists in the cifti files,
    its data is copied without resampling or dilation. Dilation is done with the
    'nearest' method, and is done on <new-sphere> for surface data. Volume
    components are padded before dilation so that dilation doesn't run into the
    edge of the component bounding box.
    
    To get the v1.3.2 and earlier behavior of weighted dilation, specify
    exponent of 2 for surface and volume, and -legacy-cutoff for both surface
    and volume.
    
    The <volume-method> argument must be one of the following:
    
    CUBIC
    ENCLOSING_VOXEL
    TRILINEAR
    
    The <surface-method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    
    Args:
        runner: Command runner
        cifti_in: the cifti file to resample
        cifti_template: a cifti file containing the cifti space to resample to
        template_direction: the direction of the template to use as the
            resampling space, ROW or COLUMN
        surface_method: specify a surface resampling method
        volume_method: specify a volume interpolation method
        cifti_out: the output cifti file
        opt_surface_largest: use largest weight instead of weighted average when
            doing surface resampling
        opt_volume_predilate_dilate_mm: dilate the volume components before
            resampling: distance, in mm, to dilate
        opt_surface_postdilate_dilate_mm: dilate the surface components after
            resampling: distance, in mm, to dilate
        opt_affine_affine_file: use an affine transformation on the volume
            components: the affine file to use
        opt_warpfield_warpfield: use a warpfield on the volume components: the
            warpfield to use
    Returns:
        NamedTuple of outputs (described in `CiftiResampleDconnMemoryOutputs`).
    """
    execution = runner.start_execution(CIFTI_RESAMPLE_DCONN_MEMORY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-resample-dconn-memory")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(execution.input_file(cifti_template))
    cargs.append(template_direction)
    cargs.append(surface_method)
    cargs.append(volume_method)
    cargs.append(execution.input_file(cifti_out))
    if opt_surface_largest:
        cargs.append("-surface-largest")
    if opt_volume_predilate_dilate_mm is not None:
        cargs.extend(["-volume-predilate", str(opt_volume_predilate_dilate_mm)])
    if opt_surface_postdilate_dilate_mm is not None:
        cargs.extend(["-surface-postdilate", str(opt_surface_postdilate_dilate_mm)])
    if opt_affine_affine_file is not None:
        cargs.extend(["-affine", opt_affine_affine_file])
    if opt_warpfield_warpfield is not None:
        cargs.extend(["-warpfield", opt_warpfield_warpfield])
    ret = CiftiResampleDconnMemoryOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
