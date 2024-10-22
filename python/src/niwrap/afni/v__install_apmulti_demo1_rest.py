# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_APMULTI_DEMO1_REST_METADATA = Metadata(
    id="67ee41d319b3699e09aba05f6d2960afa86010a5.boutiques",
    name="@Install_APMULTI_Demo1_rest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallApmultiDemo1RestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_apmulti_demo1_rest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_apmulti_demo1_rest(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> VInstallApmultiDemo1RestOutputs:
    """
    This script fetches the demo data and scripts corresponding to AFNI's Demo #1
    for processing multi-echo FMRI data (rest).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallApmultiDemo1RestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_APMULTI_DEMO1_REST_METADATA)
    cargs = []
    cargs.append("@Install_APMULTI_Demo1_rest")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = VInstallApmultiDemo1RestOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallApmultiDemo1RestOutputs",
    "V__INSTALL_APMULTI_DEMO1_REST_METADATA",
    "v__install_apmulti_demo1_rest",
]
