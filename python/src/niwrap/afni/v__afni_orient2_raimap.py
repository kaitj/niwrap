# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_ORIENT2_RAIMAP_METADATA = Metadata(
    id="ade1258888a2ab4d7104b72e6f2921d74eaf281c.boutiques",
    name="@AfniOrient2RAImap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VAfniOrient2RaimapParameters = typing.TypedDict('VAfniOrient2RaimapParameters', {
    "__STYX_TYPE__": typing.Literal["@AfniOrient2RAImap"],
    "orientation_code": str,
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
        "@AfniOrient2RAImap": v__afni_orient2_raimap_cargs,
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
    vt = {}
    return vt.get(t)


def v__afni_orient2_raimap_params(
    orientation_code: str,
) -> VAfniOrient2RaimapParameters:
    """
    Build parameters.
    
    Args:
        orientation_code: Orientation code (e.g., RAI, LSP).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@AfniOrient2RAImap",
        "orientation_code": orientation_code,
    }
    return params


def v__afni_orient2_raimap_cargs(
    params: VAfniOrient2RaimapParameters,
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
    cargs.append("@AfniOrient2RAImap")
    cargs.append(params.get("orientation_code"))
    return cargs


def v__afni_orient2_raimap_outputs(
    params: VAfniOrient2RaimapParameters,
    execution: Execution,
) -> VAfniOrient2RaimapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniOrient2RaimapOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__afni_orient2_raimap_execute(
    params: VAfniOrient2RaimapParameters,
    execution: Execution,
) -> VAfniOrient2RaimapOutputs:
    """
    Returns the index map for the RAI directions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniOrient2RaimapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__afni_orient2_raimap_cargs(params, execution)
    ret = v__afni_orient2_raimap_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_orient2_raimap(
    orientation_code: str,
    runner: Runner | None = None,
) -> VAfniOrient2RaimapOutputs:
    """
    Returns the index map for the RAI directions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        orientation_code: Orientation code (e.g., RAI, LSP).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniOrient2RaimapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_ORIENT2_RAIMAP_METADATA)
    params = v__afni_orient2_raimap_params(orientation_code=orientation_code)
    return v__afni_orient2_raimap_execute(params, execution)


__all__ = [
    "V__AFNI_ORIENT2_RAIMAP_METADATA",
    "v__afni_orient2_raimap",
    "v__afni_orient2_raimap_params",
]
