# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMDIR_INFO_MGH_METADATA = Metadata(
    id="8a135eb2c424e8fca3c65b45cb1c892c036acc1e.boutiques",
    name="dcmdir-info-mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DcmdirInfoMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmdir_info_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_mgz_files: OutputPathType
    """Converted DICOM files to MGZ format with naming sequencename_runR.mgz,
    where R is the run number"""


def dcmdir_info_mgh(
    dicomdir: str,
    unpackdir: str | None = None,
    version: bool = False,
    help_: bool = False,
    nopre: bool = False,
    runner: Runner | None = None,
) -> DcmdirInfoMghOutputs:
    """
    Scans a DICOM directory and extracts information about each series.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dicomdir: Input DICOM directory.
        unpackdir: Directory where the unpacked data will be stored (optional).\
            If specified, DICOM files are converted to MGZ format.
        version: Print version and exit.
        help_: Print help and exit.
        nopre: Do not assume filenames use the NNNNNN- prefix convention.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmdirInfoMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMDIR_INFO_MGH_METADATA)
    cargs = []
    cargs.append("dcmdir-info-mgh")
    cargs.append(dicomdir)
    if unpackdir is not None:
        cargs.append(unpackdir)
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    if nopre:
        cargs.append("--nopre")
    ret = DcmdirInfoMghOutputs(
        root=execution.output_file("."),
        converted_mgz_files=execution.output_file("sequencename_run*.mgz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMDIR_INFO_MGH_METADATA",
    "DcmdirInfoMghOutputs",
    "dcmdir_info_mgh",
]