# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA = Metadata(
    id="255cbc9bcd0a4cdb77830871dfed14d27befa862.boutiques",
    name="SegmentSubfieldsT1Longitudinal",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SegmentSubfieldsT1LongitudinalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subfields_t1_longitudinal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Output file containing the segmented subfields"""


def segment_subfields_t1_longitudinal(
    subject_id: str,
    input_image: InputPathType,
    output_dir: str,
    runner: Runner | None = None,
) -> SegmentSubfieldsT1LongitudinalOutputs:
    """
    FreeSurfer tool for segmenting subfields in longitudinal T1-weighted images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID for the longitudinal analysis.
        input_image: Input T1-weighted image.
        output_dir: Directory to save the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubfieldsT1LongitudinalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA)
    cargs = []
    cargs.append("SegmentSubfieldsT1Longitudinal")
    cargs.append(subject_id)
    cargs.append(execution.input_file(input_image))
    cargs.append(output_dir)
    ret = SegmentSubfieldsT1LongitudinalOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(output_dir + "/subfields_segmentation.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_SUBFIELDS_T1_LONGITUDINAL_METADATA",
    "SegmentSubfieldsT1LongitudinalOutputs",
    "segment_subfields_t1_longitudinal",
]