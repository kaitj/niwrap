# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SLICES_METADATA = Metadata(
    id="a8594492356fc058a9bcf77bee3fdf328139290d.boutiques",
    name="slices",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
SlicesParameters = typing.TypedDict('SlicesParameters', {
    "__STYX_TYPE__": typing.Literal["slices"],
    "primary_input": InputPathType,
    "secondary_input": typing.NotRequired[InputPathType | None],
    "scale_factor": typing.NotRequired[float | None],
    "intensity_range": typing.NotRequired[list[float] | None],
    "output_gif": typing.NotRequired[str | None],
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
        "slices": slices_cargs,
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


class SlicesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slices(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slices_params(
    primary_input: InputPathType,
    secondary_input: InputPathType | None = None,
    scale_factor: float | None = None,
    intensity_range: list[float] | None = None,
    output_gif: str | None = None,
) -> SlicesParameters:
    """
    Build parameters.
    
    Args:
        primary_input: Primary input image file (e.g. img1.nii.gz).
        secondary_input: Secondary input image file (e.g. img2.nii.gz).
        scale_factor: Scale factor to apply to images.
        intensity_range: Intensity range to consider (minimum and maximum\
            values).
        output_gif: Output GIF file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "slices",
        "primary_input": primary_input,
    }
    if secondary_input is not None:
        params["secondary_input"] = secondary_input
    if scale_factor is not None:
        params["scale_factor"] = scale_factor
    if intensity_range is not None:
        params["intensity_range"] = intensity_range
    if output_gif is not None:
        params["output_gif"] = output_gif
    return params


def slices_cargs(
    params: SlicesParameters,
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
    cargs.append("slices")
    cargs.append(execution.input_file(params.get("primary_input")))
    if params.get("secondary_input") is not None:
        cargs.append(execution.input_file(params.get("secondary_input")))
    if params.get("scale_factor") is not None:
        cargs.extend([
            "-s",
            str(params.get("scale_factor"))
        ])
    if params.get("intensity_range") is not None:
        cargs.extend([
            "-i",
            *map(str, params.get("intensity_range"))
        ])
    if params.get("output_gif") is not None:
        cargs.extend([
            "-o",
            params.get("output_gif")
        ])
    return cargs


def slices_outputs(
    params: SlicesParameters,
    execution: Execution,
) -> SlicesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SlicesOutputs(
        root=execution.output_file("."),
    )
    return ret


def slices_execute(
    params: SlicesParameters,
    execution: Execution,
) -> SlicesOutputs:
    """
    Generate a set of slices from an image, possibly with some scaling and intensity
    range options, and save as a GIF.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SlicesOutputs`).
    """
    params = execution.params(params)
    cargs = slices_cargs(params, execution)
    ret = slices_outputs(params, execution)
    execution.run(cargs)
    return ret


def slices(
    primary_input: InputPathType,
    secondary_input: InputPathType | None = None,
    scale_factor: float | None = None,
    intensity_range: list[float] | None = None,
    output_gif: str | None = None,
    runner: Runner | None = None,
) -> SlicesOutputs:
    """
    Generate a set of slices from an image, possibly with some scaling and intensity
    range options, and save as a GIF.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        primary_input: Primary input image file (e.g. img1.nii.gz).
        secondary_input: Secondary input image file (e.g. img2.nii.gz).
        scale_factor: Scale factor to apply to images.
        intensity_range: Intensity range to consider (minimum and maximum\
            values).
        output_gif: Output GIF file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICES_METADATA)
    params = slices_params(primary_input=primary_input, secondary_input=secondary_input, scale_factor=scale_factor, intensity_range=intensity_range, output_gif=output_gif)
    return slices_execute(params, execution)


__all__ = [
    "SLICES_METADATA",
    "SlicesOutputs",
    "SlicesParameters",
    "slices",
    "slices_params",
]
