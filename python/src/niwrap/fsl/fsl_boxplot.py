# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_BOXPLOT_METADATA = Metadata(
    id="8abcb032f30a04f5dd6924727b860dc8df188123.boutiques",
    name="fsl_boxplot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FslBoxplotParameters = typing.TypedDict('FslBoxplotParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_boxplot"],
    "input_files": list[InputPathType],
    "output_image": str,
    "title": typing.NotRequired[str | None],
    "legend_file": typing.NotRequired[InputPathType | None],
    "x_label": typing.NotRequired[str | None],
    "y_label": typing.NotRequired[str | None],
    "plot_height": typing.NotRequired[float | None],
    "plot_width": typing.NotRequired[float | None],
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
        "fsl_boxplot": fsl_boxplot_cargs,
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
        "fsl_boxplot": fsl_boxplot_outputs,
    }
    return vt.get(t)


class FslBoxplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_boxplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_png: OutputPathType
    """The output boxplot image in PNG format"""


def fsl_boxplot_params(
    input_files: list[InputPathType],
    output_image: str,
    title: str | None = None,
    legend_file: InputPathType | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    plot_height: float | None = 450,
    plot_width: float | None = None,
) -> FslBoxplotParameters:
    """
    Build parameters.
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrices, one column per boxplot).
        output_image: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        x_label: X-axis label.
        y_label: Y-axis label.
        plot_height: Plot height in pixels (default 450).
        plot_width: Plot width in pixels (default 80*#boxplots).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_boxplot",
        "input_files": input_files,
        "output_image": output_image,
    }
    if title is not None:
        params["title"] = title
    if legend_file is not None:
        params["legend_file"] = legend_file
    if x_label is not None:
        params["x_label"] = x_label
    if y_label is not None:
        params["y_label"] = y_label
    if plot_height is not None:
        params["plot_height"] = plot_height
    if plot_width is not None:
        params["plot_width"] = plot_width
    return params


def fsl_boxplot_cargs(
    params: FslBoxplotParameters,
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
    cargs.append("fsl_boxplot")
    cargs.extend([
        "--in",
        *[execution.input_file(f) for f in params.get("input_files")]
    ])
    cargs.extend([
        "--out",
        params.get("output_image")
    ])
    if params.get("title") is not None:
        cargs.extend([
            "--title",
            params.get("title")
        ])
    if params.get("legend_file") is not None:
        cargs.extend([
            "--legend",
            execution.input_file(params.get("legend_file"))
        ])
    if params.get("x_label") is not None:
        cargs.extend([
            "--xlabel",
            params.get("x_label")
        ])
    if params.get("y_label") is not None:
        cargs.extend([
            "--ylabel",
            params.get("y_label")
        ])
    if params.get("plot_height") is not None:
        cargs.extend([
            "--height",
            str(params.get("plot_height"))
        ])
    if params.get("plot_width") is not None:
        cargs.extend([
            "--width",
            str(params.get("plot_width"))
        ])
    return cargs


def fsl_boxplot_outputs(
    params: FslBoxplotParameters,
    execution: Execution,
) -> FslBoxplotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslBoxplotOutputs(
        root=execution.output_file("."),
        output_png=execution.output_file(params.get("output_image") + ".png"),
    )
    return ret


def fsl_boxplot_execute(
    params: FslBoxplotParameters,
    execution: Execution,
) -> FslBoxplotOutputs:
    """
    Tool for creating boxplot images from ASCII text matrices.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslBoxplotOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fsl_boxplot_cargs(params, execution)
    ret = fsl_boxplot_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_boxplot(
    input_files: list[InputPathType],
    output_image: str,
    title: str | None = None,
    legend_file: InputPathType | None = None,
    x_label: str | None = None,
    y_label: str | None = None,
    plot_height: float | None = 450,
    plot_width: float | None = None,
    runner: Runner | None = None,
) -> FslBoxplotOutputs:
    """
    Tool for creating boxplot images from ASCII text matrices.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrices, one column per boxplot).
        output_image: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        x_label: X-axis label.
        y_label: Y-axis label.
        plot_height: Plot height in pixels (default 450).
        plot_width: Plot width in pixels (default 80*#boxplots).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslBoxplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_BOXPLOT_METADATA)
    params = fsl_boxplot_params(input_files=input_files, output_image=output_image, title=title, legend_file=legend_file, x_label=x_label, y_label=y_label, plot_height=plot_height, plot_width=plot_width)
    return fsl_boxplot_execute(params, execution)


__all__ = [
    "FSL_BOXPLOT_METADATA",
    "FslBoxplotOutputs",
    "fsl_boxplot",
    "fsl_boxplot_params",
]
