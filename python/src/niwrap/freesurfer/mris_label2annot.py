# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_LABEL2ANNOT_METADATA = Metadata(
    id="59e49ff6cbbaf0d71f17134eac97a483503970a4.boutiques",
    name="mris_label2annot",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisLabel2annotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label2annot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    annot_file: OutputPathType
    """Generated annotation file"""


def mris_label2annot(
    subject: str,
    hemi: str,
    ctabfile: InputPathType,
    annotname: str,
    runner: Runner | None = None,
) -> MrisLabel2annotOutputs:
    """
    Converts a set of surface labels to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject.
        hemi: Hemisphere (lh or rh).
        ctabfile: Colortable file (like FreeSurferColorLUT.txt).
        annotname: Output annotation name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabel2annotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL2ANNOT_METADATA)
    cargs = []
    cargs.append("mris_label2annot")
    cargs.extend([
        "-s",
        "-" + subject
    ])
    cargs.extend([
        "-h",
        "-" + hemi
    ])
    cargs.extend([
        "-ctab",
        "-" + execution.input_file(ctabfile)
    ])
    cargs.extend([
        "-a",
        "-" + annotname
    ])
    cargs.append("[OPTIONAL_ARGS]")
    ret = MrisLabel2annotOutputs(
        root=execution.output_file("."),
        annot_file=execution.output_file(hemi + "." + annotname + ".annot"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_LABEL2ANNOT_METADATA",
    "MrisLabel2annotOutputs",
    "mris_label2annot",
]
