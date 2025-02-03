# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_MOTION_CORR_METADATA = Metadata(
    id="101179d7b402b3245503ed337e9b9c5479b1f966.boutiques",
    name="antsMotionCorr",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsMotionCorrParameters = typing.TypedDict('AntsMotionCorrParameters', {
    "__STYX_TYPE__": typing.Literal["antsMotionCorr"],
    "dimensionality": typing.NotRequired[typing.Literal[2, 3] | None],
    "n_images": typing.NotRequired[int | None],
    "metric": typing.NotRequired[str | None],
    "use_fixed_reference_image": typing.NotRequired[typing.Literal[0, 1] | None],
    "use_scales_estimator": bool,
    "transform": typing.NotRequired[str | None],
    "iterations": typing.NotRequired[str | None],
    "smoothing_sigmas": typing.NotRequired[str | None],
    "shrink_factors": typing.NotRequired[str | None],
    "output": typing.NotRequired[str | None],
    "average_image": bool,
    "write_displacement": bool,
    "use_histogram_matching": typing.NotRequired[typing.Literal[0, 1] | None],
    "random_seed": typing.NotRequired[int | None],
    "interpolation": typing.NotRequired[typing.Literal["Linear", "NearestNeighbor", "BSpline", "BlackmanWindowedSinc", "CosineWindowedSinc", "WelchWindowedSinc", "HammingWindowedSinc", "LanczosWindowedSinc"] | None],
    "verbose": typing.NotRequired[typing.Literal[0, 1] | None],
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
        "antsMotionCorr": ants_motion_corr_cargs,
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
        "antsMotionCorr": ants_motion_corr_outputs,
    }
    return vt.get(t)


class AntsMotionCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_motion_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform_prefix: OutputPathType
    """The output is the transformation matrix."""
    warped_image: OutputPathType
    """The output is the warped moving image."""
    average_image_output: OutputPathType
    """The output is the averaged image of the input time series."""


def ants_motion_corr_params(
    dimensionality: typing.Literal[2, 3] | None = None,
    n_images: int | None = None,
    metric: str | None = None,
    use_fixed_reference_image: typing.Literal[0, 1] | None = None,
    use_scales_estimator: bool = False,
    transform: str | None = None,
    iterations: str | None = None,
    smoothing_sigmas: str | None = None,
    shrink_factors: str | None = None,
    output: str | None = None,
    average_image: bool = False,
    write_displacement: bool = False,
    use_histogram_matching: typing.Literal[0, 1] | None = None,
    random_seed: int | None = None,
    interpolation: typing.Literal["Linear", "NearestNeighbor", "BSpline", "BlackmanWindowedSinc", "CosineWindowedSinc", "WelchWindowedSinc", "HammingWindowedSinc", "LanczosWindowedSinc"] | None = None,
    verbose: typing.Literal[0, 1] | None = None,
) -> AntsMotionCorrParameters:
    """
    Build parameters.
    
    Args:
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        n_images: This option sets the number of images to use to construct the\
            template image.
        metric: Metrics for registration: GC (global correlation), CC (ANTS\
            neighborhood cross correlation), MI (Mutual information), and Demons.
        use_fixed_reference_image: Use a fixed reference image to correct all\
            volumes, instead of correcting each image to the prior volume in the\
            time series.
        use_scales_estimator: Use the scale estimator to control optimization.
        transform: Several transform options are available: Affine, Rigid,\
            GaussianDisplacementField, SyN.
        iterations: Specify the number of iterations at each level.
        smoothing_sigmas: Specify the sigma for smoothing at each level.\
            Smoothing may be specified in mm units or voxels with 'AxBxCmm' or\
            'AxBxCvox'. No units implies voxels.
        shrink_factors: Specify the shrink factor for the virtual domain\
            (typically the fixed image) at each level.
        output: Specify the output transform prefix (output format is .nii.gz\
            ). Optionally, one can choose to warp the moving image to the fixed\
            space and, if the inverse transform exists, one can also output the\
            warped fixed image.
        average_image: Average the input time series image.
        write_displacement: Write the low-dimensional 3D transforms to a 4D\
            displacement field.
        use_histogram_matching: Histogram match the moving images to the\
            reference image.
        random_seed: Use a fixed seed for random number generation.
        interpolation: Several interpolation options are available in ITK. The\
            above are available (default Linear).
        verbose: Verbose output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsMotionCorr",
        "use_scales_estimator": use_scales_estimator,
        "average_image": average_image,
        "write_displacement": write_displacement,
    }
    if dimensionality is not None:
        params["dimensionality"] = dimensionality
    if n_images is not None:
        params["n_images"] = n_images
    if metric is not None:
        params["metric"] = metric
    if use_fixed_reference_image is not None:
        params["use_fixed_reference_image"] = use_fixed_reference_image
    if transform is not None:
        params["transform"] = transform
    if iterations is not None:
        params["iterations"] = iterations
    if smoothing_sigmas is not None:
        params["smoothing_sigmas"] = smoothing_sigmas
    if shrink_factors is not None:
        params["shrink_factors"] = shrink_factors
    if output is not None:
        params["output"] = output
    if use_histogram_matching is not None:
        params["use_histogram_matching"] = use_histogram_matching
    if random_seed is not None:
        params["random_seed"] = random_seed
    if interpolation is not None:
        params["interpolation"] = interpolation
    if verbose is not None:
        params["verbose"] = verbose
    return params


def ants_motion_corr_cargs(
    params: AntsMotionCorrParameters,
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
    cargs.append("antsMotionCorr")
    if params.get("dimensionality") is not None:
        cargs.extend([
            "--dimensionality",
            str(params.get("dimensionality"))
        ])
    if params.get("n_images") is not None:
        cargs.extend([
            "--n-images",
            str(params.get("n_images"))
        ])
    if params.get("metric") is not None:
        cargs.extend([
            "--metric",
            params.get("metric")
        ])
    if params.get("use_fixed_reference_image") is not None:
        cargs.extend([
            "--useFixedReferenceImage",
            str(params.get("use_fixed_reference_image"))
        ])
    if params.get("use_scales_estimator"):
        cargs.append("--useScalesEstimator")
    if params.get("transform") is not None:
        cargs.extend([
            "--transform",
            params.get("transform")
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "--iterations",
            params.get("iterations")
        ])
    if params.get("smoothing_sigmas") is not None:
        cargs.extend([
            "--smoothingSigmas",
            params.get("smoothing_sigmas")
        ])
    if params.get("shrink_factors") is not None:
        cargs.extend([
            "--shrinkFactors",
            params.get("shrink_factors")
        ])
    if params.get("output") is not None:
        cargs.extend([
            "--output",
            params.get("output")
        ])
    if params.get("average_image"):
        cargs.append("--average-image")
    if params.get("write_displacement"):
        cargs.append("--write-displacement")
    if params.get("use_histogram_matching") is not None:
        cargs.extend([
            "--use-histogram-matching",
            str(params.get("use_histogram_matching"))
        ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "--random-seed",
            str(params.get("random_seed"))
        ])
    if params.get("interpolation") is not None:
        cargs.extend([
            "--interpolation",
            params.get("interpolation")
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "--verbose",
            str(params.get("verbose"))
        ])
    return cargs


def ants_motion_corr_outputs(
    params: AntsMotionCorrParameters,
    execution: Execution,
) -> AntsMotionCorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsMotionCorrOutputs(
        root=execution.output_file("."),
        output_transform_prefix=execution.output_file("[OUTPUT_TRANSFORM_PREFIX]Affine.mat"),
        warped_image=execution.output_file("[OUTPUT_TRANSFORM_PREFIX]Warped.nii.gz"),
        average_image_output=execution.output_file("[OUTPUT_TRANSFORM_PREFIX]Average.nii.gz"),
    )
    return ret


def ants_motion_corr_execute(
    params: AntsMotionCorrParameters,
    execution: Execution,
) -> AntsMotionCorrOutputs:
    """
    ANTS Motion Correction application to perform motion correction on 4D time
    series data.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_motion_corr_cargs(params, execution)
    ret = ants_motion_corr_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_motion_corr(
    dimensionality: typing.Literal[2, 3] | None = None,
    n_images: int | None = None,
    metric: str | None = None,
    use_fixed_reference_image: typing.Literal[0, 1] | None = None,
    use_scales_estimator: bool = False,
    transform: str | None = None,
    iterations: str | None = None,
    smoothing_sigmas: str | None = None,
    shrink_factors: str | None = None,
    output: str | None = None,
    average_image: bool = False,
    write_displacement: bool = False,
    use_histogram_matching: typing.Literal[0, 1] | None = None,
    random_seed: int | None = None,
    interpolation: typing.Literal["Linear", "NearestNeighbor", "BSpline", "BlackmanWindowedSinc", "CosineWindowedSinc", "WelchWindowedSinc", "HammingWindowedSinc", "LanczosWindowedSinc"] | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AntsMotionCorrOutputs:
    """
    ANTS Motion Correction application to perform motion correction on 4D time
    series data.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        n_images: This option sets the number of images to use to construct the\
            template image.
        metric: Metrics for registration: GC (global correlation), CC (ANTS\
            neighborhood cross correlation), MI (Mutual information), and Demons.
        use_fixed_reference_image: Use a fixed reference image to correct all\
            volumes, instead of correcting each image to the prior volume in the\
            time series.
        use_scales_estimator: Use the scale estimator to control optimization.
        transform: Several transform options are available: Affine, Rigid,\
            GaussianDisplacementField, SyN.
        iterations: Specify the number of iterations at each level.
        smoothing_sigmas: Specify the sigma for smoothing at each level.\
            Smoothing may be specified in mm units or voxels with 'AxBxCmm' or\
            'AxBxCvox'. No units implies voxels.
        shrink_factors: Specify the shrink factor for the virtual domain\
            (typically the fixed image) at each level.
        output: Specify the output transform prefix (output format is .nii.gz\
            ). Optionally, one can choose to warp the moving image to the fixed\
            space and, if the inverse transform exists, one can also output the\
            warped fixed image.
        average_image: Average the input time series image.
        write_displacement: Write the low-dimensional 3D transforms to a 4D\
            displacement field.
        use_histogram_matching: Histogram match the moving images to the\
            reference image.
        random_seed: Use a fixed seed for random number generation.
        interpolation: Several interpolation options are available in ITK. The\
            above are available (default Linear).
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsMotionCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_MOTION_CORR_METADATA)
    params = ants_motion_corr_params(dimensionality=dimensionality, n_images=n_images, metric=metric, use_fixed_reference_image=use_fixed_reference_image, use_scales_estimator=use_scales_estimator, transform=transform, iterations=iterations, smoothing_sigmas=smoothing_sigmas, shrink_factors=shrink_factors, output=output, average_image=average_image, write_displacement=write_displacement, use_histogram_matching=use_histogram_matching, random_seed=random_seed, interpolation=interpolation, verbose=verbose)
    return ants_motion_corr_execute(params, execution)


__all__ = [
    "ANTS_MOTION_CORR_METADATA",
    "AntsMotionCorrOutputs",
    "ants_motion_corr",
    "ants_motion_corr_params",
]
