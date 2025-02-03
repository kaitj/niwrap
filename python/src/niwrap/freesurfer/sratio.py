# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SRATIO_METADATA = Metadata(
    id="b9e1c106ac7eb065c902d7e719b87ca6cd2c12c5.boutiques",
    name="sratio",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SratioParameters = typing.TypedDict('SratioParameters', {
    "__STYX_TYPE__": typing.Literal["sratio"],
    "value_a": float,
    "value_b": float,
    "abs_flag": bool,
    "mask_threshold": typing.NotRequired[float | None],
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
        "sratio": sratio_cargs,
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
        "sratio": sratio_outputs,
    }
    return vt.get(t)


class SratioOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sratio(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sratio_result: OutputPathType
    """Result of the sratio operation"""


def sratio_params(
    value_a: float,
    value_b: float,
    abs_flag: bool = False,
    mask_threshold: float | None = None,
) -> SratioParameters:
    """
    Build parameters.
    
    Args:
        value_a: First value for the sratio operation.
        value_b: Second value for the sratio operation.
        abs_flag: Compute absolute value of both A and B before sratio.
        mask_threshold: Threshold based on max(abs(A),abs(B)) > thresh.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sratio",
        "value_a": value_a,
        "value_b": value_b,
        "abs_flag": abs_flag,
    }
    if mask_threshold is not None:
        params["mask_threshold"] = mask_threshold
    return params


def sratio_cargs(
    params: SratioParameters,
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
    cargs.append("sratio")
    cargs.append(str(params.get("value_a")))
    cargs.append(str(params.get("value_b")))
    if params.get("abs_flag"):
        cargs.append("--abs")
    if params.get("mask_threshold") is not None:
        cargs.extend([
            "--mask-thresh",
            str(params.get("mask_threshold"))
        ])
    return cargs


def sratio_outputs(
    params: SratioParameters,
    execution: Execution,
) -> SratioOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SratioOutputs(
        root=execution.output_file("."),
        sratio_result=execution.output_file("[SRATIO_RESULT]"),
    )
    return ret


def sratio_execute(
    params: SratioParameters,
    execution: Execution,
) -> SratioOutputs:
    """
    Tool to compute ratio A/B if A>B, -B/A if B>A, with options for absolute
    computation and threshold masking.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SratioOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sratio_cargs(params, execution)
    ret = sratio_outputs(params, execution)
    execution.run(cargs)
    return ret


def sratio(
    value_a: float,
    value_b: float,
    abs_flag: bool = False,
    mask_threshold: float | None = None,
    runner: Runner | None = None,
) -> SratioOutputs:
    """
    Tool to compute ratio A/B if A>B, -B/A if B>A, with options for absolute
    computation and threshold masking.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        value_a: First value for the sratio operation.
        value_b: Second value for the sratio operation.
        abs_flag: Compute absolute value of both A and B before sratio.
        mask_threshold: Threshold based on max(abs(A),abs(B)) > thresh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SratioOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SRATIO_METADATA)
    params = sratio_params(value_a=value_a, value_b=value_b, abs_flag=abs_flag, mask_threshold=mask_threshold)
    return sratio_execute(params, execution)


__all__ = [
    "SRATIO_METADATA",
    "SratioOutputs",
    "sratio",
    "sratio_params",
]
