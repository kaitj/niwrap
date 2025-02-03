# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_VEC_RGB_TO_HSL_METADATA = Metadata(
    id="6117ba68b426e9e30b15374be67ca0934595ccef.boutiques",
    name="3dVecRGB_to_HSL",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dVecRgbToHslParameters = typing.TypedDict('V3dVecRgbToHslParameters', {
    "__STYX_TYPE__": typing.Literal["3dVecRGB_to_HSL"],
    "prefix": str,
    "in_vec": InputPathType,
    "mask": typing.NotRequired[InputPathType | None],
    "in_scal": typing.NotRequired[InputPathType | None],
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
        "3dVecRGB_to_HSL": v_3d_vec_rgb_to_hsl_cargs,
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
        "3dVecRGB_to_HSL": v_3d_vec_rgb_to_hsl_outputs,
    }
    return vt.get(t)


class V3dVecRgbToHslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_vec_rgb_to_hsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_hsl_dataset: OutputPathType
    """Output HSL dataset"""


def v_3d_vec_rgb_to_hsl_params(
    prefix: str,
    in_vec: InputPathType,
    mask: InputPathType | None = None,
    in_scal: InputPathType | None = None,
) -> V3dVecRgbToHslParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file name part.
        in_vec: Input RGB vector file of three bricks, presumably each having\
            values in the interval [0,1].
        mask: Whole brain mask within which to calculate things. Otherwise,\
            data should be masked already.
        in_scal: Scalar file (single brick) which will be appended to the\
            output file, mainly aimed at loading in an FA data set for tract volume\
            coloration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dVecRGB_to_HSL",
        "prefix": prefix,
        "in_vec": in_vec,
    }
    if mask is not None:
        params["mask"] = mask
    if in_scal is not None:
        params["in_scal"] = in_scal
    return params


def v_3d_vec_rgb_to_hsl_cargs(
    params: V3dVecRgbToHslParameters,
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
    cargs.append("3dVecRGB_to_HSL")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-in_vec",
        execution.input_file(params.get("in_vec"))
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("in_scal") is not None:
        cargs.extend([
            "-in_scal",
            execution.input_file(params.get("in_scal"))
        ])
    return cargs


def v_3d_vec_rgb_to_hsl_outputs(
    params: V3dVecRgbToHslParameters,
    execution: Execution,
) -> V3dVecRgbToHslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dVecRgbToHslOutputs(
        root=execution.output_file("."),
        output_hsl_dataset=execution.output_file(params.get("prefix") + "_HSL+*.HEAD"),
    )
    return ret


def v_3d_vec_rgb_to_hsl_execute(
    params: V3dVecRgbToHslParameters,
    execution: Execution,
) -> V3dVecRgbToHslOutputs:
    """
    Convert a 3-brick RGB (red, green, blue) data set to an HSL (hue, saturation,
    luminance) one.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dVecRgbToHslOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_vec_rgb_to_hsl_cargs(params, execution)
    ret = v_3d_vec_rgb_to_hsl_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_vec_rgb_to_hsl(
    prefix: str,
    in_vec: InputPathType,
    mask: InputPathType | None = None,
    in_scal: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dVecRgbToHslOutputs:
    """
    Convert a 3-brick RGB (red, green, blue) data set to an HSL (hue, saturation,
    luminance) one.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name part.
        in_vec: Input RGB vector file of three bricks, presumably each having\
            values in the interval [0,1].
        mask: Whole brain mask within which to calculate things. Otherwise,\
            data should be masked already.
        in_scal: Scalar file (single brick) which will be appended to the\
            output file, mainly aimed at loading in an FA data set for tract volume\
            coloration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dVecRgbToHslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_VEC_RGB_TO_HSL_METADATA)
    params = v_3d_vec_rgb_to_hsl_params(prefix=prefix, in_vec=in_vec, mask=mask, in_scal=in_scal)
    return v_3d_vec_rgb_to_hsl_execute(params, execution)


__all__ = [
    "V3dVecRgbToHslOutputs",
    "V_3D_VEC_RGB_TO_HSL_METADATA",
    "v_3d_vec_rgb_to_hsl",
    "v_3d_vec_rgb_to_hsl_params",
]
