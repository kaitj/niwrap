# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SURFACE_STATS_METADATA = Metadata(
    id="a615c38b1e647ea0789fa48d75a57ab954bd3b51.boutiques",
    name="mris_surface_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisSurfaceStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_surface_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    std_output: OutputPathType
    """Standard deviation map of the input thickness difference maps"""
    mean_output: OutputPathType | None
    """Mean map of the input thickness difference maps"""
    absmean_output: OutputPathType | None
    """Absolute mean map of the input thickness difference maps"""
    absstd_output: OutputPathType | None
    """Standard deviation map of the absolute differences"""
    zscore_output: OutputPathType | None
    """Z-score map of the input thickness difference maps"""


def mris_surface_stats(
    surf_name: InputPathType,
    out_name: str,
    data_files: list[InputPathType],
    nsmooth: float | None = None,
    mask_name: InputPathType | None = None,
    mean: str | None = None,
    absmean: str | None = None,
    absstd: str | None = None,
    zscore: str | None = None,
    first_group_size: float | None = None,
    src_type: str | None = None,
    trg_type: str | None = None,
    debug: float | None = None,
    runner: Runner | None = None,
) -> MrisSurfaceStatsOutputs:
    """
    Computes the group-wise mean and standard deviation of thickness differences at
    every vertex of the template surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surf_name: Set the surface filename.
        out_name: Set the output filename (standard deviation of data).
        data_files: List of input data files for computation.
        nsmooth: Specify number of smoothing steps.
        mask_name: Set the filename for surface mask.
        mean: Set the output filename for mean.
        absmean: Set the output filename for absolute mean.
        absstd: Set the output filename for standard deviation of absolute mean.
        zscore: Set the output filename for z-score (only if first_group_size >\
            0).
        first_group_size: Specify how many subjects at the beginning belong to\
            first group.
        src_type: Input surface data format (default = paint).
        trg_type: Output format (default = paint).
        debug: Specify which surface vertex number to debug.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSurfaceStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SURFACE_STATS_METADATA)
    cargs = []
    cargs.append("mris_surface_stats")
    if nsmooth is not None:
        cargs.extend([
            "-nsmooth",
            str(nsmooth)
        ])
    cargs.extend([
        "-surf_name",
        execution.input_file(surf_name)
    ])
    if mask_name is not None:
        cargs.extend([
            "-mask_name",
            execution.input_file(mask_name)
        ])
    cargs.extend([
        "-out_name",
        out_name
    ])
    if mean is not None:
        cargs.extend([
            "-mean",
            mean
        ])
    if absmean is not None:
        cargs.extend([
            "-absmean",
            absmean
        ])
    if absstd is not None:
        cargs.extend([
            "-absstd",
            absstd
        ])
    if zscore is not None:
        cargs.extend([
            "-zscore",
            zscore
        ])
    if first_group_size is not None:
        cargs.extend([
            "-first_group_size",
            str(first_group_size)
        ])
    if src_type is not None:
        cargs.extend([
            "-src_type",
            src_type
        ])
    if trg_type is not None:
        cargs.extend([
            "-trg_type",
            trg_type
        ])
    if debug is not None:
        cargs.extend([
            "-debug",
            str(debug)
        ])
    cargs.extend([execution.input_file(f) for f in data_files])
    ret = MrisSurfaceStatsOutputs(
        root=execution.output_file("."),
        std_output=execution.output_file(out_name),
        mean_output=execution.output_file(mean) if (mean is not None) else None,
        absmean_output=execution.output_file(absmean) if (absmean is not None) else None,
        absstd_output=execution.output_file(absstd) if (absstd is not None) else None,
        zscore_output=execution.output_file(zscore) if (zscore is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_SURFACE_STATS_METADATA",
    "MrisSurfaceStatsOutputs",
    "mris_surface_stats",
]