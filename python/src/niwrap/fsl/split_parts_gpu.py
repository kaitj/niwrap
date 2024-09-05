# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SPLIT_PARTS_GPU_METADATA = Metadata(
    id="71e2866ff20511dbd2491b8e598c537de5bba7fb",
    name="split_parts_gpu",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class SplitPartsGpuOutputs(typing.NamedTuple):
    """
    Output object returned when calling `split_parts_gpu(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_parts: OutputPathType
    """Output parts files"""


def split_parts_gpu(
    datafile: InputPathType,
    maskfile: InputPathType,
    bvals_file: InputPathType,
    bvecs_file: InputPathType,
    use_grad_file: int,
    total_num_parts: int,
    output_directory: str,
    grad_file: str | None = None,
    runner: Runner | None = None,
) -> SplitPartsGpuOutputs:
    """
    split_parts_gpu by Unknown.
    
    Splits parts of data for GPU processing.
    
    Args:
        datafile: Input data file.
        maskfile: Input mask file.
        bvals_file: bvals file.
        bvecs_file: bvecs file.
        use_grad_file: Use gradient file (0 or 1).
        total_num_parts: Total number of parts.
        output_directory: Output directory.
        grad_file: Gradient file (can be null).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SplitPartsGpuOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPLIT_PARTS_GPU_METADATA)
    cargs = []
    cargs.append("split_parts_gpu")
    cargs.append(execution.input_file(datafile))
    cargs.append(execution.input_file(maskfile))
    cargs.append(execution.input_file(bvals_file))
    cargs.append(execution.input_file(bvecs_file))
    if grad_file is not None:
        cargs.append(grad_file)
    cargs.append(str(use_grad_file))
    cargs.append(str(total_num_parts))
    cargs.append(output_directory)
    ret = SplitPartsGpuOutputs(
        root=execution.output_file("."),
        output_parts=execution.output_file(f"{output_directory}/part_*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPLIT_PARTS_GPU_METADATA",
    "SplitPartsGpuOutputs",
    "split_parts_gpu",
]