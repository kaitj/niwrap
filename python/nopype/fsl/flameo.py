# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


FLAMEO_METADATA = Metadata(
    id="5e27bb366f2f7207fc4a014aa45ef5c5dea0c053",
    name="FLAMEO",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FlameoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flameo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dummy_output: OutputPathType
    """Description missing"""


def flameo(
    runner: Runner,
    dummy_input: InputPathType,
) -> FlameoOutputs:
    """
    Automatic nipype2boutiques conversion failed.
    
    Args:
        runner: Command runner
        dummy_input: Description missing
    Returns:
        NamedTuple of outputs (described in `FlameoOutputs`).
    """
    execution = runner.start_execution(FLAMEO_METADATA)
    cargs = []
    cargs.append("dummy")
    ret = FlameoOutputs(
        root=execution.output_file("."),
        dummy_output=execution.output_file(f"dummy_output.txt"),
    )
    execution.run(cargs)
    return ret
