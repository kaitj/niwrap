# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_REDUCE_METADATA = Metadata(
    id="8f69a9fb5fec167f808d9feb0478740e661cda26.boutiques",
    name="metric-reduce",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class MetricReduceExcludeOutliers:
    """
    exclude non-numeric values and outliers by standard deviation.
    """
    sigma_below: float
    """number of standard deviations below the mean to include"""
    sigma_above: float
    """number of standard deviations above the mean to include"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-exclude-outliers")
        cargs.append(str(self.sigma_below))
        cargs.append(str(self.sigma_above))
        return cargs


class MetricReduceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_reduce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_reduce(
    metric_in: InputPathType,
    operation: str,
    metric_out: str,
    exclude_outliers: MetricReduceExcludeOutliers | None = None,
    opt_only_numeric: bool = False,
    runner: Runner | None = None,
) -> MetricReduceOutputs:
    """
    Perform reduction operation across metric columns.
    
    For each surface vertex, takes the data across columns as a vector, and
    performs the specified reduction on it, putting the result into the single
    output column at that vertex. The reduction operators are as follows:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric_in: the metric to reduce.
        operation: the reduction operator to use.
        metric_out: the output metric.
        exclude_outliers: exclude non-numeric values and outliers by standard\
            deviation.
        opt_only_numeric: exclude non-numeric values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricReduceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_REDUCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-reduce")
    cargs.append(execution.input_file(metric_in))
    cargs.append(operation)
    cargs.append(metric_out)
    if exclude_outliers is not None:
        cargs.extend(exclude_outliers.run(execution))
    if opt_only_numeric:
        cargs.append("-only-numeric")
    ret = MetricReduceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_REDUCE_METADATA",
    "MetricReduceExcludeOutliers",
    "MetricReduceOutputs",
    "metric_reduce",
]
