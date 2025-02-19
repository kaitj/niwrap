# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RCA_CONFIG_METADATA = Metadata(
    id="51c0aae9a34d0b770555399cc01f066ce00769c7.boutiques",
    name="rca-config",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
RcaConfigParameters = typing.TypedDict('RcaConfigParameters', {
    "__STYX_TYPE__": typing.Literal["rca-config"],
    "source_config": InputPathType,
    "updated_config": InputPathType,
    "unknown_args_file": InputPathType,
    "args": typing.NotRequired[list[str] | None],
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
        "rca-config": rca_config_cargs,
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


class RcaConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rca_config(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rca_config_params(
    source_config: InputPathType,
    updated_config: InputPathType,
    unknown_args_file: InputPathType,
    args: list[str] | None = None,
) -> RcaConfigParameters:
    """
    Build parameters.
    
    Args:
        source_config: Path to the source configuration file.
        updated_config: Path to the updated configuration file.
        unknown_args_file: Path to the file where unknown arguments are\
            recorded.
        args: Additional arguments to be processed.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "rca-config",
        "source_config": source_config,
        "updated_config": updated_config,
        "unknown_args_file": unknown_args_file,
    }
    if args is not None:
        params["args"] = args
    return params


def rca_config_cargs(
    params: RcaConfigParameters,
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
    cargs.extend([
        "-config",
        "recon" + execution.input_file(params.get("source_config"))
    ])
    cargs.append(execution.input_file(params.get("updated_config")))
    cargs.append(execution.input_file(params.get("unknown_args_file")))
    if params.get("args") is not None:
        cargs.extend(params.get("args"))
    return cargs


def rca_config_outputs(
    params: RcaConfigParameters,
    execution: Execution,
) -> RcaConfigOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RcaConfigOutputs(
        root=execution.output_file("."),
    )
    return ret


def rca_config_execute(
    params: RcaConfigParameters,
    execution: Execution,
) -> RcaConfigOutputs:
    """
    A command-line tool that processes configuration files and arguments.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RcaConfigOutputs`).
    """
    params = execution.params(params)
    cargs = rca_config_cargs(params, execution)
    ret = rca_config_outputs(params, execution)
    execution.run(cargs)
    return ret


def rca_config(
    source_config: InputPathType,
    updated_config: InputPathType,
    unknown_args_file: InputPathType,
    args: list[str] | None = None,
    runner: Runner | None = None,
) -> RcaConfigOutputs:
    """
    A command-line tool that processes configuration files and arguments.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_config: Path to the source configuration file.
        updated_config: Path to the updated configuration file.
        unknown_args_file: Path to the file where unknown arguments are\
            recorded.
        args: Additional arguments to be processed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RcaConfigOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RCA_CONFIG_METADATA)
    params = rca_config_params(source_config=source_config, updated_config=updated_config, unknown_args_file=unknown_args_file, args=args)
    return rca_config_execute(params, execution)


__all__ = [
    "RCA_CONFIG_METADATA",
    "RcaConfigOutputs",
    "RcaConfigParameters",
    "rca_config",
    "rca_config_params",
]
