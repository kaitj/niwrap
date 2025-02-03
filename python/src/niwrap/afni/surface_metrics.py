# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_METRICS_METADATA = Metadata(
    id="5e58dccd9bd1540ac2ae342efc61a7a9fc45c4c2.boutiques",
    name="SurfaceMetrics",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfaceMetricsParameters = typing.TypedDict('SurfaceMetricsParameters', {
    "__STYX_TYPE__": typing.Literal["SurfaceMetrics"],
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "internal_nodes": bool,
    "surf1": str,
    "tlrc": bool,
    "prefix": typing.NotRequired[str | None],
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
        "SurfaceMetrics": surface_metrics_cargs,
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


def surface_metrics_params(
    surf1: str,
    internal_nodes: bool = False,
    internal_nodes_: bool = False,
    internal_nodes_2: bool = False,
    internal_nodes_3: bool = False,
    internal_nodes_4: bool = False,
    internal_nodes_5: bool = False,
    internal_nodes_6: bool = False,
    internal_nodes_7: bool = False,
    internal_nodes_8: bool = False,
    internal_nodes_9: bool = False,
    internal_nodes_10: bool = False,
    internal_nodes_11: bool = False,
    internal_nodes_12: bool = False,
    internal_nodes_13: bool = False,
    internal_nodes_14: bool = False,
    internal_nodes_15: bool = False,
    internal_nodes_16: bool = False,
    internal_nodes_17: bool = False,
    internal_nodes_18: bool = False,
    internal_nodes_19: bool = False,
    tlrc: bool = False,
    prefix: str | None = None,
) -> SurfaceMetricsParameters:
    """
    Build parameters.
    
    Args:
        surf1: Specifies the input surface.
        internal_nodes: Output nodes that are not a boundary.
        internal_nodes_: Output nodes that are not a boundary.
        internal_nodes_2: Output nodes that are not a boundary.
        internal_nodes_3: Output nodes that are not a boundary.
        internal_nodes_4: Output nodes that are not a boundary.
        internal_nodes_5: Output nodes that are not a boundary.
        internal_nodes_6: Output nodes that are not a boundary.
        internal_nodes_7: Output nodes that are not a boundary.
        internal_nodes_8: Output nodes that are not a boundary.
        internal_nodes_9: Output nodes that are not a boundary.
        internal_nodes_10: Output nodes that are not a boundary.
        internal_nodes_11: Output nodes that are not a boundary.
        internal_nodes_12: Output nodes that are not a boundary.
        internal_nodes_13: Output nodes that are not a boundary.
        internal_nodes_14: Output nodes that are not a boundary.
        internal_nodes_15: Output nodes that are not a boundary.
        internal_nodes_16: Output nodes that are not a boundary.
        internal_nodes_17: Output nodes that are not a boundary.
        internal_nodes_18: Output nodes that are not a boundary.
        internal_nodes_19: Output nodes that are not a boundary.
        tlrc: Apply Talairach transform to surface.
        prefix: Use prefix for output files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfaceMetrics",
        "internal_nodes": internal_nodes,
        "internal_nodes": internal_nodes_,
        "internal_nodes": internal_nodes_2,
        "internal_nodes": internal_nodes_3,
        "internal_nodes": internal_nodes_4,
        "internal_nodes": internal_nodes_5,
        "internal_nodes": internal_nodes_6,
        "internal_nodes": internal_nodes_7,
        "internal_nodes": internal_nodes_8,
        "internal_nodes": internal_nodes_9,
        "internal_nodes": internal_nodes_10,
        "internal_nodes": internal_nodes_11,
        "internal_nodes": internal_nodes_12,
        "internal_nodes": internal_nodes_13,
        "internal_nodes": internal_nodes_14,
        "internal_nodes": internal_nodes_15,
        "internal_nodes": internal_nodes_16,
        "internal_nodes": internal_nodes_17,
        "internal_nodes": internal_nodes_18,
        "internal_nodes": internal_nodes_19,
        "surf1": surf1,
        "tlrc": tlrc,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def surface_metrics_cargs(
    params: SurfaceMetricsParameters,
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
    cargs.append("SurfaceMetrics")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    if params.get("internal_nodes"):
        cargs.append("-internal_nodes")
    cargs.extend([
        "-SURF_1",
        params.get("surf1")
    ])
    if params.get("tlrc"):
        cargs.append("-tlrc")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def surface_metrics_outputs(
    params: SurfaceMetricsParameters,
    execution: Execution,
) -> SurfaceMetricsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceMetricsOutputs(
        root=execution.output_file("."),
    )
    return ret


def surface_metrics_execute(
    params: SurfaceMetricsParameters,
    execution: Execution,
) -> SurfaceMetricsOutputs:
    """
    Outputs information about a surface's mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceMetricsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_metrics_cargs(params, execution)
    ret = surface_metrics_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_metrics(
    surf1: str,
    internal_nodes: bool = False,
    internal_nodes_: bool = False,
    internal_nodes_2: bool = False,
    internal_nodes_3: bool = False,
    internal_nodes_4: bool = False,
    internal_nodes_5: bool = False,
    internal_nodes_6: bool = False,
    internal_nodes_7: bool = False,
    internal_nodes_8: bool = False,
    internal_nodes_9: bool = False,
    internal_nodes_10: bool = False,
    internal_nodes_11: bool = False,
    internal_nodes_12: bool = False,
    internal_nodes_13: bool = False,
    internal_nodes_14: bool = False,
    internal_nodes_15: bool = False,
    internal_nodes_16: bool = False,
    internal_nodes_17: bool = False,
    internal_nodes_18: bool = False,
    internal_nodes_19: bool = False,
    tlrc: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> SurfaceMetricsOutputs:
    """
    Outputs information about a surface's mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surf1: Specifies the input surface.
        internal_nodes: Output nodes that are not a boundary.
        internal_nodes_: Output nodes that are not a boundary.
        internal_nodes_2: Output nodes that are not a boundary.
        internal_nodes_3: Output nodes that are not a boundary.
        internal_nodes_4: Output nodes that are not a boundary.
        internal_nodes_5: Output nodes that are not a boundary.
        internal_nodes_6: Output nodes that are not a boundary.
        internal_nodes_7: Output nodes that are not a boundary.
        internal_nodes_8: Output nodes that are not a boundary.
        internal_nodes_9: Output nodes that are not a boundary.
        internal_nodes_10: Output nodes that are not a boundary.
        internal_nodes_11: Output nodes that are not a boundary.
        internal_nodes_12: Output nodes that are not a boundary.
        internal_nodes_13: Output nodes that are not a boundary.
        internal_nodes_14: Output nodes that are not a boundary.
        internal_nodes_15: Output nodes that are not a boundary.
        internal_nodes_16: Output nodes that are not a boundary.
        internal_nodes_17: Output nodes that are not a boundary.
        internal_nodes_18: Output nodes that are not a boundary.
        internal_nodes_19: Output nodes that are not a boundary.
        tlrc: Apply Talairach transform to surface.
        prefix: Use prefix for output files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceMetricsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_METRICS_METADATA)
    params = surface_metrics_params(internal_nodes=internal_nodes, internal_nodes_=internal_nodes_, internal_nodes_2=internal_nodes_2, internal_nodes_3=internal_nodes_3, internal_nodes_4=internal_nodes_4, internal_nodes_5=internal_nodes_5, internal_nodes_6=internal_nodes_6, internal_nodes_7=internal_nodes_7, internal_nodes_8=internal_nodes_8, internal_nodes_9=internal_nodes_9, internal_nodes_10=internal_nodes_10, internal_nodes_11=internal_nodes_11, internal_nodes_12=internal_nodes_12, internal_nodes_13=internal_nodes_13, internal_nodes_14=internal_nodes_14, internal_nodes_15=internal_nodes_15, internal_nodes_16=internal_nodes_16, internal_nodes_17=internal_nodes_17, internal_nodes_18=internal_nodes_18, internal_nodes_19=internal_nodes_19, surf1=surf1, tlrc=tlrc, prefix=prefix)
    return surface_metrics_execute(params, execution)


__all__ = [
    "SURFACE_METRICS_METADATA",
    "surface_metrics",
    "surface_metrics_params",
]
