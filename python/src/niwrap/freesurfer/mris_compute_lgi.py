# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_LGI_METADATA = Metadata(
    id="336847c2bd9448a616f5ba616c1806f2492345d6.boutiques",
    name="mris_compute_lgi",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisComputeLgiParameters = typing.TypedDict('MrisComputeLgiParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_lgi"],
    "input_surface": InputPathType,
    "close_sphere_size": typing.NotRequired[float | None],
    "smooth_iters": typing.NotRequired[float | None],
    "step_size": typing.NotRequired[float | None],
    "echo": bool,
    "dontrun": bool,
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
        "mris_compute_lgi": mris_compute_lgi_cargs,
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
        "mris_compute_lgi": mris_compute_lgi_outputs,
    }
    return vt.get(t)


class MrisComputeLgiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_lgi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface_map: OutputPathType
    """Surface map file containing local gyrification measures"""


def mris_compute_lgi_params(
    input_surface: InputPathType,
    close_sphere_size: float | None = None,
    smooth_iters: float | None = None,
    step_size: float | None = None,
    echo: bool = False,
    dontrun: bool = False,
) -> MrisComputeLgiParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file, typically lh.pial or rh.pial.
        close_sphere_size: Use sphere of specified size in mm for morph closing\
            operation (default: 15mm).
        smooth_iters: Smooth outer-surface specified number of iterations\
            (default: 30).
        step_size: Skip every specified number of vertices when computing lGI\
            (default: 100).
        echo: Enable command echo, for debug.
        dontrun: Just show commands (don't run them).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_lgi",
        "input_surface": input_surface,
        "echo": echo,
        "dontrun": dontrun,
    }
    if close_sphere_size is not None:
        params["close_sphere_size"] = close_sphere_size
    if smooth_iters is not None:
        params["smooth_iters"] = smooth_iters
    if step_size is not None:
        params["step_size"] = step_size
    return params


def mris_compute_lgi_cargs(
    params: MrisComputeLgiParameters,
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
    cargs.append("mris_compute_lgi")
    cargs.extend([
        "--i",
        execution.input_file(params.get("input_surface"))
    ])
    if params.get("close_sphere_size") is not None:
        cargs.extend([
            "--close_sphere_size",
            str(params.get("close_sphere_size"))
        ])
    if params.get("smooth_iters") is not None:
        cargs.extend([
            "--smooth_iters",
            str(params.get("smooth_iters"))
        ])
    if params.get("step_size") is not None:
        cargs.extend([
            "--step_size",
            str(params.get("step_size"))
        ])
    if params.get("echo"):
        cargs.append("--echo")
    if params.get("dontrun"):
        cargs.append("--dontrun")
    return cargs


def mris_compute_lgi_outputs(
    params: MrisComputeLgiParameters,
    execution: Execution,
) -> MrisComputeLgiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeLgiOutputs(
        root=execution.output_file("."),
        output_surface_map=execution.output_file(pathlib.Path(params.get("input_surface")).name + "_lgi"),
    )
    return ret


def mris_compute_lgi_execute(
    params: MrisComputeLgiParameters,
    execution: Execution,
) -> MrisComputeLgiOutputs:
    """
    Computes local measurements of gyrification at thousands of points over the
    entire cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeLgiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_compute_lgi_cargs(params, execution)
    ret = mris_compute_lgi_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_lgi(
    input_surface: InputPathType,
    close_sphere_size: float | None = None,
    smooth_iters: float | None = None,
    step_size: float | None = None,
    echo: bool = False,
    dontrun: bool = False,
    runner: Runner | None = None,
) -> MrisComputeLgiOutputs:
    """
    Computes local measurements of gyrification at thousands of points over the
    entire cortical surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file, typically lh.pial or rh.pial.
        close_sphere_size: Use sphere of specified size in mm for morph closing\
            operation (default: 15mm).
        smooth_iters: Smooth outer-surface specified number of iterations\
            (default: 30).
        step_size: Skip every specified number of vertices when computing lGI\
            (default: 100).
        echo: Enable command echo, for debug.
        dontrun: Just show commands (don't run them).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeLgiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_LGI_METADATA)
    params = mris_compute_lgi_params(input_surface=input_surface, close_sphere_size=close_sphere_size, smooth_iters=smooth_iters, step_size=step_size, echo=echo, dontrun=dontrun)
    return mris_compute_lgi_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_LGI_METADATA",
    "MrisComputeLgiOutputs",
    "mris_compute_lgi",
    "mris_compute_lgi_params",
]
