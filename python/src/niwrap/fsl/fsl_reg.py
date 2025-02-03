# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_REG_METADATA = Metadata(
    id="f171f8428dfe12c0d48e1add4d10229ca1a75e4f.boutiques",
    name="fsl_reg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslRegParameters = typing.TypedDict('FslRegParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_reg"],
    "input_file": InputPathType,
    "reference_file": InputPathType,
    "output_file": str,
    "estimate_only_flag": bool,
    "affine_only_flag": bool,
    "fnirt_fa_config_flag": bool,
    "flirt_options": typing.NotRequired[str | None],
    "fnirt_options": typing.NotRequired[str | None],
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
        "fsl_reg": fsl_reg_cargs,
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
        "fsl_reg": fsl_reg_outputs,
    }
    return vt.get(t)


class FslRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_file: OutputPathType
    """Output transformation file"""


def fsl_reg_params(
    input_file: InputPathType,
    reference_file: InputPathType,
    output_file: str,
    estimate_only_flag: bool = False,
    affine_only_flag: bool = False,
    fnirt_fa_config_flag: bool = False,
    flirt_options: str | None = None,
    fnirt_options: str | None = None,
) -> FslRegParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image file.
        reference_file: Reference image file.
        output_file: Output transformation file.
        estimate_only_flag: Estimate transformation but don't apply it.
        affine_only_flag: Affine-only registration.
        fnirt_fa_config_flag: Use FNIRT config file optimised for FA data.
        flirt_options: Options to be passed onto flirt (inside double-quotes).
        fnirt_options: Options to be passed onto fnirt (inside double-quotes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_reg",
        "input_file": input_file,
        "reference_file": reference_file,
        "output_file": output_file,
        "estimate_only_flag": estimate_only_flag,
        "affine_only_flag": affine_only_flag,
        "fnirt_fa_config_flag": fnirt_fa_config_flag,
    }
    if flirt_options is not None:
        params["flirt_options"] = flirt_options
    if fnirt_options is not None:
        params["fnirt_options"] = fnirt_options
    return params


def fsl_reg_cargs(
    params: FslRegParameters,
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
    cargs.append("fsl_reg")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(execution.input_file(params.get("reference_file")))
    cargs.append(params.get("output_file"))
    if params.get("estimate_only_flag"):
        cargs.append("-e")
    if params.get("affine_only_flag"):
        cargs.append("-a")
    if params.get("fnirt_fa_config_flag"):
        cargs.append("-FA")
    if params.get("flirt_options") is not None:
        cargs.extend([
            "-flirt",
            params.get("flirt_options")
        ])
    if params.get("fnirt_options") is not None:
        cargs.extend([
            "-fnirt",
            params.get("fnirt_options")
        ])
    return cargs


def fsl_reg_outputs(
    params: FslRegParameters,
    execution: Execution,
) -> FslRegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslRegOutputs(
        root=execution.output_file("."),
        output_transform_file=execution.output_file(params.get("output_file")),
    )
    return ret


def fsl_reg_execute(
    params: FslRegParameters,
    execution: Execution,
) -> FslRegOutputs:
    """
    Image registration using FSL tools.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslRegOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsl_reg_cargs(params, execution)
    ret = fsl_reg_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_reg(
    input_file: InputPathType,
    reference_file: InputPathType,
    output_file: str,
    estimate_only_flag: bool = False,
    affine_only_flag: bool = False,
    fnirt_fa_config_flag: bool = False,
    flirt_options: str | None = None,
    fnirt_options: str | None = None,
    runner: Runner | None = None,
) -> FslRegOutputs:
    """
    Image registration using FSL tools.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image file.
        reference_file: Reference image file.
        output_file: Output transformation file.
        estimate_only_flag: Estimate transformation but don't apply it.
        affine_only_flag: Affine-only registration.
        fnirt_fa_config_flag: Use FNIRT config file optimised for FA data.
        flirt_options: Options to be passed onto flirt (inside double-quotes).
        fnirt_options: Options to be passed onto fnirt (inside double-quotes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslRegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_REG_METADATA)
    params = fsl_reg_params(input_file=input_file, reference_file=reference_file, output_file=output_file, estimate_only_flag=estimate_only_flag, affine_only_flag=affine_only_flag, fnirt_fa_config_flag=fnirt_fa_config_flag, flirt_options=flirt_options, fnirt_options=fnirt_options)
    return fsl_reg_execute(params, execution)


__all__ = [
    "FSL_REG_METADATA",
    "FslRegOutputs",
    "fsl_reg",
    "fsl_reg_params",
]
