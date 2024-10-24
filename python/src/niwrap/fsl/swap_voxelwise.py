# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SWAP_VOXELWISE_METADATA = Metadata(
    id="05f789c598386ac6160bcda86def15193dd2c92e.boutiques",
    name="swap_voxelwise",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SwapVoxelwiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swap_voxelwise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    reordered_output: OutputPathType | None
    """Output file with reordered vectors (default name 'reordered.nii.gz')"""


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
    cargs = []
    cargs.append("swap_voxelwise")
    cargs.append("-v")
    cargs.extend([
        "-v",
        execution.input_file(vectors_file_list)
    ])
    cargs.append("-s")
    if scalars_file_list is not None:
        cargs.extend([
            "-s",
            execution.input_file(scalars_file_list)
        ])
    cargs.append("-m")
    cargs.extend([
        "-m",
        execution.input_file(mask)
    ])
    cargs.append("-b")
    if output_base_name is not None:
        cargs.extend([
            "-b",
            output_base_name
        ])
    cargs.append("--mode")
    if reorder_mode is not None:
        cargs.extend([
            "--mode",
            reorder_mode
        ])
    cargs.append("--initmask")
    if init_mask is not None:
        cargs.extend([
            "--initmask",
            execution.input_file(init_mask)
        ])
    cargs.append("--xthresh")
    if crossing_thresh is not None:
        cargs.extend([
            "--xthresh",
            str(crossing_thresh)
        ])
    cargs.append("-V")
    ret = SwapVoxelwiseOutputs(
        root=execution.output_file("."),
        reordered_output=execution.output_file(output_base_name + ".nii.gz") if (output_base_name is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SWAP_VOXELWISE_METADATA",
    "SwapVoxelwiseOutputs",
    "swap_voxelwise",
]
