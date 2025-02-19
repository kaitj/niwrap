# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ANTS_ALIGN_ORIGIN_METADATA = Metadata(
    id="74cc71ee1dbe0d0c58e8719cd30215507f2ae81e.boutiques",
    name="antsAlignOrigin",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsAlignOriginParameters = typing.TypedDict('AntsAlignOriginParameters', {
    "__STYX_TYPE__": typing.Literal["antsAlignOrigin"],
    "dimensionality": typing.NotRequired[typing.Literal[2, 3] | None],
    "input": InputPathType,
    "reference_image": InputPathType,
    "output": str,
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
        "antsAlignOrigin": ants_align_origin_cargs,
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
        "antsAlignOrigin": ants_align_origin_outputs,
    }.get(t)


class AntsAlignOriginOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_align_origin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_image: OutputPathType
    """The output is the aligned image."""


def ants_align_origin_params(
    input_: InputPathType,
    reference_image: InputPathType,
    output: str,
    dimensionality: typing.Literal[2, 3] | None = None,
) -> AntsAlignOriginParameters:
    """
    Build parameters.
    
    Args:
        input_: Currently, the only input objects supported are image objects.\
            However, the current framework allows for warping of other objects such\
            as meshes and point sets.
        reference_image: For warping input images, the reference image defines\
            the spacing, origin, size, and direction of the output warped image.
        output: One can either output the warped image or, if the boolean is\
            set, one can print out the displacement field based on the composite\
            transform and the reference image.
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, antsWarp tries to infer\
            the dimensionality from the input image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsAlignOrigin",
        "input": input_,
        "reference_image": reference_image,
        "output": output,
    }
    if dimensionality is not None:
        params["dimensionality"] = dimensionality
    return params


def ants_align_origin_cargs(
    params: AntsAlignOriginParameters,
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
    cargs.append("antsAlignOrigin")
    if params.get("dimensionality") is not None:
        cargs.extend([
            "--dimensionality",
            str(params.get("dimensionality"))
        ])
    cargs.extend([
        "--input",
        execution.input_file(params.get("input"))
    ])
    cargs.extend([
        "--reference-image",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend([
        "--output",
        params.get("output")
    ])
    return cargs


def ants_align_origin_outputs(
    params: AntsAlignOriginParameters,
    execution: Execution,
) -> AntsAlignOriginOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsAlignOriginOutputs(
        root=execution.output_file("."),
        aligned_image=execution.output_file(params.get("output")),
    )
    return ret


def ants_align_origin_execute(
    params: AntsAlignOriginParameters,
    execution: Execution,
) -> AntsAlignOriginOutputs:
    """
    antsAlignOrigin, applied to an input image, transforms it according to a
    reference image and a transform (or a set of transforms).
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsAlignOriginOutputs`).
    """
    params = execution.params(params)
    cargs = ants_align_origin_cargs(params, execution)
    ret = ants_align_origin_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_align_origin(
    input_: InputPathType,
    reference_image: InputPathType,
    output: str,
    dimensionality: typing.Literal[2, 3] | None = None,
    runner: Runner | None = None,
) -> AntsAlignOriginOutputs:
    """
    antsAlignOrigin, applied to an input image, transforms it according to a
    reference image and a transform (or a set of transforms).
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        input_: Currently, the only input objects supported are image objects.\
            However, the current framework allows for warping of other objects such\
            as meshes and point sets.
        reference_image: For warping input images, the reference image defines\
            the spacing, origin, size, and direction of the output warped image.
        output: One can either output the warped image or, if the boolean is\
            set, one can print out the displacement field based on the composite\
            transform and the reference image.
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, antsWarp tries to infer\
            the dimensionality from the input image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsAlignOriginOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_ALIGN_ORIGIN_METADATA)
    params = ants_align_origin_params(dimensionality=dimensionality, input_=input_, reference_image=reference_image, output=output)
    return ants_align_origin_execute(params, execution)


__all__ = [
    "ANTS_ALIGN_ORIGIN_METADATA",
    "AntsAlignOriginOutputs",
    "AntsAlignOriginParameters",
    "ants_align_origin",
    "ants_align_origin_params",
]
