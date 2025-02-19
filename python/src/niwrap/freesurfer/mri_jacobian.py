# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_JACOBIAN_METADATA = Metadata(
    id="261fa5191d385d242b16ec1808b1a5ac51b44bc2.boutiques",
    name="mri_jacobian",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriJacobianParameters = typing.TypedDict('MriJacobianParameters', {
    "__STYX_TYPE__": typing.Literal["mri_jacobian"],
    "morph_file": InputPathType,
    "template_vol": InputPathType,
    "output_vol": str,
    "atlas_coord": bool,
    "write_area_vols": bool,
    "log_jacobian": bool,
    "smooth_sigma": typing.NotRequired[float | None],
    "zero_mean_log": bool,
    "tm3d": bool,
    "help2": bool,
    "dt": bool,
    "debug_voxel": typing.NotRequired[list[float] | None],
    "remove": bool,
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
        "mri_jacobian": mri_jacobian_cargs,
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
        "mri_jacobian": mri_jacobian_outputs,
    }.get(t)


class MriJacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_jacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result_vol: OutputPathType
    """Resulting volume file after Jacobian computation"""


def mri_jacobian_params(
    morph_file: InputPathType,
    template_vol: InputPathType,
    output_vol: str,
    atlas_coord: bool = False,
    write_area_vols: bool = False,
    log_jacobian: bool = False,
    smooth_sigma: float | None = None,
    zero_mean_log: bool = False,
    tm3d: bool = False,
    help2: bool = False,
    dt: bool = False,
    debug_voxel: list[float] | None = None,
    remove: bool = False,
) -> MriJacobianParameters:
    """
    Build parameters.
    
    Args:
        morph_file: 3D morph input file.
        template_vol: Template volume file.
        output_vol: Output volume file.
        atlas_coord: Output is written in atlas coordinate system.
        write_area_vols: Writing area volumes.
        log_jacobian: Taking log of Jacobian values before saving.
        smooth_sigma: Smoothing Jacobian volume with sigma.
        zero_mean_log: Make log Jacobian zero mean.
        tm3d: The input morph (m3z) originated from tm3d (mri_cvs_register).
        help2: Writing out help.
        dt: DT option (description not provided in help text).
        debug_voxel: Debug voxel with specified Gx, Gy, Gz coordinates.
        remove: Remove option (description not provided in help text).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_jacobian",
        "morph_file": morph_file,
        "template_vol": template_vol,
        "output_vol": output_vol,
        "atlas_coord": atlas_coord,
        "write_area_vols": write_area_vols,
        "log_jacobian": log_jacobian,
        "zero_mean_log": zero_mean_log,
        "tm3d": tm3d,
        "help2": help2,
        "dt": dt,
        "remove": remove,
    }
    if smooth_sigma is not None:
        params["smooth_sigma"] = smooth_sigma
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    return params


def mri_jacobian_cargs(
    params: MriJacobianParameters,
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
    cargs.append("mri_jacobian")
    cargs.append(execution.input_file(params.get("morph_file")))
    cargs.append(execution.input_file(params.get("template_vol")))
    cargs.append(params.get("output_vol"))
    if params.get("atlas_coord"):
        cargs.append("-a")
    if params.get("write_area_vols"):
        cargs.append("-w")
    if params.get("log_jacobian"):
        cargs.append("-l")
    if params.get("smooth_sigma") is not None:
        cargs.extend([
            "-s",
            str(params.get("smooth_sigma"))
        ])
    if params.get("zero_mean_log"):
        cargs.append("-z")
    if params.get("tm3d"):
        cargs.append("-tm3d")
    if params.get("help2"):
        cargs.append("-u")
    if params.get("dt"):
        cargs.append("-dt")
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    if params.get("remove"):
        cargs.append("-remove")
    return cargs


def mri_jacobian_outputs(
    params: MriJacobianParameters,
    execution: Execution,
) -> MriJacobianOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriJacobianOutputs(
        root=execution.output_file("."),
        result_vol=execution.output_file(params.get("output_vol")),
    )
    return ret


def mri_jacobian_execute(
    params: MriJacobianParameters,
    execution: Execution,
) -> MriJacobianOutputs:
    """
    Compute the Jacobian of a morph with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriJacobianOutputs`).
    """
    params = execution.params(params)
    cargs = mri_jacobian_cargs(params, execution)
    ret = mri_jacobian_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_jacobian(
    morph_file: InputPathType,
    template_vol: InputPathType,
    output_vol: str,
    atlas_coord: bool = False,
    write_area_vols: bool = False,
    log_jacobian: bool = False,
    smooth_sigma: float | None = None,
    zero_mean_log: bool = False,
    tm3d: bool = False,
    help2: bool = False,
    dt: bool = False,
    debug_voxel: list[float] | None = None,
    remove: bool = False,
    runner: Runner | None = None,
) -> MriJacobianOutputs:
    """
    Compute the Jacobian of a morph with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        morph_file: 3D morph input file.
        template_vol: Template volume file.
        output_vol: Output volume file.
        atlas_coord: Output is written in atlas coordinate system.
        write_area_vols: Writing area volumes.
        log_jacobian: Taking log of Jacobian values before saving.
        smooth_sigma: Smoothing Jacobian volume with sigma.
        zero_mean_log: Make log Jacobian zero mean.
        tm3d: The input morph (m3z) originated from tm3d (mri_cvs_register).
        help2: Writing out help.
        dt: DT option (description not provided in help text).
        debug_voxel: Debug voxel with specified Gx, Gy, Gz coordinates.
        remove: Remove option (description not provided in help text).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriJacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_JACOBIAN_METADATA)
    params = mri_jacobian_params(morph_file=morph_file, template_vol=template_vol, output_vol=output_vol, atlas_coord=atlas_coord, write_area_vols=write_area_vols, log_jacobian=log_jacobian, smooth_sigma=smooth_sigma, zero_mean_log=zero_mean_log, tm3d=tm3d, help2=help2, dt=dt, debug_voxel=debug_voxel, remove=remove)
    return mri_jacobian_execute(params, execution)


__all__ = [
    "MRI_JACOBIAN_METADATA",
    "MriJacobianOutputs",
    "MriJacobianParameters",
    "mri_jacobian",
    "mri_jacobian_params",
]
