# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_EXTRACT_SURFACE_MEASUREMENTS_METADATA = Metadata(
    id="1571ae7852c5d0ff3bb69988315d8db4d363f2a7.boutiques",
    name="dmri_extractSurfaceMeasurements",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriExtractSurfaceMeasurementsParameters = typing.TypedDict('DmriExtractSurfaceMeasurementsParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_extractSurfaceMeasurements"],
    "streamline_file": InputPathType,
    "lh_surface_file": InputPathType,
    "lh_thickness_overlay": InputPathType,
    "lh_curvature_overlay": InputPathType,
    "rh_surface_file": InputPathType,
    "rh_thickness_overlay": InputPathType,
    "rh_curvature_overlay": InputPathType,
    "output_directory": str,
    "reference_image": typing.NotRequired[InputPathType | None],
    "reference_image_anatomical": typing.NotRequired[InputPathType | None],
    "transformation": typing.NotRequired[InputPathType | None],
    "annotation_file": typing.NotRequired[InputPathType | None],
    "fa_options": typing.NotRequired[list[str] | None],
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
        "dmri_extractSurfaceMeasurements": dmri_extract_surface_measurements_cargs,
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
    }.get(t)


class DmriExtractSurfaceMeasurementsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_extract_surface_measurements(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_extract_surface_measurements_params(
    streamline_file: InputPathType,
    lh_surface_file: InputPathType,
    lh_thickness_overlay: InputPathType,
    lh_curvature_overlay: InputPathType,
    rh_surface_file: InputPathType,
    rh_thickness_overlay: InputPathType,
    rh_curvature_overlay: InputPathType,
    output_directory: str,
    reference_image: InputPathType | None = None,
    reference_image_anatomical: InputPathType | None = None,
    transformation: InputPathType | None = None,
    annotation_file: InputPathType | None = None,
    fa_options: list[str] | None = None,
) -> DmriExtractSurfaceMeasurementsParameters:
    """
    Build parameters.
    
    Args:
        streamline_file: Streamline file in .trk format.
        lh_surface_file: Left hemisphere surface file.
        lh_thickness_overlay: Left hemisphere thickness overlay file.
        lh_curvature_overlay: Left hemisphere curvature overlay file.
        rh_surface_file: Right hemisphere surface file.
        rh_thickness_overlay: Right hemisphere thickness overlay file.
        rh_curvature_overlay: Right hemisphere curvature overlay file.
        output_directory: Output directory.
        reference_image: Reference image for situations where FA is not used.
        reference_image_anatomical: Reference image for anatomical space when\
            diffusion and anatomical spaces are not registered.
        transformation: Transformation from diffusion to anatomical space.
        annotation_file: Annotation file.
        fa_options: FA options including the number of files and their\
            respective paths.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_extractSurfaceMeasurements",
        "streamline_file": streamline_file,
        "lh_surface_file": lh_surface_file,
        "lh_thickness_overlay": lh_thickness_overlay,
        "lh_curvature_overlay": lh_curvature_overlay,
        "rh_surface_file": rh_surface_file,
        "rh_thickness_overlay": rh_thickness_overlay,
        "rh_curvature_overlay": rh_curvature_overlay,
        "output_directory": output_directory,
    }
    if reference_image is not None:
        params["reference_image"] = reference_image
    if reference_image_anatomical is not None:
        params["reference_image_anatomical"] = reference_image_anatomical
    if transformation is not None:
        params["transformation"] = transformation
    if annotation_file is not None:
        params["annotation_file"] = annotation_file
    if fa_options is not None:
        params["fa_options"] = fa_options
    return params


def dmri_extract_surface_measurements_cargs(
    params: DmriExtractSurfaceMeasurementsParameters,
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
    cargs.append("dmri_extractSurfaceMeasurements")
    cargs.extend([
        "-i",
        execution.input_file(params.get("streamline_file"))
    ])
    cargs.extend([
        "-sl",
        execution.input_file(params.get("lh_surface_file"))
    ])
    cargs.extend([
        "-tl",
        execution.input_file(params.get("lh_thickness_overlay"))
    ])
    cargs.extend([
        "-cl",
        execution.input_file(params.get("lh_curvature_overlay"))
    ])
    cargs.extend([
        "-sr",
        execution.input_file(params.get("rh_surface_file"))
    ])
    cargs.extend([
        "-tr",
        execution.input_file(params.get("rh_thickness_overlay"))
    ])
    cargs.extend([
        "-cr",
        execution.input_file(params.get("rh_curvature_overlay"))
    ])
    cargs.extend([
        "-o",
        params.get("output_directory")
    ])
    if params.get("reference_image") is not None:
        cargs.extend([
            "-rid",
            execution.input_file(params.get("reference_image"))
        ])
    if params.get("reference_image_anatomical") is not None:
        cargs.extend([
            "-ria",
            execution.input_file(params.get("reference_image_anatomical"))
        ])
    if params.get("transformation") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("transformation"))
        ])
    if params.get("annotation_file") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("annotation_file"))
        ])
    if params.get("fa_options") is not None:
        cargs.extend([
            "-fa",
            *params.get("fa_options")
        ])
    return cargs


def dmri_extract_surface_measurements_outputs(
    params: DmriExtractSurfaceMeasurementsParameters,
    execution: Execution,
) -> DmriExtractSurfaceMeasurementsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriExtractSurfaceMeasurementsOutputs(
        root=execution.output_file("."),
    )
    return ret


def dmri_extract_surface_measurements_execute(
    params: DmriExtractSurfaceMeasurementsParameters,
    execution: Execution,
) -> DmriExtractSurfaceMeasurementsOutputs:
    """
    A tool for extracting surface measurements from diffusion MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriExtractSurfaceMeasurementsOutputs`).
    """
    params = execution.params(params)
    cargs = dmri_extract_surface_measurements_cargs(params, execution)
    ret = dmri_extract_surface_measurements_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_extract_surface_measurements(
    streamline_file: InputPathType,
    lh_surface_file: InputPathType,
    lh_thickness_overlay: InputPathType,
    lh_curvature_overlay: InputPathType,
    rh_surface_file: InputPathType,
    rh_thickness_overlay: InputPathType,
    rh_curvature_overlay: InputPathType,
    output_directory: str,
    reference_image: InputPathType | None = None,
    reference_image_anatomical: InputPathType | None = None,
    transformation: InputPathType | None = None,
    annotation_file: InputPathType | None = None,
    fa_options: list[str] | None = None,
    runner: Runner | None = None,
) -> DmriExtractSurfaceMeasurementsOutputs:
    """
    A tool for extracting surface measurements from diffusion MRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        streamline_file: Streamline file in .trk format.
        lh_surface_file: Left hemisphere surface file.
        lh_thickness_overlay: Left hemisphere thickness overlay file.
        lh_curvature_overlay: Left hemisphere curvature overlay file.
        rh_surface_file: Right hemisphere surface file.
        rh_thickness_overlay: Right hemisphere thickness overlay file.
        rh_curvature_overlay: Right hemisphere curvature overlay file.
        output_directory: Output directory.
        reference_image: Reference image for situations where FA is not used.
        reference_image_anatomical: Reference image for anatomical space when\
            diffusion and anatomical spaces are not registered.
        transformation: Transformation from diffusion to anatomical space.
        annotation_file: Annotation file.
        fa_options: FA options including the number of files and their\
            respective paths.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriExtractSurfaceMeasurementsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_EXTRACT_SURFACE_MEASUREMENTS_METADATA)
    params = dmri_extract_surface_measurements_params(streamline_file=streamline_file, lh_surface_file=lh_surface_file, lh_thickness_overlay=lh_thickness_overlay, lh_curvature_overlay=lh_curvature_overlay, rh_surface_file=rh_surface_file, rh_thickness_overlay=rh_thickness_overlay, rh_curvature_overlay=rh_curvature_overlay, output_directory=output_directory, reference_image=reference_image, reference_image_anatomical=reference_image_anatomical, transformation=transformation, annotation_file=annotation_file, fa_options=fa_options)
    return dmri_extract_surface_measurements_execute(params, execution)


__all__ = [
    "DMRI_EXTRACT_SURFACE_MEASUREMENTS_METADATA",
    "DmriExtractSurfaceMeasurementsOutputs",
    "DmriExtractSurfaceMeasurementsParameters",
    "dmri_extract_surface_measurements",
    "dmri_extract_surface_measurements_params",
]
