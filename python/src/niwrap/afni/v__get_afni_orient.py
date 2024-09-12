# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__GET_AFNI_ORIENT_METADATA = Metadata(
    id="6aeb16aa28781e5b4982e7cc092248302d14798d.boutiques",
    name="@GetAfniOrient",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VGetAfniOrientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_orient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_orient_code: OutputPathType
    """File containing the orientation code"""


def v__get_afni_orient(
    infile: InputPathType,
    exploratory: bool = False,
    runner: Runner | None = None,
) -> VGetAfniOrientOutputs:
    """
    Returns the orient code of AFNI datasets.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@GetAfniOrient.html
    
    Args:
        infile: Input AFNI dataset (e.g. Hello+orig.HEAD).
        exploratory: Exploratory flag for additional functionalities.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniOrientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_ORIENT_METADATA)
    cargs = []
    cargs.append("@GetAfniOrient")
    if exploratory:
        cargs.append("-exp")
    cargs.append(execution.input_file(infile))
    ret = VGetAfniOrientOutputs(
        root=execution.output_file("."),
        output_orient_code=execution.output_file(pathlib.Path(infile).name + "_orient_code.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGetAfniOrientOutputs",
    "V__GET_AFNI_ORIENT_METADATA",
    "v__get_afni_orient",
]
