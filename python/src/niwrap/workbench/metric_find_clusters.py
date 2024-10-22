# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_FIND_CLUSTERS_METADATA = Metadata(
    id="5bfb24c9f6b693315454fc4ff224b769c7c3f6b9.boutiques",
    name="metric-find-clusters",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class MetricFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_find_clusters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_find_clusters(
    surface: InputPathType,
    metric_in: InputPathType,
    value_threshold: float,
    minimum_area: float,
    metric_out: str,
    opt_less_than: bool = False,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_size_ratio_ratio: float | None = None,
    opt_distance_distance: float | None = None,
    opt_start_startval: int | None = None,
    runner: Runner | None = None,
) -> MetricFindClustersOutputs:
    """
    Filter clusters by surface area.
    
    Outputs a metric with nonzero integers for all vertices within a large
    enough cluster, and zeros elsewhere. The integers denote cluster membership
    (by default, first cluster found will use value 1, second cluster 2, etc).
    Cluster values are not reused across maps of the output, but instead keep
    counting up. By default, values greater than <value-threshold> are
    considered to be in a cluster, use -less-than to test for values less than
    the threshold. To apply this as a mask to the data, or to do more
    complicated thresholding, see -metric-math.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface: the surface to compute on.
        metric_in: the input metric.
        value_threshold: threshold for data values.
        minimum_area: threshold for cluster area, in mm^2.
        metric_out: the output metric.
        opt_less_than: find values less than <value-threshold>, rather than\
            greater.
        opt_roi_roi_metric: select a region of interest: the roi, as a metric.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        opt_column_column: select a single column: the column number or name.
        opt_size_ratio_ratio: ignore clusters smaller than a given fraction of\
            the largest cluster in map: fraction of the largest cluster's area.
        opt_distance_distance: ignore clusters further than a given distance\
            from the largest cluster: how far from the largest cluster a cluster\
            can be, edge to edge, in mm.
        opt_start_startval: start labeling clusters from a value other than 1:\
            the value to give the first cluster found.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricFindClustersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_FIND_CLUSTERS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-find-clusters")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(str(value_threshold))
    cargs.append(str(minimum_area))
    cargs.append(metric_out)
    if opt_less_than:
        cargs.append("-less-than")
    if opt_roi_roi_metric is not None:
        cargs.extend([
            "-roi",
            execution.input_file(opt_roi_roi_metric)
        ])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(opt_corrected_areas_area_metric)
        ])
    if opt_column_column is not None:
        cargs.extend([
            "-column",
            opt_column_column
        ])
    if opt_size_ratio_ratio is not None:
        cargs.extend([
            "-size-ratio",
            str(opt_size_ratio_ratio)
        ])
    if opt_distance_distance is not None:
        cargs.extend([
            "-distance",
            str(opt_distance_distance)
        ])
    if opt_start_startval is not None:
        cargs.extend([
            "-start",
            str(opt_start_startval)
        ])
    ret = MetricFindClustersOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_FIND_CLUSTERS_METADATA",
    "MetricFindClustersOutputs",
    "metric_find_clusters",
]
