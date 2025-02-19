# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__REORDER_METADATA = Metadata(
    id="93af53020ee1088a33b0e58234dc8960b688e23e.boutiques",
    name="@Reorder",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VReorderParameters = typing.TypedDict('VReorderParameters', {
    "__STYX_TYPE__": typing.Literal["@Reorder"],
    "input_dataset": InputPathType,
    "mapfile": InputPathType,
    "prefix": str,
    "offset": typing.NotRequired[float | None],
    "save_work": bool,
    "test": bool,
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
        "@Reorder": v__reorder_cargs,
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
        "@Reorder": v__reorder_outputs,
    }.get(t)


class VReorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__reorder(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Reordered output dataset"""


def v__reorder_params(
    input_dataset: InputPathType,
    mapfile: InputPathType,
    prefix: str,
    offset: float | None = None,
    save_work: bool = False,
    test: bool = False,
) -> VReorderParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset to reorder (e.g. EPI+tlrc).
        mapfile: TR to event mapping file (e.g. events.txt).
        prefix: Prefix for the output dataset.
        offset: Offset mapfile TR indices by OFFSET (in TRs).
        save_work: Do not delete work directory (reorder.work.dir) at the end.
        test: Just report sub-bricks, do not create datasets.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Reorder",
        "input_dataset": input_dataset,
        "mapfile": mapfile,
        "prefix": prefix,
        "save_work": save_work,
        "test": test,
    }
    if offset is not None:
        params["offset"] = offset
    return params


def v__reorder_cargs(
    params: VReorderParameters,
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
    cargs.append("@Reorder")
    cargs.append(execution.input_file(params.get("input_dataset")))
    cargs.append(execution.input_file(params.get("mapfile")))
    cargs.append(params.get("prefix"))
    if params.get("offset") is not None:
        cargs.extend([
            "-offset",
            str(params.get("offset"))
        ])
    if params.get("save_work"):
        cargs.append("-save_work")
    if params.get("test"):
        cargs.append("-test")
    return cargs


def v__reorder_outputs(
    params: VReorderParameters,
    execution: Execution,
) -> VReorderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VReorderOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + "+tlrc"),
    )
    return ret


def v__reorder_execute(
    params: VReorderParameters,
    execution: Execution,
) -> VReorderOutputs:
    """
    Reorder sub-bricks of a dataset based on event mapping. Works similarly to the
    Reorder plugin.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VReorderOutputs`).
    """
    params = execution.params(params)
    cargs = v__reorder_cargs(params, execution)
    ret = v__reorder_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__reorder(
    input_dataset: InputPathType,
    mapfile: InputPathType,
    prefix: str,
    offset: float | None = None,
    save_work: bool = False,
    test: bool = False,
    runner: Runner | None = None,
) -> VReorderOutputs:
    """
    Reorder sub-bricks of a dataset based on event mapping. Works similarly to the
    Reorder plugin.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset to reorder (e.g. EPI+tlrc).
        mapfile: TR to event mapping file (e.g. events.txt).
        prefix: Prefix for the output dataset.
        offset: Offset mapfile TR indices by OFFSET (in TRs).
        save_work: Do not delete work directory (reorder.work.dir) at the end.
        test: Just report sub-bricks, do not create datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VReorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__REORDER_METADATA)
    params = v__reorder_params(input_dataset=input_dataset, mapfile=mapfile, prefix=prefix, offset=offset, save_work=save_work, test=test)
    return v__reorder_execute(params, execution)


__all__ = [
    "VReorderOutputs",
    "VReorderParameters",
    "V__REORDER_METADATA",
    "v__reorder",
    "v__reorder_params",
]
