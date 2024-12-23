# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_MULTI_THRESH_METADATA = Metadata(
    id="ac6c6a539a206612134e8a96c0fd7291780ddc36.boutiques",
    name="3dMultiThresh",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dMultiThreshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_multi_thresh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Thresholded version of the input dataset."""
    mask_output: OutputPathType | None
    """0/1 mask dataset of voxels that survive the process."""
    all_mask_output: OutputPathType | None
    """Multi-volume dataset where each volume is the binary mask of voxels that
    pass ONE of the tests."""


def v_3d_multi_thresh(
    mthresh_file: InputPathType,
    input_file: InputPathType,
    index: float | None = None,
    signed_flag: str | None = None,
    positive_sign_flag: bool = False,
    negative_sign_flag: bool = False,
    prefix: str | None = None,
    mask_only_flag: bool = False,
    all_mask: str | None = None,
    no_zero_flag: bool = False,
    quiet_flag: bool = False,
    runner: Runner | None = None,
) -> V3dMultiThreshOutputs:
    """
    Program to apply a multi-threshold (mthresh) dataset to an input dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        mthresh_file: Multi-threshold dataset from 3dXClustSim, usually via\
            running '3dttest++ -ETAC'.
        input_file: Dataset to threshold.
        index: Index (sub-brick) on which to threshold.
        signed_flag: Indicates if the .mthresh.nii file from 3dXClustSim was\
            created using 1-sided thresholding. Choose sign + or -.
        positive_sign_flag: Same as '-signed +'.
        negative_sign_flag: Same as '-signed -'.
        prefix: Prefix for output dataset. Can be 'NULL' to get no output\
            dataset.
        mask_only_flag: Instead of outputting a thresholded version of the\
            input dataset, just output a 0/1 mask dataset of voxels that survive\
            the process.
        all_mask: Write out a multi-volume dataset with prefix 'qqq' where each\
            volume is the binary mask of voxels that pass ONE of the tests.
        no_zero_flag: Prevents the output of a dataset if it would be all zero.
        quiet_flag: Turn off progress report messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMultiThreshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MULTI_THRESH_METADATA)
    cargs = []
    cargs.append("3dMultiThresh")
    cargs.extend([
        "-mthresh",
        execution.input_file(mthresh_file)
    ])
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    if index is not None:
        cargs.extend([
            "-1tindex",
            str(index)
        ])
    if signed_flag is not None:
        cargs.extend([
            "-signed",
            signed_flag
        ])
    if positive_sign_flag:
        cargs.append("-pos")
    if negative_sign_flag:
        cargs.append("-neg")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if mask_only_flag:
        cargs.append("-maskonly")
    if all_mask is not None:
        cargs.extend([
            "-allmask",
            all_mask
        ])
    if no_zero_flag:
        cargs.append("-nozero")
    if quiet_flag:
        cargs.append("-quiet")
    ret = V3dMultiThreshOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + ".nii.gz") if (prefix is not None) else None,
        mask_output=execution.output_file(prefix + "_mask.nii.gz") if (prefix is not None) else None,
        all_mask_output=execution.output_file(all_mask + ".nii.gz") if (all_mask is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMultiThreshOutputs",
    "V_3D_MULTI_THRESH_METADATA",
    "v_3d_multi_thresh",
]
