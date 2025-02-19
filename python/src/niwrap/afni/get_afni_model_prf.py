# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GET_AFNI_MODEL_PRF_METADATA = Metadata(
    id="cb7d3b9ba2d4dd13509959e5b0788f67b7ac9d2f.boutiques",
    name="get_afni_model_PRF",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
GetAfniModelPrfParameters = typing.TypedDict('GetAfniModelPrfParameters', {
    "__STYX_TYPE__": typing.Literal["get_afni_model_PRF"],
    "amplitude": float,
    "x_coord": float,
    "y_coord": float,
    "sigma": float,
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
        "get_afni_model_PRF": get_afni_model_prf_cargs,
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
    }.get(t)


class GetAfniModelPrfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_afni_model_prf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def get_afni_model_prf_params(
    amplitude: float,
    x_coord: float,
    y_coord: float,
    sigma: float,
) -> GetAfniModelPrfParameters:
    """
    Build parameters.
    
    Args:
        amplitude: Amplitude for the AFNI model.
        x_coord: X-coordinate for the AFNI model.
        y_coord: Y-coordinate for the AFNI model.
        sigma: Sigma value for the AFNI model.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "get_afni_model_PRF",
        "amplitude": amplitude,
        "x_coord": x_coord,
        "y_coord": y_coord,
        "sigma": sigma,
    }
    return params


def get_afni_model_prf_cargs(
    params: GetAfniModelPrfParameters,
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
    cargs.append("get_afni_model_PRF")
    cargs.append(str(params.get("amplitude")))
    cargs.append(str(params.get("x_coord")))
    cargs.append(str(params.get("y_coord")))
    cargs.append(str(params.get("sigma")))
    return cargs


def get_afni_model_prf_outputs(
    params: GetAfniModelPrfParameters,
    execution: Execution,
) -> GetAfniModelPrfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GetAfniModelPrfOutputs(
        root=execution.output_file("."),
    )
    return ret


def get_afni_model_prf_execute(
    params: GetAfniModelPrfParameters,
    execution: Execution,
) -> GetAfniModelPrfOutputs:
    """
    A tool to get AFNI model parameters assuming a PRF framework.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrfOutputs`).
    """
    params = execution.params(params)
    cargs = get_afni_model_prf_cargs(params, execution)
    ret = get_afni_model_prf_outputs(params, execution)
    execution.run(cargs)
    return ret


def get_afni_model_prf(
    amplitude: float,
    x_coord: float,
    y_coord: float,
    sigma: float,
    runner: Runner | None = None,
) -> GetAfniModelPrfOutputs:
    """
    A tool to get AFNI model parameters assuming a PRF framework.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        amplitude: Amplitude for the AFNI model.
        x_coord: X-coordinate for the AFNI model.
        y_coord: Y-coordinate for the AFNI model.
        sigma: Sigma value for the AFNI model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniModelPrfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_AFNI_MODEL_PRF_METADATA)
    params = get_afni_model_prf_params(amplitude=amplitude, x_coord=x_coord, y_coord=y_coord, sigma=sigma)
    return get_afni_model_prf_execute(params, execution)


__all__ = [
    "GET_AFNI_MODEL_PRF_METADATA",
    "GetAfniModelPrfOutputs",
    "GetAfniModelPrfParameters",
    "get_afni_model_prf",
    "get_afni_model_prf_params",
]
