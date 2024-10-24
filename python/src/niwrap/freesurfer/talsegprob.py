# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TALSEGPROB_METADATA = Metadata(
    id="ddb70e26f179b8729ed68da2fa771aa79e55b360.boutiques",
    name="talsegprob",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TalsegprobOutputs(typing.NamedTuple):
    """
    Output object returned when calling `talsegprob(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_output_file: OutputPathType | None
    """Probability output file."""
    vote_output_file: OutputPathType | None
    """Vote output file."""
    concat_output_file: OutputPathType | None
    """Concatenated output file."""


def talsegprob(
    subjects_list: list[str] | None = None,
    fsgd_file: InputPathType | None = None,
    segmentation_number: float | None = None,
    second_segmentation_number: float | None = None,
    hippo_flag: bool = False,
    left_hippo_flag: bool = False,
    right_hippo_flag: bool = False,
    segmentation_file: InputPathType | None = None,
    probability_output: str | None = None,
    vote_output: str | None = None,
    concat_output: str | None = None,
    xform_file: InputPathType | None = None,
    subjects_dir: str | None = None,
    tmpdir: str | None = None,
    nocleanup_flag: bool = False,
    version_flag: bool = False,
    echo_flag: bool = False,
    runner: Runner | None = None,
) -> TalsegprobOutputs:
    """
    Tool to create a binary probability volume from aseg.mgz based on segmentation
    numbers, resliced to talirach/MNI305/fsaverage space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_list: List of subjects to include in the analysis.
        fsgd_file: FSGD file to get subject list.
        segmentation_number: Segmentation number.
        second_segmentation_number: Second segmentation number.
        hippo_flag: Use segmentation numbers 17 and 53.
        left_hippo_flag: Use segmentation number 17.
        right_hippo_flag: Use segmentation number 53.
        segmentation_file: Use subject/mri/segfile.mgz instead of aseg.
        probability_output: Probability output file name.
        vote_output: Vote output file name.
        concat_output: Concatenated output file name.
        xform_file: Transformation file to use (default is talairach.xfm).
        subjects_dir: SUBJECTS_DIR to use instead of the one in the\
            environment.
        tmpdir: Temporary directory (implies --nocleanup).
        nocleanup_flag: Do not delete temporary directory.
        version_flag: Display script version information.
        echo_flag: Enable command echo, for debug.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TalsegprobOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALSEGPROB_METADATA)
    cargs = []
    cargs.append("talsegprob")
    if subjects_list is not None:
        cargs.extend([
            "--subjects",
            *subjects_list
        ])
    if fsgd_file is not None:
        cargs.extend([
            "--fsgd",
            execution.input_file(fsgd_file)
        ])
    if segmentation_number is not None:
        cargs.extend([
            "--seg",
            str(segmentation_number)
        ])
    if second_segmentation_number is not None:
        cargs.extend([
            "<--seg",
            str(second_segmentation_number)
        ])
    if hippo_flag:
        cargs.append("--hippo")
    if left_hippo_flag:
        cargs.append("--left-hippo")
    if right_hippo_flag:
        cargs.append("--right-hippo")
    if segmentation_file is not None:
        cargs.extend([
            "--segmentation",
            execution.input_file(segmentation_file)
        ])
    if probability_output is not None:
        cargs.extend([
            "--p",
            probability_output
        ])
    if vote_output is not None:
        cargs.extend([
            "--vote",
            vote_output
        ])
    if concat_output is not None:
        cargs.extend([
            "--c",
            concat_output
        ])
    if xform_file is not None:
        cargs.extend([
            "--xform",
            execution.input_file(xform_file)
        ])
    if subjects_dir is not None:
        cargs.extend([
            "--sdir",
            subjects_dir
        ])
    if tmpdir is not None:
        cargs.extend([
            "--tmpdir",
            tmpdir
        ])
    if nocleanup_flag:
        cargs.append("--nocleanup")
    if version_flag:
        cargs.append("--version")
    if echo_flag:
        cargs.append("--echo")
    ret = TalsegprobOutputs(
        root=execution.output_file("."),
        probability_output_file=execution.output_file(probability_output) if (probability_output is not None) else None,
        vote_output_file=execution.output_file(vote_output) if (vote_output is not None) else None,
        concat_output_file=execution.output_file(concat_output) if (concat_output is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TALSEGPROB_METADATA",
    "TalsegprobOutputs",
    "talsegprob",
]
