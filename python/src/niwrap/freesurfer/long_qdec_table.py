# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LONG_QDEC_TABLE_METADATA = Metadata(
    id="3e490486cd37e1e7aa6f857009bf74cde0ba7251.boutiques",
    name="long_qdec_table",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
LongQdecTableParameters = typing.TypedDict('LongQdecTableParameters', {
    "__STYX_TYPE__": typing.Literal["long_qdec_table"],
    "qdec_table": InputPathType,
    "split": typing.NotRequired[str | None],
    "cross_flag": bool,
    "sort": typing.NotRequired[str | None],
    "out": typing.NotRequired[str | None],
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
        "long_qdec_table": long_qdec_table_cargs,
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
        "long_qdec_table": long_qdec_table_outputs,
    }
    return vt.get(t)


class LongQdecTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_qdec_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType | None
    """Output table file generated by the specified operations"""


def long_qdec_table_params(
    qdec_table: InputPathType,
    split: str | None = None,
    cross_flag: bool = False,
    sort: str | None = None,
    out: str | None = None,
) -> LongQdecTableParameters:
    """
    Build parameters.
    
    Args:
        qdec_table: QDEC table file specifying the subjects and time points.
        split: Split table based on column (e.g., use 'fsid-base' to separate\
            subjects).
        cross_flag: Collapse table to cross sectional (one line per subject).
        sort: Sort table based on column within subject (e.g., 'age').
        out: Output file name for operations producing a single table.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "long_qdec_table",
        "qdec_table": qdec_table,
        "cross_flag": cross_flag,
    }
    if split is not None:
        params["split"] = split
    if sort is not None:
        params["sort"] = sort
    if out is not None:
        params["out"] = out
    return params


def long_qdec_table_cargs(
    params: LongQdecTableParameters,
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
    cargs.append("long_qdec_table")
    cargs.extend([
        "--qdec",
        execution.input_file(params.get("qdec_table"))
    ])
    if params.get("split") is not None:
        cargs.extend([
            "--split",
            params.get("split")
        ])
    if params.get("cross_flag"):
        cargs.append("--cross")
    if params.get("sort") is not None:
        cargs.extend([
            "--sort",
            params.get("sort")
        ])
    if params.get("out") is not None:
        cargs.extend([
            "--out",
            params.get("out")
        ])
    return cargs


def long_qdec_table_outputs(
    params: LongQdecTableParameters,
    execution: Execution,
) -> LongQdecTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LongQdecTableOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(params.get("out")) if (params.get("out") is not None) else None,
    )
    return ret


def long_qdec_table_execute(
    params: LongQdecTableParameters,
    execution: Execution,
) -> LongQdecTableOutputs:
    """
    Tool to operate on longitudinal QDEC tables.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LongQdecTableOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = long_qdec_table_cargs(params, execution)
    ret = long_qdec_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def long_qdec_table(
    qdec_table: InputPathType,
    split: str | None = None,
    cross_flag: bool = False,
    sort: str | None = None,
    out: str | None = None,
    runner: Runner | None = None,
) -> LongQdecTableOutputs:
    """
    Tool to operate on longitudinal QDEC tables.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec_table: QDEC table file specifying the subjects and time points.
        split: Split table based on column (e.g., use 'fsid-base' to separate\
            subjects).
        cross_flag: Collapse table to cross sectional (one line per subject).
        sort: Sort table based on column within subject (e.g., 'age').
        out: Output file name for operations producing a single table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongQdecTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_QDEC_TABLE_METADATA)
    params = long_qdec_table_params(qdec_table=qdec_table, split=split, cross_flag=cross_flag, sort=sort, out=out)
    return long_qdec_table_execute(params, execution)


__all__ = [
    "LONG_QDEC_TABLE_METADATA",
    "LongQdecTableOutputs",
    "long_qdec_table",
    "long_qdec_table_params",
]
