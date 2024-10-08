# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_CDIFLIST_TO_GRADS_PY_METADATA = Metadata(
    id="3af0782a4a10f77f0152928db451c26a4a27a4b6.boutiques",
    name="convert_cdiflist_to_grads.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ConvertCdiflistToGradsPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_cdiflist_to_grads_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rvec: OutputPathType
    """Row-format of gradients (unit magnitude)."""
    output_bval: OutputPathType
    """Row-format of bvals."""
    output_cvec: OutputPathType
    """Col-format of gradients (scaled by b-values)."""


def convert_cdiflist_to_grads_py(
    cdiflist: InputPathType,
    bval_max: float,
    prefix: str,
    ver: bool = False,
    date: bool = False,
    help_: bool = False,
    hview: bool = False,
    runner: Runner | None = None,
) -> ConvertCdiflistToGradsPyOutputs:
    """
    This program reads in a GE cdiflist and outputs gradient file and file of
    bvalues for subsequent processing.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/convert_cdiflist_to_grads.py.html
    
    Args:
        cdiflist: Name(s) of cdiflist text file output by GE scanners when\
            acquiring DWIs.
        bval_max: Max bvalue used, which provides a reference value for scaling\
            everything else.
        prefix: Output basename for the subsequent grad and bvalue files\
            (suffix and extensions will be added).
        ver: Display current version.
        date: Display release/editing date of current version.
        help_: Display help in terminal.
        hview: Display help in terminal.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertCdiflistToGradsPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_CDIFLIST_TO_GRADS_PY_METADATA)
    cargs = []
    cargs.append("convert_cdiflist_to_grads.py")
    cargs.append("-cdiflist")
    cargs.extend([
        "-cdiflist",
        execution.input_file(cdiflist)
    ])
    cargs.append("-bval_max")
    cargs.extend([
        "-bval_max",
        str(bval_max)
    ])
    cargs.append("-prefix")
    cargs.extend([
        "-prefix",
        prefix
    ])
    if ver:
        cargs.append("-ver")
    if date:
        cargs.append("-date")
    if help_:
        cargs.append("-help")
    if hview:
        cargs.append("-h")
    ret = ConvertCdiflistToGradsPyOutputs(
        root=execution.output_file("."),
        output_rvec=execution.output_file(prefix + "_rvec.dat"),
        output_bval=execution.output_file(prefix + "_bval.dat"),
        output_cvec=execution.output_file(prefix + "_cvec.dat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_CDIFLIST_TO_GRADS_PY_METADATA",
    "ConvertCdiflistToGradsPyOutputs",
    "convert_cdiflist_to_grads_py",
]
