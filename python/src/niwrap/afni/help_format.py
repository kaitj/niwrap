# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

HELP_FORMAT_METADATA = Metadata(
    id="94a8ca9630967c536e2f2bc2dfbd0fa19cb662a9.boutiques",
    name="help_format",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class HelpFormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `help_format(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    formatted_output: OutputPathType
    """The formatted text with hyperlinks"""


def help_format(
    runner: Runner | None = None,
) -> HelpFormatOutputs:
    """
    Formats text by converting URLs into HTML hyperlinks.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/help_format.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HelpFormatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HELP_FORMAT_METADATA)
    cargs = []
    cargs.append("help_format")
    ret = HelpFormatOutputs(
        root=execution.output_file("."),
        formatted_output=execution.output_file("formatted_output.html"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "HELP_FORMAT_METADATA",
    "HelpFormatOutputs",
    "help_format",
]
