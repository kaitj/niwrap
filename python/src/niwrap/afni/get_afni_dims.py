# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GET_AFNI_DIMS_METADATA = Metadata(
    id="6cda6d2d778ae7fa76728ef0174566006c7d6a7d.boutiques",
    name="GetAfniDims",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class GetAfniDimsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_afni_dims(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dims_output: OutputPathType
    """Text file containing the dimensions of the input dataset"""


def get_afni_dims(
    input_dset: InputPathType,
    runner: Runner | None = None,
) -> GetAfniDimsOutputs:
    """
    A utility tool to return dimensions of AFNI dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dset: Input AFNI dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniDimsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_AFNI_DIMS_METADATA)
    cargs = []
    cargs.append("GetAfniDims")
    cargs.append(execution.input_file(input_dset))
    ret = GetAfniDimsOutputs(
        root=execution.output_file("."),
        dims_output=execution.output_file("dims_output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GET_AFNI_DIMS_METADATA",
    "GetAfniDimsOutputs",
    "get_afni_dims",
]
