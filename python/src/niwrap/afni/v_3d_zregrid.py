# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ZREGRID_METADATA = Metadata(
    id="2597cdebba8fe75de8a28bb8bff140590938cb2b.boutiques",
    name="3dZregrid",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dZregridOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zregrid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_head: OutputPathType | None
    """Output dataset with new grid"""
    outfile_brik: OutputPathType | None
    """Output dataset with new grid"""


def v_3d_zregrid(
    infile: InputPathType,
    z_thickness: float | None = None,
    slice_count: float | None = None,
    z_size: float | None = None,
    prefix: str | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dZregridOutputs:
    """
    Alters the input dataset's slice thickness and/or number.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input dataset.
        z_thickness: Set slice thickness to D mm.
        slice_count: Set slice count to N.
        z_size: Set thickness of dataset (center-to-center of first and last\
            slices) to Z mm.
        prefix: Write result to dataset with prefix P.
        verbose: Write progress reports to stderr.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZregridOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZREGRID_METADATA)
    cargs = []
    cargs.append("3dZregrid")
    if z_thickness is not None:
        cargs.extend([
            "-dz",
            str(z_thickness)
        ])
    if slice_count is not None:
        cargs.extend([
            "-nz",
            str(slice_count)
        ])
    if z_size is not None:
        cargs.extend([
            "-zsize",
            str(z_size)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    cargs.append(execution.input_file(infile))
    if verbose:
        cargs.append("-verb")
    ret = V3dZregridOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
        outfile_brik=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZregridOutputs",
    "V_3D_ZREGRID_METADATA",
    "v_3d_zregrid",
]
