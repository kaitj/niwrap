# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_ADD_XFORM_TO_HEADER_METADATA = Metadata(
    id="a352e8c6ada4a640929cf21a7797106f093df774.boutiques",
    name="mri_add_xform_to_header",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriAddXformToHeaderParameters = typing.TypedDict('MriAddXformToHeaderParameters', {
    "__STYX_TYPE__": typing.Literal["mri_add_xform_to_header"],
    "xfm_file": InputPathType,
    "input_volume": InputPathType,
    "output_volume": str,
    "verbose": bool,
    "copy_name": bool,
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
        "mri_add_xform_to_header": mri_add_xform_to_header_cargs,
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
        "mri_add_xform_to_header": mri_add_xform_to_header_outputs,
    }
    return vt.get(t)


class MriAddXformToHeaderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_add_xform_to_header(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """Volume output with added transformation."""


def mri_add_xform_to_header_params(
    xfm_file: InputPathType,
    input_volume: InputPathType,
    output_volume: str,
    verbose: bool = False,
    copy_name: bool = False,
) -> MriAddXformToHeaderParameters:
    """
    Build parameters.
    
    Args:
        xfm_file: Transformation file to be added to the volume header.
        input_volume: Input volume to which the transformation is added.
        output_volume: Output volume with the transformation included.
        verbose: Enable verbose output for more detailed logging.
        copy_name: Copy the name of the xfm file without loading it.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_add_xform_to_header",
        "xfm_file": xfm_file,
        "input_volume": input_volume,
        "output_volume": output_volume,
        "verbose": verbose,
        "copy_name": copy_name,
    }
    return params


def mri_add_xform_to_header_cargs(
    params: MriAddXformToHeaderParameters,
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
    cargs.append("mri_add_xform_to_header")
    cargs.append(execution.input_file(params.get("xfm_file")))
    cargs.append(execution.input_file(params.get("input_volume")))
    cargs.append(params.get("output_volume"))
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("copy_name"):
        cargs.append("-c")
    return cargs


def mri_add_xform_to_header_outputs(
    params: MriAddXformToHeaderParameters,
    execution: Execution,
) -> MriAddXformToHeaderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriAddXformToHeaderOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_add_xform_to_header_execute(
    params: MriAddXformToHeaderParameters,
    execution: Execution,
) -> MriAddXformToHeaderOutputs:
    """
    Program to add specified transformation to the volume header.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriAddXformToHeaderOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_add_xform_to_header_cargs(params, execution)
    ret = mri_add_xform_to_header_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_add_xform_to_header(
    xfm_file: InputPathType,
    input_volume: InputPathType,
    output_volume: str,
    verbose: bool = False,
    copy_name: bool = False,
    runner: Runner | None = None,
) -> MriAddXformToHeaderOutputs:
    """
    Program to add specified transformation to the volume header.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        xfm_file: Transformation file to be added to the volume header.
        input_volume: Input volume to which the transformation is added.
        output_volume: Output volume with the transformation included.
        verbose: Enable verbose output for more detailed logging.
        copy_name: Copy the name of the xfm file without loading it.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAddXformToHeaderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ADD_XFORM_TO_HEADER_METADATA)
    params = mri_add_xform_to_header_params(xfm_file=xfm_file, input_volume=input_volume, output_volume=output_volume, verbose=verbose, copy_name=copy_name)
    return mri_add_xform_to_header_execute(params, execution)


__all__ = [
    "MRI_ADD_XFORM_TO_HEADER_METADATA",
    "MriAddXformToHeaderOutputs",
    "mri_add_xform_to_header",
    "mri_add_xform_to_header_params",
]
