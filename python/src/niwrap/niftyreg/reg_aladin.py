# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_ALADIN_METADATA = Metadata(
    id="0cdcd5294ca36b2c6f5e68cc4ee34d2019bd8f9f.boutiques",
    name="reg_aladin",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)
RegAladinParameters = typing.TypedDict('RegAladinParameters', {
    "__STYX_TYPE__": typing.Literal["reg_aladin"],
    "reference_image": InputPathType,
    "floating_image": InputPathType,
    "symmetric": bool,
    "output_affine": typing.NotRequired[str | None],
    "rigid_only": bool,
    "direct_affine": bool,
    "smooth_ref": typing.NotRequired[float | None],
    "smooth_float": typing.NotRequired[float | None],
    "num_levels": typing.NotRequired[float | None],
    "first_levels": typing.NotRequired[float | None],
    "use_nifti_origin": bool,
    "percent_block": typing.NotRequired[float | None],
    "percent_inlier": typing.NotRequired[float | None],
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
        "reg_aladin": reg_aladin_cargs,
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
        "reg_aladin": reg_aladin_outputs,
    }
    return vt.get(t)


class RegAladinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_aladin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_affine_file: OutputPathType
    """File containing the output affine transformation"""


def reg_aladin_params(
    reference_image: InputPathType,
    floating_image: InputPathType,
    symmetric: bool = False,
    output_affine: str | None = None,
    rigid_only: bool = False,
    direct_affine: bool = False,
    smooth_ref: float | None = None,
    smooth_float: float | None = None,
    num_levels: float | None = None,
    first_levels: float | None = None,
    use_nifti_origin: bool = False,
    percent_block: float | None = None,
    percent_inlier: float | None = None,
) -> RegAladinParameters:
    """
    Build parameters.
    
    Args:
        reference_image: Filename of the reference (target) image.
        floating_image: Filename of the floating (source) image.
        symmetric: Uses symmetric version of the algorithm.
        output_affine: Filename which contains the output affine transformation.
        rigid_only: To perform a rigid registration only.
        direct_affine: Directly optimize 12 DoF affine.
        smooth_ref: Smooth the reference image using the specified sigma (mm).
        smooth_float: Smooth the floating image using the specified sigma (mm).
        num_levels: Number of levels to perform.
        first_levels: Only perform the first levels.
        use_nifti_origin: Use the NIFTI header origins to initialize the\
            translation.
        percent_block: Percentage of block to use.
        percent_inlier: Percentage of inlier for the LTS.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "reg_aladin",
        "reference_image": reference_image,
        "floating_image": floating_image,
        "symmetric": symmetric,
        "rigid_only": rigid_only,
        "direct_affine": direct_affine,
        "use_nifti_origin": use_nifti_origin,
    }
    if output_affine is not None:
        params["output_affine"] = output_affine
    if smooth_ref is not None:
        params["smooth_ref"] = smooth_ref
    if smooth_float is not None:
        params["smooth_float"] = smooth_float
    if num_levels is not None:
        params["num_levels"] = num_levels
    if first_levels is not None:
        params["first_levels"] = first_levels
    if percent_block is not None:
        params["percent_block"] = percent_block
    if percent_inlier is not None:
        params["percent_inlier"] = percent_inlier
    return params


def reg_aladin_cargs(
    params: RegAladinParameters,
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
    cargs.append("reg_aladin")
    cargs.extend([
        "-ref",
        execution.input_file(params.get("reference_image"))
    ])
    cargs.extend([
        "-flo",
        execution.input_file(params.get("floating_image"))
    ])
    if params.get("symmetric"):
        cargs.append("-sym")
    if params.get("output_affine") is not None:
        cargs.extend([
            "-aff",
            params.get("output_affine")
        ])
    if params.get("rigid_only"):
        cargs.append("-rigOnly")
    if params.get("direct_affine"):
        cargs.append("-affDirect")
    if params.get("smooth_ref") is not None:
        cargs.extend([
            "-smooR",
            str(params.get("smooth_ref"))
        ])
    if params.get("smooth_float") is not None:
        cargs.extend([
            "-smooF",
            str(params.get("smooth_float"))
        ])
    if params.get("num_levels") is not None:
        cargs.extend([
            "-ln",
            str(params.get("num_levels"))
        ])
    if params.get("first_levels") is not None:
        cargs.extend([
            "-lp",
            str(params.get("first_levels"))
        ])
    if params.get("use_nifti_origin"):
        cargs.append("-nac")
    if params.get("percent_block") is not None:
        cargs.extend([
            "-%v",
            str(params.get("percent_block"))
        ])
    if params.get("percent_inlier") is not None:
        cargs.extend([
            "-%i",
            str(params.get("percent_inlier"))
        ])
    return cargs


def reg_aladin_outputs(
    params: RegAladinParameters,
    execution: Execution,
) -> RegAladinOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = RegAladinOutputs(
        root=execution.output_file("."),
        output_affine_file=execution.output_file("outputAffine.txt"),
    )
    return ret


def reg_aladin_execute(
    params: RegAladinParameters,
    execution: Execution,
) -> RegAladinOutputs:
    """
    Block Matching algorithm for global registration based on "Reconstructing a 3D
    structure from serial histological sections", Image and Vision Computing, 2001.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `RegAladinOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = reg_aladin_cargs(params, execution)
    ret = reg_aladin_outputs(params, execution)
    execution.run(cargs)
    return ret


def reg_aladin(
    reference_image: InputPathType,
    floating_image: InputPathType,
    symmetric: bool = False,
    output_affine: str | None = None,
    rigid_only: bool = False,
    direct_affine: bool = False,
    smooth_ref: float | None = None,
    smooth_float: float | None = None,
    num_levels: float | None = None,
    first_levels: float | None = None,
    use_nifti_origin: bool = False,
    percent_block: float | None = None,
    percent_inlier: float | None = None,
    runner: Runner | None = None,
) -> RegAladinOutputs:
    """
    Block Matching algorithm for global registration based on "Reconstructing a 3D
    structure from serial histological sections", Image and Vision Computing, 2001.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference (target) image.
        floating_image: Filename of the floating (source) image.
        symmetric: Uses symmetric version of the algorithm.
        output_affine: Filename which contains the output affine transformation.
        rigid_only: To perform a rigid registration only.
        direct_affine: Directly optimize 12 DoF affine.
        smooth_ref: Smooth the reference image using the specified sigma (mm).
        smooth_float: Smooth the floating image using the specified sigma (mm).
        num_levels: Number of levels to perform.
        first_levels: Only perform the first levels.
        use_nifti_origin: Use the NIFTI header origins to initialize the\
            translation.
        percent_block: Percentage of block to use.
        percent_inlier: Percentage of inlier for the LTS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegAladinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_ALADIN_METADATA)
    params = reg_aladin_params(reference_image=reference_image, floating_image=floating_image, symmetric=symmetric, output_affine=output_affine, rigid_only=rigid_only, direct_affine=direct_affine, smooth_ref=smooth_ref, smooth_float=smooth_float, num_levels=num_levels, first_levels=first_levels, use_nifti_origin=use_nifti_origin, percent_block=percent_block, percent_inlier=percent_inlier)
    return reg_aladin_execute(params, execution)


__all__ = [
    "REG_ALADIN_METADATA",
    "RegAladinOutputs",
    "reg_aladin",
    "reg_aladin_params",
]
