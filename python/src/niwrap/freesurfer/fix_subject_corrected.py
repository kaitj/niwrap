# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIX_SUBJECT_CORRECTED_METADATA = Metadata(
    id="e9683c6b2300288726f90faacf8034788b095c6c.boutiques",
    name="fix_subject_corrected",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FixSubjectCorrectedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fix_subject_corrected(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fix_subject_corrected(
    subject_directory: str,
    output_directory: str,
    runner: Runner | None = None,
) -> FixSubjectCorrectedOutputs:
    """
    Corrects subject data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_directory: Path to the subject's directory.
        output_directory: Path to the output directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixSubjectCorrectedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIX_SUBJECT_CORRECTED_METADATA)
    cargs = []
    cargs.append("fix_subject_corrected")
    cargs.append(subject_directory)
    cargs.append(output_directory)
    ret = FixSubjectCorrectedOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIX_SUBJECT_CORRECTED_METADATA",
    "FixSubjectCorrectedOutputs",
    "fix_subject_corrected",
]
