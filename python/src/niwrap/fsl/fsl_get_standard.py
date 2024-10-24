# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_GET_STANDARD_METADATA = Metadata(
    id="728c316a44d42029a6f3db7d477d865274c0fac1.boutiques",
    name="fsl_get_standard",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslGetStandardOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_get_standard(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_get_standard(
    image_type: typing.Literal["whole_head", "brain", "brain_mask"],
    resolution: float | None = None,
    verbose_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> FslGetStandardOutputs:
    """
    Generate paths to FSL standard space images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        image_type: Image type - one of 'whole_head' (the default), 'brain', or\
            'brain_mask'.
        resolution: Desired isotropic resolution in millimetres.
        verbose_flag: Output more information.
        version_flag: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslGetStandardOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_GET_STANDARD_METADATA)
    cargs = []
    cargs.append("fsl_get_standard")
    cargs.append(image_type)
    if resolution is not None:
        cargs.extend([
            "-r",
            str(resolution)
        ])
    if verbose_flag:
        cargs.append("-v")
    if version_flag:
        cargs.append("-V")
    ret = FslGetStandardOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_GET_STANDARD_METADATA",
    "FslGetStandardOutputs",
    "fsl_get_standard",
]
