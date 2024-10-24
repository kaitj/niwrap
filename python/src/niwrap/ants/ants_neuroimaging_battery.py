# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_NEUROIMAGING_BATTERY_METADATA = Metadata(
    id="8d5f7d9ec665c8a4728e1d76b9ae72be2a9a3489.boutiques",
    name="antsNeuroimagingBattery",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsNeuroimagingBatteryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_neuroimaging_battery(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_transform: OutputPathType
    """Output transform files."""


def ants_neuroimaging_battery(
    input_directory: str,
    output_directory: str,
    output_name: str,
    anatomical_image: InputPathType,
    anatomical_mask: InputPathType,
    runner: Runner | None = None,
) -> AntsNeuroimagingBatteryOutputs:
    """
    Align MR modalities to a common within-subject (and optional template) space.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        input_directory: Directory where to look for modality images.
        output_directory: Directory where output goes (where\
            antsCorticalThickness output lives).
        output_name: File prefix for outputs.
        anatomical_image: Reference subject image (usually T1).
        anatomical_mask: Mask of anatomical image, should contain cerebrum,\
            cerebellum, and brainstem.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsNeuroimagingBatteryOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_NEUROIMAGING_BATTERY_METADATA)
    cargs = []
    cargs.append("antsNeuroimagingBattery.pl")
    cargs.extend([
        "--input-directory",
        input_directory
    ])
    cargs.extend([
        "--output-directory",
        output_directory
    ])
    cargs.extend([
        "--output-name",
        output_name
    ])
    cargs.extend([
        "--anatomical",
        execution.input_file(anatomical_image)
    ])
    cargs.extend([
        "--anatomical-mask",
        execution.input_file(anatomical_mask)
    ])
    cargs.append("[OPTIONAL_INPUTS]")
    ret = AntsNeuroimagingBatteryOutputs(
        root=execution.output_file("."),
        output_transform=execution.output_file(output_directory + "/" + output_name + ".*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_NEUROIMAGING_BATTERY_METADATA",
    "AntsNeuroimagingBatteryOutputs",
    "ants_neuroimaging_battery",
]
