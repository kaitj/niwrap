# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLCHFILETYPE_METADATA = Metadata(
    id="e5da91ed052295c7eb624ffec87c6d89c4506faf.boutiques",
    name="fslchfiletype",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslchfiletypeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslchfiletype(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output file with the new file type."""


def fslchfiletype(
    filetype: str,
    filename: InputPathType,
    filename2: str | None = None,
    runner: Runner | None = None,
) -> FslchfiletypeOutputs:
    """
    Tool to change the file type of an image file or copy it to a new file.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filetype: The type of the file to convert to. Valid values include:\
            ANALYZE, ANALYZE_GZ, NIFTI, NIFTI_GZ, NIFTI_PAIR, NIFTI_PAIR_GZ,\
            NIFTI2, NIFTI2_GZ, NIFTI2_PAIR, NIFTI2_PAIR_GZ.
        filename: The name of the input image file.
        filename2: The name of the output image file (optional).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslchfiletypeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLCHFILETYPE_METADATA)
    cargs = []
    cargs.append("fslchfiletype")
    cargs.append(filetype)
    cargs.append(execution.input_file(filename))
    if filename2 is not None:
        cargs.append(filename2)
    ret = FslchfiletypeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(filename2) if (filename2 is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLCHFILETYPE_METADATA",
    "FslchfiletypeOutputs",
    "fslchfiletype",
]
