# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_INTERMODALITY_INTRASUBJECT_SH_METADATA = Metadata(
    id="e4f43efff74611f07e60c00f682c377a411a79c7.boutiques",
    name="antsIntermodalityIntrasubject.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
AntsIntermodalityIntrasubjectShParameters = typing.TypedDict('AntsIntermodalityIntrasubjectShParameters', {
    "__STYX_TYPE__": typing.Literal["antsIntermodalityIntrasubject.sh"],
    "dimension": int,
    "anatomical_t1_image": InputPathType,
    "anatomical_reference_image": typing.NotRequired[InputPathType | None],
    "scalar_image_to_match": InputPathType,
    "anatomical_t1brainmask": InputPathType,
    "transform_type": typing.Literal[0, 1, 2, 3],
    "t1_to_template_prefix": str,
    "template_space": typing.NotRequired[str | None],
    "output_prefix": str,
    "labels_in_template_space": typing.NotRequired[InputPathType | None],
    "auxiliary_scalar_images": typing.NotRequired[InputPathType | None],
    "auxiliary_dt_image": typing.NotRequired[InputPathType | None],
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
        "antsIntermodalityIntrasubject.sh": ants_intermodality_intrasubject_sh_cargs,
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
        "antsIntermodalityIntrasubject.sh": ants_intermodality_intrasubject_sh_outputs,
    }
    return vt.get(t)


class AntsIntermodalityIntrasubjectShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_intermodality_intrasubject_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transformed_image: OutputPathType
    """Output transformed image after registration."""
    output_transform: OutputPathType
    """Transformation matrix or warp field from the registration."""
    output_warped_image: OutputPathType
    """Output warped image in the template space."""


def ants_intermodality_intrasubject_sh_params(
    dimension: int,
    anatomical_t1_image: InputPathType,
    scalar_image_to_match: InputPathType,
    anatomical_t1brainmask: InputPathType,
    transform_type: typing.Literal[0, 1, 2, 3],
    t1_to_template_prefix: str,
    output_prefix: str,
    anatomical_reference_image: InputPathType | None = None,
    template_space: str | None = None,
    labels_in_template_space: InputPathType | None = None,
    auxiliary_scalar_images: InputPathType | None = None,
    auxiliary_dt_image: InputPathType | None = None,
) -> AntsIntermodalityIntrasubjectShParameters:
    """
    Build parameters.
    
    Args:
        dimension: Dimensionality of the image, typically 3 for 3D images.
        anatomical_t1_image: Anatomical T1 image (brain or whole-head) to align\
            to.
        scalar_image_to_match: Scalar image to be matched, such as average\
            BOLD, average DWI, etc.
        anatomical_t1brainmask: Brain mask for the anatomical T1 image, should\
            mask out regions not appearing in the scalar image.
        transform_type: Type of transform: 0=rigid, 1=affine,\
            2=rigid+small_def, 3=affine+small_def.
        t1_to_template_prefix: Prefix for T1 to template transform files.
        output_prefix: Prefix for output files.
        anatomical_reference_image: Anatomical reference image to warp to,\
            often higher resolution than the anatomical T1 image.
        template_space: Template space.
        labels_in_template_space: Labels in the template space.
        auxiliary_scalar_images: Auxiliary scalar images to warp to the\
            template.
        auxiliary_dt_image: Auxiliary DT image to warp to the template.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "antsIntermodalityIntrasubject.sh",
        "dimension": dimension,
        "anatomical_t1_image": anatomical_t1_image,
        "scalar_image_to_match": scalar_image_to_match,
        "anatomical_t1brainmask": anatomical_t1brainmask,
        "transform_type": transform_type,
        "t1_to_template_prefix": t1_to_template_prefix,
        "output_prefix": output_prefix,
    }
    if anatomical_reference_image is not None:
        params["anatomical_reference_image"] = anatomical_reference_image
    if template_space is not None:
        params["template_space"] = template_space
    if labels_in_template_space is not None:
        params["labels_in_template_space"] = labels_in_template_space
    if auxiliary_scalar_images is not None:
        params["auxiliary_scalar_images"] = auxiliary_scalar_images
    if auxiliary_dt_image is not None:
        params["auxiliary_dt_image"] = auxiliary_dt_image
    return params


def ants_intermodality_intrasubject_sh_cargs(
    params: AntsIntermodalityIntrasubjectShParameters,
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
    cargs.append("antsIntermodalityIntrasubject.sh")
    cargs.extend([
        "-d",
        str(params.get("dimension"))
    ])
    cargs.extend([
        "-r",
        execution.input_file(params.get("anatomical_t1_image"))
    ])
    if params.get("anatomical_reference_image") is not None:
        cargs.extend([
            "-R",
            execution.input_file(params.get("anatomical_reference_image"))
        ])
    cargs.extend([
        "-i",
        execution.input_file(params.get("scalar_image_to_match"))
    ])
    cargs.extend([
        "-x",
        execution.input_file(params.get("anatomical_t1brainmask"))
    ])
    cargs.extend([
        "-t",
        str(params.get("transform_type"))
    ])
    cargs.extend([
        "-w",
        params.get("t1_to_template_prefix")
    ])
    if params.get("template_space") is not None:
        cargs.extend([
            "-T",
            params.get("template_space")
        ])
    cargs.extend([
        "-o",
        params.get("output_prefix")
    ])
    if params.get("labels_in_template_space") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("labels_in_template_space"))
        ])
    if params.get("auxiliary_scalar_images") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("auxiliary_scalar_images"))
        ])
    if params.get("auxiliary_dt_image") is not None:
        cargs.extend([
            "-b",
            execution.input_file(params.get("auxiliary_dt_image"))
        ])
    return cargs


def ants_intermodality_intrasubject_sh_outputs(
    params: AntsIntermodalityIntrasubjectShParameters,
    execution: Execution,
) -> AntsIntermodalityIntrasubjectShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AntsIntermodalityIntrasubjectShOutputs(
        root=execution.output_file("."),
        output_transformed_image=execution.output_file(params.get("output_prefix") + "Transformed.nii.gz"),
        output_transform=execution.output_file(params.get("output_prefix") + "Transform.mat"),
        output_warped_image=execution.output_file(params.get("output_prefix") + "Warped.nii.gz"),
    )
    return ret


def ants_intermodality_intrasubject_sh_execute(
    params: AntsIntermodalityIntrasubjectShParameters,
    execution: Execution,
) -> AntsIntermodalityIntrasubjectShOutputs:
    """
    Performs registration between a scalar image and a T1 image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AntsIntermodalityIntrasubjectShOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = ants_intermodality_intrasubject_sh_cargs(params, execution)
    ret = ants_intermodality_intrasubject_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def ants_intermodality_intrasubject_sh(
    dimension: int,
    anatomical_t1_image: InputPathType,
    scalar_image_to_match: InputPathType,
    anatomical_t1brainmask: InputPathType,
    transform_type: typing.Literal[0, 1, 2, 3],
    t1_to_template_prefix: str,
    output_prefix: str,
    anatomical_reference_image: InputPathType | None = None,
    template_space: str | None = None,
    labels_in_template_space: InputPathType | None = None,
    auxiliary_scalar_images: InputPathType | None = None,
    auxiliary_dt_image: InputPathType | None = None,
    runner: Runner | None = None,
) -> AntsIntermodalityIntrasubjectShOutputs:
    """
    Performs registration between a scalar image and a T1 image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        dimension: Dimensionality of the image, typically 3 for 3D images.
        anatomical_t1_image: Anatomical T1 image (brain or whole-head) to align\
            to.
        scalar_image_to_match: Scalar image to be matched, such as average\
            BOLD, average DWI, etc.
        anatomical_t1brainmask: Brain mask for the anatomical T1 image, should\
            mask out regions not appearing in the scalar image.
        transform_type: Type of transform: 0=rigid, 1=affine,\
            2=rigid+small_def, 3=affine+small_def.
        t1_to_template_prefix: Prefix for T1 to template transform files.
        output_prefix: Prefix for output files.
        anatomical_reference_image: Anatomical reference image to warp to,\
            often higher resolution than the anatomical T1 image.
        template_space: Template space.
        labels_in_template_space: Labels in the template space.
        auxiliary_scalar_images: Auxiliary scalar images to warp to the\
            template.
        auxiliary_dt_image: Auxiliary DT image to warp to the template.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsIntermodalityIntrasubjectShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_INTERMODALITY_INTRASUBJECT_SH_METADATA)
    params = ants_intermodality_intrasubject_sh_params(dimension=dimension, anatomical_t1_image=anatomical_t1_image, anatomical_reference_image=anatomical_reference_image, scalar_image_to_match=scalar_image_to_match, anatomical_t1brainmask=anatomical_t1brainmask, transform_type=transform_type, t1_to_template_prefix=t1_to_template_prefix, template_space=template_space, output_prefix=output_prefix, labels_in_template_space=labels_in_template_space, auxiliary_scalar_images=auxiliary_scalar_images, auxiliary_dt_image=auxiliary_dt_image)
    return ants_intermodality_intrasubject_sh_execute(params, execution)


__all__ = [
    "ANTS_INTERMODALITY_INTRASUBJECT_SH_METADATA",
    "AntsIntermodalityIntrasubjectShOutputs",
    "ants_intermodality_intrasubject_sh",
    "ants_intermodality_intrasubject_sh_params",
]
