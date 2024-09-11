# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__EXTRACT_MEICA_ORTVEC_METADATA = Metadata(
    id="8c025b037f2f85a5a7f3a6b1ead831118fcdc316.boutiques",
    name="@extract_meica_ortvec",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VExtractMeicaOrtvecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__extract_meica_ortvec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output 1D ortvec file"""


def v__extract_meica_ortvec(
    prefix: str,
    meica_dir: str | None = None,
    reject_ignored: int | None = None,
    reject_midk: int | None = None,
    work_dir: str | None = None,
    verbosity: str | None = None,
    runner: Runner | None = None,
) -> VExtractMeicaOrtvecOutputs:
    """
    Project good MEICA components out of bad ones.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@extract_meica_ortvec.html
    
    Args:
        prefix: Name for output 1D ortvec file.
        meica_dir: Directory for MEICA files.
        reject_ignored: Do we reject ignored components (0=keep, 1=reject),\
            default is 0.
        reject_midk: Do we reject midk components (0=keep, 1=reject), default\
            is 1.
        work_dir: Sub-directory for work.
        verbosity: Set verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VExtractMeicaOrtvecOutputs`).
    """
    if reject_ignored is not None and not (0 <= reject_ignored <= 1): 
        raise ValueError(f"'reject_ignored' must be between 0 <= x <= 1 but was {reject_ignored}")
    if reject_midk is not None and not (0 <= reject_midk <= 1): 
        raise ValueError(f"'reject_midk' must be between 0 <= x <= 1 but was {reject_midk}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__EXTRACT_MEICA_ORTVEC_METADATA)
    cargs = []
    cargs.append("@extract_meica_ortvec")
    cargs.extend([
        "-prefix",
        prefix
    ])
    if meica_dir is not None:
        cargs.extend([
            "-meica_dir",
            meica_dir
        ])
    if reject_ignored is not None:
        cargs.extend([
            "-reject_ignored",
            str(reject_ignored)
        ])
    if reject_midk is not None:
        cargs.extend([
            "-reject_midk",
            str(reject_midk)
        ])
    if work_dir is not None:
        cargs.extend([
            "-work_dir",
            work_dir
        ])
    if verbosity is not None:
        cargs.extend([
            "-verb",
            verbosity
        ])
    ret = VExtractMeicaOrtvecOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(prefix + ".1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VExtractMeicaOrtvecOutputs",
    "V__EXTRACT_MEICA_ORTVEC_METADATA",
    "v__extract_meica_ortvec",
]