# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CONVERT_METADATA = Metadata(
    id="072cf5d2422186514e5e2726e7afe06ff330f744.boutiques",
    name="mri_convert",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriConvertParameters = typing.TypedDict('MriConvertParameters', {
    "__STYX_TYPE__": typing.Literal["mri_convert"],
    "inp_volume": InputPathType,
    "out_volume": str,
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
        "mri_convert": mri_convert_cargs,
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
        "mri_convert": mri_convert_outputs,
    }
    return vt.get(t)


class MriConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_volume: OutputPathType
    """Converted volume output file"""


def mri_convert_params(
    inp_volume: InputPathType,
    out_volume: str,
) -> MriConvertParameters:
    """
    Build parameters.
    
    Args:
        inp_volume: The input volume file.
        out_volume: The output volume file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_convert",
        "inp_volume": inp_volume,
        "out_volume": out_volume,
    }
    return params


def mri_convert_cargs(
    params: MriConvertParameters,
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
    cargs.append("mri_convert")
    cargs.append(execution.input_file(params.get("inp_volume")))
    cargs.append(params.get("out_volume"))
    cargs.append("[OPTIONS]")
    return cargs


def mri_convert_outputs(
    params: MriConvertParameters,
    execution: Execution,
) -> MriConvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriConvertOutputs(
        root=execution.output_file("."),
        converted_volume=execution.output_file(params.get("out_volume")),
    )
    return ret


def mri_convert_execute(
    params: MriConvertParameters,
    execution: Execution,
) -> MriConvertOutputs:
    """
    A general purpose utility for converting between different file formats
    supported by FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriConvertOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_convert_cargs(params, execution)
    ret = mri_convert_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_convert(
    inp_volume: InputPathType,
    out_volume: str,
    runner: Runner | None = None,
) -> MriConvertOutputs:
    """
    A general purpose utility for converting between different file formats
    supported by FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        inp_volume: The input volume file.
        out_volume: The output volume file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONVERT_METADATA)
    params = mri_convert_params(inp_volume=inp_volume, out_volume=out_volume)
    return mri_convert_execute(params, execution)


__all__ = [
    "MRI_CONVERT_METADATA",
    "MriConvertOutputs",
    "mri_convert",
    "mri_convert_params",
]
