# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TTOZ_METADATA = Metadata(
    id="9988bec3a64455c5b76a5e959148ef7d7d9455c4.boutiques",
    name="ttoz",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
TtozParameters = typing.TypedDict('TtozParameters', {
    "__STYX_TYPE__": typing.Literal["ttoz"],
    "varsfile": InputPathType,
    "cbsfile": InputPathType,
    "dof": int,
    "outputvol": typing.NotRequired[str | None],
    "help_flag": bool,
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
        "ttoz": ttoz_cargs,
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
        "ttoz": ttoz_outputs,
    }
    return vt.get(t)


class TtozOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ttoz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_zvol: OutputPathType | None
    """Output Z-statistic volume"""


def ttoz_params(
    varsfile: InputPathType,
    cbsfile: InputPathType,
    dof: int,
    outputvol: str | None = None,
    help_flag: bool = False,
) -> TtozParameters:
    """
    Build parameters.
    
    Args:
        varsfile: Input variables file.
        cbsfile: Input CBS file.
        dof: Degrees of freedom.
        outputvol: Output volume name (default is zstats).
        help_flag: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ttoz",
        "varsfile": varsfile,
        "cbsfile": cbsfile,
        "dof": dof,
        "help_flag": help_flag,
    }
    if outputvol is not None:
        params["outputvol"] = outputvol
    return params


def ttoz_cargs(
    params: TtozParameters,
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
    cargs.append("ttoz")
    cargs.append(execution.input_file(params.get("varsfile")))
    cargs.append(execution.input_file(params.get("cbsfile")))
    cargs.append(str(params.get("dof")))
    if params.get("outputvol") is not None:
        cargs.extend([
            "-zout",
            params.get("outputvol")
        ])
    if params.get("help_flag"):
        cargs.append("-help")
    return cargs


def ttoz_outputs(
    params: TtozParameters,
    execution: Execution,
) -> TtozOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TtozOutputs(
        root=execution.output_file("."),
        output_zvol=execution.output_file(params.get("outputvol") + ".nii.gz") if (params.get("outputvol") is not None) else None,
    )
    return ret


def ttoz_execute(
    params: TtozParameters,
    execution: Execution,
) -> TtozOutputs:
    """
    Tool to convert a T-statistic image to a Z-statistic image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TtozOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ttoz_cargs(params, execution)
    ret = ttoz_outputs(params, execution)
    execution.run(cargs)
    return ret


def ttoz(
    varsfile: InputPathType,
    cbsfile: InputPathType,
    dof: int,
    outputvol: str | None = None,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> TtozOutputs:
    """
    Tool to convert a T-statistic image to a Z-statistic image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        varsfile: Input variables file.
        cbsfile: Input CBS file.
        dof: Degrees of freedom.
        outputvol: Output volume name (default is zstats).
        help_flag: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TtozOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TTOZ_METADATA)
    params = ttoz_params(varsfile=varsfile, cbsfile=cbsfile, dof=dof, outputvol=outputvol, help_flag=help_flag)
    return ttoz_execute(params, execution)


__all__ = [
    "TTOZ_METADATA",
    "TtozOutputs",
    "ttoz",
    "ttoz_params",
]
