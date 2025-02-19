# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SPHERE_METADATA = Metadata(
    id="ff70a8889110348344f49593918baf25bab92371.boutiques",
    name="mris_sphere",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisSphereParameters = typing.TypedDict('MrisSphereParameters', {
    "__STYX_TYPE__": typing.Literal["mris_sphere"],
    "surface_file": InputPathType,
    "patch_file": InputPathType,
    "output_patch": str,
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
        "mris_sphere": mris_sphere_cargs,
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
        "mris_sphere": mris_sphere_outputs,
    }.get(t)


class MrisSphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_patch_file: OutputPathType
    """Output patch file."""


def mris_sphere_params(
    surface_file: InputPathType,
    patch_file: InputPathType,
    output_patch: str,
) -> MrisSphereParameters:
    """
    Build parameters.
    
    Args:
        surface_file: Input surface file.
        patch_file: Input patch file name.
        output_patch: Output patch file name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_sphere",
        "surface_file": surface_file,
        "patch_file": patch_file,
        "output_patch": output_patch,
    }
    return params


def mris_sphere_cargs(
    params: MrisSphereParameters,
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
    cargs.append("mris_sphere")
    cargs.append(execution.input_file(params.get("surface_file")))
    cargs.append(execution.input_file(params.get("patch_file")))
    cargs.append(params.get("output_patch"))
    return cargs


def mris_sphere_outputs(
    params: MrisSphereParameters,
    execution: Execution,
) -> MrisSphereOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSphereOutputs(
        root=execution.output_file("."),
        output_patch_file=execution.output_file(params.get("output_patch")),
    )
    return ret


def mris_sphere_execute(
    params: MrisSphereParameters,
    execution: Execution,
) -> MrisSphereOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSphereOutputs`).
    """
    params = execution.params(params)
    cargs = mris_sphere_cargs(params, execution)
    ret = mris_sphere_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_sphere(
    surface_file: InputPathType,
    patch_file: InputPathType,
    output_patch: str,
    runner: Runner | None = None,
) -> MrisSphereOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface_file: Input surface file.
        patch_file: Input patch file name.
        output_patch: Output patch file name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SPHERE_METADATA)
    params = mris_sphere_params(surface_file=surface_file, patch_file=patch_file, output_patch=output_patch)
    return mris_sphere_execute(params, execution)


__all__ = [
    "MRIS_SPHERE_METADATA",
    "MrisSphereOutputs",
    "MrisSphereParameters",
    "mris_sphere",
    "mris_sphere_params",
]
