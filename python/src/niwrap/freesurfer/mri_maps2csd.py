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
MriMaps2csdParameters = typing.TypedDict('MriMaps2csdParameters', {
    "__STYX_TYPE__": typing.Literal["mri_maps2csd"],
    "input_files": list[str],
    "csd_file": typing.NotRequired[str | None],
    "pdf_file": typing.NotRequired[str | None],
    "subject_hemi_surf": typing.NotRequired[str | None],
    "thresh": typing.NotRequired[float | None],
    "sign": typing.NotRequired[str | None],
    "csd_apply_file": typing.NotRequired[str | None],
    "apply_out": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "debug": bool,
    "checkopts": bool,
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
        "mri_maps2csd": mri_maps2csd_cargs,
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
    vt = {}
    return vt.get(t)


def mri_maps2csd_params(
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
) -> MriMaps2csdParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_maps2csd",
        "input_files": input_files,
        "debug": debug,
        "checkopts": checkopts,
    }
    if csd_file is not None:
        params["csd_file"] = csd_file
    if pdf_file is not None:
        params["pdf_file"] = pdf_file
    if subject_hemi_surf is not None:
        params["subject_hemi_surf"] = subject_hemi_surf
    if thresh is not None:
        params["thresh"] = thresh
    if sign is not None:
        params["sign"] = sign
    if csd_apply_file is not None:
        params["csd_apply_file"] = csd_apply_file
    if apply_out is not None:
        params["apply_out"] = apply_out
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    return params


def mri_maps2csd_cargs(
    params: MriMaps2csdParameters,
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
    cargs.append("mri_maps2csd")
    cargs.extend([
        "--i",
        *params.get("input_files")
    ])
    if params.get("csd_file") is not None:
        cargs.extend([
            "--csd",
            params.get("csd_file")
        ])
    if params.get("pdf_file") is not None:
        cargs.extend([
            "--pdf",
            params.get("pdf_file")
        ])
    if params.get("subject_hemi_surf") is not None:
        cargs.extend([
            "--s",
            params.get("subject_hemi_surf")
        ])
    if params.get("thresh") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("thresh"))
        ])
    if params.get("sign") is not None:
        cargs.extend([
            "--sign",
            params.get("sign")
        ])
    if params.get("csd_apply_file") is not None:
        cargs.extend([
            "--csd-apply",
            params.get("csd_apply_file")
        ])
    if params.get("apply_out") is not None:
        cargs.append(params.get("apply_out"))
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subjects_dir")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    return cargs


def mri_maps2csd_outputs(
    params: MriMaps2csdParameters,
    execution: Execution,
) -> MriMaps2csdOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriMaps2csdOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_maps2csd_execute(
    params: MriMaps2csdParameters,
    execution: Execution,
) -> MriMaps2csdOutputs:
    """
    Tool to create CSD files and PDFs from input maps and apply them.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriMaps2csdOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_maps2csd_cargs(params, execution)
    ret = mri_maps2csd_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = mri_maps2csd_params(input_files=input_files, csd_file=csd_file, pdf_file=pdf_file, subject_hemi_surf=subject_hemi_surf, thresh=thresh, sign=sign, csd_apply_file=csd_apply_file, apply_out=apply_out, subjects_dir=subjects_dir, debug=debug, checkopts=checkopts)
    return mri_maps2csd_execute(params, execution)


__all__ = [
    "MRI_MAPS2CSD_METADATA",
    "mri_maps2csd",
    "mri_maps2csd_params",
]
