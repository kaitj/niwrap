# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__INSTALL_3D_PFM_DEMO_METADATA = Metadata(
    id="0f9cb4b2fe5d3ed4f3ad4eca9fb9d2d2fb453961.boutiques",
    name="@Install_3dPFM_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VInstall3dPfmDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__install_3d_pfm_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    readme_file: OutputPathType
    """Instructions for demo usage"""


def v__install_3d_pfm_demo(
    output_directory: str,
    runner: Runner | None = None,
) -> VInstall3dPfmDemoOutputs:
    """
    Installs the demo archive for the 3dPFM function.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_3dPFM_Demo.html
    
    Args:
        output_directory: Output directory where the demo archive will be\
            downloaded and unpacked.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VInstall3dPfmDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__INSTALL_3D_PFM_DEMO_METADATA)
    cargs = []
    cargs.append("Install_3dPFM_Demo")
    cargs.append(output_directory)
    ret = VInstall3dPfmDemoOutputs(
        root=execution.output_file("."),
        readme_file=execution.output_file(output_directory + "/README.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VInstall3dPfmDemoOutputs",
    "V__INSTALL_3D_PFM_DEMO_METADATA",
    "v__install_3d_pfm_demo",
]