# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_COMPARE_AFFINE_METADATA = Metadata(
    id="e60f9cf65b751e5f6d51d1348f9d18b1103b2e2a.boutiques",
    name="3dCompareAffine",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dCompareAffineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_compare_affine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing comparison results of affine transformations"""


def v_3d_compare_affine(
    runner: Runner | None = None,
) -> V3dCompareAffineOutputs:
    """
    Compares two (or more) affine spatial transformations on a dataset and outputs
    measurements of their differences in spatial displacements.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dCompareAffine.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCompareAffineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_COMPARE_AFFINE_METADATA)
    cargs = []
    cargs.append("3dCompareAffine")
    cargs.append("[OPTIONS]")
    ret = V3dCompareAffineOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("[OUTPUT_PREFIX]_comparison.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dCompareAffineOutputs",
    "V_3D_COMPARE_AFFINE_METADATA",
    "v_3d_compare_affine",
]