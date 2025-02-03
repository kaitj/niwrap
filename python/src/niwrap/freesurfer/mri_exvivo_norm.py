# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EXVIVO_NORM_METADATA = Metadata(
    id="a88bc50afe4bde5d431a45ef570ba7c5a89a8c36.boutiques",
    name="mri_exvivo_norm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriExvivoNormParameters = typing.TypedDict('MriExvivoNormParameters', {
    "__STYX_TYPE__": typing.Literal["mri_exvivo_norm"],
    "input_volume": InputPathType,
    "output_volume": str,
    "hemi": str,
    "prediction_volume": typing.NotRequired[str | None],
    "normalized_volume": typing.NotRequired[str | None],
    "freeview": bool,
    "normalize_output_mean": bool,
    "write_normalization_rounds": bool,
    "upper_threshold": typing.NotRequired[float | None],
    "bias_field_sigma": typing.NotRequired[float | None],
    "normalization_rounds": typing.NotRequired[float | None],
    "multichannel": bool,
    "model_file": typing.NotRequired[InputPathType | None],
    "weights_file": typing.NotRequired[InputPathType | None],
    "gpu_number": typing.NotRequired[float | None],
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
        "mri_exvivo_norm": mri_exvivo_norm_cargs,
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
        "mri_exvivo_norm": mri_exvivo_norm_outputs,
    }
    return vt.get(t)


class MriExvivoNormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_exvivo_norm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Output MRI volume"""


def mri_exvivo_norm_params(
    input_volume: InputPathType,
    output_volume: str,
    hemi: str,
    prediction_volume: str | None = None,
    normalized_volume: str | None = None,
    freeview: bool = False,
    normalize_output_mean: bool = False,
    write_normalization_rounds: bool = False,
    upper_threshold: float | None = None,
    bias_field_sigma: float | None = None,
    normalization_rounds: float | None = None,
    multichannel: bool = False,
    model_file: InputPathType | None = None,
    weights_file: InputPathType | None = None,
    gpu_number: float | None = None,
) -> MriExvivoNormParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Input MRI volume.
        output_volume: Output MRI volume.
        hemi: Hemi to process.
        prediction_volume: Write prediction volume.
        normalized_volume: Write normalized volume.
        freeview: Bring up freeview to show results.
        normalize_output_mean: Normalize output mean to match input mean.
        write_normalization_rounds: Write normalization results after each\
            round.
        upper_threshold: Specify threshold to erase above.
        bias_field_sigma: Sigma to smooth bias field.
        normalization_rounds: Number of rounds of iterative normalization to\
            apply.
        multichannel: Specify that data has multiple channels.
        model_file: Use alternative model file.
        weights_file: Alternative weights filename.
        gpu_number: GPU number - if not supplied, CPU is used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_exvivo_norm",
        "input_volume": input_volume,
        "output_volume": output_volume,
        "hemi": hemi,
        "freeview": freeview,
        "normalize_output_mean": normalize_output_mean,
        "write_normalization_rounds": write_normalization_rounds,
        "multichannel": multichannel,
    }
    if prediction_volume is not None:
        params["prediction_volume"] = prediction_volume
    if normalized_volume is not None:
        params["normalized_volume"] = normalized_volume
    if upper_threshold is not None:
        params["upper_threshold"] = upper_threshold
    if bias_field_sigma is not None:
        params["bias_field_sigma"] = bias_field_sigma
    if normalization_rounds is not None:
        params["normalization_rounds"] = normalization_rounds
    if model_file is not None:
        params["model_file"] = model_file
    if weights_file is not None:
        params["weights_file"] = weights_file
    if gpu_number is not None:
        params["gpu_number"] = gpu_number
    return params


def mri_exvivo_norm_cargs(
    params: MriExvivoNormParameters,
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
    cargs.append("mri_exvivo_norm")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_volume"))
    ])
    cargs.extend([
        "-o",
        params.get("output_volume")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    if params.get("prediction_volume") is not None:
        cargs.extend([
            "--pred",
            params.get("prediction_volume")
        ])
    if params.get("normalized_volume") is not None:
        cargs.extend([
            "--norm",
            params.get("normalized_volume")
        ])
    if params.get("freeview"):
        cargs.append("--fv")
    if params.get("normalize_output_mean"):
        cargs.append("--norm_mean")
    if params.get("write_normalization_rounds"):
        cargs.append("--write_rounds")
    if params.get("upper_threshold") is not None:
        cargs.extend([
            "--uthresh",
            str(params.get("upper_threshold"))
        ])
    if params.get("bias_field_sigma") is not None:
        cargs.extend([
            "--sigma",
            str(params.get("bias_field_sigma"))
        ])
    if params.get("normalization_rounds") is not None:
        cargs.extend([
            "--nrounds",
            str(params.get("normalization_rounds"))
        ])
    if params.get("multichannel"):
        cargs.append("--multichannel")
    if params.get("model_file") is not None:
        cargs.extend([
            "--model",
            execution.input_file(params.get("model_file"))
        ])
    if params.get("weights_file") is not None:
        cargs.extend([
            "--wts",
            execution.input_file(params.get("weights_file"))
        ])
    if params.get("gpu_number") is not None:
        cargs.extend([
            "--gpu",
            str(params.get("gpu_number"))
        ])
    return cargs


def mri_exvivo_norm_outputs(
    params: MriExvivoNormParameters,
    execution: Execution,
) -> MriExvivoNormOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriExvivoNormOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_exvivo_norm_execute(
    params: MriExvivoNormParameters,
    execution: Execution,
) -> MriExvivoNormOutputs:
    """
    MRI Ex Vivo Normalization Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriExvivoNormOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_exvivo_norm_cargs(params, execution)
    ret = mri_exvivo_norm_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_exvivo_norm(
    input_volume: InputPathType,
    output_volume: str,
    hemi: str,
    prediction_volume: str | None = None,
    normalized_volume: str | None = None,
    freeview: bool = False,
    normalize_output_mean: bool = False,
    write_normalization_rounds: bool = False,
    upper_threshold: float | None = None,
    bias_field_sigma: float | None = None,
    normalization_rounds: float | None = None,
    multichannel: bool = False,
    model_file: InputPathType | None = None,
    weights_file: InputPathType | None = None,
    gpu_number: float | None = None,
    runner: Runner | None = None,
) -> MriExvivoNormOutputs:
    """
    MRI Ex Vivo Normalization Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MRI volume.
        output_volume: Output MRI volume.
        hemi: Hemi to process.
        prediction_volume: Write prediction volume.
        normalized_volume: Write normalized volume.
        freeview: Bring up freeview to show results.
        normalize_output_mean: Normalize output mean to match input mean.
        write_normalization_rounds: Write normalization results after each\
            round.
        upper_threshold: Specify threshold to erase above.
        bias_field_sigma: Sigma to smooth bias field.
        normalization_rounds: Number of rounds of iterative normalization to\
            apply.
        multichannel: Specify that data has multiple channels.
        model_file: Use alternative model file.
        weights_file: Alternative weights filename.
        gpu_number: GPU number - if not supplied, CPU is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriExvivoNormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EXVIVO_NORM_METADATA)
    params = mri_exvivo_norm_params(input_volume=input_volume, output_volume=output_volume, hemi=hemi, prediction_volume=prediction_volume, normalized_volume=normalized_volume, freeview=freeview, normalize_output_mean=normalize_output_mean, write_normalization_rounds=write_normalization_rounds, upper_threshold=upper_threshold, bias_field_sigma=bias_field_sigma, normalization_rounds=normalization_rounds, multichannel=multichannel, model_file=model_file, weights_file=weights_file, gpu_number=gpu_number)
    return mri_exvivo_norm_execute(params, execution)


__all__ = [
    "MRI_EXVIVO_NORM_METADATA",
    "MriExvivoNormOutputs",
    "mri_exvivo_norm",
    "mri_exvivo_norm_params",
]
