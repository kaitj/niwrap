# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_FLAG_MOTION_METADATA = Metadata(
    id="12ffa6b4e618d89798e3c857043643e105256e61.boutiques",
    name="1dFlagMotion",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dFlagMotionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_flag_motion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_points: OutputPathType
    """List of points exceeding the motion bounds in 1D format"""


def v_1d_flag_motion(
    input_motion_file: InputPathType,
    max_translation: float | None = None,
    max_rotation: float | None = None,
    runner: Runner | None = None,
) -> V1dFlagMotionOutputs:
    """
    Produces a list of time points with excessive motion relative to the previous
    time point.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dFlagMotion.html
    
    Args:
        input_motion_file: Input file with EXACTLY 6 columns: roll pitch yaw\
            delta-SI delta-LR delta-AP (angles in degrees followed by translations\
            in mm).
        max_translation: Maximum translation allowed in any direction (defaults\
            to 1.5mm).
        max_rotation: Maximum rotation allowed in any direction (defaults to\
            1.25 degrees).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dFlagMotionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_FLAG_MOTION_METADATA)
    cargs = []
    cargs.append("1dFlagMotion")
    cargs.append(execution.input_file(input_motion_file))
    if max_translation is not None:
        cargs.extend([
            "-MaxTrans",
            str(max_translation)
        ])
    if max_rotation is not None:
        cargs.extend([
            "-MaxRot",
            str(max_rotation)
        ])
    ret = V1dFlagMotionOutputs(
        root=execution.output_file("."),
        output_points=execution.output_file("output_motion_points.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dFlagMotionOutputs",
    "V_1D_FLAG_MOTION_METADATA",
    "v_1d_flag_motion",
]