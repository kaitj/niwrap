# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_MRS_PROC_METADATA = Metadata(
    id="5fd108d3b19ebf7c9e48acb899701457a3805385.boutiques",
    name="fsl_mrs_proc",
    package="fsl",
)


class FslMrsProcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_mrs_proc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_mrs_proc(
    runner: Runner | None = None,
) -> FslMrsProcOutputs:
    """
    FSL Magnetic Resonance Spectroscopy - Preprocessing.
    
    Author: FMRIB Centre, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslMrsProcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_MRS_PROC_METADATA)
    cargs = []
    cargs.append("fsl_mrs_proc")
    cargs.append("[GLOBAL_OPTIONS]")
    cargs.append("<subcommand>")
    cargs.append("[SUBCOMMAND_OPTIONS]")
    ret = FslMrsProcOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_MRS_PROC_METADATA",
    "FslMrsProcOutputs",
    "fsl_mrs_proc",
]