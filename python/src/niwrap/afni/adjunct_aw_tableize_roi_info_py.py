# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_AW_TABLEIZE_ROI_INFO_PY_METADATA = Metadata(
    id="f3b1d8f86fae63b736e5c4974abc3020bd5bced1.boutiques",
    name="adjunct_aw_tableize_roi_info.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctAwTableizeRoiInfoPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_aw_tableize_roi_info_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Text file containing ROI count/size information"""


def adjunct_aw_tableize_roi_info_py(
    output_file: str,
    warped_atlas: InputPathType,
    warped_mask: InputPathType,
    reference_atlas: InputPathType,
    reference_mask: InputPathType,
    modesmooth_value: float,
    runner: Runner | None = None,
) -> AdjunctAwTableizeRoiInfoPyOutputs:
    """
    A simple helper function for the fat_proc scripts that generates a text file
    containing ROI count/size information based on provided atlases and masks.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_aw_tableize_roi_info.py.html
    
    Args:
        output_file: Output file name.
        warped_atlas: Warped atlas of interest, with subbrick selector if\
            necessary.
        warped_mask: Mask for the warped atlas (same grid).
        reference_atlas: Reference atlas (unwarped), with subbrick selector if\
            necessary.
        reference_mask: Mask for the reference atlas (same grid).
        modesmooth_value: Modesmooth value, from modal smoothing used after\
            warping.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctAwTableizeRoiInfoPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_AW_TABLEIZE_ROI_INFO_PY_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/adjunct_aw_tableize_roi_info.py")
    cargs.append(output_file)
    cargs.append(execution.input_file(warped_atlas))
    cargs.append(execution.input_file(warped_mask))
    cargs.append(execution.input_file(reference_atlas))
    cargs.append(execution.input_file(reference_mask))
    cargs.append(str(modesmooth_value))
    ret = AdjunctAwTableizeRoiInfoPyOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_AW_TABLEIZE_ROI_INFO_PY_METADATA",
    "AdjunctAwTableizeRoiInfoPyOutputs",
    "adjunct_aw_tableize_roi_info_py",
]