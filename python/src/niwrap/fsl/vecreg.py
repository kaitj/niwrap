# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VECREG_METADATA = Metadata(
    id="6c7d48cef02fef3fe66c2282a3eb56099599fdb5.boutiques",
    name="vecreg",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class VecregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vecreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_output: OutputPathType
    """Output file of registered vector or tensor field"""


def vecreg(
    input_file: InputPathType,
    output_file: str,
    reference_volume: InputPathType,
    transform_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    secondary_affine: InputPathType | None = None,
    secondary_warp: InputPathType | None = None,
    interp_method: str | None = "trilinear",
    brain_mask: InputPathType | None = None,
    ref_brain_mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> VecregOutputs:
    """
    Vector Affine/NonLinear Transformation with Orientation Preservation.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT
    
    Args:
        input_file: Filename for input vector or tensor field.
        output_file: Filename for output registered vector or tensor field.
        reference_volume: Filename for reference (target) volume.
        transform_file: Filename for affine transformation matrix.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        secondary_affine: Filename for secondary affine matrix; if set, this\
            will be used for the rotation of the vector/tensor field.
        secondary_warp: Filename for secondary warp field; if set, this will be\
            used for the rotation of the vector/tensor field.
        interp_method: Interpolation method (nearestneighbour, trilinear\
            (default), sinc, or spline).
        brain_mask: Brain mask in input space.
        ref_brain_mask: Brain mask in output space (useful for speed up of\
            nonlinear registration).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VecregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VECREG_METADATA)
    cargs = []
    cargs.append("vecreg")
    cargs.extend([
        "-i",
        execution.input_file(input_file)
    ])
    cargs.extend([
        "-o",
        output_file
    ])
    cargs.extend([
        "-r",
        execution.input_file(reference_volume)
    ])
    if transform_file is not None:
        cargs.extend([
            "-t",
            execution.input_file(transform_file)
        ])
    if verbose_flag:
        cargs.append("-v")
    if help_flag:
        cargs.append("-h")
    if secondary_affine is not None:
        cargs.extend([
            "--rotmat",
            execution.input_file(secondary_affine)
        ])
    if secondary_warp is not None:
        cargs.extend([
            "--rotwarp",
            execution.input_file(secondary_warp)
        ])
    if interp_method is not None:
        cargs.extend([
            "--interp",
            interp_method
        ])
    if brain_mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(brain_mask)
        ])
    if ref_brain_mask is not None:
        cargs.extend([
            "--refmask",
            execution.input_file(ref_brain_mask)
        ])
    ret = VecregOutputs(
        root=execution.output_file("."),
        registered_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VECREG_METADATA",
    "VecregOutputs",
    "vecreg",
]