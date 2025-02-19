# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

EXTRACT_REGION_FROM_IMAGE_BY_MASK_METADATA = Metadata(
    id="aec2f60db8048987a495410600ad2f857750da61.boutiques",
    name="ExtractRegionFromImageByMask",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
ExtractRegionFromImageByMaskParameters = typing.TypedDict('ExtractRegionFromImageByMaskParameters', {
    "__STYX_TYPE__": typing.Literal["ExtractRegionFromImageByMask"],
    "image_dimension": int,
    "input_image": InputPathType,
    "output_image": InputPathType,
    "label_mask_image": InputPathType,
    "label": typing.NotRequired[int | None],
    "pad_radius": typing.NotRequired[int | None],
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
        "ExtractRegionFromImageByMask": extract_region_from_image_by_mask_cargs,
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


class ExtractRegionFromImageByMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `extract_region_from_image_by_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def extract_region_from_image_by_mask_params(
    image_dimension: int,
    input_image: InputPathType,
    output_image: InputPathType,
    label_mask_image: InputPathType,
    label: int | None = 1,
    pad_radius: int | None = 0,
) -> ExtractRegionFromImageByMaskParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: Dimension of the input image.
        input_image: The input image from which a region will be extracted.
        output_image: The output image containing the extracted region.
        label_mask_image: The label mask image used to extract the bounding\
            box.
        label: The label value used to extract the sub-region.
        pad_radius: Optional padding radius to be added around the bounding\
            box.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ExtractRegionFromImageByMask",
        "image_dimension": image_dimension,
        "input_image": input_image,
        "output_image": output_image,
        "label_mask_image": label_mask_image,
    }
    if label is not None:
        params["label"] = label
    if pad_radius is not None:
        params["pad_radius"] = pad_radius
    return params


def extract_region_from_image_by_mask_cargs(
    params: ExtractRegionFromImageByMaskParameters,
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
    cargs.append("ExtractRegionFromImageByMask")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(execution.input_file(params.get("output_image")))
    cargs.append(execution.input_file(params.get("label_mask_image")))
    if params.get("label") is not None:
        cargs.append(str(params.get("label")))
    if params.get("pad_radius") is not None:
        cargs.append(str(params.get("pad_radius")))
    return cargs


def extract_region_from_image_by_mask_outputs(
    params: ExtractRegionFromImageByMaskParameters,
    execution: Execution,
) -> ExtractRegionFromImageByMaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ExtractRegionFromImageByMaskOutputs(
        root=execution.output_file("."),
    )
    return ret


def extract_region_from_image_by_mask_execute(
    params: ExtractRegionFromImageByMaskParameters,
    execution: Execution,
) -> ExtractRegionFromImageByMaskOutputs:
    """
    Extract a sub-region from an image using the bounding box from a label image,
    with an optional padding radius.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ExtractRegionFromImageByMaskOutputs`).
    """
    params = execution.params(params)
    cargs = extract_region_from_image_by_mask_cargs(params, execution)
    ret = extract_region_from_image_by_mask_outputs(params, execution)
    execution.run(cargs)
    return ret


def extract_region_from_image_by_mask(
    image_dimension: int,
    input_image: InputPathType,
    output_image: InputPathType,
    label_mask_image: InputPathType,
    label: int | None = 1,
    pad_radius: int | None = 0,
    runner: Runner | None = None,
) -> ExtractRegionFromImageByMaskOutputs:
    """
    Extract a sub-region from an image using the bounding box from a label image,
    with an optional padding radius.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimension of the input image.
        input_image: The input image from which a region will be extracted.
        output_image: The output image containing the extracted region.
        label_mask_image: The label mask image used to extract the bounding\
            box.
        label: The label value used to extract the sub-region.
        pad_radius: Optional padding radius to be added around the bounding\
            box.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ExtractRegionFromImageByMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EXTRACT_REGION_FROM_IMAGE_BY_MASK_METADATA)
    params = extract_region_from_image_by_mask_params(image_dimension=image_dimension, input_image=input_image, output_image=output_image, label_mask_image=label_mask_image, label=label, pad_radius=pad_radius)
    return extract_region_from_image_by_mask_execute(params, execution)


__all__ = [
    "EXTRACT_REGION_FROM_IMAGE_BY_MASK_METADATA",
    "ExtractRegionFromImageByMaskOutputs",
    "ExtractRegionFromImageByMaskParameters",
    "extract_region_from_image_by_mask",
    "extract_region_from_image_by_mask_params",
]
