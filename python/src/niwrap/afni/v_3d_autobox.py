# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AUTOBOX_METADATA = Metadata(
    id="cb59992f4ec4d434248144323328230a163e219b.boutiques",
    name="3dAutobox",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dAutoboxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_autobox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_autobox(
    input_: InputPathType,
    prefix: str | None = None,
    alt_input: InputPathType | None = None,
    noclust: bool = False,
    extent: bool = False,
    extent_ijk: bool = False,
    extent_ijk_to_file: str | None = None,
    extent_ijk_midslice: bool = False,
    extent_ijkord: bool = False,
    extent_ijkord_to_file: str | None = None,
    extent_xyz_to_file: str | None = None,
    extent_xyz_midslice: bool = False,
    npad: float | None = None,
    npad_safety_on: bool = False,
    runner: Runner | None = None,
) -> V3dAutoboxOutputs:
    """
    Computes size of a box that fits around the volume. Can also be used to crop the
    volume to that box.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAutobox.html
    
    Args:
        input_: Input dataset.
        prefix: Crop the input dataset to the size of the box, and write an\
            output dataset with PREFIX for the name. If not used, no new volume is\
            written out.
        alt_input: An alternate way to specify the input dataset.
        noclust: Don't do any clustering to find the box. Any non-zero voxel\
            will be preserved in the cropped volume.
        extent: Write to standard out the spatial extent of the box.
        extent_ijk: Write out the 6 auto bbox ijk slice numbers to screen: imin\
            imax jmin jmax kmin kmax.
        extent_ijk_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            simple-formatted text file FF: imin imax jmin jmax kmin kmax.
        extent_ijk_midslice: Write out the 3 ijk midslices of the autobox to\
            the screen: imid jmid kmid.
        extent_ijkord: Write out the 6 auto bbox ijk slice numbers to screen in\
            a particular order and format. Useful for scripting.
        extent_ijkord_to_file: Write out the 6 auto bbox ijk slice numbers to a\
            file in a particular order and format. Useful for 3dcalc expressions.
        extent_xyz_to_file: Write out the 6 auto bbox xyz coordinates to a\
            simple-formatted text file GG: xmin xmax ymin ymax zmin zmax.
        extent_xyz_midslice: Write out the 3 xyz midslices of the autobox to\
            the screen: xmid ymid zmid.
        npad: Number of extra voxels to pad on each side of box.
        npad_safety_on: Constrain npad-ded extents to be within dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAutoboxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AUTOBOX_METADATA)
    cargs = []
    cargs.append("3dAutobox")
    cargs.append(execution.input_file(input_))
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if alt_input is not None:
        cargs.extend([
            "-input",
            execution.input_file(alt_input)
        ])
    if noclust:
        cargs.append("-noclust")
    if extent:
        cargs.append("-extent")
    if extent_ijk:
        cargs.append("-extent_ijk")
    if extent_ijk_to_file is not None:
        cargs.extend([
            "-extent_ijk_to_file",
            extent_ijk_to_file
        ])
    if extent_ijk_midslice:
        cargs.append("-extent_ijk_midslice")
    if extent_ijkord:
        cargs.append("-extent_ijkord")
    if extent_ijkord_to_file is not None:
        cargs.extend([
            "-extent_ijkord_to_file",
            extent_ijkord_to_file
        ])
    if extent_xyz_to_file is not None:
        cargs.extend([
            "-extent_xyz_to_file",
            extent_xyz_to_file
        ])
    if extent_xyz_midslice:
        cargs.append("-extent_xyz_midslice")
    if npad is not None:
        cargs.extend([
            "-npad",
            str(npad)
        ])
    if npad_safety_on:
        cargs.append("-npad_safety_on")
    ret = V3dAutoboxOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAutoboxOutputs",
    "V_3D_AUTOBOX_METADATA",
    "v_3d_autobox",
]
