# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAP_ICOSAHEDRON_METADATA = Metadata(
    id="7b5613e068758f60512d81bd807662763219e569.boutiques",
    name="MapIcosahedron",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class MapIcosahedronOutputs(typing.NamedTuple):
    """
    Output object returned when calling `map_icosahedron(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def map_icosahedron(
    spec_file: InputPathType,
    rec_depth: float | None = None,
    lin_depth: float | None = None,
    morph_surf: str | None = None,
    num_it: float | None = None,
    prefix: str | None = None,
    nn_dset: str | None = None,
    dset: str | None = None,
    fix_cut_surfaces: bool = False,
    verbosity: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MapIcosahedronOutputs:
    """
    Creates new versions of original-mesh surfaces using the mesh of an icosahedron.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/MapIcosahedron.html
    
    Args:
        spec_file: Spec file containing original-mesh surfaces.
        rec_depth: Recursive (binary) tessellation depth for icosahedron\
            (default: 3).
        lin_depth: Number of edge divides for linear icosahedron tessellation.
        morph_surf: Specifies the morphSurf surface.
        num_it: Number of smoothing iterations.
        prefix: Prefix for output files (default: 'std.').
        nn_dset: Map DSET onto the new mesh using Nearest Neighbor\
            interpolation.
        dset: Map DSET onto the new mesh using barycentric interpolation.
        fix_cut_surfaces: Check and fix standard-mesh surfaces with cuts for\
            cross-cut connections.
        verbosity: Enable verbose output.
        help_: Display the help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MapIcosahedronOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAP_ICOSAHEDRON_METADATA)
    cargs = []
    cargs.append("MapIcosahedron")
    cargs.append(execution.input_file(spec_file))
    if rec_depth is not None:
        cargs.extend([
            "-rd",
            str(rec_depth)
        ])
    if lin_depth is not None:
        cargs.extend([
            "-ld",
            str(lin_depth)
        ])
    if morph_surf is not None:
        cargs.extend([
            "-morph",
            morph_surf
        ])
    if num_it is not None:
        cargs.extend([
            "-it",
            str(num_it)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if nn_dset is not None:
        cargs.extend([
            "-NN_dset_map",
            nn_dset
        ])
    if dset is not None:
        cargs.extend([
            "-dset_map",
            dset
        ])
    if fix_cut_surfaces:
        cargs.append("-fix_cut_surfaces")
    if verbosity:
        cargs.append("-verb")
    if help_:
        cargs.append("-help")
    ret = MapIcosahedronOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAP_ICOSAHEDRON_METADATA",
    "MapIcosahedronOutputs",
    "map_icosahedron",
]