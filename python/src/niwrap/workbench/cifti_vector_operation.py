# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_VECTOR_OPERATION_METADATA = Metadata(
    id="fbbf59a0a76d3a468e344bce994c87058094a9be.boutiques",
    name="cifti-vector-operation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class CiftiVectorOperationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_vector_operation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output file"""


def cifti_vector_operation(
    vectors_a: InputPathType,
    vectors_b: InputPathType,
    operation: str,
    cifti_out: str,
    opt_normalize_a: bool = False,
    opt_normalize_b: bool = False,
    opt_normalize_output: bool = False,
    opt_magnitude: bool = False,
    runner: Runner | None = None,
) -> CiftiVectorOperationOutputs:
    """
    Do a vector operation on cifti files.
    
    Does a vector operation on two cifti files (that must have a multiple of 3
    columns). Either of the inputs may have multiple vectors (more than 3
    columns), but not both (at least one must have exactly 3 columns). The
    -magnitude and -normalize-output options may not be specified together, or
    with an operation that returns a scalar (dot product). The <operation>
    parameter must be one of the following:
    
    DOT
    CROSS
    ADD
    SUBTRACT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        vectors_a: first vector input file.
        vectors_b: second vector input file.
        operation: what vector operation to do.
        cifti_out: the output file.
        opt_normalize_a: normalize vectors of first input.
        opt_normalize_b: normalize vectors of second input.
        opt_normalize_output: normalize output vectors (not valid for dot\
            product).
        opt_magnitude: output the magnitude of the result (not valid for dot\
            product).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiVectorOperationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_VECTOR_OPERATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-vector-operation")
    cargs.append(execution.input_file(vectors_a))
    cargs.append(execution.input_file(vectors_b))
    cargs.append(operation)
    cargs.append(cifti_out)
    if opt_normalize_a:
        cargs.append("-normalize-a")
    if opt_normalize_b:
        cargs.append("-normalize-b")
    if opt_normalize_output:
        cargs.append("-normalize-output")
    if opt_magnitude:
        cargs.append("-magnitude")
    ret = CiftiVectorOperationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_VECTOR_OPERATION_METADATA",
    "CiftiVectorOperationOutputs",
    "cifti_vector_operation",
]
