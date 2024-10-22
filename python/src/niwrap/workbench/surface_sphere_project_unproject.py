# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_SPHERE_PROJECT_UNPROJECT_METADATA = Metadata(
    id="d8f632b8bb06dad43a9bfe9937a7752ac0d165db.boutiques",
    name="surface-sphere-project-unproject",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceSphereProjectUnprojectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_sphere_project_unproject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_sphere_project_unproject(
    sphere_in: InputPathType,
    sphere_project_to: InputPathType,
    sphere_unproject_from: InputPathType,
    sphere_out: str,
    runner: Runner | None = None,
) -> SurfaceSphereProjectUnprojectOutputs:
    """
    Copy registration deformations to different sphere.
    
    Background: A surface registration starts with an input sphere, and moves
    its vertices around on the sphere until it matches the template data. This
    means that the registration deformation is actually represented as the
    difference between two separate files - the starting sphere, and the
    registered sphere. Since the starting sphere of the registration may not
    have vertex correspondence to any other sphere (often, it is a native
    sphere), it can be inconvenient to manipulate or compare these deformations
    across subjects, etc.
    
    The purpose of this command is to be able to apply these deformations onto a
    new sphere of the user's choice, to make it easier to compare or manipulate
    them. Common uses are to concatenate two successive separate registrations
    (e.g. Human to Chimpanzee, and then Chimpanzee to Macaque) or inversion (for
    dedrifting or symmetric registration schemes).
    
    <sphere-in> must already be considered to be in alignment with one of the
    two ends of the registration (if your registration is Human to Chimpanzee,
    <sphere-in> must be in register with either Human or Chimpanzee). The
    'project-to' sphere must be the side of the registration that is aligned
    with <sphere-in> (if your registration is Human to Chimpanzee, and
    <sphere-in> is aligned with Human, then 'project-to' should be the original
    Human sphere). The 'unproject-from' sphere must be the remaining sphere of
    the registration (original vs deformed/registered). The output is as if you
    had run the same registration with <sphere-in> as the starting sphere, in
    the direction of deforming the 'project-to' sphere to create the
    'unproject-from' sphere.
    
    Note that this command cannot check for you what spheres are aligned with
    other spheres, and using the wrong spheres or in the incorrect order will
    not necessarily cause an error message. In some cases, it may be useful to
    use a new, arbitrary sphere as the input, which can be created with the
    -surface-create-sphere command.
    
    Example 1: You have a Human to Chimpanzee registration, and a Chimpanzee to
    Macaque registration, and want to combine them. If you use the Human sphere
    registered to Chimpanzee as sphere-in, the Chimpanzee standard sphere as
    project-to, and the Chimpanzee sphere registered to Macaque as
    unproject-from, the output will be the Human sphere in register with the
    Macaque.
    
    Example 2: You have a Human to Chimpanzee registration, but what you really
    want is the inverse, that is, the sphere as if you had run the registration
    from Chimpanzee to Human. If you use the Chimpanzee standard sphere as
    sphere-in, the Human sphere registered to Chimpanzee as project-to, and the
    standard Human sphere as unproject-from, the output will be the Chimpanzee
    sphere in register with the Human.
    
    Technical details: Each vertex of <sphere-in> is projected to a triangle of
    <sphere-project-to>, and its new position is determined by the position of
    the corresponding triangle in <sphere-unproject-from>. The output is a
    sphere with the topology of <sphere-in>, but coordinates shifted by the
    deformation from <sphere-project-to> to <sphere-unproject-from>.
    <sphere-project-to> and <sphere-unproject-from> must have the same topology
    as each other, but <sphere-in> may have any topology.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        sphere_in: a sphere with the desired output mesh.
        sphere_project_to: a sphere that aligns with sphere-in.
        sphere_unproject_from: <sphere-project-to> deformed to the desired\
            output space.
        sphere_out: the output sphere.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceSphereProjectUnprojectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SPHERE_PROJECT_UNPROJECT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-sphere-project-unproject")
    cargs.append(execution.input_file(sphere_in))
    cargs.append(execution.input_file(sphere_project_to))
    cargs.append(execution.input_file(sphere_unproject_from))
    cargs.append(sphere_out)
    ret = SurfaceSphereProjectUnprojectOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(sphere_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_SPHERE_PROJECT_UNPROJECT_METADATA",
    "SurfaceSphereProjectUnprojectOutputs",
    "surface_sphere_project_unproject",
]
