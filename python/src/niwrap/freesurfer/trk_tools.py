# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TRK_TOOLS_METADATA = Metadata(
    id="4dc371140c0aeb4d9bc3aacbdf63d35a219d2dd8.boutiques",
    name="trk_tools",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TrkToolsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `trk_tools(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    trk_output_file: OutputPathType | None
    """The processed output TRK file"""
    image_output_file: OutputPathType | None
    """Image exported from TRK file"""
    vtk_output_file: OutputPathType | None
    """VTK file containing streamlines"""


def trk_tools(
    reference_image: InputPathType,
    input_trk: InputPathType,
    output_trk: str | None = None,
    output_image: str | None = None,
    update_header: bool = False,
    output_vtk: str | None = None,
    runner: Runner | None = None,
) -> TrkToolsOutputs:
    """
    Tool for processing TRK files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        reference_image: Reference image for TRK processing.
        input_trk: Input TRK file to be processed.
        output_trk: Output TRK file.
        output_image: Export TRK into an image.
        update_header: Update TRK header with reference image.
        output_vtk: Output streamlines in VTK format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TrkToolsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRK_TOOLS_METADATA)
    cargs = []
    cargs.append("trk_tools")
    cargs.extend([
        "-i",
        execution.input_file(reference_image)
    ])
    cargs.extend([
        "-f",
        execution.input_file(input_trk)
    ])
    if output_trk is not None:
        cargs.extend([
            "-o",
            output_trk
        ])
    if output_image is not None:
        cargs.extend([
            "-e",
            output_image
        ])
    if update_header:
        cargs.append("-u")
    if output_vtk is not None:
        cargs.extend([
            "-v",
            output_vtk
        ])
    ret = TrkToolsOutputs(
        root=execution.output_file("."),
        trk_output_file=execution.output_file(output_trk) if (output_trk is not None) else None,
        image_output_file=execution.output_file(output_image) if (output_image is not None) else None,
        vtk_output_file=execution.output_file(output_vtk) if (output_vtk is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRK_TOOLS_METADATA",
    "TrkToolsOutputs",
    "trk_tools",
]
