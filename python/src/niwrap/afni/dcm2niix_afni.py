# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCM2NIIX_AFNI_METADATA = Metadata(
    id="3383de2437c0051596b4454348bb01994bf4c301.boutiques",
    name="dcm2niix_afni",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class Dcm2niixAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcm2niix_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    nifti_files: OutputPathType
    """The main output NIfTI files"""


def dcm2niix_afni(
    input_folder: str,
    compression_level: int | None = None,
    adjacent_dicoms: str | None = None,
    bids_sidecar: str | None = None,
    anonymize_bids: str | None = None,
    comment: str | None = None,
    directory_search_depth: int | None = None,
    export_format: str | None = None,
    filename_template: str | None = None,
    generate_defaults: str | None = None,
    ignore_images: str | None = None,
    lossless_scale: str | None = None,
    merge_slices: str | None = None,
    series_crc_number: list[str] | None = None,
    output_directory: str | None = None,
    phillips_scaling: str | None = None,
    rename_dicoms: str | None = None,
    single_file_mode: str | None = None,
    up_to_date: bool = False,
    verbose: str | None = None,
    write_behavior: int | None = None,
    crop_3d: str | None = None,
    gz_compress: str | None = None,
    big_endian: str | None = None,
    progress: str | None = None,
    ignore_trigger_times: bool = False,
    terse: bool = False,
    version: bool = False,
    xml_: bool = False,
    runner: Runner | None = None,
) -> Dcm2niixAfniOutputs:
    """
    DICOM to NIfTI converter optimized for AFNI.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/dcm2niix_afni.html
    
    Args:
        input_folder: Folder containing DICOM files.
        compression_level: GZ compression level (1=fastest..9=smallest, default\
            6).
        adjacent_dicoms: Adjacent DICOMs (images from same series always in\
            same folder) for faster conversion (n/y, default n).
        bids_sidecar: BIDS sidecar (y/n/o [o=only: no NIfTI], default y).
        anonymize_bids: Anonymize BIDS (y/n, default y).
        comment: Comment stored in NIfTI aux_file (provide up to 24 characters\
            e.g. '-c first_visit').
        directory_search_depth: Directory search depth. Convert DICOMs in\
            sub-folders of in_folder? (0..9, default 5).
        export_format: Export as NRRD (y) or MGH (o) instead of NIfTI (y/n/o,\
            default n).
        filename_template: Filename template for output (default '%f_%p_%t_%s').
        generate_defaults: Generate defaults file (y/n/o/i [o=only: reset and\
            write defaults; i=ignore: reset defaults], default n).
        ignore_images: Ignore derived, localizer and 2D images (y/n, default n).
        lossless_scale: Losslessly scale 16-bit integers to use dynamic range\
            (y/n/o, default o).
        merge_slices: Merge 2D slices from same series regardless of echo,\
            exposure, etc. (n/y or 0/1/2, default 2).
        series_crc_number: Only convert this series CRC number - can be used up\
            to 16 times (default convert all).
        output_directory: Output directory (omit to save to input folder).
        phillips_scaling: Philips precise float (not display) scaling (y/n,\
            default y).
        rename_dicoms: Rename instead of convert DICOMs (y/n, default n).
        single_file_mode: Single file mode, do not convert other images in\
            folder (y/n, default n).
        up_to_date: Up-to-date check.
        verbose: Verbose (n/y or 0/1/2, default 0).
        write_behavior: Write behavior for name conflicts (0=skip duplicates,\
            1=overwrite, 2=add suffix).
        crop_3d: Crop 3D acquisitions (y/n/i, default n, use 'i'gnore to\
            neither crop nor rotate 3D acquisitions).
        gz_compress: GZ compress images (y/o/i/n/3, default n) [y=pigz,\
            o=optimal pigz, i=internal:miniz, n=no, 3=no,3D].
        big_endian: Byte order (y/n/o, default o) [y=big-endian,\
            n=little-endian, o=optimal/native].
        progress: Slicer format progress information (y/n, default n).
        ignore_trigger_times: Disregard values in 0018, 1060 and 0020, 9153.
        terse: Omit filename post-fixes (can cause overwrites).
        version: Report version.
        xml_: Slicer format features.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Dcm2niixAfniOutputs`).
    """
    if series_crc_number is not None and not (len(series_crc_number) <= 16): 
        raise ValueError(f"Length of 'series_crc_number' must be less than 16 but was {len(series_crc_number)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCM2NIIX_AFNI_METADATA)
    cargs = []
    cargs.append("dcm2niix_afni")
    cargs.append(input_folder)
    if compression_level is not None:
        cargs.extend([
            "-1..-9",
            str(compression_level)
        ])
    if adjacent_dicoms is not None:
        cargs.extend([
            "-a",
            adjacent_dicoms
        ])
    if bids_sidecar is not None:
        cargs.extend([
            "-b",
            bids_sidecar
        ])
    if anonymize_bids is not None:
        cargs.extend([
            "-ba",
            anonymize_bids
        ])
    if comment is not None:
        cargs.extend([
            "-c",
            comment
        ])
    if directory_search_depth is not None:
        cargs.extend([
            "-d",
            str(directory_search_depth)
        ])
    if export_format is not None:
        cargs.extend([
            "-e",
            export_format
        ])
    if filename_template is not None:
        cargs.extend([
            "-f",
            filename_template
        ])
    if generate_defaults is not None:
        cargs.extend([
            "-g",
            generate_defaults
        ])
    if ignore_images is not None:
        cargs.extend([
            "-i",
            ignore_images
        ])
    if lossless_scale is not None:
        cargs.extend([
            "-l",
            lossless_scale
        ])
    if merge_slices is not None:
        cargs.extend([
            "-m",
            merge_slices
        ])
    if series_crc_number is not None:
        cargs.extend([
            "-n",
            *series_crc_number
        ])
    if output_directory is not None:
        cargs.extend([
            "-o",
            output_directory
        ])
    if phillips_scaling is not None:
        cargs.extend([
            "-p",
            phillips_scaling
        ])
    if rename_dicoms is not None:
        cargs.extend([
            "-r",
            rename_dicoms
        ])
    if single_file_mode is not None:
        cargs.extend([
            "-s",
            single_file_mode
        ])
    if up_to_date:
        cargs.append("-u")
    if verbose is not None:
        cargs.extend([
            "-v",
            verbose
        ])
    if write_behavior is not None:
        cargs.extend([
            "-w",
            str(write_behavior)
        ])
    if crop_3d is not None:
        cargs.extend([
            "-x",
            crop_3d
        ])
    if gz_compress is not None:
        cargs.extend([
            "-z",
            gz_compress
        ])
    if big_endian is not None:
        cargs.extend([
            "--big-endian",
            big_endian
        ])
    if progress is not None:
        cargs.extend([
            "--progress",
            progress
        ])
    if ignore_trigger_times:
        cargs.append("--ignore_trigger_times")
    if terse:
        cargs.append("--terse")
    if version:
        cargs.append("--version")
    if xml_:
        cargs.append("--xml")
    ret = Dcm2niixAfniOutputs(
        root=execution.output_file("."),
        nifti_files=execution.output_file("<OUTPUT_DIRECTORY>/*.nii"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCM2NIIX_AFNI_METADATA",
    "Dcm2niixAfniOutputs",
    "dcm2niix_afni",
]
