# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RTFEEDME_METADATA = Metadata(
    id="a0ef4cb49b545bf74279792ff7d85ddf55c16151.boutiques",
    name="rtfeedme",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class RtfeedmeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rtfeedme(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rtfeedme(
    datasets: list[InputPathType],
    runner: Runner | None = None,
) -> RtfeedmeOutputs:
    """
    Test the real-time plugin by sending all the bricks in 'dataset' to AFNI.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/rtfeedme.html
    
    Args:
        datasets: List of datasets to send to AFNI, specified as paths to\
            dataset files. Multiple datasets can be specified.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RtfeedmeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RTFEEDME_METADATA)
    cargs = []
    cargs.append("rtfeedme")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in datasets])
    cargs.append("[DATASETS")
    cargs.append("...]")
    ret = RtfeedmeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RTFEEDME_METADATA",
    "RtfeedmeOutputs",
    "rtfeedme",
]