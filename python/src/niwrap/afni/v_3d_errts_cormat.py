# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ERRTS_CORMAT_METADATA = Metadata(
    id="2f4cd813e00c21c8ed95885addacf3502e722a23.boutiques",
    name="3dErrtsCormat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dErrtsCormatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_errts_cormat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """1D file of the Toeplitz entries."""


def v_3d_errts_cormat(
    dset: InputPathType,
    concat: str | None = None,
    input_: InputPathType | None = None,
    mask: InputPathType | None = None,
    maxlag: float | None = None,
    polort: float | None = None,
    runner: Runner | None = None,
) -> V3dErrtsCormatOutputs:
    """
    Computes the correlation matrix corresponding to the residual (or error) time
    series in 'dset'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Dataset to read, usually the '-errts' output from 3dDeconvolve.
        concat: As used in 3dDeconvolve.
        input_: Alternate way of specifying the dataset to read.
        mask: Mask dataset to apply.
        maxlag: Set maximum lag.
        polort: Set polort level. Default is 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dErrtsCormatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ERRTS_CORMAT_METADATA)
    cargs = []
    cargs.append("3dErrtsCormat")
    cargs.append(execution.input_file(dset))
    if concat is not None:
        cargs.extend([
            "-concat",
            concat
        ])
    if input_ is not None:
        cargs.extend([
            "-input",
            execution.input_file(input_)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if maxlag is not None:
        cargs.extend([
            "-maxlag",
            str(maxlag)
        ])
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    ret = V3dErrtsCormatOutputs(
        root=execution.output_file("."),
        output=execution.output_file("stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dErrtsCormatOutputs",
    "V_3D_ERRTS_CORMAT_METADATA",
    "v_3d_errts_cormat",
]
