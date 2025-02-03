# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_NORMALIZE_TP2_METADATA = Metadata(
    id="aee73f5df022fe02e7fc4d5e4771e952936204f3.boutiques",
    name="mri_normalize_tp2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNormalizeTp2Parameters = typing.TypedDict('MriNormalizeTp2Parameters', {
    "__STYX_TYPE__": typing.Literal["mri_normalize_tp2"],
    "input_vol": InputPathType,
    "normalized_vol": str,
    "t1_volume": typing.NotRequired[InputPathType | None],
    "mask1": typing.NotRequired[InputPathType | None],
    "mask2": typing.NotRequired[InputPathType | None],
    "threshold": typing.NotRequired[float | None],
    "ctrl": typing.NotRequired[InputPathType | None],
    "xform": typing.NotRequired[InputPathType | None],
    "invert_flag": bool,
    "lta_src": typing.NotRequired[InputPathType | None],
    "lta_dst": typing.NotRequired[InputPathType | None],
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
        "mri_normalize_tp2": mri_normalize_tp2_cargs,
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
        "mri_normalize_tp2": mri_normalize_tp2_outputs,
    }
    return vt.get(t)


class MriNormalizeTp2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_normalize_tp2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_normalized_vol: OutputPathType
    """The resulting normalized volume"""


def mri_normalize_tp2_params(
    input_vol: InputPathType,
    normalized_vol: str,
    t1_volume: InputPathType | None = None,
    mask1: InputPathType | None = None,
    mask2: InputPathType | None = None,
    threshold: float | None = None,
    ctrl: InputPathType | None = None,
    xform: InputPathType | None = None,
    invert_flag: bool = False,
    lta_src: InputPathType | None = None,
    lta_dst: InputPathType | None = None,
) -> MriNormalizeTp2Parameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input volume to be normalized.
        normalized_vol: Output normalized volume.
        t1_volume: T1 volume for tp1 where normalization is applied.
        mask1: Brain mask for tp1, mapped to tp2 via the xform.
        mask2: Brain mask for tp2, mapped to tp1 via the inverse xform.
        threshold: Threshold for background (default = 1.0).
        ctrl: Control point volume for tp1.
        xform: LTA transform that aligns tp1 to tp2.
        invert_flag: Reversely apply -xform.
        lta_src: Source volume for -xform if not available from the xform file.
        lta_dst: Target volume for -xform if not available from the xform file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_normalize_tp2",
        "input_vol": input_vol,
        "normalized_vol": normalized_vol,
        "invert_flag": invert_flag,
    }
    if t1_volume is not None:
        params["t1_volume"] = t1_volume
    if mask1 is not None:
        params["mask1"] = mask1
    if mask2 is not None:
        params["mask2"] = mask2
    if threshold is not None:
        params["threshold"] = threshold
    if ctrl is not None:
        params["ctrl"] = ctrl
    if xform is not None:
        params["xform"] = xform
    if lta_src is not None:
        params["lta_src"] = lta_src
    if lta_dst is not None:
        params["lta_dst"] = lta_dst
    return params


def mri_normalize_tp2_cargs(
    params: MriNormalizeTp2Parameters,
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
    cargs.append("mri_normalize_tp2")
    cargs.append(execution.input_file(params.get("input_vol")))
    cargs.append(params.get("normalized_vol"))
    if params.get("t1_volume") is not None:
        cargs.extend([
            "-T1",
            execution.input_file(params.get("t1_volume"))
        ])
    if params.get("mask1") is not None:
        cargs.extend([
            "-mask1",
            execution.input_file(params.get("mask1"))
        ])
    if params.get("mask2") is not None:
        cargs.extend([
            "-mask2",
            execution.input_file(params.get("mask2"))
        ])
    if params.get("threshold") is not None:
        cargs.extend([
            "-threshold",
            str(params.get("threshold"))
        ])
    if params.get("ctrl") is not None:
        cargs.extend([
            "-ctrl",
            execution.input_file(params.get("ctrl"))
        ])
    if params.get("xform") is not None:
        cargs.extend([
            "-xform",
            execution.input_file(params.get("xform"))
        ])
    if params.get("invert_flag"):
        cargs.append("-invert")
    if params.get("lta_src") is not None:
        cargs.extend([
            "-lta_src",
            execution.input_file(params.get("lta_src"))
        ])
    if params.get("lta_dst") is not None:
        cargs.extend([
            "-lta_dst",
            execution.input_file(params.get("lta_dst"))
        ])
    return cargs


def mri_normalize_tp2_outputs(
    params: MriNormalizeTp2Parameters,
    execution: Execution,
) -> MriNormalizeTp2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNormalizeTp2Outputs(
        root=execution.output_file("."),
        output_normalized_vol=execution.output_file(params.get("normalized_vol")),
    )
    return ret


def mri_normalize_tp2_execute(
    params: MriNormalizeTp2Parameters,
    execution: Execution,
) -> MriNormalizeTp2Outputs:
    """
    Normalize the input volume using control points of tp1 to help normalize tp2.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNormalizeTp2Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_normalize_tp2_cargs(params, execution)
    ret = mri_normalize_tp2_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_normalize_tp2(
    input_vol: InputPathType,
    normalized_vol: str,
    t1_volume: InputPathType | None = None,
    mask1: InputPathType | None = None,
    mask2: InputPathType | None = None,
    threshold: float | None = None,
    ctrl: InputPathType | None = None,
    xform: InputPathType | None = None,
    invert_flag: bool = False,
    lta_src: InputPathType | None = None,
    lta_dst: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriNormalizeTp2Outputs:
    """
    Normalize the input volume using control points of tp1 to help normalize tp2.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input volume to be normalized.
        normalized_vol: Output normalized volume.
        t1_volume: T1 volume for tp1 where normalization is applied.
        mask1: Brain mask for tp1, mapped to tp2 via the xform.
        mask2: Brain mask for tp2, mapped to tp1 via the inverse xform.
        threshold: Threshold for background (default = 1.0).
        ctrl: Control point volume for tp1.
        xform: LTA transform that aligns tp1 to tp2.
        invert_flag: Reversely apply -xform.
        lta_src: Source volume for -xform if not available from the xform file.
        lta_dst: Target volume for -xform if not available from the xform file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNormalizeTp2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NORMALIZE_TP2_METADATA)
    params = mri_normalize_tp2_params(input_vol=input_vol, normalized_vol=normalized_vol, t1_volume=t1_volume, mask1=mask1, mask2=mask2, threshold=threshold, ctrl=ctrl, xform=xform, invert_flag=invert_flag, lta_src=lta_src, lta_dst=lta_dst)
    return mri_normalize_tp2_execute(params, execution)


__all__ = [
    "MRI_NORMALIZE_TP2_METADATA",
    "MriNormalizeTp2Outputs",
    "mri_normalize_tp2",
    "mri_normalize_tp2_params",
]
