# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_ORIENT_SIGN_METADATA = Metadata(
    id="00274662998dcb521547fcdff2a1a41db4f7d529.boutiques",
    name="AfniOrientSign",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniOrientSignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_orient_sign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the orientation signs of the dataset"""


def afni_orient_sign(
    infile: InputPathType,
    runner: Runner | None = None,
) -> AfniOrientSignOutputs:
    """
    A tool within the AFNI suite to determine the orientation signs of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input image file to determine orientation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniOrientSignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_ORIENT_SIGN_METADATA)
    cargs = []
    cargs.append("3dinfo")
    cargs.append("-orient")
    cargs.append(execution.input_file(infile))
    ret = AfniOrientSignOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(pathlib.Path(infile).name + "_orient.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_ORIENT_SIGN_METADATA",
    "AfniOrientSignOutputs",
    "afni_orient_sign",
]
