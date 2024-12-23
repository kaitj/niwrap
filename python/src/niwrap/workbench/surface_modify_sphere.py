# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_MODIFY_SPHERE_METADATA = Metadata(
    id="7ba7bdfa9f75a3f280b0446651d5074e673b22aa.boutiques",
    name="surface-modify-sphere",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceModifySphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_modify_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_modify_sphere(
    sphere_in: InputPathType,
    radius: float,
    sphere_out: str,
    opt_recenter: bool = False,
    runner: Runner | None = None,
) -> SurfaceModifySphereOutputs:
    """
    Change radius and optionally recenter a sphere.
    
    This command may be useful if you have used -surface-resample to resample a
    sphere, which can suffer from problems generally not present in
    -surface-sphere-project-unproject. If the sphere should already be centered
    around the origin, using -recenter may still shift it slightly before
    changing the radius, which is likely to be undesireable.
    
    If <sphere-in> is not close to spherical, or not centered around the origin
    and -recenter is not used, a warning is printed.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        sphere_in: the sphere to modify.
        radius: the radius the output sphere should have.
        sphere_out: the output sphere.
        opt_recenter: recenter the sphere by means of the bounding box.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceModifySphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_MODIFY_SPHERE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-modify-sphere")
    cargs.append(execution.input_file(sphere_in))
    cargs.append(str(radius))
    cargs.append(sphere_out)
    if opt_recenter:
        cargs.append("-recenter")
    ret = SurfaceModifySphereOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(sphere_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_MODIFY_SPHERE_METADATA",
    "SurfaceModifySphereOutputs",
    "surface_modify_sphere",
]
