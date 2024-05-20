# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_CREATE_DENSE_TIMESERIES_METADATA = Metadata(
    id="38666dc15ec56f09ae0f0d65d1fffb32abc6b89d",
    name="cifti-create-dense-timeseries",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiCreateDenseTimeseriesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_dense_timeseries(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_dense_timeseries(
    runner: Runner,
    cifti_out: InputPathType,
    opt_left_metric_metric: InputPathType | None = None,
    opt_right_metric_metric: InputPathType | None = None,
    opt_cerebellum_metric_metric: InputPathType | None = None,
    opt_timestep_interval: float | int | None = None,
    opt_timestart_start: float | int | None = None,
    opt_unit_unit: str | None = None,
) -> CiftiCreateDenseTimeseriesOutputs:
    """
    CREATE A CIFTI DENSE TIMESERIES.
    
    All input files must have the same number of columns/subvolumes. Only the
    specified components will be in the output cifti. At least one component
    must be specified.
    
    See -volume-label-import and -volume-help for format details of label volume
    files. The structure-label-volume should have some of the label names from
    this list, all other label names will be ignored:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    
    The -unit option accepts these values:
    
    SECOND
    HERTZ
    METER
    RADIAN
    
    Args:
        runner: Command runner
        cifti_out: the output cifti file
        opt_left_metric_metric: metric for left surface: the metric file
        opt_right_metric_metric: metric for left surface: the metric file
        opt_cerebellum_metric_metric: metric for the cerebellum: the metric file
        opt_timestep_interval: set the timestep: the timestep, in seconds
            (default 1.0)
        opt_timestart_start: set the start time: the time at the first frame, in
            seconds (default 0.0)
        opt_unit_unit: use a unit other than time: unit identifier (default
            SECOND)
    Returns:
        NamedTuple of outputs (described in `CiftiCreateDenseTimeseriesOutputs`).
    """
    execution = runner.start_execution(CIFTI_CREATE_DENSE_TIMESERIES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-dense-timeseries")
    cargs.append(execution.input_file(cifti_out))
    if opt_left_metric_metric is not None:
        cargs.extend(["-left-metric", execution.input_file(opt_left_metric_metric)])
    if opt_right_metric_metric is not None:
        cargs.extend(["-right-metric", execution.input_file(opt_right_metric_metric)])
    if opt_cerebellum_metric_metric is not None:
        cargs.extend(["-cerebellum-metric", execution.input_file(opt_cerebellum_metric_metric)])
    if opt_timestep_interval is not None:
        cargs.extend(["-timestep", str(opt_timestep_interval)])
    if opt_timestart_start is not None:
        cargs.extend(["-timestart", str(opt_timestart_start)])
    if opt_unit_unit is not None:
        cargs.extend(["-unit", opt_unit_unit])
    ret = CiftiCreateDenseTimeseriesOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
