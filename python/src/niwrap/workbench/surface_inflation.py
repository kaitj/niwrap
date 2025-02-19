# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_INFLATION_METADATA = Metadata(
    id="36f016a31d3d3dcd623e236f9e609fe3ad4ba0fe.boutiques",
    name="surface-inflation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceInflationParameters = typing.TypedDict('SurfaceInflationParameters', {
    "__STYX_TYPE__": typing.Literal["surface-inflation"],
    "anatomical_surface_in": InputPathType,
    "surface_in": InputPathType,
    "number_of_smoothing_cycles": int,
    "smoothing_strength": float,
    "smoothing_iterations": int,
    "inflation_factor": float,
    "surface_out": str,
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
        "surface-inflation": surface_inflation_cargs,
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
        "surface-inflation": surface_inflation_outputs,
    }.get(t)


class SurfaceInflationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_inflation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_inflation_params(
    anatomical_surface_in: InputPathType,
    surface_in: InputPathType,
    number_of_smoothing_cycles: int,
    smoothing_strength: float,
    smoothing_iterations: int,
    inflation_factor: float,
    surface_out: str,
) -> SurfaceInflationParameters:
    """
    Build parameters.
    
    Args:
        anatomical_surface_in: the anatomical surface.
        surface_in: the surface file to inflate.
        number_of_smoothing_cycles: number of smoothing cycles.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        inflation_factor: inflation factor.
        surface_out: output surface file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-inflation",
        "anatomical_surface_in": anatomical_surface_in,
        "surface_in": surface_in,
        "number_of_smoothing_cycles": number_of_smoothing_cycles,
        "smoothing_strength": smoothing_strength,
        "smoothing_iterations": smoothing_iterations,
        "inflation_factor": inflation_factor,
        "surface_out": surface_out,
    }
    return params


def surface_inflation_cargs(
    params: SurfaceInflationParameters,
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
    cargs.append("-surface-inflation")
    cargs.append(execution.input_file(params.get("anatomical_surface_in")))
    cargs.append(execution.input_file(params.get("surface_in")))
    cargs.append(str(params.get("number_of_smoothing_cycles")))
    cargs.append(str(params.get("smoothing_strength")))
    cargs.append(str(params.get("smoothing_iterations")))
    cargs.append(str(params.get("inflation_factor")))
    cargs.append(params.get("surface_out"))
    return cargs


def surface_inflation_outputs(
    params: SurfaceInflationParameters,
    execution: Execution,
) -> SurfaceInflationOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceInflationOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(params.get("surface_out")),
    )
    return ret


def surface_inflation_execute(
    params: SurfaceInflationParameters,
    execution: Execution,
) -> SurfaceInflationOutputs:
    """
    Surface inflation.
    
    Inflate a surface by performing cycles that consist of smoothing followed by
    inflation (to correct shrinkage caused by smoothing).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceInflationOutputs`).
    """
    params = execution.params(params)
    cargs = surface_inflation_cargs(params, execution)
    ret = surface_inflation_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_inflation(
    anatomical_surface_in: InputPathType,
    surface_in: InputPathType,
    number_of_smoothing_cycles: int,
    smoothing_strength: float,
    smoothing_iterations: int,
    inflation_factor: float,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceInflationOutputs:
    """
    Surface inflation.
    
    Inflate a surface by performing cycles that consist of smoothing followed by
    inflation (to correct shrinkage caused by smoothing).
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        anatomical_surface_in: the anatomical surface.
        surface_in: the surface file to inflate.
        number_of_smoothing_cycles: number of smoothing cycles.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        inflation_factor: inflation factor.
        surface_out: output surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceInflationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_INFLATION_METADATA)
    params = surface_inflation_params(anatomical_surface_in=anatomical_surface_in, surface_in=surface_in, number_of_smoothing_cycles=number_of_smoothing_cycles, smoothing_strength=smoothing_strength, smoothing_iterations=smoothing_iterations, inflation_factor=inflation_factor, surface_out=surface_out)
    return surface_inflation_execute(params, execution)


__all__ = [
    "SURFACE_INFLATION_METADATA",
    "SurfaceInflationOutputs",
    "SurfaceInflationParameters",
    "surface_inflation",
    "surface_inflation_params",
]
