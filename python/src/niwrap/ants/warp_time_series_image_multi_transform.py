# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA = Metadata(
    id="02d7706a3d3c92924bed3c01a243b77e5b1a013b.boutiques",
    name="WarpTimeSeriesImageMultiTransform",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
WarpTimeSeriesImageMultiTransformParameters = typing.TypedDict('WarpTimeSeriesImageMultiTransformParameters', {
    "__STYX_TYPE__": typing.Literal["WarpTimeSeriesImageMultiTransform"],
    "image_dimension": typing.Literal[3, 4],
    "moving_image": InputPathType,
    "output_image": str,
    "reference_image": InputPathType,
    "transforms": list[str],
    "interpolation": typing.NotRequired[typing.Literal["NearestNeighbor", "BSpline"] | None],
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
        "WarpTimeSeriesImageMultiTransform": warp_time_series_image_multi_transform_cargs,
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
        "WarpTimeSeriesImageMultiTransform": warp_time_series_image_multi_transform_outputs,
    }
    return vt.get(t)


class WarpTimeSeriesImageMultiTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warp_time_series_image_multi_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_result: OutputPathType
    """The transformed image that is saved as output."""


def warp_time_series_image_multi_transform_params(
    image_dimension: typing.Literal[3, 4],
    moving_image: InputPathType,
    output_image: str,
    reference_image: InputPathType,
    transforms: list[str],
    interpolation: typing.Literal["NearestNeighbor", "BSpline"] | None = None,
) -> WarpTimeSeriesImageMultiTransformParameters:
    """
    Build parameters.
    
    Args:
        image_dimension: The dimensionality of the input images (3D or 4D).
        moving_image: The image to which the transformation will be applied. It\
            can be a 3D image with vector voxels or a 4D image with scalar voxels.
        output_image: The output image after transformation. It is resampled\
            based on the reference image domain.
        reference_image: The reference image that defines the space into which\
            the input image will be warped.
        transforms: A list of transformation files, such as affine\
            transformation matrices and warps, applied in sequence.
        interpolation: Specifies the type of interpolation to use: Nearest\
            Neighbor or 3rd order B-Spline.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "WarpTimeSeriesImageMultiTransform",
        "image_dimension": image_dimension,
        "moving_image": moving_image,
        "output_image": output_image,
        "reference_image": reference_image,
        "transforms": transforms,
    }
    if interpolation is not None:
        params["interpolation"] = interpolation
    return params


def warp_time_series_image_multi_transform_cargs(
    params: WarpTimeSeriesImageMultiTransformParameters,
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
    cargs.append("WarpTimeSeriesImageMultiTransform")
    cargs.append(str(params.get("image_dimension")))
    cargs.append(execution.input_file(params.get("moving_image")))
    cargs.append(params.get("output_image"))
    cargs.extend([
        "-R",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend(params.get("transforms"))
    if params.get("interpolation") is not None:
        cargs.append(params.get("interpolation"))
    return cargs


def warp_time_series_image_multi_transform_outputs(
    params: WarpTimeSeriesImageMultiTransformParameters,
    execution: Execution,
) -> WarpTimeSeriesImageMultiTransformOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WarpTimeSeriesImageMultiTransformOutputs(
        root=execution.output_file("."),
        output_image_result=execution.output_file(params.get("output_image")),
    )
    return ret


def warp_time_series_image_multi_transform_execute(
    params: WarpTimeSeriesImageMultiTransformParameters,
    execution: Execution,
) -> WarpTimeSeriesImageMultiTransformOutputs:
    """
    WarpTimeSeriesImageMultiTransform is a tool used to apply a series of
    transformations to a time series image, either forward or reverse, using affine
    transforms and warps.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WarpTimeSeriesImageMultiTransformOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = warp_time_series_image_multi_transform_cargs(params, execution)
    ret = warp_time_series_image_multi_transform_outputs(params, execution)
    execution.run(cargs)
    return ret


def warp_time_series_image_multi_transform(
    image_dimension: typing.Literal[3, 4],
    moving_image: InputPathType,
    output_image: str,
    reference_image: InputPathType,
    transforms: list[str],
    interpolation: typing.Literal["NearestNeighbor", "BSpline"] | None = None,
    runner: Runner | None = None,
) -> WarpTimeSeriesImageMultiTransformOutputs:
    """
    WarpTimeSeriesImageMultiTransform is a tool used to apply a series of
    transformations to a time series image, either forward or reverse, using affine
    transforms and warps.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input images (3D or 4D).
        moving_image: The image to which the transformation will be applied. It\
            can be a 3D image with vector voxels or a 4D image with scalar voxels.
        output_image: The output image after transformation. It is resampled\
            based on the reference image domain.
        reference_image: The reference image that defines the space into which\
            the input image will be warped.
        transforms: A list of transformation files, such as affine\
            transformation matrices and warps, applied in sequence.
        interpolation: Specifies the type of interpolation to use: Nearest\
            Neighbor or 3rd order B-Spline.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WarpTimeSeriesImageMultiTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA)
    params = warp_time_series_image_multi_transform_params(image_dimension=image_dimension, moving_image=moving_image, output_image=output_image, reference_image=reference_image, transforms=transforms, interpolation=interpolation)
    return warp_time_series_image_multi_transform_execute(params, execution)


__all__ = [
    "WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA",
    "WarpTimeSeriesImageMultiTransformOutputs",
    "warp_time_series_image_multi_transform",
    "warp_time_series_image_multi_transform_params",
]
