# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_CONVERT_DCM_DWIS_METADATA = Metadata(
    id="7f33106a46c812f0022cc7b3e2edadb8a7e0a4b3.boutiques",
    name="fat_proc_convert_dcm_dwis",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class FatProcConvertDcmDwisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_convert_dcm_dwis(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_nifti: OutputPathType
    """A NIFTI file with N volumes."""
    output_rvec: OutputPathType
    """A row-wise (3xN) bvec file of the (unit-magnitude) gradient
    orientations."""
    output_bval: OutputPathType
    """A row-wise (1xN) bval file of the gradient magnitudes."""
    output_mat_a: OutputPathType
    """A column-wise (Nx6) AFNI-style matrix file of the (scaled) b-matrix
    values."""
    output_mat_t: OutputPathType
    """A column-wise (Nx6) TORTOISE-style matrix file of the (scaled) b-matrix
    values."""
    output_cvec: OutputPathType
    """A column-wise (Nx3) bvec file of the (b-magn scaled) gradient
    orientations."""


def fat_proc_convert_dcm_dwis(
    dicom_dir: str,
    output_prefix: str,
    nifti_files: list[InputPathType] | None = None,
    bvec_files: list[InputPathType] | None = None,
    bval_files: list[InputPathType] | None = None,
    work_dir: str | None = None,
    orientation: str | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    no_flip: bool = False,
    qc_prefix: str | None = None,
    reorient_off: bool = False,
    no_clean: bool = False,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    do_movie: str | None = None,
    runner: Runner | None = None,
) -> FatProcConvertDcmDwisOutputs:
    """
    Convert sets of DWIs in DICOM format into 'nicer' volume+grad format, reorient
    volumetric data, and glue together multiple sessions/directories of data.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_proc_convert_dcm_dwis.html
    
    Args:
        dicom_dir: Directory of DICOM files of the DWI data with 'AP' phase\
            encoding. Can contain a wildcard expression for several directories.
        output_prefix: Prefix (and path) for output data (e.g., *.nii.gz,\
            *.bvec, *.bval files). Required.
        nifti_files: One or more NIFTI files of DWIs.
        bvec_files: One or more row-wise, gradient (unit-magnitude) files\
            (e.g., *.bvec).
        bval_files: One or more bvalue files (e.g., *.bval).
        work_dir: Optional working directory for intermediate files.
        orientation: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        flip_x: Flip gradients along the X-axis.
        flip_y: Flip gradients along the Y-axis.
        flip_z: Flip gradients along the Z-axis.
        no_flip: Prevent flipping of gradients (default).
        qc_prefix: Set the prefix for QC image files separately (default is\
            '').
        reorient_off: Turn off reorigin calculation and reorientation.
        no_clean: Do not remove the working directory of intermediate files\
            (default is to delete it).
        no_cmd_out: Do not save the command line call and location where it was\
            run.
        no_qc_view: Do not generate QC image files.
        do_movie: Generate a movie of the newly created dataset (AGIF or MPEG).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmDwisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_CONVERT_DCM_DWIS_METADATA)
    cargs = []
    cargs.append("fat_proc_convert_dcm_dwis")
    cargs.append("-indir")
    cargs.append(dicom_dir)
    cargs.append("-prefix")
    cargs.append(output_prefix)
    cargs.append("-innii")
    if nifti_files is not None:
        cargs.extend([execution.input_file(f) for f in nifti_files])
    cargs.append("-inbvec")
    if bvec_files is not None:
        cargs.extend([execution.input_file(f) for f in bvec_files])
    cargs.append("-inbval")
    if bval_files is not None:
        cargs.extend([execution.input_file(f) for f in bval_files])
    cargs.append("-workdir")
    if work_dir is not None:
        cargs.append(work_dir)
    cargs.append("-orient")
    if orientation is not None:
        cargs.append(orientation)
    cargs.append("-origin_xyz")
    cargs.append("[ORIGIN_X]")
    cargs.append("[ORIGIN_Y]")
    cargs.append("[ORIGIN_Z]")
    cargs.append("-flip_x")
    if flip_x:
        cargs.append("-flip_x")
    cargs.append("-flip_y")
    if flip_y:
        cargs.append("-flip_y")
    cargs.append("-flip_z")
    if flip_z:
        cargs.append("-flip_z")
    cargs.append("-no_flip")
    if no_flip:
        cargs.append("-no_flip")
    cargs.append("-qc_prefix")
    if qc_prefix is not None:
        cargs.append(qc_prefix)
    cargs.append("-reorig_reorient_off")
    if reorient_off:
        cargs.append("-reorig_reorient_off")
    cargs.append("-no_clean")
    if no_clean:
        cargs.append("-no_clean")
    cargs.append("-no_cmd_out")
    if no_cmd_out:
        cargs.append("-no_cmd_out")
    cargs.append("-no_qc_view")
    if no_qc_view:
        cargs.append("-no_qc_view")
    cargs.append("-do_movie")
    if do_movie is not None:
        cargs.extend([
            "-do_movie",
            do_movie
        ])
    ret = FatProcConvertDcmDwisOutputs(
        root=execution.output_file("."),
        output_nifti=execution.output_file(output_prefix + ".nii.gz"),
        output_rvec=execution.output_file(output_prefix + ".rvec"),
        output_bval=execution.output_file(output_prefix + ".bval"),
        output_mat_a=execution.output_file(output_prefix + "_matA.dat"),
        output_mat_t=execution.output_file(output_prefix + "_matT.dat"),
        output_cvec=execution.output_file(output_prefix + "_cvec.dat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_CONVERT_DCM_DWIS_METADATA",
    "FatProcConvertDcmDwisOutputs",
    "fat_proc_convert_dcm_dwis",
]