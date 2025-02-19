# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_TFILTER_METADATA = Metadata(
    id="4735e83a23f97826ec3c39f708b0bfaeaff9f5e9.boutiques",
    name="3dTfilter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTfilterParameters = typing.TypedDict('V3dTfilterParameters', {
    "__STYX_TYPE__": typing.Literal["3dTfilter"],
    "inputdataset": InputPathType,
    "outputdataset": str,
    "filters": list[str],
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
        "3dTfilter": v_3d_tfilter_cargs,
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
        "3dTfilter": v_3d_tfilter_outputs,
    }.get(t)


class V3dTfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Filtered output dataset"""


def v_3d_tfilter_params(
    inputdataset: InputPathType,
    outputdataset: str,
    filters: list[str],
) -> V3dTfilterParameters:
    """
    Build parameters.
    
    Args:
        inputdataset: Input dataset.
        outputdataset: Output dataset.
        filters: Filter function(s) to apply.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTfilter",
        "inputdataset": inputdataset,
        "outputdataset": outputdataset,
        "filters": filters,
    }
    return params


def v_3d_tfilter_cargs(
    params: V3dTfilterParameters,
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
    cargs.append("3dTfilter")
    cargs.extend([
        "-input",
        execution.input_file(params.get("inputdataset"))
    ])
    cargs.extend([
        "-prefix",
        params.get("outputdataset")
    ])
    cargs.extend([
        "-filter",
        *params.get("filters")
    ])
    return cargs


def v_3d_tfilter_outputs(
    params: V3dTfilterParameters,
    execution: Execution,
) -> V3dTfilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTfilterOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("outputdataset")),
    )
    return ret


def v_3d_tfilter_execute(
    params: V3dTfilterParameters,
    execution: Execution,
) -> V3dTfilterOutputs:
    """
    3dTfilter filters the time series in each voxel according to the user-specified
    filter functions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTfilterOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_tfilter_cargs(params, execution)
    ret = v_3d_tfilter_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_tfilter(
    inputdataset: InputPathType,
    outputdataset: str,
    filters: list[str],
    runner: Runner | None = None,
) -> V3dTfilterOutputs:
    """
    3dTfilter filters the time series in each voxel according to the user-specified
    filter functions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inputdataset: Input dataset.
        outputdataset: Output dataset.
        filters: Filter function(s) to apply.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TFILTER_METADATA)
    params = v_3d_tfilter_params(inputdataset=inputdataset, outputdataset=outputdataset, filters=filters)
    return v_3d_tfilter_execute(params, execution)


__all__ = [
    "V3dTfilterOutputs",
    "V3dTfilterParameters",
    "V_3D_TFILTER_METADATA",
    "v_3d_tfilter",
    "v_3d_tfilter_params",
]
