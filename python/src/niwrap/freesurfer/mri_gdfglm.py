# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_GDFGLM_METADATA = Metadata(
    id="6bfd0a6b2b32f6fa09eb9767dc1f8e35ce2df1d6.boutiques",
    name="mri_gdfglm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriGdfglmParameters = typing.TypedDict('MriGdfglmParameters', {
    "__STYX_TYPE__": typing.Literal["mri_gdfglm"],
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
        "mri_gdfglm": mri_gdfglm_cargs,
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
        "mri_gdfglm": mri_gdfglm_outputs,
    }
    return vt.get(t)


class MriGdfglmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_gdfglm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outputs: OutputPathType
    """Output information is not available because the command has been
    removed."""


def mri_gdfglm_params(
) -> MriGdfglmParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_gdfglm",
    }
    return params


def mri_gdfglm_cargs(
    params: MriGdfglmParameters,
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
    cargs.append("mri_gdfglm")
    return cargs


def mri_gdfglm_outputs(
    params: MriGdfglmParameters,
    execution: Execution,
) -> MriGdfglmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriGdfglmOutputs(
        root=execution.output_file("."),
        outputs=execution.output_file("[OUTPUT]"),
    )
    return ret


def mri_gdfglm_execute(
    params: MriGdfglmParameters,
    execution: Execution,
) -> MriGdfglmOutputs:
    """
    The mri_gdfglm command has been removed from the current version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriGdfglmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_gdfglm_cargs(params, execution)
    ret = mri_gdfglm_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_gdfglm(
    runner: Runner | None = None,
) -> MriGdfglmOutputs:
    """
    The mri_gdfglm command has been removed from the current version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriGdfglmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_GDFGLM_METADATA)
    params = mri_gdfglm_params()
    return mri_gdfglm_execute(params, execution)


__all__ = [
    "MRI_GDFGLM_METADATA",
    "MriGdfglmOutputs",
    "mri_gdfglm",
    "mri_gdfglm_params",
]
