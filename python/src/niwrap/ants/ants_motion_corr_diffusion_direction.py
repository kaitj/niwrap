# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA = Metadata(
    id="3f81491f1faf2e11f2fe0e69121f28544825a2d4.boutiques",
    name="antsMotionCorrDiffusionDirection",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsMotionCorrDiffusionDirectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_motion_corr_diffusion_direction(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_scheme: OutputPathType
    """The output file for corrected diffusion directions."""


def ants_motion_corr_diffusion_direction(
    scheme: InputPathType,
    bvec: InputPathType,
    physical: InputPathType,
    moco: InputPathType,
    output: str,
    runner: Runner | None = None,
) -> AntsMotionCorrDiffusionDirectionOutputs:
    """
    This tool adjusts the diffusion scheme for motion correction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        scheme: Camino scheme file specify acquisition parameters.
        bvec: bvec image specifying diffusion directions.
        physical: 3D image in dwi space.
        moco: Motion correction parameters from antsMotionCorr.
        output: Specify the output file for corrected directions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrDiffusionDirectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA)
    cargs = []
    cargs.append("antsMotionCorrDiffusionDirection")
    cargs.extend([
        "-s",
        execution.input_file(scheme)
    ])
    cargs.extend([
        "-b",
        execution.input_file(bvec)
    ])
    cargs.extend([
        "-p",
        execution.input_file(physical)
    ])
    cargs.extend([
        "-m",
        execution.input_file(moco)
    ])
    cargs.extend([
        "-o",
        output
    ])
    ret = AntsMotionCorrDiffusionDirectionOutputs(
        root=execution.output_file("."),
        corrected_scheme=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_MOTION_CORR_DIFFUSION_DIRECTION_METADATA",
    "AntsMotionCorrDiffusionDirectionOutputs",
    "ants_motion_corr_diffusion_direction",
]