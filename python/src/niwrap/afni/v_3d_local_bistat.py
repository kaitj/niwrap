# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LOCAL_BISTAT_METADATA = Metadata(
    id="e90dc29ecfbe470e814874e0a612f6a2f98a8350.boutiques",
    name="3dLocalBistat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dLocalBistatParameters = typing.TypedDict('V3dLocalBistatParameters', {
    "__STYX_TYPE__": typing.Literal["3dLocalBistat"],
    "nbhd": str,
    "stats": list[str],
    "mask": typing.NotRequired[InputPathType | None],
    "automask": bool,
    "weight": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "histpow": typing.NotRequired[float | None],
    "histbin": typing.NotRequired[float | None],
    "hclip1": typing.NotRequired[list[str] | None],
    "hclip2": typing.NotRequired[list[str] | None],
    "dataset1": InputPathType,
    "dataset2": InputPathType,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "3dLocalBistat": v_3d_local_bistat_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "3dLocalBistat": v_3d_local_bistat_outputs,
    }
    return vt.get(t)


class V3dLocalBistatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_bistat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType
    """Output dataset header for AFNI format"""
    output_brik: OutputPathType
    """Output dataset BRIK for AFNI format"""


def v_3d_local_bistat_params(
    nbhd: str,
    stats: list[str],
    prefix: str,
    dataset1: InputPathType,
    dataset2: InputPathType,
    mask: InputPathType | None = None,
    automask: bool = False,
    weight: InputPathType | None = None,
    histpow: float | None = None,
    histbin: float | None = None,
    hclip1: list[str] | None = None,
    hclip2: list[str] | None = None,
) -> V3dLocalBistatParameters:
    """
    Build parameters.
    
    Args:
        nbhd: Specifies the neighborhood around each voxel for statistics\
            calculation. Types include: SPHERE(r), RECT(a,b,c), RHDD(r), TOHD(r).
        stats: Statistic to compute in the region around each voxel. Multiple\
            options allowed. Includes: pearson, spearman, quadrant, mutinfo,\
            normuti, jointent, hellinger, crU, crM, crA, L2slope, L1slope, num,\
            ALL.
        prefix: Prefix of the output dataset.
        dataset1: The first input dataset (e.g. data1.nii).
        dataset2: The second input dataset (e.g. data2.nii).
        mask: Read in a dataset to use as a mask. Non-zero voxels define the\
            mask region.
        automask: Compute the mask as in program 3dAutomask. Mutually exclusive\
            with -mask.
        weight: Use dataset as a weight (applies to pearson).
        histpow: Sets the exponent for the number of bins in the histogram used\
            for Hellinger, Mutual Information, and Correlation Ratio statistics.
        histbin: Sets the number of bins directly in the histogram used for\
            Hellinger, Mutual Information, and Correlation Ratio statistics.
        hclip1: Clip dataset1 to lie between specified values.
        hclip2: Clip dataset2 to lie between specified values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLocalBistat",
        "nbhd": nbhd,
        "stats": stats,
        "automask": automask,
        "prefix": prefix,
        "dataset1": dataset1,
        "dataset2": dataset2,
    }
    if mask is not None:
        params["mask"] = mask
    if weight is not None:
        params["weight"] = weight
    if histpow is not None:
        params["histpow"] = histpow
    if histbin is not None:
        params["histbin"] = histbin
    if hclip1 is not None:
        params["hclip1"] = hclip1
    if hclip2 is not None:
        params["hclip2"] = hclip2
    return params


def v_3d_local_bistat_cargs(
    params: V3dLocalBistatParameters,
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
    cargs.append("3dLocalBistat")
    cargs.extend([
        "-nbhd",
        params.get("nbhd")
    ])
    cargs.extend([
        "-stat",
        *params.get("stats")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("weight") is not None:
        cargs.extend([
            "-weight",
            execution.input_file(params.get("weight"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("histpow") is not None:
        cargs.extend([
            "-histpow",
            str(params.get("histpow"))
        ])
    if params.get("histbin") is not None:
        cargs.extend([
            "-histbin",
            str(params.get("histbin"))
        ])
    if params.get("hclip1") is not None:
        cargs.extend([
            "-hclip1",
            *params.get("hclip1")
        ])
    if params.get("hclip2") is not None:
        cargs.extend([
            "-hclip2",
            *params.get("hclip2")
        ])
    cargs.append(execution.input_file(params.get("dataset1")))
    cargs.append(execution.input_file(params.get("dataset2")))
    return cargs


def v_3d_local_bistat_outputs(
    params: V3dLocalBistatParameters,
    execution: Execution,
) -> V3dLocalBistatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLocalBistatOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(params.get("prefix") + "+orig.HEAD"),
        output_brik=execution.output_file(params.get("prefix") + "+orig.BRIK"),
    )
    return ret


def v_3d_local_bistat_execute(
    params: V3dLocalBistatParameters,
    execution: Execution,
) -> V3dLocalBistatOutputs:
    """
    Compute statistics between 2 datasets at each voxel based on a local
    neighborhood.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLocalBistatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_local_bistat_cargs(params, execution)
    ret = v_3d_local_bistat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_local_bistat(
    nbhd: str,
    stats: list[str],
    prefix: str,
    dataset1: InputPathType,
    dataset2: InputPathType,
    mask: InputPathType | None = None,
    automask: bool = False,
    weight: InputPathType | None = None,
    histpow: float | None = None,
    histbin: float | None = None,
    hclip1: list[str] | None = None,
    hclip2: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dLocalBistatOutputs:
    """
    Compute statistics between 2 datasets at each voxel based on a local
    neighborhood.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        nbhd: Specifies the neighborhood around each voxel for statistics\
            calculation. Types include: SPHERE(r), RECT(a,b,c), RHDD(r), TOHD(r).
        stats: Statistic to compute in the region around each voxel. Multiple\
            options allowed. Includes: pearson, spearman, quadrant, mutinfo,\
            normuti, jointent, hellinger, crU, crM, crA, L2slope, L1slope, num,\
            ALL.
        prefix: Prefix of the output dataset.
        dataset1: The first input dataset (e.g. data1.nii).
        dataset2: The second input dataset (e.g. data2.nii).
        mask: Read in a dataset to use as a mask. Non-zero voxels define the\
            mask region.
        automask: Compute the mask as in program 3dAutomask. Mutually exclusive\
            with -mask.
        weight: Use dataset as a weight (applies to pearson).
        histpow: Sets the exponent for the number of bins in the histogram used\
            for Hellinger, Mutual Information, and Correlation Ratio statistics.
        histbin: Sets the number of bins directly in the histogram used for\
            Hellinger, Mutual Information, and Correlation Ratio statistics.
        hclip1: Clip dataset1 to lie between specified values.
        hclip2: Clip dataset2 to lie between specified values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalBistatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_BISTAT_METADATA)
    params = v_3d_local_bistat_params(nbhd=nbhd, stats=stats, mask=mask, automask=automask, weight=weight, prefix=prefix, histpow=histpow, histbin=histbin, hclip1=hclip1, hclip2=hclip2, dataset1=dataset1, dataset2=dataset2)
    return v_3d_local_bistat_execute(params, execution)


__all__ = [
    "V3dLocalBistatOutputs",
    "V_3D_LOCAL_BISTAT_METADATA",
    "v_3d_local_bistat",
    "v_3d_local_bistat_params",
]
