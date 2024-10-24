# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_LOCAL_STAT_METADATA = Metadata(
    id="2b7eeee2dd047b080808536600a152ac4ca47630.boutiques",
    name="SurfLocalStat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SurfLocalStatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_local_stat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Computed local statistics dataset"""


def surf_local_stat(
    prefix: str,
    stat_: typing.Literal["mean", "mode", "num", "FWHM", "ALL"],
    input_dataset: InputPathType,
    surface: InputPathType,
    hood: float | None = None,
    nbhd_rad: float | None = None,
    runner: Runner | None = None,
) -> SurfLocalStatOutputs:
    """
    Compute local statistics on a surface mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix of output data set.
        stat_: Compute the specified statistic on the values extracted from the\
            region around each voxel. Options: mean, mode, num, FWHM, ALL.
        input_dataset: Input dataset.
        surface: Input GIFTI surface file.
        hood: Neighborhood of nodes within the specified radius R.
        nbhd_rad: Distance from node n as measured by the shortest distance\
            along the mesh.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfLocalStatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_LOCAL_STAT_METADATA)
    cargs = []
    cargs.append("SurfLocalstat")
    if hood is not None:
        cargs.extend([
            "-hood",
            str(hood)
        ])
    if nbhd_rad is not None:
        cargs.extend([
            "-nbhd_rad",
            str(nbhd_rad)
        ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.extend([
        "-stat",
        stat_
    ])
    cargs.extend([
        "-input",
        execution.input_file(input_dataset)
    ])
    cargs.extend([
        "-i_gii",
        execution.input_file(surface)
    ])
    ret = SurfLocalStatOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + ".niml.dset"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_LOCAL_STAT_METADATA",
    "SurfLocalStatOutputs",
    "surf_local_stat",
]
