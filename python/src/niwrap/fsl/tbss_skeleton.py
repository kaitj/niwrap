# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TBSS_SKELETON_METADATA = Metadata(
    id="25571f737489a24f1ca40f7027b3aa2c256d8dc2.boutiques",
    name="tbss_skeleton",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
TbssSkeletonParameters = typing.TypedDict('TbssSkeletonParameters', {
    "__STYX_TYPE__": typing.Literal["tbss_skeleton"],
    "input_image": InputPathType,
    "output_image": typing.NotRequired[str | None],
    "skeleton_params": typing.NotRequired[list[str] | None],
    "alt_4d": typing.NotRequired[InputPathType | None],
    "alt_skeleton": typing.NotRequired[InputPathType | None],
    "debug_flag": bool,
    "debug2_flag": typing.NotRequired[InputPathType | None],
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
        "tbss_skeleton": tbss_skeleton_cargs,
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
        "tbss_skeleton": tbss_skeleton_outputs,
    }.get(t)


class TbssSkeletonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_skeleton(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType | None
    """Output skeleton image"""
    projected_4d_file: OutputPathType
    """Projected 4D data"""
    alt_4d_file: OutputPathType | None
    """Alternative 4D data"""
    alt_skeleton_file: OutputPathType | None
    """Alternative skeleton image"""
    debug2_image_outputs: OutputPathType | None
    """De-projected skelpoints points on skeleton back to all_FA space"""


def tbss_skeleton_params(
    input_image: InputPathType,
    output_image: str | None = None,
    skeleton_params: list[str] | None = None,
    alt_4d: InputPathType | None = None,
    alt_skeleton: InputPathType | None = None,
    debug_flag: bool = False,
    debug2_flag: InputPathType | None = None,
) -> TbssSkeletonParameters:
    """
    Build parameters.
    
    Args:
        input_image: Input image.
        output_image: Output skeleton image.
        skeleton_params: Skeletonization parameters: <skel_thresh>\
            <distancemap> <search_rule_mask> <4Ddata> <projected_4Ddata>.
        alt_4d: Alternative 4D data (e.g., L1).
        alt_skeleton: Alternative skeleton.
        debug_flag: Switch on debugging image outputs.
        debug2_flag: De-project skelpoints points on skeleton back to all_FA\
            space.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tbss_skeleton",
        "input_image": input_image,
        "debug_flag": debug_flag,
    }
    if output_image is not None:
        params["output_image"] = output_image
    if skeleton_params is not None:
        params["skeleton_params"] = skeleton_params
    if alt_4d is not None:
        params["alt_4d"] = alt_4d
    if alt_skeleton is not None:
        params["alt_skeleton"] = alt_skeleton
    if debug2_flag is not None:
        params["debug2_flag"] = debug2_flag
    return params


def tbss_skeleton_cargs(
    params: TbssSkeletonParameters,
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
    cargs.append("tbss_skeleton")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_image"))
    ])
    if params.get("output_image") is not None:
        cargs.extend([
            "-o",
            params.get("output_image")
        ])
    if params.get("skeleton_params") is not None:
        cargs.extend([
            "-p",
            *params.get("skeleton_params")
        ])
    if params.get("alt_4d") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("alt_4d"))
        ])
    if params.get("alt_skeleton") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("alt_skeleton"))
        ])
    if params.get("debug_flag"):
        cargs.append("-d")
    if params.get("debug2_flag") is not None:
        cargs.extend([
            "-D",
            execution.input_file(params.get("debug2_flag"))
        ])
    return cargs


def tbss_skeleton_outputs(
    params: TbssSkeletonParameters,
    execution: Execution,
) -> TbssSkeletonOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TbssSkeletonOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(params.get("output_image")) if (params.get("output_image") is not None) else None,
        projected_4d_file=execution.output_file("[PROJECTED_4D]"),
        alt_4d_file=execution.output_file(pathlib.Path(params.get("alt_4d")).name) if (params.get("alt_4d") is not None) else None,
        alt_skeleton_file=execution.output_file(pathlib.Path(params.get("alt_skeleton")).name) if (params.get("alt_skeleton") is not None) else None,
        debug2_image_outputs=execution.output_file(pathlib.Path(params.get("debug2_flag")).name) if (params.get("debug2_flag") is not None) else None,
    )
    return ret


def tbss_skeleton_execute(
    params: TbssSkeletonParameters,
    execution: Execution,
) -> TbssSkeletonOutputs:
    """
    A tool for defining a 'skeleton' of white matter tracts in the brain to help
    compare them across subjects.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TbssSkeletonOutputs`).
    """
    params = execution.params(params)
    cargs = tbss_skeleton_cargs(params, execution)
    ret = tbss_skeleton_outputs(params, execution)
    execution.run(cargs)
    return ret


def tbss_skeleton(
    input_image: InputPathType,
    output_image: str | None = None,
    skeleton_params: list[str] | None = None,
    alt_4d: InputPathType | None = None,
    alt_skeleton: InputPathType | None = None,
    debug_flag: bool = False,
    debug2_flag: InputPathType | None = None,
    runner: Runner | None = None,
) -> TbssSkeletonOutputs:
    """
    A tool for defining a 'skeleton' of white matter tracts in the brain to help
    compare them across subjects.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image.
        output_image: Output skeleton image.
        skeleton_params: Skeletonization parameters: <skel_thresh>\
            <distancemap> <search_rule_mask> <4Ddata> <projected_4Ddata>.
        alt_4d: Alternative 4D data (e.g., L1).
        alt_skeleton: Alternative skeleton.
        debug_flag: Switch on debugging image outputs.
        debug2_flag: De-project skelpoints points on skeleton back to all_FA\
            space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TbssSkeletonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_SKELETON_METADATA)
    params = tbss_skeleton_params(input_image=input_image, output_image=output_image, skeleton_params=skeleton_params, alt_4d=alt_4d, alt_skeleton=alt_skeleton, debug_flag=debug_flag, debug2_flag=debug2_flag)
    return tbss_skeleton_execute(params, execution)


__all__ = [
    "TBSS_SKELETON_METADATA",
    "TbssSkeletonOutputs",
    "TbssSkeletonParameters",
    "tbss_skeleton",
    "tbss_skeleton_params",
]
