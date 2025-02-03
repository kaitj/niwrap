# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STATTABLEDIFF_METADATA = Metadata(
    id="1700b5a4affda702434ee9916d498190f06c350c.boutiques",
    name="stattablediff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
StattablediffParameters = typing.TypedDict('StattablediffParameters', {
    "__STYX_TYPE__": typing.Literal["stattablediff"],
    "t1": InputPathType,
    "t2": InputPathType,
    "output": str,
    "percent_diff": bool,
    "percent_diff_t1": bool,
    "percent_diff_t2": bool,
    "multiply": typing.NotRequired[float | None],
    "divide": typing.NotRequired[float | None],
    "common": bool,
    "remove_exvivo": bool,
    "diff_subjects": bool,
    "noreplace53": bool,
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
        "stattablediff": stattablediff_cargs,
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
        "stattablediff": stattablediff_outputs,
    }
    return vt.get(t)


class StattablediffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stattablediff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_diff_table: OutputPathType
    """Generated table of differences"""


def stattablediff_params(
    t1: InputPathType,
    t2: InputPathType,
    output: str,
    percent_diff: bool = False,
    percent_diff_t1: bool = False,
    percent_diff_t2: bool = False,
    multiply: float | None = None,
    divide: float | None = None,
    common: bool = False,
    remove_exvivo: bool = False,
    diff_subjects: bool = False,
    noreplace53: bool = False,
) -> StattablediffParameters:
    """
    Build parameters.
    
    Args:
        t1: Input table 1 (output of asegstats2table or aparcstats2table).
        t2: Input table 2 (output of asegstats2table or aparcstats2table).
        output: Output file for the table of differences.
        percent_diff: Compute percent difference with respect to mean of tables.
        percent_diff_t1: Compute percent difference with respect to table 1.
        percent_diff_t2: Compute percent difference with respect to table 2.
        multiply: Multiply by mulval.
        divide: Divide by divval.
        common: Compute difference on common segments (may reorder).
        remove_exvivo: Remove the string '_exvivo' from the column header.
        diff_subjects: Compare subjects with different names.
        noreplace53: Do not replace 5.3 structure names with later names.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stattablediff",
        "t1": t1,
        "t2": t2,
        "output": output,
        "percent_diff": percent_diff,
        "percent_diff_t1": percent_diff_t1,
        "percent_diff_t2": percent_diff_t2,
        "common": common,
        "remove_exvivo": remove_exvivo,
        "diff_subjects": diff_subjects,
        "noreplace53": noreplace53,
    }
    if multiply is not None:
        params["multiply"] = multiply
    if divide is not None:
        params["divide"] = divide
    return params


def stattablediff_cargs(
    params: StattablediffParameters,
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
    cargs.append("stattablediff")
    cargs.append(execution.input_file(params.get("t1")))
    cargs.append(execution.input_file(params.get("t2")))
    cargs.append(params.get("output"))
    if params.get("percent_diff"):
        cargs.append("--percent")
    if params.get("percent_diff_t1"):
        cargs.append("--percent1")
    if params.get("percent_diff_t2"):
        cargs.append("--percent2")
    if params.get("multiply") is not None:
        cargs.extend([
            "--mul",
            str(params.get("multiply"))
        ])
    if params.get("divide") is not None:
        cargs.extend([
            "--div",
            str(params.get("divide"))
        ])
    if params.get("common"):
        cargs.append("--common")
    if params.get("remove_exvivo"):
        cargs.append("--rm-exvivo")
    if params.get("diff_subjects"):
        cargs.append("--diff-subjs")
    if params.get("noreplace53"):
        cargs.append("--noreplace53")
    return cargs


def stattablediff_outputs(
    params: StattablediffParameters,
    execution: Execution,
) -> StattablediffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = StattablediffOutputs(
        root=execution.output_file("."),
        output_diff_table=execution.output_file(params.get("output")),
    )
    return ret


def stattablediff_execute(
    params: StattablediffParameters,
    execution: Execution,
) -> StattablediffOutputs:
    """
    Creates a table of the differences between two stats tables.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `StattablediffOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = stattablediff_cargs(params, execution)
    ret = stattablediff_outputs(params, execution)
    execution.run(cargs)
    return ret


def stattablediff(
    t1: InputPathType,
    t2: InputPathType,
    output: str,
    percent_diff: bool = False,
    percent_diff_t1: bool = False,
    percent_diff_t2: bool = False,
    multiply: float | None = None,
    divide: float | None = None,
    common: bool = False,
    remove_exvivo: bool = False,
    diff_subjects: bool = False,
    noreplace53: bool = False,
    runner: Runner | None = None,
) -> StattablediffOutputs:
    """
    Creates a table of the differences between two stats tables.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1: Input table 1 (output of asegstats2table or aparcstats2table).
        t2: Input table 2 (output of asegstats2table or aparcstats2table).
        output: Output file for the table of differences.
        percent_diff: Compute percent difference with respect to mean of tables.
        percent_diff_t1: Compute percent difference with respect to table 1.
        percent_diff_t2: Compute percent difference with respect to table 2.
        multiply: Multiply by mulval.
        divide: Divide by divval.
        common: Compute difference on common segments (may reorder).
        remove_exvivo: Remove the string '_exvivo' from the column header.
        diff_subjects: Compare subjects with different names.
        noreplace53: Do not replace 5.3 structure names with later names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StattablediffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STATTABLEDIFF_METADATA)
    params = stattablediff_params(t1=t1, t2=t2, output=output, percent_diff=percent_diff, percent_diff_t1=percent_diff_t1, percent_diff_t2=percent_diff_t2, multiply=multiply, divide=divide, common=common, remove_exvivo=remove_exvivo, diff_subjects=diff_subjects, noreplace53=noreplace53)
    return stattablediff_execute(params, execution)


__all__ = [
    "STATTABLEDIFF_METADATA",
    "StattablediffOutputs",
    "stattablediff",
    "stattablediff_params",
]
