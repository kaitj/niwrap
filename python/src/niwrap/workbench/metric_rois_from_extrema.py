# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_ROIS_FROM_EXTREMA_METADATA = Metadata(
    id="8077c16d8f1d062ca939cbb2744aaee3511e4ec7.boutiques",
    name="metric-rois-from-extrema",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricRoisFromExtremaParameters = typing.TypedDict('MetricRoisFromExtremaParameters', {
    "__STYX_TYPE__": typing.Literal["metric-rois-from-extrema"],
    "surface": InputPathType,
    "metric": InputPathType,
    "limit": float,
    "metric_out": str,
    "opt_gaussian_sigma": typing.NotRequired[float | None],
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "opt_overlap_logic_method": typing.NotRequired[str | None],
    "opt_column_column": typing.NotRequired[str | None],
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
        "metric-rois-from-extrema": metric_rois_from_extrema_cargs,
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
        "metric-rois-from-extrema": metric_rois_from_extrema_outputs,
    }
    return vt.get(t)


class MetricRoisFromExtremaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_rois_from_extrema(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def metric_rois_from_extrema_params(
    surface: InputPathType,
    metric: InputPathType,
    limit: float,
    metric_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_column_column: str | None = None,
) -> MetricRoisFromExtremaParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to use for geodesic distance.
        metric: the input metric file.
        limit: geodesic distance limit from vertex, in mm.
        metric_out: the output metric file.
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:\
            the sigma for the gaussian kernel, in mm.
        opt_roi_roi_metric: select a region of interest to use: the area to\
            use, as a metric.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_column_column: select a single input column to use: the column\
            number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-rois-from-extrema",
        "surface": surface,
        "metric": metric,
        "limit": limit,
        "metric_out": metric_out,
    }
    if opt_gaussian_sigma is not None:
        params["opt_gaussian_sigma"] = opt_gaussian_sigma
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if opt_overlap_logic_method is not None:
        params["opt_overlap_logic_method"] = opt_overlap_logic_method
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    return params


def metric_rois_from_extrema_cargs(
    params: MetricRoisFromExtremaParameters,
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
    cargs.append("wb_command")
    cargs.append("-metric-rois-from-extrema")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric")))
    cargs.append(str(params.get("limit")))
    cargs.append(params.get("metric_out"))
    if params.get("opt_gaussian_sigma") is not None:
        cargs.extend([
            "-gaussian",
            str(params.get("opt_gaussian_sigma"))
        ])
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("opt_overlap_logic_method") is not None:
        cargs.extend([
            "-overlap-logic",
            params.get("opt_overlap_logic_method")
        ])
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    return cargs


def metric_rois_from_extrema_outputs(
    params: MetricRoisFromExtremaParameters,
    execution: Execution,
) -> MetricRoisFromExtremaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricRoisFromExtremaOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_rois_from_extrema_execute(
    params: MetricRoisFromExtremaParameters,
    execution: Execution,
) -> MetricRoisFromExtremaOutputs:
    """
    Create metric roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricRoisFromExtremaOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metric_rois_from_extrema_cargs(params, execution)
    ret = metric_rois_from_extrema_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_rois_from_extrema(
    surface: InputPathType,
    metric: InputPathType,
    limit: float,
    metric_out: str,
    opt_gaussian_sigma: float | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_overlap_logic_method: str | None = None,
    opt_column_column: str | None = None,
    runner: Runner | None = None,
) -> MetricRoisFromExtremaOutputs:
    """
    Create metric roi maps from extrema maps.
    
    For each nonzero value in each map, make a map with an ROI around that
    location. If the -gaussian option is specified, then normalized gaussian
    kernels are output instead of ROIs. The <method> argument to -overlap-logic
    must be one of ALLOW, CLOSEST, or EXCLUDE. ALLOW is the default, and means
    that ROIs are treated independently and may overlap. CLOSEST means that ROIs
    may not overlap, and that no ROI contains vertices that are closer to a
    different seed vertex. EXCLUDE means that ROIs may not overlap, and that any
    vertex within range of more than one ROI does not belong to any ROI.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to use for geodesic distance.
        metric: the input metric file.
        limit: geodesic distance limit from vertex, in mm.
        metric_out: the output metric file.
        opt_gaussian_sigma: generate a gaussian kernel instead of a flat ROI:\
            the sigma for the gaussian kernel, in mm.
        opt_roi_roi_metric: select a region of interest to use: the area to\
            use, as a metric.
        opt_overlap_logic_method: how to handle overlapping ROIs, default\
            ALLOW: the method of resolving overlaps.
        opt_column_column: select a single input column to use: the column\
            number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricRoisFromExtremaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ROIS_FROM_EXTREMA_METADATA)
    params = metric_rois_from_extrema_params(surface=surface, metric=metric, limit=limit, metric_out=metric_out, opt_gaussian_sigma=opt_gaussian_sigma, opt_roi_roi_metric=opt_roi_roi_metric, opt_overlap_logic_method=opt_overlap_logic_method, opt_column_column=opt_column_column)
    return metric_rois_from_extrema_execute(params, execution)


__all__ = [
    "METRIC_ROIS_FROM_EXTREMA_METADATA",
    "MetricRoisFromExtremaOutputs",
    "metric_rois_from_extrema",
    "metric_rois_from_extrema_params",
]
