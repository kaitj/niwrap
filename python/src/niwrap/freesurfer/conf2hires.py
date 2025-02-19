# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONF2HIRES_METADATA = Metadata(
    id="0daec93cecaaf674dbbc3d770b70999cf8bff082.boutiques",
    name="conf2hires",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
Conf2hiresParameters = typing.TypedDict('Conf2hiresParameters', {
    "__STYX_TYPE__": typing.Literal["conf2hires"],
    "subject": str,
    "no_t2": bool,
    "mm_norm_sigma": typing.NotRequired[float | None],
    "no_flair": bool,
    "threads": typing.NotRequired[float | None],
    "copy_bias_from_conf": bool,
    "norm_opts_rca": bool,
    "trilin": bool,
    "no_dev": bool,
    "bbr_t2": bool,
    "first_peak_d1": bool,
    "first_peak_d2": bool,
    "stopmask": typing.NotRequired[str | None],
    "expert": typing.NotRequired[str | None],
    "force_update": bool,
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
        "conf2hires": conf2hires_cargs,
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
    }.get(t)


class Conf2hiresOutputs(typing.NamedTuple):
    """
    Output object returned when calling `conf2hires(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def conf2hires_params(
    subject: str,
    no_t2: bool = False,
    mm_norm_sigma: float | None = 8,
    no_flair: bool = False,
    threads: float | None = None,
    copy_bias_from_conf: bool = False,
    norm_opts_rca: bool = False,
    trilin: bool = False,
    no_dev: bool = False,
    bbr_t2: bool = False,
    first_peak_d1: bool = False,
    first_peak_d2: bool = False,
    stopmask: str | None = None,
    expert: str | None = None,
    force_update: bool = False,
) -> Conf2hiresParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        no_t2: Disable T2 processing (default).
        mm_norm_sigma: Smoothing level for T2 mri_normalize (default is 8).
        no_flair: Disable FLAIR processing (default).
        threads: Number of threads to use.
        copy_bias_from_conf: Copy bias field from conformed instead of\
            computing directly.
        norm_opts_rca: Compute bias directly using recon-all opts to\
            mri_normalize.
        trilin: Use trilinear normalization (default, applies with\
            --copy-bias-from-conf).
        no_dev: Do not use mris_make_surfaces.dev (default).
        bbr_t2: Set BBR contrast type to t2.
        first_peak_d1: Refine surface targets in MRIScomputeBorderValues()\
            using first peak method D1.
        first_peak_d2: Refine surface targets in MRIScomputeBorderValues()\
            using first peak method D2.
        stopmask: Specify stop mask.
        expert: Use expert options.
        force_update: Force update of final surfaces.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "conf2hires",
        "subject": subject,
        "no_t2": no_t2,
        "no_flair": no_flair,
        "copy_bias_from_conf": copy_bias_from_conf,
        "norm_opts_rca": norm_opts_rca,
        "trilin": trilin,
        "no_dev": no_dev,
        "bbr_t2": bbr_t2,
        "first_peak_d1": first_peak_d1,
        "first_peak_d2": first_peak_d2,
        "force_update": force_update,
    }
    if mm_norm_sigma is not None:
        params["mm_norm_sigma"] = mm_norm_sigma
    if threads is not None:
        params["threads"] = threads
    if stopmask is not None:
        params["stopmask"] = stopmask
    if expert is not None:
        params["expert"] = expert
    return params


def conf2hires_cargs(
    params: Conf2hiresParameters,
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
    cargs.append("conf2hires")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("no_t2"):
        cargs.append("--no-t2")
    if params.get("mm_norm_sigma") is not None:
        cargs.extend([
            "--mm-norm-sigma",
            str(params.get("mm_norm_sigma"))
        ])
    if params.get("no_flair"):
        cargs.append("--no-flair")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    if params.get("copy_bias_from_conf"):
        cargs.append("--copy-bias-from-conf")
    if params.get("norm_opts_rca"):
        cargs.append("--norm-opts-rca")
    if params.get("trilin"):
        cargs.append("--trilin")
    if params.get("no_dev"):
        cargs.append("--no-dev")
    if params.get("bbr_t2"):
        cargs.append("--bbr-t2")
    if params.get("first_peak_d1"):
        cargs.append("--first-peak-d1")
    if params.get("first_peak_d2"):
        cargs.append("--first-peak-d2")
    if params.get("stopmask") is not None:
        cargs.extend([
            "--stopmask",
            params.get("stopmask")
        ])
    if params.get("expert") is not None:
        cargs.extend([
            "--expert",
            params.get("expert")
        ])
    if params.get("force_update"):
        cargs.append("--force-update")
    return cargs


def conf2hires_outputs(
    params: Conf2hiresParameters,
    execution: Execution,
) -> Conf2hiresOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Conf2hiresOutputs(
        root=execution.output_file("."),
    )
    return ret


def conf2hires_execute(
    params: Conf2hiresParameters,
    execution: Execution,
) -> Conf2hiresOutputs:
    """
    Places the surfaces on high resolution T1 (and maybe T2) volumes based on an
    initial placement on a conformed volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Conf2hiresOutputs`).
    """
    params = execution.params(params)
    cargs = conf2hires_cargs(params, execution)
    ret = conf2hires_outputs(params, execution)
    execution.run(cargs)
    return ret


def conf2hires(
    subject: str,
    no_t2: bool = False,
    mm_norm_sigma: float | None = 8,
    no_flair: bool = False,
    threads: float | None = None,
    copy_bias_from_conf: bool = False,
    norm_opts_rca: bool = False,
    trilin: bool = False,
    no_dev: bool = False,
    bbr_t2: bool = False,
    first_peak_d1: bool = False,
    first_peak_d2: bool = False,
    stopmask: str | None = None,
    expert: str | None = None,
    force_update: bool = False,
    runner: Runner | None = None,
) -> Conf2hiresOutputs:
    """
    Places the surfaces on high resolution T1 (and maybe T2) volumes based on an
    initial placement on a conformed volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        no_t2: Disable T2 processing (default).
        mm_norm_sigma: Smoothing level for T2 mri_normalize (default is 8).
        no_flair: Disable FLAIR processing (default).
        threads: Number of threads to use.
        copy_bias_from_conf: Copy bias field from conformed instead of\
            computing directly.
        norm_opts_rca: Compute bias directly using recon-all opts to\
            mri_normalize.
        trilin: Use trilinear normalization (default, applies with\
            --copy-bias-from-conf).
        no_dev: Do not use mris_make_surfaces.dev (default).
        bbr_t2: Set BBR contrast type to t2.
        first_peak_d1: Refine surface targets in MRIScomputeBorderValues()\
            using first peak method D1.
        first_peak_d2: Refine surface targets in MRIScomputeBorderValues()\
            using first peak method D2.
        stopmask: Specify stop mask.
        expert: Use expert options.
        force_update: Force update of final surfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Conf2hiresOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONF2HIRES_METADATA)
    params = conf2hires_params(subject=subject, no_t2=no_t2, mm_norm_sigma=mm_norm_sigma, no_flair=no_flair, threads=threads, copy_bias_from_conf=copy_bias_from_conf, norm_opts_rca=norm_opts_rca, trilin=trilin, no_dev=no_dev, bbr_t2=bbr_t2, first_peak_d1=first_peak_d1, first_peak_d2=first_peak_d2, stopmask=stopmask, expert=expert, force_update=force_update)
    return conf2hires_execute(params, execution)


__all__ = [
    "CONF2HIRES_METADATA",
    "Conf2hiresOutputs",
    "Conf2hiresParameters",
    "conf2hires",
    "conf2hires_params",
]
