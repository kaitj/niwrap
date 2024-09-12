# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BORDER_LENGTH_METADATA = Metadata(
    id="1c7cf169d78e6b37032b0df2eb8b08b4d96f80e1.boutiques",
    name="border-length",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


class BorderLengthOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_length(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def border_length(
    border: InputPathType,
    surface: InputPathType,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_separate_pieces: bool = False,
    opt_hide_border_name: bool = False,
    runner: Runner | None = None,
) -> BorderLengthOutputs:
    """
    Report length of borders.
    
    For each border, print its length along the surface, in mm. If a border has
    multiple parts, their lengths are summed before printing, unless
    -separate-pieces is specified.
    
    The -corrected-areas option is intended for when the length is not
    meaningfully measurable on individual surfaces, it is only an approximate
    correction for the reduction in structure of a group average surface.
    
    Author: Washington University School of Medicin
    
    Args:
        border: the input border file.
        surface: the surface to measure the borders on.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_separate_pieces: report lengths for multi-part borders as separate\
            numbers.
        opt_hide_border_name: don't print border name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderLengthOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_LENGTH_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-length")
    cargs.append(execution.input_file(border))
    cargs.append(execution.input_file(surface))
    if opt_corrected_areas_area_metric is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(opt_corrected_areas_area_metric)
        ])
    if opt_separate_pieces:
        cargs.append("-separate-pieces")
    if opt_hide_border_name:
        cargs.append("-hide-border-name")
    ret = BorderLengthOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BORDER_LENGTH_METADATA",
    "BorderLengthOutputs",
    "border_length",
]
