# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TWOTO_COMPLEX_METADATA = Metadata(
    id="bf9493b3c937b76d0584de14a9b270a71cce9ca0.boutiques",
    name="3dTwotoComplex",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTwotoComplexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_twoto_complex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brick: OutputPathType | None
    """Output complex-valued dataset with prefix"""
    out_head: OutputPathType | None
    """Header for the complex-valued dataset"""


def v_3d_twoto_complex(
    dataset1: InputPathType,
    dataset2: InputPathType | None = None,
    prefix: str | None = None,
    ri: bool = False,
    mp: bool = False,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dTwotoComplexOutputs:
    """
    Converts 2 sub-bricks of input to a complex-valued dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset1: Input dataset (either as 1 dataset with 2 sub-bricks or 2\
            separate datasets).
        dataset2: Second input dataset (optional if 2 sub-bricks in the first\
            dataset).
        prefix: Prefix for the output dataset [default='cmplx'].
        ri: Specify that the 2 inputs are real and imaginary parts [this is the\
            default].
        mp: Specify that the 2 inputs are magnitude and phase [phase is in\
            radians].
        mask: Only output nonzero values where the mask dataset is nonzero.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTwotoComplexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TWOTO_COMPLEX_METADATA)
    cargs = []
    cargs.append("3dTwotoComplex")
    cargs.append(execution.input_file(dataset1))
    if dataset2 is not None:
        cargs.append(execution.input_file(dataset2))
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if ri:
        cargs.append("-RI")
    if mp:
        cargs.append("-MP")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    ret = V3dTwotoComplexOutputs(
        root=execution.output_file("."),
        out_brick=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
        out_head=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTwotoComplexOutputs",
    "V_3D_TWOTO_COMPLEX_METADATA",
    "v_3d_twoto_complex",
]
