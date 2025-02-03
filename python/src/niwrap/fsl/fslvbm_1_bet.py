# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLVBM_1_BET_METADATA = Metadata(
    id="b14f656e797f3613fc30f4f42a5942f8c36bc438.boutiques",
    name="fslvbm_1_bet",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Fslvbm1BetParameters = typing.TypedDict('Fslvbm1BetParameters', {
    "__STYX_TYPE__": typing.Literal["fslvbm_1_bet"],
    "increased_robustness": bool,
    "bet_parameters": typing.NotRequired[str | None],
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
        "fslvbm_1_bet": fslvbm_1_bet_cargs,
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


def fslvbm_1_bet_params(
    increased_robustness: bool = False,
    bet_parameters: str | None = None,
) -> Fslvbm1BetParameters:
    """
    Build parameters.
    
    Args:
        increased_robustness: Increased robustness in the brain extraction when\
            a lot of neck is present.
        bet_parameters: Additional options to be passed on to BET.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslvbm_1_bet",
        "increased_robustness": increased_robustness,
    }
    if bet_parameters is not None:
        params["bet_parameters"] = bet_parameters
    return params


def fslvbm_1_bet_cargs(
    params: Fslvbm1BetParameters,
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
    cargs.append("fslvbm_1_bet")
    if params.get("increased_robustness"):
        cargs.append("-N")
    if params.get("bet_parameters") is not None:
        cargs.append(params.get("bet_parameters"))
    return cargs


def fslvbm_1_bet_outputs(
    params: Fslvbm1BetParameters,
    execution: Execution,
) -> Fslvbm1BetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fslvbm1BetOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslvbm_1_bet_execute(
    params: Fslvbm1BetParameters,
    execution: Execution,
) -> Fslvbm1BetOutputs:
    """
    Brain extraction for VBM using FSL BET.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fslvbm1BetOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslvbm_1_bet_cargs(params, execution)
    ret = fslvbm_1_bet_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslvbm_1_bet(
    increased_robustness: bool = False,
    bet_parameters: str | None = None,
    runner: Runner | None = None,
) -> Fslvbm1BetOutputs:
    """
    Brain extraction for VBM using FSL BET.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        increased_robustness: Increased robustness in the brain extraction when\
            a lot of neck is present.
        bet_parameters: Additional options to be passed on to BET.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm1BetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVBM_1_BET_METADATA)
    params = fslvbm_1_bet_params(increased_robustness=increased_robustness, bet_parameters=bet_parameters)
    return fslvbm_1_bet_execute(params, execution)


__all__ = [
    "FSLVBM_1_BET_METADATA",
    "fslvbm_1_bet",
    "fslvbm_1_bet_params",
]
