# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_SEPARATE_METADATA = Metadata(
    id="41d4890a042ed121dafd6bdf71322fef11d629bf.boutiques",
    name="cifti-separate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiSeparateVolumeAllParameters = typing.TypedDict('CiftiSeparateVolumeAllParameters', {
    "__STYX_TYPE__": typing.Literal["volume_all"],
    "volume_out": str,
    "opt_roi_roi_out": typing.NotRequired[str | None],
    "opt_label_label_out": typing.NotRequired[str | None],
    "opt_crop": bool,
})
CiftiSeparateLabelParameters = typing.TypedDict('CiftiSeparateLabelParameters', {
    "__STYX_TYPE__": typing.Literal["label"],
    "structure": str,
    "label_out": str,
    "opt_roi_roi_out": typing.NotRequired[str | None],
})
CiftiSeparateMetricParameters = typing.TypedDict('CiftiSeparateMetricParameters', {
    "__STYX_TYPE__": typing.Literal["metric"],
    "structure": str,
    "metric_out": str,
    "opt_roi_roi_out": typing.NotRequired[str | None],
})
CiftiSeparateVolumeParameters = typing.TypedDict('CiftiSeparateVolumeParameters', {
    "__STYX_TYPE__": typing.Literal["volume"],
    "structure": str,
    "volume_out": str,
    "opt_roi_roi_out": typing.NotRequired[str | None],
    "opt_crop": bool,
})
CiftiSeparateParameters = typing.TypedDict('CiftiSeparateParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-separate"],
    "cifti_in": InputPathType,
    "direction": str,
    "volume_all": typing.NotRequired[CiftiSeparateVolumeAllParameters | None],
    "label": typing.NotRequired[list[CiftiSeparateLabelParameters] | None],
    "metric": typing.NotRequired[list[CiftiSeparateMetricParameters] | None],
    "volume": typing.NotRequired[list[CiftiSeparateVolumeParameters] | None],
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
        "cifti-separate": cifti_separate_cargs,
        "volume_all": cifti_separate_volume_all_cargs,
        "label": cifti_separate_label_cargs,
        "metric": cifti_separate_metric_cargs,
        "volume": cifti_separate_volume_cargs,
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
        "cifti-separate": cifti_separate_outputs,
        "volume_all": cifti_separate_volume_all_outputs,
        "label": cifti_separate_label_outputs,
        "metric": cifti_separate_metric_outputs,
        "volume": cifti_separate_volume_outputs,
    }.get(t)


class CiftiSeparateVolumeAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `CiftiSeparateVolumeAllParameters | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""
    opt_roi_roi_out: OutputPathType | None
    """also output the roi of which voxels have data: the roi output volume"""
    opt_label_label_out: OutputPathType | None
    """output a volume label file indicating the location of structures: the
    label output volume"""


def cifti_separate_volume_all_params(
    volume_out: str,
    opt_roi_roi_out: str | None = None,
    opt_label_label_out: str | None = None,
    opt_crop: bool = False,
) -> CiftiSeparateVolumeAllParameters:
    """
    Build parameters.
    
    Args:
        volume_out: the output volume.
        opt_roi_roi_out: also output the roi of which voxels have data: the roi\
            output volume.
        opt_label_label_out: output a volume label file indicating the location\
            of structures: the label output volume.
        opt_crop: crop volume to the size of the data rather than using the\
            original volume size.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume_all",
        "volume_out": volume_out,
        "opt_crop": opt_crop,
    }
    if opt_roi_roi_out is not None:
        params["opt_roi_roi_out"] = opt_roi_roi_out
    if opt_label_label_out is not None:
        params["opt_label_label_out"] = opt_label_label_out
    return params


def cifti_separate_volume_all_cargs(
    params: CiftiSeparateVolumeAllParameters,
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
    cargs.append("-volume-all")
    cargs.append(params.get("volume_out"))
    if params.get("opt_roi_roi_out") is not None:
        cargs.extend([
            "-roi",
            params.get("opt_roi_roi_out")
        ])
    if params.get("opt_label_label_out") is not None:
        cargs.extend([
            "-label",
            params.get("opt_label_label_out")
        ])
    if params.get("opt_crop"):
        cargs.append("-crop")
    return cargs


def cifti_separate_volume_all_outputs(
    params: CiftiSeparateVolumeAllParameters,
    execution: Execution,
) -> CiftiSeparateVolumeAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiSeparateVolumeAllOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
        opt_roi_roi_out=execution.output_file(params.get("opt_roi_roi_out")) if (params.get("opt_roi_roi_out") is not None) else None,
        opt_label_label_out=execution.output_file(params.get("opt_label_label_out")) if (params.get("opt_label_label_out") is not None) else None,
    )
    return ret


class CiftiSeparateLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `list[CiftiSeparateLabelParameters] | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""
    opt_roi_roi_out: OutputPathType | None
    """also output the roi of which vertices have data: the roi output metric"""


