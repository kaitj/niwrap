# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_SPAT_NORM_METADATA = Metadata(
    id="8d7db75f92933be52b0cbbed3f0d36b77707ffef",
    name="3dSpatNorm",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dSpatNormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_spat_norm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_head: OutputPathType | None
    """Output dataset (HEAD file)"""
    out_brik: OutputPathType | None
    """Output dataset (BRIK file)"""


def v_3d_spat_norm(
    dataset: InputPathType,
    prefix: str | None = None,
    orig_space: bool = False,
    verbose: bool = False,
    monkey: bool = False,
    marmot: bool = False,
    rat: bool = False,
    human: bool = False,
    bottom_cuts: str | None = None,
    runner: Runner | None = None,
) -> V3dSpatNormOutputs:
    """
    3dSpatNorm by AFNI Team.
    
    An obsolete tool for spatial normalization.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSpatNorm.html
    
    Args:
        dataset: Input dataset.
        prefix: Write output dataset using 'ppp' for the prefix.
        orig_space: Write output dataset using the same grid as dataset.
        verbose: Write out progress reports.
        monkey: Monkey business.
        marmot: Marmoset head.
        rat: Rat head.
        human: Bone head (default).
        bottom_cuts: Make approximate cuts at the bottom to shave non-brain\
            areas. CUTFLAGS is a string of characters indicating which sides to\
            cut: 'A' for anterior, 'P' for posterior, 'R' for right, 'L' for left.\
            Example: -bottom_cuts APLR.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSpatNormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SPAT_NORM_METADATA)
    cargs = []
    cargs.append("3dSpatNorm")
    cargs.append(execution.input_file(dataset))
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if orig_space:
        cargs.append("-orig_space")
    if verbose:
        cargs.append("-verb")
    if monkey:
        cargs.append("-monkey")
    if marmot:
        cargs.append("-marmost")
    if rat:
        cargs.append("-rat")
    if human:
        cargs.append("-human")
    if bottom_cuts is not None:
        cargs.extend(["-bottom_cuts", bottom_cuts])
    ret = V3dSpatNormOutputs(
        root=execution.output_file("."),
        out_head=execution.output_file(f"{prefix}+orig.HEAD") if prefix is not None else None,
        out_brik=execution.output_file(f"{prefix}+orig.BRIK") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSpatNormOutputs",
    "V_3D_SPAT_NORM_METADATA",
    "v_3d_spat_norm",
]