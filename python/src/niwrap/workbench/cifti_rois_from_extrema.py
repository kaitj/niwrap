# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="8e061a8d05a30a7fd1f981ce8c2c497e6199855c",
    name="cifti-rois-from-extrema",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_rois_from_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_rois_from_extrema(
    cifti: InputPathType,
    surf_limit: float | int,
    vol_limit: float | int,
    direction: str,
    cifti_out: InputPathType,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_merged_volume: bool = False,
    runner: Runner = None,
) -> CiftiRoisFromExtremaOutputs:
    """
    cifti-rois-from-extrema by Washington University School of Medicin.
    
    CREATE CIFTI ROI MAPS FROM EXTREMA MAPS.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Args:
        cifti: the input cifti
        surf_limit: geodesic distance limit from vertex, in mm
        vol_limit: euclidean distance limit from voxel center, in mm
        direction: which dimension an extrema map is along, ROW or COLUMN
        cifti_out: the output cifti
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        opt_overlap_logic_method: how to handle overlapping ROIs, default ALLOW:
            the method of resolving overlaps
        opt_merged_volume: treat volume components as if they were a single
            component
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiRoisFromExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ROIS_FROM_EXTREMA_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-rois-from-extrema")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surf_limit))
    cargs.append(str(vol_limit))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    if opt_overlap_logic_method is not None:
        cargs.extend(["-overlap-logic", opt_overlap_logic_method])
    if opt_merged_volume:
        cargs.append("-merged-volume")
    ret = CiftiRoisFromExtremaOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ROIS_FROM_EXTREMA_METADATA",
    "CiftiRoisFromExtremaOutputs",
    "cifti_rois_from_extrema",
]
