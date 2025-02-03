# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_LABEL_VALS_METADATA = Metadata(
    id="f676fd9e1e255bdfcf8e5d6db1b8b8906a5d7a0e.boutiques",
    name="mri_label_vals",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriLabelValsParameters = typing.TypedDict('MriLabelValsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_label_vals"],
    "volume": InputPathType,
    "label_file": InputPathType,
    "cras_flag": bool,
    "help_flag": bool,
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
        "mri_label_vals": mri_label_vals_cargs,
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


def mri_label_vals_params(
    volume: InputPathType,
    label_file: InputPathType,
    cras_flag: bool = False,
    help_flag: bool = False,
) -> MriLabelValsParameters:
    """
    Build parameters.
    
    Args:
        volume: Input volume file.
        label_file: Input label file.
        cras_flag: Use this option if the label was created where c_(r,a,s) !=\
            0.
        help_flag: Print help.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_label_vals",
        "volume": volume,
        "label_file": label_file,
        "cras_flag": cras_flag,
        "help_flag": help_flag,
    }
    return params


def mri_label_vals_cargs(
    params: MriLabelValsParameters,
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
    cargs.append("mri_label_vals")
    cargs.append(execution.input_file(params.get("volume")))
    cargs.append(execution.input_file(params.get("label_file")))
    if params.get("cras_flag"):
        cargs.append("-cras")
    if params.get("help_flag"):
        cargs.append("-u")
    return cargs


def mri_label_vals_outputs(
    params: MriLabelValsParameters,
    execution: Execution,
) -> MriLabelValsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriLabelValsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_label_vals_execute(
    params: MriLabelValsParameters,
    execution: Execution,
) -> MriLabelValsOutputs:
    """
    Extract values at label coordinates from a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriLabelValsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_label_vals_cargs(params, execution)
    ret = mri_label_vals_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_label_vals(
    volume: InputPathType,
    label_file: InputPathType,
    cras_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriLabelValsOutputs:
    """
    Extract values at label coordinates from a volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume: Input volume file.
        label_file: Input label file.
        cras_flag: Use this option if the label was created where c_(r,a,s) !=\
            0.
        help_flag: Print help.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriLabelValsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_LABEL_VALS_METADATA)
    params = mri_label_vals_params(volume=volume, label_file=label_file, cras_flag=cras_flag, help_flag=help_flag)
    return mri_label_vals_execute(params, execution)


__all__ = [
    "MRI_LABEL_VALS_METADATA",
    "mri_label_vals",
    "mri_label_vals_params",
]
