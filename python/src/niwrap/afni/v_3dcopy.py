# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DCOPY_METADATA = Metadata(
    id="4b8187d004c6f4ba95518e709ad1f9b3eb4ed322.boutiques",
    name="3dcopy",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dcopyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dcopy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dcopy(
    verbose: bool = False,
    denote: bool = False,
    runner: Runner | None = None,
) -> V3dcopyOutputs:
    """
    3dcopy copies datasets with or without altering prefixes and converting formats.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        verbose: Print progress reports.
        denote: Remove any Notes from the file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dcopyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCOPY_METADATA)
    cargs = []
    cargs.append("3dcopy")
    if verbose:
        cargs.append("-verb")
    if denote:
        cargs.append("-denote")
    cargs.append("{OLD_PREFIX}+{VIEW}")
    cargs.append("{NEW_PREFIX}")
    ret = V3dcopyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dcopyOutputs",
    "V_3DCOPY_METADATA",
    "v_3dcopy",
]
