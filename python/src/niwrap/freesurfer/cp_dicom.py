# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CP_DICOM_METADATA = Metadata(
    id="e87057efacb16ed69de0523e99719b16d1c3fb64.boutiques",
    name="cp-dicom",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class CpDicomOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cp_dicom(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cp_dicom(
    dicom_dir: str,
    output_dir: str,
    debug: bool = False,
    runner: Runner | None = None,
) -> CpDicomOutputs:
    """
    Copies DICOM files into separate directories for each series based on DICOM
    headers.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dicom_dir: Directory containing DICOM files.
        output_dir: Output directory where sorted DICOM files will be stored.
        debug: Print additional debug information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CpDicomOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CP_DICOM_METADATA)
    cargs = []
    cargs.append("cp-dicom")
    cargs.extend([
        "-d",
        dicom_dir
    ])
    cargs.extend([
        "-o",
        output_dir
    ])
    if debug:
        cargs.append("-debug")
    ret = CpDicomOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CP_DICOM_METADATA",
    "CpDicomOutputs",
    "cp_dicom",
]
