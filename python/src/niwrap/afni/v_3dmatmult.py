# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DMATMULT_METADATA = Metadata(
    id="b0403f3583c32fcce165812afa6ff2fc1aa6d6df.boutiques",
    name="3dmatmult",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmatmultOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmatmult(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset from the matrix multiplication"""


def v_3dmatmult(
    input_a: InputPathType,
    input_b: InputPathType,
    prefix: str,
    datum: str | None = None,
    verb: float | None = None,
    runner: Runner | None = None,
) -> V3dmatmultOutputs:
    """
    Multiply AFNI datasets slice-by-slice as matrices.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmatmult.html
    
    Args:
        input_a: Specify first (matrix) dataset.
        input_b: Specify second (matrix) dataset.
        prefix: Specify output dataset prefix.
        datum: Specify output data type ('byte', 'short', 'float').
        verb: Specify verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmatmultOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMATMULT_METADATA)
    cargs = []
    cargs.append("3dmatmult")
    cargs.extend([
        "-inputA",
        execution.input_file(input_a)
    ])
    cargs.extend([
        "-inputB",
        execution.input_file(input_b)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if datum is not None:
        cargs.extend([
            "-datum",
            datum
        ])
    if verb is not None:
        cargs.extend([
            "-verb",
            str(verb)
        ])
    ret = V3dmatmultOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmatmultOutputs",
    "V_3DMATMULT_METADATA",
    "v_3dmatmult",
]
