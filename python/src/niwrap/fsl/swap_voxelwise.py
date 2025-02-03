# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SWAP_VOXELWISE_METADATA = Metadata(
    id="4d3f862f263904d851a583fa7d717c4e6949c262.boutiques",
    name="swap_voxelwise",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SwapVoxelwiseParameters = typing.TypedDict('SwapVoxelwiseParameters', {
    "__STYX_TYPE__": typing.Literal["swap_voxelwise"],
    "vectors_file_list": InputPathType,
    "scalars_file_list": typing.NotRequired[InputPathType | None],
    "mask": InputPathType,
    "output_base_name": typing.NotRequired[str | None],
    "reorder_mode": typing.NotRequired[str | None],
    "init_mask": typing.NotRequired[InputPathType | None],
    "crossing_thresh": typing.NotRequired[float | None],
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
        "swap_voxelwise": swap_voxelwise_cargs,
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
        "swap_voxelwise": swap_voxelwise_outputs,
    }
    return vt.get(t)


class SwapVoxelwiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swap_voxelwise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reordered_output: OutputPathType | None
    """Output file with reordered vectors (default name 'reordered.nii.gz')"""


def swap_voxelwise_params(
    vectors_file_list: InputPathType,
    mask: InputPathType,
    scalars_file_list: InputPathType | None = None,
    output_base_name: str | None = "reordered",
    reorder_mode: str | None = "voxels",
    init_mask: InputPathType | None = None,
    crossing_thresh: float | None = 0.1,
) -> SwapVoxelwiseParameters:
    """
    Build parameters.
    
    Args:
        vectors_file_list: Text file containing list of vectors.
        mask: Filename of brain mask or skeleton.
        scalars_file_list: Text file containing list of scalars.
        output_base_name: Output base name.
        reorder_mode: Reordering mode - choose between 'voxels' (default) or\
            'volumes'.
        init_mask: Filename of initialization mask.
        crossing_thresh: Threshold for considering a crossing fibre region -\
            default=0.1.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "swap_voxelwise",
        "vectors_file_list": vectors_file_list,
        "mask": mask,
    }
    if scalars_file_list is not None:
        params["scalars_file_list"] = scalars_file_list
    if output_base_name is not None:
        params["output_base_name"] = output_base_name
    if reorder_mode is not None:
        params["reorder_mode"] = reorder_mode
    if init_mask is not None:
        params["init_mask"] = init_mask
    if crossing_thresh is not None:
        params["crossing_thresh"] = crossing_thresh
    return params


def swap_voxelwise_cargs(
    params: SwapVoxelwiseParameters,
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
    cargs.append("swap_voxelwise")
    cargs.extend([
        "-v",
        execution.input_file(params.get("vectors_file_list"))
    ])
    if params.get("scalars_file_list") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("scalars_file_list"))
        ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("mask"))
    ])
    if params.get("output_base_name") is not None:
        cargs.extend([
            "-b",
            params.get("output_base_name")
        ])
    if params.get("reorder_mode") is not None:
        cargs.extend([
            "--mode",
            params.get("reorder_mode")
        ])
    if params.get("init_mask") is not None:
        cargs.extend([
            "--initmask",
            execution.input_file(params.get("init_mask"))
        ])
    if params.get("crossing_thresh") is not None:
        cargs.extend([
            "--xthresh",
            str(params.get("crossing_thresh"))
        ])
    cargs.append("-V")
    return cargs


def swap_voxelwise_outputs(
    params: SwapVoxelwiseParameters,
    execution: Execution,
) -> SwapVoxelwiseOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SwapVoxelwiseOutputs(
        root=execution.output_file("."),
        reordered_output=execution.output_file(params.get("output_base_name") + ".nii.gz") if (params.get("output_base_name") is not None) else None,
    )
    return ret


def swap_voxelwise_execute(
    params: SwapVoxelwiseParameters,
    execution: Execution,
) -> SwapVoxelwiseOutputs:
    """
    Reordering of vectors with direction preservation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SwapVoxelwiseOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = swap_voxelwise_cargs(params, execution)
    ret = swap_voxelwise_outputs(params, execution)
    execution.run(cargs)
    return ret


def swap_voxelwise(
    vectors_file_list: InputPathType,
    mask: InputPathType,
    scalars_file_list: InputPathType | None = None,
    output_base_name: str | None = "reordered",
    reorder_mode: str | None = "voxels",
    init_mask: InputPathType | None = None,
    crossing_thresh: float | None = 0.1,
    runner: Runner | None = None,
) -> SwapVoxelwiseOutputs:
    """
    Reordering of vectors with direction preservation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        vectors_file_list: Text file containing list of vectors.
        mask: Filename of brain mask or skeleton.
        scalars_file_list: Text file containing list of scalars.
        output_base_name: Output base name.
        reorder_mode: Reordering mode - choose between 'voxels' (default) or\
            'volumes'.
        init_mask: Filename of initialization mask.
        crossing_thresh: Threshold for considering a crossing fibre region -\
            default=0.1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SwapVoxelwiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SWAP_VOXELWISE_METADATA)
    params = swap_voxelwise_params(vectors_file_list=vectors_file_list, scalars_file_list=scalars_file_list, mask=mask, output_base_name=output_base_name, reorder_mode=reorder_mode, init_mask=init_mask, crossing_thresh=crossing_thresh)
    return swap_voxelwise_execute(params, execution)


__all__ = [
    "SWAP_VOXELWISE_METADATA",
    "SwapVoxelwiseOutputs",
    "swap_voxelwise",
    "swap_voxelwise_params",
]
