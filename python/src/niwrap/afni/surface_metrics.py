# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_METRICS_METADATA = Metadata(
    id="9c7c68750ba7fdd75cdb0aab145fa2f084713b18.boutiques",
    name="SurfaceMetrics",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceMetricsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_metrics(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_metrics(
    runner: Runner | None = None,
) -> SurfaceMetricsOutputs:
    """
    Outputs information about a surface's mesh.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfaceMetrics.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceMetricsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_METRICS_METADATA)
    cargs = []
    cargs.append("SurfaceMetrics")
    cargs.append("<METRIC>")
    cargs.append("-SURF_1")
    cargs.append("[-tlrc]")
    cargs.append("[-prefix")
    cargs.append("PREFIX]")
    ret = SurfaceMetricsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_METRICS_METADATA",
    "SurfaceMetricsOutputs",
    "surface_metrics",
]