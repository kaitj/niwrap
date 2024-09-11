# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_PERIODOGRAM_METADATA = Metadata(
    id="dc8a9f789b7c2bed3cade4f730ed9bf8e7477dd4.boutiques",
    name="3dPeriodogram",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dPeriodogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_periodogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_header: OutputPathType | None
    """Output dataset header file"""
    output_brick: OutputPathType | None
    """Output dataset brick file"""


def v_3d_periodogram(
    dataset: InputPathType,
    prefix: str | None = None,
    taper: float | None = None,
    nfft: float | None = None,
    runner: Runner | None = None,
) -> V3dPeriodogramOutputs:
    """
    Computes the periodogram of each voxel time series. The periodogram is a crude
    estimate of the power spectrum.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dPeriodogram.html
    
    Args:
        dataset: Input dataset.
        prefix: Prefix for the output dataset.
        taper: Fraction of data to taper.
        nfft: Set FFT length to a specific number of points.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPeriodogramOutputs`).
    """
    if taper is not None and not (0 <= taper <= 1): 
        raise ValueError(f"'taper' must be between 0 <= x <= 1 but was {taper}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_PERIODOGRAM_METADATA)
    cargs = []
    cargs.append("3dPeriodogram")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if taper is not None:
        cargs.extend([
            "-taper",
            str(taper)
        ])
    if nfft is not None:
        cargs.extend([
            "-nfft",
            str(nfft)
        ])
    cargs.append(execution.input_file(dataset))
    ret = V3dPeriodogramOutputs(
        root=execution.output_file("."),
        output_header=execution.output_file(prefix + ".HEAD") if (prefix is not None) else None,
        output_brick=execution.output_file(prefix + ".BRIK") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dPeriodogramOutputs",
    "V_3D_PERIODOGRAM_METADATA",
    "v_3d_periodogram",
]
