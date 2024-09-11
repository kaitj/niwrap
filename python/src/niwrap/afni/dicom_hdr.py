# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DICOM_HDR_METADATA = Metadata(
    id="7940d1c952c1985b31235192fa73e53002e6d4f9.boutiques",
    name="dicom_hdr",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class DicomHdrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dicom_hdr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dicom_hdr(
    files: list[InputPathType],
    runner: Runner | None = None,
) -> DicomHdrOutputs:
    """
    A tool to print DICOM file information to stdout.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/dicom_hdr.html
    
    Args:
        files: DICOM file(s) to read.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DicomHdrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DICOM_HDR_METADATA)
    cargs = []
    cargs.append("dicom_hdr")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in files])
    ret = DicomHdrOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DICOM_HDR_METADATA",
    "DicomHdrOutputs",
    "dicom_hdr",
]