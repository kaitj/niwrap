# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SFA2FIELDSIGN_METADATA = Metadata(
    id="673483cb133e81114140c357c0715b77a189756a.boutiques",
    name="sfa2fieldsign",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Sfa2fieldsignParameters = typing.TypedDict('Sfa2fieldsignParameters', {
    "__STYX_TYPE__": typing.Literal["sfa2fieldsign"],
    "sfadir": str,
    "register_dat": str,
    "threshold": typing.NotRequired[float | None],
    "fwhm": typing.NotRequired[float | None],
    "proj_frac": typing.NotRequired[float | None],
    "occip": bool,
    "patch": typing.NotRequired[str | None],
    "osd": typing.NotRequired[str | None],
    "lh": bool,
    "rh": bool,
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
        "sfa2fieldsign": sfa2fieldsign_cargs,
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
        "sfa2fieldsign": sfa2fieldsign_outputs,
    }
    return vt.get(t)


class Sfa2fieldsignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sfa2fieldsign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fsig_bin: OutputPathType
    """Intersection of polar and eccentricity thresholded fieldsigns"""
    eccen_masked: OutputPathType
    """Eccentricity angle (rad) volume masked by fieldsign bin"""
    polar_masked: OutputPathType
    """Polar angle (rad) volume masked by fieldsign bin"""
    eccen_masked_mgh: OutputPathType
    """Masked eccentricity angle sampled on the hemisphere surface"""
    polar_masked_mgh: OutputPathType
    """Masked polar angle sampled on the hemisphere surface"""
    fieldsign_masked_mgh: OutputPathType
    """Masked fieldsign map"""


def sfa2fieldsign_params(
    sfadir: str,
    register_dat: str,
    threshold: float | None = 2,
    fwhm: float | None = 10,
    proj_frac: float | None = 0.5,
    occip: bool = False,
    patch: str | None = None,
    osd: str | None = None,
    lh: bool = False,
    rh: bool = False,
) -> Sfa2fieldsignParameters:
    """
    Build parameters.
    
    Args:
        sfadir: Output directory of sfa-sess.
        register_dat: Registration file.
        threshold: Sigthresh threshold (Default: 2).
        fwhm: Full width at half maximum (FWHM) (Default: 10mm).
        proj_frac: Projection fraction (Default: 0.5).
        occip: Use ?h.occip.patch.flat.
        patch: Use specific patch (?)h.patch.
        osd: Directory under SFA to put output (Default: fieldsign).
        lh: Process left hemisphere only.
        rh: Process right hemisphere only.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sfa2fieldsign",
        "sfadir": sfadir,
        "register_dat": register_dat,
        "occip": occip,
        "lh": lh,
        "rh": rh,
    }
    if threshold is not None:
        params["threshold"] = threshold
    if fwhm is not None:
        params["fwhm"] = fwhm
    if proj_frac is not None:
        params["proj_frac"] = proj_frac
    if patch is not None:
        params["patch"] = patch
    if osd is not None:
        params["osd"] = osd
    return params


def sfa2fieldsign_cargs(
    params: Sfa2fieldsignParameters,
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
    cargs.append("sfa2fieldsign")
    cargs.extend([
        "--sfa",
        params.get("sfadir")
    ])
    cargs.extend([
        "--reg",
        params.get("register_dat")
    ])
    if params.get("threshold") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("threshold"))
        ])
    if params.get("fwhm") is not None:
        cargs.extend([
            "--fwhm",
            str(params.get("fwhm"))
        ])
    if params.get("proj_frac") is not None:
        cargs.extend([
            "--proj-frac",
            str(params.get("proj_frac"))
        ])
    if params.get("occip"):
        cargs.append("--occip")
    if params.get("patch") is not None:
        cargs.extend([
            "--patch",
            params.get("patch")
        ])
    if params.get("osd") is not None:
        cargs.extend([
            "--osd",
            params.get("osd")
        ])
    if params.get("lh"):
        cargs.append("--lh")
    if params.get("rh"):
        cargs.append("--rh")
    return cargs


def sfa2fieldsign_outputs(
    params: Sfa2fieldsignParameters,
    execution: Execution,
) -> Sfa2fieldsignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Sfa2fieldsignOutputs(
        root=execution.output_file("."),
        fsig_bin=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/fsig.bin.nii"),
        eccen_masked=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/eccen.masked.nii"),
        polar_masked=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/polar.masked.nii"),
        eccen_masked_mgh=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/?h.eccen.masked.mgh"),
        polar_masked_mgh=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/?h.polar.masked.mgh"),
        fieldsign_masked_mgh=execution.output_file(params.get("sfadir") + "/[OSD or fieldsign]/?h.fieldsign.masked.mgh"),
    )
    return ret


def sfa2fieldsign_execute(
    params: Sfa2fieldsignParameters,
    execution: Execution,
) -> Sfa2fieldsignOutputs:
    """
    Computes fieldsign map from sfa-sess output. Masks the angle volumes and samples
    them to the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Sfa2fieldsignOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sfa2fieldsign_cargs(params, execution)
    ret = sfa2fieldsign_outputs(params, execution)
    execution.run(cargs)
    return ret


def sfa2fieldsign(
    sfadir: str,
    register_dat: str,
    threshold: float | None = 2,
    fwhm: float | None = 10,
    proj_frac: float | None = 0.5,
    occip: bool = False,
    patch: str | None = None,
    osd: str | None = None,
    lh: bool = False,
    rh: bool = False,
    runner: Runner | None = None,
) -> Sfa2fieldsignOutputs:
    """
    Computes fieldsign map from sfa-sess output. Masks the angle volumes and samples
    them to the surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        sfadir: Output directory of sfa-sess.
        register_dat: Registration file.
        threshold: Sigthresh threshold (Default: 2).
        fwhm: Full width at half maximum (FWHM) (Default: 10mm).
        proj_frac: Projection fraction (Default: 0.5).
        occip: Use ?h.occip.patch.flat.
        patch: Use specific patch (?)h.patch.
        osd: Directory under SFA to put output (Default: fieldsign).
        lh: Process left hemisphere only.
        rh: Process right hemisphere only.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Sfa2fieldsignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SFA2FIELDSIGN_METADATA)
    params = sfa2fieldsign_params(sfadir=sfadir, register_dat=register_dat, threshold=threshold, fwhm=fwhm, proj_frac=proj_frac, occip=occip, patch=patch, osd=osd, lh=lh, rh=rh)
    return sfa2fieldsign_execute(params, execution)


__all__ = [
    "SFA2FIELDSIGN_METADATA",
    "Sfa2fieldsignOutputs",
    "sfa2fieldsign",
    "sfa2fieldsign_params",
]
