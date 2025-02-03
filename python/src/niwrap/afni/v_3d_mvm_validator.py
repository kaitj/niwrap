# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_MVM_VALIDATOR_METADATA = Metadata(
    id="922fe2d0a794693ed3858b8e880aa7f811995c48.boutiques",
    name="3dMVM_validator",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dMvmValidatorParameters = typing.TypedDict('V3dMvmValidatorParameters', {
    "__STYX_TYPE__": typing.Literal["3dMVM_validator"],
    "datatable": InputPathType,
    "shinyfolder": typing.NotRequired[str | None],
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
        "3dMVM_validator": v_3d_mvm_validator_cargs,
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
        "3dMVM_validator": v_3d_mvm_validator_outputs,
    }
    return vt.get(t)


class V3dMvmValidatorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mvm_validator(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    temp_folder: OutputPathType
    """Temporary folder created during the shiny app session."""


def v_3d_mvm_validator_params(
    datatable: InputPathType,
    shinyfolder: str | None = None,
) -> V3dMvmValidatorParameters:
    """
    Build parameters.
    
    Args:
        datatable: A file containing a data table formatted like the 3dMVM\
            "-dataTable".
        shinyfolder: Use a custom shiny folder (for testing purposes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMVM_validator",
        "datatable": datatable,
    }
    if shinyfolder is not None:
        params["shinyfolder"] = shinyfolder
    return params


def v_3d_mvm_validator_cargs(
    params: V3dMvmValidatorParameters,
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
    cargs.append("3dMVM_validator")
    cargs.append(execution.input_file(params.get("datatable")))
    if params.get("shinyfolder") is not None:
        cargs.extend([
            "-ShinyFolder",
            params.get("shinyfolder")
        ])
    return cargs


def v_3d_mvm_validator_outputs(
    params: V3dMvmValidatorParameters,
    execution: Execution,
) -> V3dMvmValidatorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMvmValidatorOutputs(
        root=execution.output_file("."),
        temp_folder=execution.output_file("__*_3dMVM_validator_temp_delete"),
    )
    return ret


def v_3d_mvm_validator_execute(
    params: V3dMvmValidatorParameters,
    execution: Execution,
) -> V3dMvmValidatorOutputs:
    """
    Launch the 3dMVM model validation shiny app in a web browser.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMvmValidatorOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_mvm_validator_cargs(params, execution)
    ret = v_3d_mvm_validator_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mvm_validator(
    datatable: InputPathType,
    shinyfolder: str | None = None,
    runner: Runner | None = None,
) -> V3dMvmValidatorOutputs:
    """
    Launch the 3dMVM model validation shiny app in a web browser.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datatable: A file containing a data table formatted like the 3dMVM\
            "-dataTable".
        shinyfolder: Use a custom shiny folder (for testing purposes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMvmValidatorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MVM_VALIDATOR_METADATA)
    params = v_3d_mvm_validator_params(datatable=datatable, shinyfolder=shinyfolder)
    return v_3d_mvm_validator_execute(params, execution)


__all__ = [
    "V3dMvmValidatorOutputs",
    "V_3D_MVM_VALIDATOR_METADATA",
    "v_3d_mvm_validator",
    "v_3d_mvm_validator_params",
]
