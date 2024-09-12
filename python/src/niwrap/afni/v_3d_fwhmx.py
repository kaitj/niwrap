# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_FWHMX_METADATA = Metadata(
    id="547e4dbe790636f5635f53fd7e3368f8b4d428a8.boutiques",
    name="3dFWHMx",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dFwhmxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_fwhmx(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output file containing FWHM/ACF estimates"""
    detrended_dataset: OutputPathType | None
    """Detrended dataset file"""


def v_3d_fwhmx(
    infile: InputPathType,
    mask: InputPathType | None = None,
    automask: bool = False,
    demed: bool = False,
    unif: bool = False,
    detrend: float | None = None,
    detprefix: str | None = None,
    geom: bool = False,
    arith: bool = False,
    combine: bool = False,
    out: str | None = None,
    compat: bool = False,
    acf: str | None = None,
    runner: Runner | None = None,
) -> V3dFwhmxOutputs:
    """
    Compute Full Width at Half Maximum (FWHM) for FMRI datasets using
    AutoCorrelation Function (ACF).
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dFWHMx.html
    
    Args:
        infile: Input dataset.
        mask: Use only voxels that are nonzero in dataset 'mmm'.
        automask: Compute a mask from THIS dataset.
        demed: if the input dataset has more than one sub-brick then subtract\
            the median of each voxel's time series before processing FWHM.
        unif: Normalize each voxel's time series to have the same MAD before\
            processing FWHM, implies -demed.
        detrend: Detrend to order 'q'. If q is not given, the program picks\
            q=NT/30; -detrend disables -demed, and includes -unif.
        detprefix: Save the detrended file into a dataset with prefix 'd'.
        geom: Compute the final estimate as the geometric mean.
        arith: Compute the final estimate as the arithmetic mean.
        combine: Combine the final measurements along each axis into one result.
        out: Write output to file 'ttt' (3 columns of numbers). If not given,\
            the sub-brick outputs are not written. Use '-out -' to write to stdout,\
            if desired.
        compat: Be compatible with the older 3dFWHM.
        acf: Compute the spatial autocorrelation of the data as a function of\
            radius, then fit that to a model and output the model parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dFwhmxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_FWHMX_METADATA)
    cargs = []
    cargs.append("3dFWHMx")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if automask:
        cargs.append("-automask")
    if demed:
        cargs.append("-demed")
    if unif:
        cargs.append("-unif")
    if detrend is not None:
        cargs.extend([
            "-detrend",
            str(detrend)
        ])
    if detprefix is not None:
        cargs.extend([
            "-detprefix",
            detprefix
        ])
    if geom:
        cargs.append("-geom")
    if arith:
        cargs.append("-arith")
    if combine:
        cargs.append("-combine")
    if out is not None:
        cargs.extend([
            "-out",
            out
        ])
    if compat:
        cargs.append("-compat")
    if acf is not None:
        cargs.extend([
            "-acf",
            acf
        ])
    cargs.append(execution.input_file(infile))
    ret = V3dFwhmxOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(out + ".1D") if (out is not None) else None,
        detrended_dataset=execution.output_file(detprefix + ".nii.gz") if (detprefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dFwhmxOutputs",
    "V_3D_FWHMX_METADATA",
    "v_3d_fwhmx",
]
