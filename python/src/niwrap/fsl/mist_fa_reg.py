# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MIST_FA_REG_METADATA = Metadata(
    id="45a9d3529b9890b437032ed4b1edac4f90d4e0ac.boutiques",
    name="mist_FA_reg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MistFaRegParameters = typing.TypedDict('MistFaRegParameters', {
    "__STYX_TYPE__": typing.Literal["mist_FA_reg"],
    "fa_volume": InputPathType,
    "s0_volume": InputPathType,
    "reference_t1_volume": InputPathType,
    "output_filename": str,
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
        "mist_FA_reg": mist_fa_reg_cargs,
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
        "mist_FA_reg": mist_fa_reg_outputs,
    }
    return vt.get(t)


class MistFaRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mist_fa_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file for the registered volume"""


def mist_fa_reg_params(
    fa_volume: InputPathType,
    s0_volume: InputPathType,
    reference_t1_volume: InputPathType,
    output_filename: str,
) -> MistFaRegParameters:
    """
    Build parameters.
    
    Args:
        fa_volume: The FA volume to be registered.
        s0_volume: The S0 volume corresponding to the FA volume.
        reference_t1_volume: The reference T1 volume to register against.
        output_filename: The output filename for the registered volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mist_FA_reg",
        "fa_volume": fa_volume,
        "s0_volume": s0_volume,
        "reference_t1_volume": reference_t1_volume,
        "output_filename": output_filename,
    }
    return params


def mist_fa_reg_cargs(
    params: MistFaRegParameters,
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
    cargs.append("mist_FA_reg")
    cargs.append(execution.input_file(params.get("fa_volume")))
    cargs.append(execution.input_file(params.get("s0_volume")))
    cargs.append(execution.input_file(params.get("reference_t1_volume")))
    cargs.append(params.get("output_filename"))
    return cargs


def mist_fa_reg_outputs(
    params: MistFaRegParameters,
    execution: Execution,
) -> MistFaRegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MistFaRegOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_filename")),
    )
    return ret


def mist_fa_reg_execute(
    params: MistFaRegParameters,
    execution: Execution,
) -> MistFaRegOutputs:
    """
    Tool for registering FA volumes to a reference T1 volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MistFaRegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mist_fa_reg_cargs(params, execution)
    ret = mist_fa_reg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mist_fa_reg(
    fa_volume: InputPathType,
    s0_volume: InputPathType,
    reference_t1_volume: InputPathType,
    output_filename: str,
    runner: Runner | None = None,
) -> MistFaRegOutputs:
    """
    Tool for registering FA volumes to a reference T1 volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        fa_volume: The FA volume to be registered.
        s0_volume: The S0 volume corresponding to the FA volume.
        reference_t1_volume: The reference T1 volume to register against.
        output_filename: The output filename for the registered volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MistFaRegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MIST_FA_REG_METADATA)
    params = mist_fa_reg_params(fa_volume=fa_volume, s0_volume=s0_volume, reference_t1_volume=reference_t1_volume, output_filename=output_filename)
    return mist_fa_reg_execute(params, execution)


__all__ = [
    "MIST_FA_REG_METADATA",
    "MistFaRegOutputs",
    "mist_fa_reg",
    "mist_fa_reg_params",
]
