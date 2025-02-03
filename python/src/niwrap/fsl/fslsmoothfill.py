# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLSMOOTHFILL_METADATA = Metadata(
    id="decfe9aa72638e1ec65326903fe3b064f1752e01.boutiques",
    name="fslsmoothfill",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslsmoothfillParameters = typing.TypedDict('FslsmoothfillParameters', {
    "__STYX_TYPE__": typing.Literal["fslsmoothfill"],
    "input_image": InputPathType,
    "mask_image": InputPathType,
    "output_image": str,
    "number_of_iterations": typing.NotRequired[int | None],
    "debug_flag": bool,
    "verbose_flag": bool,
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
        "fslsmoothfill": fslsmoothfill_cargs,
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
    vt = {}
    return vt.get(t)


def fslsmoothfill_params(
    input_image: InputPathType,
    mask_image: InputPathType,
    output_image: str,
    number_of_iterations: int | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
) -> FslsmoothfillParameters:
    """
    Build parameters.
    
    Args:
        input_image: Filename of the input image.
        mask_image: Filename of the mask image.
        output_image: Filename for the output smoothed result image.
        number_of_iterations: Number of iterations.
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslsmoothfill",
        "input_image": input_image,
        "mask_image": mask_image,
        "output_image": output_image,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
    }
    if number_of_iterations is not None:
        params["number_of_iterations"] = number_of_iterations
    return params


def fslsmoothfill_cargs(
    params: FslsmoothfillParameters,
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
    cargs.append("fslsmoothfill")
    cargs.append("-i")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_image"))
    ])
    cargs.append("-m")
    cargs.extend([
        "--mask",
        execution.input_file(params.get("mask_image"))
    ])
    cargs.append("-o")
    cargs.extend([
        "--out",
        params.get("output_image")
    ])
    if params.get("number_of_iterations") is not None:
        cargs.extend([
            "--niter",
            str(params.get("number_of_iterations"))
        ])
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    return cargs


def fslsmoothfill_outputs(
    params: FslsmoothfillParameters,
    execution: Execution,
) -> FslsmoothfillOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslsmoothfillOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslsmoothfill_execute(
    params: FslsmoothfillParameters,
    execution: Execution,
) -> FslsmoothfillOutputs:
    """
    Smoothfill is a tool designed to fill in holes in images by smoothly
    interpolating the pixel values.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslsmoothfillOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslsmoothfill_cargs(params, execution)
    ret = fslsmoothfill_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslsmoothfill(
    input_image: InputPathType,
    mask_image: InputPathType,
    output_image: str,
    number_of_iterations: int | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FslsmoothfillOutputs:
    """
    Smoothfill is a tool designed to fill in holes in images by smoothly
    interpolating the pixel values.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Filename of the input image.
        mask_image: Filename of the mask image.
        output_image: Filename for the output smoothed result image.
        number_of_iterations: Number of iterations.
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsmoothfillOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSMOOTHFILL_METADATA)
    params = fslsmoothfill_params(input_image=input_image, mask_image=mask_image, output_image=output_image, number_of_iterations=number_of_iterations, debug_flag=debug_flag, verbose_flag=verbose_flag)
    return fslsmoothfill_execute(params, execution)


__all__ = [
    "FSLSMOOTHFILL_METADATA",
    "fslsmoothfill",
    "fslsmoothfill_params",
]
