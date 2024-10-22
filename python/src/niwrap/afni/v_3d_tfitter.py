# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TFITTER_METADATA = Metadata(
    id="8451a7cd8aa8de8047fb4bbe324982a2fbf6f94a.boutiques",
    name="3dTfitter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTfitterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tfitter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_prefix: OutputPathType | None
    """Output dataset for LHS parameters."""
    fitted_time_series: OutputPathType | None
    """Output fitted time series dataset."""
    error_sums: OutputPathType | None
    """Output error sums dataset."""


def v_3d_tfitter(
    rhs: str,
    lhs: list[str] | None = None,
    polort: float | None = None,
    vthr: float | None = None,
    faltung: list[str] | None = None,
    lsqfit: bool = False,
    l1fit: bool = False,
    l2lasso: list[str] | None = None,
    lasso_centro_block: list[str] | None = None,
    l2sqrtlasso: list[str] | None = None,
    consign: list[str] | None = None,
    cons_fal: str | None = None,
    prefix: str | None = None,
    label: list[str] | None = None,
    fitts: str | None = None,
    errsum: str | None = None,
    mask: str | None = None,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dTfitterOutputs:
    """
    * At each voxel, assembles and solves a set of linear equations.
    ++ The matrix at each voxel may be the same or may be different.
    ++ This flexibility (for voxel-wise regressors) is one feature
    that makes 3dTfitter different from 3dDeconvolve.
    ++ Another distinguishing feature is that 3dTfitter allows for
    L2, L1, and L2+L1 (LASSO) regression solvers, and allows you
    to impose sign constraints on the solution parameters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        rhs: Specifies the right-hand-side 3D+time dataset. ('rset' can also be\
            a 1D file with 1 column).
        lhs: Specifies a column (or columns) of the left-hand-side matrix. More\
            than one 'lset' can follow the '-LHS' option.
        polort: Add 'p+1' Legendre polynomial columns to the LHS matrix.
        vthr: The value 'v' (between 0.0 and 0.09, inclusive) defines the\
            threshold below which LHS vectors will be omitted from the regression\
            analysis.
        faltung: Specifies a convolution (German: Faltung) model to be added to\
            the LHS matrix. Followed by four arguments: 'fset', 'fpre', 'pen',\
            'fac'.
        lsqfit: Solve equations via least squares [the default method].
        l1fit: Solve equations via least sum of absolute residuals.
        l2lasso: Solve equations via least squares with a LASSO (L1) penalty on\
            the coefficients. Followed by 'lam' and optional 'i j k ...'.
        lasso_centro_block: Defines a block of coefficients that will be\
            penalized together.
        l2sqrtlasso: Similar to '-l2lasso', but aims to minimize\
            sqrt(Q2)+lam*L1.
        consign: Indicates that the sign of some output LHS parameters should\
            be constrained in the solution.
        cons_fal: Constrain the deconvolution time series from '-FALTUNG' to be\
            positive if 'c' is '+' or to be negative if 'c' is '-'.
        prefix: Prefix for the output dataset (LHS parameters) filename.
        label: Specifies sub-brick labels in the output LHS parameter dataset.
        fitts: Prefix filename for the output fitted time series dataset.
        errsum: Prefix filename for the error sums dataset.
        mask: Read in dataset 'ms' to use as a mask; only voxels with nonzero\
            values in the mask will be processed.
        quiet: Don't print progress report messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTfitterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TFITTER_METADATA)
    cargs = []
    cargs.append("3dTfitter")
    cargs.extend([
        "-RHS",
        rhs
    ])
    if lhs is not None:
        cargs.extend([
            "-LHS",
            *lhs
        ])
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    if vthr is not None:
        cargs.extend([
            "-vthr",
            str(vthr)
        ])
    if faltung is not None:
        cargs.extend([
            "-FALTUNG",
            *faltung
        ])
    if lsqfit:
        cargs.append("-lsqfit")
    if l1fit:
        cargs.append("-l1fit")
    if l2lasso is not None:
        cargs.extend([
            "-l2lasso",
            *l2lasso
        ])
    if lasso_centro_block is not None:
        cargs.extend([
            "-lasso_centro_block",
            *lasso_centro_block
        ])
    if l2sqrtlasso is not None:
        cargs.extend([
            "-l2sqrtlasso",
            *l2sqrtlasso
        ])
    if consign is not None:
        cargs.extend([
            "-consign",
            *consign
        ])
    if cons_fal is not None:
        cargs.extend([
            "-consFAL",
            cons_fal
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if label is not None:
        cargs.extend([
            "-label",
            *label
        ])
    if fitts is not None:
        cargs.extend([
            "-fitts",
            fitts
        ])
    if errsum is not None:
        cargs.extend([
            "-errsum",
            errsum
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            mask
        ])
    if quiet:
        cargs.append("-quiet")
    ret = V3dTfitterOutputs(
        root=execution.output_file("."),
        output_prefix=execution.output_file(prefix + ".nii.gz") if (prefix is not None) else None,
        fitted_time_series=execution.output_file(fitts + ".nii.gz") if (fitts is not None) else None,
        error_sums=execution.output_file(errsum + ".nii.gz") if (errsum is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTfitterOutputs",
    "V_3D_TFITTER_METADATA",
    "v_3d_tfitter",
]
