# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DIMON_METADATA = Metadata(
    id="47141d28c3f7ccd9b2aa834d602f55feeab89023.boutiques",
    name="Dimon",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
DimonParameters = typing.TypedDict('DimonParameters', {
    "__STYX_TYPE__": typing.Literal["Dimon"],
    "infile_prefix": str,
    "infile_pattern": typing.NotRequired[str | None],
    "infile_list": typing.NotRequired[InputPathType | None],
    "rt_cmd": typing.NotRequired[str | None],
    "host": typing.NotRequired[str | None],
    "drive_afni": typing.NotRequired[str | None],
    "drive_wait": typing.NotRequired[str | None],
    "te_list": typing.NotRequired[str | None],
    "sort_method": typing.NotRequired[str | None],
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
        "Dimon": dimon_cargs,
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
        "Dimon": dimon_outputs,
    }.get(t)


class DimonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dimon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sorted_files: OutputPathType
    """Sorted input files with specified prefix"""
    sorted_files_details: OutputPathType | None
    """Details about sorted files"""


def dimon_params(
    infile_prefix: str,
    infile_pattern: str | None = None,
    infile_list: InputPathType | None = None,
    rt_cmd: str | None = None,
    host: str | None = None,
    drive_afni: str | None = None,
    drive_wait: str | None = None,
    te_list: str | None = None,
    sort_method: str | None = None,
) -> DimonParameters:
    """
    Build parameters.
    
    Args:
        infile_prefix: Prefix matching input files.
        infile_pattern: Pattern for input files.
        infile_list: List of filenames.
        rt_cmd: Send COMMAND(s) to realtime plugin.
        host: Specify the host for afni communication.
        drive_afni: Send 'drive afni' command, CMND.
        drive_wait: Send delayed 'drive afni' command, CMND.
        te_list: Specify a list of echo times.
        sort_method: Apply sorting method to image structures.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "Dimon",
        "infile_prefix": infile_prefix,
    }
    if infile_pattern is not None:
        params["infile_pattern"] = infile_pattern
    if infile_list is not None:
        params["infile_list"] = infile_list
    if rt_cmd is not None:
        params["rt_cmd"] = rt_cmd
    if host is not None:
        params["host"] = host
    if drive_afni is not None:
        params["drive_afni"] = drive_afni
    if drive_wait is not None:
        params["drive_wait"] = drive_wait
    if te_list is not None:
        params["te_list"] = te_list
    if sort_method is not None:
        params["sort_method"] = sort_method
    return params


def dimon_cargs(
    params: DimonParameters,
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
    cargs.append("Dimon")
    cargs.extend([
        "-infile_prefix",
        params.get("infile_prefix")
    ])
    if params.get("infile_pattern") is not None:
        cargs.extend([
            "-infile_pattern",
            params.get("infile_pattern")
        ])
    if params.get("infile_list") is not None:
        cargs.extend([
            "-infile_list",
            execution.input_file(params.get("infile_list"))
        ])
    if params.get("rt_cmd") is not None:
        cargs.extend([
            "-rt_cmd",
            params.get("rt_cmd")
        ])
    if params.get("host") is not None:
        cargs.extend([
            "-host",
            params.get("host")
        ])
    if params.get("drive_afni") is not None:
        cargs.extend([
            "-drive_afni",
            params.get("drive_afni")
        ])
    if params.get("drive_wait") is not None:
        cargs.extend([
            "-drive_wait",
            params.get("drive_wait")
        ])
    if params.get("te_list") is not None:
        cargs.extend([
            "-te_list",
            params.get("te_list")
        ])
    if params.get("sort_method") is not None:
        cargs.extend([
            "-sort_method",
            params.get("sort_method")
        ])
    return cargs


def dimon_outputs(
    params: DimonParameters,
    execution: Execution,
) -> DimonOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DimonOutputs(
        root=execution.output_file("."),
        sorted_files=execution.output_file(params.get("infile_prefix") + "*"),
        sorted_files_details=execution.output_file(pathlib.Path(params.get("infile_list")).name + "_details") if (params.get("infile_list") is not None) else None,
    )
    return ret


def dimon_execute(
    params: DimonParameters,
    execution: Execution,
) -> DimonOutputs:
    """
    Monitor real-time acquisition of DICOM image files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DimonOutputs`).
    """
    params = execution.params(params)
    cargs = dimon_cargs(params, execution)
    ret = dimon_outputs(params, execution)
    execution.run(cargs)
    return ret


def dimon(
    infile_prefix: str,
    infile_pattern: str | None = None,
    infile_list: InputPathType | None = None,
    rt_cmd: str | None = None,
    host: str | None = None,
    drive_afni: str | None = None,
    drive_wait: str | None = None,
    te_list: str | None = None,
    sort_method: str | None = None,
    runner: Runner | None = None,
) -> DimonOutputs:
    """
    Monitor real-time acquisition of DICOM image files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile_prefix: Prefix matching input files.
        infile_pattern: Pattern for input files.
        infile_list: List of filenames.
        rt_cmd: Send COMMAND(s) to realtime plugin.
        host: Specify the host for afni communication.
        drive_afni: Send 'drive afni' command, CMND.
        drive_wait: Send delayed 'drive afni' command, CMND.
        te_list: Specify a list of echo times.
        sort_method: Apply sorting method to image structures.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DimonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIMON_METADATA)
    params = dimon_params(infile_prefix=infile_prefix, infile_pattern=infile_pattern, infile_list=infile_list, rt_cmd=rt_cmd, host=host, drive_afni=drive_afni, drive_wait=drive_wait, te_list=te_list, sort_method=sort_method)
    return dimon_execute(params, execution)


__all__ = [
    "DIMON_METADATA",
    "DimonOutputs",
    "DimonParameters",
    "dimon",
    "dimon_params",
]
