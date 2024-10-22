# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMAGE_STATS_METADATA = Metadata(
    id="e9c8953a1ff0df76630358481fd6fb61fd92bba6.boutiques",
    name="ImageStats",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class ImageStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `image_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_stat: OutputPathType
    """Any value. Stats output."""


def image_stats(
    in_file: InputPathType,
    op_string: str,
    split_4d: bool = False,
    index_mask_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    runner: Runner | None = None,
) -> ImageStatsOutputs:
    """
    Use FSL fslstats command to calculate stats from images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input file to generate stats of.
        op_string: String defining the operation, options are applied in order,\
            e.g. -m -l 10 -m will report the non-zero mean, apply a threshold and\
            then report the new nonzero mean.
        split_4d: Give a separate output line for each 3d volume of a 4d\
            timeseries.
        index_mask_file: Generate separate n submasks from indexmask, for\
            indexvalues 1..n where n is the maximum index value in indexmask, and\
            generate statistics for each submask.
        mask_file: Mask file used for option -k %s.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImageStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMAGE_STATS_METADATA)
    cargs = []
    cargs.append("ImageStats")
    if split_4d:
        cargs.append("-t")
    if index_mask_file is not None:
        cargs.extend([
            "-K",
            execution.input_file(index_mask_file)
        ])
    cargs.append(execution.input_file(in_file))
    cargs.append(op_string)
    if mask_file is not None:
        cargs.append(execution.input_file(mask_file))
    if output_type is not None:
        cargs.append(output_type)
    ret = ImageStatsOutputs(
        root=execution.output_file("."),
        out_stat=execution.output_file("out_stat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMAGE_STATS_METADATA",
    "ImageStatsOutputs",
    "image_stats",
]
