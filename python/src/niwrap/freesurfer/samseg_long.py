# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SAMSEG_LONG_METADATA = Metadata(
    id="686e2f45cf8bcf8f37552255f101cc1d16f93f40.boutiques",
    name="samseg-long",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SamsegLongParameters = typing.TypedDict('SamsegLongParameters', {
    "__STYX_TYPE__": typing.Literal["samseg-long"],
    "output_dir": str,
    "align_no_mc": bool,
    "threads": typing.NotRequired[float | None],
    "input_files": list[InputPathType],
    "save_posteriors": bool,
    "force_update": bool,
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
        "samseg-long": samseg_long_cargs,
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
        "samseg-long": samseg_long_outputs,
    }
    return vt.get(t)


class SamsegLongOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samseg_long(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tp001_output: OutputPathType
    """Samseg output folder for the first time point."""
    tp002_output: OutputPathType
    """Samseg output folder for the second time point."""
    base_output: OutputPathType
    """Base folder created by the samseg-long process."""


def samseg_long_params(
    output_dir: str,
    input_files: list[InputPathType],
    align_no_mc: bool = False,
    threads: float | None = None,
    save_posteriors: bool = False,
    force_update: bool = False,
) -> SamsegLongParameters:
    """
    Build parameters.
    
    Args:
        output_dir: Output directory.
        input_files: Input image files. All inputs must be a single modality.
        align_no_mc: Do not align inputs using robust register.
        threads: Number of threads to use.
        save_posteriors: Save posterior probabilities.
        force_update: Force update of outputs.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "samseg-long",
        "output_dir": output_dir,
        "align_no_mc": align_no_mc,
        "input_files": input_files,
        "save_posteriors": save_posteriors,
        "force_update": force_update,
    }
    if threads is not None:
        params["threads"] = threads
    return params


def samseg_long_cargs(
    params: SamsegLongParameters,
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
    cargs.append("samseg-long")
    cargs.extend([
        "--o",
        params.get("output_dir")
    ])
    if params.get("align_no_mc"):
        cargs.append("--no-mc")
    if params.get("threads") is not None:
        cargs.extend([
            "--threads",
            str(params.get("threads"))
        ])
    cargs.extend([
        "--i",
        *[execution.input_file(f) for f in params.get("input_files")]
    ])
    if params.get("save_posteriors"):
        cargs.append("--save-posteriors")
    if params.get("force_update"):
        cargs.append("--force-update")
    return cargs


def samseg_long_outputs(
    params: SamsegLongParameters,
    execution: Execution,
) -> SamsegLongOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SamsegLongOutputs(
        root=execution.output_file("."),
        tp001_output=execution.output_file(params.get("output_dir") + "/tp001"),
        tp002_output=execution.output_file(params.get("output_dir") + "/tp002"),
        base_output=execution.output_file(params.get("output_dir") + "/base"),
    )
    return ret


def samseg_long_execute(
    params: SamsegLongParameters,
    execution: Execution,
) -> SamsegLongOutputs:
    """
    Longitudinal analysis tool using SAMSEG in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SamsegLongOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = samseg_long_cargs(params, execution)
    ret = samseg_long_outputs(params, execution)
    execution.run(cargs)
    return ret


def samseg_long(
    output_dir: str,
    input_files: list[InputPathType],
    align_no_mc: bool = False,
    threads: float | None = None,
    save_posteriors: bool = False,
    force_update: bool = False,
    runner: Runner | None = None,
) -> SamsegLongOutputs:
    """
    Longitudinal analysis tool using SAMSEG in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_dir: Output directory.
        input_files: Input image files. All inputs must be a single modality.
        align_no_mc: Do not align inputs using robust register.
        threads: Number of threads to use.
        save_posteriors: Save posterior probabilities.
        force_update: Force update of outputs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SamsegLongOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMSEG_LONG_METADATA)
    params = samseg_long_params(output_dir=output_dir, align_no_mc=align_no_mc, threads=threads, input_files=input_files, save_posteriors=save_posteriors, force_update=force_update)
    return samseg_long_execute(params, execution)


__all__ = [
    "SAMSEG_LONG_METADATA",
    "SamsegLongOutputs",
    "samseg_long",
    "samseg_long_params",
]
