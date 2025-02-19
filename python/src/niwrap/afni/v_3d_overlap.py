# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_OVERLAP_METADATA = Metadata(
    id="a1bc040d8dc7e5b89536a75a10ba6ad55a1ecc95.boutiques",
    name="3dOverlap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dOverlapParameters = typing.TypedDict('V3dOverlapParameters', {
    "__STYX_TYPE__": typing.Literal["3dOverlap"],
    "dataset1": InputPathType,
    "dataset2": list[InputPathType],
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
        "3dOverlap": v_3d_overlap_cargs,
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
        "3dOverlap": v_3d_overlap_outputs,
    }.get(t)


class V3dOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType
    """BRIK file with count of overlaps at each voxel (if -save is used)"""
    output_head: OutputPathType
    """HEAD file with count of overlaps at each voxel (if -save is used)"""


def v_3d_overlap_params(
    dataset1: InputPathType,
    dataset2: list[InputPathType],
) -> V3dOverlapParameters:
    """
    Build parameters.
    
    Args:
        dataset1: First input dataset (e.g. dset1+orig).
        dataset2: Second input dataset (e.g. dset2+orig).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dOverlap",
        "dataset1": dataset1,
        "dataset2": dataset2,
    }
    return params


def v_3d_overlap_cargs(
    params: V3dOverlapParameters,
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
    cargs.append("3dOverlap")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(params.get("dataset1")))
    cargs.extend([execution.input_file(f) for f in params.get("dataset2")])
    return cargs


def v_3d_overlap_outputs(
    params: V3dOverlapParameters,
    execution: Execution,
) -> V3dOverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dOverlapOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file("[SAVE_PREFIX]+orig.BRIK"),
        output_head=execution.output_file("[SAVE_PREFIX]+orig.HEAD"),
    )
    return ret


def v_3d_overlap_execute(
    params: V3dOverlapParameters,
    execution: Execution,
) -> V3dOverlapOutputs:
    """
    Counts the number of voxels that are nonzero in all input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dOverlapOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_overlap_cargs(params, execution)
    ret = v_3d_overlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_overlap(
    dataset1: InputPathType,
    dataset2: list[InputPathType],
    runner: Runner | None = None,
) -> V3dOverlapOutputs:
    """
    Counts the number of voxels that are nonzero in all input datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset1: First input dataset (e.g. dset1+orig).
        dataset2: Second input dataset (e.g. dset2+orig).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_OVERLAP_METADATA)
    params = v_3d_overlap_params(dataset1=dataset1, dataset2=dataset2)
    return v_3d_overlap_execute(params, execution)


__all__ = [
    "V3dOverlapOutputs",
    "V3dOverlapParameters",
    "V_3D_OVERLAP_METADATA",
    "v_3d_overlap",
    "v_3d_overlap_params",
]
