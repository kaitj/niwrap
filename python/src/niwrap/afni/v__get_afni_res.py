# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__GET_AFNI_RES_METADATA = Metadata(
    id="37ef6b880d312bd816b4392e7ab249540e04a190.boutiques",
    name="@GetAfniRes",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VGetAfniResOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_res(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__get_afni_res(
    input_dataset: InputPathType,
    output_type: typing.Literal["-min", "-max", "-mean"] | None = None,
    runner: Runner | None = None,
) -> VGetAfniResOutputs:
    """
    Tool to return the voxel resolution of a dataset.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@GetAfniRes.html
    
    Args:
        input_dataset: Input dataset.
        output_type: Output type specifying whether to return the minimum,\
            maximum, or mean resolution.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniResOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_RES_METADATA)
    cargs = []
    cargs.append("@GetAfniRes")
    if output_type is not None:
        cargs.append(output_type)
    cargs.append(execution.input_file(input_dataset))
    ret = VGetAfniResOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VGetAfniResOutputs",
    "V__GET_AFNI_RES_METADATA",
    "v__get_afni_res",
]