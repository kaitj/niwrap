# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSR_IMPORT_METADATA = Metadata(
    id="0f4f0456c8df72ab9210f36b4e8bfb88e6ceba62.boutiques",
    name="fsr-import",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
FsrImportParameters = typing.TypedDict('FsrImportParameters', {
    "__STYX_TYPE__": typing.Literal["fsr-import"],
    "outdir": str,
    "force_update": bool,
    "no_conform": bool,
    "hires": bool,
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
        "fsr-import": fsr_import_cargs,
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
        "fsr-import": fsr_import_outputs,
    }
    return vt.get(t)


class FsrImportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsr_import(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_t1w: OutputPathType
    """Output directory for T1-weighted images"""
    out_t2w: OutputPathType
    """Output directory for T2-weighted images"""
    out_flair: OutputPathType
    """Output directory for FLAIR images"""
    out_custom_modes: OutputPathType
    """Output directory for custom modality images based on mode"""


def fsr_import_params(
    outdir: str,
    force_update: bool = False,
    no_conform: bool = False,
    hires: bool = False,
) -> FsrImportParameters:
    """
    Build parameters.
    
    Args:
        outdir: Root directory for output data.
        force_update: Update files regardless of timestamp.
        no_conform: Do not conform inputs to 1mm, 256 dimensions.
        hires: Same as --no-conform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsr-import",
        "outdir": outdir,
        "force_update": force_update,
        "no_conform": no_conform,
        "hires": hires,
    }
    return params


def fsr_import_cargs(
    params: FsrImportParameters,
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
    cargs.append("fsr-import")
    cargs.extend([
        "--o",
        params.get("outdir")
    ])
    cargs.append("[T1W...]")
    cargs.append("[T2W...]")
    cargs.append("[FLAIR...]")
    cargs.append("[CUSTOM_MODES...]")
    if params.get("force_update"):
        cargs.append("--force-update")
    if params.get("no_conform"):
        cargs.append("--no-conform")
    if params.get("hires"):
        cargs.append("--hires")
    return cargs


def fsr_import_outputs(
    params: FsrImportParameters,
    execution: Execution,
) -> FsrImportOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsrImportOutputs(
        root=execution.output_file("."),
        out_t1w=execution.output_file(params.get("outdir") + "/t1w/*.mgz"),
        out_t2w=execution.output_file(params.get("outdir") + "/t2w/*.mgz"),
        out_flair=execution.output_file(params.get("outdir") + "/flair/*.mgz"),
        out_custom_modes=execution.output_file(params.get("outdir") + "/*/*.mgz"),
    )
    return ret


def fsr_import_execute(
    params: FsrImportParameters,
    execution: Execution,
) -> FsrImportOutputs:
    """
    Copies/converts data into a directory structure for samseg-expected format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsrImportOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsr_import_cargs(params, execution)
    ret = fsr_import_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsr_import(
    outdir: str,
    force_update: bool = False,
    no_conform: bool = False,
    hires: bool = False,
    runner: Runner | None = None,
) -> FsrImportOutputs:
    """
    Copies/converts data into a directory structure for samseg-expected format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outdir: Root directory for output data.
        force_update: Update files regardless of timestamp.
        no_conform: Do not conform inputs to 1mm, 256 dimensions.
        hires: Same as --no-conform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsrImportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSR_IMPORT_METADATA)
    params = fsr_import_params(outdir=outdir, force_update=force_update, no_conform=no_conform, hires=hires)
    return fsr_import_execute(params, execution)


__all__ = [
    "FSR_IMPORT_METADATA",
    "FsrImportOutputs",
    "fsr_import",
    "fsr_import_params",
]
