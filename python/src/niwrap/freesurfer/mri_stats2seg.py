# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_STATS2SEG_METADATA = Metadata(
    id="a4b8c39c09b61ee54a4a039bc3c05dcc8e51531c.boutiques",
    name="mri_stats2seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriStats2segParameters = typing.TypedDict('MriStats2segParameters', {
    "__STYX_TYPE__": typing.Literal["mri_stats2seg"],
    "stat_file": InputPathType,
    "segmentation_volume": InputPathType,
    "output_file": str,
    "debug": bool,
    "check_opts": bool,
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
        "mri_stats2seg": mri_stats2seg_cargs,
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
        "mri_stats2seg": mri_stats2seg_outputs,
    }.get(t)


class MriStats2segOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_stats2seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output: OutputPathType
    """Output segmented file."""


def mri_stats2seg_params(
    stat_file: InputPathType,
    segmentation_volume: InputPathType,
    output_file: str,
    debug: bool = False,
    check_opts: bool = False,
) -> MriStats2segParameters:
    """
    Build parameters.
    
    Args:
        stat_file: Stat file in an MRI format.
        segmentation_volume: Segmentation volume file.
        output_file: Output file.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_stats2seg",
        "stat_file": stat_file,
        "segmentation_volume": segmentation_volume,
        "output_file": output_file,
        "debug": debug,
        "check_opts": check_opts,
    }
    return params


def mri_stats2seg_cargs(
    params: MriStats2segParameters,
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
    cargs.append("mri_stats2seg")
    cargs.extend([
        "--stat",
        execution.input_file(params.get("stat_file"))
    ])
    cargs.extend([
        "--seg",
        execution.input_file(params.get("segmentation_volume"))
    ])
    cargs.extend([
        "--o",
        params.get("output_file")
    ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("check_opts"):
        cargs.append("--checkopts")
    return cargs


def mri_stats2seg_outputs(
    params: MriStats2segParameters,
    execution: Execution,
) -> MriStats2segOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriStats2segOutputs(
        root=execution.output_file("."),
        segmented_output=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_stats2seg_execute(
    params: MriStats2segParameters,
    execution: Execution,
) -> MriStats2segOutputs:
    """
    A command-line tool for converting MRI statistical maps to segmented volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriStats2segOutputs`).
    """
    params = execution.params(params)
    cargs = mri_stats2seg_cargs(params, execution)
    ret = mri_stats2seg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_stats2seg(
    stat_file: InputPathType,
    segmentation_volume: InputPathType,
    output_file: str,
    debug: bool = False,
    check_opts: bool = False,
    runner: Runner | None = None,
) -> MriStats2segOutputs:
    """
    A command-line tool for converting MRI statistical maps to segmented volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        stat_file: Stat file in an MRI format.
        segmentation_volume: Segmentation volume file.
        output_file: Output file.
        debug: Turn on debugging.
        check_opts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriStats2segOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_STATS2SEG_METADATA)
    params = mri_stats2seg_params(stat_file=stat_file, segmentation_volume=segmentation_volume, output_file=output_file, debug=debug, check_opts=check_opts)
    return mri_stats2seg_execute(params, execution)


__all__ = [
    "MRI_STATS2SEG_METADATA",
    "MriStats2segOutputs",
    "MriStats2segParameters",
    "mri_stats2seg",
    "mri_stats2seg_params",
]
