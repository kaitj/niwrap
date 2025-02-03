# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ZTOP_METADATA = Metadata(
    id="aaa21f331bdaf4f959165aeb5f8d7c495a9d8f9d.boutiques",
    name="ztop",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ZtopParameters = typing.TypedDict('ZtopParameters', {
    "__STYX_TYPE__": typing.Literal["ztop"],
    "z_score": float,
    "tail_flag": bool,
    "grf_flag": bool,
    "number_of_resels": typing.NotRequired[float | None],
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
        "ztop": ztop_cargs,
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


def ztop_params(
    z_score: float,
    tail_flag: bool = False,
    grf_flag: bool = False,
    number_of_resels: float | None = None,
) -> ZtopParameters:
    """
    Build parameters.
    
    Args:
        z_score: Input z-score.
        tail_flag: Use 2-tailed conversion (default is 1-tailed).
        grf_flag: Use GRF maximum-height theory instead of Gaussian PDF.
        number_of_resels: Number of resels (resolution elements) for GRF\
            correction.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ztop",
        "z_score": z_score,
        "tail_flag": tail_flag,
        "grf_flag": grf_flag,
    }
    if number_of_resels is not None:
        params["number_of_resels"] = number_of_resels
    return params


def ztop_cargs(
    params: ZtopParameters,
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
    cargs.append("ztop")
    cargs.append(str(params.get("z_score")))
    if params.get("tail_flag"):
        cargs.append("-2")
    if params.get("grf_flag"):
        cargs.append("-g")
    if params.get("number_of_resels") is not None:
        cargs.append(str(params.get("number_of_resels")))
    return cargs


def ztop_outputs(
    params: ZtopParameters,
    execution: Execution,
) -> ZtopOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ZtopOutputs(
        root=execution.output_file("."),
    )
    return ret


def ztop_execute(
    params: ZtopParameters,
    execution: Execution,
) -> ZtopOutputs:
    """
    Converts a z-score to a p-value.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ZtopOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ztop_cargs(params, execution)
    ret = ztop_outputs(params, execution)
    execution.run(cargs)
    return ret


def ztop(
    z_score: float,
    tail_flag: bool = False,
    grf_flag: bool = False,
    number_of_resels: float | None = None,
    runner: Runner | None = None,
) -> ZtopOutputs:
    """
    Converts a z-score to a p-value.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        z_score: Input z-score.
        tail_flag: Use 2-tailed conversion (default is 1-tailed).
        grf_flag: Use GRF maximum-height theory instead of Gaussian PDF.
        number_of_resels: Number of resels (resolution elements) for GRF\
            correction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ZtopOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZTOP_METADATA)
    params = ztop_params(z_score=z_score, tail_flag=tail_flag, grf_flag=grf_flag, number_of_resels=number_of_resels)
    return ztop_execute(params, execution)


__all__ = [
    "ZTOP_METADATA",
    "ztop",
    "ztop_params",
]
