# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__CLUST_EXP_RUN_SHINY_METADATA = Metadata(
    id="fda3a7d2925f29a17f3a4aecaecf82a67d6aa1fc.boutiques",
    name="@ClustExp_run_shiny",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VClustExpRunShinyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__clust_exp_run_shiny(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__clust_exp_run_shiny(
    directory: str,
    help_: bool = False,
    runner: Runner | None = None,
) -> VClustExpRunShinyOutputs:
    """
    Launch a shiny app that was created by ClustExp_StatParse.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        directory: Folder created by ClustExp_StatParse.py.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VClustExpRunShinyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CLUST_EXP_RUN_SHINY_METADATA)
    cargs = []
    cargs.append("@ClustExp_run_shiny")
    cargs.append(directory)
    if help_:
        cargs.append("-help")
    ret = VClustExpRunShinyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VClustExpRunShinyOutputs",
    "V__CLUST_EXP_RUN_SHINY_METADATA",
    "v__clust_exp_run_shiny",
]
