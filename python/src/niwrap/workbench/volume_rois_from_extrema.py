# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

VOLUME_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="c4fedde00f78c99eb288d08659b236035a5d3048.boutiques",
    name="volume-rois-from-extrema",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeRoisFromExtremaParameters = typing.TypedDict('VolumeRoisFromExtremaParameters', {
    "__STYX_TYPE__": typing.Literal["volume-rois-from-extrema"],
    "volume_in": InputPathType,
    "limit": float,
    "volume_out": str,
    "opt_gaussian_sigma": typing.NotRequired[float | None],
    "opt_roi_roi_volume": typing.NotRequired[InputPathType | None],
    "opt_overlap_logic_method": typing.NotRequired[str | None],
    "opt_subvolume_subvol": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "volume-rois-from-extrema": volume_rois_from_extrema_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "volume-rois-from-extrema": volume_rois_from_extrema_outputs,
    }.get(t)


class VolumeRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_rois_from_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_rois_from_extrema_params(
    volume_in: InputPathType,
    limit: float,
    volume_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_subvolume_subvol: str | None = None,
) -> VolumeRoisFromExtremaParameters:
    """
    Build parameters.
    
    Args:
        volume_in: the input volume.
        limit: distance limit from voxel center, in mm.
        volume_out: the output volume.
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:\
            the sigma for the gaussian kernel, in mm.
        opt_roi_roi_volume: select a region of interest to use: the region to\
            use.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_subvolume_subvol: select a single subvolume to take the gradient\
            of: the subvolume number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-rois-from-extrema",
        "volume_in": volume_in,
        "limit": limit,
        "volume_out": volume_out,
    }
    if opt_gaussian_sigma is not None:
        params["opt_gaussian_sigma"] = opt_gaussian_sigma
    if opt_roi_roi_volume is not None:
        params["opt_roi_roi_volume"] = opt_roi_roi_volume
    if opt_overlap_logic_method is not None:
        params["opt_overlap_logic_method"] = opt_overlap_logic_method
    if opt_subvolume_subvol is not None:
        params["opt_subvolume_subvol"] = opt_subvolume_subvol
    return params


def volume_rois_from_extrema_cargs(
    params: VolumeRoisFromExtremaParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-rois-from-extrema")
    cargs.append(execution.input_file(params.get("volume_in")))
    cargs.append(str(params.get("limit")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_gaussian_sigma") is not None:
        cargs.extend([
            "-gaussian",
            str(params.get("opt_gaussian_sigma"))
        ])
    if params.get("opt_roi_roi_volume") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_volume"))
        ])
    if params.get("opt_overlap_logic_method") is not None:
        cargs.extend([
            "-overlap-logic",
            params.get("opt_overlap_logic_method")
        ])
    if params.get("opt_subvolume_subvol") is not None:
        cargs.extend([
            "-subvolume",
            params.get("opt_subvolume_subvol")
        ])
    return cargs


def volume_rois_from_extrema_outputs(
    params: VolumeRoisFromExtremaParameters,
    execution: Execution,
) -> VolumeRoisFromExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeRoisFromExtremaOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_rois_from_extrema_execute(
    params: VolumeRoisFromExtremaParameters,
    execution: Execution,
) -> VolumeRoisFromExtremaOutputs:
    """
    Create volume roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeRoisFromExtremaOutputs`).
    """
    params = execution.params(params)
    cargs = volume_rois_from_extrema_cargs(params, execution)
    ret = volume_rois_from_extrema_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_rois_from_extrema(
    volume_in: InputPathType,
    limit: float,
    volume_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_subvolume_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeRoisFromExtremaOutputs:
    """
    Create volume roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input volume.
        limit: distance limit from voxel center, in mm.
        volume_out: the output volume.
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:\
            the sigma for the gaussian kernel, in mm.
        opt_roi_roi_volume: select a region of interest to use: the region to\
            use.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_subvolume_subvol: select a single subvolume to take the gradient\
            of: the subvolume number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeRoisFromExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ROIS_FROM_EXTREMA_METADATA)
    params = volume_rois_from_extrema_params(volume_in=volume_in, limit=limit, volume_out=volume_out, opt_gaussian_sigma=opt_gaussian_sigma, opt_roi_roi_volume=opt_roi_roi_volume, opt_overlap_logic_method=opt_overlap_logic_method, opt_subvolume_subvol=opt_subvolume_subvol)
    return volume_rois_from_extrema_execute(params, execution)


__all__ = [
    "VOLUME_ROIS_FROM_EXTREMA_METADATA",
    "VolumeRoisFromExtremaOutputs",
    "VolumeRoisFromExtremaParameters",
    "volume_rois_from_extrema",
    "volume_rois_from_extrema_params",
]
