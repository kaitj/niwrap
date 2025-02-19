# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TFITTER_METADATA = Metadata(
    id="8451a7cd8aa8de8047fb4bbe324982a2fbf6f94a.boutiques",
    name="3dTfitter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTfitterParameters = typing.TypedDict('V3dTfitterParameters', {
    "__STYX_TYPE__": typing.Literal["3dTfitter"],
    "RHS": str,
    "LHS": typing.NotRequired[list[str] | None],
    "polort": typing.NotRequired[float | None],
    "vthr": typing.NotRequired[float | None],
    "FALTUNG": typing.NotRequired[list[str] | None],
    "lsqfit": bool,
    "l1fit": bool,
    "l2lasso": typing.NotRequired[list[str] | None],
    "lasso_centro_block": typing.NotRequired[list[str] | None],
    "l2sqrtlasso": typing.NotRequired[list[str] | None],
    "consign": typing.NotRequired[list[str] | None],
    "consFAL": typing.NotRequired[str | None],
    "prefix": typing.NotRequired[str | None],
    "label": typing.NotRequired[list[str] | None],
    "fitts": typing.NotRequired[str | None],
    "errsum": typing.NotRequired[str | None],
    "mask": typing.NotRequired[str | None],
    "quiet": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "3dTfitter": v_3d_tfitter_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "3dTfitter": v_3d_tfitter_outputs,
    }.get(t)


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


def v_3d_tfitter_params(
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
) -> V3dTfitterParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTfitter",
        "RHS": rhs,
        "lsqfit": lsqfit,
        "l1fit": l1fit,
        "quiet": quiet,
    }
    if lhs is not None:
        params["LHS"] = lhs
    if polort is not None:
        params["polort"] = polort
    if vthr is not None:
        params["vthr"] = vthr
    if faltung is not None:
        params["FALTUNG"] = faltung
    if l2lasso is not None:
        params["l2lasso"] = l2lasso
    if lasso_centro_block is not None:
        params["lasso_centro_block"] = lasso_centro_block
    if l2sqrtlasso is not None:
        params["l2sqrtlasso"] = l2sqrtlasso
    if consign is not None:
        params["consign"] = consign
    if cons_fal is not None:
        params["consFAL"] = cons_fal
    if prefix is not None:
        params["prefix"] = prefix
    if label is not None:
        params["label"] = label
    if fitts is not None:
        params["fitts"] = fitts
    if errsum is not None:
        params["errsum"] = errsum
    if mask is not None:
        params["mask"] = mask
    return params


def v_3d_tfitter_cargs(
    params: V3dTfitterParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("3dTfitter")
    cargs.extend([
        "-RHS",
        params.get("RHS")
    ])
    if params.get("LHS") is not None:
        cargs.extend([
            "-LHS",
            *params.get("LHS")
        ])
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("vthr") is not None:
        cargs.extend([
            "-vthr",
            str(params.get("vthr"))
        ])
    if params.get("FALTUNG") is not None:
        cargs.extend([
            "-FALTUNG",
            *params.get("FALTUNG")
        ])
    if params.get("lsqfit"):
        cargs.append("-lsqfit")
    if params.get("l1fit"):
        cargs.append("-l1fit")
    if params.get("l2lasso") is not None:
        cargs.extend([
            "-l2lasso",
            *params.get("l2lasso")
        ])
    if params.get("lasso_centro_block") is not None:
        cargs.extend([
            "-lasso_centro_block",
            *params.get("lasso_centro_block")
        ])
    if params.get("l2sqrtlasso") is not None:
        cargs.extend([
            "-l2sqrtlasso",
            *params.get("l2sqrtlasso")
        ])
    if params.get("consign") is not None:
        cargs.extend([
            "-consign",
            *params.get("consign")
        ])
    if params.get("consFAL") is not None:
        cargs.extend([
            "-consFAL",
            params.get("consFAL")
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("label") is not None:
        cargs.extend([
            "-label",
            *params.get("label")
        ])
    if params.get("fitts") is not None:
        cargs.extend([
            "-fitts",
            params.get("fitts")
        ])
    if params.get("errsum") is not None:
        cargs.extend([
            "-errsum",
            params.get("errsum")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            params.get("mask")
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    return cargs


def v_3d_tfitter_outputs(
    params: V3dTfitterParameters,
    execution: Execution,
) -> V3dTfitterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTfitterOutputs(
        root=execution.output_file("."),
        output_prefix=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        fitted_time_series=execution.output_file(params.get("fitts") + ".nii.gz") if (params.get("fitts") is not None) else None,
        error_sums=execution.output_file(params.get("errsum") + ".nii.gz") if (params.get("errsum") is not None) else None,
    )
    return ret


def v_3d_tfitter_execute(
    params: V3dTfitterParameters,
    execution: Execution,
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
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTfitterOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tfitter_cargs(params, execution)
    ret = v_3d_tfitter_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = v_3d_tfitter_params(rhs=rhs, lhs=lhs, polort=polort, vthr=vthr, faltung=faltung, lsqfit=lsqfit, l1fit=l1fit, l2lasso=l2lasso, lasso_centro_block=lasso_centro_block, l2sqrtlasso=l2sqrtlasso, consign=consign, cons_fal=cons_fal, prefix=prefix, label=label, fitts=fitts, errsum=errsum, mask=mask, quiet=quiet)
    return v_3d_tfitter_execute(params, execution)


__all__ = [
    "V3dTfitterOutputs",
    "V3dTfitterParameters",
    "V_3D_TFITTER_METADATA",
    "v_3d_tfitter",
    "v_3d_tfitter_params",
]