def cifti_separate_label_params(
    structure: str,
    label_out: str,
    opt_roi_roi_out: str | None = None,
) -> CiftiSeparateLabelParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to output.
        label_out: the output label file.
        opt_roi_roi_out: also output the roi of which vertices have data: the\
            roi output metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label",
        "structure": structure,
        "label_out": label_out,
    }
    if opt_roi_roi_out is not None:
        params["opt_roi_roi_out"] = opt_roi_roi_out
    return params


def cifti_separate_label_cargs(
    params: CiftiSeparateLabelParameters,
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
    cargs.append("-label")
    cargs.append(params.get("structure"))
    cargs.append(params.get("label_out"))
    if params.get("opt_roi_roi_out") is not None:
        cargs.extend([
            "-roi",
            params.get("opt_roi_roi_out")
        ])
    return cargs


def cifti_separate_label_outputs(
    params: CiftiSeparateLabelParameters,
    execution: Execution,
) -> CiftiSeparateLabelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiSeparateLabelOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(params.get("label_out")),
        opt_roi_roi_out=execution.output_file(params.get("opt_roi_roi_out")) if (params.get("opt_roi_roi_out") is not None) else None,
    )
    return ret


class CiftiSeparateMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `list[CiftiSeparateMetricParameters] | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""
    opt_roi_roi_out: OutputPathType | None
    """also output the roi of which vertices have data: the roi output metric"""


def cifti_separate_metric_params(
    structure: str,
    metric_out: str,
    opt_roi_roi_out: str | None = None,
) -> CiftiSeparateMetricParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to output.
        metric_out: the output metric.
        opt_roi_roi_out: also output the roi of which vertices have data: the\
            roi output metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metric",
        "structure": structure,
        "metric_out": metric_out,
    }
    if opt_roi_roi_out is not None:
        params["opt_roi_roi_out"] = opt_roi_roi_out
    return params


def cifti_separate_metric_cargs(
    params: CiftiSeparateMetricParameters,
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
    cargs.append("-metric")
    cargs.append(params.get("structure"))
    cargs.append(params.get("metric_out"))
    if params.get("opt_roi_roi_out") is not None:
        cargs.extend([
            "-roi",
            params.get("opt_roi_roi_out")
        ])
    return cargs


def cifti_separate_metric_outputs(
    params: CiftiSeparateMetricParameters,
    execution: Execution,
) -> CiftiSeparateMetricOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiSeparateMetricOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(params.get("metric_out")),
        opt_roi_roi_out=execution.output_file(params.get("opt_roi_roi_out")) if (params.get("opt_roi_roi_out") is not None) else None,
    )
    return ret


class CiftiSeparateVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `list[CiftiSeparateVolumeParameters] | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""
    opt_roi_roi_out: OutputPathType | None
    """also output the roi of which voxels have data: the roi output volume"""


