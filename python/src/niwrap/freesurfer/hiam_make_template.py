# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

HIAM_MAKE_TEMPLATE_METADATA = Metadata(
    id="8c48bbfd46c7f8da62fb53ac9c94dd28311f4d1a.boutiques",
    name="hiam_make_template",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
HiamMakeTemplateParameters = typing.TypedDict('HiamMakeTemplateParameters', {
    "__STYX_TYPE__": typing.Literal["hiam_make_template"],
    "hemi": str,
    "surface_name": str,
    "subjects": list[str],
    "output_name": str,
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
        "hiam_make_template": hiam_make_template_cargs,
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


class HiamMakeTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `hiam_make_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def hiam_make_template_params(
    hemi: str,
    surface_name: str,
    subjects: list[str],
    output_name: str,
) -> HiamMakeTemplateParameters:
    """
    Build parameters.
    
    Args:
        hemi: Hemisphere to be processed (e.g. lh or rh).
        surface_name: Name of the surface.
        subjects: List of subject identifiers.
        output_name: Name of the output template.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "hiam_make_template",
        "hemi": hemi,
        "surface_name": surface_name,
        "subjects": subjects,
        "output_name": output_name,
    }
    return params


def hiam_make_template_cargs(
    params: HiamMakeTemplateParameters,
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
    cargs.append("hiam_make_template")
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface_name"))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_name"))
    return cargs


def hiam_make_template_outputs(
    params: HiamMakeTemplateParameters,
    execution: Execution,
) -> HiamMakeTemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = HiamMakeTemplateOutputs(
        root=execution.output_file("."),
    )
    return ret


def hiam_make_template_execute(
    params: HiamMakeTemplateParameters,
    execution: Execution,
) -> HiamMakeTemplateOutputs:
    """
    This program adds a template into an average surface using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `HiamMakeTemplateOutputs`).
    """
    params = execution.params(params)
    cargs = hiam_make_template_cargs(params, execution)
    ret = hiam_make_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def hiam_make_template(
    hemi: str,
    surface_name: str,
    subjects: list[str],
    output_name: str,
    runner: Runner | None = None,
) -> HiamMakeTemplateOutputs:
    """
    This program adds a template into an average surface using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere to be processed (e.g. lh or rh).
        surface_name: Name of the surface.
        subjects: List of subject identifiers.
        output_name: Name of the output template.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HiamMakeTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HIAM_MAKE_TEMPLATE_METADATA)
    params = hiam_make_template_params(hemi=hemi, surface_name=surface_name, subjects=subjects, output_name=output_name)
    return hiam_make_template_execute(params, execution)


__all__ = [
    "HIAM_MAKE_TEMPLATE_METADATA",
    "HiamMakeTemplateOutputs",
    "HiamMakeTemplateParameters",
    "hiam_make_template",
    "hiam_make_template_params",
]
