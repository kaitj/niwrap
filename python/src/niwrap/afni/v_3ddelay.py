# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DDELAY_METADATA = Metadata(
    id="d876295ae5d31352ba81e14a366aedff6fceb582.boutiques",
    name="3ddelay",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3ddelayParameters = typing.TypedDict('V3ddelayParameters', {
    "__STYX_TYPE__": typing.Literal["3ddelay"],
    "input_file": InputPathType,
    "reference_file": InputPathType,
    "sampling_freq": float,
    "stim_period": float,
    "prefix": typing.NotRequired[str | None],
    "polort": typing.NotRequired[float | None],
    "nodtrnd": bool,
    "units_seconds": bool,
    "units_degrees": bool,
    "units_radians": bool,
    "phzwrp": bool,
    "nophzwrp": bool,
    "phzreverse": bool,
    "phzscale": typing.NotRequired[float | None],
    "bias": bool,
    "nobias": bool,
    "dsamp": bool,
    "nodsamp": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "nfirst": typing.NotRequired[float | None],
    "nlast": typing.NotRequired[float | None],
    "co": typing.NotRequired[float | None],
    "asc": typing.NotRequired[str | None],
    "ascts": typing.NotRequired[str | None],
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
        "3ddelay": v_3ddelay_cargs,
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
        "3ddelay": v_3ddelay_outputs,
    }
    return vt.get(t)


class V3ddelayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3ddelay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brick: OutputPathType | None
    """Primary output results Brick for Delay"""
    output_asc: OutputPathType | None
    """Output ASCII file for results"""
    output_asc_log: OutputPathType | None
    """Log file containing parameter settings and warnings"""
    output_asc_ts: OutputPathType | None
    """Output ASCII file with time series"""


def v_3ddelay_params(
    input_file: InputPathType,
    reference_file: InputPathType,
    sampling_freq: float,
    stim_period: float,
    prefix: str | None = None,
    polort: float | None = None,
    nodtrnd: bool = False,
    units_seconds: bool = False,
    units_degrees: bool = False,
    units_radians: bool = False,
    phzwrp: bool = False,
    nophzwrp: bool = False,
    phzreverse: bool = False,
    phzscale: float | None = None,
    bias: bool = False,
    nobias: bool = False,
    dsamp: bool = False,
    nodsamp: bool = False,
    mask: InputPathType | None = None,
    nfirst: float | None = None,
    nlast: float | None = None,
    co: float | None = None,
    asc: str | None = None,
    ascts: str | None = None,
) -> V3ddelayParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename of the input 3D+time dataset.
        reference_file: Input ideal time series file name.
        sampling_freq: Sampling frequency in Hz. of data time series (1/TR).
        stim_period: Stimulus period in seconds. Set to 0 if stimulus is not\
            periodic.
        prefix: The prefix for the results Brick.
        polort: Detrend input time series with polynomial of specified order.\
            Default is -1 for auto selection.
        nodtrnd: Remove only the mean (equivalent to polort 0).
        units_seconds: Units for delay estimates in seconds.
        units_degrees: Units for delay estimates in degrees. Requires Tstim > 0.
        units_radians: Units for delay estimates in radians. Requires Tstim > 0.
        phzwrp: Wrap delay (or phase) values.
        nophzwrp: Do not wrap phase (default).
        phzreverse: Reverse phase such that phase -> (T-phase).
        phzscale: Scale phase: phase -> phase*SC (default no scaling).
        bias: Do not correct for the bias in the estimates.
        nobias: Correct for the bias in the estimates (default).
        dsamp: Correct for slice timing differences (default).
        nodsamp: Do not correct for slice timing differences.
        mask: Filename of mask dataset. Only voxels with non-zero values in the\
            mask will be considered.
        nfirst: Number of first dataset image to use in the delay estimate.
        nlast: Number of last dataset image to use in the delay estimate.
        co: Cross Correlation Coefficient threshold value to limit ascii output.
        asc: Write the results to an ascii file for voxels with cross\
            correlation coefficients larger than CCT.
        ascts: Write the results and time series to an ascii file for voxels\
            with cross correlation coefficients larger than CCT.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3ddelay",
        "input_file": input_file,
        "reference_file": reference_file,
        "sampling_freq": sampling_freq,
        "stim_period": stim_period,
        "nodtrnd": nodtrnd,
        "units_seconds": units_seconds,
        "units_degrees": units_degrees,
        "units_radians": units_radians,
        "phzwrp": phzwrp,
        "nophzwrp": nophzwrp,
        "phzreverse": phzreverse,
        "bias": bias,
        "nobias": nobias,
        "dsamp": dsamp,
        "nodsamp": nodsamp,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if polort is not None:
        params["polort"] = polort
    if phzscale is not None:
        params["phzscale"] = phzscale
    if mask is not None:
        params["mask"] = mask
    if nfirst is not None:
        params["nfirst"] = nfirst
    if nlast is not None:
        params["nlast"] = nlast
    if co is not None:
        params["co"] = co
    if asc is not None:
        params["asc"] = asc
    if ascts is not None:
        params["ascts"] = ascts
    return params


def v_3ddelay_cargs(
    params: V3ddelayParameters,
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
    cargs.append("3ddelay")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(execution.input_file(params.get("reference_file")))
    cargs.extend([
        "-fs",
        str(params.get("sampling_freq"))
    ])
    cargs.extend([
        "-T",
        str(params.get("stim_period"))
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("polort") is not None:
        cargs.extend([
            "-polort",
            str(params.get("polort"))
        ])
    if params.get("nodtrnd"):
        cargs.append("-nodtrnd")
    if params.get("units_seconds"):
        cargs.append("-uS")
    if params.get("units_degrees"):
        cargs.append("-uD")
    if params.get("units_radians"):
        cargs.append("-uR")
    if params.get("phzwrp"):
        cargs.append("-phzwrp")
    if params.get("nophzwrp"):
        cargs.append("-nophzwrp")
    if params.get("phzreverse"):
        cargs.append("-phzreverse")
    if params.get("phzscale") is not None:
        cargs.extend([
            "-phzscale",
            str(params.get("phzscale"))
        ])
    if params.get("bias"):
        cargs.append("-bias")
    if params.get("nobias"):
        cargs.append("-nobias")
    if params.get("dsamp"):
        cargs.append("-dsamp")
    if params.get("nodsamp"):
        cargs.append("-nodsamp")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("nfirst") is not None:
        cargs.extend([
            "-nfirst",
            str(params.get("nfirst"))
        ])
    if params.get("nlast") is not None:
        cargs.extend([
            "-nlast",
            str(params.get("nlast"))
        ])
    if params.get("co") is not None:
        cargs.extend([
            "-co",
            str(params.get("co"))
        ])
    if params.get("asc") is not None:
        cargs.extend([
            "-asc",
            params.get("asc")
        ])
    if params.get("ascts") is not None:
        cargs.extend([
            "-ascts",
            params.get("ascts")
        ])
    return cargs


def v_3ddelay_outputs(
    params: V3ddelayParameters,
    execution: Execution,
) -> V3ddelayOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3ddelayOutputs(
        root=execution.output_file("."),
        output_brick=execution.output_file(params.get("prefix") + ".DEL+orig.BRIK") if (params.get("prefix") is not None) else None,
        output_asc=execution.output_file(params.get("prefix") + ".ASC") if (params.get("prefix") is not None) else None,
        output_asc_log=execution.output_file(params.get("prefix") + ".ASC.log") if (params.get("prefix") is not None) else None,
        output_asc_ts=execution.output_file(params.get("prefix") + ".ASC.ts") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3ddelay_execute(
    params: V3ddelayParameters,
    execution: Execution,
) -> V3ddelayOutputs:
    """
    Estimates the time delay between each voxel time series in a 3D+time dataset and
    a reference time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3ddelayOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3ddelay_cargs(params, execution)
    ret = v_3ddelay_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3ddelay(
    input_file: InputPathType,
    reference_file: InputPathType,
    sampling_freq: float,
    stim_period: float,
    prefix: str | None = None,
    polort: float | None = None,
    nodtrnd: bool = False,
    units_seconds: bool = False,
    units_degrees: bool = False,
    units_radians: bool = False,
    phzwrp: bool = False,
    nophzwrp: bool = False,
    phzreverse: bool = False,
    phzscale: float | None = None,
    bias: bool = False,
    nobias: bool = False,
    dsamp: bool = False,
    nodsamp: bool = False,
    mask: InputPathType | None = None,
    nfirst: float | None = None,
    nlast: float | None = None,
    co: float | None = None,
    asc: str | None = None,
    ascts: str | None = None,
    runner: Runner | None = None,
) -> V3ddelayOutputs:
    """
    Estimates the time delay between each voxel time series in a 3D+time dataset and
    a reference time series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Filename of the input 3D+time dataset.
        reference_file: Input ideal time series file name.
        sampling_freq: Sampling frequency in Hz. of data time series (1/TR).
        stim_period: Stimulus period in seconds. Set to 0 if stimulus is not\
            periodic.
        prefix: The prefix for the results Brick.
        polort: Detrend input time series with polynomial of specified order.\
            Default is -1 for auto selection.
        nodtrnd: Remove only the mean (equivalent to polort 0).
        units_seconds: Units for delay estimates in seconds.
        units_degrees: Units for delay estimates in degrees. Requires Tstim > 0.
        units_radians: Units for delay estimates in radians. Requires Tstim > 0.
        phzwrp: Wrap delay (or phase) values.
        nophzwrp: Do not wrap phase (default).
        phzreverse: Reverse phase such that phase -> (T-phase).
        phzscale: Scale phase: phase -> phase*SC (default no scaling).
        bias: Do not correct for the bias in the estimates.
        nobias: Correct for the bias in the estimates (default).
        dsamp: Correct for slice timing differences (default).
        nodsamp: Do not correct for slice timing differences.
        mask: Filename of mask dataset. Only voxels with non-zero values in the\
            mask will be considered.
        nfirst: Number of first dataset image to use in the delay estimate.
        nlast: Number of last dataset image to use in the delay estimate.
        co: Cross Correlation Coefficient threshold value to limit ascii output.
        asc: Write the results to an ascii file for voxels with cross\
            correlation coefficients larger than CCT.
        ascts: Write the results and time series to an ascii file for voxels\
            with cross correlation coefficients larger than CCT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3ddelayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DDELAY_METADATA)
    params = v_3ddelay_params(input_file=input_file, reference_file=reference_file, sampling_freq=sampling_freq, stim_period=stim_period, prefix=prefix, polort=polort, nodtrnd=nodtrnd, units_seconds=units_seconds, units_degrees=units_degrees, units_radians=units_radians, phzwrp=phzwrp, nophzwrp=nophzwrp, phzreverse=phzreverse, phzscale=phzscale, bias=bias, nobias=nobias, dsamp=dsamp, nodsamp=nodsamp, mask=mask, nfirst=nfirst, nlast=nlast, co=co, asc=asc, ascts=ascts)
    return v_3ddelay_execute(params, execution)


__all__ = [
    "V3ddelayOutputs",
    "V_3DDELAY_METADATA",
    "v_3ddelay",
    "v_3ddelay_params",
]
