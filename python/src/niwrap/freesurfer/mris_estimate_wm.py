# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_ESTIMATE_WM_METADATA = Metadata(
    id="cac77a4401a904ea7c3d8eb641009c3991349f87.boutiques",
    name="mris_estimate_wm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisEstimateWmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_estimate_wm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_estimate_wm(
    subjs: list[str],
    hemi: str,
    sdir: str | None = None,
    model: str | None = None,
    suffix: str | None = None,
    gpu: bool = False,
    rsi: bool = False,
    single_iter: bool = False,
    vol: str | None = None,
    runner: Runner | None = None,
) -> MrisEstimateWmOutputs:
    """
    Tool to estimate white matter surfaces using MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjs: List of subjects to process.
        hemi: Hemisphere to reconstruct (lh or rh).
        sdir: Override SUBJECTS_DIR.
        model: Override default model.
        suffix: Suffix of output surface (default is 'topofit').
        gpu: Use the GPU.
        rsi: Remove self-intersecting faces during the deformation.
        single_iter: Prevent deformation steps from running more than once.
        vol: Subject volume to use as input.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisEstimateWmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ESTIMATE_WM_METADATA)
    cargs = []
    cargs.append("mris_estimate_wm")
    cargs.extend([
        "-s",
        *subjs
    ])
    cargs.extend([
        "--hemi",
        hemi
    ])
    if sdir is not None:
        cargs.extend([
            "-d",
            sdir
        ])
    if model is not None:
        cargs.extend([
            "-m",
            model
        ])
    if suffix is not None:
        cargs.extend([
            "-x",
            suffix
        ])
    if gpu:
        cargs.append("-g")
    if rsi:
        cargs.append("--rsi")
    if single_iter:
        cargs.append("--single-iter")
    if vol is not None:
        cargs.extend([
            "--vol",
            vol
        ])
    ret = MrisEstimateWmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_ESTIMATE_WM_METADATA",
    "MrisEstimateWmOutputs",
    "mris_estimate_wm",
]
