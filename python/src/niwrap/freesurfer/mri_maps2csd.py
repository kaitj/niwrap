# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MAPS2CSD_METADATA = Metadata(
    id="86fc4f48b601867360afe87e657c1be456f995cd.boutiques",
    name="mri_maps2csd",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriMaps2csdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_maps2csd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_maps2csd(
    input_files: list[str],
    csd_file: str | None = None,
    pdf_file: str | None = None,
    subject_hemi_surf: str | None = None,
    thresh: float | None = None,
    sign: str | None = None,
    csd_apply_file: str | None = None,
    apply_out: str | None = None,
    subjects_dir: str | None = None,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MriMaps2csdOutputs:
    """
    Tool to create CSD files and PDFs from input maps and apply them.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input file(s) or specify them directly on the command line.
        csd_file: Output CSD file.
        pdf_file: PDF file created from CSD.
        subject_hemi_surf: Subject name, hemisphere, and surface specification.
        thresh: Threshold for cluster-forming (-log10 scale).
        sign: Sign adjustment for threshold (+1, -1 or 0).
        csd_apply_file: Apply a CSD file to inputs, return p-value of max\
            cluster.
        apply_out:.
        subjects_dir: Subjects directory.
        debug: Turn on debugging.
        checkopts: Don't run, just check options then exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMaps2csdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MAPS2CSD_METADATA)
    cargs = []
    cargs.append("mri_maps2csd")
    cargs.extend([
        "--i",
        *input_files
    ])
    if csd_file is not None:
        cargs.extend([
            "--csd",
            csd_file
        ])
    if pdf_file is not None:
        cargs.extend([
            "--pdf",
            pdf_file
        ])
    if subject_hemi_surf is not None:
        cargs.extend([
            "--s",
            subject_hemi_surf
        ])
    if thresh is not None:
        cargs.extend([
            "--thresh",
            str(thresh)
        ])
    if sign is not None:
        cargs.extend([
            "--sign",
            sign
        ])
    if csd_apply_file is not None:
        cargs.extend([
            "--csd-apply",
            csd_apply_file
        ])
    if apply_out is not None:
        cargs.append(apply_out)
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = MriMaps2csdOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_MAPS2CSD_METADATA",
    "MriMaps2csdOutputs",
    "mri_maps2csd",
]
