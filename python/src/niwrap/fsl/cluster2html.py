# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CLUSTER2HTML_METADATA = Metadata(
    id="4888986f4fd601e816d92a86dd71f10fc36d506a.boutiques",
    name="cluster2html",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Cluster2htmlParameters = typing.TypedDict('Cluster2htmlParameters', {
    "__STYX_TYPE__": typing.Literal["cluster2html"],
    "featdir": str,
    "inroot": str,
    "std_flag": bool,
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
        "cluster2html": cluster2html_cargs,
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


class Cluster2htmlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cluster2html(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cluster2html_params(
    featdir: str,
    inroot: str,
    std_flag: bool = False,
) -> Cluster2htmlParameters:
    """
    Build parameters.
    
    Args:
        featdir: Directory containing the FEAT analysis results.
        inroot: Root name for cluster files (should not contain the _std\
            extension).
        std_flag: Indicate that the input files contain the _std extension.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cluster2html",
        "featdir": featdir,
        "inroot": inroot,
        "std_flag": std_flag,
    }
    return params


def cluster2html_cargs(
    params: Cluster2htmlParameters,
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
    cargs.append("cluster2html")
    cargs.append(params.get("featdir"))
    cargs.append(params.get("inroot"))
    if params.get("std_flag"):
        cargs.append("-std")
    return cargs


def cluster2html_outputs(
    params: Cluster2htmlParameters,
    execution: Execution,
) -> Cluster2htmlOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Cluster2htmlOutputs(
        root=execution.output_file("."),
    )
    return ret


def cluster2html_execute(
    params: Cluster2htmlParameters,
    execution: Execution,
) -> Cluster2htmlOutputs:
    """
    Generates an HTML report from cluster-based FEAT analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Cluster2htmlOutputs`).
    """
    params = execution.params(params)
    cargs = cluster2html_cargs(params, execution)
    ret = cluster2html_outputs(params, execution)
    execution.run(cargs)
    return ret


def cluster2html(
    featdir: str,
    inroot: str,
    std_flag: bool = False,
    runner: Runner | None = None,
) -> Cluster2htmlOutputs:
    """
    Generates an HTML report from cluster-based FEAT analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        featdir: Directory containing the FEAT analysis results.
        inroot: Root name for cluster files (should not contain the _std\
            extension).
        std_flag: Indicate that the input files contain the _std extension.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Cluster2htmlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUSTER2HTML_METADATA)
    params = cluster2html_params(featdir=featdir, inroot=inroot, std_flag=std_flag)
    return cluster2html_execute(params, execution)


__all__ = [
    "CLUSTER2HTML_METADATA",
    "Cluster2htmlOutputs",
    "Cluster2htmlParameters",
    "cluster2html",
    "cluster2html_params",
]
