# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_RANKIZER_METADATA = Metadata(
    id="02a24acb7252cea4f3caac760b427edb414bac4b.boutiques",
    name="3dRankizer",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dRankizerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rankizer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output float-format dataset containing ranked voxel values"""


def v_3d_rankizer(
    dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dRankizerOutputs:
    """
    Tool to rank each voxel as sorted into increasing value. Ties get the average
    rank.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dRankizer.html
    
    Args:
        dataset: Input MRI dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRankizerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RANKIZER_METADATA)
    cargs = []
    cargs.append("3dRankizer")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dataset))
    ret = V3dRankizerOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file("[PPP]+tlrc.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dRankizerOutputs",
    "V_3D_RANKIZER_METADATA",
    "v_3d_rankizer",
]
