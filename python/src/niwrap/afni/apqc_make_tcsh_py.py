# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APQC_MAKE_TCSH_PY_METADATA = Metadata(
    id="8fcca63c2c3568b6ddc9e9982d804d3b7e550688.boutiques",
    name="apqc_make_tcsh.py",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class ApqcMakeTcshPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apqc_make_tcsh_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    qc_html: OutputPathType
    """Quality Control HTML file generated by APQC."""


def apqc_make_tcsh_py(
    uvar_json: InputPathType,
    subj_dir: str,
    review_style: str | None = None,
    mot_grayplot_off: bool = False,
    vstat_list: list[str] | None = None,
    runner: Runner | None = None,
) -> ApqcMakeTcshPyOutputs:
    """
    This program creates the single subject (ss) HTML review script
    '@ss_review_html' which generates images and text for the afni_proc.py quality
    control (APQC) HTML.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/apqc_make_tcsh.py.html
    
    Args:
        uvar_json: Text file of user variables created by gen_ss_review.py that\
            catalogs important files in the results directory for the APQC.
        subj_dir: Location of AP results directory (often '.', as this program\
            is often run from within the AP results directory).
        review_style: The 'style' of the APQC HTML output HTML. Allowed\
            keywords are: {none, basic, pythonic}. Using 'pythonic' is recommended.
        mot_grayplot_off: Turn off the grayplot generation. This option was\
            created for a specific case with a large dataset. Not recommended to\
            use generally.
        vstat_list: Provide a list of label items to specify which volume's\
            images should appear in the vstat QC block. Each item should correspond\
            to subbrick label basename in the stats_dset. 'Full_Fstat' is always\
            included. If not used, default logic picks up to 5 items to show.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApqcMakeTcshPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APQC_MAKE_TCSH_PY_METADATA)
    cargs = []
    cargs.append("apqc_make_tcsh.py")
    cargs.extend([
        "-uvar_json",
        execution.input_file(uvar_json)
    ])
    cargs.extend([
        "-subj_dir",
        subj_dir
    ])
    if review_style is not None:
        cargs.extend([
            "-review_style",
            review_style
        ])
    if mot_grayplot_off:
        cargs.append("-mot_grayplot_off")
    if vstat_list is not None:
        cargs.extend([
            "-vstat_list",
            *vstat_list
        ])
    ret = ApqcMakeTcshPyOutputs(
        root=execution.output_file("."),
        qc_html=execution.output_file("qc_*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APQC_MAKE_TCSH_PY_METADATA",
    "ApqcMakeTcshPyOutputs",
    "apqc_make_tcsh_py",
]
