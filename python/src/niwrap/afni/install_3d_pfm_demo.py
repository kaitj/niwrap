# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INSTALL_3D_PFM_DEMO_METADATA = Metadata(
    id="b63e6980af69869c16da2a38efe308262e4e39c3.boutiques",
    name="Install_3dPFM_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class Install3dPfmDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_3d_pfm_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    readme_file: OutputPathType
    """Instructions for demo usage"""


def install_3d_pfm_demo(
    output_directory: str,
    runner: Runner | None = None,
) -> Install3dPfmDemoOutputs:
    """
    Installs the demo archive for the 3dPFM function.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        output_directory: Output directory where the demo archive will be\
            downloaded and unpacked.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Install3dPfmDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_3D_PFM_DEMO_METADATA)
    cargs = []
    cargs.append("Install_3dPFM_Demo")
    cargs.append(output_directory)
    ret = Install3dPfmDemoOutputs(
        root=execution.output_file("."),
        readme_file=execution.output_file(output_directory + "/README.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_3D_PFM_DEMO_METADATA",
    "Install3dPfmDemoOutputs",
    "install_3d_pfm_demo",
]
