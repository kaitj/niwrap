# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_LABEL_TO_BORDER_METADATA = Metadata(
    id="53bedd57bdb1ef00cc2cb7f6b84a5ebd39af4a72",
    name="cifti-label-to-border",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelToBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_to_border(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_label_to_border(
    runner: Runner,
    cifti_in: InputPathType,
    opt_placement_fraction: float | int | None = None,
    opt_column_column: str | None = None,
    opt_border_surface: InputPathType | None = None,
) -> CiftiLabelToBorderOutputs:
    """
    DRAW BORDERS AROUND CIFTI LABELS.
    
    For each surface, takes the labels on the matching structure and draws
    borders around the labels. Use -column to only draw borders around one label
    map.
    
    Args:
        runner: Command runner
        cifti_in: the input cifti dlabel file
        opt_placement_fraction: set how far along the edge border points are
            drawn: fraction along edge from inside vertex (default 0.33)
        opt_column_column: select a single column: the column number or name
        opt_border_surface: specify output file for a surface structure: the
            surface to use for neighbor and structure information
    Returns:
        NamedTuple of outputs (described in `CiftiLabelToBorderOutputs`).
    """
    execution = runner.start_execution(CIFTI_LABEL_TO_BORDER_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-to-border")
    cargs.append(execution.input_file(cifti_in))
    if opt_placement_fraction is not None:
        cargs.extend(["-placement", str(opt_placement_fraction)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_border_surface is not None:
        cargs.extend(["-border", execution.input_file(opt_border_surface)])
    ret = CiftiLabelToBorderOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
