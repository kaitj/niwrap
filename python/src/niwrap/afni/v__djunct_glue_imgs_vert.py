# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_GLUE_IMGS_VERT_METADATA = Metadata(
    id="0680308ab9507fccff69a60f790ac39934121936.boutiques",
    name="@djunct_glue_imgs_vert",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDjunctGlueImgsVertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_glue_imgs_vert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Output image file with glued images"""


def v__djunct_glue_imgs_vert(
    bottom_image: InputPathType,
    top_image: InputPathType,
    output_file: str,
    viewer_flag: bool = False,
    help_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> VDjunctGlueImgsVertOutputs:
    """
    This script helps in gluing two images together vertically.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@djunct_glue_imgs_vert.html
    
    Args:
        bottom_image: Bottom image file.
        top_image: Top image file.
        output_file: Output file prefix.
        viewer_flag: Open in image viewer.
        help_flag: Display help message.
        version_flag: Show version information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctGlueImgsVertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_GLUE_IMGS_VERT_METADATA)
    cargs = []
    cargs.append("adjunct_glue_imgs_vert")
    if viewer_flag:
        cargs.append("-hview")
    if help_flag:
        cargs.append("-help")
    if version_flag:
        cargs.append("-ver")
    cargs.extend([
        "-imbot",
        execution.input_file(bottom_image)
    ])
    cargs.extend([
        "-imtop",
        execution.input_file(top_image)
    ])
    cargs.extend([
        "-prefix",
        output_file
    ])
    ret = VDjunctGlueImgsVertOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDjunctGlueImgsVertOutputs",
    "V__DJUNCT_GLUE_IMGS_VERT_METADATA",
    "v__djunct_glue_imgs_vert",
]