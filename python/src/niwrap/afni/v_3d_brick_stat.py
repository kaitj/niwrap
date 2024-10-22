# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_BRICK_STAT_METADATA = Metadata(
    id="2171879e0c09931b6800be575110e0354a0a8e86.boutiques",
    name="3dBrickStat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dBrickStatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_brick_stat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    console_output: OutputPathType
    """Console output of computed statistics"""


def v_3d_brick_stat(
    dataset: str,
    quick: bool = False,
    slow: bool = False,
    min_: bool = False,
    max_: bool = False,
    mean: bool = False,
    sum_: bool = False,
    var: bool = False,
    stdev: bool = False,
    count: bool = False,
    volume: bool = False,
    positive: bool = False,
    negative: bool = False,
    zero: bool = False,
    non_positive: bool = False,
    non_negative: bool = False,
    non_zero: bool = False,
    absolute: bool = False,
    nan: bool = False,
    nonan: bool = False,
    mask: str | None = None,
    mrange: list[float] | None = None,
    mvalue: float | None = None,
    automask: bool = False,
    percentile: list[float] | None = None,
    perclist: list[float] | None = None,
    median: bool = False,
    perc_quiet: bool = False,
    ver: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> V3dBrickStatOutputs:
    """
    Compute voxel statistics of an input dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        quick: Get the information from the header only (default).
        slow: Read the whole dataset to find the min and max values.
        min_: Print the minimum value in dataset.
        max_: Print the maximum value in dataset (default).
        mean: Print the mean value in dataset.
        sum_: Print the sum of values in the dataset.
        var: Print the variance in the dataset.
        stdev: Print the standard deviation in the dataset.
        count: Print the number of voxels included.
        volume: Print the volume of voxels included in microliters.
        positive: Include only positive voxel values.
        negative: Include only negative voxel values.
        zero: Include only zero voxel values.
        non_positive: Include only voxel values 0 or negative.
        non_negative: Include only voxel values 0 or greater.
        non_zero: Include only voxel values not equal to 0.
        absolute: Use absolute value of voxel values for all calculations.
        nan: Include only voxel values that are NaN or inf. Forces -slow mode.
        nonan: Exclude voxel values that are NaN or inf.
        mask: Use the specified dataset as mask to include/exclude voxels.
        mrange: Only accept values between MIN and MAX (inclusive) from the\
            mask.
        mvalue: Only accept values equal to VAL from the mask.
        automask: Automatically compute mask for dataset. Cannot be combined\
            with -mask.
        percentile: Compute and print percentile values from p0% to p1% at a\
            step of ps%. Only one sub-brick is accepted as input with this option.
        perclist: Like -percentile, but output the given percentiles.
        median: Shortcut for -percentile 50 1 50 (or -perclist 1 50).
        perc_quiet: Only print percentile results, not input percentile cutoffs.
        ver: Print author and version info.
        help_: Print help screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBrickStatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BRICK_STAT_METADATA)
    cargs = []
    cargs.append("3dBrickStat")
    cargs.append(dataset)
    if quick:
        cargs.append("-quick")
    if slow:
        cargs.append("-slow")
    if min_:
        cargs.append("-min")
    if max_:
        cargs.append("-max")
    if mean:
        cargs.append("-mean")
    if sum_:
        cargs.append("-sum")
    if var:
        cargs.append("-var")
    if stdev:
        cargs.append("-stdev")
    if count:
        cargs.append("-count")
    if volume:
        cargs.append("-volume")
    if positive:
        cargs.append("-positive")
    if negative:
        cargs.append("-negative")
    if zero:
        cargs.append("-zero")
    if non_positive:
        cargs.append("-non-positive")
    if non_negative:
        cargs.append("-non-negative")
    if non_zero:
        cargs.append("-non-zero")
    if absolute:
        cargs.append("-absolute")
    if nan:
        cargs.append("-nan")
    if nonan:
        cargs.append("-nonan")
    if mask is not None:
        cargs.extend([
            "-mask",
            mask
        ])
    if mrange is not None:
        cargs.extend([
            "-mrange",
            *map(str, mrange)
        ])
    if mvalue is not None:
        cargs.extend([
            "-mvalue",
            str(mvalue)
        ])
    if automask:
        cargs.append("-automask")
    if percentile is not None:
        cargs.extend([
            "-percentile",
            *map(str, percentile)
        ])
    if perclist is not None:
        cargs.extend([
            "-perclist",
            *map(str, perclist)
        ])
    if median:
        cargs.append("-median")
    if perc_quiet:
        cargs.append("-perc_quiet")
    if ver:
        cargs.append("-ver")
    if help_:
        cargs.append("-help")
    ret = V3dBrickStatOutputs(
        root=execution.output_file("."),
        console_output=execution.output_file("output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBrickStatOutputs",
    "V_3D_BRICK_STAT_METADATA",
    "v_3d_brick_stat",
]
