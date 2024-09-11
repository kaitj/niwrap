# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIENAX_METADATA = Metadata(
    id="931f38e911c30e3bcdcfd92c1fbcde8da5cd8b46.boutiques",
    name="sienax",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SienaxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sienax(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType | None
    """Segmentation output file"""
    report_output: OutputPathType | None
    """Summary report file"""


def sienax(
    infile: InputPathType,
    output_dir: str | None = None,
    debug_flag: bool = False,
    bet_options: str | None = None,
    twoclass_segment_flag: bool = False,
    t2_flag: bool = False,
    top_threshold: float | None = None,
    bottom_threshold: float | None = None,
    regional_flag: bool = False,
    lesion_mask: InputPathType | None = None,
    fast_options: str | None = None,
    runner: Runner | None = None,
) -> SienaxOutputs:
    """
    A tool to estimate brain tissue volume from a single MR image and to compare it
    to an external standard.
    
    Author: FMRIB Centre, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/SIENA/SienaX
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        output_dir: Output directory (default output is <input>_sienax).
        debug_flag: Debug (don't delete intermediate files).
        bet_options: Options to pass to BET brain extraction (inside\
            double-quotes), e.g. -B "-f 0.3".
        twoclass_segment_flag: Two-class segmentation (don't segment grey and\
            white matter separately).
        t2_flag: Input image is T2-weighted (default is T1-weighted).
        top_threshold: Ignore from t (mm) upwards in MNI152/Talairach space.
        bottom_threshold: Ignore from b (mm) downwards in MNI152/Talairach\
            space (b should probably be negative).
        regional_flag: Regional - use standard-space masks to give peripheral\
            cortex GM volume (3-class segmentation only) and ventricular CSF volume.
        lesion_mask: Use lesion (or lesion+CSF) mask to remove incorrectly\
            labelled 'grey matter' voxels.
        fast_options: Options to pass to FAST segmentation (inside\
            double-quotes), e.g. -S "I 20".
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENAX_METADATA)
    cargs = []
    cargs.append("sienax")
    cargs.append(execution.input_file(infile))
    if output_dir is not None:
        cargs.extend([
            "-o",
            output_dir
        ])
    if debug_flag:
        cargs.append("-d")
    if bet_options is not None:
        cargs.extend([
            "-B",
            bet_options
        ])
    if twoclass_segment_flag:
        cargs.append("-2")
    if t2_flag:
        cargs.append("-t2")
    if top_threshold is not None:
        cargs.extend([
            "-t",
            str(top_threshold)
        ])
    if bottom_threshold is not None:
        cargs.extend([
            "-b",
            str(bottom_threshold)
        ])
    if regional_flag:
        cargs.append("-r")
    if lesion_mask is not None:
        cargs.extend([
            "-lm",
            execution.input_file(lesion_mask)
        ])
    if fast_options is not None:
        cargs.extend([
            "-S",
            fast_options
        ])
    ret = SienaxOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(output_dir + "/segmentation.nii.gz") if (output_dir is not None) else None,
        report_output=execution.output_file(output_dir + "/report.txt") if (output_dir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENAX_METADATA",
    "SienaxOutputs",
    "sienax",
]