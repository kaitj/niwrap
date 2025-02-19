# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_CURVATURE_METADATA = Metadata(
    id="47bd42166388900cd8ce701c63aa9324fd46a426.boutiques",
    name="SurfaceCurvature",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SurfaceCurvatureParameters = typing.TypedDict('SurfaceCurvatureParameters', {
    "__STYX_TYPE__": typing.Literal["SurfaceCurvature"],
    "filename_in": InputPathType,
    "filename_out": str,
    "sigma": float,
    "option": float,
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
        "SurfaceCurvature": surface_curvature_cargs,
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
        "SurfaceCurvature": surface_curvature_outputs,
    }.get(t)


class SurfaceCurvatureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_curvature(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """The processed image file."""


def surface_curvature_params(
    filename_in: InputPathType,
    filename_out: str,
    sigma: float,
    option: float,
) -> SurfaceCurvatureParameters:
    """
    Build parameters.
    
    Args:
        filename_in: The input image file in .nii format.
        filename_out: The output image file in .nii format.
        sigma: The sigma value for analysis.
        option: The operation mode: 0 for mean curvature, 5 for surface\
            characterization, 6 for Gaussian curvature, and 7 for surface area.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfaceCurvature",
        "filename_in": filename_in,
        "filename_out": filename_out,
        "sigma": sigma,
        "option": option,
    }
    return params


def surface_curvature_cargs(
    params: SurfaceCurvatureParameters,
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
    cargs.append("SurfaceCurvature" + execution.input_file(params.get("filename_in")) + params.get("filename_out") + str(params.get("sigma")) + str(params.get("option")))
    return cargs


def surface_curvature_outputs(
    params: SurfaceCurvatureParameters,
    execution: Execution,
) -> SurfaceCurvatureOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceCurvatureOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("filename_out")),
    )
    return ret


def surface_curvature_execute(
    params: SurfaceCurvatureParameters,
    execution: Execution,
) -> SurfaceCurvatureOutputs:
    """
    The Shape Operator for Differential Analysis of Images. It can operate on binary
    or gray scale images with various modes to see different effects.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceCurvatureOutputs`).
    """
    params = execution.params(params)
    cargs = surface_curvature_cargs(params, execution)
    ret = surface_curvature_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_curvature(
    filename_in: InputPathType,
    filename_out: str,
    sigma: float,
    option: float,
    runner: Runner | None = None,
) -> SurfaceCurvatureOutputs:
    """
    The Shape Operator for Differential Analysis of Images. It can operate on binary
    or gray scale images with various modes to see different effects.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        filename_in: The input image file in .nii format.
        filename_out: The output image file in .nii format.
        sigma: The sigma value for analysis.
        option: The operation mode: 0 for mean curvature, 5 for surface\
            characterization, 6 for Gaussian curvature, and 7 for surface area.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCurvatureOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CURVATURE_METADATA)
    params = surface_curvature_params(filename_in=filename_in, filename_out=filename_out, sigma=sigma, option=option)
    return surface_curvature_execute(params, execution)


__all__ = [
    "SURFACE_CURVATURE_METADATA",
    "SurfaceCurvatureOutputs",
    "SurfaceCurvatureParameters",
    "surface_curvature",
    "surface_curvature_params",
]
