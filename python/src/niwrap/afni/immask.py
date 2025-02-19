# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMMASK_METADATA = Metadata(
    id="9c1f93c0cb09202023e9490b9f3feb5a319f6f59.boutiques",
    name="immask",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ImmaskParameters = typing.TypedDict('ImmaskParameters', {
    "__STYX_TYPE__": typing.Literal["immask"],
    "threshold": typing.NotRequired[float | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "positive_only": bool,
    "input_image": InputPathType,
    "output_image": str,
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
        "immask": immask_cargs,
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
        "immask": immask_outputs,
    }.get(t)


class ImmaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `immask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Masked output image"""


def immask_params(
    input_image: InputPathType,
    output_image: str,
    threshold: float | None = None,
    mask_image: InputPathType | None = None,
    positive_only: bool = False,
) -> ImmaskParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image to be masked.
        output_image: Output image after masking.
        threshold: Threshold value; all pixels with absolute value below this\
            will be set to zero in the output image.
        mask_image: Mask image; only locations that are nonzero in the mask\
            image will be nonzero in the output image.
        positive_only: Use only positive pixels from input image.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "immask",
        "positive_only": positive_only,
        "input_image": input_image,
        "output_image": output_image,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if mask_image is not None:
        params["mask_image"] = mask_image
    return params


def immask_cargs(
    params: ImmaskParameters,
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
    cargs.append("immask")
    if params.get("threshold") is not None:
        cargs.extend([
            "-thresh",
            str(params.get("threshold"))
        ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("positive_only"):
        cargs.append("-pos")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_image"))
    return cargs


def immask_outputs(
    params: ImmaskParameters,
    execution: Execution,
) -> ImmaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ImmaskOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_image")),
    )
    return ret


def immask_execute(
    params: ImmaskParameters,
    execution: Execution,
) -> ImmaskOutputs:
    """
    Masks the input image based on specified criteria and produces the output image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ImmaskOutputs`).
    """
    params = execution.params(params)
    cargs = immask_cargs(params, execution)
    ret = immask_outputs(params, execution)
    execution.run(cargs)
    return ret


def immask(
    input_image: InputPathType,
    output_image: str,
    threshold: float | None = None,
    mask_image: InputPathType | None = None,
    positive_only: bool = False,
    runner: Runner | None = None,
) -> ImmaskOutputs:
    """
    Masks the input image based on specified criteria and produces the output image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_image: Input image to be masked.
        output_image: Output image after masking.
        threshold: Threshold value; all pixels with absolute value below this\
            will be set to zero in the output image.
        mask_image: Mask image; only locations that are nonzero in the mask\
            image will be nonzero in the output image.
        positive_only: Use only positive pixels from input image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImmaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMMASK_METADATA)
    params = immask_params(threshold=threshold, mask_image=mask_image, positive_only=positive_only, input_image=input_image, output_image=output_image)
    return immask_execute(params, execution)


__all__ = [
    "IMMASK_METADATA",
    "ImmaskOutputs",
    "ImmaskParameters",
    "immask",
    "immask_params",
]
