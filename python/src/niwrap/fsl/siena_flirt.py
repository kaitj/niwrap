# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIENA_FLIRT_METADATA = Metadata(
    id="43c7f5fc0eb419d283af74ab74f219134df428d4.boutiques",
    name="siena_flirt",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SienaFlirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena_flirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_matrix: OutputPathType
    """Output transformation matrix file"""
    output_registered_image: OutputPathType
    """Output registered image"""


def siena_flirt(
    input1_fileroot: str,
    input2_fileroot: str,
    runner: Runner | None = None,
) -> SienaFlirtOutputs:
    """
    Wrapper for FLIRT image registration within the SIENA framework.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    Args:
        input1_fileroot: First input file root (e.g. first time-point image\
            root, without file extension).
        input2_fileroot: Second input file root (e.g. second time-point image\
            root, without file extension).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaFlirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_FLIRT_METADATA)
    cargs = []
    cargs.append("siena_flirt")
    cargs.append(input1_fileroot)
    cargs.append(input2_fileroot)
    ret = SienaFlirtOutputs(
        root=execution.output_file("."),
        output_transform_matrix=execution.output_file(input1_fileroot + "_to_" + input2_fileroot + "_flirt.mat"),
        output_registered_image=execution.output_file(input1_fileroot + "_to_" + input2_fileroot + "_flirt.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENA_FLIRT_METADATA",
    "SienaFlirtOutputs",
    "siena_flirt",
]
