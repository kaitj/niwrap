# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GCATRAINSKULL_METADATA = Metadata(
    id="89af41167df36313b39cb032d8e1c2c288ba043b.boutiques",
    name="gcatrainskull",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
GcatrainskullParameters = typing.TypedDict('GcatrainskullParameters', {
    "__STYX_TYPE__": typing.Literal["gcatrainskull"],
    "gcatrain_dir": str,
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
        "gcatrainskull": gcatrainskull_cargs,
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


def gcatrainskull_params(
    gcatrain_dir: str,
) -> GcatrainskullParameters:
    """
    Build parameters.
    
    Args:
        gcatrain_dir: Directory containing GCA training data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gcatrainskull",
        "gcatrain_dir": gcatrain_dir,
    }
    return params


def gcatrainskull_cargs(
    params: GcatrainskullParameters,
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
    cargs.append("gcatrainskull")
    cargs.extend([
        "--g",
        params.get("gcatrain_dir")
    ])
    return cargs


def gcatrainskull_outputs(
    params: GcatrainskullParameters,
    execution: Execution,
) -> GcatrainskullOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GcatrainskullOutputs(
        root=execution.output_file("."),
    )
    return ret


def gcatrainskull_execute(
    params: GcatrainskullParameters,
    execution: Execution,
) -> GcatrainskullOutputs:
    """
    GCA train skull stripping tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GcatrainskullOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = gcatrainskull_cargs(params, execution)
    ret = gcatrainskull_outputs(params, execution)
    execution.run(cargs)
    return ret


def gcatrainskull(
    gcatrain_dir: str,
    runner: Runner | None = None,
) -> GcatrainskullOutputs:
    """
    GCA train skull stripping tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gcatrain_dir: Directory containing GCA training data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GcatrainskullOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GCATRAINSKULL_METADATA)
    params = gcatrainskull_params(gcatrain_dir=gcatrain_dir)
    return gcatrainskull_execute(params, execution)


__all__ = [
    "GCATRAINSKULL_METADATA",
    "gcatrainskull",
    "gcatrainskull_params",
]
