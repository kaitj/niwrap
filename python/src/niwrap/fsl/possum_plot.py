# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

POSSUM_PLOT_METADATA = Metadata(
    id="8ed3fa6e50d07f3853fcec9ca53f667a78d048a0.boutiques",
    name="possum_plot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PossumPlotParameters = typing.TypedDict('PossumPlotParameters', {
    "__STYX_TYPE__": typing.Literal["possum_plot"],
    "input_file": InputPathType,
    "output_basename": str,
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
        "possum_plot": possum_plot_cargs,
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
        "possum_plot": possum_plot_outputs,
    }
    return vt.get(t)


class PossumPlotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_plot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_plots: OutputPathType
    """Output plot images from POSSUM"""


def possum_plot_params(
    input_file: InputPathType,
    output_basename: str,
) -> PossumPlotParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file from POSSUM simulation (e.g.\
            simulation_results.txt).
        output_basename: Basename for output files (e.g. plot_output).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "possum_plot",
        "input_file": input_file,
        "output_basename": output_basename,
    }
    return params


def possum_plot_cargs(
    params: PossumPlotParameters,
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
    cargs.append("possum_plot.py")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_basename"))
    return cargs


def possum_plot_outputs(
    params: PossumPlotParameters,
    execution: Execution,
) -> PossumPlotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PossumPlotOutputs(
        root=execution.output_file("."),
        output_plots=execution.output_file(params.get("output_basename") + "_*.png"),
    )
    return ret


def possum_plot_execute(
    params: PossumPlotParameters,
    execution: Execution,
) -> PossumPlotOutputs:
    """
    Tool for plotting results from POSSUM simulations in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PossumPlotOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = possum_plot_cargs(params, execution)
    ret = possum_plot_outputs(params, execution)
    execution.run(cargs)
    return ret


def possum_plot(
    input_file: InputPathType,
    output_basename: str,
    runner: Runner | None = None,
) -> PossumPlotOutputs:
    """
    Tool for plotting results from POSSUM simulations in FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file from POSSUM simulation (e.g.\
            simulation_results.txt).
        output_basename: Basename for output files (e.g. plot_output).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumPlotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_PLOT_METADATA)
    params = possum_plot_params(input_file=input_file, output_basename=output_basename)
    return possum_plot_execute(params, execution)


__all__ = [
    "POSSUM_PLOT_METADATA",
    "PossumPlotOutputs",
    "possum_plot",
    "possum_plot_params",
]
