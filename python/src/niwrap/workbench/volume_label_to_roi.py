# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_LABEL_TO_ROI_METADATA = Metadata(
    id="b3cda0fa9bc982ba11f500591ea9473a5a0a4fc2.boutiques",
    name="volume-label-to-roi",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
VolumeLabelToRoiParameters = typing.TypedDict('VolumeLabelToRoiParameters', {
    "__STYX_TYPE__": typing.Literal["volume-label-to-roi"],
    "label_in": InputPathType,
    "volume_out": str,
    "opt_name_label_name": typing.NotRequired[str | None],
    "opt_key_label_key": typing.NotRequired[int | None],
    "opt_map_map": typing.NotRequired[str | None],
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
        "volume-label-to-roi": volume_label_to_roi_cargs,
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
        "volume-label-to-roi": volume_label_to_roi_outputs,
    }
    return vt.get(t)


class VolumeLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_to_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume file"""


def volume_label_to_roi_params(
    label_in: InputPathType,
    volume_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
) -> VolumeLabelToRoiParameters:
    """
    Build parameters.
    
    Args:
        label_in: the input volume label file.
        volume_out: the output volume file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "volume-label-to-roi",
        "label_in": label_in,
        "volume_out": volume_out,
    }
    if opt_name_label_name is not None:
        params["opt_name_label_name"] = opt_name_label_name
    if opt_key_label_key is not None:
        params["opt_key_label_key"] = opt_key_label_key
    if opt_map_map is not None:
        params["opt_map_map"] = opt_map_map
    return params


def volume_label_to_roi_cargs(
    params: VolumeLabelToRoiParameters,
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
    cargs.append("wb_command")
    cargs.append("-volume-label-to-roi")
    cargs.append(execution.input_file(params.get("label_in")))
    cargs.append(params.get("volume_out"))
    if params.get("opt_name_label_name") is not None:
        cargs.extend([
            "-name",
            params.get("opt_name_label_name")
        ])
    if params.get("opt_key_label_key") is not None:
        cargs.extend([
            "-key",
            str(params.get("opt_key_label_key"))
        ])
    if params.get("opt_map_map") is not None:
        cargs.extend([
            "-map",
            params.get("opt_map_map")
        ])
    return cargs


def volume_label_to_roi_outputs(
    params: VolumeLabelToRoiParameters,
    execution: Execution,
) -> VolumeLabelToRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VolumeLabelToRoiOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(params.get("volume_out")),
    )
    return ret


def volume_label_to_roi_execute(
    params: VolumeLabelToRoiParameters,
    execution: Execution,
) -> VolumeLabelToRoiOutputs:
    """
    Make a volume label into an roi volume.
    
    For each map in <label-in>, a map is created in <volume-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToRoiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = volume_label_to_roi_cargs(params, execution)
    ret = volume_label_to_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def volume_label_to_roi(
    label_in: InputPathType,
    volume_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
    runner: Runner | None = None,
) -> VolumeLabelToRoiOutputs:
    """
    Make a volume label into an roi volume.
    
    For each map in <label-in>, a map is created in <volume-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        label_in: the input volume label file.
        volume_out: the output volume file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeLabelToRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_TO_ROI_METADATA)
    params = volume_label_to_roi_params(label_in=label_in, volume_out=volume_out, opt_name_label_name=opt_name_label_name, opt_key_label_key=opt_key_label_key, opt_map_map=opt_map_map)
    return volume_label_to_roi_execute(params, execution)


__all__ = [
    "VOLUME_LABEL_TO_ROI_METADATA",
    "VolumeLabelToRoiOutputs",
    "volume_label_to_roi",
    "volume_label_to_roi_params",
]
