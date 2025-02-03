# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICEANIMATE_METADATA = Metadata(
    id="05268b7eca1ce9802cba56c1e5171a4d5003db1c.boutiques",
    name="sliceanimate",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SliceanimateParameters = typing.TypedDict('SliceanimateParameters', {
    "__STYX_TYPE__": typing.Literal["sliceanimate"],
    "output_file": str,
    "input_files": list[InputPathType],
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
        "sliceanimate": sliceanimate_cargs,
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
        "sliceanimate": sliceanimate_outputs,
    }
    return vt.get(t)


class SliceanimateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sliceanimate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    animated_gif: OutputPathType
    """Generated animated GIF"""


def sliceanimate_params(
    output_file: str,
    input_files: list[InputPathType],
) -> SliceanimateParameters:
    """
    Build parameters.
    
    Args:
        output_file: Output animated GIF file.
        input_files: Input image files for animation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sliceanimate",
        "output_file": output_file,
        "input_files": input_files,
    }
    return params


def sliceanimate_cargs(
    params: SliceanimateParameters,
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
    cargs.append("sliceanimate")
    cargs.append(params.get("output_file"))
    cargs.append("--")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    return cargs


def sliceanimate_outputs(
    params: SliceanimateParameters,
    execution: Execution,
) -> SliceanimateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SliceanimateOutputs(
        root=execution.output_file("."),
        animated_gif=execution.output_file(params.get("output_file")),
    )
    return ret


def sliceanimate_execute(
    params: SliceanimateParameters,
    execution: Execution,
) -> SliceanimateOutputs:
    """
    A tool for animating slices of an image using whirlgif.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SliceanimateOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sliceanimate_cargs(params, execution)
    ret = sliceanimate_outputs(params, execution)
    execution.run(cargs)
    return ret


def sliceanimate(
    output_file: str,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> SliceanimateOutputs:
    """
    A tool for animating slices of an image using whirlgif.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output_file: Output animated GIF file.
        input_files: Input image files for animation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SliceanimateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICEANIMATE_METADATA)
    params = sliceanimate_params(output_file=output_file, input_files=input_files)
    return sliceanimate_execute(params, execution)


__all__ = [
    "SLICEANIMATE_METADATA",
    "SliceanimateOutputs",
    "sliceanimate",
    "sliceanimate_params",
]
