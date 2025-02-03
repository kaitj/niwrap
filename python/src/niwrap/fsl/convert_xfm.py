# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_XFM_METADATA = Metadata(
    id="b079bee0db4c9532ed2211cab0dd571d7a59ebde.boutiques",
    name="convert_xfm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
ConvertXfmParameters = typing.TypedDict('ConvertXfmParameters', {
    "__STYX_TYPE__": typing.Literal["convert_xfm"],
    "out_file": typing.NotRequired[str | None],
    "invert_xfm": bool,
    "concat_xfm": typing.NotRequired[InputPathType | None],
    "fix_scale_skew": typing.NotRequired[InputPathType | None],
    "in_file": InputPathType,
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
        "convert_xfm": convert_xfm_cargs,
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
        "convert_xfm": convert_xfm_outputs,
    }
    return vt.get(t)


class ConvertXfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_xfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_trasnformation: OutputPathType | None
    """Output transformation matrix."""


def convert_xfm_params(
    in_file: InputPathType,
    out_file: str | None = None,
    invert_xfm: bool = False,
    concat_xfm: InputPathType | None = None,
    fix_scale_skew: InputPathType | None = None,
) -> ConvertXfmParameters:
    """
    Build parameters.
    
    Args:
        in_file: Input transformation matrix.
        out_file: Final transformation matrix.
        invert_xfm: Invert input transformation.
        concat_xfm: A File. Write joint transformation of two input matrices.
        fix_scale_skew: A File. Use secondary matrix to fix scale and skew.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convert_xfm",
        "invert_xfm": invert_xfm,
        "in_file": in_file,
    }
    if out_file is not None:
        params["out_file"] = out_file
    if concat_xfm is not None:
        params["concat_xfm"] = concat_xfm
    if fix_scale_skew is not None:
        params["fix_scale_skew"] = fix_scale_skew
    return params


def convert_xfm_cargs(
    params: ConvertXfmParameters,
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
    cargs.append("convert_xfm")
    if params.get("out_file") is not None:
        cargs.extend([
            "-omat",
            params.get("out_file")
        ])
    if params.get("invert_xfm"):
        cargs.append("-inverse")
    if params.get("concat_xfm") is not None:
        cargs.extend([
            "-concat",
            execution.input_file(params.get("concat_xfm"))
        ])
    if params.get("fix_scale_skew") is not None:
        cargs.extend([
            "-fixscaleskew",
            execution.input_file(params.get("fix_scale_skew"))
        ])
    cargs.append(execution.input_file(params.get("in_file")))
    return cargs


def convert_xfm_outputs(
    params: ConvertXfmParameters,
    execution: Execution,
) -> ConvertXfmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertXfmOutputs(
        root=execution.output_file("."),
        output_trasnformation=execution.output_file(params.get("out_file")) if (params.get("out_file") is not None) else None,
    )
    return ret


def convert_xfm_execute(
    params: ConvertXfmParameters,
    execution: Execution,
) -> ConvertXfmOutputs:
    """
    convert_xfm is a utility that is used to convert between different
    transformation file formats. It can read and write ascii 4x4 matrices. In
    addition, it can be used to concatenate two transforms (using -concat with the
    second transform) or to find the inverse transformation (using -inverse).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertXfmOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = convert_xfm_cargs(params, execution)
    ret = convert_xfm_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_xfm(
    in_file: InputPathType,
    out_file: str | None = None,
    invert_xfm: bool = False,
    concat_xfm: InputPathType | None = None,
    fix_scale_skew: InputPathType | None = None,
    runner: Runner | None = None,
) -> ConvertXfmOutputs:
    """
    convert_xfm is a utility that is used to convert between different
    transformation file formats. It can read and write ascii 4x4 matrices. In
    addition, it can be used to concatenate two transforms (using -concat with the
    second transform) or to find the inverse transformation (using -inverse).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input transformation matrix.
        out_file: Final transformation matrix.
        invert_xfm: Invert input transformation.
        concat_xfm: A File. Write joint transformation of two input matrices.
        fix_scale_skew: A File. Use secondary matrix to fix scale and skew.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertXfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_XFM_METADATA)
    params = convert_xfm_params(out_file=out_file, invert_xfm=invert_xfm, concat_xfm=concat_xfm, fix_scale_skew=fix_scale_skew, in_file=in_file)
    return convert_xfm_execute(params, execution)


__all__ = [
    "CONVERT_XFM_METADATA",
    "ConvertXfmOutputs",
    "convert_xfm",
    "convert_xfm_params",
]
