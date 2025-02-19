# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FSLMAT_TO_LTA_METADATA = Metadata(
    id="a584f1ce4737b11d3bc46a9cd0dac5a4276a9a35.boutiques",
    name="mri_fslmat_to_lta",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFslmatToLtaParameters = typing.TypedDict('MriFslmatToLtaParameters', {
    "__STYX_TYPE__": typing.Literal["mri_fslmat_to_lta"],
    "src_vol": InputPathType,
    "target_vol": InputPathType,
    "fslmat_file": InputPathType,
    "lta_file": str,
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
        "mri_fslmat_to_lta": mri_fslmat_to_lta_cargs,
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
        "mri_fslmat_to_lta": mri_fslmat_to_lta_outputs,
    }.get(t)


class MriFslmatToLtaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fslmat_to_lta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_lta_file: OutputPathType
    """LTA transformation file created from the given source, target volumes and
    FSL matrix file"""


def mri_fslmat_to_lta_params(
    src_vol: InputPathType,
    target_vol: InputPathType,
    fslmat_file: InputPathType,
    lta_file: str,
) -> MriFslmatToLtaParameters:
    """
    Build parameters.
    
    Args:
        src_vol: Source volume file.
        target_vol: Target volume file.
        fslmat_file: FSL transformation matrix file.
        lta_file: Output LTA transformation file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_fslmat_to_lta",
        "src_vol": src_vol,
        "target_vol": target_vol,
        "fslmat_file": fslmat_file,
        "lta_file": lta_file,
    }
    return params


def mri_fslmat_to_lta_cargs(
    params: MriFslmatToLtaParameters,
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
    cargs.append("mri_fslmat_to_lta")
    cargs.append(execution.input_file(params.get("src_vol")))
    cargs.append(execution.input_file(params.get("target_vol")))
    cargs.append(execution.input_file(params.get("fslmat_file")))
    cargs.append(params.get("lta_file"))
    return cargs


def mri_fslmat_to_lta_outputs(
    params: MriFslmatToLtaParameters,
    execution: Execution,
) -> MriFslmatToLtaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFslmatToLtaOutputs(
        root=execution.output_file("."),
        output_lta_file=execution.output_file(params.get("lta_file")),
    )
    return ret


def mri_fslmat_to_lta_execute(
    params: MriFslmatToLtaParameters,
    execution: Execution,
) -> MriFslmatToLtaOutputs:
    """
    This program creates the LTA transformation file using information from the src
    and target volumes and an FSL matrix file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFslmatToLtaOutputs`).
    """
    params = execution.params(params)
    cargs = mri_fslmat_to_lta_cargs(params, execution)
    ret = mri_fslmat_to_lta_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_fslmat_to_lta(
    src_vol: InputPathType,
    target_vol: InputPathType,
    fslmat_file: InputPathType,
    lta_file: str,
    runner: Runner | None = None,
) -> MriFslmatToLtaOutputs:
    """
    This program creates the LTA transformation file using information from the src
    and target volumes and an FSL matrix file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_vol: Source volume file.
        target_vol: Target volume file.
        fslmat_file: FSL transformation matrix file.
        lta_file: Output LTA transformation file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFslmatToLtaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FSLMAT_TO_LTA_METADATA)
    params = mri_fslmat_to_lta_params(src_vol=src_vol, target_vol=target_vol, fslmat_file=fslmat_file, lta_file=lta_file)
    return mri_fslmat_to_lta_execute(params, execution)


__all__ = [
    "MRI_FSLMAT_TO_LTA_METADATA",
    "MriFslmatToLtaOutputs",
    "MriFslmatToLtaParameters",
    "mri_fslmat_to_lta",
    "mri_fslmat_to_lta_params",
]
