# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INSTALL_RSFMRI_MOTION_GROUP_DEMO_METADATA = Metadata(
    id="df3e938409986890aec3704877c4b5f0ab93b6cf.boutiques",
    name="Install_RSFMRI_Motion_Group_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class InstallRsfmriMotionGroupDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_rsfmri_motion_group_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    afni_demo_dir: OutputPathType
    """Directory where the demo data and scripts are set up."""


def install_rsfmri_motion_group_demo(
    output_dir: str,
    runner: Runner | None = None,
) -> InstallRsfmriMotionGroupDemoOutputs:
    """
    Installs and sets up an AFNI InstaCorr demo archive, based on 190 Cambridge
    subjects from FCON_1000.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        output_dir: Directory where the AFNI_Demo_Motion_Groups will be set up.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallRsfmriMotionGroupDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_RSFMRI_MOTION_GROUP_DEMO_METADATA)
    cargs = []
    cargs.append("@Install_RSFMRI_Motion_Group_Demo")
    cargs.append(output_dir)
    ret = InstallRsfmriMotionGroupDemoOutputs(
        root=execution.output_file("."),
        afni_demo_dir=execution.output_file(output_dir + "/AFNI_Demo_Motion_Groups"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_RSFMRI_MOTION_GROUP_DEMO_METADATA",
    "InstallRsfmriMotionGroupDemoOutputs",
    "install_rsfmri_motion_group_demo",
]
