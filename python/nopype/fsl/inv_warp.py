# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


INV_WARP_METADATA = Metadata(
    id="ef3b1bef7e701e4967ab676b3a228c5251f7dcbf",
    name="InvWarp",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class InvWarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `inv_warp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inverse_warp: OutputPathType
    """Name of output file, containing warps that are the "reverse" of those in --warp. this will be a field-file (rather than a file of spline coefficients), and it will have any affine component included as part of the displacements."""


def inv_warp(
    runner: Runner,
    warp: InputPathType,
    out_img: str,
    ref_img: InputPathType,
    absolute: bool = False,
    relative: bool = False,
    jacobian_max: float | int | None = None,
    jacobian_min: float | int | None = None,
    noconstraint: bool = False,
    debug: bool = False,
) -> InvWarpOutputs:
    """
    
    Use FSL Invwarp to invert a FNIRT warp
    
    Args:
        runner: Command runner
        warp: Filename for warp/shiftmap transform (volume).
        out_img: Filename for output (inverse warped) image.
        ref_img: Filename for new reference image.
        absolute: Use absolute warp convention (default): x' = w(x).
        relative: Use relative warp convention (default): x' = x + w(x).
        jacobian_max: Maximum acceptable jacobian value for constraint (default
            100.0).
        jacobian_min: Minimum acceptable jacobian value for constraint (default
            0.01).
        noconstraint: Do not apply jacobian constraint.
        debug: Turn on debugging output.
    Returns:
        NamedTuple of outputs (described in `InvWarpOutputs`).
    """
    if (
        absolute +
        relative
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "absolute,\n"
            "relative"
        )
    execution = runner.start_execution(INV_WARP_METADATA)
    cargs = []
    cargs.append("invwarp")
    cargs.append(("--warp=" + execution.input_file(warp)))
    cargs.append(("--out=" + out_img))
    cargs.append(("--ref=" + execution.input_file(ref_img)))
    if absolute:
        cargs.append("--abs")
    if relative:
        cargs.append("--rel")
    if noconstraint:
        cargs.append("--noconstraint")
    if jacobian_min is not None:
        cargs.append(("--jmin=" + str(jacobian_min)))
    if jacobian_max is not None:
        cargs.append(("--jmax=" + str(jacobian_max)))
    if debug:
        cargs.append("--debug")
    ret = InvWarpOutputs(
        root=execution.output_file("."),
        inverse_warp=execution.output_file(f"{out_img}", optional=True),
    )
    execution.run(cargs)
    return ret
