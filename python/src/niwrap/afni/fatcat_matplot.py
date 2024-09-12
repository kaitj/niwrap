# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FATCAT_MATPLOT_METADATA = Metadata(
    id="7f404852f322ecb660b36f0c63595b909d540a1f.boutiques",
    name="FATCAT_matplot",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class FatcatMatplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fatcat_matplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fatcat_matplot(
    directory: str,
    shiny_folder: bool = False,
    runner: Runner | None = None,
) -> FatcatMatplotOutputs:
    """
    Launch a shiny app to visualize .netcc and/or .grid files.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/FATCAT_matplot.html
    
    Args:
        directory: Path to a folder containing .netcc and/or .grid files.
        shiny_folder: Use a custom shiny folder (for testing purposes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatcatMatplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FATCAT_MATPLOT_METADATA)
    cargs = []
    cargs.append("FATCAT_matplot")
    cargs.append(directory)
    if shiny_folder:
        cargs.append("-ShinyFolder")
    ret = FatcatMatplotOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FATCAT_MATPLOT_METADATA",
    "FatcatMatplotOutputs",
    "fatcat_matplot",
]
