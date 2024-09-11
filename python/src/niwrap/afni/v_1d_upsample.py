# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_UPSAMPLE_METADATA = Metadata(
    id="18022a2c74b1202fca6440648cf3ceb4bd831495.boutiques",
    name="1dUpsample",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dUpsampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_upsample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Upsampled 1D time series output"""


def v_1d_upsample(
    upsample_factor: float,
    input_file: InputPathType,
    linear_interpolation: bool = False,
    runner: Runner | None = None,
) -> V1dUpsampleOutputs:
    """
    Upsamples a 1D time series to a finer time grid.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dUpsample.html
    
    Args:
        upsample_factor: Upsample factor (integer from 2..32).
        input_file: Input 1D time series file.
        linear_interpolation: Use 1st order polynomials (i.e., linear\
            interpolation) instead of 7th order polynomials.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dUpsampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_UPSAMPLE_METADATA)
    cargs = []
    cargs.append("1dUpsample")
    cargs.append(str(upsample_factor))
    cargs.append(execution.input_file(input_file))
    if linear_interpolation:
        cargs.append("-one")
    ret = V1dUpsampleOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("ethel.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dUpsampleOutputs",
    "V_1D_UPSAMPLE_METADATA",
    "v_1d_upsample",
]