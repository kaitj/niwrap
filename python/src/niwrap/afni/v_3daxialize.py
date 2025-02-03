# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DAXIALIZE_METADATA = Metadata(
    id="bcc8e30177064f95c8a4e5b95029e8dd46cb1692.boutiques",
    name="3daxialize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3daxializeParameters = typing.TypedDict('V3daxializeParameters', {
    "__STYX_TYPE__": typing.Literal["3daxialize"],
    "infile": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "verb": bool,
    "sagittal": bool,
    "coronal": bool,
    "axial": bool,
    "orient_code": typing.NotRequired[str | None],
    "frugal": bool,
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
        "3daxialize": v_3daxialize_cargs,
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
        "3daxialize": v_3daxialize_outputs,
    }
    return vt.get(t)


class V3daxializeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3daxialize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """Output dataset with axial slices orientation"""


def v_3daxialize_params(
    infile: InputPathType,
    prefix: str | None = None,
    verb: bool = False,
    sagittal: bool = False,
    coronal: bool = False,
    axial: bool = False,
    orient_code: str | None = None,
    frugal: bool = False,
) -> V3daxializeParameters:
    """
    Build parameters.
    
    Args:
        infile: Dataset to be axially oriented.
        prefix: Use specified prefix for the new dataset. Default is\
            'axialize'.
        verb: Print out a progress report.
        sagittal: Write dataset in sagittal slice order.
        coronal: Write dataset in coronal slice order.
        axial: Write dataset in axial slice order, the default orientation.
        orient_code: Orientation code for output. 3 letters: one from {R,L},\
            {A,P}, {I,S}.
        frugal: Write data as it is rotated, saving memory. Not available with\
            NIFTI datasets.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3daxialize",
        "infile": infile,
        "verb": verb,
        "sagittal": sagittal,
        "coronal": coronal,
        "axial": axial,
        "frugal": frugal,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if orient_code is not None:
        params["orient_code"] = orient_code
    return params


def v_3daxialize_cargs(
    params: V3daxializeParameters,
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
    cargs.append("3daxialize")
    cargs.append(execution.input_file(params.get("infile")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("sagittal"):
        cargs.append("-sagittal")
    if params.get("coronal"):
        cargs.append("-coronal")
    if params.get("axial"):
        cargs.append("-axial")
    if params.get("orient_code") is not None:
        cargs.extend([
            "-orient",
            params.get("orient_code")
        ])
    if params.get("frugal"):
        cargs.append("-frugal")
    return cargs


def v_3daxialize_outputs(
    params: V3daxializeParameters,
    execution: Execution,
) -> V3daxializeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3daxializeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("prefix") + "+orig") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3daxialize_execute(
    params: V3daxializeParameters,
    execution: Execution,
) -> V3daxializeOutputs:
    """
    Read and write dataset as new dataset with data brick oriented as axial slices.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3daxializeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3daxialize_cargs(params, execution)
    ret = v_3daxialize_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3daxialize(
    infile: InputPathType,
    prefix: str | None = None,
    verb: bool = False,
    sagittal: bool = False,
    coronal: bool = False,
    axial: bool = False,
    orient_code: str | None = None,
    frugal: bool = False,
    runner: Runner | None = None,
) -> V3daxializeOutputs:
    """
    Read and write dataset as new dataset with data brick oriented as axial slices.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Dataset to be axially oriented.
        prefix: Use specified prefix for the new dataset. Default is\
            'axialize'.
        verb: Print out a progress report.
        sagittal: Write dataset in sagittal slice order.
        coronal: Write dataset in coronal slice order.
        axial: Write dataset in axial slice order, the default orientation.
        orient_code: Orientation code for output. 3 letters: one from {R,L},\
            {A,P}, {I,S}.
        frugal: Write data as it is rotated, saving memory. Not available with\
            NIFTI datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3daxializeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DAXIALIZE_METADATA)
    params = v_3daxialize_params(infile=infile, prefix=prefix, verb=verb, sagittal=sagittal, coronal=coronal, axial=axial, orient_code=orient_code, frugal=frugal)
    return v_3daxialize_execute(params, execution)


__all__ = [
    "V3daxializeOutputs",
    "V_3DAXIALIZE_METADATA",
    "v_3daxialize",
    "v_3daxialize_params",
]
