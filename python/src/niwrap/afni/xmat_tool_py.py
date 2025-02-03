# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XMAT_TOOL_PY_METADATA = Metadata(
    id="3a6bcb8aee2e7ab05a9a212e21f7dfef419b3b43.boutiques",
    name="xmat_tool.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
XmatToolPyParameters = typing.TypedDict('XmatToolPyParameters', {
    "__STYX_TYPE__": typing.Literal["xmat_tool.py"],
    "no_gui": bool,
    "load_xmat": typing.NotRequired[InputPathType | None],
    "load_1d": typing.NotRequired[InputPathType | None],
    "choose_cols": typing.NotRequired[str | None],
    "choose_nonzero_cols": bool,
    "chrono": bool,
    "cormat_cutoff": typing.NotRequired[float | None],
    "cosmat_cutoff": typing.NotRequired[float | None],
    "cosmat_motion": bool,
    "verb": typing.NotRequired[float | None],
    "show_col_types": bool,
    "show_conds": bool,
    "show_cormat": bool,
    "show_cormat_warnings": bool,
    "show_cosmat": bool,
    "show_cosmat_warnings": bool,
    "show_fit_betas": bool,
    "show_fit_ts": bool,
    "show_xmat": bool,
    "show_1d": bool,
    "gui_plot_xmat_as_one": bool,
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
        "xmat_tool.py": xmat_tool_py_cargs,
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
        "xmat_tool.py": xmat_tool_py_outputs,
    }
    return vt.get(t)


class XmatToolPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xmat_tool_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_fitts: OutputPathType
    """Output fit time series"""


def xmat_tool_py_params(
    no_gui: bool = False,
    load_xmat: InputPathType | None = None,
    load_1d: InputPathType | None = None,
    choose_cols: str | None = None,
    choose_nonzero_cols: bool = False,
    chrono: bool = False,
    cormat_cutoff: float | None = None,
    cosmat_cutoff: float | None = None,
    cosmat_motion: bool = False,
    verb: float | None = None,
    show_col_types: bool = False,
    show_conds: bool = False,
    show_cormat: bool = False,
    show_cormat_warnings: bool = False,
    show_cosmat: bool = False,
    show_cosmat_warnings: bool = False,
    show_fit_betas: bool = False,
    show_fit_ts: bool = False,
    show_xmat: bool = False,
    show_1d: bool = False,
    gui_plot_xmat_as_one: bool = False,
) -> XmatToolPyParameters:
    """
    Build parameters.
    
    Args:
        no_gui: Do not start the GUI.
        load_xmat: Load the AFNI X-matrix.
        load_1d: Load the 1D time series.
        choose_cols: Select columns to fit against.
        choose_nonzero_cols: Select only non-zero columns.
        chrono: Apply options chronologically.
        cormat_cutoff: Set min cutoff for correlation matrix warnings.
        cosmat_cutoff: Set min cutoff for cosine matrix warnings.
        cosmat_motion: Include motion in cosine matrix warnings.
        verb: Set the verbose level. Valid levels are currently 0..5.
        show_col_types: Display columns by regressor types.
        show_conds: Display a list of condition numbers.
        show_cormat: Display the correlation matrix.
        show_cormat_warnings: Show correlation matrix warnings.
        show_cosmat: Display the cosine matrix.
        show_cosmat_warnings: Show cosine matrix warnings.
        show_fit_betas: Show fit betas.
        show_fit_ts: Show fit time series.
        show_xmat: Display general X-matrix information.
        show_1d: Display general 1D information.
        gui_plot_xmat_as_one: Plot Xmat columns on single axis.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "xmat_tool.py",
        "no_gui": no_gui,
        "choose_nonzero_cols": choose_nonzero_cols,
        "chrono": chrono,
        "cosmat_motion": cosmat_motion,
        "show_col_types": show_col_types,
        "show_conds": show_conds,
        "show_cormat": show_cormat,
        "show_cormat_warnings": show_cormat_warnings,
        "show_cosmat": show_cosmat,
        "show_cosmat_warnings": show_cosmat_warnings,
        "show_fit_betas": show_fit_betas,
        "show_fit_ts": show_fit_ts,
        "show_xmat": show_xmat,
        "show_1d": show_1d,
        "gui_plot_xmat_as_one": gui_plot_xmat_as_one,
    }
    if load_xmat is not None:
        params["load_xmat"] = load_xmat
    if load_1d is not None:
        params["load_1d"] = load_1d
    if choose_cols is not None:
        params["choose_cols"] = choose_cols
    if cormat_cutoff is not None:
        params["cormat_cutoff"] = cormat_cutoff
    if cosmat_cutoff is not None:
        params["cosmat_cutoff"] = cosmat_cutoff
    if verb is not None:
        params["verb"] = verb
    return params


def xmat_tool_py_cargs(
    params: XmatToolPyParameters,
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
    cargs.append("xmat_tool.py")
    if params.get("no_gui"):
        cargs.append("-no_gui")
    if params.get("load_xmat") is not None:
        cargs.extend([
            "-load_xmat",
            execution.input_file(params.get("load_xmat"))
        ])
    if params.get("load_1d") is not None:
        cargs.extend([
            "-load_1D",
            execution.input_file(params.get("load_1d"))
        ])
    if params.get("choose_cols") is not None:
        cargs.extend([
            "-choose_cols",
            params.get("choose_cols")
        ])
    if params.get("choose_nonzero_cols"):
        cargs.append("-choose_nonzero_cols")
    if params.get("chrono"):
        cargs.append("-chrono")
    if params.get("cormat_cutoff") is not None:
        cargs.extend([
            "-cormat_cutoff",
            str(params.get("cormat_cutoff"))
        ])
    if params.get("cosmat_cutoff") is not None:
        cargs.extend([
            "-cosmat_cutoff",
            str(params.get("cosmat_cutoff"))
        ])
    if params.get("cosmat_motion"):
        cargs.append("-cosmat_motion")
    if params.get("verb") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verb"))
        ])
    if params.get("show_col_types"):
        cargs.append("-show_col_types")
    if params.get("show_conds"):
        cargs.append("-show_conds")
    if params.get("show_cormat"):
        cargs.append("-show_cormat")
    if params.get("show_cormat_warnings"):
        cargs.append("-show_cormat_warnings")
    if params.get("show_cosmat"):
        cargs.append("-show_cosmat")
    if params.get("show_cosmat_warnings"):
        cargs.append("-show_cosmat_warnings")
    if params.get("show_fit_betas"):
        cargs.append("-show_fit_betas")
    if params.get("show_fit_ts"):
        cargs.append("-show_fit_ts")
    if params.get("show_xmat"):
        cargs.append("-show_xmat")
    if params.get("show_1d"):
        cargs.append("-show_1D")
    if params.get("gui_plot_xmat_as_one"):
        cargs.append("-gui_plot_xmat_as_one")
    return cargs


def xmat_tool_py_outputs(
    params: XmatToolPyParameters,
    execution: Execution,
) -> XmatToolPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = XmatToolPyOutputs(
        root=execution.output_file("."),
        output_fitts=execution.output_file("fitts.1D"),
    )
    return ret


def xmat_tool_py_execute(
    params: XmatToolPyParameters,
    execution: Execution,
) -> XmatToolPyOutputs:
    """
    A tool for evaluating an AFNI X-matrix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `XmatToolPyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = xmat_tool_py_cargs(params, execution)
    ret = xmat_tool_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def xmat_tool_py(
    no_gui: bool = False,
    load_xmat: InputPathType | None = None,
    load_1d: InputPathType | None = None,
    choose_cols: str | None = None,
    choose_nonzero_cols: bool = False,
    chrono: bool = False,
    cormat_cutoff: float | None = None,
    cosmat_cutoff: float | None = None,
    cosmat_motion: bool = False,
    verb: float | None = None,
    show_col_types: bool = False,
    show_conds: bool = False,
    show_cormat: bool = False,
    show_cormat_warnings: bool = False,
    show_cosmat: bool = False,
    show_cosmat_warnings: bool = False,
    show_fit_betas: bool = False,
    show_fit_ts: bool = False,
    show_xmat: bool = False,
    show_1d: bool = False,
    gui_plot_xmat_as_one: bool = False,
    runner: Runner | None = None,
) -> XmatToolPyOutputs:
    """
    A tool for evaluating an AFNI X-matrix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        no_gui: Do not start the GUI.
        load_xmat: Load the AFNI X-matrix.
        load_1d: Load the 1D time series.
        choose_cols: Select columns to fit against.
        choose_nonzero_cols: Select only non-zero columns.
        chrono: Apply options chronologically.
        cormat_cutoff: Set min cutoff for correlation matrix warnings.
        cosmat_cutoff: Set min cutoff for cosine matrix warnings.
        cosmat_motion: Include motion in cosine matrix warnings.
        verb: Set the verbose level. Valid levels are currently 0..5.
        show_col_types: Display columns by regressor types.
        show_conds: Display a list of condition numbers.
        show_cormat: Display the correlation matrix.
        show_cormat_warnings: Show correlation matrix warnings.
        show_cosmat: Display the cosine matrix.
        show_cosmat_warnings: Show cosine matrix warnings.
        show_fit_betas: Show fit betas.
        show_fit_ts: Show fit time series.
        show_xmat: Display general X-matrix information.
        show_1d: Display general 1D information.
        gui_plot_xmat_as_one: Plot Xmat columns on single axis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XmatToolPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XMAT_TOOL_PY_METADATA)
    params = xmat_tool_py_params(no_gui=no_gui, load_xmat=load_xmat, load_1d=load_1d, choose_cols=choose_cols, choose_nonzero_cols=choose_nonzero_cols, chrono=chrono, cormat_cutoff=cormat_cutoff, cosmat_cutoff=cosmat_cutoff, cosmat_motion=cosmat_motion, verb=verb, show_col_types=show_col_types, show_conds=show_conds, show_cormat=show_cormat, show_cormat_warnings=show_cormat_warnings, show_cosmat=show_cosmat, show_cosmat_warnings=show_cosmat_warnings, show_fit_betas=show_fit_betas, show_fit_ts=show_fit_ts, show_xmat=show_xmat, show_1d=show_1d, gui_plot_xmat_as_one=gui_plot_xmat_as_one)
    return xmat_tool_py_execute(params, execution)


__all__ = [
    "XMAT_TOOL_PY_METADATA",
    "XmatToolPyOutputs",
    "xmat_tool_py",
    "xmat_tool_py_params",
]
