# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AFNI_CHECK_OMP_METADATA = Metadata(
    id="32dd1aee513bc5242efdf26e5514ec120679a8b1.boutiques",
    name="afni_check_omp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
AfniCheckOmpParameters = typing.TypedDict('AfniCheckOmpParameters', {
    "__STYX_TYPE__": typing.Literal["afni_check_omp"],
    "iterations": typing.NotRequired[float | None],
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
        "afni_check_omp": afni_check_omp_cargs,
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


class AfniCheckOmpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_check_omp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_check_omp_params(
    iterations: float | None = None,
) -> AfniCheckOmpParameters:
    """
    Build parameters.
    
    Args:
        iterations: Number of iterations to run.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "afni_check_omp",
    }
    if iterations is not None:
        params["iterations"] = iterations
    return params


def afni_check_omp_cargs(
    params: AfniCheckOmpParameters,
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
    cargs.append("afni_check_omp")
    if params.get("iterations") is not None:
        cargs.append(str(params.get("iterations")))
    return cargs


def afni_check_omp_outputs(
    params: AfniCheckOmpParameters,
    execution: Execution,
) -> AfniCheckOmpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AfniCheckOmpOutputs(
        root=execution.output_file("."),
    )
    return ret


def afni_check_omp_execute(
    params: AfniCheckOmpParameters,
    execution: Execution,
) -> AfniCheckOmpOutputs:
    """
    Tool to check the OpenMP multi-threading environment for AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AfniCheckOmpOutputs`).
    """
    params = execution.params(params)
    cargs = afni_check_omp_cargs(params, execution)
    ret = afni_check_omp_outputs(params, execution)
    execution.run(cargs)
    return ret


def afni_check_omp(
    iterations: float | None = None,
    runner: Runner | None = None,
) -> AfniCheckOmpOutputs:
    """
    Tool to check the OpenMP multi-threading environment for AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        iterations: Number of iterations to run.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniCheckOmpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_CHECK_OMP_METADATA)
    params = afni_check_omp_params(iterations=iterations)
    return afni_check_omp_execute(params, execution)


__all__ = [
    "AFNI_CHECK_OMP_METADATA",
    "AfniCheckOmpOutputs",
    "AfniCheckOmpParameters",
    "afni_check_omp",
    "afni_check_omp_params",
]
