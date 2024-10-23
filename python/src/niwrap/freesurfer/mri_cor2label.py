# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_COR2LABEL_METADATA = Metadata(
    id="19d2be8eb2541da79ebcb3ed686f7b5c00939202.boutiques",
    name="mri_cor2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriCor2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_cor2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType
    """Generated label file."""
    output_volume_file: OutputPathType | None
    """Written volume label if specified."""


def mri_cor2label(
    input_file: InputPathType,
    label_id: float,
    label_file: str,
    threshold: float | None = None,
    volume_file: str | None = None,
    surface_overlay: list[str] | None = None,
    surface_path: str | None = None,
    optimize: list[str] | None = None,
    remove_holes_islands: bool = False,
    dilate: float | None = None,
    erode: float | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> MriCor2labelOutputs:
    """
    Converts values in a volume or surface overlay to a label. Designed to convert
    parcellation volumes stored in mri format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume or surface overlay file.
        label_id: Value to match in the input data.
        label_file: Name of the output label file.
        threshold: Threshold the input to make label, e.g., input values must\
            be greater than the threshold.
        volume_file: Write the label volume to a file.
        surface_overlay: Interpret input as a surface overlay, specifying\
            subject, hemisphere, and surface.
        surface_path: Specify surface path rather than subject/hemisphere.
        optimize: Treat input as a probability map and optimize thresholding.
        remove_holes_islands: Remove holes in label and islands (only valid\
            with --surf).
        dilate: Dilate label with specified number of dilations (only valid\
            with --surf).
        erode: Erode label with specified number of erosions (only valid with\
            --surf).
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCor2labelOutputs`).
    """
    if surface_overlay is not None and (len(surface_overlay) != 3): 
        raise ValueError(f"Length of 'surface_overlay' must be 3 but was {len(surface_overlay)}")
    if optimize is not None and (len(optimize) != 3): 
        raise ValueError(f"Length of 'optimize' must be 3 but was {len(optimize)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COR2LABEL_METADATA)
    cargs = []
    cargs.append("mri_cor2label")
    cargs.append("--i")
    cargs.append(execution.input_file(input_file))
    cargs.append("--id")
    cargs.append(str(label_id))
    cargs.append("--l")
    cargs.append(label_file)
    if threshold is not None:
        cargs.extend([
            "--thresh",
            str(threshold)
        ])
    if volume_file is not None:
        cargs.extend([
            "--v",
            volume_file
        ])
    if surface_overlay is not None:
        cargs.extend([
            "--surf",
            *surface_overlay
        ])
    if surface_path is not None:
        cargs.extend([
            "--surf-path",
            surface_path
        ])
    if optimize is not None:
        cargs.extend([
            "--opt",
            *optimize
        ])
    if remove_holes_islands:
        cargs.append("--remove-holes-islands")
    if dilate is not None:
        cargs.extend([
            "--dilate",
            str(dilate)
        ])
    if erode is not None:
        cargs.extend([
            "--erode",
            str(erode)
        ])
    if help_:
        cargs.append("--help")
    ret = MriCor2labelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file(label_file),
        output_volume_file=execution.output_file(volume_file) if (volume_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_COR2LABEL_METADATA",
    "MriCor2labelOutputs",
    "mri_cor2label",
]