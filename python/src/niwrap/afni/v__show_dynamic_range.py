# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SHOW_DYNAMIC_RANGE_METADATA = Metadata(
    id="37e737e53c93faac205a4c31de23b2a2e921083f.boutiques",
    name="@ShowDynamicRange",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VShowDynamicRangeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__show_dynamic_range(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    minpercchange_file: OutputPathType
    """Dataset showing the percent signal change that an increment of 1
    digitized value in the time series corresponds to."""
    range_file: OutputPathType
    """Dataset showing the number of discrete levels used to represent the time
    series."""


def v__show_dynamic_range(
    infile: InputPathType,
    runner: Runner | None = None,
) -> VShowDynamicRangeOutputs:
    """
    The script checks the dynamic range of the time series data at locations inside
    the brain.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ShowDynamicRange.html
    
    Args:
        infile: Input EPI time series dataset (e.g. epi.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VShowDynamicRangeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SHOW_DYNAMIC_RANGE_METADATA)
    cargs = []
    cargs.append("@ShowDynamicRange")
    cargs.append(execution.input_file(infile))
    ret = VShowDynamicRangeOutputs(
        root=execution.output_file("."),
        minpercchange_file=execution.output_file(pathlib.Path(infile).name + "_minpercchange.nii.gz"),
        range_file=execution.output_file(pathlib.Path(infile).name + ".range.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VShowDynamicRangeOutputs",
    "V__SHOW_DYNAMIC_RANGE_METADATA",
    "v__show_dynamic_range",
]