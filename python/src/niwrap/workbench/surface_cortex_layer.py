# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_CORTEX_LAYER_METADATA = Metadata(
    id="1fb2598f6c40246e1cd4406b005c1caba798780a.boutiques",
    name="surface-cortex-layer",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceCortexLayerParameters = typing.TypedDict('SurfaceCortexLayerParameters', {
    "__STYX_TYPE__": typing.Literal["surface-cortex-layer"],
    "white_surface": InputPathType,
    "pial_surface": InputPathType,
    "location": float,
    "out_surface": str,
    "opt_placement_out_placement_metric": typing.NotRequired[str | None],
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
        "surface-cortex-layer": surface_cortex_layer_cargs,
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
        "surface-cortex-layer": surface_cortex_layer_outputs,
    }
    return vt.get(t)


class SurfaceCortexLayerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_cortex_layer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surface: OutputPathType
    """the output surface"""
    opt_placement_out_placement_metric: OutputPathType | None
    """output the placement as a volume fraction from pial to white: output
    metric"""


def surface_cortex_layer_params(
    white_surface: InputPathType,
    pial_surface: InputPathType,
    location: float,
    out_surface: str,
    opt_placement_out_placement_metric: str | None = None,
) -> SurfaceCortexLayerParameters:
    """
    Build parameters.
    
    Args:
        white_surface: the white matter surface.
        pial_surface: the pial surface.
        location: what volume fraction to place the layer at.
        out_surface: the output surface.
        opt_placement_out_placement_metric: output the placement as a volume\
            fraction from pial to white: output metric.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-cortex-layer",
        "white_surface": white_surface,
        "pial_surface": pial_surface,
        "location": location,
        "out_surface": out_surface,
    }
    if opt_placement_out_placement_metric is not None:
        params["opt_placement_out_placement_metric"] = opt_placement_out_placement_metric
    return params


def surface_cortex_layer_cargs(
    params: SurfaceCortexLayerParameters,
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
    cargs.append("-surface-cortex-layer")
    cargs.append(execution.input_file(params.get("white_surface")))
    cargs.append(execution.input_file(params.get("pial_surface")))
    cargs.append(str(params.get("location")))
    cargs.append(params.get("out_surface"))
    if params.get("opt_placement_out_placement_metric") is not None:
        cargs.extend([
            "-placement-out",
            params.get("opt_placement_out_placement_metric")
        ])
    return cargs


def surface_cortex_layer_outputs(
    params: SurfaceCortexLayerParameters,
    execution: Execution,
) -> SurfaceCortexLayerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceCortexLayerOutputs(
        root=execution.output_file("."),
        out_surface=execution.output_file(params.get("out_surface")),
        opt_placement_out_placement_metric=execution.output_file(params.get("opt_placement_out_placement_metric")) if (params.get("opt_placement_out_placement_metric") is not None) else None,
    )
    return ret


def surface_cortex_layer_execute(
    params: SurfaceCortexLayerParameters,
    execution: Execution,
) -> SurfaceCortexLayerOutputs:
    """
    Create surface approximating a cortical layer.
    
    The input surfaces must have vertex correspondence. The output surface is
    generated by placing vertices between the two surfaces such that the
    enclosed volume within any small patch of the new and white surfaces is the
    given fraction of the volume of the same patch between the pial and white
    surfaces (i.e., specifying 0 would give the white surface, 1 would give the
    pial surface). .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceCortexLayerOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_cortex_layer_cargs(params, execution)
    ret = surface_cortex_layer_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_cortex_layer(
    white_surface: InputPathType,
    pial_surface: InputPathType,
    location: float,
    out_surface: str,
    opt_placement_out_placement_metric: str | None = None,
    runner: Runner | None = None,
) -> SurfaceCortexLayerOutputs:
    """
    Create surface approximating a cortical layer.
    
    The input surfaces must have vertex correspondence. The output surface is
    generated by placing vertices between the two surfaces such that the
    enclosed volume within any small patch of the new and white surfaces is the
    given fraction of the volume of the same patch between the pial and white
    surfaces (i.e., specifying 0 would give the white surface, 1 would give the
    pial surface). .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        white_surface: the white matter surface.
        pial_surface: the pial surface.
        location: what volume fraction to place the layer at.
        out_surface: the output surface.
        opt_placement_out_placement_metric: output the placement as a volume\
            fraction from pial to white: output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCortexLayerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CORTEX_LAYER_METADATA)
    params = surface_cortex_layer_params(white_surface=white_surface, pial_surface=pial_surface, location=location, out_surface=out_surface, opt_placement_out_placement_metric=opt_placement_out_placement_metric)
    return surface_cortex_layer_execute(params, execution)


__all__ = [
    "SURFACE_CORTEX_LAYER_METADATA",
    "SurfaceCortexLayerOutputs",
    "surface_cortex_layer",
    "surface_cortex_layer_params",
]
