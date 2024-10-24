# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RECON_ALL_CLINICAL_SH_METADATA = Metadata(
    id="38aa6da8e0504acf21091c65fc76ff6026418cb2.boutiques",
    name="recon-all-clinical.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ReconAllClinicalShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `recon_all_clinical_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def recon_all_clinical_sh(
    input_scan: InputPathType,
    subject_id: str,
    threads: int,
    subject_dir: str | None = None,
    runner: Runner | None = None,
) -> ReconAllClinicalShOutputs:
    """
    Recon-all-like stream for processing clinical brain MRI scans of arbitrary
    orientation, resolution, and contrast using SynthSeg and SynthSR.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_scan: Input scan file to be processed.
        subject_id: Identifier for the subject being processed.
        threads: Number of threads to use for processing.
        subject_dir: Optional subjects directory. Only necessary if the\
            environment variable SUBJECTS_DIR is not set or needs to be overridden.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconAllClinicalShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECON_ALL_CLINICAL_SH_METADATA)
    cargs = []
    cargs.append("recon-all-clinical.sh")
    cargs.append(execution.input_file(input_scan))
    cargs.append(subject_id)
    cargs.append(str(threads))
    if subject_dir is not None:
        cargs.append(subject_dir)
    ret = ReconAllClinicalShOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RECON_ALL_CLINICAL_SH_METADATA",
    "ReconAllClinicalShOutputs",
    "recon_all_clinical_sh",
]
