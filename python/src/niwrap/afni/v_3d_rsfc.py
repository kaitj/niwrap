# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_RSFC_METADATA = Metadata(
    id="6ce9640d970ae6c3fe9057ee6cdd1cbb5363c7cb.boutiques",
    name="3dRSFC",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dRsfcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rsfc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_time_series: OutputPathType
    """Filtered time series output"""
    un_bandpassed_series: OutputPathType
    """Un-bandpassed series output"""


def v_3d_rsfc(
    fbot: float,
    ftop: float,
    input_dataset: InputPathType,
    runner: Runner | None = None,
) -> V3dRsfcOutputs:
    """
    Program to calculate common resting state functional connectivity (RSFC)
    parameters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        fbot: Lowest frequency in the passband, in Hz.
        ftop: Highest frequency in the passband (must be > fbot).
        input_dataset: Input dataset (3D+time sequence of volumes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRsfcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_RSFC_METADATA)
    cargs = []
    cargs.append("3dRSFC")
    cargs.append("[OPTIONS]")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(execution.input_file(input_dataset))
    ret = V3dRsfcOutputs(
        root=execution.output_file("."),
        filtered_time_series=execution.output_file("[PREFIX]_LFF+orig.*"),
        un_bandpassed_series=execution.output_file("[PREFIX]_unBP+orig.*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dRsfcOutputs",
    "V_3D_RSFC_METADATA",
    "v_3d_rsfc",
]
