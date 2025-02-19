# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ANOVA2_METADATA = Metadata(
    id="ebf600e872cacd3686c204e18def40bac83877e7.boutiques",
    name="3dANOVA2",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dAnova2Parameters = typing.TypedDict('V3dAnova2Parameters', {
    "__STYX_TYPE__": typing.Literal["3dANOVA2"],
    "type": int,
    "alevels": int,
    "blevels": int,
    "dataset": typing.NotRequired[list[str] | None],
    "voxel": typing.NotRequired[int | None],
    "diskspace": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "ftr": typing.NotRequired[str | None],
    "fa": typing.NotRequired[str | None],
    "fb": typing.NotRequired[str | None],
    "fab": typing.NotRequired[str | None],
    "amean": typing.NotRequired[str | None],
    "bmean": typing.NotRequired[str | None],
    "xmean": typing.NotRequired[str | None],
    "adiff": typing.NotRequired[str | None],
    "bdiff": typing.NotRequired[str | None],
    "xdiff": typing.NotRequired[str | None],
    "acontr": typing.NotRequired[str | None],
    "bcontr": typing.NotRequired[str | None],
    "xcontr": typing.NotRequired[str | None],
    "bucket": typing.NotRequired[str | None],
    "old_method": bool,
    "ok": bool,
    "assume_sph": bool,
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
        "3dANOVA2": v_3d_anova2_cargs,
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
        "3dANOVA2": v_3d_anova2_outputs,
    }.get(t)


class V3dAnova2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_anova2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_ftr: OutputPathType | None
    """F-statistic for treatment effect output file"""
    output_fa: OutputPathType | None
    """F-statistic for factor A effect output file"""
    output_fb: OutputPathType | None
    """F-statistic for factor B effect output file"""
    output_fab: OutputPathType | None
    """F-statistic for interaction output file"""
    output_amean: OutputPathType | None
    """Estimate mean of factor A level output file"""
    output_bmean: OutputPathType | None
    """Estimate mean of factor B level output file"""
    output_xmean: OutputPathType | None
    """Estimate mean of cell at level i of factor A and level j of factor B
    output file"""
    output_adiff: OutputPathType | None
    """Difference between levels i and j of factor A output file"""
    output_bdiff: OutputPathType | None
    """Difference between levels i and j of factor B output file"""
    output_xdiff: OutputPathType | None
    """Difference between cell mean at A=i, B=j and cell mean at A=k, B=l output
    file"""
    output_acontr: OutputPathType | None
    """Contrast in factor A levels output file"""
    output_bcontr: OutputPathType | None
    """Contrast in factor B levels output file"""
    output_xcontr: OutputPathType | None
    """Contrast in cell means output file"""
    output_bucket: OutputPathType | None
    """Create one AFNI 'bucket' dataset file"""


def v_3d_anova2_params(
    type_: int,
    alevels: int,
    blevels: int,
    dataset: list[str] | None = None,
    voxel: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    ftr: str | None = None,
    fa: str | None = None,
    fb: str | None = None,
    fab: str | None = None,
    amean: str | None = None,
    bmean: str | None = None,
    xmean: str | None = None,
    adiff: str | None = None,
    bdiff: str | None = None,
    xdiff: str | None = None,
    acontr: str | None = None,
    bcontr: str | None = None,
    xcontr: str | None = None,
    bucket: str | None = None,
    old_method: bool = False,
    ok: bool = False,
    assume_sph: bool = False,
) -> V3dAnova2Parameters:
    """
    Build parameters.
    
    Args:
        type_: Type of ANOVA model to be used: 1=fixed, 2=random, 3=mixed.
        alevels: Number of levels of factor A.
        blevels: Number of levels of factor B.
        dataset: Data set for levels of factor A and factor B.
        voxel: Screen output for voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset 'mset' to define which voxels to\
            process.
        ftr: F-statistic for treatment effect.
        fa: F-statistic for factor A effect.
        fb: F-statistic for factor B effect.
        fab: F-statistic for interaction.
        amean: Estimate mean of factor A level.
        bmean: Estimate mean of factor B level.
        xmean: Estimate mean of cell at level i of factor A and level j of\
            factor B.
        adiff: Difference between levels i and j of factor A.
        bdiff: Difference between levels i and j of factor B.
        xdiff: Difference between cell mean at A=i, B=j and cell mean at A=k,\
            B=l.
        acontr: Contrast in factor A levels.
        bcontr: Contrast in factor B levels.
        xcontr: Contrast in cell means.
        bucket: Create one AFNI 'bucket' dataset whose sub-bricks are obtained\
            by concatenating the above output files.
        old_method: Request to perform ANOVA using the previous functionality\
            (requires -OK, also).
        ok: Confirm understanding that contrasts that do not sum to zero have\
            inflated t-stats, and contrasts that do sum to zero assume sphericity\
            (to be used with -old_method).
        assume_sph: Assume sphericity (zero-sum contrasts, only). This allows\
            use of the old_method for computing contrasts which sum to zero.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dANOVA2",
        "type": type_,
        "alevels": alevels,
        "blevels": blevels,
        "diskspace": diskspace,
        "old_method": old_method,
        "ok": ok,
        "assume_sph": assume_sph,
    }
    if dataset is not None:
        params["dataset"] = dataset
    if voxel is not None:
        params["voxel"] = voxel
    if mask is not None:
        params["mask"] = mask
    if ftr is not None:
        params["ftr"] = ftr
    if fa is not None:
        params["fa"] = fa
    if fb is not None:
        params["fb"] = fb
    if fab is not None:
        params["fab"] = fab
    if amean is not None:
        params["amean"] = amean
    if bmean is not None:
        params["bmean"] = bmean
    if xmean is not None:
        params["xmean"] = xmean
    if adiff is not None:
        params["adiff"] = adiff
    if bdiff is not None:
        params["bdiff"] = bdiff
    if xdiff is not None:
        params["xdiff"] = xdiff
    if acontr is not None:
        params["acontr"] = acontr
    if bcontr is not None:
        params["bcontr"] = bcontr
    if xcontr is not None:
        params["xcontr"] = xcontr
    if bucket is not None:
        params["bucket"] = bucket
    return params


def v_3d_anova2_cargs(
    params: V3dAnova2Parameters,
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
    cargs.append("3dANOVA2")
    cargs.extend([
        "-type",
        str(params.get("type"))
    ])
    cargs.extend([
        "-alevels",
        str(params.get("alevels"))
    ])
    cargs.extend([
        "-blevels",
        str(params.get("blevels"))
    ])
    if params.get("dataset") is not None:
        cargs.extend([
            "-dset",
            *params.get("dataset")
        ])
    if params.get("voxel") is not None:
        cargs.extend([
            "-voxel",
            str(params.get("voxel"))
        ])
    if params.get("diskspace"):
        cargs.append("-diskspace")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("ftr") is not None:
        cargs.extend([
            "-ftr",
            params.get("ftr")
        ])
    if params.get("fa") is not None:
        cargs.extend([
            "-fa",
            params.get("fa")
        ])
    if params.get("fb") is not None:
        cargs.extend([
            "-fb",
            params.get("fb")
        ])
    if params.get("fab") is not None:
        cargs.extend([
            "-fab",
            params.get("fab")
        ])
    if params.get("amean") is not None:
        cargs.extend([
            "-amean",
            params.get("amean")
        ])
    if params.get("bmean") is not None:
        cargs.extend([
            "-bmean",
            params.get("bmean")
        ])
    if params.get("xmean") is not None:
        cargs.extend([
            "-xmean",
            params.get("xmean")
        ])
    if params.get("adiff") is not None:
        cargs.extend([
            "-adiff",
            params.get("adiff")
        ])
    if params.get("bdiff") is not None:
        cargs.extend([
            "-bdiff",
            params.get("bdiff")
        ])
    if params.get("xdiff") is not None:
        cargs.extend([
            "-xdiff",
            params.get("xdiff")
        ])
    if params.get("acontr") is not None:
        cargs.extend([
            "-acontr",
            params.get("acontr")
        ])
    if params.get("bcontr") is not None:
        cargs.extend([
            "-bcontr",
            params.get("bcontr")
        ])
    if params.get("xcontr") is not None:
        cargs.extend([
            "-xcontr",
            params.get("xcontr")
        ])
    if params.get("bucket") is not None:
        cargs.extend([
            "-bucket",
            params.get("bucket")
        ])
    if params.get("old_method"):
        cargs.append("-old_method")
    if params.get("ok"):
        cargs.append("-OK")
    if params.get("assume_sph"):
        cargs.append("-assume_sph")
    return cargs


def v_3d_anova2_outputs(
    params: V3dAnova2Parameters,
    execution: Execution,
) -> V3dAnova2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAnova2Outputs(
        root=execution.output_file("."),
        output_ftr=execution.output_file(params.get("ftr") + ".+tlrc") if (params.get("ftr") is not None) else None,
        output_fa=execution.output_file(params.get("fa") + ".+tlrc") if (params.get("fa") is not None) else None,
        output_fb=execution.output_file(params.get("fb") + ".+tlrc") if (params.get("fb") is not None) else None,
        output_fab=execution.output_file(params.get("fab") + ".+tlrc") if (params.get("fab") is not None) else None,
        output_amean=execution.output_file(params.get("amean") + ".+tlrc") if (params.get("amean") is not None) else None,
        output_bmean=execution.output_file(params.get("bmean") + ".+tlrc") if (params.get("bmean") is not None) else None,
        output_xmean=execution.output_file(params.get("xmean") + ".+tlrc") if (params.get("xmean") is not None) else None,
        output_adiff=execution.output_file(params.get("adiff") + ".+tlrc") if (params.get("adiff") is not None) else None,
        output_bdiff=execution.output_file(params.get("bdiff") + ".+tlrc") if (params.get("bdiff") is not None) else None,
        output_xdiff=execution.output_file(params.get("xdiff") + ".+tlrc") if (params.get("xdiff") is not None) else None,
        output_acontr=execution.output_file(params.get("acontr") + ".+tlrc") if (params.get("acontr") is not None) else None,
        output_bcontr=execution.output_file(params.get("bcontr") + ".+tlrc") if (params.get("bcontr") is not None) else None,
        output_xcontr=execution.output_file(params.get("xcontr") + ".+tlrc") if (params.get("xcontr") is not None) else None,
        output_bucket=execution.output_file(params.get("bucket") + ".+tlrc") if (params.get("bucket") is not None) else None,
    )
    return ret


def v_3d_anova2_execute(
    params: V3dAnova2Parameters,
    execution: Execution,
) -> V3dAnova2Outputs:
    """
    This program performs a two-factor Analysis of Variance (ANOVA) on 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAnova2Outputs`).
    """
    params = execution.params(params)
    cargs = v_3d_anova2_cargs(params, execution)
    ret = v_3d_anova2_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_anova2(
    type_: int,
    alevels: int,
    blevels: int,
    dataset: list[str] | None = None,
    voxel: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    ftr: str | None = None,
    fa: str | None = None,
    fb: str | None = None,
    fab: str | None = None,
    amean: str | None = None,
    bmean: str | None = None,
    xmean: str | None = None,
    adiff: str | None = None,
    bdiff: str | None = None,
    xdiff: str | None = None,
    acontr: str | None = None,
    bcontr: str | None = None,
    xcontr: str | None = None,
    bucket: str | None = None,
    old_method: bool = False,
    ok: bool = False,
    assume_sph: bool = False,
    runner: Runner | None = None,
) -> V3dAnova2Outputs:
    """
    This program performs a two-factor Analysis of Variance (ANOVA) on 3D datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        type_: Type of ANOVA model to be used: 1=fixed, 2=random, 3=mixed.
        alevels: Number of levels of factor A.
        blevels: Number of levels of factor B.
        dataset: Data set for levels of factor A and factor B.
        voxel: Screen output for voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset 'mset' to define which voxels to\
            process.
        ftr: F-statistic for treatment effect.
        fa: F-statistic for factor A effect.
        fb: F-statistic for factor B effect.
        fab: F-statistic for interaction.
        amean: Estimate mean of factor A level.
        bmean: Estimate mean of factor B level.
        xmean: Estimate mean of cell at level i of factor A and level j of\
            factor B.
        adiff: Difference between levels i and j of factor A.
        bdiff: Difference between levels i and j of factor B.
        xdiff: Difference between cell mean at A=i, B=j and cell mean at A=k,\
            B=l.
        acontr: Contrast in factor A levels.
        bcontr: Contrast in factor B levels.
        xcontr: Contrast in cell means.
        bucket: Create one AFNI 'bucket' dataset whose sub-bricks are obtained\
            by concatenating the above output files.
        old_method: Request to perform ANOVA using the previous functionality\
            (requires -OK, also).
        ok: Confirm understanding that contrasts that do not sum to zero have\
            inflated t-stats, and contrasts that do sum to zero assume sphericity\
            (to be used with -old_method).
        assume_sph: Assume sphericity (zero-sum contrasts, only). This allows\
            use of the old_method for computing contrasts which sum to zero.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAnova2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ANOVA2_METADATA)
    params = v_3d_anova2_params(type_=type_, alevels=alevels, blevels=blevels, dataset=dataset, voxel=voxel, diskspace=diskspace, mask=mask, ftr=ftr, fa=fa, fb=fb, fab=fab, amean=amean, bmean=bmean, xmean=xmean, adiff=adiff, bdiff=bdiff, xdiff=xdiff, acontr=acontr, bcontr=bcontr, xcontr=xcontr, bucket=bucket, old_method=old_method, ok=ok, assume_sph=assume_sph)
    return v_3d_anova2_execute(params, execution)


__all__ = [
    "V3dAnova2Outputs",
    "V3dAnova2Parameters",
    "V_3D_ANOVA2_METADATA",
    "v_3d_anova2",
    "v_3d_anova2_params",
]
