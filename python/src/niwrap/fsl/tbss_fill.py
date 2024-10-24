# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TBSS_FILL_METADATA = Metadata(
    id="7017823848d50e17e75b17f5d9718126eae8a1a8.boutiques",
    name="tbss_fill",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class TbssFillOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_fill(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filled_skeleton: OutputPathType
    """Filled skeletonized FA image"""


def tbss_fill(
    stats_image: InputPathType,
    threshold: float,
    mean_fa: InputPathType,
    output: str,
    include_negative_flag: bool = False,
    runner: Runner | None = None,
) -> TbssFillOutputs:
    """
    Tool for filling skeletonized FA images in TBSS.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        stats_image: Stats image.
        threshold: Threshold value.
        mean_fa: Mean FA image.
        output: Output image.
        include_negative_flag: Include negative stat values (below -threshold).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TbssFillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_FILL_METADATA)
    cargs = []
    cargs.append("tbss_fill")
    cargs.append(execution.input_file(stats_image))
    cargs.append(str(threshold))
    cargs.append(execution.input_file(mean_fa))
    cargs.append(output)
    if include_negative_flag:
        cargs.append("-n")
    ret = TbssFillOutputs(
        root=execution.output_file("."),
        filled_skeleton=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_FILL_METADATA",
    "TbssFillOutputs",
    "tbss_fill",
]
