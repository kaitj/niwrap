# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_QWARP_METADATA = Metadata(
    id="1954e260f585075fec9612b08bcb8ffeb56ed87f.boutiques",
    name="3dQwarp",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dQwarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_qwarp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warped_dataset: OutputPathType
    """Warped dataset"""
    warp_dataset: OutputPathType
    """Warp dataset"""
    inverse_warp_dataset: OutputPathType
    """Inverse warp dataset"""


def v_3d_qwarp(
    base_dataset: InputPathType,
    source_dataset: InputPathType,
    prefix: str,
    no_warp: bool = False,
    inverse_warp: bool = False,
    no_dataset: bool = False,
    a_warp: bool = False,
    pcl: bool = False,
    pear: bool = False,
    hel: bool = False,
    mi: bool = False,
    nmi: bool = False,
    lpc: bool = False,
    lpa: bool = False,
    noneg: bool = False,
    nopenalty: bool = False,
    minpatch: float | None = None,
    maxlev: float | None = None,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dQwarpOutputs:
    """
    Computes a nonlinearly warped version of source_dataset to match base_dataset.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dQwarp.html
    
    Args:
        base_dataset: Base dataset.
        source_dataset: Source dataset.
        prefix: Prefix for the output datasets.
        no_warp: Do not save the _WARP file.
        inverse_warp: Compute and save the _WARPINV file.
        no_dataset: Do not save the warped source dataset.
        a_warp: Output the nonlinear warp when -allineate is used.
        pcl: Clipped Pearson correlation (default method).
        pear: Use strict Pearson correlation for matching.
        hel: Use Hellinger metric for matching.
        mi: Use Mutual Information for matching.
        nmi: Use Normalized Mutual Information for matching.
        lpc: Use Local Pearson correlation (signed) for matching.
        lpa: Use Local Pearson correlation (absolute value) for matching.
        noneg: Replace negative values in either input volume with 0.
        nopenalty: Don't use a penalty on the cost functional.
        minpatch: Set the minimum patch size for warp searching.
        maxlev: Set the maximum refinement level.
        verbose: Print out very verbose progress messages.
        quiet: Cut out most progress messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dQwarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_QWARP_METADATA)
    cargs = []
    cargs.append("3dQwarp")
    cargs.append(execution.input_file(base_dataset))
    cargs.append(execution.input_file(source_dataset))
    cargs.append(prefix)
    if no_warp:
        cargs.append("-nowarp")
    if inverse_warp:
        cargs.append("-iwarp")
    if no_dataset:
        cargs.append("-nodset")
    if a_warp:
        cargs.append("-awarp")
    if pcl:
        cargs.append("-pcl")
    if pear:
        cargs.append("-pear")
    if hel:
        cargs.append("-hel")
    if mi:
        cargs.append("-mi")
    if nmi:
        cargs.append("-nmi")
    if lpc:
        cargs.append("-lpc")
    if lpa:
        cargs.append("-lpa")
    if noneg:
        cargs.append("-noneg")
    if nopenalty:
        cargs.append("-nopenalty")
    if minpatch is not None:
        cargs.extend([
            "-minpatch",
            str(minpatch)
        ])
    if maxlev is not None:
        cargs.extend([
            "-maxlev",
            str(maxlev)
        ])
    if verbose:
        cargs.append("-verb")
    if quiet:
        cargs.append("-quiet")
    ret = V3dQwarpOutputs(
        root=execution.output_file("."),
        warped_dataset=execution.output_file("{PREFIX}+tlrc"),
        warp_dataset=execution.output_file("{PREFIX}_WARP+tlrc"),
        inverse_warp_dataset=execution.output_file("{PREFIX}_WARPINV+tlrc"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dQwarpOutputs",
    "V_3D_QWARP_METADATA",
    "v_3d_qwarp",
]
