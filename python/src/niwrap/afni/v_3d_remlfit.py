# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_REMLFIT_METADATA = Metadata(
    id="847ea79f5b61b9773e10438597e56d4e78c62c2e.boutiques",
    name="3dREMLfit",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRemlfitParameters = typing.TypedDict('V3dRemlfitParameters', {
    "__STYX_TYPE__": typing.Literal["3dREMLfit"],
    "input_file": InputPathType,
    "regression_matrix": InputPathType,
    "baseline_files": typing.NotRequired[list[str] | None],
    "sort_nods": bool,
    "temp_storage": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "output_prefix": typing.NotRequired[str | None],
    "go_for_it": bool,
    "max_b_param": typing.NotRequired[float | None],
    "grid_param": typing.NotRequired[float | None],
    "negative_corr": bool,
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
        "3dREMLfit": v_3d_remlfit_cargs,
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
        "3dREMLfit": v_3d_remlfit_outputs,
    }
    return vt.get(t)


class V3dRemlfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_remlfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Main default output of 3dREMLfit"""
    rvar_file: OutputPathType | None
    """REML variance parameters"""
    rbeta_file: OutputPathType | None
    """REML beta weights"""
    rbuck_file: OutputPathType | None
    """REML estimates and statistics"""
    rfitts_file: OutputPathType | None
    """REML fitted model"""
    rerrts_file: OutputPathType | None
    """REML residuals"""


def v_3d_remlfit_params(
    input_file: InputPathType,
    regression_matrix: InputPathType,
    baseline_files: list[str] | None = None,
    sort_nods: bool = False,
    temp_storage: bool = False,
    mask: InputPathType | None = None,
    output_prefix: str | None = None,
    go_for_it: bool = False,
    max_b_param: float | None = None,
    grid_param: float | None = None,
    negative_corr: bool = False,
) -> V3dRemlfitParameters:
    """
    Build parameters.
    
    Args:
        input_file: Read time series dataset.
        regression_matrix: Read the regression matrix, which should have been\
            output from 3dDeconvolve via the '-x1D' option.
        baseline_files: Add baseline model columns to the matrix. Each column\
            in the specified .1D file will be appended to the matrix.
        sort_nods: If '-dsort' is used, the output datasets reflect the impact\
            of the voxel-wise regressor(s). If you want to compare those results to\
            the case where you did NOT give the '-dsort' option, then also use\
            '-dsort_nods'.
        temp_storage: Write intermediate output to disk, to economize on RAM.
        mask: Read dataset as a mask for the input; voxels outside the mask\
            will not be fit by the regression model.
        output_prefix: Dataset prefix for saving REML variance parameters.
        go_for_it: Force the program to continue past a failed collinearity\
            check.
        max_b_param: Set max allowed MA b parameter.
        grid_param: Set the number of grid divisions in the (a,b) grid.
        negative_corr: Allows negative correlations to be used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dREMLfit",
        "input_file": input_file,
        "regression_matrix": regression_matrix,
        "sort_nods": sort_nods,
        "temp_storage": temp_storage,
        "go_for_it": go_for_it,
        "negative_corr": negative_corr,
    }
    if baseline_files is not None:
        params["baseline_files"] = baseline_files
    if mask is not None:
        params["mask"] = mask
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if max_b_param is not None:
        params["max_b_param"] = max_b_param
    if grid_param is not None:
        params["grid_param"] = grid_param
    return params


def v_3d_remlfit_cargs(
    params: V3dRemlfitParameters,
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
    cargs.append("3dREMLfit")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-matrix",
        execution.input_file(params.get("regression_matrix"))
    ])
    if params.get("baseline_files") is not None:
        cargs.extend([
            "-addbase",
            *params.get("baseline_files")
        ])
    if params.get("sort_nods"):
        cargs.append("-dsort_nods")
    if params.get("temp_storage"):
        cargs.append("-usetemp")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-Rvar",
            params.get("output_prefix")
        ])
    if params.get("go_for_it"):
        cargs.append("-GOFORIT")
    if params.get("max_b_param") is not None:
        cargs.extend([
            "-MAXb",
            str(params.get("max_b_param"))
        ])
    if params.get("grid_param") is not None:
        cargs.extend([
            "-Grid",
            str(params.get("grid_param"))
        ])
    if params.get("negative_corr"):
        cargs.append("-NEGcor")
    return cargs


