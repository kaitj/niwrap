# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EASYWARP_METADATA = Metadata(
    id="61155dbff21df2a7da1b05052571570b740944be.boutiques",
    name="mri_easywarp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriEasywarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_easywarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_deformed_image: OutputPathType
    """Output deformed image"""


def mri_easywarp(
    input_image: InputPathType,
    output_image: str,
    deformation_field: InputPathType | None = None,
    nearest_neighbor: bool = False,
    num_threads: float | None = None,
    runner: Runner | None = None,
) -> MriEasywarpOutputs:
    """
    EasyReg: deep learning registration simple and easy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input image.
        output_image: Output (deformed) image.
        deformation_field: Deformation field.
        nearest_neighbor: Use nearest neighbor (rather than linear)\
            interpolation.
        num_threads: Number of cores to be used. Default is 1. You can use -1\
            to use all available cores.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEasywarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EASYWARP_METADATA)
    cargs = []
    cargs.append("mri_easywarp")
    cargs.extend([
        "--i",
        execution.input_file(input_image)
    ])
    cargs.extend([
        "--o",
        output_image
    ])
    if deformation_field is not None:
        cargs.extend([
            "--field",
            execution.input_file(deformation_field)
        ])
    if nearest_neighbor:
        cargs.append("--nearest")
    if num_threads is not None:
        cargs.extend([
            "--threads",
            str(num_threads)
        ])
    ret = MriEasywarpOutputs(
        root=execution.output_file("."),
        output_deformed_image=execution.output_file(output_image + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_EASYWARP_METADATA",
    "MriEasywarpOutputs",
    "mri_easywarp",
]
