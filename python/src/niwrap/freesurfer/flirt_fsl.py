# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FLIRT_FSL_METADATA = Metadata(
    id="398eadb6f9dd1993cfd24de7b26c3a35c5d0f1cd.boutiques",
    name="flirt.fsl",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FlirtFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt_fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_volume: OutputPathType | None
    """Resulting registered volume"""
    transformation_matrix: OutputPathType | None
    """Resulting transformation matrix in ASCII format"""


def flirt_fsl(
    input_volume: InputPathType,
    reference_volume: InputPathType,
    output_volume: str | None = None,
    output_matrix: str | None = None,
    initial_matrix: InputPathType | None = None,
    data_type: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    search_cost_function: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff"] | None = "corratio",
    use_sform_qform: bool = False,
    display_initial_matrix: bool = False,
    angle_representation: typing.Literal["quaternion", "euler"] | None = "euler",
    interpolation_method: typing.Literal["trilinear", "nearestneighbour", "sinc"] | None = "trilinear",
    sinc_width: float | None = 7,
    sinc_window: typing.Literal["rectangular", "hanning", "blackman"] | None = None,
    histogram_bins: float | None = 256,
    degrees_of_freedom: float | None = 12,
    no_resample: bool = False,
    force_scaling: bool = False,
    min_voxel_dimension: float | None = None,
    apply_transform: bool = False,
    apply_isotropic_transform: float | None = None,
    padding_size: float | None = None,
    search_range_x: list[float] | None = [-90, 90],
    search_range_y: list[float] | None = [-90, 90],
    search_range_z: list[float] | None = [-90, 90],
    no_search: bool = False,
    coarse_search_angle: float | None = 60,
    fine_search_angle: float | None = 18,
    schedule_file: InputPathType | None = None,
    reference_weight: InputPathType | None = None,
    input_weight: InputPathType | None = None,
    no_clamp: bool = False,
    no_resample_blur: bool = False,
    rigid_body_mode: bool = False,
    verbose: bool = False,
    verbose_level: float | None = 0,
    pause_stages: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> FlirtFslOutputs:
    """
    FMRIB's Linear Image Registration Tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        reference_volume: Reference volume.
        output_volume: Output volume.
        output_matrix: Output matrix filename (4x4 ASCII format).
        initial_matrix: Input 4x4 affine matrix filename.
        data_type: Force output data type.
        cost_function: Cost function for registration.
        search_cost_function: Cost function for search.
        use_sform_qform: Initialize using appropriate sform or qform.
        display_initial_matrix: Display initial matrix.
        angle_representation: Set angle representation.
        interpolation_method: Interpolation method.
        sinc_width: Sinc interpolation width.
        sinc_window: Sinc interpolation window.
        histogram_bins: Number of histogram bins.
        degrees_of_freedom: Degrees of freedom.
        no_resample: Do not change input sampling.
        force_scaling: Force rescaling even for low-res images.
        min_voxel_dimension: Minimum voxel dimension for sampling (in mm).
        apply_transform: Apply transform (no optimisation), requires -init.
        apply_isotropic_transform: Apply transform with isotropic resampling.
        padding_size: Padding size for interpolation outside image.
        search_range_x: Search range for rotation around x-axis.
        search_range_y: Search range for rotation around y-axis.
        search_range_z: Search range for rotation around z-axis.
        no_search: Set all angular search ranges to 0.
        coarse_search_angle: Coarse search angle in degrees.
        fine_search_angle: Fine search angle in degrees.
        schedule_file: Custom schedule filename.
        reference_weight: Weights for reference volume.
        input_weight: Weights for input volume.
        no_clamp: Do not use intensity clamping.
        no_resample_blur: Do not use blurring on downsampling.
        rigid_body_mode: Use 2D rigid body mode (ignores dof).
        verbose: Equivalent to -verbose 1.
        verbose_level: Level of verbosity.
        pause_stages: Pause at each stage.
        version_flag: Print version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FlirtFslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FLIRT_FSL_METADATA)
    cargs = []
    cargs.append("flirt")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(reference_volume))
    if output_volume is not None:
        cargs.append(output_volume)
    if output_matrix is not None:
        cargs.extend([
            "-omat",
            output_matrix
        ])
    if initial_matrix is not None:
        cargs.extend([
            "-init",
            execution.input_file(initial_matrix)
        ])
    if data_type is not None:
        cargs.extend([
            "-datatype",
            data_type
        ])
    if cost_function is not None:
        cargs.extend([
            "-cost",
            cost_function
        ])
    if search_cost_function is not None:
        cargs.extend([
            "-searchcost",
            search_cost_function
        ])
    if use_sform_qform:
        cargs.append("-usesqform")
    if display_initial_matrix:
        cargs.append("-displayinit")
    if angle_representation is not None:
        cargs.extend([
            "-anglerep",
            angle_representation
        ])
    if interpolation_method is not None:
        cargs.extend([
            "-interp",
            interpolation_method
        ])
    if sinc_width is not None:
        cargs.extend([
            "-sincwidth",
            str(sinc_width)
        ])
    if sinc_window is not None:
        cargs.extend([
            "-sincwindow",
            sinc_window
        ])
    if histogram_bins is not None:
        cargs.extend([
            "-bins",
            str(histogram_bins)
        ])
    if degrees_of_freedom is not None:
        cargs.extend([
            "-dof",
            str(degrees_of_freedom)
        ])
    if no_resample:
        cargs.append("-noresample")
    if force_scaling:
        cargs.append("-forcescaling")
    if min_voxel_dimension is not None:
        cargs.extend([
            "-minsampling",
            str(min_voxel_dimension)
        ])
    if apply_transform:
        cargs.append("-applyxfm")
    if apply_isotropic_transform is not None:
        cargs.extend([
            "-applyisoxfm",
            str(apply_isotropic_transform)
        ])
    if padding_size is not None:
        cargs.extend([
            "-paddingsize",
            str(padding_size)
        ])
    if search_range_x is not None:
        cargs.extend([
            "-searchrx",
            *map(str, search_range_x)
        ])
    if search_range_y is not None:
        cargs.extend([
            "-searchry",
            *map(str, search_range_y)
        ])
    if search_range_z is not None:
        cargs.extend([
            "-searchrz",
            *map(str, search_range_z)
        ])
    if no_search:
        cargs.append("-nosearch")
    if coarse_search_angle is not None:
        cargs.extend([
            "-coarsesearch",
            str(coarse_search_angle)
        ])
    if fine_search_angle is not None:
        cargs.extend([
            "-finesearch",
            str(fine_search_angle)
        ])
    if schedule_file is not None:
        cargs.extend([
            "-schedule",
            execution.input_file(schedule_file)
        ])
    if reference_weight is not None:
        cargs.extend([
            "-refweight",
            execution.input_file(reference_weight)
        ])
    if input_weight is not None:
        cargs.extend([
            "-inweight",
            execution.input_file(input_weight)
        ])
    if no_clamp:
        cargs.append("-noclamp")
    if no_resample_blur:
        cargs.append("-noresampblur")
    if rigid_body_mode:
        cargs.append("-2D")
    if verbose:
        cargs.append("-v")
    if verbose_level is not None:
        cargs.extend([
            "-verbose",
            str(verbose_level)
        ])
    if pause_stages:
        cargs.append("-i")
    if version_flag:
        cargs.append("-version")
    ret = FlirtFslOutputs(
        root=execution.output_file("."),
        registered_volume=execution.output_file(output_volume + ".nii") if (output_volume is not None) else None,
        transformation_matrix=execution.output_file(output_matrix) if (output_matrix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FLIRT_FSL_METADATA",
    "FlirtFslOutputs",
    "flirt_fsl",
]