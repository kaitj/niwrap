# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IREPIFITVOL_GLNX64_METADATA = Metadata(
    id="e1b3c71003d88eeb91c6bc522cbeb9c8dec5641d.boutiques",
    name="irepifitvol.glnx64",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
IrepifitvolGlnx64Parameters = typing.TypedDict('IrepifitvolGlnx64Parameters', {
    "__STYX_TYPE__": typing.Literal["irepifitvol.glnx64"],
    "input_file": InputPathType,
    "output_file": str,
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
        "irepifitvol.glnx64": irepifitvol_glnx64_cargs,
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
        "irepifitvol.glnx64": irepifitvol_glnx64_outputs,
    }
    return vt.get(t)


class IrepifitvolGlnx64Outputs(typing.NamedTuple):
    """
    Output object returned when calling `irepifitvol_glnx64(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """The fitted volume output from the irepifitvol process."""


def irepifitvol_glnx64_params(
    input_file: InputPathType,
    output_file: str,
) -> IrepifitvolGlnx64Parameters:
    """
    Build parameters.
    
    Args:
        input_file: The input volume file to be processed.
        output_file: The path to save the output volume file after fitting.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "irepifitvol.glnx64",
        "input_file": input_file,
        "output_file": output_file,
    }
    return params


def irepifitvol_glnx64_cargs(
    params: IrepifitvolGlnx64Parameters,
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
    cargs.append("irepifitvol")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    return cargs


def irepifitvol_glnx64_outputs(
    params: IrepifitvolGlnx64Parameters,
    execution: Execution,
) -> IrepifitvolGlnx64Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = IrepifitvolGlnx64Outputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_file")),
    )
    return ret


def irepifitvol_glnx64_execute(
    params: IrepifitvolGlnx64Parameters,
    execution: Execution,
) -> IrepifitvolGlnx64Outputs:
    """
    This tool is a part of the FreeSurfer toolkit, designed for certain volume
    fitting tasks.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `IrepifitvolGlnx64Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = irepifitvol_glnx64_cargs(params, execution)
    ret = irepifitvol_glnx64_outputs(params, execution)
    execution.run(cargs)
    return ret


def irepifitvol_glnx64(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> IrepifitvolGlnx64Outputs:
    """
    This tool is a part of the FreeSurfer toolkit, designed for certain volume
    fitting tasks.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: The input volume file to be processed.
        output_file: The path to save the output volume file after fitting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IrepifitvolGlnx64Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IREPIFITVOL_GLNX64_METADATA)
    params = irepifitvol_glnx64_params(input_file=input_file, output_file=output_file)
    return irepifitvol_glnx64_execute(params, execution)


__all__ = [
    "IREPIFITVOL_GLNX64_METADATA",
    "IrepifitvolGlnx64Outputs",
    "irepifitvol_glnx64",
    "irepifitvol_glnx64_params",
]
