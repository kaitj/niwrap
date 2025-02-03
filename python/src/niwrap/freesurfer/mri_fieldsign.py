# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FIELDSIGN_METADATA = Metadata(
    id="ab824af01a699004ad68775dafe2a065f72a9634.boutiques",
    name="mri_fieldsign",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFieldsignParameters = typing.TypedDict('MriFieldsignParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fieldsign"],
    "fieldsign_file": str,
    "eccen_values": list[float],
    "polar_values": list[float],
    "subject": str,
    "hemisphere": str,
    "patch_file": typing.NotRequired[str | None],
    "occip_flag": bool,
    "sphere_flag": bool,
    "fwhm": typing.NotRequired[float | None],
    "nsmooth": typing.NotRequired[float | None],
    "reverse_flag": bool,
    "old_flag": bool,
    "eccen_rotation": typing.NotRequired[float | None],
    "polar_rotation": typing.NotRequired[float | None],
    "eccen_output": typing.NotRequired[float | None],
    "polar_output": typing.NotRequired[float | None],
    "eccen_sfa_file": typing.NotRequired[InputPathType | None],
    "polar_sfa_file": typing.NotRequired[InputPathType | None],
    "sfa_dir": typing.NotRequired[str | None],
    "sfa_true_flag": bool,
    "debug_flag": bool,
    "checkopts_flag": bool,
    "help_flag": bool,
    "version_flag": bool,
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
        "mri_fieldsign": mri_fieldsign_cargs,
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


def mri_fieldsign_params(
    fieldsign_file: str,
    eccen_values: list[float],
    polar_values: list[float],
    subject: str,
    hemisphere: str,
    patch_file: str | None = None,
    occip_flag: bool = False,
    sphere_flag: bool = False,
    fwhm: float | None = None,
    nsmooth: float | None = None,
    reverse_flag: bool = False,
    old_flag: bool = False,
    eccen_rotation: float | None = None,
    polar_rotation: float | None = None,
    eccen_output: float | None = None,
    polar_output: float | None = None,
    eccen_sfa_file: InputPathType | None = None,
    polar_sfa_file: InputPathType | None = None,
    sfa_dir: str | None = None,
    sfa_true_flag: bool = False,
    debug_flag: bool = False,
    checkopts_flag: bool = False,
    help_flag: bool = False,
    version_flag: bool = False,
) -> MriFieldsignParameters:
    """
    Build parameters.
    
    Args:
        fieldsign_file: Output field sign file.
        eccen_values: Eccentricity values (real and imaginary).
        polar_values: Polar values (real and imaginary).
        subject: Subject identifier.
        hemisphere: Hemisphere to process.
        patch_file: Patch file, without hemi.
        occip_flag: Use occipital patch (patchfile = occip.patch.flat).
        sphere_flag: Use spherical surface instead of patch.
        fwhm: Full-width at half-maximum (mm).
        nsmooth: Number of smoothing steps.
        reverse_flag: Reverse sign.
        old_flag: Use old FS estimation code.
        eccen_rotation: Rotate eccentricity by rotangle degrees.
        polar_rotation: Rotate polar by rotangle degrees.
        eccen_output: Output eccentricity angle.
        polar_output: Output polar angle.
        eccen_sfa_file: Eccentricity self-frequency average file.
        polar_sfa_file: Polar self-frequency average file.
        sfa_dir: SFA directory.
        sfa_true_flag: Use true real and imaginary (affects small smoothing).
        debug_flag: Turn on debugging.
        checkopts_flag: Check options and exit.
        help_flag: Display help information.
        version_flag: Print version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fieldsign",
        "fieldsign_file": fieldsign_file,
        "eccen_values": eccen_values,
        "polar_values": polar_values,
        "subject": subject,
        "hemisphere": hemisphere,
        "occip_flag": occip_flag,
        "sphere_flag": sphere_flag,
        "reverse_flag": reverse_flag,
        "old_flag": old_flag,
        "sfa_true_flag": sfa_true_flag,
        "debug_flag": debug_flag,
        "checkopts_flag": checkopts_flag,
        "help_flag": help_flag,
        "version_flag": version_flag,
    }
    if patch_file is not None:
        params["patch_file"] = patch_file
    if fwhm is not None:
        params["fwhm"] = fwhm
    if nsmooth is not None:
        params["nsmooth"] = nsmooth
    if eccen_rotation is not None:
        params["eccen_rotation"] = eccen_rotation
    if polar_rotation is not None:
        params["polar_rotation"] = polar_rotation
    if eccen_output is not None:
        params["eccen_output"] = eccen_output
    if polar_output is not None:
        params["polar_output"] = polar_output
    if eccen_sfa_file is not None:
        params["eccen_sfa_file"] = eccen_sfa_file
    if polar_sfa_file is not None:
        params["polar_sfa_file"] = polar_sfa_file
    if sfa_dir is not None:
        params["sfa_dir"] = sfa_dir
    return params


def mri_fieldsign_cargs(
    params: MriFieldsignParameters,
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
    cargs.append("mri_fieldsign")
    cargs.extend([
        "--fs",
        params.get("fieldsign_file")
    ])
    cargs.extend([
        "--eccen",
        *map(str, params.get("eccen_values"))
    ])
    cargs.extend([
        "--polar",
        *map(str, params.get("polar_values"))
    ])
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemisphere")
    ])
    if params.get("patch_file") is not None:
        cargs.extend([
            "--patch",
            params.get("patch_file")
        ])
    if params.get("occip_flag"):
        cargs.append("--occip")
    if params.get("sphere_flag"):
        cargs.append("--sphere")
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("nsmooth") is not None:
        cargs.extend([
            "--nsmooth",
            str(params.get("nsmooth"))
        ])
    if params.get("reverse_flag"):
        cargs.append("--rev")
    if params.get("old_flag"):
        cargs.append("--old")
    if params.get("eccen_rotation") is not None:
        cargs.extend([
            "--eccen-rot",
            str(params.get("eccen_rotation"))
        ])
    if params.get("polar_rotation") is not None:
        cargs.extend([
            "--polar-rot",
            str(params.get("polar_rotation"))
        ])
    if params.get("eccen_output") is not None:
        cargs.extend([
            "--eccen-out",
            str(params.get("eccen_output"))
        ])
    if params.get("polar_output") is not None:
        cargs.extend([
            "--polar-out",
            str(params.get("polar_output"))
        ])
    if params.get("eccen_sfa_file") is not None:
        cargs.extend([
            "--eccen-sfa",
            execution.input_file(params.get("eccen_sfa_file"))
        ])
    if params.get("polar_sfa_file") is not None:
        cargs.extend([
            "--polar-sfa",
            execution.input_file(params.get("polar_sfa_file"))
        ])
    if params.get("sfa_dir") is not None:
        cargs.extend([
            "--sfa",
            params.get("sfa_dir")
        ])
    if params.get("sfa_true_flag"):
        cargs.append("--sfa-true")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("checkopts_flag"):
        cargs.append("--checkopts")
    if params.get("help_flag"):
        cargs.append("--help")
    if params.get("version_flag"):
        cargs.append("--version")
    return cargs


def mri_fieldsign_outputs(
    params: MriFieldsignParameters,
    execution: Execution,
) -> MriFieldsignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFieldsignOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_fieldsign_execute(
    params: MriFieldsignParameters,
    execution: Execution,
) -> MriFieldsignOutputs:
    """
    Field Sign Mapping Tool from FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFieldsignOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_fieldsign_cargs(params, execution)
    ret = mri_fieldsign_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fieldsign(
    fieldsign_file: str,
    eccen_values: list[float],
    polar_values: list[float],
    subject: str,
    hemisphere: str,
    patch_file: str | None = None,
    occip_flag: bool = False,
    sphere_flag: bool = False,
    fwhm: float | None = None,
    nsmooth: float | None = None,
    reverse_flag: bool = False,
    old_flag: bool = False,
    eccen_rotation: float | None = None,
    polar_rotation: float | None = None,
    eccen_output: float | None = None,
    polar_output: float | None = None,
    eccen_sfa_file: InputPathType | None = None,
    polar_sfa_file: InputPathType | None = None,
    sfa_dir: str | None = None,
    sfa_true_flag: bool = False,
    debug_flag: bool = False,
    checkopts_flag: bool = False,
    help_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> MriFieldsignOutputs:
    """
    Field Sign Mapping Tool from FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        fieldsign_file: Output field sign file.
        eccen_values: Eccentricity values (real and imaginary).
        polar_values: Polar values (real and imaginary).
        subject: Subject identifier.
        hemisphere: Hemisphere to process.
        patch_file: Patch file, without hemi.
        occip_flag: Use occipital patch (patchfile = occip.patch.flat).
        sphere_flag: Use spherical surface instead of patch.
        fwhm: Full-width at half-maximum (mm).
        nsmooth: Number of smoothing steps.
        reverse_flag: Reverse sign.
        old_flag: Use old FS estimation code.
        eccen_rotation: Rotate eccentricity by rotangle degrees.
        polar_rotation: Rotate polar by rotangle degrees.
        eccen_output: Output eccentricity angle.
        polar_output: Output polar angle.
        eccen_sfa_file: Eccentricity self-frequency average file.
        polar_sfa_file: Polar self-frequency average file.
        sfa_dir: SFA directory.
        sfa_true_flag: Use true real and imaginary (affects small smoothing).
        debug_flag: Turn on debugging.
        checkopts_flag: Check options and exit.
        help_flag: Display help information.
        version_flag: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFieldsignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FIELDSIGN_METADATA)
    params = mri_fieldsign_params(fieldsign_file=fieldsign_file, eccen_values=eccen_values, polar_values=polar_values, subject=subject, hemisphere=hemisphere, patch_file=patch_file, occip_flag=occip_flag, sphere_flag=sphere_flag, fwhm=fwhm, nsmooth=nsmooth, reverse_flag=reverse_flag, old_flag=old_flag, eccen_rotation=eccen_rotation, polar_rotation=polar_rotation, eccen_output=eccen_output, polar_output=polar_output, eccen_sfa_file=eccen_sfa_file, polar_sfa_file=polar_sfa_file, sfa_dir=sfa_dir, sfa_true_flag=sfa_true_flag, debug_flag=debug_flag, checkopts_flag=checkopts_flag, help_flag=help_flag, version_flag=version_flag)
    return mri_fieldsign_execute(params, execution)


__all__ = [
    "MRI_FIELDSIGN_METADATA",
    "mri_fieldsign",
    "mri_fieldsign_params",
]
