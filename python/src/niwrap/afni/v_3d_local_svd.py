# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LOCAL_SVD_METADATA = Metadata(
    id="e97613398607a0cd7904712ae0f0562e669540a4.boutiques",
    name="3dLocalSVD",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dLocalSvdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_svd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_local_svd(
    input_file: InputPathType,
    output_file: str,
    auto_mask: bool = False,
    mask_file: InputPathType | None = None,
    nbhd: str | None = None,
    polort: str | None = None,
    vnorm: bool = False,
    vproj: float | None = None,
    runner: Runner | None = None,
) -> V3dLocalSvdOutputs:
    """
    Computes the SVD of time series from a neighborhood of each voxel.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLocalSVD.html
    
    Args:
        input_file: Input time series dataset file.
        output_file: Prefix for the output SVD vector result dataset file.
        auto_mask: Create a mask from time series dataset.
        mask_file: Restrict operations to this mask dataset.
        nbhd: Neighborhood for SVD calculation, e.g., 'SPHERE(5)'.
        polort: Detrending option, ['+' means to add trend back].
        vnorm: Normalize data vectors [strongly recommended].
        vproj: Project central data time series onto local SVD subspace of\
            dimension 'ndim'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalSvdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_SVD_METADATA)
    cargs = []
    cargs.append("3dLocalSVD")
    if auto_mask:
        cargs.append("-automask")
    cargs.append("-input")
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    if mask_file is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask_file)
        ])
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        output_file
    ])
    if nbhd is not None:
        cargs.extend([
            "-nbhd",
            nbhd
        ])
    if polort is not None:
        cargs.extend([
            "-polort",
            polort
        ])
    if vnorm:
        cargs.append("-vnorm")
    if vproj is not None:
        cargs.extend([
            "-vproj",
            str(vproj)
        ])
    ret = V3dLocalSvdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalSvdOutputs",
    "V_3D_LOCAL_SVD_METADATA",
    "v_3d_local_svd",
]