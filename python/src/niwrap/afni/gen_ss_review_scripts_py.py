# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GEN_SS_REVIEW_SCRIPTS_PY_METADATA = Metadata(
    id="16eed874bc29353419a6980c49154f8020611189.boutiques",
    name="gen_ss_review_scripts.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class GenSsReviewScriptsPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gen_ss_review_scripts_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    basic_review: OutputPathType
    """Basic review script output"""
    driver_review: OutputPathType
    """Driver review script output"""
    driver_commands: OutputPathType
    """Driver commands script output"""


def gen_ss_review_scripts_py(
    runner: Runner | None = None,
) -> GenSsReviewScriptsPyOutputs:
    """
    Generate single subject analysis review scripts.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/gen_ss_review_scripts.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GenSsReviewScriptsPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GEN_SS_REVIEW_SCRIPTS_PY_METADATA)
    cargs = []
    cargs.append("gen_ss_review_scripts.py")
    cargs.append("[INPUT_FILES]")
    cargs.append("[OPTIONS]")
    ret = GenSsReviewScriptsPyOutputs(
        root=execution.output_file("."),
        basic_review=execution.output_file("./@ss_review_basic"),
        driver_review=execution.output_file("./@ss_review_driver"),
        driver_commands=execution.output_file("./@ss_review_driver_commands"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GEN_SS_REVIEW_SCRIPTS_PY_METADATA",
    "GenSsReviewScriptsPyOutputs",
    "gen_ss_review_scripts_py",
]