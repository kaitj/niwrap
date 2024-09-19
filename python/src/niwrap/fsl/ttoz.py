# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TTOZ_METADATA = Metadata(
    id="2fd3ff40a0a94383f946c29b5284870363bf0a26.boutiques",
    name="ttoz",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class TtozOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ttoz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_zvol: OutputPathType | None
    """Output Z-statistic volume"""


def ttoz(
    varsfile: InputPathType,
    cbsfile: InputPathType,
    dof: int,
    outputvol: str | None = None,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> TtozOutputs:
    """
    Tool to convert a T-statistic image to a Z-statistic image.
    
    Args:
        varsfile: Input variables file.
        cbsfile: Input CBS file.
        dof: Degrees of freedom.
        outputvol: Output volume name (default is zstats).
        help_flag: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TtozOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TTOZ_METADATA)
    cargs = []
    cargs.append("ttoz")
    cargs.append(execution.input_file(varsfile))
    cargs.append(execution.input_file(cbsfile))
    cargs.append(str(dof))
    if outputvol is not None:
        cargs.extend([
            "-zout",
            outputvol
        ])
    if help_flag:
        cargs.append("-help")
    ret = TtozOutputs(
        root=execution.output_file("."),
        output_zvol=execution.output_file(outputvol + ".nii.gz") if (outputvol is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TTOZ_METADATA",
    "TtozOutputs",
    "ttoz",
]
