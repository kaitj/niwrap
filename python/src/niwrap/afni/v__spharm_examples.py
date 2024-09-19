# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SPHARM_EXAMPLES_METADATA = Metadata(
    id="4e0cfd08072915ed372892853cb57b3f45c5d67f.boutiques",
    name="@Spharm.examples",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSpharmExamplesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__spharm_examples(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__spharm_examples(
    help_web: bool = False,
    help_web_alias: bool = False,
    help_view: bool = False,
    help_view_alias: bool = False,
    all_opts: bool = False,
    help_find: str | None = None,
    runner: Runner | None = None,
) -> VSpharmExamplesOutputs:
    """
    A script to demonstrate the usage of spherical harmonics decomposition with
    SUMA.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Spharm.examples.html
    
    Args:
        help_web: Open webpage with help for this program.
        help_web_alias: Same as -h_web.
        help_view: Open -help output in a GUI editor.
        help_view_alias: Same as -h_view.
        all_opts: List all of the options for this script.
        help_find: Search for lines containing WORD in -help output. Search is\
            approximate.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSpharmExamplesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SPHARM_EXAMPLES_METADATA)
    cargs = []
    cargs.append("@Spharm.examples")
    if help_web:
        cargs.append("-h_web")
    if help_web_alias:
        cargs.append("-hweb")
    if help_view:
        cargs.append("-h_view")
    if help_view_alias:
        cargs.append("-hview")
    if all_opts:
        cargs.append("-all_opts")
    if help_find is not None:
        cargs.extend([
            "-h_find",
            help_find
        ])
    ret = VSpharmExamplesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSpharmExamplesOutputs",
    "V__SPHARM_EXAMPLES_METADATA",
    "v__spharm_examples",
]
