# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


LABEL_MASK_METADATA = Metadata(
    id="f5f87079f541ccf6eb3c4babb5c69a0082bf1e30",
    name="label-mask",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def label_mask(
    label: InputPathType,
    mask: InputPathType,
    label_out: InputPathType,
    opt_column_column: str | None = None,
    runner: Runner = None,
) -> LabelMaskOutputs:
    """
    label-mask by Washington University School of Medicin.
    
    MASK A LABEL FILE.
    
    By default, the output label is a copy of the input label, but with the
    'unused' label wherever the mask metric is zero or negative. if -column is
    specified, the output contains only one column, the masked version of the
    specified input column.
    
    Args:
        label: the label file to mask
        mask: the mask metric
        label_out: the output label file
        opt_column_column: select a single column: the column number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `LabelMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MASK_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-mask")
    cargs.append(execution.input_file(label))
    cargs.append(execution.input_file(mask))
    cargs.append(execution.input_file(label_out))
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = LabelMaskOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{pathlib.Path(label_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL_MASK_METADATA",
    "LabelMaskOutputs",
    "label_mask",
]
