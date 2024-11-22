# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_DESPIKE_METADATA = Metadata(
    id="8f18218a5319eef4d610e78223fa66e963614328.boutiques",
    name="3dDespike",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dDespikeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_despike(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output file."""


def v_3d_despike(
    in_file: InputPathType,
    runner: Runner | None = None,
) -> V3dDespikeOutputs:
    """
    Removes 'spikes' from the 3D+time input dataset and writes a new dataset with
    the spike values replaced by something more pleasing to the eye.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_file: Input file to 3ddespike.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDespikeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DESPIKE_METADATA)
    cargs = []
    cargs.append("3dDespike")
    cargs.append(execution.input_file(in_file))
    ret = V3dDespikeOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(in_file).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDespikeOutputs",
    "V_3D_DESPIKE_METADATA",
    "v_3d_despike",
]
