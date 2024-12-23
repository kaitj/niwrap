# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_LOCAL_ACF_METADATA = Metadata(
    id="f02de9f266ae864cf54889181b4c744098070407.boutiques",
    name="3dLocalACF",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dLocalAcfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_local_acf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset with ACF estimates"""


def v_3d_local_acf(
    prefix: str,
    input_file: InputPathType,
    neighborhood: str | None = None,
    mask_file: InputPathType | None = None,
    auto_mask: bool = False,
    runner: Runner | None = None,
) -> V3dLocalAcfOutputs:
    """
    Estimate the spatial AutoCorrelation Function (ACF) locally in a neighborhood
    around each voxel.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for output dataset.
        input_file: Input time series dataset.
        neighborhood: Neighborhood specification (e.g., SPHERE(25)).
        mask_file: Dataset to mask the analysis.
        auto_mask: Automatically generate brain mask from input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dLocalAcfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_LOCAL_ACF_METADATA)
    cargs = []
    cargs.append("3dLocalACF")
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.append(execution.input_file(input_file))
    if neighborhood is not None:
        cargs.extend([
            "-nbhd",
            neighborhood
        ])
    if mask_file is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask_file)
        ])
    if auto_mask:
        cargs.append("-automask")
    ret = V3dLocalAcfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalAcfOutputs",
    "V_3D_LOCAL_ACF_METADATA",
    "v_3d_local_acf",
]
