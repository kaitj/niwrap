# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_COMBINE_STR_PY_METADATA = Metadata(
    id="fd97336f40bb633027085aedee51887ccb728352.boutiques",
    name="adjunct_combine_str.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AdjunctCombineStrPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_combine_str_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_selector_file: OutputPathType
    """The output file containing the new string selector"""


def adjunct_combine_str_py(
    output_file: str,
    upper_index: float,
    string_selectors: list[str],
    runner: Runner | None = None,
) -> AdjunctCombineStrPyOutputs:
    """
    A simple helper function for fat_proc* scripts that processes string selectors
    and outputs a new string selector.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_combine_str.py.html
    
    Args:
        output_file: An output file name.
        upper_index: An int that is the upper index for the selector (-1 means\
            to use the max number in the input strings).
        string_selectors: One or more string selector strings of *goods* to\
            keep.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctCombineStrPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_COMBINE_STR_PY_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/adjunct_combine_str.py")
    cargs.append(output_file)
    cargs.append(str(upper_index))
    cargs.extend(string_selectors)
    ret = AdjunctCombineStrPyOutputs(
        root=execution.output_file("."),
        output_selector_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_COMBINE_STR_PY_METADATA",
    "AdjunctCombineStrPyOutputs",
    "adjunct_combine_str_py",
]