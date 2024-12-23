# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SURF_SMOOTH_HEAT_07_EXAMPLES_METADATA = Metadata(
    id="dc0b150ee17a89e1651ca52dbda01cc2f717b438.boutiques",
    name="@SurfSmooth.HEAT_07.examples",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSurfSmoothHeat07ExamplesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__surf_smooth_heat_07_examples(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__surf_smooth_heat_07_examples(
    path_to_suma_demo: str,
    runner: Runner | None = None,
) -> VSurfSmoothHeat07ExamplesOutputs:
    """
    A script to illustrate controlled blurring of data on the surface.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        path_to_suma_demo: Path to SUMA demo directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSurfSmoothHeat07ExamplesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SURF_SMOOTH_HEAT_07_EXAMPLES_METADATA)
    cargs = []
    cargs.append("@SurfSmooth.HEAT_07.examples")
    cargs.append(path_to_suma_demo)
    ret = VSurfSmoothHeat07ExamplesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSurfSmoothHeat07ExamplesOutputs",
    "V__SURF_SMOOTH_HEAT_07_EXAMPLES_METADATA",
    "v__surf_smooth_heat_07_examples",
]
