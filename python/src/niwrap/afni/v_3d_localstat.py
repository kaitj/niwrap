# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LOCALSTAT_METADATA = Metadata(
    id="f927c9d4ad8b0ef0fa566fe0b9648789d0b3eb44.boutiques",
    name="3dLocalstat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dLocalstatParameters = typing.TypedDict('V3dLocalstatParameters', {
    "__STYX_TYPE__": typing.Literal["3dLocalstat"],
    "dataset": InputPathType,
    "nbhd": str,
    "stat": typing.NotRequired[list[str] | None],
    "mask": typing.NotRequired[InputPathType | None],
    "automask": bool,
    "use_nonmask": bool,
    "prefix": typing.NotRequired[str | None],
    "datum": typing.NotRequired[str | None],
    "label_ext": typing.NotRequired[str | None],
    "reduce_grid": typing.NotRequired[list[float] | None],
    "reduce_restore_grid": typing.NotRequired[list[float] | None],
    "reduce_max_vox": typing.NotRequired[float | None],
    "grid_rmode": typing.NotRequired[str | None],
    "quiet": bool,
    "verbose": bool,
    "proceed_small_N": bool,
    "fillvalue": typing.NotRequired[float | None],
    "unfillvalue": typing.NotRequired[float | None],
    "maskvalue": typing.NotRequired[float | None],
    "maskvalue2": typing.NotRequired[float | None],
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
        "3dLocalstat": v_3d_localstat_cargs,
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
        "3dLocalstat": v_3d_localstat_outputs,
    }
    return vt.get(t)


