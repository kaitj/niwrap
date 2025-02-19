# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__GET_AFNI_RES_METADATA = Metadata(
    id="8e9d3bd1817738927cfd2699a3bf4ffe4e305e07.boutiques",
    name="@GetAfniRes",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VGetAfniResParameters = typing.TypedDict('VGetAfniResParameters', {
    "__STYX_TYPE__": typing.Literal["@GetAfniRes"],
    "output_type": typing.NotRequired[typing.Literal["-min", "-max", "-mean"] | None],
    "input_dataset": InputPathType,
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
        "@GetAfniRes": v__get_afni_res_cargs,
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


class VGetAfniResOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__get_afni_res(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__get_afni_res_params(
    input_dataset: InputPathType,
    output_type: typing.Literal["-min", "-max", "-mean"] | None = None,
) -> VGetAfniResParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset.
        output_type: Output type specifying whether to return the minimum,\
            maximum, or mean resolution.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@GetAfniRes",
        "input_dataset": input_dataset,
    }
    if output_type is not None:
        params["output_type"] = output_type
    return params


def v__get_afni_res_cargs(
    params: VGetAfniResParameters,
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
    if params.get("output_type") is not None:
        cargs.append("@GetAfniRes" + params.get("output_type"))
    cargs.append(execution.input_file(params.get("input_dataset")))
    return cargs


def v__get_afni_res_outputs(
    params: VGetAfniResParameters,
    execution: Execution,
) -> VGetAfniResOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VGetAfniResOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__get_afni_res_execute(
    params: VGetAfniResParameters,
    execution: Execution,
) -> VGetAfniResOutputs:
    """
    Tool to return the voxel resolution of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VGetAfniResOutputs`).
    """
    params = execution.params(params)
    cargs = v__get_afni_res_cargs(params, execution)
    ret = v__get_afni_res_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__get_afni_res(
    input_dataset: InputPathType,
    output_type: typing.Literal["-min", "-max", "-mean"] | None = None,
    runner: Runner | None = None,
) -> VGetAfniResOutputs:
    """
    Tool to return the voxel resolution of a dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset.
        output_type: Output type specifying whether to return the minimum,\
            maximum, or mean resolution.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VGetAfniResOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__GET_AFNI_RES_METADATA)
    params = v__get_afni_res_params(output_type=output_type, input_dataset=input_dataset)
    return v__get_afni_res_execute(params, execution)


__all__ = [
    "VGetAfniResOutputs",
    "VGetAfniResParameters",
    "V__GET_AFNI_RES_METADATA",
    "v__get_afni_res",
    "v__get_afni_res_params",
]
