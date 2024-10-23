# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CORRECT_SEGMENTATIONS_METADATA = Metadata(
    id="45cea5873b2b41eef7c438be147547c7c9e700a9.boutiques",
    name="mri_correct_segmentations",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriCorrectSegmentationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_correct_segmentations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_correct_segmentations(
    input_file_1: InputPathType,
    input_file_2: InputPathType,
    runner: Runner | None = None,
) -> MriCorrectSegmentationsOutputs:
    """
    Tool for correcting automated infant segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file_1: First input file for correction (e.g. segmentation file).
        input_file_2: Second input file for correction (e.g. reference file).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCorrectSegmentationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CORRECT_SEGMENTATIONS_METADATA)
    cargs = []
    cargs.append("mri_correct_segmentations")
    cargs.append(execution.input_file(input_file_1))
    cargs.append(execution.input_file(input_file_2))
    ret = MriCorrectSegmentationsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CORRECT_SEGMENTATIONS_METADATA",
    "MriCorrectSegmentationsOutputs",
    "mri_correct_segmentations",
]