# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

METRIC_TFCE_METADATA = Metadata(
    id="9baf4e0d50cc6f0f392ab929c38e08f04f8b352f.boutiques",
    name="metric-tfce",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetricTfcePresmoothParameters = typing.TypedDict('MetricTfcePresmoothParameters', {
    "__STYX_TYPE__": typing.Literal["presmooth"],
    "kernel": float,
    "opt_fwhm": bool,
})
MetricTfceParametersParameters = typing.TypedDict('MetricTfceParametersParameters', {
    "__STYX_TYPE__": typing.Literal["parameters"],
    "e": float,
    "h": float,
})
MetricTfceParameters = typing.TypedDict('MetricTfceParameters', {
    "__STYX_TYPE__": typing.Literal["metric-tfce"],
    "surface": InputPathType,
    "metric_in": InputPathType,
    "metric_out": str,
    "presmooth": typing.NotRequired[MetricTfcePresmoothParameters | None],
    "opt_roi_roi_metric": typing.NotRequired[InputPathType | None],
    "parameters": typing.NotRequired[MetricTfceParametersParameters | None],
    "opt_column_column": typing.NotRequired[str | None],
    "opt_corrected_areas_area_metric": typing.NotRequired[InputPathType | None],
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
        "metric-tfce": metric_tfce_cargs,
        "presmooth": metric_tfce_presmooth_cargs,
        "parameters": metric_tfce_parameters_cargs,
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
        "metric-tfce": metric_tfce_outputs,
    }.get(t)


def metric_tfce_presmooth_params(
    kernel: float,
    opt_fwhm: bool = False,
) -> MetricTfcePresmoothParameters:
    """
    Build parameters.
    
    Args:
        kernel: the size of the gaussian smoothing kernel in mm, as sigma by\
            default.
        opt_fwhm: kernel size is FWHM, not sigma.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "presmooth",
        "kernel": kernel,
        "opt_fwhm": opt_fwhm,
    }
    return params


def metric_tfce_presmooth_cargs(
    params: MetricTfcePresmoothParameters,
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
    cargs.append("-presmooth")
    cargs.append(str(params.get("kernel")))
    if params.get("opt_fwhm"):
        cargs.append("-fwhm")
    return cargs


def metric_tfce_parameters_params(
    e: float,
    h: float,
) -> MetricTfceParametersParameters:
    """
    Build parameters.
    
    Args:
        e: exponent for cluster area (default 1.0).
        h: exponent for threshold value (default 2.0).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "parameters",
        "e": e,
        "h": h,
    }
    return params


def metric_tfce_parameters_cargs(
    params: MetricTfceParametersParameters,
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
    cargs.append("-parameters")
    cargs.append(str(params.get("e")))
    cargs.append(str(params.get("h")))
    return cargs


class MetricTfceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_tfce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_tfce_params(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    presmooth: MetricTfcePresmoothParameters | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    parameters: MetricTfceParametersParameters | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricTfceParameters:
    """
    Build parameters.
    
    Args:
        surface: the surface to compute on.
        metric_in: the metric to run TFCE on.
        metric_out: the output metric.
        presmooth: smooth the metric before running TFCE.
        opt_roi_roi_metric: select a region of interest to run TFCE on: the\
            area to run TFCE on, as a metric.
        parameters: set parameters for TFCE integral.
        opt_column_column: select a single column: the column number or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric-tfce",
        "surface": surface,
        "metric_in": metric_in,
        "metric_out": metric_out,
    }
    if presmooth is not None:
        params["presmooth"] = presmooth
    if opt_roi_roi_metric is not None:
        params["opt_roi_roi_metric"] = opt_roi_roi_metric
    if parameters is not None:
        params["parameters"] = parameters
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if opt_corrected_areas_area_metric is not None:
        params["opt_corrected_areas_area_metric"] = opt_corrected_areas_area_metric
    return params


def metric_tfce_cargs(
    params: MetricTfceParameters,
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
    cargs.append("-metric-tfce")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("metric_in")))
    cargs.append(params.get("metric_out"))
    if params.get("presmooth") is not None:
        cargs.extend(dyn_cargs(params.get("presmooth")["__STYXTYPE__"])(params.get("presmooth"), execution))
    if params.get("opt_roi_roi_metric") is not None:
        cargs.extend([
            "-roi",
            execution.input_file(params.get("opt_roi_roi_metric"))
        ])
    if params.get("parameters") is not None:
        cargs.extend(dyn_cargs(params.get("parameters")["__STYXTYPE__"])(params.get("parameters"), execution))
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("opt_corrected_areas_area_metric") is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(params.get("opt_corrected_areas_area_metric"))
        ])
    return cargs


def metric_tfce_outputs(
    params: MetricTfceParameters,
    execution: Execution,
) -> MetricTfceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetricTfceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
    )
    return ret


def metric_tfce_execute(
    params: MetricTfceParameters,
    execution: Execution,
) -> MetricTfceOutputs:
    """
    Do tfce on a metric file.
    
    This command does not do any statistical analysis. Please use something like
    PALM if you are just trying to do statistics on your data.
    
    Threshold-free cluster enhancement is a method to increase the relative
    value of regions that would form clusters in a standard thresholding test.
    This is accomplished by evaluating the integral of:
    
    e(h, p)^E * h^H * dh
    
    at each vertex p, where h ranges from 0 to the maximum value in the data,
    and e(h, p) is the extent of the cluster containing vertex p at threshold h.
    Negative values are similarly enhanced by negating the data, running the
    same process, and negating the result.
    
    When using -presmooth with -corrected-areas, note that it is an approximate
    correction within the smoothing algorithm (the TFCE correction is exact).
    Doing smoothing on individual surfaces before averaging/TFCE is preferred,
    when possible, in order to better tie the smoothing kernel size to the
    original feature size.
    
    The TFCE method is explained in: Smith SM, Nichols TE., "Threshold-free
    cluster enhancement: addressing problems of smoothing, threshold dependence
    and localisation in cluster inference." Neuroimage. 2009 Jan 1;44(1):83-98.
    PMID: 18501637.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetricTfceOutputs`).
    """
    params = execution.params(params)
    cargs = metric_tfce_cargs(params, execution)
    ret = metric_tfce_outputs(params, execution)
    execution.run(cargs)
    return ret


def metric_tfce(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    presmooth: MetricTfcePresmoothParameters | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    parameters: MetricTfceParametersParameters | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> MetricTfceOutputs:
    """
    Do tfce on a metric file.
    
    This command does not do any statistical analysis. Please use something like
    PALM if you are just trying to do statistics on your data.
    
    Threshold-free cluster enhancement is a method to increase the relative
    value of regions that would form clusters in a standard thresholding test.
    This is accomplished by evaluating the integral of:
    
    e(h, p)^E * h^H * dh
    
    at each vertex p, where h ranges from 0 to the maximum value in the data,
    and e(h, p) is the extent of the cluster containing vertex p at threshold h.
    Negative values are similarly enhanced by negating the data, running the
    same process, and negating the result.
    
    When using -presmooth with -corrected-areas, note that it is an approximate
    correction within the smoothing algorithm (the TFCE correction is exact).
    Doing smoothing on individual surfaces before averaging/TFCE is preferred,
    when possible, in order to better tie the smoothing kernel size to the
    original feature size.
    
    The TFCE method is explained in: Smith SM, Nichols TE., "Threshold-free
    cluster enhancement: addressing problems of smoothing, threshold dependence
    and localisation in cluster inference." Neuroimage. 2009 Jan 1;44(1):83-98.
    PMID: 18501637.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute on.
        metric_in: the metric to run TFCE on.
        metric_out: the output metric.
        presmooth: smooth the metric before running TFCE.
        opt_roi_roi_metric: select a region of interest to run TFCE on: the\
            area to run TFCE on, as a metric.
        parameters: set parameters for TFCE integral.
        opt_column_column: select a single column: the column number or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricTfceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_TFCE_METADATA)
    params = metric_tfce_params(surface=surface, metric_in=metric_in, metric_out=metric_out, presmooth=presmooth, opt_roi_roi_metric=opt_roi_roi_metric, parameters=parameters, opt_column_column=opt_column_column, opt_corrected_areas_area_metric=opt_corrected_areas_area_metric)
    return metric_tfce_execute(params, execution)


__all__ = [
    "METRIC_TFCE_METADATA",
    "MetricTfceOutputs",
    "MetricTfceParameters",
    "MetricTfceParametersParameters",
    "MetricTfcePresmoothParameters",
    "metric_tfce",
    "metric_tfce_parameters_params",
    "metric_tfce_params",
    "metric_tfce_presmooth_params",
]
