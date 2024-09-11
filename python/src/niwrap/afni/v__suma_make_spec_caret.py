# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_MAKE_SPEC_CARET_METADATA = Metadata(
    id="51ff878f5f2952a5ca43b33050e7b7c540ec84d6.boutiques",
    name="@SUMA_Make_Spec_Caret",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VSumaMakeSpecCaretOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_make_spec_caret(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    left_hemisphere_spec: OutputPathType
    """Output spec file for the left hemisphere"""
    right_hemisphere_spec: OutputPathType
    """Output spec file for the right hemisphere"""


def v__suma_make_spec_caret(
    subject_id: str,
    runner: Runner | None = None,
) -> VSumaMakeSpecCaretOutputs:
    """
    Prepare surfaces for viewing in SUMA, tested with Caret-5.2 surfaces.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@SUMA_Make_Spec_Caret.html
    
    Args:
        subject_id: Subject ID for file naming.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecCaretOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_MAKE_SPEC_CARET_METADATA)
    cargs = []
    cargs.append("@SUMA_Make_Spec_Caret")
    cargs.append("[OPTIONS]")
    cargs.append("-sid")
    cargs.extend([
        "-sid",
        subject_id
    ])
    ret = VSumaMakeSpecCaretOutputs(
        root=execution.output_file("."),
        left_hemisphere_spec=execution.output_file(subject_id + "_lh.spec"),
        right_hemisphere_spec=execution.output_file(subject_id + "_rh.spec"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSumaMakeSpecCaretOutputs",
    "V__SUMA_MAKE_SPEC_CARET_METADATA",
    "v__suma_make_spec_caret",
]