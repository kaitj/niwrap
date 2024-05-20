# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


V_3D_DEGREE_CENTRALITY_METADATA = Metadata(
    id="ed259d22b5331de010f683c90fb01c0fcb129871",
    name="3dDegreeCentrality",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dDegreeCentralityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_degree_centrality(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    oned_file_outfile: OutputPathType | None
    """The text output of the similarity matrix computed after thresholding with one-dimensional and ijk voxel indices, correlations, image extents, and affine matrix."""


def v_3d_degree_centrality(
    runner: Runner,
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    oned_file: str | None = None,
    polort: int | None = None,
    sparsity: float | int | None = None,
    thresh: float | int | None = None,
) -> V3dDegreeCentralityOutputs:
    """
    Computes voxelwise weighted and binary degree centrality and stores the result
    in a new 3D bucket dataset as floats to preserve their values. Degree centrality
    reflects the strength and extent of the correlation of a voxel with every other
    voxel in the brain.
    
    Args:
        runner: Command runner
        in_file: Input file to 3ddegreecentrality.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        mask: Mask file to mask input data.
        oned_file: Output filepath to text dump of correlation matrix.
        polort: No description provided.
        sparsity: Only take the top percent of connections.
        thresh: Threshold to exclude connections where corr <= thresh.
    Returns:
        NamedTuple of outputs (described in `V3dDegreeCentralityOutputs`).
    """
    execution = runner.start_execution(V_3D_DEGREE_CENTRALITY_METADATA)
    cargs = []
    cargs.append("3dDegreeCentrality")
    cargs.append(execution.input_file(in_file))
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if oned_file is not None:
        cargs.extend(["-out1D", oned_file])
    cargs.append("[OUT_FILE]")
    if polort is not None:
        cargs.extend(["-polort", str(polort)])
    if sparsity is not None:
        cargs.extend(["-sparsity", str(sparsity)])
    if thresh is not None:
        cargs.extend(["-thresh", str(thresh)])
    ret = V3dDegreeCentralityOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).stem}", optional=True),
        oned_file_outfile=execution.output_file(f"{oned_file}", optional=True) if oned_file is not None else None,
    )
    execution.run(cargs)
    return ret
