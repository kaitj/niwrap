# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_24SWAP_METADATA = Metadata(
    id="36522de60f2db30203ed34354f5c2bb34bc52aca.boutiques",
    name="24swap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V24swapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_24swap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_24swap(
    input_files: list[InputPathType],
    quiet: bool = False,
    pattern: str | None = None,
    runner: Runner | None = None,
) -> V24swapOutputs:
    """
    Swaps bytes pairs and/or quadruples on the files listed.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/24swap.html
    
    Args:
        input_files: Input file(s) to swap bytes.
        quiet: Operate quietly.
        pattern: Pattern that determines the pattern of 2 and 4 byte swaps.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V24swapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_24SWAP_METADATA)
    cargs = []
    cargs.append("24swap")
    if quiet:
        cargs.append("-q")
    if pattern is not None:
        cargs.extend([
            "-pattern",
            pattern
        ])
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V24swapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V24swapOutputs",
    "V_24SWAP_METADATA",
    "v_24swap",
]