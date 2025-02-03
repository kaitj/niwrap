# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EXVIVO_STRIP_METADATA = Metadata(
    id="656236688df22fbf848368ed1bf41f141adaf38d.boutiques",
    name="mri_exvivo_strip",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriExvivoStripParameters = typing.TypedDict('MriExvivoStripParameters', {
    "__STYX_TYPE__": typing.Literal["mri_exvivo_strip"],
    "invol": InputPathType,
    "outvol": str,
    "hemi": str,
    "pred": typing.NotRequired[InputPathType | None],
    "norm": typing.NotRequired[InputPathType | None],
    "fv": bool,
    "uthresh": typing.NotRequired[float | None],
    "border": typing.NotRequired[float | None],
    "multichannel": bool,
    "model": typing.NotRequired[InputPathType | None],
    "wts": typing.NotRequired[InputPathType | None],
    "gpu": typing.NotRequired[float | None],
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
        "mri_exvivo_strip": mri_exvivo_strip_cargs,
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
        "mri_exvivo_strip": mri_exvivo_strip_outputs,
    }
    return vt.get(t)


class MriExvivoStripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_exvivo_strip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Processed output MRI volume"""
    prediction_output: OutputPathType | None
    """Prediction volume if specified"""
    normalized_output: OutputPathType | None
    """Normalized volume if specified"""


def mri_exvivo_strip_params(
    invol: InputPathType,
    outvol: str,
    hemi: str,
    pred: InputPathType | None = None,
    norm: InputPathType | None = None,
    fv: bool = False,
    uthresh: float | None = None,
    border: float | None = None,
    multichannel: bool = False,
    model: InputPathType | None = None,
    wts: InputPathType | None = None,
    gpu: float | None = None,
) -> MriExvivoStripParameters:
    """
    Build parameters.
    
    Args:
        invol: Input MRI volume.
        outvol: Output MRI volume.
        hemi: Hemi to process.
        pred: Write prediction volume.
        norm: Write normalized volume.
        fv: Bring up freeview to show results.
        uthresh: Specify threshold to erase above.
        border: Number of border voxels to set threshold at.
        multichannel: Specify that data has multiple channels.
        model: Use alternative model file.
        wts: Weight filename.
        gpu: GPU number - if not supplied, CPU is used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_exvivo_strip",
        "invol": invol,
        "outvol": outvol,
        "hemi": hemi,
        "fv": fv,
        "multichannel": multichannel,
    }
    if pred is not None:
        params["pred"] = pred
    if norm is not None:
        params["norm"] = norm
    if uthresh is not None:
        params["uthresh"] = uthresh
    if border is not None:
        params["border"] = border
    if model is not None:
        params["model"] = model
    if wts is not None:
        params["wts"] = wts
    if gpu is not None:
        params["gpu"] = gpu
    return params


def mri_exvivo_strip_cargs(
    params: MriExvivoStripParameters,
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
    cargs.append("mri_exvivo_strip")
    cargs.extend([
        "-i",
        execution.input_file(params.get("invol"))
    ])
    cargs.extend([
        "-o",
        params.get("outvol")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    if params.get("pred") is not None:
        cargs.extend([
            "--pred",
            execution.input_file(params.get("pred"))
        ])
    if params.get("norm") is not None:
        cargs.extend([
            "--norm",
            execution.input_file(params.get("norm"))
        ])
    if params.get("fv"):
        cargs.append("--fv")
    if params.get("uthresh") is not None:
        cargs.extend([
            "--uthresh",
            str(params.get("uthresh"))
        ])
    if params.get("border") is not None:
        cargs.extend([
            "--border",
            str(params.get("border"))
        ])
    if params.get("multichannel"):
        cargs.append("--multichannel")
    if params.get("model") is not None:
        cargs.extend([
            "--model",
            execution.input_file(params.get("model"))
        ])
    if params.get("wts") is not None:
        cargs.extend([
            "--wts",
            execution.input_file(params.get("wts"))
        ])
    if params.get("gpu") is not None:
        cargs.extend([
            "--gpu",
            str(params.get("gpu"))
        ])
    return cargs


def mri_exvivo_strip_outputs(
    params: MriExvivoStripParameters,
    execution: Execution,
) -> MriExvivoStripOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriExvivoStripOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("outvol")),
        prediction_output=execution.output_file(pathlib.Path(params.get("pred")).name) if (params.get("pred") is not None) else None,
        normalized_output=execution.output_file(pathlib.Path(params.get("norm")).name) if (params.get("norm") is not None) else None,
    )
    return ret


def mri_exvivo_strip_execute(
    params: MriExvivoStripParameters,
    execution: Execution,
) -> MriExvivoStripOutputs:
    """
    Tool for processing MRI volumes for ex vivo data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriExvivoStripOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_exvivo_strip_cargs(params, execution)
    ret = mri_exvivo_strip_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_exvivo_strip(
    invol: InputPathType,
    outvol: str,
    hemi: str,
    pred: InputPathType | None = None,
    norm: InputPathType | None = None,
    fv: bool = False,
    uthresh: float | None = None,
    border: float | None = None,
    multichannel: bool = False,
    model: InputPathType | None = None,
    wts: InputPathType | None = None,
    gpu: float | None = None,
    runner: Runner | None = None,
) -> MriExvivoStripOutputs:
    """
    Tool for processing MRI volumes for ex vivo data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        invol: Input MRI volume.
        outvol: Output MRI volume.
        hemi: Hemi to process.
        pred: Write prediction volume.
        norm: Write normalized volume.
        fv: Bring up freeview to show results.
        uthresh: Specify threshold to erase above.
        border: Number of border voxels to set threshold at.
        multichannel: Specify that data has multiple channels.
        model: Use alternative model file.
        wts: Weight filename.
        gpu: GPU number - if not supplied, CPU is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriExvivoStripOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EXVIVO_STRIP_METADATA)
    params = mri_exvivo_strip_params(invol=invol, outvol=outvol, hemi=hemi, pred=pred, norm=norm, fv=fv, uthresh=uthresh, border=border, multichannel=multichannel, model=model, wts=wts, gpu=gpu)
    return mri_exvivo_strip_execute(params, execution)


__all__ = [
    "MRI_EXVIVO_STRIP_METADATA",
    "MriExvivoStripOutputs",
    "mri_exvivo_strip",
    "mri_exvivo_strip_params",
]
