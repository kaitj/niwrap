# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CA_TISSUE_PARMS_METADATA = Metadata(
    id="1d6429470b2b62de7212566259b4407543b03a79.boutiques",
    name="mri_ca_tissue_parms",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriCaTissueParmsParameters = typing.TypedDict('MriCaTissueParmsParameters', {
    "__STYX_TYPE__": typing.Literal["mri_ca_tissue_parms"],
    "subjects": list[str],
    "output_file": str,
    "spacing_flag": bool,
    "gradient_flag": bool,
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
        "mri_ca_tissue_parms": mri_ca_tissue_parms_cargs,
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
        "mri_ca_tissue_parms": mri_ca_tissue_parms_outputs,
    }.get(t)


class MriCaTissueParmsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_ca_tissue_parms(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """File containing the computed tissue parameters."""


def mri_ca_tissue_parms_params(
    subjects: list[str],
    output_file: str,
    spacing_flag: bool = False,
    gradient_flag: bool = False,
) -> MriCaTissueParmsParameters:
    """
    Build parameters.
    
    Args:
        subjects: List of subjects for processing.
        output_file: Output file for storing results.
        spacing_flag: Specify spacing of classifiers in canonical space.
        gradient_flag: Use intensity gradient as input to classifier.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_ca_tissue_parms",
        "subjects": subjects,
        "output_file": output_file,
        "spacing_flag": spacing_flag,
        "gradient_flag": gradient_flag,
    }
    return params


def mri_ca_tissue_parms_cargs(
    params: MriCaTissueParmsParameters,
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
    cargs.append("mri_ca_tissue_parms")
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_file"))
    if params.get("spacing_flag"):
        cargs.append("-spacing")
    if params.get("gradient_flag"):
        cargs.append("-gradient")
    return cargs


def mri_ca_tissue_parms_outputs(
    params: MriCaTissueParmsParameters,
    execution: Execution,
) -> MriCaTissueParmsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCaTissueParmsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def mri_ca_tissue_parms_execute(
    params: MriCaTissueParmsParameters,
    execution: Execution,
) -> MriCaTissueParmsOutputs:
    """
    Tool for computing tissue parameters in canonical space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCaTissueParmsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_ca_tissue_parms_cargs(params, execution)
    ret = mri_ca_tissue_parms_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_ca_tissue_parms(
    subjects: list[str],
    output_file: str,
    spacing_flag: bool = False,
    gradient_flag: bool = False,
    runner: Runner | None = None,
) -> MriCaTissueParmsOutputs:
    """
    Tool for computing tissue parameters in canonical space.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subjects for processing.
        output_file: Output file for storing results.
        spacing_flag: Specify spacing of classifiers in canonical space.
        gradient_flag: Use intensity gradient as input to classifier.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCaTissueParmsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CA_TISSUE_PARMS_METADATA)
    params = mri_ca_tissue_parms_params(subjects=subjects, output_file=output_file, spacing_flag=spacing_flag, gradient_flag=gradient_flag)
    return mri_ca_tissue_parms_execute(params, execution)


__all__ = [
    "MRI_CA_TISSUE_PARMS_METADATA",
    "MriCaTissueParmsOutputs",
    "MriCaTissueParmsParameters",
    "mri_ca_tissue_parms",
    "mri_ca_tissue_parms_params",
]
