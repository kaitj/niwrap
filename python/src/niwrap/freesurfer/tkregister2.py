# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TKREGISTER2_METADATA = Metadata(
    id="5b91df2c41f022fb3500d5826ced751292eade8d.boutiques",
    name="tkregister2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Tkregister2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `tkregister2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_reg_file: OutputPathType
    """Resulting registration file"""


def tkregister2(
    fixed_volume: InputPathType,
    moving_volume: InputPathType,
    reg_file: InputPathType,
    noedit: bool = False,
    lta: bool = False,
    surf_reg: bool = False,
    reg_only: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> Tkregister2Outputs:
    """
    tkregister2 is a tool from FreeSurfer used for registration of MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        fixed_volume: Fixed volume (e.g., anatomical image).
        moving_volume: Moving volume (e.g., functional image).
        reg_file: Registration file to be saved or loaded.
        noedit: Run in no-edit mode, useful for scripting.
        lta: Use LTA format for registration file.
        surf_reg: Use surface registration.
        reg_only: Don't show GUI, just save registration.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tkregister2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKREGISTER2_METADATA)
    cargs = []
    cargs.append("tkregister2")
    cargs.append(execution.input_file(fixed_volume))
    cargs.append(execution.input_file(moving_volume))
    cargs.append(execution.input_file(reg_file))
    if noedit:
        cargs.append("--noedit")
    if lta:
        cargs.append("--lta")
    if surf_reg:
        cargs.append("--surf")
    if reg_only:
        cargs.append("--regonly")
    if help_:
        cargs.append("--help")
    ret = Tkregister2Outputs(
        root=execution.output_file("."),
        output_reg_file=execution.output_file(pathlib.Path(reg_file).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TKREGISTER2_METADATA",
    "Tkregister2Outputs",
    "tkregister2",
]