def v_3d_remlfit_outputs(
    params: V3dRemlfitParameters,
    execution: Execution,
) -> V3dRemlfitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRemlfitOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("output_prefix") + ".nii.gz") if (params.get("output_prefix") is not None) else None,
        rvar_file=execution.output_file(params.get("output_prefix") + "_Rvar.nii.gz") if (params.get("output_prefix") is not None) else None,
        rbeta_file=execution.output_file(params.get("output_prefix") + "_Rbeta.nii.gz") if (params.get("output_prefix") is not None) else None,
        rbuck_file=execution.output_file(params.get("output_prefix") + "_Rbuck.nii.gz") if (params.get("output_prefix") is not None) else None,
        rfitts_file=execution.output_file(params.get("output_prefix") + "_Rfitts.nii.gz") if (params.get("output_prefix") is not None) else None,
        rerrts_file=execution.output_file(params.get("output_prefix") + "_Rerrts.nii.gz") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v_3d_remlfit_execute(
    params: V3dRemlfitParameters,
    execution: Execution,
) -> V3dRemlfitOutputs:
    """
    Generalized least squares time series fit, with REML estimation of the temporal
    auto-correlation structure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRemlfitOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_remlfit_cargs(params, execution)
    ret = v_3d_remlfit_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_remlfit(
    input_file: InputPathType,
    regression_matrix: InputPathType,
    baseline_files: list[str] | None = None,
    sort_nods: bool = False,
    temp_storage: bool = False,
    mask: InputPathType | None = None,
    output_prefix: str | None = None,
    go_for_it: bool = False,
    max_b_param: float | None = None,
    grid_param: float | None = None,
    negative_corr: bool = False,
    runner: Runner | None = None,
) -> V3dRemlfitOutputs:
    """
    Generalized least squares time series fit, with REML estimation of the temporal
    auto-correlation structure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Read time series dataset.
        regression_matrix: Read the regression matrix, which should have been\
            output from 3dDeconvolve via the '-x1D' option.
        baseline_files: Add baseline model columns to the matrix. Each column\
            in the specified .1D file will be appended to the matrix.
        sort_nods: If '-dsort' is used, the output datasets reflect the impact\
            of the voxel-wise regressor(s). If you want to compare those results to\
            the case where you did NOT give the '-dsort' option, then also use\
            '-dsort_nods'.
        temp_storage: Write intermediate output to disk, to economize on RAM.
        mask: Read dataset as a mask for the input; voxels outside the mask\
            will not be fit by the regression model.
        output_prefix: Dataset prefix for saving REML variance parameters.
        go_for_it: Force the program to continue past a failed collinearity\
            check.
        max_b_param: Set max allowed MA b parameter.
        grid_param: Set the number of grid divisions in the (a,b) grid.
        negative_corr: Allows negative correlations to be used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRemlfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_REMLFIT_METADATA)
    params = v_3d_remlfit_params(input_file=input_file, regression_matrix=regression_matrix, baseline_files=baseline_files, sort_nods=sort_nods, temp_storage=temp_storage, mask=mask, output_prefix=output_prefix, go_for_it=go_for_it, max_b_param=max_b_param, grid_param=grid_param, negative_corr=negative_corr)
    return v_3d_remlfit_execute(params, execution)


__all__ = [
    "V3dRemlfitOutputs",
    "V_3D_REMLFIT_METADATA",
    "v_3d_remlfit",
    "v_3d_remlfit_params",
]
