# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIENA_FLOW2STD_METADATA = Metadata(
    id="d8e526a5d3b8a1c0f3fbe998ccfb5fd249f84b74.boutiques",
    name="siena_flow2std",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SienaFlow2stdParameters = typing.TypedDict('SienaFlow2stdParameters', {
    "__STYX_TYPE__": typing.Literal["siena_flow2std"],
    "fileroot1": str,
    "fileroot2": str,
    "sigma": typing.NotRequired[float | None],
    "debug_flag": bool,
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
        "siena_flow2std": siena_flow2std_cargs,
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


def siena_flow2std_params(
    fileroot1: str,
    fileroot2: str,
    sigma: float | None = 5,
    debug_flag: bool = False,
) -> SienaFlow2stdParameters:
    """
    Build parameters.
    
    Args:
        fileroot1: Input file root 1.
        fileroot2: Input file root 2.
        sigma: Spatial smoothing of standard-space edge-flow image, sigma\
            (HWHM) in mm (default=5).
        debug_flag: Debug (don't delete intermediate files).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "siena_flow2std",
        "fileroot1": fileroot1,
        "fileroot2": fileroot2,
        "debug_flag": debug_flag,
    }
    if sigma is not None:
        params["sigma"] = sigma
    return params


def siena_flow2std_cargs(
    params: SienaFlow2stdParameters,
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
    cargs.append("siena_flow2std")
    cargs.append(params.get("fileroot1"))
    cargs.append(params.get("fileroot2"))
    if params.get("sigma") is not None:
        cargs.extend([
            "-s",
            str(params.get("sigma"))
        ])
    if params.get("debug_flag"):
        cargs.append("-d")
    return cargs


def siena_flow2std_outputs(
    params: SienaFlow2stdParameters,
    execution: Execution,
) -> SienaFlow2stdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SienaFlow2stdOutputs(
        root=execution.output_file("."),
    )
    return ret


def siena_flow2std_execute(
    params: SienaFlow2stdParameters,
    execution: Execution,
) -> SienaFlow2stdOutputs:
    """
    Convert edge flow to standard space.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SienaFlow2stdOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = siena_flow2std_cargs(params, execution)
    ret = siena_flow2std_outputs(params, execution)
    execution.run(cargs)
    return ret


def siena_flow2std(
    fileroot1: str,
    fileroot2: str,
    sigma: float | None = 5,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> SienaFlow2stdOutputs:
    """
    Convert edge flow to standard space.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        fileroot1: Input file root 1.
        fileroot2: Input file root 2.
        sigma: Spatial smoothing of standard-space edge-flow image, sigma\
            (HWHM) in mm (default=5).
        debug_flag: Debug (don't delete intermediate files).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaFlow2stdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_FLOW2STD_METADATA)
    params = siena_flow2std_params(fileroot1=fileroot1, fileroot2=fileroot2, sigma=sigma, debug_flag=debug_flag)
    return siena_flow2std_execute(params, execution)


__all__ = [
    "SIENA_FLOW2STD_METADATA",
    "siena_flow2std",
    "siena_flow2std_params",
]
