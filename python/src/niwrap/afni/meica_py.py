# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MEICA_PY_METADATA = Metadata(
    id="4f8853ae256f37ea17513108bcc3c27cb471dc45.boutiques",
    name="meica.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
MeicaPyParameters = typing.TypedDict('MeicaPyParameters', {
    "__STYX_TYPE__": typing.Literal["meica.py"],
    "infile": InputPathType,
    "echo_times": str,
    "affine": str,
    "output_directory": str,
    "components": typing.NotRequired[float | None],
    "talairach": bool,
    "threshold": typing.NotRequired[float | None],
    "debug": bool,
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
        "meica.py": meica_py_cargs,
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
        "meica.py": meica_py_outputs,
    }
    return vt.get(t)


class MeicaPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meica_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cleaned_bold: OutputPathType
    """Cleaned BOLD image after ME-ICA processing"""
    components_output: OutputPathType
    """Independent components result of ICA"""


def meica_py_params(
    infile: InputPathType,
    echo_times: str,
    affine: str,
    output_directory: str,
    components: float | None = None,
    talairach: bool = False,
    threshold: float | None = None,
    debug: bool = False,
) -> MeicaPyParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image dataset (e.g. dataset.nii.gz).
        echo_times: Echo times (e.g. 15.0,30.0,45.0).
        affine: Affine registration matrix.
        output_directory: Output directory.
        components: Number of components for ICA.
        talairach: Apply standard Talairach transformation.
        threshold: Threshold value for masking.
        debug: Enable debug mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "meica.py",
        "infile": infile,
        "echo_times": echo_times,
        "affine": affine,
        "output_directory": output_directory,
        "talairach": talairach,
        "debug": debug,
    }
    if components is not None:
        params["components"] = components
    if threshold is not None:
        params["threshold"] = threshold
    return params


def meica_py_cargs(
    params: MeicaPyParameters,
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
    cargs.append("meica.py")
    cargs.extend([
        "-d",
        execution.input_file(params.get("infile"))
    ])
    cargs.extend([
        "-e",
        params.get("echo_times")
    ])
    cargs.extend([
        "-a",
        params.get("affine")
    ])
    cargs.extend([
        "-o",
        params.get("output_directory")
    ])
    if params.get("components") is not None:
        cargs.extend([
            "-c",
            str(params.get("components"))
        ])
    if params.get("talairach"):
        cargs.append("-t")
    if params.get("threshold") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("threshold"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def meica_py_outputs(
    params: MeicaPyParameters,
    execution: Execution,
) -> MeicaPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MeicaPyOutputs(
        root=execution.output_file("."),
        cleaned_bold=execution.output_file(params.get("output_directory") + "/cleaned_bold.nii.gz"),
        components_output=execution.output_file(params.get("output_directory") + "/components.nii.gz"),
    )
    return ret


def meica_py_execute(
    params: MeicaPyParameters,
    execution: Execution,
) -> MeicaPyOutputs:
    """
    Multi-Echo Independent Component Analysis for fMRI denoising.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MeicaPyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = meica_py_cargs(params, execution)
    ret = meica_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def meica_py(
    infile: InputPathType,
    echo_times: str,
    affine: str,
    output_directory: str,
    components: float | None = None,
    talairach: bool = False,
    threshold: float | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> MeicaPyOutputs:
    """
    Multi-Echo Independent Component Analysis for fMRI denoising.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input image dataset (e.g. dataset.nii.gz).
        echo_times: Echo times (e.g. 15.0,30.0,45.0).
        affine: Affine registration matrix.
        output_directory: Output directory.
        components: Number of components for ICA.
        talairach: Apply standard Talairach transformation.
        threshold: Threshold value for masking.
        debug: Enable debug mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MeicaPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEICA_PY_METADATA)
    params = meica_py_params(infile=infile, echo_times=echo_times, affine=affine, output_directory=output_directory, components=components, talairach=talairach, threshold=threshold, debug=debug)
    return meica_py_execute(params, execution)


__all__ = [
    "MEICA_PY_METADATA",
    "MeicaPyOutputs",
    "meica_py",
    "meica_py_params",
]
