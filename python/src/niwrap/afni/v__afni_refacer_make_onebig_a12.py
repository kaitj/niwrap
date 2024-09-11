# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA = Metadata(
    id="f333abd3f2327025fd4bba049bf71d844b0709cd.boutiques",
    name="@afni_refacer_make_onebigA12",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VAfniRefacerMakeOnebigA12Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_refacer_make_onebig_a12(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_output: OutputPathType
    """Aligned T1w dataset to MNI template with expanded 'big' grid"""


def v__afni_refacer_make_onebig_a12(
    t1w_dataset: InputPathType,
    runner: Runner | None = None,
) -> VAfniRefacerMakeOnebigA12Outputs:
    """
    Script to align a single T1w dataset to the MNI template and expand it to a
    'big' grid.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_refacer_make_onebigA12.html
    
    Args:
        t1w_dataset: Input T1w dataset name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRefacerMakeOnebigA12Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA)
    cargs = []
    cargs.append("@afni_refacer_make_onebigA12")
    cargs.append(execution.input_file(t1w_dataset))
    ret = VAfniRefacerMakeOnebigA12Outputs(
        root=execution.output_file("."),
        aligned_output=execution.output_file(pathlib.Path(t1w_dataset).name + "_aligned_to_MNI.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniRefacerMakeOnebigA12Outputs",
    "V__AFNI_REFACER_MAKE_ONEBIG_A12_METADATA",
    "v__afni_refacer_make_onebig_a12",
]