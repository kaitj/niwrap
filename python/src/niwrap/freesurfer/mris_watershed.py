# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_WATERSHED_METADATA = Metadata(
    id="9a2bd956b5f350b8c0603b62d7b760dba26dc82d.boutiques",
    name="mris_watershed",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisWatershedParameters = typing.TypedDict('MrisWatershedParameters', {
    "__STYX_TYPE__": typing.Literal["mris_watershed"],
    "input_surface": InputPathType,
    "input_gradient_field": InputPathType,
    "output_annotation": str,
    "max_clusters": typing.NotRequired[float | None],
    "mask_label": typing.NotRequired[str | None],
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
        "mris_watershed": mris_watershed_cargs,
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
        "mris_watershed": mris_watershed_outputs,
    }
    return vt.get(t)


class MrisWatershedOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_watershed(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_annotation_file: OutputPathType
    """The resulting annotation file from the watershed transform"""


def mris_watershed_params(
    input_surface: InputPathType,
    input_gradient_field: InputPathType,
    output_annotation: str,
    max_clusters: float | None = None,
    mask_label: str | None = None,
) -> MrisWatershedParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file.
        input_gradient_field: Input gradient field file.
        output_annotation: Output annotation file.
        max_clusters: Set the number of maximum clusters.
        mask_label: Read in and mask the input volume that is not in the\
            specified label.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_watershed",
        "input_surface": input_surface,
        "input_gradient_field": input_gradient_field,
        "output_annotation": output_annotation,
    }
    if max_clusters is not None:
        params["max_clusters"] = max_clusters
    if mask_label is not None:
        params["mask_label"] = mask_label
    return params


def mris_watershed_cargs(
    params: MrisWatershedParameters,
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
    cargs.append("mris_watershed")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("input_gradient_field")))
    cargs.append(params.get("output_annotation"))
    if params.get("max_clusters") is not None:
        cargs.extend([
            "-M",
            str(params.get("max_clusters"))
        ])
    if params.get("mask_label") is not None:
        cargs.extend([
            "-mask_label",
            params.get("mask_label")
        ])
    return cargs


def mris_watershed_outputs(
    params: MrisWatershedParameters,
    execution: Execution,
) -> MrisWatershedOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisWatershedOutputs(
        root=execution.output_file("."),
        output_annotation_file=execution.output_file(params.get("output_annotation")),
    )
    return ret


def mris_watershed_execute(
    params: MrisWatershedParameters,
    execution: Execution,
) -> MrisWatershedOutputs:
    """
    This program computes the watershed transform on the surface of an intensity
    gradient and writes the resulting measurement into a .annot file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisWatershedOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_watershed_cargs(params, execution)
    ret = mris_watershed_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_watershed(
    input_surface: InputPathType,
    input_gradient_field: InputPathType,
    output_annotation: str,
    max_clusters: float | None = None,
    mask_label: str | None = None,
    runner: Runner | None = None,
) -> MrisWatershedOutputs:
    """
    This program computes the watershed transform on the surface of an intensity
    gradient and writes the resulting measurement into a .annot file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file.
        input_gradient_field: Input gradient field file.
        output_annotation: Output annotation file.
        max_clusters: Set the number of maximum clusters.
        mask_label: Read in and mask the input volume that is not in the\
            specified label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisWatershedOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_WATERSHED_METADATA)
    params = mris_watershed_params(input_surface=input_surface, input_gradient_field=input_gradient_field, output_annotation=output_annotation, max_clusters=max_clusters, mask_label=mask_label)
    return mris_watershed_execute(params, execution)


__all__ = [
    "MRIS_WATERSHED_METADATA",
    "MrisWatershedOutputs",
    "mris_watershed",
    "mris_watershed_params",
]
