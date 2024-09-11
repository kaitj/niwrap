# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DMERGE_METADATA = Metadata(
    id="9f01ea10771b0203e54683725aa61c74654978d7.boutiques",
    name="3dmerge",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset file"""


def v_3dmerge(
    input_files: list[InputPathType],
    output_file: str,
    runner: Runner | None = None,
) -> V3dmergeOutputs:
    """
    3dmerge edits and merges 3D datasets by applying various operations like
    thresholding, blurring, clustering, and more.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmerge.html
    
    Args:
        input_files: Input dataset files.
        output_file: Output dataset prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMERGE_METADATA)
    cargs = []
    cargs.append("3dmerge")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.append("[EDITING_OPTIONS]")
    cargs.append("[MERGING_OPTIONS]")
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        output_file
    ])
    ret = V3dmergeOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmergeOutputs",
    "V_3DMERGE_METADATA",
    "v_3dmerge",
]