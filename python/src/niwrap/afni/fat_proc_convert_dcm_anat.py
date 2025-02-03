# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_CONVERT_DCM_ANAT_METADATA = Metadata(
    id="b710eae3e3dfce23951c6f5d44bae1dc65d2b536.boutiques",
    name="fat_proc_convert_dcm_anat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatProcConvertDcmAnatParameters = typing.TypedDict('FatProcConvertDcmAnatParameters', {
    "__STYX_TYPE__": typing.Literal["fat_proc_convert_dcm_anat"],
    "nifti_input": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "workdir": typing.NotRequired[str | None],
    "orient": typing.NotRequired[str | None],
    "no_clean": bool,
    "reorig_reorient_off": bool,
    "qc_prefix": typing.NotRequired[str | None],
    "no_cmd_out": bool,
    "no_qc_view": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "fat_proc_convert_dcm_anat": fat_proc_convert_dcm_anat_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "fat_proc_convert_dcm_anat": fat_proc_convert_dcm_anat_outputs,
    }
    return vt.get(t)


class FatProcConvertDcmAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_convert_dcm_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Converted anatomical volume output."""


def fat_proc_convert_dcm_anat_params(
    prefix: str,
    nifti_input: InputPathType | None = None,
    workdir: str | None = None,
    orient: str | None = None,
    no_clean: bool = False,
    reorig_reorient_off: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
) -> FatProcConvertDcmAnatParameters:
    """
    Build parameters.
    
    Args:
        prefix: Set prefix (and path) for output data.
        nifti_input: Input as NIFTI file (zipped or unzipped fine). Alternative\
            to '-indir ..'.
        workdir: Specify a working directory, which can be removed (default\
            name = '__WORKING_convert_dcm_anat').
        orient: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        no_clean: Prevents removal of working directory.
        reorig_reorient_off: Turns off the nicety of putting (0, 0, 0) at\
            brain's center of mass (-> 'reorigin' calc) and reorienting data (->\
            'reorient' calc).
        qc_prefix: Set the prefix of the QC image files separately (default is\
            '').
        no_cmd_out: Don't save the command line call and the location where it\
            was run.
        no_qc_view: Turn off generating QC image files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_proc_convert_dcm_anat",
        "prefix": prefix,
        "no_clean": no_clean,
        "reorig_reorient_off": reorig_reorient_off,
        "no_cmd_out": no_cmd_out,
        "no_qc_view": no_qc_view,
    }
    if nifti_input is not None:
        params["nifti_input"] = nifti_input
    if workdir is not None:
        params["workdir"] = workdir
    if orient is not None:
        params["orient"] = orient
    if qc_prefix is not None:
        params["qc_prefix"] = qc_prefix
    return params


def fat_proc_convert_dcm_anat_cargs(
    params: FatProcConvertDcmAnatParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fat_proc_convert_dcm_anat")
    if params.get("nifti_input") is not None:
        cargs.extend([
            "-innii",
            execution.input_file(params.get("nifti_input"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("workdir") is not None:
        cargs.extend([
            "-workdir",
            params.get("workdir")
        ])
    if params.get("orient") is not None:
        cargs.extend([
            "-orient",
            params.get("orient")
        ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("reorig_reorient_off"):
        cargs.append("-reorig_reorient_off")
    if params.get("qc_prefix") is not None:
        cargs.extend([
            "-qc_prefix",
            params.get("qc_prefix")
        ])
    if params.get("no_cmd_out"):
        cargs.append("-no_cmd_out")
    if params.get("no_qc_view"):
        cargs.append("-no_qc_view")
    return cargs


def fat_proc_convert_dcm_anat_outputs(
    params: FatProcConvertDcmAnatParameters,
    execution: Execution,
) -> FatProcConvertDcmAnatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatProcConvertDcmAnatOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("prefix") + ".nii.gz"),
    )
    return ret


def fat_proc_convert_dcm_anat_execute(
    params: FatProcConvertDcmAnatParameters,
    execution: Execution,
) -> FatProcConvertDcmAnatOutputs:
    """
    Converts an anatomical dataset from DICOM files into a volume, specifically
    designed to fit in line with other processing such as DTI analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmAnatOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fat_proc_convert_dcm_anat_cargs(params, execution)
    ret = fat_proc_convert_dcm_anat_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_proc_convert_dcm_anat(
    prefix: str,
    nifti_input: InputPathType | None = None,
    workdir: str | None = None,
    orient: str | None = None,
    no_clean: bool = False,
    reorig_reorient_off: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    runner: Runner | None = None,
) -> FatProcConvertDcmAnatOutputs:
    """
    Converts an anatomical dataset from DICOM files into a volume, specifically
    designed to fit in line with other processing such as DTI analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Set prefix (and path) for output data.
        nifti_input: Input as NIFTI file (zipped or unzipped fine). Alternative\
            to '-indir ..'.
        workdir: Specify a working directory, which can be removed (default\
            name = '__WORKING_convert_dcm_anat').
        orient: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        no_clean: Prevents removal of working directory.
        reorig_reorient_off: Turns off the nicety of putting (0, 0, 0) at\
            brain's center of mass (-> 'reorigin' calc) and reorienting data (->\
            'reorient' calc).
        qc_prefix: Set the prefix of the QC image files separately (default is\
            '').
        no_cmd_out: Don't save the command line call and the location where it\
            was run.
        no_qc_view: Turn off generating QC image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_CONVERT_DCM_ANAT_METADATA)
    params = fat_proc_convert_dcm_anat_params(nifti_input=nifti_input, prefix=prefix, workdir=workdir, orient=orient, no_clean=no_clean, reorig_reorient_off=reorig_reorient_off, qc_prefix=qc_prefix, no_cmd_out=no_cmd_out, no_qc_view=no_qc_view)
    return fat_proc_convert_dcm_anat_execute(params, execution)


__all__ = [
    "FAT_PROC_CONVERT_DCM_ANAT_METADATA",
    "FatProcConvertDcmAnatOutputs",
    "fat_proc_convert_dcm_anat",
    "fat_proc_convert_dcm_anat_params",
]