def cifti_separate_volume_params(
    structure: str,
    volume_out: str,
    opt_roi_roi_out: str | None = None,
    opt_crop: bool = False,
) -> CiftiSeparateVolumeParameters:
    """
    Build parameters.
    
    Args:
        structure: the structure to output.
        volume_out: the output volume.
        opt_roi_roi_out: also output the roi of which voxels have data: the roi\
            output volume.
        opt_crop: crop volume to the size of the component rather than using\
            the original volume size.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume",
        "structure": structure,
        "volume_out": volume_out,
        "opt_crop": opt_crop,
    }
    if opt_roi_roi_out is not None:
        params["opt_roi_roi_out"] = opt_roi_roi_out
    return params


def cifti_separate_volume_cargs(
    params: CiftiSeparateVolumeParameters,
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
    cargs.append("-volume")
    cargs.append(params.get("structure"))
    cargs.append(params.get("volume_out"))
    if params.get("opt_roi_roi_out") is not None:
        cargs.extend([
            "-roi",
            params.get("opt_roi_roi_out")
        ])
    if params.get("opt_crop"):
        cargs.append("-crop")
    return cargs


def cifti_separate_volume_outputs(
    params: CiftiSeparateVolumeParameters,
    execution: Execution,
) -> CiftiSeparateVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiSeparateVolumeOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
        opt_roi_roi_out=execution.output_file(params.get("opt_roi_roi_out")) if (params.get("opt_roi_roi_out") is not None) else None,
    )
    return ret


class CiftiSeparateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_separate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_all: CiftiSeparateVolumeAllOutputs | None
    """Outputs from `cifti_separate_volume_all_outputs`."""
    label: list[CiftiSeparateLabelOutputs] | None
    """Outputs from `cifti_separate_label_outputs`.This is a list of outputs
    with the same length and order as the inputs."""
    metric: list[CiftiSeparateMetricOutputs] | None
    """Outputs from `cifti_separate_metric_outputs`.This is a list of outputs
    with the same length and order as the inputs."""
    volume: list[CiftiSeparateVolumeOutputs] | None
    """Outputs from `cifti_separate_volume_outputs`.This is a list of outputs
    with the same length and order as the inputs."""


def cifti_separate_params(
    cifti_in: InputPathType,
    direction: str,
    volume_all: CiftiSeparateVolumeAllParameters | None = None,
    label: list[CiftiSeparateLabelParameters] | None = None,
    metric: list[CiftiSeparateMetricParameters] | None = None,
    volume: list[CiftiSeparateVolumeParameters] | None = None,
) -> CiftiSeparateParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the cifti to separate a component of.
        direction: which direction to separate into components, ROW or COLUMN.
        volume_all: separate all volume structures into a volume file.
        label: separate a surface model into a surface label file.
        metric: separate a surface model into a metric file.
        volume: separate a volume structure into a volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-separate",
        "cifti_in": cifti_in,
        "direction": direction,
    }
    if volume_all is not None:
        params["volume_all"] = volume_all
    if label is not None:
        params["label"] = label
    if metric is not None:
        params["metric"] = metric
    if volume is not None:
        params["volume"] = volume
    return params


def cifti_separate_cargs(
    params: CiftiSeparateParameters,
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
    cargs.append("-cifti-separate")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("direction"))
    if params.get("volume_all") is not None:
        cargs.extend(dyn_cargs(params.get("volume_all")["__STYXTYPE__"])(params.get("volume_all"), execution))
    if params.get("label") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("label")] for a in c])
    if params.get("metric") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("metric")] for a in c])
    if params.get("volume") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("volume")] for a in c])
    return cargs


def cifti_separate_outputs(
    params: CiftiSeparateParameters,
    execution: Execution,
) -> CiftiSeparateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiSeparateOutputs(
        root=execution.output_file("."),
        volume_all=dyn_outputs(params.get("volume_all")["__STYXTYPE__"])(params.get("volume_all"), execution) if params.get("volume_all") else None,
        label=[dyn_outputs(i["__STYXTYPE__"])(i, execution) if dyn_outputs(i["__STYXTYPE__"]) else None for i in params.get("label")] if params.get("label") else None,
        metric=[dyn_outputs(i["__STYXTYPE__"])(i, execution) if dyn_outputs(i["__STYXTYPE__"]) else None for i in params.get("metric")] if params.get("metric") else None,
        volume=[dyn_outputs(i["__STYXTYPE__"])(i, execution) if dyn_outputs(i["__STYXTYPE__"]) else None for i in params.get("volume")] if params.get("volume") else None,
    )
    return ret


def cifti_separate_execute(
    params: CiftiSeparateParameters,
    execution: Execution,
) -> CiftiSeparateOutputs:
    """
    Write a cifti structure as metric, label or volume.
    
    For dtseries, dscalar, and dlabel, use COLUMN for <direction>, and if you
    have a symmetric dconn, COLUMN is more efficient.
    
    You must specify at least one of -metric, -volume-all, -volume, or -label
    for this command to do anything. Output volumes will spatially line up with
    their original positions, whether or not they are cropped. Volume files
    produced by separating a dlabel file, or from the -label suboption of
    -volume-all, will be label volumes, see -volume-help.
    
    For each <structure> argument, use one of the following strings:
    
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
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiSeparateOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_separate_cargs(params, execution)
    ret = cifti_separate_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_separate(
    cifti_in: InputPathType,
    direction: str,
    volume_all: CiftiSeparateVolumeAllParameters | None = None,
    label: list[CiftiSeparateLabelParameters] | None = None,
    metric: list[CiftiSeparateMetricParameters] | None = None,
    volume: list[CiftiSeparateVolumeParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiSeparateOutputs:
    """
    Write a cifti structure as metric, label or volume.
    
    For dtseries, dscalar, and dlabel, use COLUMN for <direction>, and if you
    have a symmetric dconn, COLUMN is more efficient.
    
    You must specify at least one of -metric, -volume-all, -volume, or -label
    for this command to do anything. Output volumes will spatially line up with
    their original positions, whether or not they are cropped. Volume files
    produced by separating a dlabel file, or from the -label suboption of
    -volume-all, will be label volumes, see -volume-help.
    
    For each <structure> argument, use one of the following strings:
    
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
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti to separate a component of.
        direction: which direction to separate into components, ROW or COLUMN.
        volume_all: separate all volume structures into a volume file.
        label: separate a surface model into a surface label file.
        metric: separate a surface model into a metric file.
        volume: separate a volume structure into a volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiSeparateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_SEPARATE_METADATA)
    params = cifti_separate_params(cifti_in=cifti_in, direction=direction, volume_all=volume_all, label=label, metric=metric, volume=volume)
    return cifti_separate_execute(params, execution)


__all__ = [
    "CIFTI_SEPARATE_METADATA",
    "CiftiSeparateLabelOutputs",
    "CiftiSeparateLabelParameters",
    "CiftiSeparateMetricOutputs",
    "CiftiSeparateMetricParameters",
    "CiftiSeparateOutputs",
    "CiftiSeparateParameters",
    "CiftiSeparateVolumeAllOutputs",
    "CiftiSeparateVolumeAllParameters",
    "CiftiSeparateVolumeOutputs",
    "CiftiSeparateVolumeParameters",
    "cifti_separate",
    "cifti_separate_label_params",
    "cifti_separate_metric_params",
    "cifti_separate_params",
    "cifti_separate_volume_all_params",
    "cifti_separate_volume_params",
]
