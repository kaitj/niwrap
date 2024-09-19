# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__ALIGN_CENTERS_METADATA = Metadata(
    id="d5e025b526c5550c43cc62b76dfb21381e4ebd71.boutiques",
    name="@Align_Centers",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VAlignCentersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__align_centers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transform_matrix: OutputPathType
    """Transform matrix needed for the shift applied to DSET."""
    shifted_dset: OutputPathType | None
    """Shifted Dataset aligned with the base volume."""
    shifted_child_dsets: OutputPathType | None
    """Shifted child datasets aligned with the base volume."""


def v__align_centers(
    base: InputPathType,
    dset: InputPathType,
    children: list[InputPathType] | None = None,
    echo: bool = False,
    overwrite: bool = False,
    prefix: str | None = None,
    matrix_only: bool = False,
    matrix_only_no_dset: bool = False,
    no_cp: bool = False,
    center_grid: bool = False,
    center_cm: bool = False,
    center_cm_no_amask: bool = False,
    shift_xform: InputPathType | None = None,
    shift_xform_inv: InputPathType | None = None,
    runner: Runner | None = None,
) -> VAlignCentersOutputs:
    """
    Moves the center of a dataset (DSET) to the center of a base volume (BASE) and
    optionally creates a transform matrix.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Align_Centers.html
    
    Args:
        base: Base volume, typically a template. Can also specify RAI\
            coordinates for center alignment.
        dset: Dataset to be aligned to BASE.
        children: Additional datasets (originally in register with DSET) that\
            should be shifted in the same way.
        echo: Echo all commands to terminal for debugging.
        overwrite: Overwrite existing output files.
        prefix: Custom prefix for the result files.
        matrix_only: Only output the transform needed to align the centers\
            without shifting any child volumes.
        matrix_only_no_dset: Like -1Dmat_only, but no datasets are created or\
            changed.
        no_cp: Do not create new data; shift existing ones. Use with caution.
        center_grid: Center is that of the volume's grid (default).
        center_cm: Center is the center of mass of the volume.
        center_cm_no_amask: Like -cm, but with no automask.
        shift_xform: Apply shift translation from a 1D file.
        shift_xform_inv: Apply inverse of shift translation from a 1D file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAlignCentersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ALIGN_CENTERS_METADATA)
    cargs = []
    cargs.append("@Align_Centers")
    cargs.append(execution.input_file(base))
    cargs.append(execution.input_file(dset))
    if children is not None:
        cargs.extend([
            "-child",
            *[execution.input_file(f) for f in children]
        ])
    if echo:
        cargs.append("-echo")
    if overwrite:
        cargs.append("-overwrite")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if matrix_only:
        cargs.append("-1Dmat_only")
    if matrix_only_no_dset:
        cargs.append("-1Dmat_only_nodset")
    if no_cp:
        cargs.append("-no_cp")
    if center_grid:
        cargs.append("-grid")
    if center_cm:
        cargs.append("-cm")
    if center_cm_no_amask:
        cargs.append("-cm_no_amask")
    if shift_xform is not None:
        cargs.extend([
            "-shift_xform",
            execution.input_file(shift_xform)
        ])
    if shift_xform_inv is not None:
        cargs.extend([
            "-shift_xform_inv",
            execution.input_file(shift_xform_inv)
        ])
    ret = VAlignCentersOutputs(
        root=execution.output_file("."),
        transform_matrix=execution.output_file(pathlib.Path(dset).name + "_shft.1D"),
        shifted_dset=execution.output_file(prefix + "_shft+orig.BRIK") if (prefix is not None) else None,
        shifted_child_dsets=execution.output_file(prefix + "_child_shft+orig.BRIK") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAlignCentersOutputs",
    "V__ALIGN_CENTERS_METADATA",
    "v__align_centers",
]
