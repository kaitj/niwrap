# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_INSTA_CORR_DEMO_METADATA = Metadata(
    id="7f4f6b252fff2b3ada398e7114eeff68065918dd.boutiques",
    name="@Install_InstaCorr_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstallInstaCorrDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_insta_corr_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__install_insta_corr_demo(
    wget: bool = False,
    curl: bool = False,
    full: bool = False,
    mini: bool = False,
    runner: Runner | None = None,
) -> VInstallInstaCorrDemoOutputs:
    """
    Installs and sets up AFNI's InstaCorr demo archive.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_InstaCorr_Demo.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        full: Install the full version of the demo. Downloads all subject\
            surfaces, resting state volume time series, etc. The script processes\
            the data and produces the files needed for running the various\
            interactive InstaCorr demos.
        mini: Install the mini version of the demo. Downloads only the files\
            needed for running the various interactive InstaCorr demos.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstallInstaCorrDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_INSTA_CORR_DEMO_METADATA)
    cargs = []
    cargs.append("@Install_InstaCorr_Demo")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    if full:
        cargs.append("-full")
    if mini:
        cargs.append("-mini")
    ret = VInstallInstaCorrDemoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstallInstaCorrDemoOutputs",
    "V__INSTALL_INSTA_CORR_DEMO_METADATA",
    "v__install_insta_corr_demo",
]