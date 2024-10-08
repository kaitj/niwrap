# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INVWARP_EXE_METADATA = Metadata(
    id="175b4b96a3fda73dd36df21eb780dd0c523a387b.boutiques",
    name="invwarp_exe",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class InvwarpExeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `invwarp_exe(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_inverse_warped_image: OutputPathType
    """Output inverse warped image"""


def invwarp_exe(
    warp_file: InputPathType,
    out_file: str,
    ref_file: InputPathType,
    rel_flag: bool = False,
    abs_flag: bool = False,
    niter: float | None = None,
    regularise: float | None = 1.0,
    initwarp: InputPathType | None = None,
    noconstraint: bool = False,
    jmin: float | None = 0.01,
    jmax: float | None = 100.0,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> InvwarpExeOutputs:
    """
    Inverse warp image volume using FSL's invwarp tool.
    
    Author: University of Oxford (Mark Jenkinson)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT/UsersGuide#A--invwarp
    
    Args:
        warp_file: Filename for warp/shiftmap transform (volume).
        out_file: Filename for output (inverse warped) image.
        ref_file: Filename for new reference image, i.e., what was originally\
            the input image (determines inverse warpvol's FOV and pixdims).
        rel_flag: Use relative warp convention: x' = x + w(x).
        abs_flag: Use absolute warp convention (default): x' = w(x).
        niter: Number of gradient-descent iterations (default=10).
        regularise: Regularisation strength (default=1.0).
        initwarp: Filename for initial warp transform (volume).
        noconstraint: Do not apply the Jacobian constraint.
        jmin: Minimum acceptable Jacobian value for constraint (default 0.01).
        jmax: Maximum acceptable Jacobian value for constraint (default 100.0).
        debug_flag: Turn on debugging output.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InvwarpExeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INVWARP_EXE_METADATA)
    cargs = []
    cargs.append("invwarp")
    cargs.append("-w")
    cargs.extend([
        "-w",
        execution.input_file(warp_file)
    ])
    cargs.append("-o")
    cargs.extend([
        "-o",
        out_file
    ])
    cargs.append("-r")
    cargs.extend([
        "-r",
        execution.input_file(ref_file)
    ])
    if rel_flag:
        cargs.append("--rel")
    if abs_flag:
        cargs.append("--abs")
    if niter is not None:
        cargs.extend([
            "-n",
            str(niter)
        ])
    if regularise is not None:
        cargs.extend([
            "--regularise",
            str(regularise)
        ])
    if initwarp is not None:
        cargs.extend([
            "--initwarp",
            execution.input_file(initwarp)
        ])
    if noconstraint:
        cargs.append("--noconstraint")
    if jmin is not None:
        cargs.extend([
            "--jmin",
            str(jmin)
        ])
    if jmax is not None:
        cargs.extend([
            "--jmax",
            str(jmax)
        ])
    if debug_flag:
        cargs.append("--debug")
    if verbose_flag:
        cargs.append("-v")
    ret = InvwarpExeOutputs(
        root=execution.output_file("."),
        output_inverse_warped_image=execution.output_file(out_file + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INVWARP_EXE_METADATA",
    "InvwarpExeOutputs",
    "invwarp_exe",
]
