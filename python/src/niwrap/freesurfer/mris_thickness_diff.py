# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_THICKNESS_DIFF_METADATA = Metadata(
    id="b447d6439b11ea7d939b51502ae54f028c61e756.boutiques",
    name="mris_thickness_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisThicknessDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_difference: OutputPathType
    """Output file with the difference mapped onto the surface"""
    output_resampled: OutputPathType | None
    """Resampled output thickness file"""


def mris_thickness_diff(
    out_file: InputPathType,
    src_type: str | None = None,
    trg_type: str | None = None,
    out_resampled: InputPathType | None = None,
    nsmooth: float | None = None,
    register: bool = False,
    xform: InputPathType | None = None,
    invert: bool = False,
    src_volume: InputPathType | None = None,
    dst_volume: InputPathType | None = None,
    abs_: bool = False,
    log_file: InputPathType | None = None,
    subject_name: str | None = None,
    runner: Runner | None = None,
) -> MrisThicknessDiffOutputs:
    """
    Computes the difference of two surface data sets defined on two surface meshes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        out_file: Output file name.
        src_type: Input surface data format (curv, paint or w).
        trg_type: Output format (paint or w).
        out_resampled: Output resampled thickness.
        nsmooth: Number of smoothing steps.
        register: Perform ICP rigid registration.
        xform: Apply LTA transform to align input surface1 to surface2.
        invert: Reversely apply -xform.
        src_volume: Source volume for -xform.
        dst_volume: Target volume for -xform.
        abs_: Compute the std of abs-thickness-diff.
        log_file: Log file name.
        subject_name: Subject name (to be recorded in logfile).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_DIFF_METADATA)
    cargs = []
    cargs.append("mris_thickness_diff")
    cargs.append("[SURFACE1]")
    cargs.append("[DATA1]")
    cargs.append("[SURFACE2]")
    cargs.append("[DATA2]")
    if src_type is not None:
        cargs.extend([
            "-src_type",
            src_type
        ])
    if trg_type is not None:
        cargs.extend([
            "-trg_type",
            trg_type
        ])
    cargs.extend([
        "-out",
        execution.input_file(out_file)
    ])
    if out_resampled is not None:
        cargs.extend([
            "-out_resampled",
            execution.input_file(out_resampled)
        ])
    if nsmooth is not None:
        cargs.extend([
            "-nsmooth",
            str(nsmooth)
        ])
    if register:
        cargs.append("-register")
    if xform is not None:
        cargs.extend([
            "-xform",
            execution.input_file(xform)
        ])
    if invert:
        cargs.append("-invert")
    if src_volume is not None:
        cargs.extend([
            "-src",
            execution.input_file(src_volume)
        ])
    if dst_volume is not None:
        cargs.extend([
            "-dst",
            execution.input_file(dst_volume)
        ])
    if abs_:
        cargs.append("-abs")
    if log_file is not None:
        cargs.extend([
            "-L",
            execution.input_file(log_file)
        ])
    if subject_name is not None:
        cargs.extend([
            "-S",
            subject_name
        ])
    ret = MrisThicknessDiffOutputs(
        root=execution.output_file("."),
        output_difference=execution.output_file(pathlib.Path(out_file).name),
        output_resampled=execution.output_file(pathlib.Path(out_resampled).name) if (out_resampled is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_THICKNESS_DIFF_METADATA",
    "MrisThicknessDiffOutputs",
    "mris_thickness_diff",
]
