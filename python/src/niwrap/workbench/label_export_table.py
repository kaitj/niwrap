# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="aa538a6947b1a8c4309745c17b03fe0e989c4686.boutiques",
    name="label-export-table",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
LabelExportTableParameters = typing.TypedDict('LabelExportTableParameters', {
    "__STYX_TYPE__": typing.Literal["label-export-table"],
    "label_in": InputPathType,
    "table_out": str,
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
        "label-export-table": label_export_table_cargs,
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
    }.get(t)


class LabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_export_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def label_export_table_params(
    label_in: InputPathType,
    table_out: str,
) -> LabelExportTableParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input label file.
        table_out: output - the output text file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label-export-table",
        "label_in": label_in,
        "table_out": table_out,
    }
    return params


def label_export_table_cargs(
    params: LabelExportTableParameters,
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
    cargs.append("wb_command")
    cargs.append("-label-export-table")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("table_out"))
    return cargs


def label_export_table_outputs(
    params: LabelExportTableParameters,
    execution: Execution,
) -> LabelExportTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LabelExportTableOutputs(
        root=execution.output_file("."),
    )
    return ret


def label_export_table_execute(
    params: LabelExportTableParameters,
    execution: Execution,
) -> LabelExportTableOutputs:
    """
    Export label table from gifti as text.
    
    Takes the label table from the gifti label file, and writes it to a text
    format matching what is expected by -metric-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LabelExportTableOutputs`).
    """
    params = execution.params(params)
    cargs = label_export_table_cargs(params, execution)
    ret = label_export_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def label_export_table(
    label_in: InputPathType,
    table_out: str,
    runner: Runner | None = None,
) -> LabelExportTableOutputs:
    """
    Export label table from gifti as text.
    
    Takes the label table from the gifti label file, and writes it to a text
    format matching what is expected by -metric-label-import.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input label file.
        table_out: output - the output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelExportTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_EXPORT_TABLE_METADATA)
    params = label_export_table_params(label_in=label_in, table_out=table_out)
    return label_export_table_execute(params, execution)


__all__ = [
    "LABEL_EXPORT_TABLE_METADATA",
    "LabelExportTableOutputs",
    "LabelExportTableParameters",
    "label_export_table",
    "label_export_table_params",
]
