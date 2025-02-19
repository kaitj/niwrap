# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_PRETESS_METADATA = Metadata(
    id="4499558e540b531e057123dc0bdd2efbb168c515.boutiques",
    name="mri_pretess",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriPretessParameters = typing.TypedDict('MriPretessParameters', {
    "__STYX_TYPE__": typing.Literal["mri_pretess"],
    "filledvol": InputPathType,
    "labelstring": str,
    "normvol": InputPathType,
    "newfilledvol": str,
    "debug_voxel": typing.NotRequired[list[float] | None],
    "nocorners": bool,
    "write": bool,
    "keep": bool,
    "test": bool,
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
        "mri_pretess": mri_pretess_cargs,
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
        "mri_pretess": mri_pretess_outputs,
    }.get(t)


class MriPretessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_pretess(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_newfilledvol: OutputPathType
    """Output new filled volume"""


def mri_pretess_params(
    filledvol: InputPathType,
    labelstring: str,
    normvol: InputPathType,
    newfilledvol: str,
    debug_voxel: list[float] | None = None,
    nocorners: bool = False,
    write: bool = False,
    keep: bool = False,
    test: bool = False,
) -> MriPretessParameters:
    """
    Build parameters.
    
    Args:
        filledvol: Input filled volume, usually wm.mgz.
        labelstring: Label string, usually wm.
        normvol: Normalization volume, usually norm.mgz.
        newfilledvol: New filled volume output, usually wm.mgz.
        debug_voxel: Specify the voxel to debug with coordinates C R S.
        nocorners: No removal of corner configurations in addition to edge ones.
        write: Turn on diagnostic writing.
        keep: Keep WM edits.
        test: Adds a voxel to test removal by mri_pretess, retained with -keep.\
            Output not saved.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_pretess",
        "filledvol": filledvol,
        "labelstring": labelstring,
        "normvol": normvol,
        "newfilledvol": newfilledvol,
        "nocorners": nocorners,
        "write": write,
        "keep": keep,
        "test": test,
    }
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    return params


def mri_pretess_cargs(
    params: MriPretessParameters,
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
    cargs.append("mri_pretess")
    cargs.append(execution.input_file(params.get("filledvol")))
    cargs.append(params.get("labelstring"))
    cargs.append(execution.input_file(params.get("normvol")))
    cargs.append(params.get("newfilledvol"))
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    if params.get("nocorners"):
        cargs.append("-nocorners")
    if params.get("write"):
        cargs.append("-w")
    if params.get("keep"):
        cargs.append("-keep")
    if params.get("test"):
        cargs.append("-test")
    return cargs


def mri_pretess_outputs(
    params: MriPretessParameters,
    execution: Execution,
) -> MriPretessOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriPretessOutputs(
        root=execution.output_file("."),
        out_newfilledvol=execution.output_file(params.get("newfilledvol")),
    )
    return ret


def mri_pretess_execute(
    params: MriPretessParameters,
    execution: Execution,
) -> MriPretessOutputs:
    """
    Tool to modify WM segmentation so that all neighbors of WM voxels have a common
    face.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriPretessOutputs`).
    """
    params = execution.params(params)
    cargs = mri_pretess_cargs(params, execution)
    ret = mri_pretess_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_pretess(
    filledvol: InputPathType,
    labelstring: str,
    normvol: InputPathType,
    newfilledvol: str,
    debug_voxel: list[float] | None = None,
    nocorners: bool = False,
    write: bool = False,
    keep: bool = False,
    test: bool = False,
    runner: Runner | None = None,
) -> MriPretessOutputs:
    """
    Tool to modify WM segmentation so that all neighbors of WM voxels have a common
    face.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        filledvol: Input filled volume, usually wm.mgz.
        labelstring: Label string, usually wm.
        normvol: Normalization volume, usually norm.mgz.
        newfilledvol: New filled volume output, usually wm.mgz.
        debug_voxel: Specify the voxel to debug with coordinates C R S.
        nocorners: No removal of corner configurations in addition to edge ones.
        write: Turn on diagnostic writing.
        keep: Keep WM edits.
        test: Adds a voxel to test removal by mri_pretess, retained with -keep.\
            Output not saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPretessOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PRETESS_METADATA)
    params = mri_pretess_params(filledvol=filledvol, labelstring=labelstring, normvol=normvol, newfilledvol=newfilledvol, debug_voxel=debug_voxel, nocorners=nocorners, write=write, keep=keep, test=test)
    return mri_pretess_execute(params, execution)


__all__ = [
    "MRI_PRETESS_METADATA",
    "MriPretessOutputs",
    "MriPretessParameters",
    "mri_pretess",
    "mri_pretess_params",
]
