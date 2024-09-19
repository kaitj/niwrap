# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STANDARD_SPACE_ROI_METADATA = Metadata(
    id="9e35445d93826b3dede29dbe499d382d5e6dae42.boutiques",
    name="standard_space_roi",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class StandardSpaceRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `standard_space_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_image: OutputPathType
    """Output image after masking and/or FOV reduction"""


def standard_space_roi(
    infile: InputPathType,
    outfile: str,
    mask_fov_flag: bool = False,
    mask_mask: InputPathType | None = None,
    mask_none_flag: bool = False,
    roi_fov_flag: bool = False,
    roi_mask: InputPathType | None = None,
    roi_none_flag: bool = False,
    ss_ref: InputPathType | None = None,
    alt_input: InputPathType | None = None,
    debug_flag: bool = False,
    bet_premask_flag: bool = False,
    runner: Runner | None = None,
) -> StandardSpaceRoiOutputs:
    """
    Masks input and/or reduces its FOV based on a standard space image or mask,
    transformed into the space of the input image.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        infile: Input image.
        outfile: Output image.
        mask_fov_flag: Mask output using transformed standard space FOV.
        mask_mask: Mask output using transformed standard space mask.
        mask_none_flag: Do not mask output.
        roi_fov_flag: Cut down input FOV using bounding box of the transformed\
            standard space FOV.
        roi_mask: Cut down input FOV using nonbackground bounding box of the\
            transformed standard space mask.
        roi_none_flag: Do not cut down input FOV.
        ss_ref: Standard space reference image to use (default:\
            /usr/local/fsl/data/standard/MNI152_T1).
        alt_input: Alternative input image to apply the ROI to (instead of the\
            one used to register to the reference).
        debug_flag: Debug mode (don't delete intermediate files).
        bet_premask_flag: Equivalent to: -maskMASK\
            /usr/local/fsl/data/standard/MNI152_T1_2mm_brain_mask_dil -roiNONE.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StandardSpaceRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STANDARD_SPACE_ROI_METADATA)
    cargs = []
    cargs.append("standard_space_roi")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if mask_fov_flag:
        cargs.append("-maskFOV")
    if mask_mask is not None:
        cargs.extend([
            "-maskMASK",
            execution.input_file(mask_mask)
        ])
    if mask_none_flag:
        cargs.append("-maskNONE")
    if roi_fov_flag:
        cargs.append("-roiFOV")
    if roi_mask is not None:
        cargs.extend([
            "-roiMASK",
            execution.input_file(roi_mask)
        ])
    if roi_none_flag:
        cargs.append("-roiNONE")
    if ss_ref is not None:
        cargs.extend([
            "-ssref",
            execution.input_file(ss_ref)
        ])
    if alt_input is not None:
        cargs.extend([
            "-altinput",
            execution.input_file(alt_input)
        ])
    if debug_flag:
        cargs.append("-d")
    if bet_premask_flag:
        cargs.append("-b")
    ret = StandardSpaceRoiOutputs(
        root=execution.output_file("."),
        out_image=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "STANDARD_SPACE_ROI_METADATA",
    "StandardSpaceRoiOutputs",
    "standard_space_roi",
]
