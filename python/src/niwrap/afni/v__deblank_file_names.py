# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DEBLANK_FILE_NAMES_METADATA = Metadata(
    id="f8ade1cbfe9a1ee930f5bb24bfe83955ccad0cf1.boutiques",
    name="@DeblankFileNames",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VDeblankFileNamesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__deblank_file_names(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__deblank_file_names(
    move: bool = False,
    nobrac: bool = False,
    demo_set: bool = False,
    echo: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VDeblankFileNamesOutputs:
    """
    A script to remove blanks and other annoying characters ([], ()) from filenames.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        move: Actually rename the files (opposite of -dry_run).
        nobrac: Do not replace () and [] in filenames, just spaces.
        demo_set: Create a toy directory with bad names for testing.
        echo: Turn on script echo.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDeblankFileNamesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DEBLANK_FILE_NAMES_METADATA)
    cargs = []
    cargs.append("@DeblankFileNames")
    if move:
        cargs.append("-move")
    if nobrac:
        cargs.append("-nobrac")
    if demo_set:
        cargs.append("-demo_set")
    if echo:
        cargs.append("-echo")
    if help_:
        cargs.append("-help")
    cargs.append("[FILES...]")
    ret = VDeblankFileNamesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDeblankFileNamesOutputs",
    "V__DEBLANK_FILE_NAMES_METADATA",
    "v__deblank_file_names",
]
