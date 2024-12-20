# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_SPLINE_METADATA = Metadata(
    id="7d3ca3a45eadd41a58c1c4e8f7cf2661b9cc81d4.boutiques",
    name="dmri_spline",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriSplineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_spline(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_volume: OutputPathType | None
    """Output volume of the interpolated spline"""
    out_points_file: OutputPathType | None
    """Output text file with interpolated spline points"""
    out_tangent_vectors: OutputPathType | None
    """Output text file containing tangent vectors"""
    out_normal_vectors: OutputPathType | None
    """Output text file containing normal vectors"""
    out_curvature: OutputPathType | None
    """Output text file containing curvatures"""


def dmri_spline(
    control_points_file: InputPathType,
    mask_volume: InputPathType,
    output_volume: str | None = None,
    show_points: bool = False,
    output_points: str | None = None,
    output_vectors_base: str | None = None,
    debug: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> DmriSplineOutputs:
    """
    Tool for interpolating and analyzing splines within a defined mask.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        control_points_file: Input text file containing control points.
        mask_volume: Input mask volume (spline is not allowed to stray off\
            mask).
        output_volume: Output volume of the interpolated spline.
        show_points: Highlight control points in output volume (default: no).
        output_points: Output text file containing all interpolated spline\
            points.
        output_vectors_base: Base name of output text files containing tangent\
            vectors, normal vectors, and curvatures at every point along the spline.
        debug: Turn on debugging.
        check_options: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriSplineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_SPLINE_METADATA)
    cargs = []
    cargs.append("dmri_spline")
    cargs.extend([
        "--cpts",
        execution.input_file(control_points_file)
    ])
    cargs.extend([
        "--mask",
        execution.input_file(mask_volume)
    ])
    if output_volume is not None:
        cargs.extend([
            "--out",
            output_volume
        ])
    if show_points:
        cargs.append("--show")
    if output_points is not None:
        cargs.extend([
            "--outpts",
            output_points
        ])
    if output_vectors_base is not None:
        cargs.extend([
            "--outvec",
            output_vectors_base
        ])
    if debug:
        cargs.append("--debug")
    if check_options:
        cargs.append("--checkopts")
    ret = DmriSplineOutputs(
        root=execution.output_file("."),
        out_volume=execution.output_file(output_volume) if (output_volume is not None) else None,
        out_points_file=execution.output_file(output_points) if (output_points is not None) else None,
        out_tangent_vectors=execution.output_file(output_vectors_base + "_tangent.txt") if (output_vectors_base is not None) else None,
        out_normal_vectors=execution.output_file(output_vectors_base + "_normal.txt") if (output_vectors_base is not None) else None,
        out_curvature=execution.output_file(output_vectors_base + "_curvature.txt") if (output_vectors_base is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_SPLINE_METADATA",
    "DmriSplineOutputs",
    "dmri_spline",
]
