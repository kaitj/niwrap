# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA = Metadata(
    id="97f1dd5239568c20aee38b5af5601267807ff55f.boutiques",
    name="cifti-create-parcellated-from-template",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
CiftiCreateParcellatedFromTemplateCiftiParameters = typing.TypedDict('CiftiCreateParcellatedFromTemplateCiftiParameters', {
    "__STYX_TYPE__": typing.Literal["cifti"],
    "cifti_in": InputPathType,
})
CiftiCreateParcellatedFromTemplateParameters = typing.TypedDict('CiftiCreateParcellatedFromTemplateParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-create-parcellated-from-template"],
    "cifti_template": InputPathType,
    "modify_direction": str,
    "cifti_out": str,
    "opt_fill_value_value": typing.NotRequired[float | None],
    "cifti": typing.NotRequired[list[CiftiCreateParcellatedFromTemplateCiftiParameters] | None],
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
        "cifti-create-parcellated-from-template": cifti_create_parcellated_from_template_cargs,
        "cifti": cifti_create_parcellated_from_template_cifti_cargs,
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
        "cifti-create-parcellated-from-template": cifti_create_parcellated_from_template_outputs,
    }
    return vt.get(t)


def cifti_create_parcellated_from_template_cifti_params(
    cifti_in: InputPathType,
) -> CiftiCreateParcellatedFromTemplateCiftiParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input parcellated cifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti",
        "cifti_in": cifti_in,
    }
    return params


def cifti_create_parcellated_from_template_cifti_cargs(
    params: CiftiCreateParcellatedFromTemplateCiftiParameters,
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
    cargs.append("-cifti")
    cargs.append(execution.input_file(params.get("cifti_in")))
    return cargs


class CiftiCreateParcellatedFromTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_parcellated_from_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_parcellated_from_template_params(
    cifti_template: InputPathType,
    modify_direction: str,
    cifti_out: str,
    opt_fill_value_value: float | None = None,
    cifti: list[CiftiCreateParcellatedFromTemplateCiftiParameters] | None = None,
) -> CiftiCreateParcellatedFromTemplateParameters:
    """
    Build parameters.
    
    Args:
        cifti_template: a cifti file with the template parcel mapping along\
            column.
        modify_direction: which dimension of the output file should match the\
            template (integer, 'ROW', or 'COLUMN').
        cifti_out: the output cifti file.
        opt_fill_value_value: specify value to be used in parcels that don't\
            match: value to use (default 0).
        cifti: specify an input cifti file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-create-parcellated-from-template",
        "cifti_template": cifti_template,
        "modify_direction": modify_direction,
        "cifti_out": cifti_out,
    }
    if opt_fill_value_value is not None:
        params["opt_fill_value_value"] = opt_fill_value_value
    if cifti is not None:
        params["cifti"] = cifti
    return params


def cifti_create_parcellated_from_template_cargs(
    params: CiftiCreateParcellatedFromTemplateParameters,
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
    cargs.append("wb_command")
    cargs.append("-cifti-create-parcellated-from-template")
    cargs.append(execution.input_file(params.get("cifti_template")))
    cargs.append(params.get("modify_direction"))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_fill_value_value") is not None:
        cargs.extend([
            "-fill-value",
            str(params.get("opt_fill_value_value"))
        ])
    if params.get("cifti") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("cifti")] for a in c])
    return cargs


def cifti_create_parcellated_from_template_outputs(
    params: CiftiCreateParcellatedFromTemplateParameters,
    execution: Execution,
) -> CiftiCreateParcellatedFromTemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiCreateParcellatedFromTemplateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_create_parcellated_from_template_execute(
    params: CiftiCreateParcellatedFromTemplateParameters,
    execution: Execution,
) -> CiftiCreateParcellatedFromTemplateOutputs:
    """
    Match parcels to template by name.
    
    For each parcel name in the template mapping, find that name in an input
    cifti file and use its data in the output file. All input cifti files must
    have a parcels mapping along <modify-direction> and matching mappings along
    other dimensions. The direction can be either an integer starting from 1, or
    the strings 'ROW' or 'COLUMN'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateParcellatedFromTemplateOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cifti_create_parcellated_from_template_cargs(params, execution)
    ret = cifti_create_parcellated_from_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_create_parcellated_from_template(
    cifti_template: InputPathType,
    modify_direction: str,
    cifti_out: str,
    opt_fill_value_value: float | None = None,
    cifti: list[CiftiCreateParcellatedFromTemplateCiftiParameters] | None = None,
    runner: Runner | None = None,
) -> CiftiCreateParcellatedFromTemplateOutputs:
    """
    Match parcels to template by name.
    
    For each parcel name in the template mapping, find that name in an input
    cifti file and use its data in the output file. All input cifti files must
    have a parcels mapping along <modify-direction> and matching mappings along
    other dimensions. The direction can be either an integer starting from 1, or
    the strings 'ROW' or 'COLUMN'.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_template: a cifti file with the template parcel mapping along\
            column.
        modify_direction: which dimension of the output file should match the\
            template (integer, 'ROW', or 'COLUMN').
        cifti_out: the output cifti file.
        opt_fill_value_value: specify value to be used in parcels that don't\
            match: value to use (default 0).
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateParcellatedFromTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA)
    params = cifti_create_parcellated_from_template_params(cifti_template=cifti_template, modify_direction=modify_direction, cifti_out=cifti_out, opt_fill_value_value=opt_fill_value_value, cifti=cifti)
    return cifti_create_parcellated_from_template_execute(params, execution)


__all__ = [
    "CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA",
    "CiftiCreateParcellatedFromTemplateOutputs",
    "cifti_create_parcellated_from_template",
    "cifti_create_parcellated_from_template_cifti_params",
    "cifti_create_parcellated_from_template_params",
]
