# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_GEN_3_D_METADATA = Metadata(
    id="fedbab806e12207f35c280ae3cff6fb5299d9f99.boutiques",
    name="fsl_gen_3D",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslGen3DParameters = typing.TypedDict('FslGen3DParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_gen_3D"],
    "infile": InputPathType,
    "outfile": InputPathType,
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
        "fsl_gen_3D": fsl_gen_3_d_cargs,
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
        "fsl_gen_3D": fsl_gen_3_d_outputs,
    }.get(t)


class FslGen3DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_gen_3_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_snapshot: OutputPathType
    """Generated 3D snapshot of the structural image"""


def fsl_gen_3_d_params(
    infile: InputPathType,
    outfile: InputPathType,
) -> FslGen3DParameters:
    """
    Build parameters.
    
    Args:
        infile: Input structural image (e.g. input.nii.gz).
        outfile: Output 3D snapshot image (e.g. output.png).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_gen_3D",
        "infile": infile,
        "outfile": outfile,
    }
    return params


def fsl_gen_3_d_cargs(
    params: FslGen3DParameters,
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
    cargs.append("fsl_gen_3D")
    cargs.append(execution.input_file(params.get("infile")))
    cargs.append(execution.input_file(params.get("outfile")))
    return cargs


def fsl_gen_3_d_outputs(
    params: FslGen3DParameters,
    execution: Execution,
) -> FslGen3DOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslGen3DOutputs(
        root=execution.output_file("."),
        output_snapshot=execution.output_file(pathlib.Path(params.get("outfile")).name),
    )
    return ret


def fsl_gen_3_d_execute(
    params: FslGen3DParameters,
    execution: Execution,
) -> FslGen3DOutputs:
    """
    Tool to generate a 3D snapshot of a structural image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslGen3DOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_gen_3_d_cargs(params, execution)
    ret = fsl_gen_3_d_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_gen_3_d(
    infile: InputPathType,
    outfile: InputPathType,
    runner: Runner | None = None,
) -> FslGen3DOutputs:
    """
    Tool to generate a 3D snapshot of a structural image.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        infile: Input structural image (e.g. input.nii.gz).
        outfile: Output 3D snapshot image (e.g. output.png).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslGen3DOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_GEN_3_D_METADATA)
    params = fsl_gen_3_d_params(infile=infile, outfile=outfile)
    return fsl_gen_3_d_execute(params, execution)


__all__ = [
    "FSL_GEN_3_D_METADATA",
    "FslGen3DOutputs",
    "FslGen3DParameters",
    "fsl_gen_3_d",
    "fsl_gen_3_d_params",
]
