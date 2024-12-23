# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__SUMA_MAKE_SPEC_SF_METADATA = Metadata(
    id="e84849d3eeb33bb18d791b3e555fb699941d3809.boutiques",
    name="@SUMA_Make_Spec_SF",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VSumaMakeSpecSfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__suma_make_spec_sf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """All created files are stored in SURFACES directory"""


def v__suma_make_spec_sf(
    subject_id: str,
    debug_level: int | None = None,
    surface_path: str | None = None,
    runner: Runner | None = None,
) -> VSumaMakeSpecSfOutputs:
    """
    Prepare for surface viewing in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subject_id: Required subject ID for file naming.
        debug_level: Print debug information along the way.
        surface_path: Path to directory containing 'SURFACES' and AFNI volume\
            used in creating the surfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VSumaMakeSpecSfOutputs`).
    """
    if debug_level is not None and not (debug_level <= 2): 
        raise ValueError(f"'debug_level' must be less than x <= 2 but was {debug_level}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__SUMA_MAKE_SPEC_SF_METADATA)
    cargs = []
    cargs.append("@SUMA_Make_Spec_SF")
    if debug_level is not None:
        cargs.extend([
            "-debug",
            str(debug_level)
        ])
    if surface_path is not None:
        cargs.extend([
            "-sfpath",
            surface_path
        ])
    cargs.extend([
        "-sid",
        subject_id
    ])
    ret = VSumaMakeSpecSfOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("SURFACES/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VSumaMakeSpecSfOutputs",
    "V__SUMA_MAKE_SPEC_SF_METADATA",
    "v__suma_make_spec_sf",
]
