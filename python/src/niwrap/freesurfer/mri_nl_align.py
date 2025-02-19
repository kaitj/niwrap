# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_NL_ALIGN_METADATA = Metadata(
    id="cd2a19b23e2fec00175500358afe679cc9ee7fc7.boutiques",
    name="mri_nl_align",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriNlAlignParameters = typing.TypedDict('MriNlAlignParameters', {
    "__STYX_TYPE__": typing.Literal["mri_nl_align"],
    "source": InputPathType,
    "target": InputPathType,
    "warp": str,
    "debug_voxel": typing.NotRequired[list[float] | None],
    "debug_node": typing.NotRequired[list[float] | None],
    "no_neg": typing.NotRequired[float | None],
    "renormalize": typing.NotRequired[float | None],
    "aseg_flag": bool,
    "diag_volume": typing.NotRequired[str | None],
    "optimal_flag": bool,
    "momentum_flag": bool,
    "fixed_flag": bool,
    "distance": typing.NotRequired[float | None],
    "dtrans": typing.NotRequired[float | None],
    "match_peak_flag": bool,
    "erode": typing.NotRequired[float | None],
    "match_mean": typing.NotRequired[float | None],
    "intensity": typing.NotRequired[float | None],
    "noregrid_flag": bool,
    "regrid_flag": bool,
    "view": typing.NotRequired[list[float] | None],
    "levels": typing.NotRequired[float | None],
    "area_smoothness": typing.NotRequired[float | None],
    "area": typing.NotRequired[float | None],
    "tolerance": typing.NotRequired[float | None],
    "sigma": typing.NotRequired[float | None],
    "min_sigma": typing.NotRequired[float | None],
    "ribbon": typing.NotRequired[InputPathType | None],
    "rthresh": typing.NotRequired[float | None],
    "scale": typing.NotRequired[float | None],
    "dt": typing.NotRequired[float | None],
    "passes": typing.NotRequired[float | None],
    "skip": typing.NotRequired[float | None],
    "apply": typing.NotRequired[float | None],
    "distance_log": typing.NotRequired[float | None],
    "momentum": typing.NotRequired[float | None],
    "iterations": typing.NotRequired[float | None],
    "smoothness": typing.NotRequired[float | None],
    "transform": typing.NotRequired[InputPathType | None],
    "inverse_transform": typing.NotRequired[InputPathType | None],
    "binary": typing.NotRequired[float | None],
    "jacobian": typing.NotRequired[float | None],
    "disable_zero_locations": typing.NotRequired[float | None],
    "smooth_averages": typing.NotRequired[float | None],
    "exp_k": typing.NotRequired[float | None],
    "diagnostics": typing.NotRequired[float | None],
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
        "mri_nl_align": mri_nl_align_cargs,
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
        "mri_nl_align": mri_nl_align_outputs,
    }.get(t)


class MriNlAlignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_nl_align(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warp_output: OutputPathType
    """Resulting warp output file after alignment"""


def mri_nl_align_params(
    source: InputPathType,
    target: InputPathType,
    warp: str,
    debug_voxel: list[float] | None = None,
    debug_node: list[float] | None = None,
    no_neg: float | None = None,
    renormalize: float | None = None,
    aseg_flag: bool = False,
    diag_volume: str | None = None,
    optimal_flag: bool = False,
    momentum_flag: bool = False,
    fixed_flag: bool = False,
    distance: float | None = None,
    dtrans: float | None = None,
    match_peak_flag: bool = False,
    erode: float | None = None,
    match_mean: float | None = None,
    intensity: float | None = None,
    noregrid_flag: bool = False,
    regrid_flag: bool = False,
    view: list[float] | None = None,
    levels: float | None = None,
    area_smoothness: float | None = None,
    area: float | None = None,
    tolerance: float | None = None,
    sigma: float | None = None,
    min_sigma: float | None = None,
    ribbon: InputPathType | None = None,
    rthresh: float | None = None,
    scale: float | None = None,
    dt: float | None = None,
    passes: float | None = None,
    skip: float | None = None,
    apply: float | None = None,
    distance_log: float | None = None,
    momentum: float | None = None,
    iterations: float | None = None,
    smoothness: float | None = None,
    transform: InputPathType | None = None,
    inverse_transform: InputPathType | None = None,
    binary: float | None = None,
    jacobian: float | None = None,
    disable_zero_locations: float | None = None,
    smooth_averages: float | None = None,
    exp_k: float | None = None,
    diagnostics: float | None = None,
) -> MriNlAlignParameters:
    """
    Build parameters.
    
    Args:
        source: Input source image file.
        target: Input target image file.
        warp: Output warp file.
        debug_voxel: Debug voxel coordinates (Gx, Gy, Gz).
        debug_node: Debug node coordinates (Gx, Gy, Gz).
        no_neg: Control allowing temporary folds during numerical minimization.
        renormalize: Control for renormalizing intensities.
        aseg_flag: Treat inputs as segmentations.
        diag_volume: Write d2 diagnostics for input volume.
        optimal_flag: Use line search optimization.
        momentum_flag: Use fixed time-step integration.
        fixed_flag: Use fixed time-step integration.
        distance: Expand border by specified mm every outer cycle.
        dtrans: Set distance transform coefficient.
        match_peak_flag: Match peak of intensity ratio histogram.
        erode: Erode source and target image specified times before morphing.
        match_mean: Control for matching peak of intensity ratio histogram.
        intensity: Set l_log_likelihood to specified value.
        noregrid_flag: Disable regridding.
        regrid_flag: Enable regridding.
        view: View voxel coordinates (Gx, Gy, Gz).
        levels: Set levels to specified value.
        area_smoothness: Set l_area_smoothness to specified value.
        area: Set l_area to specified value.
        tolerance: Set tolerance to specified value.
        sigma: Set sigma to specified value.
        min_sigma: Set minimum sigma value.
        ribbon: Read ribbon from specified file and insert into aseg.
        rthresh: Set compression ratio threshold to specified value.
        scale: Scale input values by specified factor.
        dt: Set dt to specified value.
        passes: Integrate in specified number of passes.
        skip: Skip specified number of voxels in source data.
        apply: Control for applying transform after registration.
        distance_log: Set l_distance to specified value.
        momentum: Set momentum to specified value.
        iterations: Set number of iterations to specified value.
        smoothness: Set l_smoothness to specified value.
        transform: Read the forward transform from specified file.
        inverse_transform: Read the inverse transform from specified file.
        binary: Set l_binary to specified value.
        jacobian: Set l_jacobian to specified value.
        disable_zero_locations: Control for disabling zero image locations.
        smooth_averages: Smooth gradient with specified number of averages.
        exp_k: Set exp_k to specified value.
        diagnostics: Write diagnostics at each specified iteration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_nl_align",
        "source": source,
        "target": target,
        "warp": warp,
        "aseg_flag": aseg_flag,
        "optimal_flag": optimal_flag,
        "momentum_flag": momentum_flag,
        "fixed_flag": fixed_flag,
        "match_peak_flag": match_peak_flag,
        "noregrid_flag": noregrid_flag,
        "regrid_flag": regrid_flag,
    }
    if debug_voxel is not None:
        params["debug_voxel"] = debug_voxel
    if debug_node is not None:
        params["debug_node"] = debug_node
    if no_neg is not None:
        params["no_neg"] = no_neg
    if renormalize is not None:
        params["renormalize"] = renormalize
    if diag_volume is not None:
        params["diag_volume"] = diag_volume
    if distance is not None:
        params["distance"] = distance
    if dtrans is not None:
        params["dtrans"] = dtrans
    if erode is not None:
        params["erode"] = erode
    if match_mean is not None:
        params["match_mean"] = match_mean
    if intensity is not None:
        params["intensity"] = intensity
    if view is not None:
        params["view"] = view
    if levels is not None:
        params["levels"] = levels
    if area_smoothness is not None:
        params["area_smoothness"] = area_smoothness
    if area is not None:
        params["area"] = area
    if tolerance is not None:
        params["tolerance"] = tolerance
    if sigma is not None:
        params["sigma"] = sigma
    if min_sigma is not None:
        params["min_sigma"] = min_sigma
    if ribbon is not None:
        params["ribbon"] = ribbon
    if rthresh is not None:
        params["rthresh"] = rthresh
    if scale is not None:
        params["scale"] = scale
    if dt is not None:
        params["dt"] = dt
    if passes is not None:
        params["passes"] = passes
    if skip is not None:
        params["skip"] = skip
    if apply is not None:
        params["apply"] = apply
    if distance_log is not None:
        params["distance_log"] = distance_log
    if momentum is not None:
        params["momentum"] = momentum
    if iterations is not None:
        params["iterations"] = iterations
    if smoothness is not None:
        params["smoothness"] = smoothness
    if transform is not None:
        params["transform"] = transform
    if inverse_transform is not None:
        params["inverse_transform"] = inverse_transform
    if binary is not None:
        params["binary"] = binary
    if jacobian is not None:
        params["jacobian"] = jacobian
    if disable_zero_locations is not None:
        params["disable_zero_locations"] = disable_zero_locations
    if smooth_averages is not None:
        params["smooth_averages"] = smooth_averages
    if exp_k is not None:
        params["exp_k"] = exp_k
    if diagnostics is not None:
        params["diagnostics"] = diagnostics
    return params


def mri_nl_align_cargs(
    params: MriNlAlignParameters,
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
    cargs.append("mri_nl_align")
    cargs.append(execution.input_file(params.get("source")))
    cargs.append(execution.input_file(params.get("target")))
    cargs.append(params.get("warp"))
    if params.get("debug_voxel") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel"))
        ])
    if params.get("debug_node") is not None:
        cargs.extend([
            "-debug_node",
            *map(str, params.get("debug_node"))
        ])
    if params.get("no_neg") is not None:
        cargs.extend([
            "-noneg",
            str(params.get("no_neg"))
        ])
    if params.get("renormalize") is not None:
        cargs.extend([
            "-renormalize",
            str(params.get("renormalize"))
        ])
    if params.get("aseg_flag"):
        cargs.append("-aseg")
    if params.get("diag_volume") is not None:
        cargs.extend([
            "-diag2",
            params.get("diag_volume")
        ])
    if params.get("optimal_flag"):
        cargs.append("-OPTIMAL")
    if params.get("momentum_flag"):
        cargs.append("-MOMENTUM")
    if params.get("fixed_flag"):
        cargs.append("-FIXED")
    if params.get("distance") is not None:
        cargs.extend([
            "-distance",
            str(params.get("distance"))
        ])
    if params.get("dtrans") is not None:
        cargs.extend([
            "-dtrans",
            str(params.get("dtrans"))
        ])
    if params.get("match_peak_flag"):
        cargs.append("-match_peak")
    if params.get("erode") is not None:
        cargs.extend([
            "-erode",
            str(params.get("erode"))
        ])
    if params.get("match_mean") is not None:
        cargs.extend([
            "-match_mean",
            str(params.get("match_mean"))
        ])
    if params.get("intensity") is not None:
        cargs.extend([
            "-intensity",
            str(params.get("intensity"))
        ])
    if params.get("noregrid_flag"):
        cargs.append("-noregrid")
    if params.get("regrid_flag"):
        cargs.append("-regrid")
    if params.get("view") is not None:
        cargs.extend([
            "-view",
            *map(str, params.get("view"))
        ])
    if params.get("levels") is not None:
        cargs.extend([
            "-levels",
            str(params.get("levels"))
        ])
    if params.get("area_smoothness") is not None:
        cargs.extend([
            "-areasmoothness",
            str(params.get("area_smoothness"))
        ])
    if params.get("area") is not None:
        cargs.extend([
            "-area",
            str(params.get("area"))
        ])
    if params.get("tolerance") is not None:
        cargs.extend([
            "-tol",
            str(params.get("tolerance"))
        ])
    if params.get("sigma") is not None:
        cargs.extend([
            "-sigma",
            str(params.get("sigma"))
        ])
    if params.get("min_sigma") is not None:
        cargs.extend([
            "-min_sigma",
            str(params.get("min_sigma"))
        ])
    if params.get("ribbon") is not None:
        cargs.extend([
            "-ribbon",
            execution.input_file(params.get("ribbon"))
        ])
    if params.get("rthresh") is not None:
        cargs.extend([
            "-rthresh",
            str(params.get("rthresh"))
        ])
    if params.get("scale") is not None:
        cargs.extend([
            "-scale",
            str(params.get("scale"))
        ])
    if params.get("dt") is not None:
        cargs.extend([
            "-dt",
            str(params.get("dt"))
        ])
    if params.get("passes") is not None:
        cargs.extend([
            "-passes",
            str(params.get("passes"))
        ])
    if params.get("skip") is not None:
        cargs.extend([
            "-skip",
            str(params.get("skip"))
        ])
    if params.get("apply") is not None:
        cargs.extend([
            "-apply",
            str(params.get("apply"))
        ])
    if params.get("distance_log") is not None:
        cargs.extend([
            "-D",
            str(params.get("distance_log"))
        ])
    if params.get("momentum") is not None:
        cargs.extend([
            "-M",
            str(params.get("momentum"))
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "-N",
            str(params.get("iterations"))
        ])
    if params.get("smoothness") is not None:
        cargs.extend([
            "-s",
            str(params.get("smoothness"))
        ])
    if params.get("transform") is not None:
        cargs.extend([
            "-T",
            execution.input_file(params.get("transform"))
        ])
    if params.get("inverse_transform") is not None:
        cargs.extend([
            "-I",
            execution.input_file(params.get("inverse_transform"))
        ])
    if params.get("binary") is not None:
        cargs.extend([
            "-B",
            str(params.get("binary"))
        ])
    if params.get("jacobian") is not None:
        cargs.extend([
            "-J",
            str(params.get("jacobian"))
        ])
    if params.get("disable_zero_locations") is not None:
        cargs.extend([
            "-Z",
            str(params.get("disable_zero_locations"))
        ])
    if params.get("smooth_averages") is not None:
        cargs.extend([
            "-a",
            str(params.get("smooth_averages"))
        ])
    if params.get("exp_k") is not None:
        cargs.extend([
            "-K",
            str(params.get("exp_k"))
        ])
    if params.get("diagnostics") is not None:
        cargs.extend([
            "-W",
            str(params.get("diagnostics"))
        ])
    return cargs


def mri_nl_align_outputs(
    params: MriNlAlignParameters,
    execution: Execution,
) -> MriNlAlignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriNlAlignOutputs(
        root=execution.output_file("."),
        warp_output=execution.output_file(params.get("warp")),
    )
    return ret


def mri_nl_align_execute(
    params: MriNlAlignParameters,
    execution: Execution,
) -> MriNlAlignOutputs:
    """
    mri_nl_align aligns two images using nonlinear registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriNlAlignOutputs`).
    """
    params = execution.params(params)
    cargs = mri_nl_align_cargs(params, execution)
    ret = mri_nl_align_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_nl_align(
    source: InputPathType,
    target: InputPathType,
    warp: str,
    debug_voxel: list[float] | None = None,
    debug_node: list[float] | None = None,
    no_neg: float | None = None,
    renormalize: float | None = None,
    aseg_flag: bool = False,
    diag_volume: str | None = None,
    optimal_flag: bool = False,
    momentum_flag: bool = False,
    fixed_flag: bool = False,
    distance: float | None = None,
    dtrans: float | None = None,
    match_peak_flag: bool = False,
    erode: float | None = None,
    match_mean: float | None = None,
    intensity: float | None = None,
    noregrid_flag: bool = False,
    regrid_flag: bool = False,
    view: list[float] | None = None,
    levels: float | None = None,
    area_smoothness: float | None = None,
    area: float | None = None,
    tolerance: float | None = None,
    sigma: float | None = None,
    min_sigma: float | None = None,
    ribbon: InputPathType | None = None,
    rthresh: float | None = None,
    scale: float | None = None,
    dt: float | None = None,
    passes: float | None = None,
    skip: float | None = None,
    apply: float | None = None,
    distance_log: float | None = None,
    momentum: float | None = None,
    iterations: float | None = None,
    smoothness: float | None = None,
    transform: InputPathType | None = None,
    inverse_transform: InputPathType | None = None,
    binary: float | None = None,
    jacobian: float | None = None,
    disable_zero_locations: float | None = None,
    smooth_averages: float | None = None,
    exp_k: float | None = None,
    diagnostics: float | None = None,
    runner: Runner | None = None,
) -> MriNlAlignOutputs:
    """
    mri_nl_align aligns two images using nonlinear registration.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source: Input source image file.
        target: Input target image file.
        warp: Output warp file.
        debug_voxel: Debug voxel coordinates (Gx, Gy, Gz).
        debug_node: Debug node coordinates (Gx, Gy, Gz).
        no_neg: Control allowing temporary folds during numerical minimization.
        renormalize: Control for renormalizing intensities.
        aseg_flag: Treat inputs as segmentations.
        diag_volume: Write d2 diagnostics for input volume.
        optimal_flag: Use line search optimization.
        momentum_flag: Use fixed time-step integration.
        fixed_flag: Use fixed time-step integration.
        distance: Expand border by specified mm every outer cycle.
        dtrans: Set distance transform coefficient.
        match_peak_flag: Match peak of intensity ratio histogram.
        erode: Erode source and target image specified times before morphing.
        match_mean: Control for matching peak of intensity ratio histogram.
        intensity: Set l_log_likelihood to specified value.
        noregrid_flag: Disable regridding.
        regrid_flag: Enable regridding.
        view: View voxel coordinates (Gx, Gy, Gz).
        levels: Set levels to specified value.
        area_smoothness: Set l_area_smoothness to specified value.
        area: Set l_area to specified value.
        tolerance: Set tolerance to specified value.
        sigma: Set sigma to specified value.
        min_sigma: Set minimum sigma value.
        ribbon: Read ribbon from specified file and insert into aseg.
        rthresh: Set compression ratio threshold to specified value.
        scale: Scale input values by specified factor.
        dt: Set dt to specified value.
        passes: Integrate in specified number of passes.
        skip: Skip specified number of voxels in source data.
        apply: Control for applying transform after registration.
        distance_log: Set l_distance to specified value.
        momentum: Set momentum to specified value.
        iterations: Set number of iterations to specified value.
        smoothness: Set l_smoothness to specified value.
        transform: Read the forward transform from specified file.
        inverse_transform: Read the inverse transform from specified file.
        binary: Set l_binary to specified value.
        jacobian: Set l_jacobian to specified value.
        disable_zero_locations: Control for disabling zero image locations.
        smooth_averages: Smooth gradient with specified number of averages.
        exp_k: Set exp_k to specified value.
        diagnostics: Write diagnostics at each specified iteration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriNlAlignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_NL_ALIGN_METADATA)
    params = mri_nl_align_params(source=source, target=target, warp=warp, debug_voxel=debug_voxel, debug_node=debug_node, no_neg=no_neg, renormalize=renormalize, aseg_flag=aseg_flag, diag_volume=diag_volume, optimal_flag=optimal_flag, momentum_flag=momentum_flag, fixed_flag=fixed_flag, distance=distance, dtrans=dtrans, match_peak_flag=match_peak_flag, erode=erode, match_mean=match_mean, intensity=intensity, noregrid_flag=noregrid_flag, regrid_flag=regrid_flag, view=view, levels=levels, area_smoothness=area_smoothness, area=area, tolerance=tolerance, sigma=sigma, min_sigma=min_sigma, ribbon=ribbon, rthresh=rthresh, scale=scale, dt=dt, passes=passes, skip=skip, apply=apply, distance_log=distance_log, momentum=momentum, iterations=iterations, smoothness=smoothness, transform=transform, inverse_transform=inverse_transform, binary=binary, jacobian=jacobian, disable_zero_locations=disable_zero_locations, smooth_averages=smooth_averages, exp_k=exp_k, diagnostics=diagnostics)
    return mri_nl_align_execute(params, execution)


__all__ = [
    "MRI_NL_ALIGN_METADATA",
    "MriNlAlignOutputs",
    "MriNlAlignParameters",
    "mri_nl_align",
    "mri_nl_align_params",
]
