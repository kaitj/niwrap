# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_LOCAL_ACF_METADATA = Metadata(
    id="094cded0efef3b7559949d0f09a20f4361673f6d",
    name="3dLocalACF",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    input_file: InputPathType,
    prefix: str,
    neighborhood: str | None = None,
    mask_file: InputPathType | None = None,
    auto_mask: bool = False,
    runner: Runner | None = None,
) -> V3dLocalAcfOutputs:
    """
    3dLocalACF by AFNI Team.
    
    Estimate the spatial AutoCorrelation Function (ACF) locally in a
    neighborhood around each voxel.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dLocalACF.html
    
    Args:
        input_file: Input time series dataset.
        prefix: Prefix for output dataset.
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
    cargs.extend(["-prefix", prefix])
    cargs.append(execution.input_file(input_file))
    if neighborhood is not None:
        cargs.extend(["-nbhd", neighborhood])
    if mask_file is not None:
        cargs.extend(["-mask", execution.input_file(mask_file)])
    if auto_mask:
        cargs.append("-automask")
    ret = V3dLocalAcfOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{prefix}.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dLocalAcfOutputs",
    "V_3D_LOCAL_ACF_METADATA",
    "v_3d_local_acf",
]