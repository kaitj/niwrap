# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMAXDISP_METADATA = Metadata(
    id="f43c66735d941596c417c4b7d4ad6b1b4f1e4608",
    name="3dmaxdisp",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaxdispOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaxdisp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    displacement_output: OutputPathType
    """Results showing average and maximum displacements."""


def v_3dmaxdisp(
    inset: InputPathType,
    matrix: InputPathType,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dmaxdispOutputs:
    """
    3dmaxdisp by AFNI Team.
    
    Reads in a 3D dataset and a DICOM-based affine matrix to output the average
    and maximum displacement applied to the edge voxels of the 3D dataset's
    automask.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmaxdisp.html
    
    Args:
        inset: Input dataset file used to form the mask over which\
            displacements will be computed.
        matrix: 3x4 affine transformation matrix file applied to the\
            coordinates of the voxels in the dataset mask.
        verbose: Print a few progress reports.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaxdispOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMAXDISP_METADATA)
    cargs = []
    cargs.append("3dmaxdisp")
    cargs.extend(["-inset", execution.input_file(inset)])
    cargs.extend(["-matrix", execution.input_file(matrix)])
    if verbose:
        cargs.append("-verb")
    ret = V3dmaxdispOutputs(
        root=execution.output_file("."),
        displacement_output=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaxdispOutputs",
    "V_3DMAXDISP_METADATA",
    "v_3dmaxdisp",
]