class V3dLocalstatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_localstat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output dataset"""


def v_3d_localstat_params(
    dataset: InputPathType,
    nbhd: str,
    stat_: list[str] | None = None,
    mask: InputPathType | None = None,
    automask: bool = False,
    use_nonmask: bool = False,
    prefix: str | None = None,
    datum: str | None = None,
    label_ext: str | None = None,
    reduce_grid: list[float] | None = None,
    reduce_restore_grid: list[float] | None = None,
    reduce_max_vox: float | None = None,
    grid_rmode: str | None = None,
    quiet: bool = False,
    verbose: bool = False,
    proceed_small_n: bool = False,
    fillvalue: float | None = None,
    unfillvalue: float | None = None,
    maskvalue: float | None = None,
    maskvalue2: float | None = None,
) -> V3dLocalstatParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset.
        nbhd: The region around each voxel that will be extracted for the\
            statistics calculation.
        stat_: Compute the specified statistic on the values extracted from the\
            neighborhood.
        mask: Read in dataset 'mset' and use the nonzero voxels therein as a\
            mask.
        automask: Compute the mask as in program 3dAutomask (mutually exclusive\
            with -mask).
        use_nonmask: Compute local statistics from all voxels in the\
            neighborhood that are in the mask, even if the central voxel is not in\
            the mask.
        prefix: Use the given string as the prefix for the output dataset.
        datum: Coerce the output data to be stored as the given type (byte,\
            short, float).
        label_ext: Append given label to each sub-brick label.
        reduce_grid: Compute output on a grid that is reduced by the given\
            factor in X, Y, and Z directions of the input dataset.
        reduce_restore_grid: Resample the output back to input grid after\
            reducing the grid.
        reduce_max_vox: Automatically set Rx Ry Rz so that the computation grid\
            is at a resolution of nbhd/MAX_VOX voxels.
        grid_rmode: Interpolant to use when resampling the output with\
            reduce_restore_grid option.
        quiet: Stop the highly informative progress reports.
        verbose: A little more verbose output.
        proceed_small_n: Do not crash if neighborhood is too small for certain\
            estimates.
        fillvalue: Value used for filled statistic, default=1.
        unfillvalue: Value used for unfilled statistic, default=1.
        maskvalue: Value searched for with has_mask option.
        maskvalue2: Alternate value for has_mask2 option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dLocalstat",
        "dataset": dataset,
        "nbhd": nbhd,
        "automask": automask,
        "use_nonmask": use_nonmask,
        "quiet": quiet,
        "verbose": verbose,
        "proceed_small_N": proceed_small_n,
    }
    if stat_ is not None:
        params["stat"] = stat_
    if mask is not None:
        params["mask"] = mask
    if prefix is not None:
        params["prefix"] = prefix
    if datum is not None:
        params["datum"] = datum
    if label_ext is not None:
        params["label_ext"] = label_ext
    if reduce_grid is not None:
        params["reduce_grid"] = reduce_grid
    if reduce_restore_grid is not None:
        params["reduce_restore_grid"] = reduce_restore_grid
    if reduce_max_vox is not None:
        params["reduce_max_vox"] = reduce_max_vox
    if grid_rmode is not None:
        params["grid_rmode"] = grid_rmode
    if fillvalue is not None:
        params["fillvalue"] = fillvalue
    if unfillvalue is not None:
        params["unfillvalue"] = unfillvalue
    if maskvalue is not None:
        params["maskvalue"] = maskvalue
    if maskvalue2 is not None:
        params["maskvalue2"] = maskvalue2
    return params


def v_3d_localstat_cargs(
    params: V3dLocalstatParameters,
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
    cargs.append("3dLocalstat")
    cargs.append(execution.input_file(params.get("dataset")))
    cargs.extend([
        "-nbhd",
        params.get("nbhd")
    ])
    if params.get("stat") is not None:
        cargs.extend([
            "-stat",
            *params.get("stat")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("use_nonmask"):
        cargs.append("-use_nonmask")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
        ])
    if params.get("label_ext") is not None:
        cargs.extend([
            "-label_ext",
            params.get("label_ext")
        ])
    if params.get("reduce_grid") is not None:
        cargs.extend([
            "-reduce_grid",
            *map(str, params.get("reduce_grid"))
        ])
    if params.get("reduce_restore_grid") is not None:
        cargs.extend([
            "-reduce_restore_grid",
            *map(str, params.get("reduce_restore_grid"))
        ])
    if params.get("reduce_max_vox") is not None:
        cargs.extend([
            "-reduce_max_vox",
            str(params.get("reduce_max_vox"))
        ])
    if params.get("grid_rmode") is not None:
        cargs.extend([
            "-grid_rmode",
            params.get("grid_rmode")
        ])
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("proceed_small_N"):
        cargs.append("-proceed_small_N")
    if params.get("fillvalue") is not None:
        cargs.extend([
            "-fillvalue",
            str(params.get("fillvalue"))
        ])
    if params.get("unfillvalue") is not None:
        cargs.extend([
            "-unfillvalue",
            str(params.get("unfillvalue"))
        ])
    if params.get("maskvalue") is not None:
        cargs.extend([
            "-maskvalue",
            str(params.get("maskvalue"))
        ])
    if params.get("maskvalue2") is not None:
        cargs.extend([
            "-maskvalue2",
            str(params.get("maskvalue2"))
        ])
    return cargs


def v_3d_localstat_outputs(
    params: V3dLocalstatParameters,
    execution: Execution,
) -> V3dLocalstatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dLocalstatOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_localstat_execute(
    params: V3dLocalstatParameters,
    execution: Execution,
) -> V3dLocalstatOutputs:
    """
    This program computes statistics at each voxel, based on a local neighborhood of
    that voxel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dLocalstatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_localstat_cargs(params, execution)
    ret = v_3d_localstat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_localstat(
    dataset: InputPathType,
    nbhd: str,
    stat_: list[str] | None = None,
    mask: InputPathType | None = None,
    automask: bool = False,
    use_nonmask: bool = False,
    prefix: str | None = None,
    datum: str | None = None,
    label_ext: str | None = None,
    reduce_grid: list[float] | None = None,
    reduce_restore_grid: list[float] | None = None,
    reduce_max_vox: float | None = None,
    grid_rmode: str | None = None,
    quiet: bool = False,
    verbose: bool = False,
    proceed_small_n: bool = False,
    fillvalue: float | None = None,
    unfillvalue: float | None = None,
    maskvalue: float | None = None,
    maskvalue2: float | None = None,
    runner: Runner | None = None,
) -> V3dLocalstatOutputs:
    """
    This program computes statistics at each voxel, based on a local neighborhood of
    that voxel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        nbhd: The region around each voxel that will be extracted for the\
            statistics calculation.
        stat_: Compute the specified statistic on the values extracted from the\
            neighborhood.
        mask: Read in dataset 'mset' and use the nonzero voxels therein as a\
            mask.
        automask: Compute the mask as in program 3dAutomask (mutually exclusive\
            with -mask).
        use_nonmask: Compute local statistics from all voxels in the\
            neighborhood that are in the mask, even if the central voxel is not in\
            the mask.
        prefix: Use the given string as the prefix for the output dataset.
        datum: Coerce the output data to be stored as the given type (byte,\
            short, float).
        label_ext: Append given label to each sub-brick label.
        reduce_grid: Compute output on a grid that is reduced by the given\
            factor in X, Y, and Z directions of the input dataset.
        reduce_restore_grid: Resample the output back to input grid after\
            reducing the grid.
        reduce_max_vox: Automatically set Rx Ry Rz so that the computation grid\
            is at a resolution of nbhd/MAX_VOX voxels.
        grid_rmode: Interpolant to use when resampling the output with\
            reduce_restore_grid option.
        quiet: Stop the highly informative progress reports.
        verbose: A little more verbose output.
        proceed_small_n: Do not crash if neighborhood is too small for certain\
            estimates.
        fillvalue: Value used for filled statistic, default=1.
        unfillvalue: Value used for unfilled statistic, default=1.
        maskvalue: Value searched for with has_mask option.
        maskvalue2: Alternate value for has_mask2 option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalstatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCALSTAT_METADATA)
    params = v_3d_localstat_params(dataset=dataset, nbhd=nbhd, stat_=stat_, mask=mask, automask=automask, use_nonmask=use_nonmask, prefix=prefix, datum=datum, label_ext=label_ext, reduce_grid=reduce_grid, reduce_restore_grid=reduce_restore_grid, reduce_max_vox=reduce_max_vox, grid_rmode=grid_rmode, quiet=quiet, verbose=verbose, proceed_small_n=proceed_small_n, fillvalue=fillvalue, unfillvalue=unfillvalue, maskvalue=maskvalue, maskvalue2=maskvalue2)
    return v_3d_localstat_execute(params, execution)


__all__ = [
    "V3dLocalstatOutputs",
    "V_3D_LOCALSTAT_METADATA",
    "v_3d_localstat",
    "v_3d_localstat_params",
]
