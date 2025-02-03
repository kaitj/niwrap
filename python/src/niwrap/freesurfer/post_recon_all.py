# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

POST_RECON_ALL_METADATA = Metadata(
    id="043904c04e1a7c309fb6aa5cb7234831a996fdf4.boutiques",
    name="post-recon-all",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
PostReconAllParameters = typing.TypedDict('PostReconAllParameters', {
    "__STYX_TYPE__": typing.Literal["post-recon-all"],
    "subject": str,
    "no_subfields": bool,
    "no_subregions": bool,
    "no_cvs": bool,
    "no_qcache": bool,
    "no_sclimbic": bool,
    "no_hthsu": bool,
    "no_synthstrip": bool,
    "no_synthseg": bool,
    "no_qastats": bool,
    "no_samseg": bool,
    "no_xhemi": bool,
    "no_cos7": bool,
    "threads": typing.NotRequired[float | None],
    "force": bool,
    "exit_on_error": bool,
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
        "post-recon-all": post_recon_all_cargs,
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


def post_recon_all_params(
    subject: str,
    no_subfields: bool = False,
    no_subregions: bool = False,
    no_cvs: bool = False,
    no_qcache: bool = False,
    no_sclimbic: bool = False,
    no_hthsu: bool = False,
    no_synthstrip: bool = False,
    no_synthseg: bool = False,
    no_qastats: bool = False,
    no_samseg: bool = False,
    no_xhemi: bool = False,
    no_cos7: bool = False,
    threads: float | None = None,
    force: bool = False,
    exit_on_error: bool = False,
) -> PostReconAllParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier to be processed.
        no_subfields: Do not run subfields extraction.
        no_subregions: Do not run subregions extraction.
        no_cvs: Do not run CVS processing (default behavior).
        no_qcache: Do not run qcache processing.
        no_sclimbic: Do not run sclimbic processing.
        no_hthsu: Do not run hypothalamic subunits processing.
        no_synthstrip: Do not run synthstrip processing.
        no_synthseg: Do not run synthseg processing.
        no_qastats: Do not run qastats processing.
        no_samseg: Do not run samseg processing.
        no_xhemi: Do not run xhemi processing.
        no_cos7: Do not run commands from CentOS7 container.
        threads: Number of threads to be used.
        force: Force rerunning even if output is newer than input.
        exit_on_error: Exit immediately if an error occurs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "post-recon-all",
        "subject": subject,
        "no_subfields": no_subfields,
        "no_subregions": no_subregions,
        "no_cvs": no_cvs,
        "no_qcache": no_qcache,
        "no_sclimbic": no_sclimbic,
        "no_hthsu": no_hthsu,
        "no_synthstrip": no_synthstrip,
        "no_synthseg": no_synthseg,
        "no_qastats": no_qastats,
        "no_samseg": no_samseg,
        "no_xhemi": no_xhemi,
        "no_cos7": no_cos7,
        "force": force,
        "exit_on_error": exit_on_error,
    }
    if threads is not None:
        params["threads"] = threads
    return params


def post_recon_all_cargs(
    params: PostReconAllParameters,
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
    cargs.extend([
        "-all",
        "post-recon" + params.get("subject")
    ])
    if params.get("no_subfields"):
        cargs.append("--no-subfields")
    if params.get("no_subregions"):
        cargs.append("--no-subregions")
    if params.get("no_cvs"):
        cargs.append("--no-cvs")
    if params.get("no_qcache"):
        cargs.append("--no-qcache")
    if params.get("no_sclimbic"):
        cargs.append("--no-sclimbic")
    if params.get("no_hthsu"):
        cargs.append("--no-hthsu")
    if params.get("no_synthstrip"):
        cargs.append("--no-synthstrip")
    if params.get("no_synthseg"):
        cargs.append("--no-synthseg")
    if params.get("no_qastats"):
        cargs.append("--no-qastats")
    if params.get("no_samseg"):
        cargs.append("--no-samseg")
    if params.get("no_xhemi"):
        cargs.append("--no-xhemi")
    if params.get("no_cos7"):
        cargs.append("--no-cos7")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("force"):
        cargs.append("--force")
    if params.get("exit_on_error"):
        cargs.append("--exit-on-error")
    return cargs


def post_recon_all_outputs(
    params: PostReconAllParameters,
    execution: Execution,
) -> PostReconAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PostReconAllOutputs(
        root=execution.output_file("."),
    )
    return ret


def post_recon_all_execute(
    params: PostReconAllParameters,
    execution: Execution,
) -> PostReconAllOutputs:
    """
    Post-processing script typically run after recon-all in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PostReconAllOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = post_recon_all_cargs(params, execution)
    ret = post_recon_all_outputs(params, execution)
    execution.run(cargs)
    return ret


def post_recon_all(
    subject: str,
    no_subfields: bool = False,
    no_subregions: bool = False,
    no_cvs: bool = False,
    no_qcache: bool = False,
    no_sclimbic: bool = False,
    no_hthsu: bool = False,
    no_synthstrip: bool = False,
    no_synthseg: bool = False,
    no_qastats: bool = False,
    no_samseg: bool = False,
    no_xhemi: bool = False,
    no_cos7: bool = False,
    threads: float | None = None,
    force: bool = False,
    exit_on_error: bool = False,
    runner: Runner | None = None,
) -> PostReconAllOutputs:
    """
    Post-processing script typically run after recon-all in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier to be processed.
        no_subfields: Do not run subfields extraction.
        no_subregions: Do not run subregions extraction.
        no_cvs: Do not run CVS processing (default behavior).
        no_qcache: Do not run qcache processing.
        no_sclimbic: Do not run sclimbic processing.
        no_hthsu: Do not run hypothalamic subunits processing.
        no_synthstrip: Do not run synthstrip processing.
        no_synthseg: Do not run synthseg processing.
        no_qastats: Do not run qastats processing.
        no_samseg: Do not run samseg processing.
        no_xhemi: Do not run xhemi processing.
        no_cos7: Do not run commands from CentOS7 container.
        threads: Number of threads to be used.
        force: Force rerunning even if output is newer than input.
        exit_on_error: Exit immediately if an error occurs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PostReconAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POST_RECON_ALL_METADATA)
    params = post_recon_all_params(subject=subject, no_subfields=no_subfields, no_subregions=no_subregions, no_cvs=no_cvs, no_qcache=no_qcache, no_sclimbic=no_sclimbic, no_hthsu=no_hthsu, no_synthstrip=no_synthstrip, no_synthseg=no_synthseg, no_qastats=no_qastats, no_samseg=no_samseg, no_xhemi=no_xhemi, no_cos7=no_cos7, threads=threads, force=force, exit_on_error=exit_on_error)
    return post_recon_all_execute(params, execution)


__all__ = [
    "POST_RECON_ALL_METADATA",
    "post_recon_all",
    "post_recon_all_params",
]
