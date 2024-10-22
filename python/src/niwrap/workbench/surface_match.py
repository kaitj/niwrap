# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_MATCH_METADATA = Metadata(
    id="1adbf7641d223b6c453cc098b76dada2164d90a8.boutiques",
    name="surface-match",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceMatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_match(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_match(
    match_surface_file: InputPathType,
    input_surface_file: InputPathType,
    output_surface_name: str,
    runner: Runner | None = None,
) -> SurfaceMatchOutputs:
    """
    Surface match.
    
    The Input Surface File will be transformed so that its coordinate ranges
    (bounding box) match that of the Match Surface File.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        match_surface_file: Match (Reference) Surface.
        input_surface_file: File containing surface that will be transformed.
        output_surface_name: Surface File after transformation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceMatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_MATCH_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-match")
    cargs.append(execution.input_file(match_surface_file))
    cargs.append(execution.input_file(input_surface_file))
    cargs.append(output_surface_name)
    ret = SurfaceMatchOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_MATCH_METADATA",
    "SurfaceMatchOutputs",
    "surface_match",
]
