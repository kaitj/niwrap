# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_REGISTRATION_SY_NQUICK_SH_METADATA = Metadata(
    id="95f42ebdf9e80a10a0b738811253de777466a830.boutiques",
    name="antsRegistrationSyNQuick.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsRegistrationSyNquickShParameters = typing.TypedDict('AntsRegistrationSyNquickShParameters', {
    "__STYX_TYPE__": typing.Literal["antsRegistrationSyNQuick.sh"],
    "dimensionality": typing.Literal[2, 3],
    "fixed_image": InputPathType,
    "moving_image": InputPathType,
    "output_prefix": str,
    "transform_type": typing.NotRequired[typing.Literal["s", "b"] | None],
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
        "antsRegistrationSyNQuick.sh": ants_registration_sy_nquick_sh_cargs,
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
        "antsRegistrationSyNQuick.sh": ants_registration_sy_nquick_sh_outputs,
    }
    return vt.get(t)


class AntsRegistrationSyNquickShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_registration_sy_nquick_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """Affine transformation matrix resulting from registration."""
    output_warp: OutputPathType
    """Warp field resulting from the registration."""
    output_inverse_warp: OutputPathType
    """Inverse warp field resulting from the registration."""
    output_warped_image: OutputPathType
    """Warped moving image."""


def ants_registration_sy_nquick_sh_params(
    dimensionality: typing.Literal[2, 3],
    fixed_image: InputPathType,
    moving_image: InputPathType,
    output_prefix: str,
    transform_type: typing.Literal["s", "b"] | None = None,
) -> AntsRegistrationSyNquickShParameters:
    """
    Build parameters.
    
    Args:
        dimensionality: Dimensionality of the images (2 or 3).
        fixed_image: Fixed image to which the moving image is registered.
        moving_image: Moving image that is registered to the fixed image.
        output_prefix: Prefix for the output files.
        transform_type: Type of transform: 's' for SyN, 'b' for B-spline SyN.\
            Default is 's'.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsRegistrationSyNQuick.sh",
        "dimensionality": dimensionality,
        "fixed_image": fixed_image,
        "moving_image": moving_image,
        "output_prefix": output_prefix,
    }
    if transform_type is not None:
        params["transform_type"] = transform_type
    return params


def ants_registration_sy_nquick_sh_cargs(
    params: AntsRegistrationSyNquickShParameters,
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
    cargs.append("antsRegistrationSyNQuick.sh")
    cargs.extend([
        "-d",
        str(params.get("dimensionality"))
    ])
    cargs.extend([
        "-f",
        execution.input_file(params.get("fixed_image"))
    ])
    cargs.extend([
        "-m",
        execution.input_file(params.get("moving_image"))
    ])
    cargs.extend([
        "-o",
        params.get("output_prefix")
    ])
    if params.get("transform_type") is not None:
        cargs.append(params.get("transform_type"))
    return cargs


def ants_registration_sy_nquick_sh_outputs(
    params: AntsRegistrationSyNquickShParameters,
    execution: Execution,
) -> AntsRegistrationSyNquickShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsRegistrationSyNquickShOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(params.get("output_prefix") + "0GenericAffine.mat"),
        output_warp=execution.output_file(params.get("output_prefix") + "1Warp.nii.gz"),
        output_inverse_warp=execution.output_file(params.get("output_prefix") + "1InverseWarp.nii.gz"),
        output_warped_image=execution.output_file(params.get("output_prefix") + "Warped.nii.gz"),
    )
    return ret


def ants_registration_sy_nquick_sh_execute(
    params: AntsRegistrationSyNquickShParameters,
    execution: Execution,
) -> AntsRegistrationSyNquickShOutputs:
    """
    A script to quickly compute a SyN-based registration between two images using
    ANTS.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsRegistrationSyNquickShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_registration_sy_nquick_sh_cargs(params, execution)
    ret = ants_registration_sy_nquick_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_registration_sy_nquick_sh(
    dimensionality: typing.Literal[2, 3],
    fixed_image: InputPathType,
    moving_image: InputPathType,
    output_prefix: str,
    transform_type: typing.Literal["s", "b"] | None = None,
    runner: Runner | None = None,
) -> AntsRegistrationSyNquickShOutputs:
    """
    A script to quickly compute a SyN-based registration between two images using
    ANTS.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimensionality: Dimensionality of the images (2 or 3).
        fixed_image: Fixed image to which the moving image is registered.
        moving_image: Moving image that is registered to the fixed image.
        output_prefix: Prefix for the output files.
        transform_type: Type of transform: 's' for SyN, 'b' for B-spline SyN.\
            Default is 's'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsRegistrationSyNquickShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_REGISTRATION_SY_NQUICK_SH_METADATA)
    params = ants_registration_sy_nquick_sh_params(dimensionality=dimensionality, fixed_image=fixed_image, moving_image=moving_image, output_prefix=output_prefix, transform_type=transform_type)
    return ants_registration_sy_nquick_sh_execute(params, execution)


__all__ = [
    "ANTS_REGISTRATION_SY_NQUICK_SH_METADATA",
    "AntsRegistrationSyNquickShOutputs",
    "ants_registration_sy_nquick_sh",
    "ants_registration_sy_nquick_sh_params",
]
