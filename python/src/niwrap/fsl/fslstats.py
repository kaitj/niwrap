# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSTATS_METADATA = Metadata(
    id="016440e3fb016cdcb22ca2ec304960d4e4b83af3.boutiques",
    name="fslstats",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_stats: OutputPathType
    """Statistics output file"""


def fslstats(
    input_file: InputPathType,
    index_mask: InputPathType | None = None,
    lower_threshold: float | None = None,
    upper_threshold: float | None = None,
    robust_intensity_flag: bool = False,
    minmax_intensity_flag: bool = False,
    voxels_volume_flag: bool = False,
    nonzero_voxels_volume_flag: bool = False,
    mean_flag: bool = False,
    nonzero_mean_flag: bool = False,
    std_dev_flag: bool = False,
    nonzero_std_dev_flag: bool = False,
    smallest_roi_flag: bool = False,
    max_coords_flag: bool = False,
    min_coords_flag: bool = False,
    cog_mm_flag: bool = False,
    cog_voxel_flag: bool = False,
    percentile: float | None = None,
    nonzero_percentile: float | None = None,
    absolute_values_flag: bool = False,
    nan_as_zero_flag: bool = False,
    mask_image: InputPathType | None = None,
    difference_image: InputPathType | None = None,
    hist_bins: float | None = None,
    hist_bins_min_max: str | None = None,
    timeseries_flag: bool = False,
    mean_entropy_flag: bool = False,
    nonzero_mean_entropy_flag: bool = False,
    runner: Runner | None = None,
) -> FslstatsOutputs:
    """
    FSL tool for calculating statistics on image data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image file (e.g., image.nii.gz).
        index_mask: Generate separate n submasks from indexMask, for\
            indexvalues 1..n where n is the maximum index value in indexMask, and\
            generate statistics for each submask.
        lower_threshold: Set lower threshold.
        upper_threshold: Set upper threshold.
        robust_intensity_flag: Output robust min and max intensity.
        minmax_intensity_flag: Output min and max intensity.
        voxels_volume_flag: Output voxels and volume.
        nonzero_voxels_volume_flag: Output voxels and volume (for nonzero\
            voxels).
        mean_flag: Output mean.
        nonzero_mean_flag: Output mean (for nonzero voxels).
        std_dev_flag: Output standard deviation.
        nonzero_std_dev_flag: Output standard deviation (for nonzero voxels).
        smallest_roi_flag: Output smallest ROI containing nonzero voxels.
        max_coords_flag: Output coordinates of maximum voxel.
        min_coords_flag: Output coordinates of minimum voxel.
        cog_mm_flag: Output center-of-gravity (cog) in mm coordinates.
        cog_voxel_flag: Output center-of-gravity (cog) in voxel coordinates.
        percentile: Output nth percentile.
        nonzero_percentile: Output nth percentile (for nonzero voxels).
        absolute_values_flag: Use absolute values of all image intensities.
        nan_as_zero_flag: Treat NaN or Inf as zero for subsequent stats.
        mask_image: Use the specified image for masking - overrides lower and\
            upper thresholds.
        difference_image: Take the difference between the base image and the\
            image specified here.
        hist_bins: Output a histogram for the thresholded/masked voxels only\
            with specified number of bins.
        hist_bins_min_max: Output a histogram for the thresholded/masked voxels\
            only with specified number of bins and histogram limits of min and max.
        timeseries_flag: Separate output line for each 3D volume of a 4D\
            timeseries.
        mean_entropy_flag: Output mean entropy; mean(-i*ln(i)).
        nonzero_mean_entropy_flag: Output mean entropy (of nonzero voxels).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSTATS_METADATA)
    cargs = []
    cargs.append("fslstats")
    cargs.append(execution.input_file(input_file))
    if index_mask is not None:
        cargs.extend([
            "-K",
            execution.input_file(index_mask)
        ])
    if lower_threshold is not None:
        cargs.extend([
            "-l",
            str(lower_threshold)
        ])
    if upper_threshold is not None:
        cargs.extend([
            "-u",
            str(upper_threshold)
        ])
    if robust_intensity_flag:
        cargs.append("-r")
    if minmax_intensity_flag:
        cargs.append("-R")
    if voxels_volume_flag:
        cargs.append("-v")
    if nonzero_voxels_volume_flag:
        cargs.append("-V")
    if mean_flag:
        cargs.append("-m")
    if nonzero_mean_flag:
        cargs.append("-M")
    if std_dev_flag:
        cargs.append("-s")
    if nonzero_std_dev_flag:
        cargs.append("-S")
    if smallest_roi_flag:
        cargs.append("-w")
    if max_coords_flag:
        cargs.append("-x")
    if min_coords_flag:
        cargs.append("-X")
    if cog_mm_flag:
        cargs.append("-c")
    if cog_voxel_flag:
        cargs.append("-C")
    if percentile is not None:
        cargs.extend([
            "-p",
            str(percentile)
        ])
    if nonzero_percentile is not None:
        cargs.extend([
            "-P",
            str(nonzero_percentile)
        ])
    if absolute_values_flag:
        cargs.append("-a")
    if nan_as_zero_flag:
        cargs.append("-n")
    if mask_image is not None:
        cargs.extend([
            "-k",
            execution.input_file(mask_image)
        ])
    if difference_image is not None:
        cargs.extend([
            "-d",
            execution.input_file(difference_image)
        ])
    if hist_bins is not None:
        cargs.extend([
            "-h",
            str(hist_bins)
        ])
    if hist_bins_min_max is not None:
        cargs.extend([
            "-H",
            hist_bins_min_max
        ])
    if timeseries_flag:
        cargs.append("-t")
    if mean_entropy_flag:
        cargs.append("-e")
    if nonzero_mean_entropy_flag:
        cargs.append("-E")
    ret = FslstatsOutputs(
        root=execution.output_file("."),
        output_stats=execution.output_file(pathlib.Path(input_file).name + "_stats.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSTATS_METADATA",
    "FslstatsOutputs",
    "fslstats",
]
