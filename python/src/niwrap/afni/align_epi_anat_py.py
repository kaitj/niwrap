# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ALIGN_EPI_ANAT_PY_METADATA = Metadata(
    id="950ee15ab0ff82fde109bdb6781edc6e57a40a8c.boutiques",
    name="align_epi_anat.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class AlignEpiAnatPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `align_epi_anat_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    anat_aligned: OutputPathType
    """A version of the anatomy that is aligned to the EPI"""
    epi_aligned: OutputPathType
    """A version of the EPI dataset aligned to the Anatomy"""


def align_epi_anat_py(
    epi: InputPathType,
    anat: InputPathType,
    epi_base: str,
    runner: Runner | None = None,
) -> AlignEpiAnatPyOutputs:
    """
    Align EPI to anatomical datasets or vice versa.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/align_epi_anat.py.html
    
    Args:
        epi: EPI dataset to align or to which to align.
        anat: Anatomical dataset to align or to which to align.
        epi_base: Base sub-brick to use for alignment\
            (0/mean/median/max/subbrick#).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AlignEpiAnatPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ALIGN_EPI_ANAT_PY_METADATA)
    cargs = []
    cargs.append("align_epi_anat.py")
    cargs.extend([
        "-epi",
        execution.input_file(epi)
    ])
    cargs.extend([
        "-anat",
        execution.input_file(anat)
    ])
    cargs.extend([
        "-epi_base",
        epi_base
    ])
    cargs.append("[OUTPUT_OPTIONS]")
    cargs.append("[ALIGNMENT_OPTIONS]")
    cargs.append("[PREPROCESSING_OPTIONS]")
    ret = AlignEpiAnatPyOutputs(
        root=execution.output_file("."),
        anat_aligned=execution.output_file("[ANAT]+orig"),
        epi_aligned=execution.output_file("[EPI]+orig"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ALIGN_EPI_ANAT_PY_METADATA",
    "AlignEpiAnatPyOutputs",
    "align_epi_anat_py",
]
