# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DMERGE_METADATA = Metadata(
    id="0cbb2af73cad715e36a0230029c498c4ce2e2119.boutiques",
    name="3dmerge",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset file"""


def v_3dmerge(
    input_files: list[InputPathType],
    output_file: str,
    blur_fwhm: float | None = None,
    threshold: float | None = None,
    clust: list[float] | None = None,
    dindex: float | None = None,
    tindex: float | None = None,
    absolute: bool = False,
    dxyz: bool = False,
    gmean: bool = False,
    gmax: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dmergeOutputs:
    """
    3dmerge edits and merges 3D datasets by applying various operations like
    thresholding, blurring, clustering, and more.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmerge.html
    
    Args:
        input_files: Input dataset files.
        output_file: Output dataset prefix.
        blur_fwhm: Gaussian blur with FWHM in mm.
        threshold: Threshold data to censor the intensities; only valid for\
            'fith', 'fico', or 'fitt' datasets.
        clust: Form clusters with connection distance and clip off data not in\
            clusters of a minimum volume.
        dindex: Specify sub-brick #j as the data source.
        tindex: Specify sub-brick #k as the threshold source.
        absolute: Take absolute values of intensities.
        dxyz: Force cluster editing to behave as if all voxel dimensions were\
            set to 1 mm.
        gmean: Combine datasets by averaging intensities (default).
        gmax: Combine datasets by taking max intensity.
        quiet: Reduce the number of messages shown.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMERGE_METADATA)
    cargs = []
    cargs.append("3dmerge")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.extend([
        "-prefix",
        output_file
    ])
    if blur_fwhm is not None:
        cargs.extend([
            "-1blur_fwhm",
            str(blur_fwhm)
        ])
    if threshold is not None:
        cargs.extend([
            "-1thresh",
            str(threshold)
        ])
    if clust is not None:
        cargs.extend([
            "-1clust",
            *map(str, clust)
        ])
    if dindex is not None:
        cargs.extend([
            "-1dindex",
            str(dindex)
        ])
    if tindex is not None:
        cargs.extend([
            "-1tindex",
            str(tindex)
        ])
    if absolute:
        cargs.append("-1abs")
    if dxyz:
        cargs.append("-dxyz=1")
    if gmean:
        cargs.append("-gmean")
    if gmax:
        cargs.append("-gmax")
    if quiet:
        cargs.append("-quiet")
    ret = V3dmergeOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmergeOutputs",
    "V_3DMERGE_METADATA",
    "v_3dmerge",
]
