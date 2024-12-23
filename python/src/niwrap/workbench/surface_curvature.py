# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_CURVATURE_METADATA = Metadata(
    id="42563206ac34cec769150b6b51e5edd19c49be9c.boutiques",
    name="surface-curvature",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceCurvatureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_curvature(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    opt_mean_mean_out: OutputPathType | None
    """output mean curvature: mean curvature metric"""
    opt_gauss_gauss_out: OutputPathType | None
    """output gaussian curvature: gaussian curvature metric"""


def surface_curvature(
    surface: InputPathType,
    opt_mean_mean_out: str | None = None,
    opt_gauss_gauss_out: str | None = None,
    runner: Runner | None = None,
) -> SurfaceCurvatureOutputs:
    """
    Calculate curvature of surface.
    
    Compute the curvature of the surface, using the method from:
    Interactive Texture Mapping by J. Maillot, Yahia, and Verroust, 1993.
    ACM-0-98791-601-8/93/008.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute the curvature of.
        opt_mean_mean_out: output mean curvature: mean curvature metric.
        opt_gauss_gauss_out: output gaussian curvature: gaussian curvature\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCurvatureOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CURVATURE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-curvature")
    cargs.append(execution.input_file(surface))
    if opt_mean_mean_out is not None:
        cargs.extend([
            "-mean",
            opt_mean_mean_out
        ])
    if opt_gauss_gauss_out is not None:
        cargs.extend([
            "-gauss",
            opt_gauss_gauss_out
        ])
    ret = SurfaceCurvatureOutputs(
        root=execution.output_file("."),
        opt_mean_mean_out=execution.output_file(opt_mean_mean_out) if (opt_mean_mean_out is not None) else None,
        opt_gauss_gauss_out=execution.output_file(opt_gauss_gauss_out) if (opt_gauss_gauss_out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_CURVATURE_METADATA",
    "SurfaceCurvatureOutputs",
    "surface_curvature",
]
