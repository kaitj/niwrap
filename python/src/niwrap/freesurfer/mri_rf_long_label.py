# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_RF_LONG_LABEL_METADATA = Metadata(
    id="06cc04cbd7f8fd46c1d7544632fa8c08486bcc37.boutiques",
    name="mri_rf_long_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriRfLongLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_rf_long_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_rf_long_label(
    help_flag: str | None = None,
    runner: Runner | None = None,
) -> MriRfLongLabelOutputs:
    """
    The mri_rf_long_label tool has been removed from this version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        help_flag: Displays a message that the tool has been removed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriRfLongLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_RF_LONG_LABEL_METADATA)
    cargs = []
    cargs.append("mri_rf_long_label")
    if help_flag is not None:
        cargs.append(help_flag)
    ret = MriRfLongLabelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_RF_LONG_LABEL_METADATA",
    "MriRfLongLabelOutputs",
    "mri_rf_long_label",
]
