# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_EDIT_WM_WITH_ASEG_METADATA = Metadata(
    id="f9c976c7dcbdda3256a48669b4d7c0911a56357c.boutiques",
    name="mri_edit_wm_with_aseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriEditWmWithAsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_edit_wm_with_aseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_wm_file: OutputPathType
    """Edited white matter output file"""


def mri_edit_wm_with_aseg(
    input_wm: InputPathType,
    input_t1_brain: InputPathType,
    aseg: InputPathType,
    output_wm: str,
    fillven: bool = False,
    fix_scm_ha: int | None = None,
    fix_scm_ha_only: str | None = None,
    keep: bool = False,
    keep_in: bool = False,
    lh: bool = False,
    rh: bool = False,
    fix_ento_wm: str | None = None,
    sa_fix_ento_wm: str | None = None,
    debug_voxel: list[float] | None = None,
    runner: Runner | None = None,
) -> MriEditWmWithAsegOutputs:
    """
    A tool for editing white matter with anatomical segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_wm: Input white matter file.
        input_t1_brain: Input T1/brain file.
        aseg: Anatomical segmentation file.
        output_wm: Output white matter file.
        fillven: Fill ventricular system.
        fix_scm_ha: Remove voxels in amygdala, ILV, and parts of hippocampus.
        fix_scm_ha_only: Standalone: fix SCM using aseg.presurf.mgz.
        keep: Keep edits as found in output volume.
        keep_in: Keep edits as found in input volume.
        lh: Erase right hemisphere labels from output.
        rh: Erase left hemisphere labels from output.
        fix_ento_wm: Insert lhval rhval where {3,4}006 and {3,4}201 in entowm\
            volume.
        sa_fix_ento_wm: Standalone version of fix ento-WM.
        debug_voxel: Specify a voxel to edit with coordinates Gx Gy Gz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEditWmWithAsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_EDIT_WM_WITH_ASEG_METADATA)
    cargs = []
    cargs.append("mri_edit_wm_with_aseg")
    cargs.append(execution.input_file(input_wm))
    cargs.append(execution.input_file(input_t1_brain))
    cargs.append(execution.input_file(aseg))
    cargs.append(output_wm)
    if fillven:
        cargs.append("-fillven")
    if fix_scm_ha is not None:
        cargs.extend([
            "-fix-scm-ha",
            str(fix_scm_ha)
        ])
    if fix_scm_ha_only is not None:
        cargs.extend([
            "-fix-scm-ha-only",
            fix_scm_ha_only
        ])
    if keep:
        cargs.append("-keep")
    if keep_in:
        cargs.append("-keep-in")
    if lh:
        cargs.append("-lh")
    if rh:
        cargs.append("-rh")
    if fix_ento_wm is not None:
        cargs.extend([
            "-fix-ento-wm",
            fix_ento_wm
        ])
    if sa_fix_ento_wm is not None:
        cargs.extend([
            "-sa-fix-ento-wm",
            sa_fix_ento_wm
        ])
    if debug_voxel is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, debug_voxel)
        ])
    ret = MriEditWmWithAsegOutputs(
        root=execution.output_file("."),
        output_wm_file=execution.output_file(output_wm),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_EDIT_WM_WITH_ASEG_METADATA",
    "MriEditWmWithAsegOutputs",
    "mri_edit_wm_with_aseg",
]