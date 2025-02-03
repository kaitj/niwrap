# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

POPP_METADATA = Metadata(
    id="29bde353620add34cd7a90603c61465fa385c87a.boutiques",
    name="popp",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
PoppParameters = typing.TypedDict('PoppParameters', {
    "__STYX_TYPE__": typing.Literal["popp"],
    "input_file": InputPathType,
    "output_basename": str,
    "sampling_rate": typing.NotRequired[float | None],
    "tr_value": typing.NotRequired[float | None],
    "resp_column": typing.NotRequired[float | None],
    "cardiac_column": typing.NotRequired[float | None],
    "trigger_column": typing.NotRequired[float | None],
    "rvt_flag": bool,
    "heart_rate_flag": bool,
    "pulseox_trigger_flag": bool,
    "smooth_card": typing.NotRequired[float | None],
    "smooth_resp": typing.NotRequired[float | None],
    "high_freq_cutoff": typing.NotRequired[float | None],
    "low_freq_cutoff": typing.NotRequired[float | None],
    "init_thresh_c": typing.NotRequired[float | None],
    "n_thresh_c": typing.NotRequired[float | None],
    "init_thresh_r": typing.NotRequired[float | None],
    "n_thresh_r": typing.NotRequired[float | None],
    "invert_resp_flag": bool,
    "invert_cardiac_flag": bool,
    "noclean1_flag": bool,
    "noclean2_flag": bool,
    "load_card_phase": typing.NotRequired[InputPathType | None],
    "load_resp_phase": typing.NotRequired[InputPathType | None],
    "vol_file": typing.NotRequired[InputPathType | None],
    "start_sample": typing.NotRequired[float | None],
    "resp_add": typing.NotRequired[str | None],
    "resp_del": typing.NotRequired[str | None],
    "card_add": typing.NotRequired[str | None],
    "card_del": typing.NotRequired[str | None],
    "verbose_flag": bool,
    "debug_flag": bool,
    "help_flag": bool,
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
        "popp": popp_cargs,
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
        "popp": popp_outputs,
    }
    return vt.get(t)


class PoppOutputs(typing.NamedTuple):
    """
    Output object returned when calling `popp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    processed_data_output: OutputPathType
    """Processed physiological data output"""
    timing_output: OutputPathType
    """Timing and triggers output"""
    rvt_data_output: OutputPathType
    """RVT data output file"""
    heartrate_data_output: OutputPathType
    """Heartrate data output file"""


def popp_params(
    input_file: InputPathType,
    output_basename: str,
    sampling_rate: float | None = 100,
    tr_value: float | None = None,
    resp_column: float | None = None,
    cardiac_column: float | None = None,
    trigger_column: float | None = None,
    rvt_flag: bool = False,
    heart_rate_flag: bool = False,
    pulseox_trigger_flag: bool = False,
    smooth_card: float | None = None,
    smooth_resp: float | None = None,
    high_freq_cutoff: float | None = 5,
    low_freq_cutoff: float | None = 0.1,
    init_thresh_c: float | None = 90,
    n_thresh_c: float | None = 60,
    init_thresh_r: float | None = 80,
    n_thresh_r: float | None = 80,
    invert_resp_flag: bool = False,
    invert_cardiac_flag: bool = False,
    noclean1_flag: bool = False,
    noclean2_flag: bool = False,
    load_card_phase: InputPathType | None = None,
    load_resp_phase: InputPathType | None = None,
    vol_file: InputPathType | None = None,
    start_sample: float | None = None,
    resp_add: str | None = None,
    resp_del: str | None = None,
    card_add: str | None = None,
    card_del: str | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    help_flag: bool = False,
) -> PoppParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input physiological data filename (text format).
        output_basename: Output basename for physiological data and\
            timing/triggers (no extensions).
        sampling_rate: Sampling rate in Hz (default is 100Hz).
        tr_value: TR value in seconds.
        resp_column: Specify column number of respiratory input.
        cardiac_column: Specify column number of cardiac input.
        trigger_column: Specify column number of trigger input.
        rvt_flag: Generate RVT data.
        heart_rate_flag: Generate heartrate data.
        pulseox_trigger_flag: Specify that cardiac data is a trigger.
        smooth_card: Specify smoothing amount for cardiac (in seconds).
        smooth_resp: Specify smoothing amount for respiratory (in seconds).
        high_freq_cutoff: High frequency cut off for respiratory filter in Hz\
            (default is 5Hz).
        low_freq_cutoff: Low frequency cut off for respiratory filter in Hz\
            (default is 0.1Hz).
        init_thresh_c: Initial threshold percentile for cardiac (default 90).
        n_thresh_c: Neighbourhood exclusion threshold percentile for cardiac\
            (default 60).
        init_thresh_r: Initial threshold percentile for respiratory (default\
            80).
        n_thresh_r: Neighbourhood exclusion threshold percentile for\
            respiratory (default 80).
        invert_resp_flag: Invert respiratory trace.
        invert_cardiac_flag: Invert cardiac trace.
        noclean1_flag: Turn off cleanup phase 1.
        noclean2_flag: Turn off cleanup phase 2.
        load_card_phase: Input cardiac phase for reprocessing (text format).
        load_resp_phase: Input respiratory phase for reprocessing (text format).
        vol_file: Input volumetric image (EPI) filename.
        start_sample: Set sample number of the starting time (t=0).
        resp_add: Comma separated list of times (in sec) to add to respiratory\
            peak list (uses nearest local max).
        resp_del: Comma separated list of times (in sec) to delete from\
            respiratory peak list (uses nearest existing peak).
        card_add: Comma separated list of times (in sec) to add to cardiac peak\
            list (uses nearest local max).
        card_del: Comma separated list of times (in sec) to delete from cardiac\
            peak list (uses nearest existing peak).
        verbose_flag: Switch on diagnostic messages.
        debug_flag: Output debugging information.
        help_flag: Display this help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "popp",
        "input_file": input_file,
        "output_basename": output_basename,
        "rvt_flag": rvt_flag,
        "heart_rate_flag": heart_rate_flag,
        "pulseox_trigger_flag": pulseox_trigger_flag,
        "invert_resp_flag": invert_resp_flag,
        "invert_cardiac_flag": invert_cardiac_flag,
        "noclean1_flag": noclean1_flag,
        "noclean2_flag": noclean2_flag,
        "verbose_flag": verbose_flag,
        "debug_flag": debug_flag,
        "help_flag": help_flag,
    }
    if sampling_rate is not None:
        params["sampling_rate"] = sampling_rate
    if tr_value is not None:
        params["tr_value"] = tr_value
    if resp_column is not None:
        params["resp_column"] = resp_column
    if cardiac_column is not None:
        params["cardiac_column"] = cardiac_column
    if trigger_column is not None:
        params["trigger_column"] = trigger_column
    if smooth_card is not None:
        params["smooth_card"] = smooth_card
    if smooth_resp is not None:
        params["smooth_resp"] = smooth_resp
    if high_freq_cutoff is not None:
        params["high_freq_cutoff"] = high_freq_cutoff
    if low_freq_cutoff is not None:
        params["low_freq_cutoff"] = low_freq_cutoff
    if init_thresh_c is not None:
        params["init_thresh_c"] = init_thresh_c
    if n_thresh_c is not None:
        params["n_thresh_c"] = n_thresh_c
    if init_thresh_r is not None:
        params["init_thresh_r"] = init_thresh_r
    if n_thresh_r is not None:
        params["n_thresh_r"] = n_thresh_r
    if load_card_phase is not None:
        params["load_card_phase"] = load_card_phase
    if load_resp_phase is not None:
        params["load_resp_phase"] = load_resp_phase
    if vol_file is not None:
        params["vol_file"] = vol_file
    if start_sample is not None:
        params["start_sample"] = start_sample
    if resp_add is not None:
        params["resp_add"] = resp_add
    if resp_del is not None:
        params["resp_del"] = resp_del
    if card_add is not None:
        params["card_add"] = card_add
    if card_del is not None:
        params["card_del"] = card_del
    return params


def popp_cargs(
    params: PoppParameters,
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
    cargs.append("popp")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_basename")
    ])
    if params.get("sampling_rate") is not None:
        cargs.extend([
            "-s",
            str(params.get("sampling_rate"))
        ])
    if params.get("tr_value") is not None:
        cargs.extend([
            "--tr",
            str(params.get("tr_value"))
        ])
    if params.get("resp_column") is not None:
        cargs.extend([
            "--resp",
            str(params.get("resp_column"))
        ])
    if params.get("cardiac_column") is not None:
        cargs.extend([
            "--cardiac",
            str(params.get("cardiac_column"))
        ])
    if params.get("trigger_column") is not None:
        cargs.extend([
            "--trigger",
            str(params.get("trigger_column"))
        ])
    if params.get("rvt_flag"):
        cargs.append("--rvt")
    if params.get("heart_rate_flag"):
        cargs.append("--heartrate")
    if params.get("pulseox_trigger_flag"):
        cargs.append("--pulseox_trigger")
    if params.get("smooth_card") is not None:
        cargs.extend([
            "--smoothcard",
            str(params.get("smooth_card"))
        ])
    if params.get("smooth_resp") is not None:
        cargs.extend([
            "--smoothresp",
            str(params.get("smooth_resp"))
        ])
    if params.get("high_freq_cutoff") is not None:
        cargs.extend([
            "--highfreqcutoff",
            str(params.get("high_freq_cutoff"))
        ])
    if params.get("low_freq_cutoff") is not None:
        cargs.extend([
            "--lowfreqcutoff",
            str(params.get("low_freq_cutoff"))
        ])
    if params.get("init_thresh_c") is not None:
        cargs.extend([
            "--initthreshc",
            str(params.get("init_thresh_c"))
        ])
    if params.get("n_thresh_c") is not None:
        cargs.extend([
            "--nthreshc",
            str(params.get("n_thresh_c"))
        ])
    if params.get("init_thresh_r") is not None:
        cargs.extend([
            "--initthreshr",
            str(params.get("init_thresh_r"))
        ])
    if params.get("n_thresh_r") is not None:
        cargs.extend([
            "--nthreshr",
            str(params.get("n_thresh_r"))
        ])
    if params.get("invert_resp_flag"):
        cargs.append("--invertresp")
    if params.get("invert_cardiac_flag"):
        cargs.append("--invertcardiac")
    if params.get("noclean1_flag"):
        cargs.append("--noclean1")
    if params.get("noclean2_flag"):
        cargs.append("--noclean2")
    if params.get("load_card_phase") is not None:
        cargs.extend([
            "--loadcardphase",
            execution.input_file(params.get("load_card_phase"))
        ])
    if params.get("load_resp_phase") is not None:
        cargs.extend([
            "--loadrespphase",
            execution.input_file(params.get("load_resp_phase"))
        ])
    if params.get("vol_file") is not None:
        cargs.extend([
            "--vol",
            execution.input_file(params.get("vol_file"))
        ])
    if params.get("start_sample") is not None:
        cargs.extend([
            "--startingsample",
            str(params.get("start_sample"))
        ])
    if params.get("resp_add") is not None:
        cargs.extend([
            "--respadd",
            params.get("resp_add")
        ])
    if params.get("resp_del") is not None:
        cargs.extend([
            "--respdel",
            params.get("resp_del")
        ])
    if params.get("card_add") is not None:
        cargs.extend([
            "--cardadd",
            params.get("card_add")
        ])
    if params.get("card_del") is not None:
        cargs.extend([
            "--carddel",
            params.get("card_del")
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    if params.get("debug_flag"):
        cargs.append("--debug")
    if params.get("help_flag"):
        cargs.append("-h")
    return cargs


def popp_outputs(
    params: PoppParameters,
    execution: Execution,
) -> PoppOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = PoppOutputs(
        root=execution.output_file("."),
        processed_data_output=execution.output_file(params.get("output_basename") + "_processed.txt"),
        timing_output=execution.output_file(params.get("output_basename") + "_timing.txt"),
        rvt_data_output=execution.output_file(params.get("output_basename") + "_rvt.txt"),
        heartrate_data_output=execution.output_file(params.get("output_basename") + "_heartrate.txt"),
    )
    return ret


def popp_execute(
    params: PoppParameters,
    execution: Execution,
) -> PoppOutputs:
    """
    Physiological data processing tool of FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `PoppOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = popp_cargs(params, execution)
    ret = popp_outputs(params, execution)
    execution.run(cargs)
    return ret


def popp(
    input_file: InputPathType,
    output_basename: str,
    sampling_rate: float | None = 100,
    tr_value: float | None = None,
    resp_column: float | None = None,
    cardiac_column: float | None = None,
    trigger_column: float | None = None,
    rvt_flag: bool = False,
    heart_rate_flag: bool = False,
    pulseox_trigger_flag: bool = False,
    smooth_card: float | None = None,
    smooth_resp: float | None = None,
    high_freq_cutoff: float | None = 5,
    low_freq_cutoff: float | None = 0.1,
    init_thresh_c: float | None = 90,
    n_thresh_c: float | None = 60,
    init_thresh_r: float | None = 80,
    n_thresh_r: float | None = 80,
    invert_resp_flag: bool = False,
    invert_cardiac_flag: bool = False,
    noclean1_flag: bool = False,
    noclean2_flag: bool = False,
    load_card_phase: InputPathType | None = None,
    load_resp_phase: InputPathType | None = None,
    vol_file: InputPathType | None = None,
    start_sample: float | None = None,
    resp_add: str | None = None,
    resp_del: str | None = None,
    card_add: str | None = None,
    card_del: str | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> PoppOutputs:
    """
    Physiological data processing tool of FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input physiological data filename (text format).
        output_basename: Output basename for physiological data and\
            timing/triggers (no extensions).
        sampling_rate: Sampling rate in Hz (default is 100Hz).
        tr_value: TR value in seconds.
        resp_column: Specify column number of respiratory input.
        cardiac_column: Specify column number of cardiac input.
        trigger_column: Specify column number of trigger input.
        rvt_flag: Generate RVT data.
        heart_rate_flag: Generate heartrate data.
        pulseox_trigger_flag: Specify that cardiac data is a trigger.
        smooth_card: Specify smoothing amount for cardiac (in seconds).
        smooth_resp: Specify smoothing amount for respiratory (in seconds).
        high_freq_cutoff: High frequency cut off for respiratory filter in Hz\
            (default is 5Hz).
        low_freq_cutoff: Low frequency cut off for respiratory filter in Hz\
            (default is 0.1Hz).
        init_thresh_c: Initial threshold percentile for cardiac (default 90).
        n_thresh_c: Neighbourhood exclusion threshold percentile for cardiac\
            (default 60).
        init_thresh_r: Initial threshold percentile for respiratory (default\
            80).
        n_thresh_r: Neighbourhood exclusion threshold percentile for\
            respiratory (default 80).
        invert_resp_flag: Invert respiratory trace.
        invert_cardiac_flag: Invert cardiac trace.
        noclean1_flag: Turn off cleanup phase 1.
        noclean2_flag: Turn off cleanup phase 2.
        load_card_phase: Input cardiac phase for reprocessing (text format).
        load_resp_phase: Input respiratory phase for reprocessing (text format).
        vol_file: Input volumetric image (EPI) filename.
        start_sample: Set sample number of the starting time (t=0).
        resp_add: Comma separated list of times (in sec) to add to respiratory\
            peak list (uses nearest local max).
        resp_del: Comma separated list of times (in sec) to delete from\
            respiratory peak list (uses nearest existing peak).
        card_add: Comma separated list of times (in sec) to add to cardiac peak\
            list (uses nearest local max).
        card_del: Comma separated list of times (in sec) to delete from cardiac\
            peak list (uses nearest existing peak).
        verbose_flag: Switch on diagnostic messages.
        debug_flag: Output debugging information.
        help_flag: Display this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PoppOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POPP_METADATA)
    params = popp_params(input_file=input_file, output_basename=output_basename, sampling_rate=sampling_rate, tr_value=tr_value, resp_column=resp_column, cardiac_column=cardiac_column, trigger_column=trigger_column, rvt_flag=rvt_flag, heart_rate_flag=heart_rate_flag, pulseox_trigger_flag=pulseox_trigger_flag, smooth_card=smooth_card, smooth_resp=smooth_resp, high_freq_cutoff=high_freq_cutoff, low_freq_cutoff=low_freq_cutoff, init_thresh_c=init_thresh_c, n_thresh_c=n_thresh_c, init_thresh_r=init_thresh_r, n_thresh_r=n_thresh_r, invert_resp_flag=invert_resp_flag, invert_cardiac_flag=invert_cardiac_flag, noclean1_flag=noclean1_flag, noclean2_flag=noclean2_flag, load_card_phase=load_card_phase, load_resp_phase=load_resp_phase, vol_file=vol_file, start_sample=start_sample, resp_add=resp_add, resp_del=resp_del, card_add=card_add, card_del=card_del, verbose_flag=verbose_flag, debug_flag=debug_flag, help_flag=help_flag)
    return popp_execute(params, execution)


__all__ = [
    "POPP_METADATA",
    "PoppOutputs",
    "popp",
    "popp_params",
]
