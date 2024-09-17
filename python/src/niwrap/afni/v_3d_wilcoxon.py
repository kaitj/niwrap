# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_WILCOXON_METADATA = Metadata(
    id="1ddbc2035d19f145ab6100e67855886ee6882f0b.boutiques",
    name="3dWilcoxon",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dWilcoxonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_wilcoxon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Estimated population delta and Wilcoxon signed-rank statistics"""


def v_3d_wilcoxon(
    dset1_x: list[InputPathType],
    dset2_y: list[InputPathType],
    output_prefix: str,
    workmem: float | None = None,
    voxel: float | None = None,
    runner: Runner | None = None,
) -> V3dWilcoxonOutputs:
    """
    Nonparametric Wilcoxon signed-rank test for paired comparisons of two samples.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dWilcoxon.html
    
    Args:
        dset1_x: Data set for X observations. The user must specify 1 and only\
            1 sub-brick with each -dset command.
        dset2_y: Data set for Y observations. The user must specify 1 and only\
            1 sub-brick with each -dset command.
        output_prefix: Estimated population delta and Wilcoxon signed-rank\
            statistics are written to file.
        workmem: Number of megabytes of RAM to use for statistical workspace.
        voxel: Screen output for voxel # num.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dWilcoxonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_WILCOXON_METADATA)
    cargs = []
    cargs.append("3dWilcoxon")
    if workmem is not None:
        cargs.extend([
            "-workmem",
            str(workmem)
        ])
    if voxel is not None:
        cargs.extend([
            "-voxel",
            str(voxel)
        ])
    cargs.append("-dset")
    cargs.append("1")
    cargs.extend([execution.input_file(f) for f in dset1_x])
    cargs.append("-dset")
    cargs.append("2")
    cargs.extend([execution.input_file(f) for f in dset2_y])
    cargs.append("-out")
    cargs.extend([
        "-out",
        output_prefix
    ])
    ret = V3dWilcoxonOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_prefix),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dWilcoxonOutputs",
    "V_3D_WILCOXON_METADATA",
    "v_3d_wilcoxon",
]