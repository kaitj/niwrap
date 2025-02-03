# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_NLFIM_METADATA = Metadata(
    id="b2553c2bf57346747079630757e1d16620ea8119.boutiques",
    name="3dNLfim",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dNlfimParameters = typing.TypedDict('V3dNlfimParameters', {
    "__STYX_TYPE__": typing.Literal["3dNLfim"],
    "input_file": InputPathType,
    "signal_model": str,
    "noise_model": str,
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
        "3dNLfim": v_3d_nlfim_cargs,
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
        "3dNLfim": v_3d_nlfim_outputs,
    }
    return vt.get(t)


class V3dNlfimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_nlfim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    freg_outfile: OutputPathType
    """F-test for significance of the regression"""
    frsqr_outfile: OutputPathType
    """R^2 calculation for regression"""
    fsmax_outfile: OutputPathType
    """Signed maximum signal estimate"""
    ftmax_outfile: OutputPathType
    """Time of signed maximum estimate"""
    fpsmax_outfile: OutputPathType
    """Maximum percentage change estimate"""
    farea_outfile: OutputPathType
    """Area between signal and baseline"""
    fparea_outfile: OutputPathType
    """Percentage area of signal estimate"""
    fscoef_outfile: OutputPathType
    """Signal parameter estimate"""
    fncoef_outfile: OutputPathType
    """Noise parameter estimate"""
    tscoef_outfile: OutputPathType
    """T-test for significance of signal parameter"""
    tncoef_outfile: OutputPathType
    """T-test for significance of noise parameter"""
    bucket_outfile: OutputPathType
    """AFNI 'bucket' dataset"""
    sfit_outfile: OutputPathType
    """Output 3d+time signal model fit"""
    snfit_outfile: OutputPathType
    """Output 3d+time signal+noise fit"""


def v_3d_nlfim_params(
    input_file: InputPathType,
    signal_model: str,
    noise_model: str,
) -> V3dNlfimParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename of 3d+time data file for input.
        signal_model: Name of the nonlinear signal model.
        noise_model: Name of the linear noise model.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dNLfim",
        "input_file": input_file,
        "signal_model": signal_model,
        "noise_model": noise_model,
    }
    return params


def v_3d_nlfim_cargs(
    params: V3dNlfimParameters,
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
    cargs.append("3dNLfim")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-signal",
        params.get("signal_model")
    ])
    cargs.extend([
        "-noise",
        params.get("noise_model")
    ])
    cargs.append("[ADDITIONAL_OPTIONS]")
    return cargs


def v_3d_nlfim_outputs(
    params: V3dNlfimParameters,
    execution: Execution,
) -> V3dNlfimOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dNlfimOutputs(
        root=execution.output_file("."),
        freg_outfile=execution.output_file("[FREG].fift"),
        frsqr_outfile=execution.output_file("[FRSQR].fift"),
        fsmax_outfile=execution.output_file("[FSMAX].fift"),
        ftmax_outfile=execution.output_file("[FTMAX].fift"),
        fpsmax_outfile=execution.output_file("[FPSMAX].fift"),
        farea_outfile=execution.output_file("[FAREA].fift"),
        fparea_outfile=execution.output_file("[FPAREA].fift"),
        fscoef_outfile=execution.output_file("[FSCOEF].fift"),
        fncoef_outfile=execution.output_file("[FNCOEF].fift"),
        tscoef_outfile=execution.output_file("[TSCOEF].fitt"),
        tncoef_outfile=execution.output_file("[TNCOEF].fitt"),
        bucket_outfile=execution.output_file("[BUCKET].bucket"),
        sfit_outfile=execution.output_file("[SFIT].sfit"),
        snfit_outfile=execution.output_file("[SNFIT].snfit"),
    )
    return ret


def v_3d_nlfim_execute(
    params: V3dNlfimParameters,
    execution: Execution,
) -> V3dNlfimOutputs:
    """
    Nonlinear regression for each voxel of the input AFNI 3d+time data set.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dNlfimOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_nlfim_cargs(params, execution)
    ret = v_3d_nlfim_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_nlfim(
    input_file: InputPathType,
    signal_model: str,
    noise_model: str,
    runner: Runner | None = None,
) -> V3dNlfimOutputs:
    """
    Nonlinear regression for each voxel of the input AFNI 3d+time data set.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Filename of 3d+time data file for input.
        signal_model: Name of the nonlinear signal model.
        noise_model: Name of the linear noise model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNlfimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NLFIM_METADATA)
    params = v_3d_nlfim_params(input_file=input_file, signal_model=signal_model, noise_model=noise_model)
    return v_3d_nlfim_execute(params, execution)


__all__ = [
    "V3dNlfimOutputs",
    "V_3D_NLFIM_METADATA",
    "v_3d_nlfim",
    "v_3d_nlfim_params",
]
