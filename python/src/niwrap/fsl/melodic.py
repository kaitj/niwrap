# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MELODIC_METADATA = Metadata(
    id="676ecf3f7a3e52a01972f67049800329276421c8.boutiques",
    name="melodic",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
MelodicParameters = typing.TypedDict('MelodicParameters', {
    "__STYX_TYPE__": typing.Literal["melodic"],
    "input_file": InputPathType,
    "output_directory": typing.NotRequired[str | None],
    "mask_file": typing.NotRequired[InputPathType | None],
    "dimensionality_reduction": typing.NotRequired[float | None],
    "generate_report": bool,
    "cifti_io": bool,
    "variance_normalization": bool,
    "no_masking": bool,
    "update_masking": bool,
    "no_bet": bool,
    "bg_threshold": typing.NotRequired[float | None],
    "dimest_technique": typing.NotRequired[str | None],
    "separate_variance_normalization": bool,
    "disable_migp": bool,
    "num_internal_eigenmaps": typing.NotRequired[float | None],
    "migp_shuffle": bool,
    "migp_factor": typing.NotRequired[float | None],
    "num_ics": typing.NotRequired[float | None],
    "nonlinearity": typing.NotRequired[str | None],
    "covar_weights": typing.NotRequired[InputPathType | None],
    "eps_error": typing.NotRequired[float | None],
    "eps_rank1_error": typing.NotRequired[float | None],
    "max_iters": typing.NotRequired[float | None],
    "max_restarts": typing.NotRequired[float | None],
    "mm_threshold": typing.NotRequired[float | None],
    "no_mixture_modeling": bool,
    "ic_components_file": typing.NotRequired[InputPathType | None],
    "mixing_matrix_file": typing.NotRequired[InputPathType | None],
    "session_modes_file": typing.NotRequired[InputPathType | None],
    "component_filter": typing.NotRequired[str | None],
    "background_image": typing.NotRequired[InputPathType | None],
    "tr_seconds": typing.NotRequired[float | None],
    "log_power_calc": bool,
    "time_domain_design_matrix": typing.NotRequired[InputPathType | None],
    "time_domain_t_contrast_matrix": typing.NotRequired[InputPathType | None],
    "subject_domain_design_matrix": typing.NotRequired[InputPathType | None],
    "subject_domain_t_contrast_matrix": typing.NotRequired[InputPathType | None],
    "output_unmixing_matrix": bool,
    "output_stats": bool,
    "output_pca": bool,
    "output_whitening": bool,
    "output_original_ics": bool,
    "output_mean_volume": bool,
    "version": bool,
    "copyright": bool,
    "help": bool,
    "debug": bool,
    "report_maps": typing.NotRequired[str | None],
    "keep_meanvol": bool,
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
        "melodic": melodic_cargs,
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
        "melodic": melodic_outputs,
    }.get(t)


class MelodicOutputs(typing.NamedTuple):
    """
    Output object returned when calling `melodic(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    report_file: OutputPathType | None
    """Output Melodic web report"""
    ics_output_file: OutputPathType | None
    """Output IC components file"""
    mix_output_file: OutputPathType | None
    """Output mixing matrix file"""
    temporal_mode_file: OutputPathType | None
    """Output matrix of temporal modes"""
    melodic_report_directory: OutputPathType | None
    """Output Melodic report directory"""


def melodic_params(
    input_file: InputPathType,
    output_directory: str | None = None,
    mask_file: InputPathType | None = None,
    dimensionality_reduction: float | None = None,
    generate_report: bool = False,
    cifti_io: bool = False,
    variance_normalization: bool = False,
    no_masking: bool = False,
    update_masking: bool = False,
    no_bet: bool = False,
    bg_threshold: float | None = None,
    dimest_technique: str | None = None,
    separate_variance_normalization: bool = False,
    disable_migp: bool = False,
    num_internal_eigenmaps: float | None = None,
    migp_shuffle: bool = False,
    migp_factor: float | None = None,
    num_ics: float | None = None,
    nonlinearity: str | None = None,
    covar_weights: InputPathType | None = None,
    eps_error: float | None = None,
    eps_rank1_error: float | None = None,
    max_iters: float | None = None,
    max_restarts: float | None = None,
    mm_threshold: float | None = None,
    no_mixture_modeling: bool = False,
    ic_components_file: InputPathType | None = None,
    mixing_matrix_file: InputPathType | None = None,
    session_modes_file: InputPathType | None = None,
    component_filter: str | None = None,
    background_image: InputPathType | None = None,
    tr_seconds: float | None = None,
    log_power_calc: bool = False,
    time_domain_design_matrix: InputPathType | None = None,
    time_domain_t_contrast_matrix: InputPathType | None = None,
    subject_domain_design_matrix: InputPathType | None = None,
    subject_domain_t_contrast_matrix: InputPathType | None = None,
    output_unmixing_matrix: bool = False,
    output_stats: bool = False,
    output_pca: bool = False,
    output_whitening: bool = False,
    output_original_ics: bool = False,
    output_mean_volume: bool = False,
    version: bool = False,
    copyright_: bool = False,
    help_: bool = False,
    debug: bool = False,
    report_maps: str | None = None,
    keep_meanvol: bool = False,
) -> MelodicParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file names (either single file name or\
            comma-separated list or text file).
        output_directory: Output directory name.
        mask_file: File name of mask for thresholding.
        dimensionality_reduction: Dimensionality reduction into specified\
            number of dimensions (default is automatic estimation).
        generate_report: Generate Melodic web report.
        cifti_io: Input/output as CIFTI (warning: auto-dimensionality\
            estimation for CIFTI data is currently inaccurate).
        variance_normalization: Switch off variance normalization.
        no_masking: Switch off masking.
        update_masking: Switch off mask updating.
        no_bet: Switch off BET.
        bg_threshold: Brain / non-brain threshold (only if --nobet selected).
        dimest_technique: Use specific dimensionality estimation technique:\
            lap, bic, mdl, aic, mean (default: lap).
        separate_variance_normalization: Switch on separate variance\
            normalization for each input dataset (off by default).
        disable_migp: Switch off MIGP data reduction when using -a concat (full\
            temporal concatenation will be used).
        num_internal_eigenmaps: Number of internal Eigenmaps.
        migp_shuffle: Randomize MIGP file order (default: TRUE).
        migp_factor: Internal Factor of mem-threshold relative to number of\
            Eigenmaps (default: 2).
        num_ics: Number of ICs to extract (for deflation approach).
        nonlinearity: Nonlinearity: gauss, tanh, pow3 (default), pow4.
        covar_weights: Voxel-wise weights for the covariance matrix (e.g.\
            segmentation information).
        eps_error: Minimum error change.
        eps_rank1_error: Minimum error change for rank-1 approximation in TICA.
        max_iters: Maximum number of iterations before restart.
        max_restarts: Maximum number of restarts.
        mm_threshold: Threshold for Mixture Model based inference.
        no_mixture_modeling: Switch off mixture modeling on IC maps.
        ic_components_file: Input filename of the IC components file for\
            mixture modeling.
        mixing_matrix_file: Input filename of mixing matrix for mixture\
            modeling / filtering.
        session_modes_file: Input filename of matrix of session modes for\
            report generation.
        component_filter: List of component numbers to remove.
        background_image: Specify background image for report (default: mean\
            image).
        tr_seconds: TR in seconds.
        log_power_calc: Calculate log of power for frequency spectrum.
        time_domain_design_matrix: Design matrix across time-domain.
        time_domain_t_contrast_matrix: T-contrast matrix across time-domain.
        subject_domain_design_matrix: Design matrix across subject-domain.
        subject_domain_t_contrast_matrix: T-contrast matrix across\
            subject-domain.
        output_unmixing_matrix: Output unmixing matrix.
        output_stats: Output thresholded maps and probability maps.
        output_pca: Output PCA results.
        output_whitening: Output whitening/dewhitening matrices.
        output_original_ics: Output the original ICs.
        output_mean_volume: Output mean volume.
        version: Prints version information.
        copyright_: Prints copyright information.
        help_: Prints this help message.
        debug: Switch on debug messages.
        report_maps: Control string for spatial map images (see slicer).
        keep_meanvol: Do not subtract mean volume.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "melodic",
        "input_file": input_file,
        "generate_report": generate_report,
        "cifti_io": cifti_io,
        "variance_normalization": variance_normalization,
        "no_masking": no_masking,
        "update_masking": update_masking,
        "no_bet": no_bet,
        "separate_variance_normalization": separate_variance_normalization,
        "disable_migp": disable_migp,
        "migp_shuffle": migp_shuffle,
        "no_mixture_modeling": no_mixture_modeling,
        "log_power_calc": log_power_calc,
        "output_unmixing_matrix": output_unmixing_matrix,
        "output_stats": output_stats,
        "output_pca": output_pca,
        "output_whitening": output_whitening,
        "output_original_ics": output_original_ics,
        "output_mean_volume": output_mean_volume,
        "version": version,
        "copyright": copyright_,
        "help": help_,
        "debug": debug,
        "keep_meanvol": keep_meanvol,
    }
    if output_directory is not None:
        params["output_directory"] = output_directory
    if mask_file is not None:
        params["mask_file"] = mask_file
    if dimensionality_reduction is not None:
        params["dimensionality_reduction"] = dimensionality_reduction
    if bg_threshold is not None:
        params["bg_threshold"] = bg_threshold
    if dimest_technique is not None:
        params["dimest_technique"] = dimest_technique
    if num_internal_eigenmaps is not None:
        params["num_internal_eigenmaps"] = num_internal_eigenmaps
    if migp_factor is not None:
        params["migp_factor"] = migp_factor
    if num_ics is not None:
        params["num_ics"] = num_ics
    if nonlinearity is not None:
        params["nonlinearity"] = nonlinearity
    if covar_weights is not None:
        params["covar_weights"] = covar_weights
    if eps_error is not None:
        params["eps_error"] = eps_error
    if eps_rank1_error is not None:
        params["eps_rank1_error"] = eps_rank1_error
    if max_iters is not None:
        params["max_iters"] = max_iters
    if max_restarts is not None:
        params["max_restarts"] = max_restarts
    if mm_threshold is not None:
        params["mm_threshold"] = mm_threshold
    if ic_components_file is not None:
        params["ic_components_file"] = ic_components_file
    if mixing_matrix_file is not None:
        params["mixing_matrix_file"] = mixing_matrix_file
    if session_modes_file is not None:
        params["session_modes_file"] = session_modes_file
    if component_filter is not None:
        params["component_filter"] = component_filter
    if background_image is not None:
        params["background_image"] = background_image
    if tr_seconds is not None:
        params["tr_seconds"] = tr_seconds
    if time_domain_design_matrix is not None:
        params["time_domain_design_matrix"] = time_domain_design_matrix
    if time_domain_t_contrast_matrix is not None:
        params["time_domain_t_contrast_matrix"] = time_domain_t_contrast_matrix
    if subject_domain_design_matrix is not None:
        params["subject_domain_design_matrix"] = subject_domain_design_matrix
    if subject_domain_t_contrast_matrix is not None:
        params["subject_domain_t_contrast_matrix"] = subject_domain_t_contrast_matrix
    if report_maps is not None:
        params["report_maps"] = report_maps
    return params


def melodic_cargs(
    params: MelodicParameters,
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
    cargs.append("melodic")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("output_directory") is not None:
        cargs.extend([
            "-o",
            params.get("output_directory")
        ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("dimensionality_reduction") is not None:
        cargs.extend([
            "-d",
            str(params.get("dimensionality_reduction"))
        ])
    if params.get("generate_report"):
        cargs.append("--report")
    if params.get("cifti_io"):
        cargs.append("--CIFTI")
    if params.get("variance_normalization"):
        cargs.append("--vn")
    if params.get("no_masking"):
        cargs.append("--nomask")
    if params.get("update_masking"):
        cargs.append("--update_mask")
    if params.get("no_bet"):
        cargs.append("--nobet")
    if params.get("bg_threshold") is not None:
        cargs.extend([
            "--bgthreshold",
            str(params.get("bg_threshold"))
        ])
    if params.get("dimest_technique") is not None:
        cargs.extend([
            "--dimest",
            params.get("dimest_technique")
        ])
    if params.get("separate_variance_normalization"):
        cargs.append("--sep_vn")
    if params.get("disable_migp"):
        cargs.append("--disableMigp")
    if params.get("num_internal_eigenmaps") is not None:
        cargs.extend([
            "--migpN",
            str(params.get("num_internal_eigenmaps"))
        ])
    if params.get("migp_shuffle"):
        cargs.append("--migp_shuffle")
    if params.get("migp_factor") is not None:
        cargs.extend([
            "--migp_factor",
            str(params.get("migp_factor"))
        ])
    if params.get("num_ics") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_ics"))
        ])
    if params.get("nonlinearity") is not None:
        cargs.extend([
            "--nl",
            params.get("nonlinearity")
        ])
    if params.get("covar_weights") is not None:
        cargs.extend([
            "--covarweight",
            execution.input_file(params.get("covar_weights"))
        ])
    if params.get("eps_error") is not None:
        cargs.extend([
            "--eps",
            str(params.get("eps_error"))
        ])
    if params.get("eps_rank1_error") is not None:
        cargs.extend([
            "--epsS",
            str(params.get("eps_rank1_error"))
        ])
    if params.get("max_iters") is not None:
        cargs.extend([
            "--maxit",
            str(params.get("max_iters"))
        ])
    if params.get("max_restarts") is not None:
        cargs.extend([
            "--maxrestart",
            str(params.get("max_restarts"))
        ])
    if params.get("mm_threshold") is not None:
        cargs.extend([
            "--mmthresh",
            str(params.get("mm_threshold"))
        ])
    if params.get("no_mixture_modeling"):
        cargs.append("--no_mm")
    if params.get("ic_components_file") is not None:
        cargs.extend([
            "--ICs",
            execution.input_file(params.get("ic_components_file"))
        ])
    if params.get("mixing_matrix_file") is not None:
        cargs.extend([
            "--mix",
            execution.input_file(params.get("mixing_matrix_file"))
        ])
    if params.get("session_modes_file") is not None:
        cargs.extend([
            "--smode",
            execution.input_file(params.get("session_modes_file"))
        ])
    if params.get("component_filter") is not None:
        cargs.extend([
            "-f",
            params.get("component_filter")
        ])
    if params.get("background_image") is not None:
        cargs.extend([
            "--bgimage",
            execution.input_file(params.get("background_image"))
        ])
    if params.get("tr_seconds") is not None:
        cargs.extend([
            "--tr",
            str(params.get("tr_seconds"))
        ])
    if params.get("log_power_calc"):
        cargs.append("--logPower")
    if params.get("time_domain_design_matrix") is not None:
        cargs.extend([
            "--Tdes",
            execution.input_file(params.get("time_domain_design_matrix"))
        ])
    if params.get("time_domain_t_contrast_matrix") is not None:
        cargs.extend([
            "--Tcon",
            execution.input_file(params.get("time_domain_t_contrast_matrix"))
        ])
    if params.get("subject_domain_design_matrix") is not None:
        cargs.extend([
            "--Sdes",
            execution.input_file(params.get("subject_domain_design_matrix"))
        ])
    if params.get("subject_domain_t_contrast_matrix") is not None:
        cargs.extend([
            "--Scon",
            execution.input_file(params.get("subject_domain_t_contrast_matrix"))
        ])
    if params.get("output_unmixing_matrix"):
        cargs.append("--Ounmix")
    if params.get("output_stats"):
        cargs.append("--Ostats")
    if params.get("output_pca"):
        cargs.append("--Opca")
    if params.get("output_whitening"):
        cargs.append("--Owhite")
    if params.get("output_original_ics"):
        cargs.append("--Oorig")
    if params.get("output_mean_volume"):
        cargs.append("--Omean")
    if params.get("version"):
        cargs.append("-V")
    if params.get("copyright"):
        cargs.append("--copyright")
    if params.get("help"):
        cargs.append("-h")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("report_maps") is not None:
        cargs.extend([
            "--report_maps",
            params.get("report_maps")
        ])
    if params.get("keep_meanvol"):
        cargs.append("--keep_meanvol")
    return cargs


def melodic_outputs(
    params: MelodicParameters,
    execution: Execution,
) -> MelodicOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MelodicOutputs(
        root=execution.output_file("."),
        report_file=execution.output_file(params.get("output_directory") + "/report.html") if (params.get("output_directory") is not None) else None,
        ics_output_file=execution.output_file(params.get("output_directory") + "/melodic_IC.nii.gz") if (params.get("output_directory") is not None) else None,
        mix_output_file=execution.output_file(params.get("output_directory") + "/melodic_mix") if (params.get("output_directory") is not None) else None,
        temporal_mode_file=execution.output_file(params.get("output_directory") + "/melodic_Tmodes") if (params.get("output_directory") is not None) else None,
        melodic_report_directory=execution.output_file(params.get("output_directory") + "/melodic_report") if (params.get("output_directory") is not None) else None,
    )
    return ret


def melodic_execute(
    params: MelodicParameters,
    execution: Execution,
) -> MelodicOutputs:
    """
    Multivariate Exploratory Linear Optimised Decomposition into Independent
    Components.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MelodicOutputs`).
    """
    params = execution.params(params)
    cargs = melodic_cargs(params, execution)
    ret = melodic_outputs(params, execution)
    execution.run(cargs)
    return ret


def melodic(
    input_file: InputPathType,
    output_directory: str | None = None,
    mask_file: InputPathType | None = None,
    dimensionality_reduction: float | None = None,
    generate_report: bool = False,
    cifti_io: bool = False,
    variance_normalization: bool = False,
    no_masking: bool = False,
    update_masking: bool = False,
    no_bet: bool = False,
    bg_threshold: float | None = None,
    dimest_technique: str | None = None,
    separate_variance_normalization: bool = False,
    disable_migp: bool = False,
    num_internal_eigenmaps: float | None = None,
    migp_shuffle: bool = False,
    migp_factor: float | None = None,
    num_ics: float | None = None,
    nonlinearity: str | None = None,
    covar_weights: InputPathType | None = None,
    eps_error: float | None = None,
    eps_rank1_error: float | None = None,
    max_iters: float | None = None,
    max_restarts: float | None = None,
    mm_threshold: float | None = None,
    no_mixture_modeling: bool = False,
    ic_components_file: InputPathType | None = None,
    mixing_matrix_file: InputPathType | None = None,
    session_modes_file: InputPathType | None = None,
    component_filter: str | None = None,
    background_image: InputPathType | None = None,
    tr_seconds: float | None = None,
    log_power_calc: bool = False,
    time_domain_design_matrix: InputPathType | None = None,
    time_domain_t_contrast_matrix: InputPathType | None = None,
    subject_domain_design_matrix: InputPathType | None = None,
    subject_domain_t_contrast_matrix: InputPathType | None = None,
    output_unmixing_matrix: bool = False,
    output_stats: bool = False,
    output_pca: bool = False,
    output_whitening: bool = False,
    output_original_ics: bool = False,
    output_mean_volume: bool = False,
    version: bool = False,
    copyright_: bool = False,
    help_: bool = False,
    debug: bool = False,
    report_maps: str | None = None,
    keep_meanvol: bool = False,
    runner: Runner | None = None,
) -> MelodicOutputs:
    """
    Multivariate Exploratory Linear Optimised Decomposition into Independent
    Components.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file names (either single file name or\
            comma-separated list or text file).
        output_directory: Output directory name.
        mask_file: File name of mask for thresholding.
        dimensionality_reduction: Dimensionality reduction into specified\
            number of dimensions (default is automatic estimation).
        generate_report: Generate Melodic web report.
        cifti_io: Input/output as CIFTI (warning: auto-dimensionality\
            estimation for CIFTI data is currently inaccurate).
        variance_normalization: Switch off variance normalization.
        no_masking: Switch off masking.
        update_masking: Switch off mask updating.
        no_bet: Switch off BET.
        bg_threshold: Brain / non-brain threshold (only if --nobet selected).
        dimest_technique: Use specific dimensionality estimation technique:\
            lap, bic, mdl, aic, mean (default: lap).
        separate_variance_normalization: Switch on separate variance\
            normalization for each input dataset (off by default).
        disable_migp: Switch off MIGP data reduction when using -a concat (full\
            temporal concatenation will be used).
        num_internal_eigenmaps: Number of internal Eigenmaps.
        migp_shuffle: Randomize MIGP file order (default: TRUE).
        migp_factor: Internal Factor of mem-threshold relative to number of\
            Eigenmaps (default: 2).
        num_ics: Number of ICs to extract (for deflation approach).
        nonlinearity: Nonlinearity: gauss, tanh, pow3 (default), pow4.
        covar_weights: Voxel-wise weights for the covariance matrix (e.g.\
            segmentation information).
        eps_error: Minimum error change.
        eps_rank1_error: Minimum error change for rank-1 approximation in TICA.
        max_iters: Maximum number of iterations before restart.
        max_restarts: Maximum number of restarts.
        mm_threshold: Threshold for Mixture Model based inference.
        no_mixture_modeling: Switch off mixture modeling on IC maps.
        ic_components_file: Input filename of the IC components file for\
            mixture modeling.
        mixing_matrix_file: Input filename of mixing matrix for mixture\
            modeling / filtering.
        session_modes_file: Input filename of matrix of session modes for\
            report generation.
        component_filter: List of component numbers to remove.
        background_image: Specify background image for report (default: mean\
            image).
        tr_seconds: TR in seconds.
        log_power_calc: Calculate log of power for frequency spectrum.
        time_domain_design_matrix: Design matrix across time-domain.
        time_domain_t_contrast_matrix: T-contrast matrix across time-domain.
        subject_domain_design_matrix: Design matrix across subject-domain.
        subject_domain_t_contrast_matrix: T-contrast matrix across\
            subject-domain.
        output_unmixing_matrix: Output unmixing matrix.
        output_stats: Output thresholded maps and probability maps.
        output_pca: Output PCA results.
        output_whitening: Output whitening/dewhitening matrices.
        output_original_ics: Output the original ICs.
        output_mean_volume: Output mean volume.
        version: Prints version information.
        copyright_: Prints copyright information.
        help_: Prints this help message.
        debug: Switch on debug messages.
        report_maps: Control string for spatial map images (see slicer).
        keep_meanvol: Do not subtract mean volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MelodicOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MELODIC_METADATA)
    params = melodic_params(input_file=input_file, output_directory=output_directory, mask_file=mask_file, dimensionality_reduction=dimensionality_reduction, generate_report=generate_report, cifti_io=cifti_io, variance_normalization=variance_normalization, no_masking=no_masking, update_masking=update_masking, no_bet=no_bet, bg_threshold=bg_threshold, dimest_technique=dimest_technique, separate_variance_normalization=separate_variance_normalization, disable_migp=disable_migp, num_internal_eigenmaps=num_internal_eigenmaps, migp_shuffle=migp_shuffle, migp_factor=migp_factor, num_ics=num_ics, nonlinearity=nonlinearity, covar_weights=covar_weights, eps_error=eps_error, eps_rank1_error=eps_rank1_error, max_iters=max_iters, max_restarts=max_restarts, mm_threshold=mm_threshold, no_mixture_modeling=no_mixture_modeling, ic_components_file=ic_components_file, mixing_matrix_file=mixing_matrix_file, session_modes_file=session_modes_file, component_filter=component_filter, background_image=background_image, tr_seconds=tr_seconds, log_power_calc=log_power_calc, time_domain_design_matrix=time_domain_design_matrix, time_domain_t_contrast_matrix=time_domain_t_contrast_matrix, subject_domain_design_matrix=subject_domain_design_matrix, subject_domain_t_contrast_matrix=subject_domain_t_contrast_matrix, output_unmixing_matrix=output_unmixing_matrix, output_stats=output_stats, output_pca=output_pca, output_whitening=output_whitening, output_original_ics=output_original_ics, output_mean_volume=output_mean_volume, version=version, copyright_=copyright_, help_=help_, debug=debug, report_maps=report_maps, keep_meanvol=keep_meanvol)
    return melodic_execute(params, execution)


__all__ = [
    "MELODIC_METADATA",
    "MelodicOutputs",
    "MelodicParameters",
    "melodic",
    "melodic_params",
]
