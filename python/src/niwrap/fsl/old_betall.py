# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

OLD_BETALL_METADATA = Metadata(
    id="08636e6ec0271b921d070eb58b4f14fcb6768064.boutiques",
    name="old_betall",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class OldBetallOutputs(typing.NamedTuple):
    """
    Output object returned when calling `old_betall(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_t1: OutputPathType
    """Output file root for T1 image"""
    output_t2: OutputPathType
    """Output file root for T2 image"""


def old_betall(
    t1_filerout: str,
    t2_filerout: str,
    runner: Runner | None = None,
) -> OldBetallOutputs:
    """
    Automated brain extraction tool for FSL involving both T1 and T2 images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        t1_filerout: Input T1 image file root (e.g. img_t1.nii.gz).
        t2_filerout: Input T2 image file root (e.g. img_t2.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OldBetallOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OLD_BETALL_METADATA)
    cargs = []
    cargs.append("old_betall")
    cargs.append(t1_filerout)
    cargs.append(t2_filerout)
    ret = OldBetallOutputs(
        root=execution.output_file("."),
        output_t1=execution.output_file(t1_filerout),
        output_t2=execution.output_file(t2_filerout),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "OLD_BETALL_METADATA",
    "OldBetallOutputs",
    "old_betall",
]
