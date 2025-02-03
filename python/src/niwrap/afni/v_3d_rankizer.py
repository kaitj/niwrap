# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_RANKIZER_METADATA = Metadata(
    id="e854a99a853a99ed471d7da08fb007bec90426d2.boutiques",
    name="3dRankizer",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dRankizerParameters = typing.TypedDict('V3dRankizerParameters', {
    "__STYX_TYPE__": typing.Literal["3dRankizer"],
    "dataset": InputPathType,
    "base_rank": typing.NotRequired[float | None],
    "mask": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "percentize": bool,
    "percentize_mask": bool,
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
        "3dRankizer": v_3d_rankizer_cargs,
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
        "3dRankizer": v_3d_rankizer_outputs,
    }
    return vt.get(t)


class V3dRankizerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rankizer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output float-format dataset containing ranked voxel values"""


def v_3d_rankizer_params(
    dataset: InputPathType,
    prefix: str,
    base_rank: float | None = None,
    mask: InputPathType | None = None,
    percentize: bool = False,
    percentize_mask: bool = False,
) -> V3dRankizerParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input MRI dataset.
        prefix: Write results into float-format output dataset.
        base_rank: Set the 'base' rank instead of 1.
        mask: Use the specified dataset as a mask. Only voxels with nonzero\
            values in this mask will be used from the input dataset. Voxels outside\
            the mask will get rank 0.
        percentize: Divide rank by the number of voxels in the dataset and\
            multiply by 100.0.
        percentize_mask: Divide rank by the number of voxels in the mask and\
            multiply by 100.0.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dRankizer",
        "dataset": dataset,
        "prefix": prefix,
        "percentize": percentize,
        "percentize_mask": percentize_mask,
    }
    if base_rank is not None:
        params["base_rank"] = base_rank
    if mask is not None:
        params["mask"] = mask
    return params


def v_3d_rankizer_cargs(
    params: V3dRankizerParameters,
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
    cargs.append("3dRankizer")
    cargs.append(execution.input_file(params.get("dataset")))
    if params.get("base_rank") is not None:
        cargs.extend([
            "-brank",
            str(params.get("base_rank"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("percentize"):
        cargs.append("-percentize")
    if params.get("percentize_mask"):
        cargs.append("-percentize_mask")
    return cargs


def v_3d_rankizer_outputs(
    params: V3dRankizerParameters,
    execution: Execution,
) -> V3dRankizerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dRankizerOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + "+tlrc.HEAD"),
    )
    return ret


def v_3d_rankizer_execute(
    params: V3dRankizerParameters,
    execution: Execution,
) -> V3dRankizerOutputs:
    """
    Tool to rank each voxel as sorted into increasing value. Ties get the average
    rank.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dRankizerOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_rankizer_cargs(params, execution)
    ret = v_3d_rankizer_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_rankizer(
    dataset: InputPathType,
    prefix: str,
    base_rank: float | None = None,
    mask: InputPathType | None = None,
    percentize: bool = False,
    percentize_mask: bool = False,
    runner: Runner | None = None,
) -> V3dRankizerOutputs:
    """
    Tool to rank each voxel as sorted into increasing value. Ties get the average
    rank.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input MRI dataset.
        prefix: Write results into float-format output dataset.
        base_rank: Set the 'base' rank instead of 1.
        mask: Use the specified dataset as a mask. Only voxels with nonzero\
            values in this mask will be used from the input dataset. Voxels outside\
            the mask will get rank 0.
        percentize: Divide rank by the number of voxels in the dataset and\
            multiply by 100.0.
        percentize_mask: Divide rank by the number of voxels in the mask and\
            multiply by 100.0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRankizerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RANKIZER_METADATA)
    params = v_3d_rankizer_params(dataset=dataset, base_rank=base_rank, mask=mask, prefix=prefix, percentize=percentize, percentize_mask=percentize_mask)
    return v_3d_rankizer_execute(params, execution)


__all__ = [
    "V3dRankizerOutputs",
    "V_3D_RANKIZER_METADATA",
    "v_3d_rankizer",
    "v_3d_rankizer_params",
]
