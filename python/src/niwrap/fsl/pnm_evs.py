# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

PNM_EVS_METADATA = Metadata(
    id="ad50045387407a73f19e9a4b5604b989851d1d52.boutiques",
    name="pnm_evs",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PnmEvsParameters = typing.TypedDict('PnmEvsParameters', {
    "__STYX_TYPE__": typing.Literal["pnm_evs"],
    "input_file": InputPathType,
    "output_file": str,
    "tr_value": float,
    "cardiac_file": typing.NotRequired[InputPathType | None],
    "respiratory_file": typing.NotRequired[InputPathType | None],
    "order_cardiac": typing.NotRequired[float | None],
    "order_respiratory": typing.NotRequired[float | None],
    "order_mult_cardiac": typing.NotRequired[float | None],
    "order_mult_respiratory": typing.NotRequired[float | None],
    "csf_mask": typing.NotRequired[InputPathType | None],
    "rvt_file": typing.NotRequired[InputPathType | None],
    "heartrate_file": typing.NotRequired[InputPathType | None],
    "rvt_smooth": typing.NotRequired[float | None],
    "heartrate_smooth": typing.NotRequired[float | None],
    "slice_direction": typing.NotRequired[str | None],
    "slice_order": typing.NotRequired[str | None],
    "slice_timing_file": typing.NotRequired[InputPathType | None],
    "debug_flag": bool,
    "verbose_flag": bool,
    "help_flag": bool,
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
        "pnm_evs": pnm_evs_cargs,
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
        "pnm_evs": pnm_evs_outputs,
    }.get(t)


class PnmEvsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pnm_evs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output confound/EV matrix file"""


def pnm_evs_params(
    input_file: InputPathType,
    output_file: str,
    tr_value: float,
    cardiac_file: InputPathType | None = None,
    respiratory_file: InputPathType | None = None,
    order_cardiac: float | None = 2,
    order_respiratory: float | None = 1,
    order_mult_cardiac: float | None = 0,
    order_mult_respiratory: float | None = 0,
    csf_mask: InputPathType | None = None,
    rvt_file: InputPathType | None = None,
    heartrate_file: InputPathType | None = None,
    rvt_smooth: float | None = 0,
    heartrate_smooth: float | None = None,
    slice_direction: str | None = "z",
    slice_order: str | None = None,
    slice_timing_file: InputPathType | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
) -> PnmEvsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input image filename (4D functional/EPI data).
        output_file: Output filename (for confound/EV matrix).
        tr_value: TR of fMRI volumes (in seconds).
        cardiac_file: Input filename for cardiac values (1 or 2 columns: time\
            [phase]).
        respiratory_file: Input filename for respiratory phase values (1 or 2\
            columns: time [phase]).
        order_cardiac: Order of basic cardiac regressors (number of Fourier\
            pairs).
        order_respiratory: Order of basic respiratory regressors (number of\
            Fourier pairs).
        order_mult_cardiac: Order of multiplicative cardiac terms (also need to\
            set --multr).
        order_mult_respiratory: Order of multiplicative respiratory terms (also\
            need to set --multc).
        csf_mask: Filename of CSF mask image (and generate CSF regressor).
        rvt_file: Input filename of RVT data (2 columns: time value).
        heartrate_file: Input filename for heart rate data (2 columns: time\
            value).
        rvt_smooth: Optional smoothing of RVT regressor (in seconds).
        heartrate_smooth: Optional smoothing of heart rate regressor (in\
            seconds).
        slice_direction: Specify slice direction (x/y/z).
        slice_order: Specify slice ordering\
            (up/down/interleaved_up/interleaved_down).
        slice_timing_file: Specify slice timing via an external file.
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pnm_evs",
        "input_file": input_file,
        "output_file": output_file,
        "tr_value": tr_value,
        "debug_flag": debug_flag,
        "verbose_flag": verbose_flag,
        "help_flag": help_flag,
    }
    if cardiac_file is not None:
        params["cardiac_file"] = cardiac_file
    if respiratory_file is not None:
        params["respiratory_file"] = respiratory_file
    if order_cardiac is not None:
        params["order_cardiac"] = order_cardiac
    if order_respiratory is not None:
        params["order_respiratory"] = order_respiratory
    if order_mult_cardiac is not None:
        params["order_mult_cardiac"] = order_mult_cardiac
    if order_mult_respiratory is not None:
        params["order_mult_respiratory"] = order_mult_respiratory
    if csf_mask is not None:
        params["csf_mask"] = csf_mask
    if rvt_file is not None:
        params["rvt_file"] = rvt_file
    if heartrate_file is not None:
        params["heartrate_file"] = heartrate_file
    if rvt_smooth is not None:
        params["rvt_smooth"] = rvt_smooth
    if heartrate_smooth is not None:
        params["heartrate_smooth"] = heartrate_smooth
    if slice_direction is not None:
        params["slice_direction"] = slice_direction
    if slice_order is not None:
        params["slice_order"] = slice_order
    if slice_timing_file is not None:
        params["slice_timing_file"] = slice_timing_file
    return params


def pnm_evs_cargs(
    params: PnmEvsParameters,
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
    cargs.append("pnm_evs")
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "--out",
        params.get("output_file")
    ])
    cargs.extend([
        "--tr",
        str(params.get("tr_value"))
    ])
    if params.get("cardiac_file") is not None:
        cargs.extend([
            "--cardiac",
            execution.input_file(params.get("cardiac_file"))
        ])
    if params.get("respiratory_file") is not None:
        cargs.extend([
            "--respiratory",
            execution.input_file(params.get("respiratory_file"))
        ])
    if params.get("order_cardiac") is not None:
        cargs.extend([
            "--oc",
            str(params.get("order_cardiac"))
        ])
    if params.get("order_respiratory") is not None:
        cargs.extend([
            "--or",
            str(params.get("order_respiratory"))
        ])
    if params.get("order_mult_cardiac") is not None:
        cargs.extend([
            "--multc",
            str(params.get("order_mult_cardiac"))
        ])
    if params.get("order_mult_respiratory") is not None:
        cargs.extend([
            "--multr",
            str(params.get("order_mult_respiratory"))
        ])
    if params.get("csf_mask") is not None:
        cargs.extend([
            "--csfmask",
            execution.input_file(params.get("csf_mask"))
        ])
    if params.get("rvt_file") is not None:
        cargs.extend([
            "--rvt",
            execution.input_file(params.get("rvt_file"))
        ])
    if params.get("heartrate_file") is not None:
        cargs.extend([
            "--heartrate",
            execution.input_file(params.get("heartrate_file"))
        ])
    if params.get("rvt_smooth") is not None:
        cargs.extend([
            "--rvtsmooth",
            str(params.get("rvt_smooth"))
        ])
    if params.get("heartrate_smooth") is not None:
        cargs.extend([
            "--heartratesmooth",
            str(params.get("heartrate_smooth"))
        ])
    if params.get("slice_direction") is not None:
        cargs.extend([
            "--slicedir",
            params.get("slice_direction")
        ])
    if params.get("slice_order") is not None:
        cargs.extend([
            "--sliceorder",
            params.get("slice_order")
        ])
    if params.get("slice_timing_file") is not None:
        cargs.extend([
            "--slicetiming",
            execution.input_file(params.get("slice_timing_file"))
        ])
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    if params.get("help_flag"):
        cargs.append("--help")
    return cargs


def pnm_evs_outputs(
    params: PnmEvsParameters,
    execution: Execution,
) -> PnmEvsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PnmEvsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def pnm_evs_execute(
    params: PnmEvsParameters,
    execution: Execution,
) -> PnmEvsOutputs:
    """
    PNM EVs: Generates physiological noise regressors for fMRI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PnmEvsOutputs`).
    """
    params = execution.params(params)
    cargs = pnm_evs_cargs(params, execution)
    ret = pnm_evs_outputs(params, execution)
    execution.run(cargs)
    return ret


def pnm_evs(
    input_file: InputPathType,
    output_file: str,
    tr_value: float,
    cardiac_file: InputPathType | None = None,
    respiratory_file: InputPathType | None = None,
    order_cardiac: float | None = 2,
    order_respiratory: float | None = 1,
    order_mult_cardiac: float | None = 0,
    order_mult_respiratory: float | None = 0,
    csf_mask: InputPathType | None = None,
    rvt_file: InputPathType | None = None,
    heartrate_file: InputPathType | None = None,
    rvt_smooth: float | None = 0,
    heartrate_smooth: float | None = None,
    slice_direction: str | None = "z",
    slice_order: str | None = None,
    slice_timing_file: InputPathType | None = None,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> PnmEvsOutputs:
    """
    PNM EVs: Generates physiological noise regressors for fMRI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input image filename (4D functional/EPI data).
        output_file: Output filename (for confound/EV matrix).
        tr_value: TR of fMRI volumes (in seconds).
        cardiac_file: Input filename for cardiac values (1 or 2 columns: time\
            [phase]).
        respiratory_file: Input filename for respiratory phase values (1 or 2\
            columns: time [phase]).
        order_cardiac: Order of basic cardiac regressors (number of Fourier\
            pairs).
        order_respiratory: Order of basic respiratory regressors (number of\
            Fourier pairs).
        order_mult_cardiac: Order of multiplicative cardiac terms (also need to\
            set --multr).
        order_mult_respiratory: Order of multiplicative respiratory terms (also\
            need to set --multc).
        csf_mask: Filename of CSF mask image (and generate CSF regressor).
        rvt_file: Input filename of RVT data (2 columns: time value).
        heartrate_file: Input filename for heart rate data (2 columns: time\
            value).
        rvt_smooth: Optional smoothing of RVT regressor (in seconds).
        heartrate_smooth: Optional smoothing of heart rate regressor (in\
            seconds).
        slice_direction: Specify slice direction (x/y/z).
        slice_order: Specify slice ordering\
            (up/down/interleaved_up/interleaved_down).
        slice_timing_file: Specify slice timing via an external file.
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PnmEvsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PNM_EVS_METADATA)
    params = pnm_evs_params(input_file=input_file, output_file=output_file, tr_value=tr_value, cardiac_file=cardiac_file, respiratory_file=respiratory_file, order_cardiac=order_cardiac, order_respiratory=order_respiratory, order_mult_cardiac=order_mult_cardiac, order_mult_respiratory=order_mult_respiratory, csf_mask=csf_mask, rvt_file=rvt_file, heartrate_file=heartrate_file, rvt_smooth=rvt_smooth, heartrate_smooth=heartrate_smooth, slice_direction=slice_direction, slice_order=slice_order, slice_timing_file=slice_timing_file, debug_flag=debug_flag, verbose_flag=verbose_flag, help_flag=help_flag)
    return pnm_evs_execute(params, execution)


__all__ = [
    "PNM_EVS_METADATA",
    "PnmEvsOutputs",
    "PnmEvsParameters",
    "pnm_evs",
    "pnm_evs_params",
]
