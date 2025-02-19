# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TKREGISTER2_METADATA = Metadata(
    id="5b91df2c41f022fb3500d5826ced751292eade8d.boutiques",
    name="tkregister2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Tkregister2Parameters = typing.TypedDict('Tkregister2Parameters', {
    "__STYX_TYPE__": typing.Literal["tkregister2"],
    "fixed_volume": InputPathType,
    "moving_volume": InputPathType,
    "reg_file": InputPathType,
    "noedit": bool,
    "lta": bool,
    "surf_reg": bool,
    "reg_only": bool,
    "help": bool,
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
        "tkregister2": tkregister2_cargs,
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
        "tkregister2": tkregister2_outputs,
    }.get(t)


class Tkregister2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `tkregister2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_reg_file: OutputPathType
    """Resulting registration file"""


def tkregister2_params(
    fixed_volume: InputPathType,
    moving_volume: InputPathType,
    reg_file: InputPathType,
    noedit: bool = False,
    lta: bool = False,
    surf_reg: bool = False,
    reg_only: bool = False,
    help_: bool = False,
) -> Tkregister2Parameters:
    """
    Build parameters.
    
    Args:
        fixed_volume: Fixed volume (e.g., anatomical image).
        moving_volume: Moving volume (e.g., functional image).
        reg_file: Registration file to be saved or loaded.
        noedit: Run in no-edit mode, useful for scripting.
        lta: Use LTA format for registration file.
        surf_reg: Use surface registration.
        reg_only: Don't show GUI, just save registration.
        help_: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tkregister2",
        "fixed_volume": fixed_volume,
        "moving_volume": moving_volume,
        "reg_file": reg_file,
        "noedit": noedit,
        "lta": lta,
        "surf_reg": surf_reg,
        "reg_only": reg_only,
        "help": help_,
    }
    return params


def tkregister2_cargs(
    params: Tkregister2Parameters,
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
    cargs.append("tkregister2")
    cargs.append(execution.input_file(params.get("fixed_volume")))
    cargs.append(execution.input_file(params.get("moving_volume")))
    cargs.append(execution.input_file(params.get("reg_file")))
    if params.get("noedit"):
        cargs.append("--noedit")
    if params.get("lta"):
        cargs.append("--lta")
    if params.get("surf_reg"):
        cargs.append("--surf")
    if params.get("reg_only"):
        cargs.append("--regonly")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def tkregister2_outputs(
    params: Tkregister2Parameters,
    execution: Execution,
) -> Tkregister2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tkregister2Outputs(
        root=execution.output_file("."),
        output_reg_file=execution.output_file(pathlib.Path(params.get("reg_file")).name),
    )
    return ret


def tkregister2_execute(
    params: Tkregister2Parameters,
    execution: Execution,
) -> Tkregister2Outputs:
    """
    tkregister2 is a tool from FreeSurfer used for registration of MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tkregister2Outputs`).
    """
    params = execution.params(params)
    cargs = tkregister2_cargs(params, execution)
    ret = tkregister2_outputs(params, execution)
    execution.run(cargs)
    return ret


def tkregister2(
    fixed_volume: InputPathType,
    moving_volume: InputPathType,
    reg_file: InputPathType,
    noedit: bool = False,
    lta: bool = False,
    surf_reg: bool = False,
    reg_only: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> Tkregister2Outputs:
    """
    tkregister2 is a tool from FreeSurfer used for registration of MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        fixed_volume: Fixed volume (e.g., anatomical image).
        moving_volume: Moving volume (e.g., functional image).
        reg_file: Registration file to be saved or loaded.
        noedit: Run in no-edit mode, useful for scripting.
        lta: Use LTA format for registration file.
        surf_reg: Use surface registration.
        reg_only: Don't show GUI, just save registration.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tkregister2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKREGISTER2_METADATA)
    params = tkregister2_params(fixed_volume=fixed_volume, moving_volume=moving_volume, reg_file=reg_file, noedit=noedit, lta=lta, surf_reg=surf_reg, reg_only=reg_only, help_=help_)
    return tkregister2_execute(params, execution)


__all__ = [
    "TKREGISTER2_METADATA",
    "Tkregister2Outputs",
    "Tkregister2Parameters",
    "tkregister2",
    "tkregister2_params",
]
