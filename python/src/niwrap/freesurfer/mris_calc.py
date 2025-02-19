# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CALC_METADATA = Metadata(
    id="0f04865341178eeb624695b7ff33be523bb926b5.boutiques",
    name="mris_calc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisCalcParameters = typing.TypedDict('MrisCalcParameters', {
    "__STYX_TYPE__": typing.Literal["mris_calc"],
    "input_file1": InputPathType,
    "action": str,
    "input_file2_or_float": typing.NotRequired[InputPathType | None],
    "output_file": typing.NotRequired[str | None],
    "label_file": typing.NotRequired[InputPathType | None],
    "verbosity": typing.NotRequired[str | None],
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
        "mris_calc": mris_calc_cargs,
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
        "mris_calc": mris_calc_outputs,
    }.get(t)


class MrisCalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_calc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_curv_file: OutputPathType | None
    """The resulting FreeSurfer curvature overlay or volume file."""


def mris_calc_params(
    input_file1: InputPathType,
    action: str,
    input_file2_or_float: InputPathType | None = None,
    output_file: str | None = None,
    label_file: InputPathType | None = None,
    verbosity: str | None = None,
) -> MrisCalcParameters:
    """
    Build parameters.
    
    Args:
        input_file1: The name of a FreeSurfer curvature overlay (e.g., rh.curv)\
            or volume file (e.g., orig.mgz).
        action: Mathematical action to perform on the input file(s), written as\
            a text string.
        input_file2_or_float: The second input for the calculation. Can be a\
            file (e.g., rh.thickness) or a float number if the file does not exist.
        output_file: Specify the output file name for the result of the\
            calculation.
        label_file: Constrain the calculation to vertices defined in the\
            FreeSurfer label file.
        verbosity: Set the verbosity of the program.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_calc",
        "input_file1": input_file1,
        "action": action,
    }
    if input_file2_or_float is not None:
        params["input_file2_or_float"] = input_file2_or_float
    if output_file is not None:
        params["output_file"] = output_file
    if label_file is not None:
        params["label_file"] = label_file
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def mris_calc_cargs(
    params: MrisCalcParameters,
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
    cargs.append("mris_calc")
    cargs.append(execution.input_file(params.get("input_file1")))
    cargs.append(params.get("action"))
    if params.get("input_file2_or_float") is not None:
        cargs.append(execution.input_file(params.get("input_file2_or_float")))
    if params.get("output_file") is not None:
        cargs.extend([
            "--output",
            params.get("output_file")
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("verbosity") is not None:
        cargs.extend([
            "--verbosity",
            params.get("verbosity")
        ])
    return cargs


def mris_calc_outputs(
    params: MrisCalcParameters,
    execution: Execution,
) -> MrisCalcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCalcOutputs(
        root=execution.output_file("."),
        output_curv_file=execution.output_file(params.get("output_file")) if (params.get("output_file") is not None) else None,
    )
    return ret


def mris_calc_execute(
    params: MrisCalcParameters,
    execution: Execution,
) -> MrisCalcOutputs:
    """
    Simple calculator that operates on FreeSurfer curvatures and volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCalcOutputs`).
    """
    params = execution.params(params)
    cargs = mris_calc_cargs(params, execution)
    ret = mris_calc_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_calc(
    input_file1: InputPathType,
    action: str,
    input_file2_or_float: InputPathType | None = None,
    output_file: str | None = None,
    label_file: InputPathType | None = None,
    verbosity: str | None = None,
    runner: Runner | None = None,
) -> MrisCalcOutputs:
    """
    Simple calculator that operates on FreeSurfer curvatures and volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file1: The name of a FreeSurfer curvature overlay (e.g., rh.curv)\
            or volume file (e.g., orig.mgz).
        action: Mathematical action to perform on the input file(s), written as\
            a text string.
        input_file2_or_float: The second input for the calculation. Can be a\
            file (e.g., rh.thickness) or a float number if the file does not exist.
        output_file: Specify the output file name for the result of the\
            calculation.
        label_file: Constrain the calculation to vertices defined in the\
            FreeSurfer label file.
        verbosity: Set the verbosity of the program.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CALC_METADATA)
    params = mris_calc_params(input_file1=input_file1, action=action, input_file2_or_float=input_file2_or_float, output_file=output_file, label_file=label_file, verbosity=verbosity)
    return mris_calc_execute(params, execution)


__all__ = [
    "MRIS_CALC_METADATA",
    "MrisCalcOutputs",
    "MrisCalcParameters",
    "mris_calc",
    "mris_calc_params",
]
