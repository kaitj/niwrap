# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ROI_DECLUSTER_METADATA = Metadata(
    id="410294ea3a285d00e233f31b000eb1bd4e758cb5.boutiques",
    name="ROI decluster",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RoiDeclusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roi_decluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Final output dataset"""


def roi_decluster(
    input_dset: InputPathType,
    output_dir: str | None = None,
    nvox_thresh: float | None = None,
    frac_thresh: float | None = None,
    prefix: str | None = None,
    neighborhood_type: int | None = None,
    runner: Runner | None = None,
) -> RoiDeclusterOutputs:
    """
    Script to remove small clusters or standalone voxels from an ROI/atlas dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dset: Required input dataset. This dataset should be set of\
            integer values. The program mostly assumes approximate isotropic\
            voxels.
        output_dir: Directory name for output. All output goes to this\
            directory.
        nvox_thresh: Number of voxels in a cluster to keep.
        frac_thresh: Fraction of voxels in a cluster to keep [0.0-1.0].
        prefix: Base name of final output dataset, i.e. baseprefix.nii.gz.
        neighborhood_type: Neighborhood type using in finding mode: 1 - facing\
            neighbors, 2 - edges, 3 - corners.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RoiDeclusterOutputs`).
    """
    if neighborhood_type is not None and not (1 <= neighborhood_type <= 3): 
        raise ValueError(f"'neighborhood_type' must be between 1 <= x <= 3 but was {neighborhood_type}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROI_DECLUSTER_METADATA)
    cargs = []
    cargs.append("ROI")
    cargs.append("decluster")
    cargs.extend([
        "-input",
        execution.input_file(input_dset)
    ])
    if output_dir is not None:
        cargs.extend([
            "-outdir",
            output_dir
        ])
    if nvox_thresh is not None:
        cargs.extend([
            "-nvox_thresh",
            str(nvox_thresh)
        ])
    if frac_thresh is not None:
        cargs.extend([
            "-frac_thresh",
            str(frac_thresh)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if neighborhood_type is not None:
        cargs.extend([
            "-NN",
            str(neighborhood_type)
        ])
    ret = RoiDeclusterOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + ".nii.gz") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROI_DECLUSTER_METADATA",
    "RoiDeclusterOutputs",
    "roi_decluster",
]
