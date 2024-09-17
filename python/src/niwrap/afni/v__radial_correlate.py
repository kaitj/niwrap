# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__RADIAL_CORRELATE_METADATA = Metadata(
    id="b1a552cc3d34915cce72bfbd9edfd04ef85c61b5.boutiques",
    name="@radial_correlate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VRadialCorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__radial_correlate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corr_volumes: OutputPathType
    """Directory containing correlation volumes"""


def v__radial_correlate(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> VRadialCorrelateOutputs:
    """
    Check datasets for correlation artifacts.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@radial_correlate.html
    
    Args:
        input_files: A list of EPI datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRadialCorrelateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__RADIAL_CORRELATE_METADATA)
    cargs = []
    cargs.append("@radial_correlate")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.append("[OPTIONS]")
    ret = VRadialCorrelateOutputs(
        root=execution.output_file("."),
        corr_volumes=execution.output_file("[RESULTS_DIR]/correlation_volumes"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VRadialCorrelateOutputs",
    "V__RADIAL_CORRELATE_METADATA",
    "v__radial_correlate",
]