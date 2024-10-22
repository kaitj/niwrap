# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BALLOON_METADATA = Metadata(
    id="d51a9a16b7b5ef48e2f34c8e205b9eb2d6df6b2a.boutiques",
    name="balloon",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class BalloonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `balloon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def balloon(
    tr: float,
    num_scans: int,
    event_times: InputPathType,
    t_fall: list[float] | None = None,
    runner: Runner | None = None,
) -> BalloonOutputs:
    """
    Simulation of haemodynamic response using the balloon model. Based on the
    theoretical model proposed by Buxton et al. (1998).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tr: Scan repetition time in seconds (TR), the interval at which the\
            output curve will be sampled.
        num_scans: Number of scans (N), the output curve will comprise this\
            number of samples.
        event_times: The name of a file containing the event timings, in\
            seconds, as ASCII strings separated by white space, with time 0 being\
            the time at which the initial scan occurred.
        t_fall: Haemodynamic fall time in seconds (typically between 4s and\
            6s).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BalloonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BALLOON_METADATA)
    cargs = []
    cargs.append("balloon")
    cargs.append(str(tr))
    cargs.append(str(num_scans))
    cargs.append(execution.input_file(event_times))
    if t_fall is not None:
        cargs.extend(map(str, t_fall))
    ret = BalloonOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BALLOON_METADATA",
    "BalloonOutputs",
    "balloon",
]
