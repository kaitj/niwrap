# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_SUBJECT_LH_METADATA = Metadata(
    id="7d0356b3f6c9aa3f4b85726ed2a881ba4666df16.boutiques",
    name="morph_subject-lh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MorphSubjectLhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_subject_lh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def morph_subject_lh(
    subject_id: str,
    runner: Runner | None = None,
) -> MorphSubjectLhOutputs:
    """
    A tool for morphing subject's left hemisphere.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject ID.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphSubjectLhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_SUBJECT_LH_METADATA)
    cargs = []
    cargs.append("morph_subject-lh")
    cargs.append(subject_id)
    ret = MorphSubjectLhOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MORPH_SUBJECT_LH_METADATA",
    "MorphSubjectLhOutputs",
    "morph_subject_lh",
]