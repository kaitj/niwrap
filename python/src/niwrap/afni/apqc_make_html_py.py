# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APQC_MAKE_HTML_PY_METADATA = Metadata(
    id="1cc63e58e9b64d6635146ce733bef0bda4712a25.boutiques",
    name="apqc_make_html.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ApqcMakeHtmlPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apqc_make_html_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def apqc_make_html_py(
    qc_dir: str,
    runner: Runner | None = None,
) -> ApqcMakeHtmlPyOutputs:
    """
    Tool to generate HTML reports.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/apqc_make_html.py.html
    
    Args:
        qc_dir: Directory where QC files will be saved.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApqcMakeHtmlPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APQC_MAKE_HTML_PY_METADATA)
    cargs = []
    cargs.append("apqc_make_html.py")
    cargs.append("-qc_dir")
    cargs.append(qc_dir)
    ret = ApqcMakeHtmlPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APQC_MAKE_HTML_PY_METADATA",
    "ApqcMakeHtmlPyOutputs",
    "apqc_make_html_py",
]
