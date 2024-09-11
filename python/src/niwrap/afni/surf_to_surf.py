# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_TO_SURF_METADATA = Metadata(
    id="7ea5720d005f8ca36112681007b6c97602751bc5.boutiques",
    name="SurfToSurf",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfToSurfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_to_surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file in 1D format"""


def surf_to_surf(
    make_consistent: bool = False,
    runner: Runner | None = None,
) -> SurfToSurfOutputs:
    """
    Interpolate data from one surface to another.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfToSurf.html
    
    Args:
        make_consistent: Force a consistency check and correct triangle\
            orientation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfToSurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_TO_SURF_METADATA)
    cargs = []
    cargs.append("SurfToSurf")
    cargs.append("<-i_TYPE")
    cargs.append("S1>")
    cargs.append("[<-sv")
    cargs.append("SV1>]")
    cargs.append("<-i_TYPE")
    cargs.append("S2>")
    cargs.append("[<-sv")
    cargs.append("SV1>]")
    cargs.append("[<-prefix")
    cargs.append("PREFIX>]")
    cargs.append("[<-output_params")
    cargs.append("PARAM_LIST>]")
    cargs.append("[<-node_indices")
    cargs.append("NODE_INDICES>]")
    cargs.append("[<-proj_dir")
    cargs.append("PROJ_DIR>]")
    cargs.append("[<-data")
    cargs.append("DATA>]")
    cargs.append("[<-node_debug")
    cargs.append("NODE>]")
    cargs.append("[<-debug")
    cargs.append("DBG_LEVEL>]")
    if make_consistent:
        cargs.append("-make_consistent")
    cargs.append("[<-dset")
    cargs.append("DSET>]")
    cargs.append("[<-mapfile")
    cargs.append("MAP_INFO>]")
    ret = SurfToSurfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[PREFIX].1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_TO_SURF_METADATA",
    "SurfToSurfOutputs",
    "surf_to_surf",
]