# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_FDR_METADATA = Metadata(
    id="052b0ab8a12acc2def2e27ee40fa90c4b23263c0.boutiques",
    name="3dFDR",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dFdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_fdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType
    """Output dataset in BRIK format"""
    output_head: OutputPathType
    """Output dataset in HEAD format"""
    output_1d: OutputPathType
    """Output list of voxel q-values"""


def v_3d_fdr(
    input_file: InputPathType,
    prefix: str,
    mask_file: InputPathType | None = None,
    mask_threshold: float | None = None,
    constant_type: typing.Literal["cind", "cdep"] | None = None,
    quiet: bool = False,
    list_: bool = False,
    mode_option: typing.Literal["old", "new"] | None = None,
    pmask: bool = False,
    nopmask: bool = False,
    force: bool = False,
    float_: bool = False,
    qval: bool = False,
    runner: Runner | None = None,
) -> V3dFdrOutputs:
    """
    A tool for applying False Discovery Rate (FDR) thresholding to voxelwise
    statistics in 3D functional datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input 3D functional dataset filename.
        prefix: Use 'pname' for the output dataset prefix name.
        mask_file: Use mask values from file mname. If file mname contains more\
            than 1 sub-brick, the mask sub-brick must be specified. Generally\
            should be used to avoid counting non-brain voxels.
        mask_threshold: Only voxels whose corresponding mask value is greater\
            than or equal to the specified value in absolute terms will be\
            considered. Default is 1.
        constant_type: Set constant c(N): 1 for independent p-values (default)\
            or sum(1/i, i=1,...,N) for any joint distribution.
        quiet: Suppress screen output.
        list_: Write sorted list of voxel q-values to screen.
        mode_option: Use the old or new mode of operation. 'new' is now the\
            default.
        pmask: Ignore p=1 voxels (default in new mode).
        nopmask: Count p=1 voxels (default in old mode).
        force: Force conversion of all sub-bricks, treating them as p-values.
        float_: Force the output of z-scores in floating point format.
        qval: Force the output of q-values rather than z-scores.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dFdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_FDR_METADATA)
    cargs = []
    cargs.append("3dFDR")
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    if mask_file is not None:
        cargs.extend([
            "-mask_file",
            execution.input_file(mask_file)
        ])
    if mask_threshold is not None:
        cargs.extend([
            "-mask_thr",
            str(mask_threshold)
        ])
    if constant_type is not None:
        cargs.extend([
            "-c",
            constant_type
        ])
    if quiet:
        cargs.append("-quiet")
    if list_:
        cargs.append("-list")
    cargs.extend([
        "-prefix",
        prefix
    ])
    if mode_option is not None:
        cargs.extend([
            "-",
            mode_option
        ])
    if pmask:
        cargs.append("-pmask")
    if nopmask:
        cargs.append("-nopmask")
    if force:
        cargs.append("-force")
    if float_:
        cargs.append("-float")
    if qval:
        cargs.append("-qval")
    ret = V3dFdrOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(prefix + "+orig.BRIK"),
        output_head=execution.output_file(prefix + "+orig.HEAD"),
        output_1d=execution.output_file(prefix + ".1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dFdrOutputs",
    "V_3D_FDR_METADATA",
    "v_3d_fdr",
]
