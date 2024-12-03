# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEGCENTROIDS_METADATA = Metadata(
    id="60e55d3e62c17ddebe1721176cd1445c815b5c8c.boutiques",
    name="mri_segcentroids",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSegcentroidsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segcentroids(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_centroids: OutputPathType
    """Output text file containing the centroids."""


def mri_segcentroids(
    input_segmentation: InputPathType,
    output_file: str,
    pointset_flag: bool = False,
    registration_file: InputPathType | None = None,
    weights_file: InputPathType | None = None,
    lut_file: InputPathType | None = None,
    default_lut_flag: bool = False,
    runner: Runner | None = None,
) -> MriSegcentroidsOutputs:
    """
    Computes the center of mass for individual structures in a segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_segmentation: Input segmentation volume file.
        output_file: Output text file for centroids.
        pointset_flag: Save centroids as a Freeview pointset (json).
        registration_file: Apply a linear registration (lta).
        weights_file: Compute weighted centroids with provided voxel weights.
        lut_file: Specify label lookup table.
        default_lut_flag: Use default FreeSurferColorLUT.txt for lookup table.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegcentroidsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGCENTROIDS_METADATA)
    cargs = []
    cargs.append("mri_segcentroids")
    cargs.extend([
        "--i",
        execution.input_file(input_segmentation)
    ])
    cargs.extend([
        "--o",
        output_file
    ])
    if pointset_flag:
        cargs.append("--p")
    if registration_file is not None:
        cargs.extend([
            "--reg",
            execution.input_file(registration_file)
        ])
    if weights_file is not None:
        cargs.extend([
            "--weights",
            execution.input_file(weights_file)
        ])
    if lut_file is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(lut_file)
        ])
    if default_lut_flag:
        cargs.append("--ctab-default")
    ret = MriSegcentroidsOutputs(
        root=execution.output_file("."),
        output_centroids=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SEGCENTROIDS_METADATA",
    "MriSegcentroidsOutputs",
    "mri_segcentroids",
]