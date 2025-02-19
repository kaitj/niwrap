# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLORIENT_FSL_METADATA = Metadata(
    id="91c87d301655f1a487272843a72c1efbca6dd79a.boutiques",
    name="fslorient.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FslorientFslParameters = typing.TypedDict('FslorientFslParameters', {
    "__STYX_TYPE__": typing.Literal["fslorient.fsl"],
    "swap_orient": bool,
    "filename": InputPathType,
    "set_qform": typing.NotRequired[list[float] | None],
    "set_qform_code": typing.NotRequired[str | None],
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
        "fslorient.fsl": fslorient_fsl_cargs,
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


class FslorientFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslorient_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslorient_fsl_params(
    filename: InputPathType,
    swap_orient: bool = False,
    set_qform: list[float] | None = None,
    set_qform_code: str | None = None,
) -> FslorientFslParameters:
    """
    Build parameters.
    
    Args:
        filename: Input image filename.
        swap_orient: Swaps FSL radiological and FSL neurological.
        set_qform: Sets the 16 elements of the qform matrix.
        set_qform_code: Sets qform integer code.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslorient.fsl",
        "swap_orient": swap_orient,
        "filename": filename,
    }
    if set_qform is not None:
        params["set_qform"] = set_qform
    if set_qform_code is not None:
        params["set_qform_code"] = set_qform_code
    return params


def fslorient_fsl_cargs(
    params: FslorientFslParameters,
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
    cargs.append("fslorient")
    if params.get("swap_orient"):
        cargs.append("-swaporient")
    cargs.append(execution.input_file(params.get("filename")))
    if params.get("set_qform") is not None:
        cargs.extend([
            "-setqform",
            *map(str, params.get("set_qform"))
        ])
    if params.get("set_qform_code") is not None:
        cargs.extend([
            "-setqformcode",
            params.get("set_qform_code")
        ])
    return cargs


def fslorient_fsl_outputs(
    params: FslorientFslParameters,
    execution: Execution,
) -> FslorientFslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslorientFslOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslorient_fsl_execute(
    params: FslorientFslParameters,
    execution: Execution,
) -> FslorientFslOutputs:
    """
    A tool for managing the orientations and orientation headers of NIFTI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslorientFslOutputs`).
    """
    params = execution.params(params)
    cargs = fslorient_fsl_cargs(params, execution)
    ret = fslorient_fsl_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslorient_fsl(
    filename: InputPathType,
    swap_orient: bool = False,
    set_qform: list[float] | None = None,
    set_qform_code: str | None = None,
    runner: Runner | None = None,
) -> FslorientFslOutputs:
    """
    A tool for managing the orientations and orientation headers of NIFTI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        filename: Input image filename.
        swap_orient: Swaps FSL radiological and FSL neurological.
        set_qform: Sets the 16 elements of the qform matrix.
        set_qform_code: Sets qform integer code.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslorientFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLORIENT_FSL_METADATA)
    params = fslorient_fsl_params(swap_orient=swap_orient, filename=filename, set_qform=set_qform, set_qform_code=set_qform_code)
    return fslorient_fsl_execute(params, execution)


__all__ = [
    "FSLORIENT_FSL_METADATA",
    "FslorientFslOutputs",
    "FslorientFslParameters",
    "fslorient_fsl",
    "fslorient_fsl_params",
]
