# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MEAN_METADATA = Metadata(
    id="d608ce9fea57e85bfbfc19ea1af870315c233573.boutiques",
    name="mean",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MeanParameters = typing.TypedDict('MeanParameters', {
    "__STYX_TYPE__": typing.Literal["mean"],
    "datafile": InputPathType,
    "maskfile": InputPathType,
    "verbose_flag": bool,
    "debug_level": typing.NotRequired[float | None],
    "timing_flag": bool,
    "log_dir": typing.NotRequired[str | None],
    "forcedir_flag": bool,
    "inference_tech": typing.NotRequired[str | None],
    "num_jumps": typing.NotRequired[float | None],
    "num_burnin": typing.NotRequired[float | None],
    "num_sample_every": typing.NotRequired[float | None],
    "num_update_proposalevery": typing.NotRequired[float | None],
    "acceptance_rate": typing.NotRequired[float | None],
    "seed": typing.NotRequired[float | None],
    "error_precision": typing.NotRequired[float | None],
    "noamp_flag": bool,
    "prior_mean": typing.NotRequired[float | None],
    "prior_std": typing.NotRequired[float | None],
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
        "mean": mean_cargs,
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
        "mean": mean_outputs,
    }.get(t)


class MeanOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mean(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_log: OutputPathType
    """Output log of mean computation"""


def mean_params(
    datafile: InputPathType,
    maskfile: InputPathType,
    verbose_flag: bool = False,
    debug_level: float | None = None,
    timing_flag: bool = False,
    log_dir: str | None = None,
    forcedir_flag: bool = False,
    inference_tech: str | None = None,
    num_jumps: float | None = None,
    num_burnin: float | None = None,
    num_sample_every: float | None = None,
    num_update_proposalevery: float | None = None,
    acceptance_rate: float | None = None,
    seed: float | None = None,
    error_precision: float | None = None,
    noamp_flag: bool = False,
    prior_mean: float | None = None,
    prior_std: float | None = None,
) -> MeanParameters:
    """
    Build parameters.
    
    Args:
        datafile: Regressor data file.
        maskfile: Mask file.
        verbose_flag: Switch on diagnostic messages.
        debug_level: Set debug level.
        timing_flag: Turn timing on.
        log_dir: Log directory (default is logdir).
        forcedir_flag: Use the actual directory name given - i.e. don't add +\
            to make a new directory.
        inference_tech: Inference technique: mcmc or laplace (default is mcmc).
        num_jumps: Number of jumps to be made by MCMC (default is 5000).
        num_burnin: Number of jumps at start of MCMC to be discarded (default\
            is 500).
        num_sample_every: Number of jumps for each sample (MCMC) (default is 1).
        num_update_proposalevery: Number of jumps for each update to the\
            proposal density std (MCMC) (default is 40).
        acceptance_rate: Acceptance rate to aim for (MCMC) (default is 0.6).
        seed: Seed for pseudo random number generator.
        error_precision: Value to fix error precision to (default is -1, which\
            means error precision is not fixed).
        noamp_flag: Turn off Analytical Marginalisation of error Precision.
        prior_mean: Prior mean.
        prior_std: Prior standard deviation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mean",
        "datafile": datafile,
        "maskfile": maskfile,
        "verbose_flag": verbose_flag,
        "timing_flag": timing_flag,
        "forcedir_flag": forcedir_flag,
        "noamp_flag": noamp_flag,
    }
    if debug_level is not None:
        params["debug_level"] = debug_level
    if log_dir is not None:
        params["log_dir"] = log_dir
    if inference_tech is not None:
        params["inference_tech"] = inference_tech
    if num_jumps is not None:
        params["num_jumps"] = num_jumps
    if num_burnin is not None:
        params["num_burnin"] = num_burnin
    if num_sample_every is not None:
        params["num_sample_every"] = num_sample_every
    if num_update_proposalevery is not None:
        params["num_update_proposalevery"] = num_update_proposalevery
    if acceptance_rate is not None:
        params["acceptance_rate"] = acceptance_rate
    if seed is not None:
        params["seed"] = seed
    if error_precision is not None:
        params["error_precision"] = error_precision
    if prior_mean is not None:
        params["prior_mean"] = prior_mean
    if prior_std is not None:
        params["prior_std"] = prior_std
    return params


def mean_cargs(
    params: MeanParameters,
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
    cargs.append("mean")
    cargs.extend([
        "--data",
        execution.input_file(params.get("datafile"))
    ])
    cargs.extend([
        "--mask",
        execution.input_file(params.get("maskfile"))
    ])
    if params.get("verbose_flag"):
        cargs.append("--verbose")
    if params.get("debug_level") is not None:
        cargs.extend([
            "--debug",
            str(params.get("debug_level"))
        ])
    if params.get("timing_flag"):
        cargs.append("--to")
    if params.get("log_dir") is not None:
        cargs.extend([
            "--ld",
            params.get("log_dir")
        ])
    if params.get("forcedir_flag"):
        cargs.append("--forcedir")
    if params.get("inference_tech") is not None:
        cargs.extend([
            "--inf",
            params.get("inference_tech")
        ])
    if params.get("num_jumps") is not None:
        cargs.extend([
            "--nj",
            str(params.get("num_jumps"))
        ])
    if params.get("num_burnin") is not None:
        cargs.extend([
            "--bi",
            str(params.get("num_burnin"))
        ])
    if params.get("num_sample_every") is not None:
        cargs.extend([
            "--se",
            str(params.get("num_sample_every"))
        ])
    if params.get("num_update_proposalevery") is not None:
        cargs.extend([
            "--upe",
            str(params.get("num_update_proposalevery"))
        ])
    if params.get("acceptance_rate") is not None:
        cargs.extend([
            "--arate",
            str(params.get("acceptance_rate"))
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("error_precision") is not None:
        cargs.extend([
            "--prec",
            str(params.get("error_precision"))
        ])
    if params.get("noamp_flag"):
        cargs.append("--noamp")
    if params.get("prior_mean") is not None:
        cargs.extend([
            "--pm",
            str(params.get("prior_mean"))
        ])
    if params.get("prior_std") is not None:
        cargs.extend([
            "--ps",
            str(params.get("prior_std"))
        ])
    return cargs


def mean_outputs(
    params: MeanParameters,
    execution: Execution,
) -> MeanOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MeanOutputs(
        root=execution.output_file("."),
        output_log=execution.output_file("logdir/mean_output.txt"),
    )
    return ret


def mean_execute(
    params: MeanParameters,
    execution: Execution,
) -> MeanOutputs:
    """
    Diagnostic tool for analyzing and computing mean values for FSL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MeanOutputs`).
    """
    params = execution.params(params)
    cargs = mean_cargs(params, execution)
    ret = mean_outputs(params, execution)
    execution.run(cargs)
    return ret


def mean(
    datafile: InputPathType,
    maskfile: InputPathType,
    verbose_flag: bool = False,
    debug_level: float | None = None,
    timing_flag: bool = False,
    log_dir: str | None = None,
    forcedir_flag: bool = False,
    inference_tech: str | None = None,
    num_jumps: float | None = None,
    num_burnin: float | None = None,
    num_sample_every: float | None = None,
    num_update_proposalevery: float | None = None,
    acceptance_rate: float | None = None,
    seed: float | None = None,
    error_precision: float | None = None,
    noamp_flag: bool = False,
    prior_mean: float | None = None,
    prior_std: float | None = None,
    runner: Runner | None = None,
) -> MeanOutputs:
    """
    Diagnostic tool for analyzing and computing mean values for FSL data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        datafile: Regressor data file.
        maskfile: Mask file.
        verbose_flag: Switch on diagnostic messages.
        debug_level: Set debug level.
        timing_flag: Turn timing on.
        log_dir: Log directory (default is logdir).
        forcedir_flag: Use the actual directory name given - i.e. don't add +\
            to make a new directory.
        inference_tech: Inference technique: mcmc or laplace (default is mcmc).
        num_jumps: Number of jumps to be made by MCMC (default is 5000).
        num_burnin: Number of jumps at start of MCMC to be discarded (default\
            is 500).
        num_sample_every: Number of jumps for each sample (MCMC) (default is 1).
        num_update_proposalevery: Number of jumps for each update to the\
            proposal density std (MCMC) (default is 40).
        acceptance_rate: Acceptance rate to aim for (MCMC) (default is 0.6).
        seed: Seed for pseudo random number generator.
        error_precision: Value to fix error precision to (default is -1, which\
            means error precision is not fixed).
        noamp_flag: Turn off Analytical Marginalisation of error Precision.
        prior_mean: Prior mean.
        prior_std: Prior standard deviation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MeanOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEAN_METADATA)
    params = mean_params(datafile=datafile, maskfile=maskfile, verbose_flag=verbose_flag, debug_level=debug_level, timing_flag=timing_flag, log_dir=log_dir, forcedir_flag=forcedir_flag, inference_tech=inference_tech, num_jumps=num_jumps, num_burnin=num_burnin, num_sample_every=num_sample_every, num_update_proposalevery=num_update_proposalevery, acceptance_rate=acceptance_rate, seed=seed, error_precision=error_precision, noamp_flag=noamp_flag, prior_mean=prior_mean, prior_std=prior_std)
    return mean_execute(params, execution)


__all__ = [
    "MEAN_METADATA",
    "MeanOutputs",
    "MeanParameters",
    "mean",
    "mean_params",
]
