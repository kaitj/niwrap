# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SIMULATE_MOTION_METADATA = Metadata(
    id="29610b1a1e2e528bee711b23ea7ec7ab12c28c38.boutiques",
    name="@simulate_motion",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSimulateMotionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__simulate_motion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    simulated_motion_output: OutputPathType
    """Motion simulated EPI time series"""


def v__simulate_motion(
    epi: InputPathType,
    motion_file: InputPathType,
    runner: Runner | None = None,
) -> VSimulateMotionOutputs:
    """
    Create simulated motion time series in an EPI dataset based on the provided
    motion parameters and an input volume.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@simulate_motion.html
    
    Args:
        epi: Input EPI volume or time series (only a volreg base is needed,\
            though more is okay).
        motion_file: Motion parameter file (as output by 3dvolreg).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSimulateMotionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SIMULATE_MOTION_METADATA)
    cargs = []
    cargs.append("@simulate_motion")
    cargs.append("[options]")
    cargs.append("-epi")
    cargs.extend([
        "-epi",
        execution.input_file(epi)
    ])
    cargs.append("-motion_file")
    cargs.extend([
        "-motion_file",
        execution.input_file(motion_file)
    ])
    ret = VSimulateMotionOutputs(
        root=execution.output_file("."),
        simulated_motion_output=execution.output_file("[PREFIX]_simulated_motion.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSimulateMotionOutputs",
    "V__SIMULATE_MOTION_METADATA",
    "v__simulate_motion",
]