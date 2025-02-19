# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

STAT_NORMALIZE_METADATA = Metadata(
    id="8f7cdbd11149e9374f79034222936da63d116040.boutiques",
    name="stat_normalize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
StatNormalizeParameters = typing.TypedDict('StatNormalizeParameters', {
    "__STYX_TYPE__": typing.Literal["stat_normalize"],
    "input_sv_prefix": str,
    "output_sv_prefix": str,
    "resolution": typing.NotRequired[float | None],
    "field_of_view": typing.NotRequired[float | None],
    "sph_avg": typing.NotRequired[str | None],
    "xfm_file": typing.NotRequired[str | None],
    "fix_xfm_flag": bool,
    "float2int_option": typing.NotRequired[str | None],
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
        "stat_normalize": stat_normalize_cargs,
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


class StatNormalizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stat_normalize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def stat_normalize_params(
    input_sv_prefix: str,
    output_sv_prefix: str,
    resolution: float | None = None,
    field_of_view: float | None = None,
    sph_avg: str | None = None,
    xfm_file: str | None = None,
    fix_xfm_flag: bool = False,
    float2int_option: str | None = None,
) -> StatNormalizeParameters:
    """
    Build parameters.
    
    Args:
        input_sv_prefix: Input subject volume prefix.
        output_sv_prefix: Output subject volume prefix.
        resolution: Set output resolution in mm (default is 8mm).
        field_of_view: Set output field of view (default is 256).
        sph_avg: Average in spherical coordinates by specifying hemisphere and\
            surface.
        xfm_file: Use specified transform file (subjid/mri/transforms/xfmfile).
        fix_xfm_flag: Fix transform for non-zero center of original volume.
        float2int_option: Specify float to int conversion to tkregister or\
            round.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stat_normalize",
        "input_sv_prefix": input_sv_prefix,
        "output_sv_prefix": output_sv_prefix,
        "fix_xfm_flag": fix_xfm_flag,
    }
    if resolution is not None:
        params["resolution"] = resolution
    if field_of_view is not None:
        params["field_of_view"] = field_of_view
    if sph_avg is not None:
        params["sph_avg"] = sph_avg
    if xfm_file is not None:
        params["xfm_file"] = xfm_file
    if float2int_option is not None:
        params["float2int_option"] = float2int_option
    return params


def stat_normalize_cargs(
    params: StatNormalizeParameters,
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
    cargs.append("stat_normalize")
    cargs.append(params.get("input_sv_prefix"))
    cargs.append(params.get("output_sv_prefix"))
    if params.get("resolution") is not None:
        cargs.extend([
            "-r",
            str(params.get("resolution"))
        ])
    if params.get("field_of_view") is not None:
        cargs.extend([
            "-f",
            str(params.get("field_of_view"))
        ])
    if params.get("sph_avg") is not None:
        cargs.extend([
            "-S",
            params.get("sph_avg")
        ])
    if params.get("xfm_file") is not None:
        cargs.extend([
            "-x",
            params.get("xfm_file")
        ])
    if params.get("fix_xfm_flag"):
        cargs.append("-i")
    if params.get("float2int_option") is not None:
        cargs.extend([
            "-c",
            params.get("float2int_option")
        ])
    return cargs


def stat_normalize_outputs(
    params: StatNormalizeParameters,
    execution: Execution,
) -> StatNormalizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = StatNormalizeOutputs(
        root=execution.output_file("."),
    )
    return ret


def stat_normalize_execute(
    params: StatNormalizeParameters,
    execution: Execution,
) -> StatNormalizeOutputs:
    """
    This program will convert and average a sequence of volume-based statistics in
    Talairach space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `StatNormalizeOutputs`).
    """
    params = execution.params(params)
    cargs = stat_normalize_cargs(params, execution)
    ret = stat_normalize_outputs(params, execution)
    execution.run(cargs)
    return ret


def stat_normalize(
    input_sv_prefix: str,
    output_sv_prefix: str,
    resolution: float | None = None,
    field_of_view: float | None = None,
    sph_avg: str | None = None,
    xfm_file: str | None = None,
    fix_xfm_flag: bool = False,
    float2int_option: str | None = None,
    runner: Runner | None = None,
) -> StatNormalizeOutputs:
    """
    This program will convert and average a sequence of volume-based statistics in
    Talairach space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_sv_prefix: Input subject volume prefix.
        output_sv_prefix: Output subject volume prefix.
        resolution: Set output resolution in mm (default is 8mm).
        field_of_view: Set output field of view (default is 256).
        sph_avg: Average in spherical coordinates by specifying hemisphere and\
            surface.
        xfm_file: Use specified transform file (subjid/mri/transforms/xfmfile).
        fix_xfm_flag: Fix transform for non-zero center of original volume.
        float2int_option: Specify float to int conversion to tkregister or\
            round.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StatNormalizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STAT_NORMALIZE_METADATA)
    params = stat_normalize_params(input_sv_prefix=input_sv_prefix, output_sv_prefix=output_sv_prefix, resolution=resolution, field_of_view=field_of_view, sph_avg=sph_avg, xfm_file=xfm_file, fix_xfm_flag=fix_xfm_flag, float2int_option=float2int_option)
    return stat_normalize_execute(params, execution)


__all__ = [
    "STAT_NORMALIZE_METADATA",
    "StatNormalizeOutputs",
    "StatNormalizeParameters",
    "stat_normalize",
    "stat_normalize_params",
]
