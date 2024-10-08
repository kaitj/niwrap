# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFF2RIGID_METADATA = Metadata(
    id="6a4fe2b1580c1e86111e4b2f175216d1182a533d.boutiques",
    name="aff2rigid",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class Aff2rigidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aff2rigid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def aff2rigid(
    input_transform: InputPathType,
    output_transform: str,
    runner: Runner | None = None,
) -> Aff2rigidOutputs:
    """
    Tool for converting affine transformations to rigid transformations.
    
    Author: FMRIB, University of Oxford
    
    Args:
        input_transform: Input FLIRT transform (12 DOF) from the input image to\
            standard space.
        output_transform: Output matrix which will convert the input image to\
            standard space using a 6 DOF transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Aff2rigidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFF2RIGID_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/aff2rigid")
    cargs.append(execution.input_file(input_transform))
    cargs.append(output_transform)
    ret = Aff2rigidOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFF2RIGID_METADATA",
    "Aff2rigidOutputs",
    "aff2rigid",
]
