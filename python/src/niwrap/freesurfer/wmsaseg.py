# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

WMSASEG_METADATA = Metadata(
    id="70413a8a1c01bd4a41bdede39664427061f28431.boutiques",
    name="wmsaseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
WmsasegParameters = typing.TypedDict('WmsasegParameters', {
    "__STYX_TYPE__": typing.Literal["wmsaseg"],
    "subject": str,
    "source_orig": typing.NotRequired[str | None],
    "source_long": bool,
    "output_subdir": typing.NotRequired[str | None],
    "gca_file": typing.NotRequired[InputPathType | None],
    "no_reg": bool,
    "no_canorm": bool,
    "init_spm": bool,
    "reg_only": bool,
    "halo1": bool,
    "halo2": bool,
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
        "wmsaseg": wmsaseg_cargs,
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
        "wmsaseg": wmsaseg_outputs,
    }.get(t)


class WmsasegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wmsaseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    t1_canorm: OutputPathType | None
    """CA normalized T1 output"""
    wmsa_lta: OutputPathType | None
    """Linear transform to average space"""


def wmsaseg_params(
    subject: str,
    source_orig: str | None = None,
    source_long: bool = False,
    output_subdir: str | None = None,
    gca_file: InputPathType | None = None,
    no_reg: bool = False,
    no_canorm: bool = False,
    init_spm: bool = False,
    reg_only: bool = False,
    halo1: bool = False,
    halo2: bool = False,
) -> WmsasegParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        source_orig: Use T2 and PD images from original subject.
        source_long: Use T2 and PD images from longitudinal subject.
        output_subdir: Output subdirectory name (default is wmsa).
        gca_file: GCA file path.
        no_reg: Do not register mode to anatomical image.
        no_canorm: Do not run mri_ca_normalize.
        init_spm: Initialize SPM (default is FSL).
        reg_only: Only perform registration.
        halo1: Halo 1 option.
        halo2: Halo 2 option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "wmsaseg",
        "subject": subject,
        "source_long": source_long,
        "no_reg": no_reg,
        "no_canorm": no_canorm,
        "init_spm": init_spm,
        "reg_only": reg_only,
        "halo1": halo1,
        "halo2": halo2,
    }
    if source_orig is not None:
        params["source_orig"] = source_orig
    if output_subdir is not None:
        params["output_subdir"] = output_subdir
    if gca_file is not None:
        params["gca_file"] = gca_file
    return params


def wmsaseg_cargs(
    params: WmsasegParameters,
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
    cargs.append("wmsaseg")
    cargs.extend([
        "-s",
        "-" + params.get("subject")
    ])
    if params.get("source_orig") is not None:
        cargs.extend([
            "--s+orig",
            params.get("source_orig")
        ])
    if params.get("source_long"):
        cargs.append("--s+long")
    if params.get("output_subdir") is not None:
        cargs.extend([
            "--sub",
            params.get("output_subdir")
        ])
    if params.get("gca_file") is not None:
        cargs.extend([
            "--gca",
            execution.input_file(params.get("gca_file"))
        ])
    if params.get("no_reg"):
        cargs.append("--no-reg")
    if params.get("no_canorm"):
        cargs.append("--no-canorm")
    if params.get("init_spm"):
        cargs.append("--init-spm")
    if params.get("reg_only"):
        cargs.append("--reg-only")
    if params.get("halo1"):
        cargs.append("--halo1")
    if params.get("halo2"):
        cargs.append("--halo2")
    return cargs


def wmsaseg_outputs(
    params: WmsasegParameters,
    execution: Execution,
) -> WmsasegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = WmsasegOutputs(
        root=execution.output_file("."),
        t1_canorm=execution.output_file(params.get("output_subdir") + "/T1.canorm.mgz") if (params.get("output_subdir") is not None) else None,
        wmsa_lta=execution.output_file(params.get("output_subdir") + "/wmsa.lta") if (params.get("output_subdir") is not None) else None,
    )
    return ret


def wmsaseg_execute(
    params: WmsasegParameters,
    execution: Execution,
) -> WmsasegOutputs:
    """
    White Matter Hyperintensity Segmentation Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `WmsasegOutputs`).
    """
    params = execution.params(params)
    cargs = wmsaseg_cargs(params, execution)
    ret = wmsaseg_outputs(params, execution)
    execution.run(cargs)
    return ret


def wmsaseg(
    subject: str,
    source_orig: str | None = None,
    source_long: bool = False,
    output_subdir: str | None = None,
    gca_file: InputPathType | None = None,
    no_reg: bool = False,
    no_canorm: bool = False,
    init_spm: bool = False,
    reg_only: bool = False,
    halo1: bool = False,
    halo2: bool = False,
    runner: Runner | None = None,
) -> WmsasegOutputs:
    """
    White Matter Hyperintensity Segmentation Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        source_orig: Use T2 and PD images from original subject.
        source_long: Use T2 and PD images from longitudinal subject.
        output_subdir: Output subdirectory name (default is wmsa).
        gca_file: GCA file path.
        no_reg: Do not register mode to anatomical image.
        no_canorm: Do not run mri_ca_normalize.
        init_spm: Initialize SPM (default is FSL).
        reg_only: Only perform registration.
        halo1: Halo 1 option.
        halo2: Halo 2 option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WmsasegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WMSASEG_METADATA)
    params = wmsaseg_params(subject=subject, source_orig=source_orig, source_long=source_long, output_subdir=output_subdir, gca_file=gca_file, no_reg=no_reg, no_canorm=no_canorm, init_spm=init_spm, reg_only=reg_only, halo1=halo1, halo2=halo2)
    return wmsaseg_execute(params, execution)


__all__ = [
    "WMSASEG_METADATA",
    "WmsasegOutputs",
    "WmsasegParameters",
    "wmsaseg",
    "wmsaseg_params",
]
