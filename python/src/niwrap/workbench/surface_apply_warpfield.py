# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURFACE_APPLY_WARPFIELD_METADATA = Metadata(
    id="62d776ef4770f80788d15439d0c09cdb0b85568a.boutiques",
    name="surface-apply-warpfield",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceApplyWarpfieldParameters = typing.TypedDict('SurfaceApplyWarpfieldParameters', {
    "__STYX_TYPE__": typing.Literal["surface-apply-warpfield"],
    "in_surf": InputPathType,
    "warpfield": str,
    "out_surf": str,
    "opt_fnirt_forward_warp": typing.NotRequired[str | None],
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
        "surface-apply-warpfield": surface_apply_warpfield_cargs,
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
        "surface-apply-warpfield": surface_apply_warpfield_outputs,
    }.get(t)


class SurfaceApplyWarpfieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_apply_warpfield(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType
    """the output transformed surface"""


def surface_apply_warpfield_params(
    in_surf: InputPathType,
    warpfield: str,
    out_surf: str,
    opt_fnirt_forward_warp: str | None = None,
) -> SurfaceApplyWarpfieldParameters:
    """
    Build parameters.
    
    Args:
        in_surf: the surface to transform.
        warpfield: the INVERSE warpfield.
        out_surf: the output transformed surface.
        opt_fnirt_forward_warp: MUST be used if using a fnirt warpfield: the\
            forward warpfield.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-apply-warpfield",
        "in_surf": in_surf,
        "warpfield": warpfield,
        "out_surf": out_surf,
    }
    if opt_fnirt_forward_warp is not None:
        params["opt_fnirt_forward_warp"] = opt_fnirt_forward_warp
    return params


def surface_apply_warpfield_cargs(
    params: SurfaceApplyWarpfieldParameters,
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
    cargs.append("wb_command")
    cargs.append("-surface-apply-warpfield")
    cargs.append(execution.input_file(params.get("in_surf")))
    cargs.append(params.get("warpfield"))
    cargs.append(params.get("out_surf"))
    if params.get("opt_fnirt_forward_warp") is not None:
        cargs.extend([
            "-fnirt",
            params.get("opt_fnirt_forward_warp")
        ])
    return cargs


def surface_apply_warpfield_outputs(
    params: SurfaceApplyWarpfieldParameters,
    execution: Execution,
) -> SurfaceApplyWarpfieldOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceApplyWarpfieldOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(params.get("out_surf")),
    )
    return ret


def surface_apply_warpfield_execute(
    params: SurfaceApplyWarpfieldParameters,
    execution: Execution,
) -> SurfaceApplyWarpfieldOutputs:
    """
    Apply warpfield to surface file.
    
    NOTE: warping a surface requires the INVERSE of the warpfield used to warp
    the volume it lines up with. The header of the forward warp is needed by the
    -fnirt option in order to correctly interpret the displacements in the fnirt
    warpfield.
    
    If the -fnirt option is not present, the warpfield must be a nifti 'world'
    warpfield, which can be obtained with the -convert-warpfield command.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceApplyWarpfieldOutputs`).
    """
    params = execution.params(params)
    cargs = surface_apply_warpfield_cargs(params, execution)
    ret = surface_apply_warpfield_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_apply_warpfield(
    in_surf: InputPathType,
    warpfield: str,
    out_surf: str,
    opt_fnirt_forward_warp: str | None = None,
    runner: Runner | None = None,
) -> SurfaceApplyWarpfieldOutputs:
    """
    Apply warpfield to surface file.
    
    NOTE: warping a surface requires the INVERSE of the warpfield used to warp
    the volume it lines up with. The header of the forward warp is needed by the
    -fnirt option in order to correctly interpret the displacements in the fnirt
    warpfield.
    
    If the -fnirt option is not present, the warpfield must be a nifti 'world'
    warpfield, which can be obtained with the -convert-warpfield command.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        in_surf: the surface to transform.
        warpfield: the INVERSE warpfield.
        out_surf: the output transformed surface.
        opt_fnirt_forward_warp: MUST be used if using a fnirt warpfield: the\
            forward warpfield.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceApplyWarpfieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_APPLY_WARPFIELD_METADATA)
    params = surface_apply_warpfield_params(in_surf=in_surf, warpfield=warpfield, out_surf=out_surf, opt_fnirt_forward_warp=opt_fnirt_forward_warp)
    return surface_apply_warpfield_execute(params, execution)


__all__ = [
    "SURFACE_APPLY_WARPFIELD_METADATA",
    "SurfaceApplyWarpfieldOutputs",
    "SurfaceApplyWarpfieldParameters",
    "surface_apply_warpfield",
    "surface_apply_warpfield_params",
]
