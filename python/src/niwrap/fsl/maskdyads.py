# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MASKDYADS_METADATA = Metadata(
    id="7202ebf9fac4f093011a592184e5ec67cfb619d5.boutiques",
    name="maskdyads",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MaskdyadsParameters = typing.TypedDict('MaskdyadsParameters', {
    "__STYX_TYPE__": typing.Literal["maskdyads"],
    "dyads": InputPathType,
    "fsamples": InputPathType,
    "threshold": typing.NotRequired[float | None],
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
        "maskdyads": maskdyads_cargs,
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


def maskdyads_params(
    dyads: InputPathType,
    fsamples: InputPathType,
    threshold: float | None = 0.05,
) -> MaskdyadsParameters:
    """
    Build parameters.
    
    Args:
        dyads: Input dyads file.
        fsamples: Input fsamples file.
        threshold: Threshold (default is 0.05).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "maskdyads",
        "dyads": dyads,
        "fsamples": fsamples,
    }
    if threshold is not None:
        params["threshold"] = threshold
    return params


def maskdyads_cargs(
    params: MaskdyadsParameters,
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
    cargs.append("maskdyads")
    cargs.append(execution.input_file(params.get("dyads")))
    cargs.append(execution.input_file(params.get("fsamples")))
    if params.get("threshold") is not None:
        cargs.extend([
            "[THR]",
            str(params.get("threshold"))
        ])
    return cargs


def maskdyads_outputs(
    params: MaskdyadsParameters,
    execution: Execution,
) -> MaskdyadsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MaskdyadsOutputs(
        root=execution.output_file("."),
    )
    return ret


def maskdyads_execute(
    params: MaskdyadsParameters,
    execution: Execution,
) -> MaskdyadsOutputs:
    """
    Tool to mask dyads with threshold.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MaskdyadsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = maskdyads_cargs(params, execution)
    ret = maskdyads_outputs(params, execution)
    execution.run(cargs)
    return ret


def maskdyads(
    dyads: InputPathType,
    fsamples: InputPathType,
    threshold: float | None = 0.05,
    runner: Runner | None = None,
) -> MaskdyadsOutputs:
    """
    Tool to mask dyads with threshold.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        dyads: Input dyads file.
        fsamples: Input fsamples file.
        threshold: Threshold (default is 0.05).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MaskdyadsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MASKDYADS_METADATA)
    params = maskdyads_params(dyads=dyads, fsamples=fsamples, threshold=threshold)
    return maskdyads_execute(params, execution)


__all__ = [
    "MASKDYADS_METADATA",
    "maskdyads",
    "maskdyads_params",
]
