# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__HELP_AFNI_METADATA = Metadata(
    id="87ebd1e4083856099825a6ef50fde5abb2dad615.boutiques",
    name="@help.AFNI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VHelpAfniParameters = typing.TypedDict('VHelpAfniParameters', {
    "__STYX_TYPE__": typing.Literal["@help.AFNI"],
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
        "@help.AFNI": v__help_afni_cargs,
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
    }.get(t)


class VHelpAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__help_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__help_afni_params(
) -> VHelpAfniParameters:
    """
    Build parameters.
    
    Args:
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@help.AFNI",
    }
    return params


def v__help_afni_cargs(
    params: VHelpAfniParameters,
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
    cargs.append("@help.AFNI")
    cargs.append("[OPTIONS]")
    return cargs


def v__help_afni_outputs(
    params: VHelpAfniParameters,
    execution: Execution,
) -> VHelpAfniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VHelpAfniOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__help_afni_execute(
    params: VHelpAfniParameters,
    execution: Execution,
) -> VHelpAfniOutputs:
    """
    A script to retrieve and search AFNI's help page for all programs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VHelpAfniOutputs`).
    """
    params = execution.params(params)
    cargs = v__help_afni_cargs(params, execution)
    ret = v__help_afni_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__help_afni(
    runner: Runner | None = None,
) -> VHelpAfniOutputs:
    """
    A script to retrieve and search AFNI's help page for all programs.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VHelpAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__HELP_AFNI_METADATA)
    params = v__help_afni_params()
    return v__help_afni_execute(params, execution)


__all__ = [
    "VHelpAfniOutputs",
    "VHelpAfniParameters",
    "V__HELP_AFNI_METADATA",
    "v__help_afni",
    "v__help_afni_params",
]
