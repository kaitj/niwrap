# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_TO_SURFACE_3D_DISTANCE_METADATA = Metadata(
    id="5074938721a51c04a19cea4fff3d5ee34fe2233f.boutiques",
    name="surface-to-surface-3d-distance",
    package="workbench",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceToSurface3dDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_to_surface_3d_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dists_out: OutputPathType
    """the output distances"""
    vectors_out: OutputPathType
    """the output vectors"""


def surface_to_surface_3d_distance(
    surface_comp: InputPathType,
    surface_ref: InputPathType,
    dists_out: str,
    vectors_out: str,
    opt_vectors: bool = False,
    runner: Runner | None = None,
) -> SurfaceToSurface3dDistanceOutputs:
    """
    Compute distance between corresponding vertices.
    
    Computes the vector difference between the vertices of each surface with the
    same index, as (comp - ref), and output the magnitudes, and optionally the
    displacement vectors.
    
    Author: Washington University School of Medicin
    
    Args:
        surface_comp: the surface to compare to the reference.
        surface_ref: the surface to use as the reference.
        dists_out: the output distances.
        vectors_out: the output vectors.
        opt_vectors: output the displacement vectors.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceToSurface3dDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_TO_SURFACE_3D_DISTANCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-to-surface-3d-distance")
    cargs.append(execution.input_file(surface_comp))
    cargs.append(execution.input_file(surface_ref))
    cargs.append(dists_out)
    if opt_vectors:
        cargs.append("-vectors")
    cargs.append(vectors_out)
    ret = SurfaceToSurface3dDistanceOutputs(
        root=execution.output_file("."),
        dists_out=execution.output_file(dists_out),
        vectors_out=execution.output_file(vectors_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_TO_SURFACE_3D_DISTANCE_METADATA",
    "SurfaceToSurface3dDistanceOutputs",
    "surface_to_surface_3d_distance",
]
