# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICE_METADATA = Metadata(
    id="f71a1a10052c96f6d549130064fdecff0de60fb9.boutiques",
    name="Slice",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SliceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slice_(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_files: OutputPathType
    """No description provided."""


def slice_(
    in_file: InputPathType,
    out_base_name: str | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    runner: Runner | None = None,
) -> SliceOutputs:
    """
    Use fslslice to split a 3D file into lots of 2D files (along z-axis).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input filename.
        out_base_name: Outputs prefix.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SliceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICE_METADATA)
    cargs = []
    cargs.append("Slice")
    cargs.append(execution.input_file(in_file))
    if out_base_name is not None:
        cargs.append(out_base_name)
    if output_type is not None:
        cargs.append(output_type)
    ret = SliceOutputs(
        root=execution.output_file("."),
        out_files=execution.output_file("out_files"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICE_METADATA",
    "SliceOutputs",
    "slice_",
]
