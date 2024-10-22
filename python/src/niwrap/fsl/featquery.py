# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FEATQUERY_METADATA = Metadata(
    id="e0857c89efe3dc65e9e7c5ae1d214d90f31388fc.boutiques",
    name="featquery",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FeatqueryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `featquery(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    query_report: OutputPathType
    """Generated query report file"""


def featquery(
    n_featdirs: float,
    featdirs: list[str],
    n_stats: float,
    stats: list[str],
    output_rootname: str,
    mask_file: InputPathType,
    atlas_flag: str | None = None,
    percent_convert_flag: bool = False,
    thresh_flag: bool = False,
    interp_thresh: float | None = 0.5,
    timeseries_flag: bool = False,
    weight_flag: bool = False,
    browser_flag: bool = False,
    coords: list[float] | None = None,
    runner: Runner | None = None,
) -> FeatqueryOutputs:
    """
    Tool to extract statistics and/or time series from FEAT directories.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        n_featdirs: Number of feat directories.
        featdirs: List of feat directories.
        n_stats: Number of stats to query.
        stats: List of stats.
        output_rootname: Root name for output files.
        mask_file: Mask file used as a reference for coordinates; if relative,\
            searched within each FEAT directory.
        atlas_flag: Use selected atlas to generate label (etc.) information.
        percent_convert_flag: Convert PE / COPE values into percentages.
        thresh_flag: Threshold stats images.
        interp_thresh: Affect size of resampled masks by changing\
            post-interpolation thresholding (default 0.5).
        timeseries_flag: Create time-series plots.
        weight_flag: Do not binarise mask (allow weighting).
        browser_flag: Popup results in browser when finished.
        coords: Coordinates specified in voxels (X Y Z).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FeatqueryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FEATQUERY_METADATA)
    cargs = []
    cargs.append("featquery")
    cargs.append(str(n_featdirs))
    cargs.extend(featdirs)
    cargs.append(str(n_stats))
    cargs.extend(stats)
    cargs.append(output_rootname)
    if atlas_flag is not None:
        cargs.extend([
            "-a",
            atlas_flag
        ])
    if percent_convert_flag:
        cargs.append("-p")
    if thresh_flag:
        cargs.append("-t")
    if interp_thresh is not None:
        cargs.extend([
            "-i",
            str(interp_thresh)
        ])
    if timeseries_flag:
        cargs.append("-s")
    if weight_flag:
        cargs.append("-w")
    if browser_flag:
        cargs.append("-b")
    cargs.append(execution.input_file(mask_file))
    if coords is not None:
        cargs.extend([
            "-vox",
            *map(str, coords)
        ])
    ret = FeatqueryOutputs(
        root=execution.output_file("."),
        query_report=execution.output_file(output_rootname + "_queryreport.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FEATQUERY_METADATA",
    "FeatqueryOutputs",
    "featquery",
]
