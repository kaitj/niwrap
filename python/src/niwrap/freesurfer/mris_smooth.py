# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SMOOTH_METADATA = Metadata(
    id="75bc8e87c534738bfed1dc6d67307d0c1e29317a.boutiques",
    name="mris_smooth",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisSmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_smooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_file: OutputPathType
    """Output smoothed surface file."""
    curvature_file: OutputPathType
    """Output curvature file (if written)."""
    area_file: OutputPathType
    """Output area file (if written)."""


def mris_smooth(
    input_surface: InputPathType,
    output_surface: str,
    average_iters: float | None = 10,
    smoothing_iters: float | None = 10,
    no_write: bool = False,
    curvature_name: str | None = "curv",
    area_name: str | None = "area",
    gaussian_params: list[float] | None = None,
    normalize_area: bool = False,
    momentum: float | None = None,
    snapshot_interval: float | None = None,
    runner: Runner | None = None,
) -> MrisSmoothOutputs:
    """
    This program smooths the tessellation of a cortical surface and writes out the
    mean curvature and area files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file for smoothing.
        output_surface: Output surface file after smoothing.
        average_iters: Specify number of curvature averaging iterations\
            (default is 10).
        smoothing_iters: Specify number of smoothing iterations (default is\
            10).
        no_write: Disable writing of curvature and area estimates.
        curvature_name: Write curvature to a specified file name (default\
            'curv').
        area_name: Write area to a specified file name (default 'area').
        gaussian_params: Use Gaussian curvature smoothing with specified norm\
            and steps.
        normalize_area: Normalize area after smoothing.
        momentum: Set momentum value.
        snapshot_interval: Write snapshot every specified number of iterations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SMOOTH_METADATA)
    cargs = []
    cargs.append("mris_smooth")
    cargs.append(execution.input_file(input_surface))
    cargs.append(output_surface)
    if average_iters is not None:
        cargs.extend([
            "-a",
            str(average_iters)
        ])
    if smoothing_iters is not None:
        cargs.extend([
            "-n",
            str(smoothing_iters)
        ])
    if no_write:
        cargs.append("-nw")
    if curvature_name is not None:
        cargs.extend([
            "-c",
            curvature_name
        ])
    if area_name is not None:
        cargs.extend([
            "-b",
            area_name
        ])
    if gaussian_params is not None:
        cargs.extend([
            "-g",
            *map(str, gaussian_params)
        ])
    if normalize_area:
        cargs.append("-area")
    if momentum is not None:
        cargs.extend([
            "-m",
            str(momentum)
        ])
    if snapshot_interval is not None:
        cargs.extend([
            "-w",
            str(snapshot_interval)
        ])
    ret = MrisSmoothOutputs(
        root=execution.output_file("."),
        output_surface_file=execution.output_file(output_surface),
        curvature_file=execution.output_file("${OUTPUT_SURFACE}_curvature"),
        area_file=execution.output_file("${OUTPUT_SURFACE}_area"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_SMOOTH_METADATA",
    "MrisSmoothOutputs",
    "mris_smooth",
]
