# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BIANCA_CLUSTER_STATS_METADATA = Metadata(
    id="7bb9fbd0c4cce5e06e0aa8bae75dec0c569b1f20.boutiques",
    name="bianca_cluster_stats",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
BiancaClusterStatsParameters = typing.TypedDict('BiancaClusterStatsParameters', {
    "__STYX_TYPE__": typing.Literal["bianca_cluster_stats"],
    "bianca_output_map": InputPathType,
    "threshold": float,
    "min_cluster_size": float,
    "mask": typing.NotRequired[InputPathType | None],
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
        "bianca_cluster_stats": bianca_cluster_stats_cargs,
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
    vt = {}
    return vt.get(t)


def bianca_cluster_stats_params(
    bianca_output_map: InputPathType,
    threshold: float,
    min_cluster_size: float,
    mask: InputPathType | None = None,
) -> BiancaClusterStatsParameters:
    """
    Build parameters.
    
    Args:
        bianca_output_map: BIANCA output map file.
        threshold: Threshold value to apply.
        min_cluster_size: Minimum cluster size in voxels.
        mask: Optional mask file (in the same space as the BIANCA output map).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bianca_cluster_stats",
        "bianca_output_map": bianca_output_map,
        "threshold": threshold,
        "min_cluster_size": min_cluster_size,
    }
    if mask is not None:
        params["mask"] = mask
    return params


def bianca_cluster_stats_cargs(
    params: BiancaClusterStatsParameters,
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
    cargs.append("bianca_cluster_stats")
    cargs.append(execution.input_file(params.get("bianca_output_map")))
    cargs.append(str(params.get("threshold")))
    cargs.append(str(params.get("min_cluster_size")))
    if params.get("mask") is not None:
        cargs.append(execution.input_file(params.get("mask")))
    return cargs


def bianca_cluster_stats_outputs(
    params: BiancaClusterStatsParameters,
    execution: Execution,
) -> BiancaClusterStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BiancaClusterStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def bianca_cluster_stats_execute(
    params: BiancaClusterStatsParameters,
    execution: Execution,
) -> BiancaClusterStatsOutputs:
    """
    Calculate number of clusters and WMH volume in a BIANCA output map.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BiancaClusterStatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = bianca_cluster_stats_cargs(params, execution)
    ret = bianca_cluster_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def bianca_cluster_stats(
    bianca_output_map: InputPathType,
    threshold: float,
    min_cluster_size: float,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> BiancaClusterStatsOutputs:
    """
    Calculate number of clusters and WMH volume in a BIANCA output map.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        bianca_output_map: BIANCA output map file.
        threshold: Threshold value to apply.
        min_cluster_size: Minimum cluster size in voxels.
        mask: Optional mask file (in the same space as the BIANCA output map).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BiancaClusterStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BIANCA_CLUSTER_STATS_METADATA)
    params = bianca_cluster_stats_params(bianca_output_map=bianca_output_map, threshold=threshold, min_cluster_size=min_cluster_size, mask=mask)
    return bianca_cluster_stats_execute(params, execution)


__all__ = [
    "BIANCA_CLUSTER_STATS_METADATA",
    "bianca_cluster_stats",
    "bianca_cluster_stats_params",
]
