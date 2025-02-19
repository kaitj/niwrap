# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PLUGOUT_DRIVE_METADATA = Metadata(
    id="65a44f6f7d92c1ad9ba4ed1d48f6c277a7f935fb.boutiques",
    name="plugout_drive",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
PlugoutDriveParameters = typing.TypedDict('PlugoutDriveParameters', {
    "__STYX_TYPE__": typing.Literal["plugout_drive"],
    "host": typing.NotRequired[str | None],
    "verbose": bool,
    "port": typing.NotRequired[float | None],
    "maxwait": typing.NotRequired[float | None],
    "name": typing.NotRequired[str | None],
    "command": typing.NotRequired[list[str] | None],
    "quit": bool,
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
        "plugout_drive": plugout_drive_cargs,
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


class PlugoutDriveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `plugout_drive(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def plugout_drive_params(
    host: str | None = None,
    verbose: bool = False,
    port: float | None = None,
    maxwait: float | None = None,
    name: str | None = None,
    command: list[str] | None = None,
    quit_: bool = False,
) -> PlugoutDriveParameters:
    """
    Build parameters.
    
    Args:
        host: Connect to AFNI running on the specified host using TCP/IP.\
            Default is 'localhost'.
        verbose: Verbose mode.
        port: Use TCP/IP port number. Default is 8099.
        maxwait: Maximum wait time in seconds for AFNI to connect. Default is 9\
            seconds.
        name: Name that AFNI assigns to this plugout. Default is a pre-defined\
            name.
        command: Command to be executed on AFNI. Example: '-com "SET_FUNCTION\
            SomeFunction"'.
        quit_: Quit after executing all -com commands. Default is to wait for\
            more commands.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "plugout_drive",
        "verbose": verbose,
        "quit": quit_,
    }
    if host is not None:
        params["host"] = host
    if port is not None:
        params["port"] = port
    if maxwait is not None:
        params["maxwait"] = maxwait
    if name is not None:
        params["name"] = name
    if command is not None:
        params["command"] = command
    return params


def plugout_drive_cargs(
    params: PlugoutDriveParameters,
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
    cargs.append("plugout_drive")
    if params.get("host") is not None:
        cargs.extend([
            "-host",
            params.get("host")
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("port") is not None:
        cargs.extend([
            "-port",
            str(params.get("port"))
        ])
    if params.get("maxwait") is not None:
        cargs.extend([
            "-maxwait",
            str(params.get("maxwait"))
        ])
    if params.get("name") is not None:
        cargs.extend([
            "-name",
            params.get("name")
        ])
    if params.get("command") is not None:
        cargs.extend([
            "-com",
            *params.get("command")
        ])
    if params.get("quit"):
        cargs.append("-quit")
    return cargs


def plugout_drive_outputs(
    params: PlugoutDriveParameters,
    execution: Execution,
) -> PlugoutDriveOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PlugoutDriveOutputs(
        root=execution.output_file("."),
    )
    return ret


def plugout_drive_execute(
    params: PlugoutDriveParameters,
    execution: Execution,
) -> PlugoutDriveOutputs:
    """
    This program connects to AFNI and sends commands that the user specifies
    interactively or on command line over to AFNI to be executed.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PlugoutDriveOutputs`).
    """
    params = execution.params(params)
    cargs = plugout_drive_cargs(params, execution)
    ret = plugout_drive_outputs(params, execution)
    execution.run(cargs)
    return ret


def plugout_drive(
    host: str | None = None,
    verbose: bool = False,
    port: float | None = None,
    maxwait: float | None = None,
    name: str | None = None,
    command: list[str] | None = None,
    quit_: bool = False,
    runner: Runner | None = None,
) -> PlugoutDriveOutputs:
    """
    This program connects to AFNI and sends commands that the user specifies
    interactively or on command line over to AFNI to be executed.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        host: Connect to AFNI running on the specified host using TCP/IP.\
            Default is 'localhost'.
        verbose: Verbose mode.
        port: Use TCP/IP port number. Default is 8099.
        maxwait: Maximum wait time in seconds for AFNI to connect. Default is 9\
            seconds.
        name: Name that AFNI assigns to this plugout. Default is a pre-defined\
            name.
        command: Command to be executed on AFNI. Example: '-com "SET_FUNCTION\
            SomeFunction"'.
        quit_: Quit after executing all -com commands. Default is to wait for\
            more commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PlugoutDriveOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PLUGOUT_DRIVE_METADATA)
    params = plugout_drive_params(host=host, verbose=verbose, port=port, maxwait=maxwait, name=name, command=command, quit_=quit_)
    return plugout_drive_execute(params, execution)


__all__ = [
    "PLUGOUT_DRIVE_METADATA",
    "PlugoutDriveOutputs",
    "PlugoutDriveParameters",
    "plugout_drive",
    "plugout_drive_params",
]
