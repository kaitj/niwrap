# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TQUAL_METADATA = Metadata(
    id="a5953b420d22f8f6c2b20824e280582d44af991c.boutiques",
    name="3dTqual",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTqualOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tqual(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    time_series: OutputPathType
    """The 1D time series with the quality index for each sub-brick"""


def v_3d_tqual(
    dataset: InputPathType,
    spearman: bool = False,
    quadrant: bool = False,
    autoclip: bool = False,
    automask: bool = False,
    clip: float | None = None,
    mask: InputPathType | None = None,
    range_: bool = False,
    runner: Runner | None = None,
) -> V3dTqualOutputs:
    """
    Computes a quality index for each sub-brick in a 3D+time dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input 3D+time dataset.
        spearman: Quality index is 1 minus the Spearman (rank) correlation\
            coefficient of each sub-brick with the median sub-brick (default\
            method).
        quadrant: Quality index is 1 minus the quadrant correlation coefficient\
            as the quality index.
        autoclip: Clip off low-intensity regions in the median sub-brick, only\
            compute correlation between high-intensity voxels.
        automask: Automatically mask and compute correlation only across\
            high-intensity (presumably brain) voxels.
        clip: Clip off values below given threshold in the median sub-brick.
        mask: Compute correlation only across masked voxels from the given\
            dataset.
        range_: Print the median-3.5*MAD and median+3.5*MAD values with each\
            quality index for plotting.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTqualOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TQUAL_METADATA)
    cargs = []
    cargs.append("3dTqual")
    cargs.append(execution.input_file(dataset))
    if spearman:
        cargs.append("-spearman")
    if quadrant:
        cargs.append("-quadrant")
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if clip is not None:
        cargs.extend([
            "-clip",
            str(clip)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if range_:
        cargs.append("-range")
    ret = V3dTqualOutputs(
        root=execution.output_file("."),
        time_series=execution.output_file("stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTqualOutputs",
    "V_3D_TQUAL_METADATA",
    "v_3d_tqual",
]
