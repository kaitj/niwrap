# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_MATRIX4_TO_MATRIX2_METADATA = Metadata(
    id="48a77936cf53d052fce7b98678ac0929264dbd4c.boutiques",
    name="convert-matrix4-to-matrix2",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
ConvertMatrix4ToMatrix2IndividualFibersParameters = typing.TypedDict('ConvertMatrix4ToMatrix2IndividualFibersParameters', {
    "__STYX_TYPE__": typing.Literal["individual_fibers"],
    "fiber_1": str,
    "fiber_2": str,
    "fiber_3": str,
})
ConvertMatrix4ToMatrix2Parameters = typing.TypedDict('ConvertMatrix4ToMatrix2Parameters', {
    "__STYX_TYPE__": typing.Literal["convert-matrix4-to-matrix2"],
    "matrix4_wbsparse": str,
    "counts_out": str,
    "opt_distances_distance_out": typing.NotRequired[str | None],
    "individual_fibers": typing.NotRequired[ConvertMatrix4ToMatrix2IndividualFibersParameters | None],
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
        "convert-matrix4-to-matrix2": convert_matrix4_to_matrix2_cargs,
        "individual_fibers": convert_matrix4_to_matrix2_individual_fibers_cargs,
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
        "convert-matrix4-to-matrix2": convert_matrix4_to_matrix2_outputs,
        "individual_fibers": convert_matrix4_to_matrix2_individual_fibers_outputs,
    }
    return vt.get(t)


class ConvertMatrix4ToMatrix2IndividualFibersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ConvertMatrix4ToMatrix2IndividualFibersParameters | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fiber_1: OutputPathType
    """output file for first fiber"""
    fiber_2: OutputPathType
    """output file for second fiber"""
    fiber_3: OutputPathType
    """output file for third fiber"""


def convert_matrix4_to_matrix2_individual_fibers_params(
    fiber_1: str,
    fiber_2: str,
    fiber_3: str,
) -> ConvertMatrix4ToMatrix2IndividualFibersParameters:
    """
    Build parameters.
    
    Args:
        fiber_1: output file for first fiber.
        fiber_2: output file for second fiber.
        fiber_3: output file for third fiber.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "individual_fibers",
        "fiber_1": fiber_1,
        "fiber_2": fiber_2,
        "fiber_3": fiber_3,
    }
    return params


def convert_matrix4_to_matrix2_individual_fibers_cargs(
    params: ConvertMatrix4ToMatrix2IndividualFibersParameters,
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
    cargs.append("-individual-fibers")
    cargs.append(params.get("fiber_1"))
    cargs.append(params.get("fiber_2"))
    cargs.append(params.get("fiber_3"))
    return cargs


def convert_matrix4_to_matrix2_individual_fibers_outputs(
    params: ConvertMatrix4ToMatrix2IndividualFibersParameters,
    execution: Execution,
) -> ConvertMatrix4ToMatrix2IndividualFibersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertMatrix4ToMatrix2IndividualFibersOutputs(
        root=execution.output_file("."),
        fiber_1=execution.output_file(params.get("fiber_1")),
        fiber_2=execution.output_file(params.get("fiber_2")),
        fiber_3=execution.output_file(params.get("fiber_3")),
    )
    return ret


class ConvertMatrix4ToMatrix2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_matrix4_to_matrix2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    counts_out: OutputPathType
    """the total fiber counts, as a cifti file"""
    opt_distances_distance_out: OutputPathType | None
    """output average trajectory distance: the distances, as a cifti file"""
    individual_fibers: ConvertMatrix4ToMatrix2IndividualFibersOutputs | None
    """Outputs from `convert_matrix4_to_matrix2_individual_fibers_outputs`."""


def convert_matrix4_to_matrix2_params(
    matrix4_wbsparse: str,
    counts_out: str,
    opt_distances_distance_out: str | None = None,
    individual_fibers: ConvertMatrix4ToMatrix2IndividualFibersParameters | None = None,
) -> ConvertMatrix4ToMatrix2Parameters:
    """
    Build parameters.
    
    Args:
        matrix4_wbsparse: a wbsparse matrix4 file.
        counts_out: the total fiber counts, as a cifti file.
        opt_distances_distance_out: output average trajectory distance: the\
            distances, as a cifti file.
        individual_fibers: output files for each fiber direction.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "convert-matrix4-to-matrix2",
        "matrix4_wbsparse": matrix4_wbsparse,
        "counts_out": counts_out,
    }
    if opt_distances_distance_out is not None:
        params["opt_distances_distance_out"] = opt_distances_distance_out
    if individual_fibers is not None:
        params["individual_fibers"] = individual_fibers
    return params


