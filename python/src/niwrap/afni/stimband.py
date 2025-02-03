# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

STIMBAND_METADATA = Metadata(
    id="464e80031a1b4a970344b72621a7160776336ad8.boutiques",
    name="stimband",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
StimbandParameters = typing.TypedDict('StimbandParameters', {
    "__STYX_TYPE__": typing.Literal["stimband"],
    "verbose_flag": bool,
    "min_freq": typing.NotRequired[float | None],
    "min_bwidth": typing.NotRequired[float | None],
    "min_pow": typing.NotRequired[float | None],
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
        "stimband": stimband_cargs,
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
        "stimband": stimband_outputs,
    }
    return vt.get(t)


class StimbandOutputs(typing.NamedTuple):
    """
    Output object returned when calling `stimband(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_band: OutputPathType
    """The frequency band covering at least 90% of the power of the stimulus
    columns."""


def stimband_params(
    verbose_flag: bool = False,
    min_freq: float | None = None,
    min_bwidth: float | None = None,
    min_pow: float | None = None,
) -> StimbandParameters:
    """
    Build parameters.
    
    Args:
        verbose_flag: Print the power band for each individual stimulus column\
            from each matrix.
        min_freq: Set the minimum frequency output for the band. Default value\
            is 0.01.
        min_bwidth: Set the minimum bandwidth output (top frequency minus\
            bottom frequency). Default is 0.03.
        min_pow: Set the minimum power fraction (percentage) to 'ff' instead of\
            the default 90%. Value must be in the range 50..99.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "stimband",
        "verbose_flag": verbose_flag,
    }
    if min_freq is not None:
        params["min_freq"] = min_freq
    if min_bwidth is not None:
        params["min_bwidth"] = min_bwidth
    if min_pow is not None:
        params["min_pow"] = min_pow
    return params


def stimband_cargs(
    params: StimbandParameters,
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
    cargs.append("stimband")
    if params.get("verbose_flag"):
        cargs.append("-verb")
    cargs.append("[MATRIXFILES...]")
    cargs.append("[ADDITIONAL_MATRIXFILES...]")
    if params.get("min_freq") is not None:
        cargs.extend([
            "-min_freq",
            str(params.get("min_freq"))
        ])
    if params.get("min_bwidth") is not None:
        cargs.extend([
            "-min_bwidth",
            str(params.get("min_bwidth"))
        ])
    if params.get("min_pow") is not None:
        cargs.extend([
            "-min_pow",
            str(params.get("min_pow"))
        ])
    return cargs


def stimband_outputs(
    params: StimbandParameters,
    execution: Execution,
) -> StimbandOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = StimbandOutputs(
        root=execution.output_file("."),
        output_band=execution.output_file("stdout"),
    )
    return ret


def stimband_execute(
    params: StimbandParameters,
    execution: Execution,
) -> StimbandOutputs:
    """
    Determines frequency band covering at least 90% of the 'power' (|FFT|^2) of
    stimulus columns from X.nocensor.xmat.1D files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `StimbandOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = stimband_cargs(params, execution)
    ret = stimband_outputs(params, execution)
    execution.run(cargs)
    return ret


def stimband(
    verbose_flag: bool = False,
    min_freq: float | None = None,
    min_bwidth: float | None = None,
    min_pow: float | None = None,
    runner: Runner | None = None,
) -> StimbandOutputs:
    """
    Determines frequency band covering at least 90% of the 'power' (|FFT|^2) of
    stimulus columns from X.nocensor.xmat.1D files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        verbose_flag: Print the power band for each individual stimulus column\
            from each matrix.
        min_freq: Set the minimum frequency output for the band. Default value\
            is 0.01.
        min_bwidth: Set the minimum bandwidth output (top frequency minus\
            bottom frequency). Default is 0.03.
        min_pow: Set the minimum power fraction (percentage) to 'ff' instead of\
            the default 90%. Value must be in the range 50..99.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StimbandOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STIMBAND_METADATA)
    params = stimband_params(verbose_flag=verbose_flag, min_freq=min_freq, min_bwidth=min_bwidth, min_pow=min_pow)
    return stimband_execute(params, execution)


__all__ = [
    "STIMBAND_METADATA",
    "StimbandOutputs",
    "stimband",
    "stimband_params",
]
