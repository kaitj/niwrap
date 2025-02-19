# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_SYNTHESIZE_METADATA = Metadata(
    id="f7b287047be218e070a0e814059c1a76d0ae4655.boutiques",
    name="mri_synthesize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriSynthesizeParameters = typing.TypedDict('MriSynthesizeParameters', {
    "__STYX_TYPE__": typing.Literal["mri_synthesize"],
    "tr": float,
    "alpha": float,
    "te": float,
    "t1_volume": InputPathType,
    "pd_volume": InputPathType,
    "output_volume": str,
    "fixed_weight": bool,
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
        "mri_synthesize": mri_synthesize_cargs,
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
        "mri_synthesize": mri_synthesize_outputs,
    }.get(t)


class MriSynthesizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_synthesize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    synthesized_output: OutputPathType
    """The synthesized FLASH acquisition output volume."""


def mri_synthesize_params(
    tr: float,
    alpha: float,
    te: float,
    t1_volume: InputPathType,
    pd_volume: InputPathType,
    output_volume: str,
    fixed_weight: bool = False,
) -> MriSynthesizeParameters:
    """
    Build parameters.
    
    Args:
        tr: Repetition time (TR) for the synthesis.
        alpha: Flip angle (alpha) in degrees.
        te: Echo time (TE) for the synthesis.
        t1_volume: Path to the T1 volume.
        pd_volume: Path to the PD volume.
        output_volume: Path for the output volume.
        fixed_weight: Use a fixed weighting to generate an output volume with\
            optimal gray/white contrast.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_synthesize",
        "tr": tr,
        "alpha": alpha,
        "te": te,
        "t1_volume": t1_volume,
        "pd_volume": pd_volume,
        "output_volume": output_volume,
        "fixed_weight": fixed_weight,
    }
    return params


def mri_synthesize_cargs(
    params: MriSynthesizeParameters,
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
    cargs.append("mri_synthesize")
    cargs.append(str(params.get("tr")))
    cargs.append(str(params.get("alpha")))
    cargs.append(str(params.get("te")))
    cargs.append(execution.input_file(params.get("t1_volume")))
    cargs.append(execution.input_file(params.get("pd_volume")))
    cargs.append(params.get("output_volume"))
    if params.get("fixed_weight"):
        cargs.append("-w")
    return cargs


def mri_synthesize_outputs(
    params: MriSynthesizeParameters,
    execution: Execution,
) -> MriSynthesizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriSynthesizeOutputs(
        root=execution.output_file("."),
        synthesized_output=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_synthesize_execute(
    params: MriSynthesizeParameters,
    execution: Execution,
) -> MriSynthesizeOutputs:
    """
    This program synthesizes a FLASH acquisition based on previously computed T1/PD
    maps.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriSynthesizeOutputs`).
    """
    params = execution.params(params)
    cargs = mri_synthesize_cargs(params, execution)
    ret = mri_synthesize_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_synthesize(
    tr: float,
    alpha: float,
    te: float,
    t1_volume: InputPathType,
    pd_volume: InputPathType,
    output_volume: str,
    fixed_weight: bool = False,
    runner: Runner | None = None,
) -> MriSynthesizeOutputs:
    """
    This program synthesizes a FLASH acquisition based on previously computed T1/PD
    maps.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        tr: Repetition time (TR) for the synthesis.
        alpha: Flip angle (alpha) in degrees.
        te: Echo time (TE) for the synthesis.
        t1_volume: Path to the T1 volume.
        pd_volume: Path to the PD volume.
        output_volume: Path for the output volume.
        fixed_weight: Use a fixed weighting to generate an output volume with\
            optimal gray/white contrast.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSynthesizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SYNTHESIZE_METADATA)
    params = mri_synthesize_params(tr=tr, alpha=alpha, te=te, t1_volume=t1_volume, pd_volume=pd_volume, output_volume=output_volume, fixed_weight=fixed_weight)
    return mri_synthesize_execute(params, execution)


__all__ = [
    "MRI_SYNTHESIZE_METADATA",
    "MriSynthesizeOutputs",
    "MriSynthesizeParameters",
    "mri_synthesize",
    "mri_synthesize_params",
]