def convert_matrix4_to_matrix2_cargs(
    params: ConvertMatrix4ToMatrix2Parameters,
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
    cargs.append("-convert-matrix4-to-matrix2")
    cargs.append(params.get("matrix4_wbsparse"))
    cargs.append(params.get("counts_out"))
    if params.get("opt_distances_distance_out") is not None:
        cargs.extend([
            "-distances",
            params.get("opt_distances_distance_out")
        ])
    if params.get("individual_fibers") is not None:
        cargs.extend(dyn_cargs(params.get("individual_fibers")["__STYXTYPE__"])(params.get("individual_fibers"), execution))
    return cargs


def convert_matrix4_to_matrix2_outputs(
    params: ConvertMatrix4ToMatrix2Parameters,
    execution: Execution,
) -> ConvertMatrix4ToMatrix2Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertMatrix4ToMatrix2Outputs(
        root=execution.output_file("."),
        counts_out=execution.output_file(params.get("counts_out")),
        opt_distances_distance_out=execution.output_file(params.get("opt_distances_distance_out")) if (params.get("opt_distances_distance_out") is not None) else None,
        individual_fibers=dyn_outputs(individual_fibers["__STYXTYPE__"])(individual_fibers, execution) if individual_fibers else None,
    )
    return ret


def convert_matrix4_to_matrix2_execute(
    params: ConvertMatrix4ToMatrix2Parameters,
    execution: Execution,
) -> ConvertMatrix4ToMatrix2Outputs:
    """
    Generates a matrix2 cifti from matrix4 wbsparse.
    
    This command makes a cifti file from the fiber counts in a matrix4 wbsparse
    file, and optionally a second cifti file from the distances. Note that while
    the total count is stored exactly, the per-fiber counts are stored as
    approximate fractions, so the output of -individual-fibers will contain
    nonintegers.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertMatrix4ToMatrix2Outputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = convert_matrix4_to_matrix2_cargs(params, execution)
    ret = convert_matrix4_to_matrix2_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_matrix4_to_matrix2(
    matrix4_wbsparse: str,
    counts_out: str,
    opt_distances_distance_out: str | None = None,
    individual_fibers: ConvertMatrix4ToMatrix2IndividualFibersParameters | None = None,
    runner: Runner | None = None,
) -> ConvertMatrix4ToMatrix2Outputs:
    """
    Generates a matrix2 cifti from matrix4 wbsparse.
    
    This command makes a cifti file from the fiber counts in a matrix4 wbsparse
    file, and optionally a second cifti file from the distances. Note that while
    the total count is stored exactly, the per-fiber counts are stored as
    approximate fractions, so the output of -individual-fibers will contain
    nonintegers.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        matrix4_wbsparse: a wbsparse matrix4 file.
        counts_out: the total fiber counts, as a cifti file.
        opt_distances_distance_out: output average trajectory distance: the\
            distances, as a cifti file.
        individual_fibers: output files for each fiber direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertMatrix4ToMatrix2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_MATRIX4_TO_MATRIX2_METADATA)
    params = convert_matrix4_to_matrix2_params(matrix4_wbsparse=matrix4_wbsparse, counts_out=counts_out, opt_distances_distance_out=opt_distances_distance_out, individual_fibers=individual_fibers)
    return convert_matrix4_to_matrix2_execute(params, execution)


__all__ = [
    "CONVERT_MATRIX4_TO_MATRIX2_METADATA",
    "ConvertMatrix4ToMatrix2IndividualFibersOutputs",
    "ConvertMatrix4ToMatrix2Outputs",
    "convert_matrix4_to_matrix2",
    "convert_matrix4_to_matrix2_individual_fibers_params",
    "convert_matrix4_to_matrix2_params",
]
