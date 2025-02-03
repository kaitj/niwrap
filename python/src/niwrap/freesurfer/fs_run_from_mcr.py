# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FS_RUN_FROM_MCR_METADATA = Metadata(
    id="cde2b930dda53cf7f6ac5ac2d3c81e82bcafc347.boutiques",
    name="fs_run_from_mcr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsRunFromMcrParameters = typing.TypedDict('FsRunFromMcrParameters', {
    "__STYX_TYPE__": typing.Literal["fs_run_from_mcr"],
    "name": typing.NotRequired[str | None],
    "command": typing.NotRequired[str | None],
    "zeroth_flag": bool,
    "empty_env_flag": bool,
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
        "fs_run_from_mcr": fs_run_from_mcr_cargs,
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


def fs_run_from_mcr_params(
    name: str | None = None,
    command: str | None = None,
    zeroth_flag: bool = False,
    empty_env_flag: bool = False,
) -> FsRunFromMcrParameters:
    """
    Build parameters.
    
    Args:
        name: Pass NAME as the zeroth argument to COMMAND.
        command: The command to execute.
        zeroth_flag: Place a dash in the zeroth argument to COMMAND.
        empty_env_flag: Execute COMMAND with an empty environment.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs_run_from_mcr",
        "zeroth_flag": zeroth_flag,
        "empty_env_flag": empty_env_flag,
    }
    if name is not None:
        params["name"] = name
    if command is not None:
        params["command"] = command
    return params


def fs_run_from_mcr_cargs(
    params: FsRunFromMcrParameters,
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
    cargs.append("fs_run_from_mcr")
    if params.get("name") is not None:
        cargs.extend([
            "-a",
            params.get("name")
        ])
    if params.get("command") is not None:
        cargs.append(params.get("command"))
    if params.get("zeroth_flag"):
        cargs.append("-l")
    if params.get("empty_env_flag"):
        cargs.append("-c")
    return cargs


def fs_run_from_mcr_outputs(
    params: FsRunFromMcrParameters,
    execution: Execution,
) -> FsRunFromMcrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsRunFromMcrOutputs(
        root=execution.output_file("."),
    )
    return ret


def fs_run_from_mcr_execute(
    params: FsRunFromMcrParameters,
    execution: Execution,
) -> FsRunFromMcrOutputs:
    """
    Replace the shell with the given command.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsRunFromMcrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fs_run_from_mcr_cargs(params, execution)
    ret = fs_run_from_mcr_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_run_from_mcr(
    name: str | None = None,
    command: str | None = None,
    zeroth_flag: bool = False,
    empty_env_flag: bool = False,
    runner: Runner | None = None,
) -> FsRunFromMcrOutputs:
    """
    Replace the shell with the given command.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        name: Pass NAME as the zeroth argument to COMMAND.
        command: The command to execute.
        zeroth_flag: Place a dash in the zeroth argument to COMMAND.
        empty_env_flag: Execute COMMAND with an empty environment.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsRunFromMcrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_RUN_FROM_MCR_METADATA)
    params = fs_run_from_mcr_params(name=name, command=command, zeroth_flag=zeroth_flag, empty_env_flag=empty_env_flag)
    return fs_run_from_mcr_execute(params, execution)


__all__ = [
    "FS_RUN_FROM_MCR_METADATA",
    "fs_run_from_mcr",
    "fs_run_from_mcr_params",
]
