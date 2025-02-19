# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MEDIAN_FILTER_METADATA = Metadata(
    id="e4ff1f00010a20a209cf31d2f6355a6142d17c25.boutiques",
    name="3dMedianFilter",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dMedianFilterParameters = typing.TypedDict('V3dMedianFilterParameters', {
    "__STYX_TYPE__": typing.Literal["3dMedianFilter"],
    "irad": typing.NotRequired[float | None],
    "iter": typing.NotRequired[float | None],
    "verbose": bool,
    "prefix": typing.NotRequired[str | None],
    "automask": bool,
    "dataset": InputPathType,
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
        "3dMedianFilter": v_3d_median_filter_cargs,
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
        "3dMedianFilter": v_3d_median_filter_outputs,
    }.get(t)


class V3dMedianFilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_median_filter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brik: OutputPathType | None
    """Output dataset is stored in float format."""
    output_head: OutputPathType | None
    """Output dataset header file."""


def v_3d_median_filter_params(
    dataset: InputPathType,
    irad: float | None = None,
    iter_: float | None = None,
    verbose: bool = False,
    prefix: str | None = None,
    automask: bool = False,
) -> V3dMedianFilterParameters:
    """
    Build parameters.
    
    Args:
        dataset: Input dataset.
        irad: Radius in voxels of spherical regions.
        iter_: Iterate 'n' times [default=1].
        verbose: Be verbose during run.
        prefix: Use 'pp' for prefix of output dataset.
        automask: Create a mask (a la 3dAutomask).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMedianFilter",
        "verbose": verbose,
        "automask": automask,
        "dataset": dataset,
    }
    if irad is not None:
        params["irad"] = irad
    if iter_ is not None:
        params["iter"] = iter_
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v_3d_median_filter_cargs(
    params: V3dMedianFilterParameters,
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
    cargs.append("3dMedianFilter")
    if params.get("irad") is not None:
        cargs.extend([
            "-irad",
            str(params.get("irad"))
        ])
    if params.get("iter") is not None:
        cargs.extend([
            "-iter",
            str(params.get("iter"))
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("automask"):
        cargs.append("-automask")
    cargs.append(execution.input_file(params.get("dataset")))
    return cargs


def v_3d_median_filter_outputs(
    params: V3dMedianFilterParameters,
    execution: Execution,
) -> V3dMedianFilterOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMedianFilterOutputs(
        root=execution.output_file("."),
        output_brik=execution.output_file(params.get("prefix") + "+tlrc.BRIK") if (params.get("prefix") is not None) else None,
        output_head=execution.output_file(params.get("prefix") + "+tlrc.HEAD") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_median_filter_execute(
    params: V3dMedianFilterParameters,
    execution: Execution,
) -> V3dMedianFilterOutputs:
    """
    Computes the median in a spherical neighborhood around each point in the input
    to produce the output.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMedianFilterOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_median_filter_cargs(params, execution)
    ret = v_3d_median_filter_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_median_filter(
    dataset: InputPathType,
    irad: float | None = None,
    iter_: float | None = None,
    verbose: bool = False,
    prefix: str | None = None,
    automask: bool = False,
    runner: Runner | None = None,
) -> V3dMedianFilterOutputs:
    """
    Computes the median in a spherical neighborhood around each point in the input
    to produce the output.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        irad: Radius in voxels of spherical regions.
        iter_: Iterate 'n' times [default=1].
        verbose: Be verbose during run.
        prefix: Use 'pp' for prefix of output dataset.
        automask: Create a mask (a la 3dAutomask).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMedianFilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MEDIAN_FILTER_METADATA)
    params = v_3d_median_filter_params(irad=irad, iter_=iter_, verbose=verbose, prefix=prefix, automask=automask, dataset=dataset)
    return v_3d_median_filter_execute(params, execution)


__all__ = [
    "V3dMedianFilterOutputs",
    "V3dMedianFilterParameters",
    "V_3D_MEDIAN_FILTER_METADATA",
    "v_3d_median_filter",
    "v_3d_median_filter_params",
]
