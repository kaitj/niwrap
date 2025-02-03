# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CVS_REGISTER_METADATA = Metadata(
    id="bb0813a0151b53cc7fd810cb07043b52e37cd609.boutiques",
    name="mri_cvs_register",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriCvsRegisterParameters = typing.TypedDict('MriCvsRegisterParameters', {
    "__STYX_TYPE__": typing.Literal["mri_cvs_register"],
    "mov_subjid": str,
    "template_subjid": typing.NotRequired[str | None],
    "templatedir": typing.NotRequired[str | None],
    "mni_flag": bool,
    "outdir": typing.NotRequired[str | None],
    "asegfname": typing.NotRequired[str | None],
    "voltype": typing.NotRequired[str | None],
    "step1_flag": bool,
    "step2_flag": bool,
    "step3_flag": bool,
    "noaseg_flag": bool,
    "nointensity_flag": bool,
    "hemi_flag": bool,
    "masktargethemi_flag": bool,
    "maskmovinghemi_flag": bool,
    "nocleanup_flag": bool,
    "keepelreg_flag": bool,
    "keepallm3z_flag": bool,
    "cleanall_flag": bool,
    "cleansurfreg_flag": bool,
    "cleanelreg_flag": bool,
    "cleanvolreg_flag": bool,
    "m3d_flag": bool,
    "openmp": typing.NotRequired[int | None],
    "nolog_flag": bool,
    "version_flag": bool,
    "help_flag": bool,
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
        "mri_cvs_register": mri_cvs_register_cargs,
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
        "mri_cvs_register": mri_cvs_register_outputs,
    }
    return vt.get(t)


class MriCvsRegisterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cvs_register(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    final_cvs_morph: OutputPathType | None
    """The final morph that combines correspondences recovered in all
    registration steps."""
    final_cvs_morphed_norm: OutputPathType | None
    """The CVS morphed norm.mgz file; final result of CVS with all registration
    steps contributions."""
    final_cvs_morphed_aseg: OutputPathType | None
    """The CVS morphed aseg.mgz file with all registration steps
    contributions."""
    step1_morphed_aseg: OutputPathType | None
    """Morphed aseg.mgz file result of CVS up to step (3)(i) and contains elatic
    morph and aseg-based nonlinear registration."""
    step1_morphed_norm: OutputPathType | None
    """Morphed norm.mgz file result of CVS up to step (3)(i) and contains elatic
    morph and aseg-based nonlinear registration."""


def mri_cvs_register_params(
    mov_subjid: str,
    template_subjid: str | None = None,
    templatedir: str | None = None,
    mni_flag: bool = False,
    outdir: str | None = None,
    asegfname: str | None = None,
    voltype: str | None = None,
    step1_flag: bool = False,
    step2_flag: bool = False,
    step3_flag: bool = False,
    noaseg_flag: bool = False,
    nointensity_flag: bool = False,
    hemi_flag: bool = False,
    masktargethemi_flag: bool = False,
    maskmovinghemi_flag: bool = False,
    nocleanup_flag: bool = False,
    keepelreg_flag: bool = False,
    keepallm3z_flag: bool = False,
    cleanall_flag: bool = False,
    cleansurfreg_flag: bool = False,
    cleanelreg_flag: bool = False,
    cleanvolreg_flag: bool = False,
    m3d_flag: bool = False,
    openmp: int | None = None,
    nolog_flag: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
) -> MriCvsRegisterParameters:
    """
    Build parameters.
    
    Args:
        mov_subjid: FreeSurfer subject name as found in $SUBJECTS_DIR. This\
            identifies the subject that is to be moved / registered to the target.
        template_subjid: FreeSurfer subject name as found in $SUBJECTS_DIR (or\
            --templatedir). This identifies the subject that is to be kept fixed\
            (template).
        templatedir: Directory of the template subject's SUBJECTS_DIR if\
            different from that of the moving subject.
        mni_flag: Use the CVS atlas in MNI152 space as a target for\
            registration.
        outdir: Name of the output directory where all the registration results\
            are written.
        asegfname: Name of the segmentation volume used in volumetric\
            registration step. Do not use the file extension.
        voltype: Changes the input from norm.mgz to voltype.mgz.
        step1_flag: Only do step 1 (spherical registration).
        step2_flag: Only do step 2 (elastic registration).
        step3_flag: Only do step 3 (volumetric registration).
        noaseg_flag: Do not use aseg volumes in the volumetric registration\
            pipeline.
        nointensity_flag: Do not use intensity volumes in the volumetric\
            registration pipeline.
        hemi_flag: Run CVS registration only on one hemisphere.
        masktargethemi_flag: Use with --hemi when hemi is registered to full\
            brain target.
        maskmovinghemi_flag: Use with --hemi when full brain is registered to\
            single hemi target.
        nocleanup_flag: Do not delete temporary files.
        keepelreg_flag: Do not delete elastic registration outcomes.
        keepallm3z_flag: Do not delete m3z morph files computed during CVS.
        cleanall_flag: Overwrite / recompute all CVS-related morphs.
        cleansurfreg_flag: Overwrite/recompute CVS-related surface registration\
            morphs.
        cleanelreg_flag: Overwrite / recompute CVS-related elastic registration\
            morph.
        cleanvolreg_flag: Overwrite / recompute CVS-related volumetric morphs.
        m3d_flag: Use m3d instead of m3z for registration morphs.
        openmp: Assign the number of nodes for openmp runs.
        nolog_flag: Do not produce a log file.
        version_flag: Print version and exit.
        help_flag: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_cvs_register",
        "mov_subjid": mov_subjid,
        "mni_flag": mni_flag,
        "step1_flag": step1_flag,
        "step2_flag": step2_flag,
        "step3_flag": step3_flag,
        "noaseg_flag": noaseg_flag,
        "nointensity_flag": nointensity_flag,
        "hemi_flag": hemi_flag,
        "masktargethemi_flag": masktargethemi_flag,
        "maskmovinghemi_flag": maskmovinghemi_flag,
        "nocleanup_flag": nocleanup_flag,
        "keepelreg_flag": keepelreg_flag,
        "keepallm3z_flag": keepallm3z_flag,
        "cleanall_flag": cleanall_flag,
        "cleansurfreg_flag": cleansurfreg_flag,
        "cleanelreg_flag": cleanelreg_flag,
        "cleanvolreg_flag": cleanvolreg_flag,
        "m3d_flag": m3d_flag,
        "nolog_flag": nolog_flag,
        "version_flag": version_flag,
        "help_flag": help_flag,
    }
    if template_subjid is not None:
        params["template_subjid"] = template_subjid
    if templatedir is not None:
        params["templatedir"] = templatedir
    if outdir is not None:
        params["outdir"] = outdir
    if asegfname is not None:
        params["asegfname"] = asegfname
    if voltype is not None:
        params["voltype"] = voltype
    if openmp is not None:
        params["openmp"] = openmp
    return params


def mri_cvs_register_cargs(
    params: MriCvsRegisterParameters,
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
    cargs.append("mri_cvs_register")
    cargs.extend([
        "--mov",
        params.get("mov_subjid")
    ])
    if params.get("template_subjid") is not None:
        cargs.extend([
            "--template",
            params.get("template_subjid")
        ])
    if params.get("templatedir") is not None:
        cargs.extend([
            "--templatedir",
            params.get("templatedir")
        ])
    if params.get("mni_flag"):
        cargs.append("--mni")
    if params.get("outdir") is not None:
        cargs.extend([
            "--outdir",
            params.get("outdir")
        ])
    if params.get("asegfname") is not None:
        cargs.extend([
            "--asegfname",
            params.get("asegfname")
        ])
    if params.get("voltype") is not None:
        cargs.extend([
            "--voltype",
            params.get("voltype")
        ])
    if params.get("step1_flag"):
        cargs.append("--step1")
    if params.get("step2_flag"):
        cargs.append("--step2")
    if params.get("step3_flag"):
        cargs.append("--step3")
    if params.get("noaseg_flag"):
        cargs.append("--noaseg")
    if params.get("nointensity_flag"):
        cargs.append("--nointensity")
    if params.get("hemi_flag"):
        cargs.append("--hemi")
    if params.get("masktargethemi_flag"):
        cargs.append("--masktargethemi")
    if params.get("maskmovinghemi_flag"):
        cargs.append("--maskmovinghemi")
    if params.get("nocleanup_flag"):
        cargs.append("--nocleanup")
    if params.get("keepelreg_flag"):
        cargs.append("--keepelreg")
    if params.get("keepallm3z_flag"):
        cargs.append("--keepallm3z")
    if params.get("cleanall_flag"):
        cargs.append("--cleanall")
    if params.get("cleansurfreg_flag"):
        cargs.append("--cleansurfreg")
    if params.get("cleanelreg_flag"):
        cargs.append("--cleanelreg")
    if params.get("cleanvolreg_flag"):
        cargs.append("--cleanvolreg")
    if params.get("m3d_flag"):
        cargs.append("--m3d")
    if params.get("openmp") is not None:
        cargs.extend([
            "--openmp",
            str(params.get("openmp"))
        ])
    if params.get("nolog_flag"):
        cargs.append("--nolog")
    if params.get("version_flag"):
        cargs.append("--version")
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def mri_cvs_register_outputs(
    params: MriCvsRegisterParameters,
    execution: Execution,
) -> MriCvsRegisterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCvsRegisterOutputs(
        root=execution.output_file("."),
        final_cvs_morph=execution.output_file(params.get("outdir") + "/final_CVSmorph_toTEMPLATE.m3z") if (params.get("outdir") is not None) else None,
        final_cvs_morphed_norm=execution.output_file(params.get("outdir") + "/final_CVSmorphed_toTEMPLATE_norm.mgz") if (params.get("outdir") is not None) else None,
        final_cvs_morphed_aseg=execution.output_file(params.get("outdir") + "/final_CVSmorphed_toTEMPLATE_aseg.mgz") if (params.get("outdir") is not None) else None,
        step1_morphed_aseg=execution.output_file(params.get("outdir") + "/step1_CVSmorphed_toTEMPLATE_aseg.mgz") if (params.get("outdir") is not None) else None,
        step1_morphed_norm=execution.output_file(params.get("outdir") + "/step1_CVSmorphed_toTEMPLATE_norm.mgz") if (params.get("outdir") is not None) else None,
    )
    return ret


def mri_cvs_register_execute(
    params: MriCvsRegisterParameters,
    execution: Execution,
) -> MriCvsRegisterOutputs:
    """
    Combined Volume and Surface Registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCvsRegisterOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_cvs_register_cargs(params, execution)
    ret = mri_cvs_register_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_cvs_register(
    mov_subjid: str,
    template_subjid: str | None = None,
    templatedir: str | None = None,
    mni_flag: bool = False,
    outdir: str | None = None,
    asegfname: str | None = None,
    voltype: str | None = None,
    step1_flag: bool = False,
    step2_flag: bool = False,
    step3_flag: bool = False,
    noaseg_flag: bool = False,
    nointensity_flag: bool = False,
    hemi_flag: bool = False,
    masktargethemi_flag: bool = False,
    maskmovinghemi_flag: bool = False,
    nocleanup_flag: bool = False,
    keepelreg_flag: bool = False,
    keepallm3z_flag: bool = False,
    cleanall_flag: bool = False,
    cleansurfreg_flag: bool = False,
    cleanelreg_flag: bool = False,
    cleanvolreg_flag: bool = False,
    m3d_flag: bool = False,
    openmp: int | None = None,
    nolog_flag: bool = False,
    version_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MriCvsRegisterOutputs:
    """
    Combined Volume and Surface Registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mov_subjid: FreeSurfer subject name as found in $SUBJECTS_DIR. This\
            identifies the subject that is to be moved / registered to the target.
        template_subjid: FreeSurfer subject name as found in $SUBJECTS_DIR (or\
            --templatedir). This identifies the subject that is to be kept fixed\
            (template).
        templatedir: Directory of the template subject's SUBJECTS_DIR if\
            different from that of the moving subject.
        mni_flag: Use the CVS atlas in MNI152 space as a target for\
            registration.
        outdir: Name of the output directory where all the registration results\
            are written.
        asegfname: Name of the segmentation volume used in volumetric\
            registration step. Do not use the file extension.
        voltype: Changes the input from norm.mgz to voltype.mgz.
        step1_flag: Only do step 1 (spherical registration).
        step2_flag: Only do step 2 (elastic registration).
        step3_flag: Only do step 3 (volumetric registration).
        noaseg_flag: Do not use aseg volumes in the volumetric registration\
            pipeline.
        nointensity_flag: Do not use intensity volumes in the volumetric\
            registration pipeline.
        hemi_flag: Run CVS registration only on one hemisphere.
        masktargethemi_flag: Use with --hemi when hemi is registered to full\
            brain target.
        maskmovinghemi_flag: Use with --hemi when full brain is registered to\
            single hemi target.
        nocleanup_flag: Do not delete temporary files.
        keepelreg_flag: Do not delete elastic registration outcomes.
        keepallm3z_flag: Do not delete m3z morph files computed during CVS.
        cleanall_flag: Overwrite / recompute all CVS-related morphs.
        cleansurfreg_flag: Overwrite/recompute CVS-related surface registration\
            morphs.
        cleanelreg_flag: Overwrite / recompute CVS-related elastic registration\
            morph.
        cleanvolreg_flag: Overwrite / recompute CVS-related volumetric morphs.
        m3d_flag: Use m3d instead of m3z for registration morphs.
        openmp: Assign the number of nodes for openmp runs.
        nolog_flag: Do not produce a log file.
        version_flag: Print version and exit.
        help_flag: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCvsRegisterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CVS_REGISTER_METADATA)
    params = mri_cvs_register_params(mov_subjid=mov_subjid, template_subjid=template_subjid, templatedir=templatedir, mni_flag=mni_flag, outdir=outdir, asegfname=asegfname, voltype=voltype, step1_flag=step1_flag, step2_flag=step2_flag, step3_flag=step3_flag, noaseg_flag=noaseg_flag, nointensity_flag=nointensity_flag, hemi_flag=hemi_flag, masktargethemi_flag=masktargethemi_flag, maskmovinghemi_flag=maskmovinghemi_flag, nocleanup_flag=nocleanup_flag, keepelreg_flag=keepelreg_flag, keepallm3z_flag=keepallm3z_flag, cleanall_flag=cleanall_flag, cleansurfreg_flag=cleansurfreg_flag, cleanelreg_flag=cleanelreg_flag, cleanvolreg_flag=cleanvolreg_flag, m3d_flag=m3d_flag, openmp=openmp, nolog_flag=nolog_flag, version_flag=version_flag, help_flag=help_flag)
    return mri_cvs_register_execute(params, execution)


__all__ = [
    "MRI_CVS_REGISTER_METADATA",
    "MriCvsRegisterOutputs",
    "mri_cvs_register",
    "mri_cvs_register_params",
]
