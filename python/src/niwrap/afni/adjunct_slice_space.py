# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_SLICE_SPACE_METADATA = Metadata(
    id="5305861dda9c3754eb6168adb64a351683433bbe.boutiques",
    name="adjunct_slice_space",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctSliceSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_slice_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_slice_space(
    inset: InputPathType,
    nwin: float,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AdjunctSliceSpaceOutputs:
    """
    A tiny adjunct program for @chauffeur_afni to calculate how to evenly space a
    number of slices within each view plane of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: Name of input dataset.
        nwin: Number of windows (i.e., slices) that you want across each view\
            plane.
        help_: See helpfile.
        version: See version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSliceSpaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SLICE_SPACE_METADATA)
    cargs = []
    cargs.append("adjunct_slice_space")
    cargs.append(execution.input_file(inset))
    cargs.append(str(nwin))
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-ver")
    ret = AdjunctSliceSpaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_SLICE_SPACE_METADATA",
    "AdjunctSliceSpaceOutputs",
    "adjunct_slice_space",
]
