# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

RECON_ALL_METADATA = Metadata(
    id="de72948bacd270ce7d872b3cb30e555b07de540c.boutiques",
    name="recon-all",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
ReconAllParameters = typing.TypedDict('ReconAllParameters', {
    "__STYX_TYPE__": typing.Literal["recon-all"],
    "subjid": str,
    "autorecon3_flag": bool,
    "hemi": typing.NotRequired[str | None],
    "pons_crs": typing.NotRequired[list[float] | None],
    "cc_crs": typing.NotRequired[list[float] | None],
    "lh_crs": typing.NotRequired[list[float] | None],
    "rh_crs": typing.NotRequired[list[float] | None],
    "nofill": bool,
    "watershed": typing.NotRequired[str | None],
    "external_brain_mask": typing.NotRequired[InputPathType | None],
    "wsless": bool,
    "wsmore": bool,
    "wsatlas": bool,
    "no_wsatlas": bool,
    "no_wsgcaatlas": bool,
    "wsthresh": typing.NotRequired[float | None],
    "wsseed": typing.NotRequired[list[float] | None],
    "norm_3d_iters": typing.NotRequired[float | None],
    "norm_max_grad": typing.NotRequired[float | None],
    "norm1_b": typing.NotRequired[float | None],
    "norm2_b": typing.NotRequired[float | None],
    "norm1_n": typing.NotRequired[float | None],
    "norm2_n": typing.NotRequired[float | None],
    "cm": bool,
    "no_fix_with_ga": bool,
    "fix_diag_only": bool,
    "seg_wlo": typing.NotRequired[float | None],
    "seg_ghi": typing.NotRequired[float | None],
    "nothicken": bool,
    "no_ca_align_after": bool,
    "no_ca_align": bool,
    "deface": bool,
    "expert_file": typing.NotRequired[InputPathType | None],
    "xopts_use": bool,
    "xopts_clean": bool,
    "xopts_overwrite": bool,
    "termscript_file": typing.NotRequired[InputPathType | None],
    "mprage": bool,
    "washu_mprage": bool,
    "schwartzya3t_atlas": bool,
    "threads": typing.NotRequired[float | None],
    "waitfor_file": typing.NotRequired[InputPathType | None],
    "notify_file": typing.NotRequired[InputPathType | None],
    "log_file": typing.NotRequired[InputPathType | None],
    "status_file": typing.NotRequired[InputPathType | None],
    "noappend": bool,
    "no_isrunning": bool,
    "hippocampal_subfields_t1": bool,
    "hippocampal_subfields_t2": typing.NotRequired[str | None],
    "hippocampal_subfields_t1t2": typing.NotRequired[str | None],
    "brainstem_structures": bool,
    "subjects_dir": typing.NotRequired[str | None],
    "mail_user": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
    "group_id": typing.NotRequired[str | None],
    "only_versions": bool,
    "debug": bool,
    "allow_coredump": bool,
    "dontrun": bool,
    "version": bool,
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "recon-all": recon_all_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "recon-all": recon_all_outputs,
    }.get(t)


class ReconAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `recon_all(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    logfile: OutputPathType
    """Log file of the recon-all process"""
    statusfile: OutputPathType
    """Status file of the recon-all process"""


def recon_all_params(
    subjid: str,
    autorecon3_flag: bool = False,
    hemi: str | None = None,
    pons_crs: list[float] | None = None,
    cc_crs: list[float] | None = None,
    lh_crs: list[float] | None = None,
    rh_crs: list[float] | None = None,
    nofill: bool = False,
    watershed: str | None = None,
    external_brain_mask: InputPathType | None = None,
    wsless: bool = False,
    wsmore: bool = False,
    wsatlas: bool = False,
    no_wsatlas: bool = False,
    no_wsgcaatlas: bool = False,
    wsthresh: float | None = None,
    wsseed: list[float] | None = None,
    norm_3d_iters: float | None = None,
    norm_max_grad: float | None = None,
    norm1_b: float | None = None,
    norm2_b: float | None = None,
    norm1_n: float | None = None,
    norm2_n: float | None = None,
    cm: bool = False,
    no_fix_with_ga: bool = False,
    fix_diag_only: bool = False,
    seg_wlo: float | None = None,
    seg_ghi: float | None = None,
    nothicken: bool = False,
    no_ca_align_after: bool = False,
    no_ca_align: bool = False,
    deface: bool = False,
    expert_file: InputPathType | None = None,
    xopts_use: bool = False,
    xopts_clean: bool = False,
    xopts_overwrite: bool = False,
    termscript_file: InputPathType | None = None,
    mprage: bool = False,
    washu_mprage: bool = False,
    schwartzya3t_atlas: bool = False,
    threads: float | None = None,
    waitfor_file: InputPathType | None = None,
    notify_file: InputPathType | None = None,
    log_file: InputPathType | None = None,
    status_file: InputPathType | None = None,
    noappend: bool = False,
    no_isrunning: bool = False,
    hippocampal_subfields_t1: bool = False,
    hippocampal_subfields_t2: str | None = None,
    hippocampal_subfields_t1t2: str | None = None,
    brainstem_structures: bool = False,
    subjects_dir: str | None = None,
    mail_user: str | None = None,
    umask: str | None = None,
    group_id: str | None = None,
    only_versions: bool = False,
    debug: bool = False,
    allow_coredump: bool = False,
    dontrun: bool = False,
    version: bool = False,
    help_: bool = False,
) -> ReconAllParameters:
    """
    Build parameters.
    
    Args:
        subjid: Subject ID for the FreeSurfer analysis.
        autorecon3_flag: Process stages 24-34.
        hemi: Specify hemisphere ('lh' or 'rh').
        pons_crs: Specify CRS for pons during fill operation.
        cc_crs: Specify CRS for corpus callosum during fill operation.
        lh_crs: Specify CRS for left hemisphere during fill operation.
        rh_crs: Specify CRS for right hemisphere during fill operation.
        nofill: Do not use automatic subcortical seg to fill.
        watershed: Control skull stripping/watershed program.
        external_brain_mask: Custom external brain mask file.
        wsless: Decrease watershed threshold.
        wsmore: Increase watershed threshold.
        wsatlas: Use atlas when skull stripping.
        no_wsatlas: Do not use atlas when skull stripping.
        no_wsgcaatlas: Do not use GCA atlas when skull stripping.
        wsthresh: Explicitly set watershed threshold.
        wsseed: Identify an index (C, R, S) point in the skull.
        norm_3d_iters: Number of 3D iterations for mri_normalize.
        norm_max_grad: Max grad for mri_normalize.
        norm1_b: First usage of mri_normalize with control point intensity N\
            below target.
        norm2_b: Second usage of mri_normalize with control point intensity N\
            below target.
        norm1_n: First usage of mri_normalize, number of iterations.
        norm2_n: Second usage of mri_normalize, number of iterations.
        cm: Conform volumes to the min voxel size.
        no_fix_with_ga: Do not use genetic algorithm when fixing topology.
        fix_diag_only: Topology fixer runs until ?h.defect_labels files are\
            created.
        seg_wlo: Set WLO value for mri_segment and mris_make_surfaces.
        seg_ghi: Set GHI value for mri_segment and mris_make_surfaces.
        nothicken: Pass '-thicken 0' to mri_segment.
        no_ca_align_after: Turn off '-align-after' with mri_ca_register.
        no_ca_align: Turn off '-align' with mri_ca_label.
        deface: Deface subject, written to orig_defaced.mgz.
        expert_file: Read-in expert options file.
        xopts_use: Use pre-existing expert options file.
        xopts_clean: Delete pre-existing expert options file.
        xopts_overwrite: Overwrite pre-existing expert options file.
        termscript_file: Run script before exiting.
        mprage: Assume scan parameters are MGH MP-RAGE protocol.
        washu_mprage: Assume scan parameters are Wash.U. MP-RAGE protocol.
        schwartzya3t_atlas: Use special young adult 3T atlas for tal reg.
        threads: Set number of threads to use.
        waitfor_file: Wait for file to appear before beginning.
        notify_file: Create this file after finishing.
        log_file: Specify log file.
        status_file: Specify status file.
        noappend: Start new log and status files instead of appending.
        no_isrunning: Do not check whether this subject is currently being\
            processed.
        hippocampal_subfields_t1: Segmentation of hippocampal subfields using\
            input T1 scan.
        hippocampal_subfields_t2: Segmentation using an additional scan and\
            input T2 scan.
        hippocampal_subfields_t1t2: Segmentation using additional scan and\
            input T1.
        brainstem_structures: Segmentation of brainstem structures.
        subjects_dir: Specify subjects directory.
        mail_user: Mail user when done.
        umask: Set unix file permission mask.
        group_id: Check that current group is alpha group.
        only_versions: Print version of each binary and exit.
        debug: Print out lots of info.
        allow_coredump: Set coredump limit to unlimited.
        dontrun: Do everything but execute each command.
        version: Print version of this script and exit.
        help_: Display help message and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "recon-all",
        "subjid": subjid,
        "autorecon3_flag": autorecon3_flag,
        "nofill": nofill,
        "wsless": wsless,
        "wsmore": wsmore,
        "wsatlas": wsatlas,
        "no_wsatlas": no_wsatlas,
        "no_wsgcaatlas": no_wsgcaatlas,
        "cm": cm,
        "no_fix_with_ga": no_fix_with_ga,
        "fix_diag_only": fix_diag_only,
        "nothicken": nothicken,
        "no_ca_align_after": no_ca_align_after,
        "no_ca_align": no_ca_align,
        "deface": deface,
        "xopts_use": xopts_use,
        "xopts_clean": xopts_clean,
        "xopts_overwrite": xopts_overwrite,
        "mprage": mprage,
        "washu_mprage": washu_mprage,
        "schwartzya3t_atlas": schwartzya3t_atlas,
        "noappend": noappend,
        "no_isrunning": no_isrunning,
        "hippocampal_subfields_t1": hippocampal_subfields_t1,
        "brainstem_structures": brainstem_structures,
        "only_versions": only_versions,
        "debug": debug,
        "allow_coredump": allow_coredump,
        "dontrun": dontrun,
        "version": version,
        "help": help_,
    }
    if hemi is not None:
        params["hemi"] = hemi
    if pons_crs is not None:
        params["pons_crs"] = pons_crs
    if cc_crs is not None:
        params["cc_crs"] = cc_crs
    if lh_crs is not None:
        params["lh_crs"] = lh_crs
    if rh_crs is not None:
        params["rh_crs"] = rh_crs
    if watershed is not None:
        params["watershed"] = watershed
    if external_brain_mask is not None:
        params["external_brain_mask"] = external_brain_mask
    if wsthresh is not None:
        params["wsthresh"] = wsthresh
    if wsseed is not None:
        params["wsseed"] = wsseed
    if norm_3d_iters is not None:
        params["norm_3d_iters"] = norm_3d_iters
    if norm_max_grad is not None:
        params["norm_max_grad"] = norm_max_grad
    if norm1_b is not None:
        params["norm1_b"] = norm1_b
    if norm2_b is not None:
        params["norm2_b"] = norm2_b
    if norm1_n is not None:
        params["norm1_n"] = norm1_n
    if norm2_n is not None:
        params["norm2_n"] = norm2_n
    if seg_wlo is not None:
        params["seg_wlo"] = seg_wlo
    if seg_ghi is not None:
        params["seg_ghi"] = seg_ghi
    if expert_file is not None:
        params["expert_file"] = expert_file
    if termscript_file is not None:
        params["termscript_file"] = termscript_file
    if threads is not None:
        params["threads"] = threads
    if waitfor_file is not None:
        params["waitfor_file"] = waitfor_file
    if notify_file is not None:
        params["notify_file"] = notify_file
    if log_file is not None:
        params["log_file"] = log_file
    if status_file is not None:
        params["status_file"] = status_file
    if hippocampal_subfields_t2 is not None:
        params["hippocampal_subfields_t2"] = hippocampal_subfields_t2
    if hippocampal_subfields_t1t2 is not None:
        params["hippocampal_subfields_t1t2"] = hippocampal_subfields_t1t2
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if mail_user is not None:
        params["mail_user"] = mail_user
    if umask is not None:
        params["umask"] = umask
    if group_id is not None:
        params["group_id"] = group_id
    return params


def recon_all_cargs(
    params: ReconAllParameters,
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
    cargs.append("recon-all")
    cargs.extend([
        "-subjid",
        params.get("subjid")
    ])
    if params.get("autorecon3_flag"):
        cargs.append("-autorecon3")
    if params.get("hemi") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemi")
        ])
    if params.get("pons_crs") is not None:
        cargs.extend([
            "-pons-crs",
            *map(str, params.get("pons_crs"))
        ])
    if params.get("cc_crs") is not None:
        cargs.extend([
            "-cc-crs",
            *map(str, params.get("cc_crs"))
        ])
    if params.get("lh_crs") is not None:
        cargs.extend([
            "-lh-crs",
            *map(str, params.get("lh_crs"))
        ])
    if params.get("rh_crs") is not None:
        cargs.extend([
            "-rh-crs",
            *map(str, params.get("rh_crs"))
        ])
    if params.get("nofill"):
        cargs.append("-nofill")
    if params.get("watershed") is not None:
        cargs.extend([
            "-watershed",
            params.get("watershed")
        ])
    if params.get("external_brain_mask") is not None:
        cargs.extend([
            "-xmask",
            execution.input_file(params.get("external_brain_mask"))
        ])
    if params.get("wsless"):
        cargs.append("-wsless")
    if params.get("wsmore"):
        cargs.append("-wsmore")
    if params.get("wsatlas"):
        cargs.append("-wsatlas")
    if params.get("no_wsatlas"):
        cargs.append("-no-wsatlas")
    if params.get("no_wsgcaatlas"):
        cargs.append("-no-wsgcaatlas")
    if params.get("wsthresh") is not None:
        cargs.extend([
            "-wsthresh",
            str(params.get("wsthresh"))
        ])
    if params.get("wsseed") is not None:
        cargs.extend([
            "-wsseed",
            *map(str, params.get("wsseed"))
        ])
    if params.get("norm_3d_iters") is not None:
        cargs.extend([
            "-norm3diters",
            str(params.get("norm_3d_iters"))
        ])
    if params.get("norm_max_grad") is not None:
        cargs.extend([
            "-normmaxgrad",
            str(params.get("norm_max_grad"))
        ])
    if params.get("norm1_b") is not None:
        cargs.extend([
            "-norm1-b",
            str(params.get("norm1_b"))
        ])
    if params.get("norm2_b") is not None:
        cargs.extend([
            "-norm2-b",
            str(params.get("norm2_b"))
        ])
    if params.get("norm1_n") is not None:
        cargs.extend([
            "-norm1-n",
            str(params.get("norm1_n"))
        ])
    if params.get("norm2_n") is not None:
        cargs.extend([
            "-norm2-n",
            str(params.get("norm2_n"))
        ])
    if params.get("cm"):
        cargs.append("-cm")
    if params.get("no_fix_with_ga"):
        cargs.append("-no-fix-with-ga")
    if params.get("fix_diag_only"):
        cargs.append("-fix-diag-only")
    if params.get("seg_wlo") is not None:
        cargs.extend([
            "-seg-wlo",
            str(params.get("seg_wlo"))
        ])
    if params.get("seg_ghi") is not None:
        cargs.extend([
            "-seg-ghi",
            str(params.get("seg_ghi"))
        ])
    if params.get("nothicken"):
        cargs.append("-nothicken")
    if params.get("no_ca_align_after"):
        cargs.append("-no-ca-align-after")
    if params.get("no_ca_align"):
        cargs.append("-no-ca-align")
    if params.get("deface"):
        cargs.append("-deface")
    if params.get("expert_file") is not None:
        cargs.extend([
            "-expert",
            execution.input_file(params.get("expert_file"))
        ])
    if params.get("xopts_use"):
        cargs.append("-xopts-use")
    if params.get("xopts_clean"):
        cargs.append("-xopts-clean")
    if params.get("xopts_overwrite"):
        cargs.append("-xopts-overwrite")
    if params.get("termscript_file") is not None:
        cargs.extend([
            "-termscript",
            execution.input_file(params.get("termscript_file"))
        ])
    if params.get("mprage"):
        cargs.append("-mprage")
    if params.get("washu_mprage"):
        cargs.append("-washu_mprage")
    if params.get("schwartzya3t_atlas"):
        cargs.append("-schwartzya3t-atlas")
    if params.get("threads") is not None:
        cargs.extend([
            "-threads",
            str(params.get("threads"))
        ])
    if params.get("waitfor_file") is not None:
        cargs.extend([
            "-waitfor",
            execution.input_file(params.get("waitfor_file"))
        ])
    if params.get("notify_file") is not None:
        cargs.extend([
            "-notify",
            execution.input_file(params.get("notify_file"))
        ])
    if params.get("log_file") is not None:
        cargs.extend([
            "-log",
            execution.input_file(params.get("log_file"))
        ])
    if params.get("status_file") is not None:
        cargs.extend([
            "-status",
            execution.input_file(params.get("status_file"))
        ])
    if params.get("noappend"):
        cargs.append("-noappend")
    if params.get("no_isrunning"):
        cargs.append("-no-isrunning")
    if params.get("hippocampal_subfields_t1"):
        cargs.append("-hippocampal-subfields-T1")
    if params.get("hippocampal_subfields_t2") is not None:
        cargs.extend([
            "-hippocampal-subfields-T2",
            params.get("hippocampal_subfields_t2")
        ])
    if params.get("hippocampal_subfields_t1t2") is not None:
        cargs.extend([
            "-hippocampal-subfields-T1T2",
            params.get("hippocampal_subfields_t1t2")
        ])
    if params.get("brainstem_structures"):
        cargs.append("-brainstem-structures")
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sd",
            params.get("subjects_dir")
        ])
    if params.get("mail_user") is not None:
        cargs.extend([
            "-mail",
            params.get("mail_user")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    if params.get("group_id") is not None:
        cargs.extend([
            "-grp",
            params.get("group_id")
        ])
    if params.get("only_versions"):
        cargs.append("-onlyversions")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("allow_coredump"):
        cargs.append("-allowcoredump")
    if params.get("dontrun"):
        cargs.append("-dontrun")
    if params.get("version"):
        cargs.append("-version")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def recon_all_outputs(
    params: ReconAllParameters,
    execution: Execution,
) -> ReconAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ReconAllOutputs(
        root=execution.output_file("."),
        logfile=execution.output_file(params.get("subjid") + "/scripts/recon-all.log"),
        statusfile=execution.output_file(params.get("subjid") + "/scripts/recon-all-status.log"),
    )
    return ret


def recon_all_execute(
    params: ReconAllParameters,
    execution: Execution,
) -> ReconAllOutputs:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ReconAllOutputs`).
    """
    params = execution.params(params)
    cargs = recon_all_cargs(params, execution)
    ret = recon_all_outputs(params, execution)
    execution.run(cargs)
    return ret


def recon_all(
    subjid: str,
    autorecon3_flag: bool = False,
    hemi: str | None = None,
    pons_crs: list[float] | None = None,
    cc_crs: list[float] | None = None,
    lh_crs: list[float] | None = None,
    rh_crs: list[float] | None = None,
    nofill: bool = False,
    watershed: str | None = None,
    external_brain_mask: InputPathType | None = None,
    wsless: bool = False,
    wsmore: bool = False,
    wsatlas: bool = False,
    no_wsatlas: bool = False,
    no_wsgcaatlas: bool = False,
    wsthresh: float | None = None,
    wsseed: list[float] | None = None,
    norm_3d_iters: float | None = None,
    norm_max_grad: float | None = None,
    norm1_b: float | None = None,
    norm2_b: float | None = None,
    norm1_n: float | None = None,
    norm2_n: float | None = None,
    cm: bool = False,
    no_fix_with_ga: bool = False,
    fix_diag_only: bool = False,
    seg_wlo: float | None = None,
    seg_ghi: float | None = None,
    nothicken: bool = False,
    no_ca_align_after: bool = False,
    no_ca_align: bool = False,
    deface: bool = False,
    expert_file: InputPathType | None = None,
    xopts_use: bool = False,
    xopts_clean: bool = False,
    xopts_overwrite: bool = False,
    termscript_file: InputPathType | None = None,
    mprage: bool = False,
    washu_mprage: bool = False,
    schwartzya3t_atlas: bool = False,
    threads: float | None = None,
    waitfor_file: InputPathType | None = None,
    notify_file: InputPathType | None = None,
    log_file: InputPathType | None = None,
    status_file: InputPathType | None = None,
    noappend: bool = False,
    no_isrunning: bool = False,
    hippocampal_subfields_t1: bool = False,
    hippocampal_subfields_t2: str | None = None,
    hippocampal_subfields_t1t2: str | None = None,
    brainstem_structures: bool = False,
    subjects_dir: str | None = None,
    mail_user: str | None = None,
    umask: str | None = None,
    group_id: str | None = None,
    only_versions: bool = False,
    debug: bool = False,
    allow_coredump: bool = False,
    dontrun: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> ReconAllOutputs:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjid: Subject ID for the FreeSurfer analysis.
        autorecon3_flag: Process stages 24-34.
        hemi: Specify hemisphere ('lh' or 'rh').
        pons_crs: Specify CRS for pons during fill operation.
        cc_crs: Specify CRS for corpus callosum during fill operation.
        lh_crs: Specify CRS for left hemisphere during fill operation.
        rh_crs: Specify CRS for right hemisphere during fill operation.
        nofill: Do not use automatic subcortical seg to fill.
        watershed: Control skull stripping/watershed program.
        external_brain_mask: Custom external brain mask file.
        wsless: Decrease watershed threshold.
        wsmore: Increase watershed threshold.
        wsatlas: Use atlas when skull stripping.
        no_wsatlas: Do not use atlas when skull stripping.
        no_wsgcaatlas: Do not use GCA atlas when skull stripping.
        wsthresh: Explicitly set watershed threshold.
        wsseed: Identify an index (C, R, S) point in the skull.
        norm_3d_iters: Number of 3D iterations for mri_normalize.
        norm_max_grad: Max grad for mri_normalize.
        norm1_b: First usage of mri_normalize with control point intensity N\
            below target.
        norm2_b: Second usage of mri_normalize with control point intensity N\
            below target.
        norm1_n: First usage of mri_normalize, number of iterations.
        norm2_n: Second usage of mri_normalize, number of iterations.
        cm: Conform volumes to the min voxel size.
        no_fix_with_ga: Do not use genetic algorithm when fixing topology.
        fix_diag_only: Topology fixer runs until ?h.defect_labels files are\
            created.
        seg_wlo: Set WLO value for mri_segment and mris_make_surfaces.
        seg_ghi: Set GHI value for mri_segment and mris_make_surfaces.
        nothicken: Pass '-thicken 0' to mri_segment.
        no_ca_align_after: Turn off '-align-after' with mri_ca_register.
        no_ca_align: Turn off '-align' with mri_ca_label.
        deface: Deface subject, written to orig_defaced.mgz.
        expert_file: Read-in expert options file.
        xopts_use: Use pre-existing expert options file.
        xopts_clean: Delete pre-existing expert options file.
        xopts_overwrite: Overwrite pre-existing expert options file.
        termscript_file: Run script before exiting.
        mprage: Assume scan parameters are MGH MP-RAGE protocol.
        washu_mprage: Assume scan parameters are Wash.U. MP-RAGE protocol.
        schwartzya3t_atlas: Use special young adult 3T atlas for tal reg.
        threads: Set number of threads to use.
        waitfor_file: Wait for file to appear before beginning.
        notify_file: Create this file after finishing.
        log_file: Specify log file.
        status_file: Specify status file.
        noappend: Start new log and status files instead of appending.
        no_isrunning: Do not check whether this subject is currently being\
            processed.
        hippocampal_subfields_t1: Segmentation of hippocampal subfields using\
            input T1 scan.
        hippocampal_subfields_t2: Segmentation using an additional scan and\
            input T2 scan.
        hippocampal_subfields_t1t2: Segmentation using additional scan and\
            input T1.
        brainstem_structures: Segmentation of brainstem structures.
        subjects_dir: Specify subjects directory.
        mail_user: Mail user when done.
        umask: Set unix file permission mask.
        group_id: Check that current group is alpha group.
        only_versions: Print version of each binary and exit.
        debug: Print out lots of info.
        allow_coredump: Set coredump limit to unlimited.
        dontrun: Do everything but execute each command.
        version: Print version of this script and exit.
        help_: Display help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ReconAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RECON_ALL_METADATA)
    params = recon_all_params(subjid=subjid, autorecon3_flag=autorecon3_flag, hemi=hemi, pons_crs=pons_crs, cc_crs=cc_crs, lh_crs=lh_crs, rh_crs=rh_crs, nofill=nofill, watershed=watershed, external_brain_mask=external_brain_mask, wsless=wsless, wsmore=wsmore, wsatlas=wsatlas, no_wsatlas=no_wsatlas, no_wsgcaatlas=no_wsgcaatlas, wsthresh=wsthresh, wsseed=wsseed, norm_3d_iters=norm_3d_iters, norm_max_grad=norm_max_grad, norm1_b=norm1_b, norm2_b=norm2_b, norm1_n=norm1_n, norm2_n=norm2_n, cm=cm, no_fix_with_ga=no_fix_with_ga, fix_diag_only=fix_diag_only, seg_wlo=seg_wlo, seg_ghi=seg_ghi, nothicken=nothicken, no_ca_align_after=no_ca_align_after, no_ca_align=no_ca_align, deface=deface, expert_file=expert_file, xopts_use=xopts_use, xopts_clean=xopts_clean, xopts_overwrite=xopts_overwrite, termscript_file=termscript_file, mprage=mprage, washu_mprage=washu_mprage, schwartzya3t_atlas=schwartzya3t_atlas, threads=threads, waitfor_file=waitfor_file, notify_file=notify_file, log_file=log_file, status_file=status_file, noappend=noappend, no_isrunning=no_isrunning, hippocampal_subfields_t1=hippocampal_subfields_t1, hippocampal_subfields_t2=hippocampal_subfields_t2, hippocampal_subfields_t1t2=hippocampal_subfields_t1t2, brainstem_structures=brainstem_structures, subjects_dir=subjects_dir, mail_user=mail_user, umask=umask, group_id=group_id, only_versions=only_versions, debug=debug, allow_coredump=allow_coredump, dontrun=dontrun, version=version, help_=help_)
    return recon_all_execute(params, execution)


__all__ = [
    "RECON_ALL_METADATA",
    "ReconAllOutputs",
    "ReconAllParameters",
    "recon_all",
    "recon_all_params",
]
