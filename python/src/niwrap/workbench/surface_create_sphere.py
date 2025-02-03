# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_CREATE_SPHERE_METADATA = Metadata(
    id="4f2f655e81d545740a448403ba6bbaff1b89f0a6.boutiques",
    name="surface-create-sphere",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
SurfaceCreateSphereParameters = typing.TypedDict('SurfaceCreateSphereParameters', {
    "__STYX_TYPE__": typing.Literal["surface-create-sphere"],
    "num_vertices": int,
    "sphere_out": str,
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
        "surface-create-sphere": surface_create_sphere_cargs,
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
        "surface-create-sphere": surface_create_sphere_outputs,
    }
    return vt.get(t)


class SurfaceCreateSphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_create_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_create_sphere_params(
    num_vertices: int,
    sphere_out: str,
) -> SurfaceCreateSphereParameters:
    """
    Build parameters.
    
    Args:
        num_vertices: desired number of vertices.
        sphere_out: the output sphere.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface-create-sphere",
        "num_vertices": num_vertices,
        "sphere_out": sphere_out,
    }
    return params


def surface_create_sphere_cargs(
    params: SurfaceCreateSphereParameters,
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
    cargs.append("-surface-create-sphere")
    cargs.append(str(params.get("num_vertices")))
    cargs.append(params.get("sphere_out"))
    return cargs


def surface_create_sphere_outputs(
    params: SurfaceCreateSphereParameters,
    execution: Execution,
) -> SurfaceCreateSphereOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfaceCreateSphereOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(params.get("sphere_out")),
    )
    return ret


def surface_create_sphere_execute(
    params: SurfaceCreateSphereParameters,
    execution: Execution,
) -> SurfaceCreateSphereOutputs:
    """
    Generate a sphere with consistent vertex areas.
    
    Generates a sphere by regularly dividing the triangles of an icosahedron, to
    come as close to the desired number of vertices as possible, and modifying
    it to have very similar vertex areas for all vertices. To generate a pair of
    vertex-matched left and right spheres, use this command, then
    -surface-flip-lr to generate the other sphere, then -set-structure on each.
    For example:
    
    $ wb_command -surface-create-sphere 6000 Sphere.6k.R.surf.gii
    $ wb_command -surface-flip-lr Sphere.6k.R.surf.gii Sphere.6k.L.surf.gii
    $ wb_command -set-structure Sphere.6k.R.surf.gii CORTEX_RIGHT
    $ wb_command -set-structure Sphere.6k.L.surf.gii CORTEX_LEFT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfaceCreateSphereOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = surface_create_sphere_cargs(params, execution)
    ret = surface_create_sphere_outputs(params, execution)
    execution.run(cargs)
    return ret


def surface_create_sphere(
    num_vertices: int,
    sphere_out: str,
    runner: Runner | None = None,
) -> SurfaceCreateSphereOutputs:
    """
    Generate a sphere with consistent vertex areas.
    
    Generates a sphere by regularly dividing the triangles of an icosahedron, to
    come as close to the desired number of vertices as possible, and modifying
    it to have very similar vertex areas for all vertices. To generate a pair of
    vertex-matched left and right spheres, use this command, then
    -surface-flip-lr to generate the other sphere, then -set-structure on each.
    For example:
    
    $ wb_command -surface-create-sphere 6000 Sphere.6k.R.surf.gii
    $ wb_command -surface-flip-lr Sphere.6k.R.surf.gii Sphere.6k.L.surf.gii
    $ wb_command -set-structure Sphere.6k.R.surf.gii CORTEX_RIGHT
    $ wb_command -set-structure Sphere.6k.L.surf.gii CORTEX_LEFT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        num_vertices: desired number of vertices.
        sphere_out: the output sphere.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCreateSphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CREATE_SPHERE_METADATA)
    params = surface_create_sphere_params(num_vertices=num_vertices, sphere_out=sphere_out)
    return surface_create_sphere_execute(params, execution)


__all__ = [
    "SURFACE_CREATE_SPHERE_METADATA",
    "SurfaceCreateSphereOutputs",
    "surface_create_sphere",
    "surface_create_sphere_params",
]
