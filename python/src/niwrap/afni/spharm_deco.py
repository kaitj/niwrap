# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SPHARM_DECO_METADATA = Metadata(
    id="6d15519a5c1313333c559fb924ae8964f9b076e5.boutiques",
    name="SpharmDeco",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SpharmDecoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spharm_deco(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    harmonics_file: OutputPathType
    """File for harmonics of each order l."""
    beta_coefficients: OutputPathType
    """Beta coefficients for each data column."""
    reconstructed_data: OutputPathType
    """Reconstructed data or surface files named based on PREFIX."""


def spharm_deco(
    debug: float | None = None,
    sigma: float | None = None,
    runner: Runner | None = None,
) -> SpharmDecoOutputs:
    """
    Spherical Harmonics Decomposition of a surface's coordinates or data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        debug: Debug levels (1-3).
        sigma: Smoothing parameter (0 .. 0.001) which weighs down the\
            contribution of higher order harmonics.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpharmDecoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPHARM_DECO_METADATA)
    cargs = []
    cargs.append("SpharmDeco")
    cargs.append("[<-i_TYPE")
    cargs.append("S>]")
    cargs.append("[<-unit_sph")
    cargs.append("UNIT_SPH_LABEL>]")
    cargs.append("[<-l")
    cargs.append("L>]")
    cargs.append("[<-i_TYPE")
    cargs.append("SD>]")
    cargs.append("[<-data")
    cargs.append("D>]")
    cargs.append("[-bases_prefix")
    cargs.append("BASES]")
    cargs.append("[-prefix")
    cargs.append("PREFIX]")
    cargs.append("[-o_TYPE")
    cargs.append("SDR]")
    if debug is not None:
        cargs.extend([
            "-debug",
            str(debug)
        ])
    if sigma is not None:
        cargs.extend([
            "-sigma",
            str(sigma)
        ])
    ret = SpharmDecoOutputs(
        root=execution.output_file("."),
        harmonics_file=execution.output_file("BASES_PREFIX.sph*.1D"),
        beta_coefficients=execution.output_file("PREFIX.beta.col*.1D.dset"),
        reconstructed_data=execution.output_file("<PREFIX>_reconstructed"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPHARM_DECO_METADATA",
    "SpharmDecoOutputs",
    "spharm_deco",
]
