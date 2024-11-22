# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_BRAIN_EXTRACTION_SH_METADATA = Metadata(
    id="1c41875abbfc51258f43fa8c151154d15b83f120.boutiques",
    name="antsBrainExtraction.sh",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsBrainExtractionShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_brain_extraction_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    brain_extracted_image: OutputPathType | None
    """Brain extracted image"""
    brain_mask: OutputPathType | None
    """Brain mask"""
    brain_probability_mask: OutputPathType | None
    """Brain probability mask"""


def ants_brain_extraction_sh(
    anatomical_image: InputPathType,
    template: InputPathType,
    probability_mask: InputPathType,
    image_dimension: int = 3,
    tissue_classification: str | None = None,
    brain_extraction_registration_mask: InputPathType | None = None,
    keep_temporary_files: bool = False,
    single_floating_point_precision: bool = False,
    initial_moving_transform: InputPathType | None = None,
    rotation_search_params: str | None = None,
    image_file_suffix: str | None = None,
    translation_search_params: str | None = None,
    random_seeding: bool = False,
    debug_mode: bool = False,
    output_prefix: str | None = "output",
    runner: Runner | None = None,
) -> AntsBrainExtractionShOutputs:
    """
    antsBrainExtraction.sh performs template-based brain extraction.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        anatomical_image: Anatomical image (Structural image, typically T1).
        template: Brain extraction template (Anatomical template).
        probability_mask: Brain extraction probability mask.
        image_dimension: Image dimension (2 or 3).
        tissue_classification: Tissue classification.
        brain_extraction_registration_mask: Brain extraction registration mask.
        keep_temporary_files: Keep temporary files.
        single_floating_point_precision: Use single floating point precision.
        initial_moving_transform: Initial moving transform.
        rotation_search_params: Rotation search parameters.
        image_file_suffix: Image file suffix.
        translation_search_params: Translation search parameters.
        random_seeding: Use random seeding.
        debug_mode: Test / debug mode.
        output_prefix: Output prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsBrainExtractionShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_BRAIN_EXTRACTION_SH_METADATA)
    cargs = []
    cargs.append("antsBrainExtraction.sh")
    cargs.append("-d")
    cargs.append(str(image_dimension))
    cargs.append("-a")
    cargs.append(execution.input_file(anatomical_image))
    cargs.append("-e")
    cargs.append(execution.input_file(template))
    cargs.append("-m")
    cargs.append(execution.input_file(probability_mask))
    if tissue_classification is not None:
        cargs.extend([
            "-c",
            tissue_classification
        ])
    if brain_extraction_registration_mask is not None:
        cargs.extend([
            "-f",
            execution.input_file(brain_extraction_registration_mask)
        ])
    if keep_temporary_files:
        cargs.append("-k")
    if single_floating_point_precision:
        cargs.append("-q")
    if initial_moving_transform is not None:
        cargs.extend([
            "-r",
            execution.input_file(initial_moving_transform)
        ])
    if rotation_search_params is not None:
        cargs.extend([
            "-R",
            rotation_search_params
        ])
    if image_file_suffix is not None:
        cargs.extend([
            "-s",
            image_file_suffix
        ])
    if translation_search_params is not None:
        cargs.extend([
            "-T",
            translation_search_params
        ])
    if random_seeding:
        cargs.append("-u")
    if debug_mode:
        cargs.append("-z")
    cargs.append("-o")
    if output_prefix is not None:
        cargs.append(output_prefix)
    ret = AntsBrainExtractionShOutputs(
        root=execution.output_file("."),
        brain_extracted_image=execution.output_file(output_prefix + "_BrainExtractionBrain.nii.gz") if (output_prefix is not None) else None,
        brain_mask=execution.output_file(output_prefix + "_BrainExtractionMask.nii.gz") if (output_prefix is not None) else None,
        brain_probability_mask=execution.output_file(output_prefix + "_BrainExtractionPrior0GenericAffine.mat") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_BRAIN_EXTRACTION_SH_METADATA",
    "AntsBrainExtractionShOutputs",
    "ants_brain_extraction_sh",
]
