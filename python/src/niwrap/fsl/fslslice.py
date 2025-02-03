# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSLICE_METADATA = Metadata(
    id="a89f4489f329457c259411cef949573bce403a21.boutiques",
    name="fslslice",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslsliceParameters = typing.TypedDict('FslsliceParameters', {
    "__STYX_TYPE__": typing.Literal["fslslice"],
    "volume": InputPathType,
    "output_basename": typing.NotRequired[str | None],
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
        "fslslice": fslslice_cargs,
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
        "fslslice": fslslice_outputs,
    }
    return vt.get(t)


class FslsliceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslslice(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_slices: OutputPathType | None
    """Extracted 2D slices from the 3D volume"""


def fslslice_params(
    volume: InputPathType,
    output_basename: str | None = None,
) -> FslsliceParameters:
    """
    Build parameters.
    
    Args:
        volume: Input 3D volume (e.g. volume.nii.gz).
        output_basename: Output basename for extracted slices.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslslice",
        "volume": volume,
    }
    if output_basename is not None:
        params["output_basename"] = output_basename
    return params


def fslslice_cargs(
    params: FslsliceParameters,
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
    cargs.append("fslslice")
    cargs.append(execution.input_file(params.get("volume")))
    if params.get("output_basename") is not None:
        cargs.append(params.get("output_basename"))
    return cargs


def fslslice_outputs(
    params: FslsliceParameters,
    execution: Execution,
) -> FslsliceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslsliceOutputs(
        root=execution.output_file("."),
        output_slices=execution.output_file(params.get("output_basename") + "_slice*.nii.gz") if (params.get("output_basename") is not None) else None,
    )
    return ret


def fslslice_execute(
    params: FslsliceParameters,
    execution: Execution,
) -> FslsliceOutputs:
    """
    Tool to extract all slices from a 3D volume and store as 2D images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslsliceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslslice_cargs(params, execution)
    ret = fslslice_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslslice(
    volume: InputPathType,
    output_basename: str | None = None,
    runner: Runner | None = None,
) -> FslsliceOutputs:
    """
    Tool to extract all slices from a 3D volume and store as 2D images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        volume: Input 3D volume (e.g. volume.nii.gz).
        output_basename: Output basename for extracted slices.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsliceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSLICE_METADATA)
    params = fslslice_params(volume=volume, output_basename=output_basename)
    return fslslice_execute(params, execution)


__all__ = [
    "FSLSLICE_METADATA",
    "FslsliceOutputs",
    "fslslice",
    "fslslice_params",
]
