# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DTTEST___METADATA = Metadata(
    id="33a898457760fd3e5996a7102c5222527b95b998.boutiques",
    name="3dttest++",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dttestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dttest__(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Main output dataset"""
    residuals: OutputPathType
    """Output residuals dataset"""


def v_3dttest__(
    set_b: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dttestOutputs:
    """
    Gosset (Student) t-test of sets of 3D datasets in AFNI.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dttest++.html
    
    Args:
        set_b: Set B in short form, e.g., 'x+tlrc[3]' y+tlrc[3] ...'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dttestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DTTEST___METADATA)
    cargs = []
    cargs.append("3dttest++")
    if set_b is not None:
        cargs.extend([
            "-setB",
            *set_b
        ])
    cargs.append("[OPTIONS]")
    cargs.append("[MASK_OPTIONS]")
    cargs.append("[ETAC_OPTIONS]")
    cargs.append("[OTHER_OPTIONS]")
    ret = V3dttestOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file("[PREFIX].nii.gz"),
        residuals=execution.output_file("[PREFIX_RESID].nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dttestOutputs",
    "V_3DTTEST___METADATA",
    "v_3dttest__",
]
