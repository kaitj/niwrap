# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ADJUNCT_VOL_3SLICE_SELECT_METADATA = Metadata(
    id="9d2e316549deea2f5e976b40728b81fb4fa220f4",
    name="adjunct_vol_3slice_select",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AdjunctVol3sliceSelectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_vol_3slice_select(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    ijk_output: OutputPathType
    """File that contains the output indices i j k."""


def adjunct_vol_3slice_select(
    dataset_file: InputPathType,
    coord_x: float | int,
    coord_y: float | int,
    coord_z: float | int,
    runner: Runner | None = None,
) -> AdjunctVol3sliceSelectOutputs:
    """
    adjunct_vol_3slice_select by AFNI Team.
    
    Helper script to convert (x, y, z) coordinates to (i, j, k) indices for a
    dataset. It will return an error if any indices are outside the dataset's
    matrix.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@djunct_vol_3slice_select.html
    
    Args:
        dataset_file: The name of the dataset file.
        coord_x: The x-coordinate in the dataset.
        coord_y: The y-coordinate in the dataset.
        coord_z: The z-coordinate in the dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctVol3sliceSelectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_VOL_3SLICE_SELECT_METADATA)
    cargs = []
    cargs.append("adjunct_vol_3slice_select")
    cargs.append(execution.input_file(dataset_file))
    cargs.append(str(coord_x))
    cargs.append(str(coord_y))
    cargs.append(str(coord_z))
    ret = AdjunctVol3sliceSelectOutputs(
        root=execution.output_file("."),
        ijk_output=execution.output_file(f"ijk_indices.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_VOL_3SLICE_SELECT_METADATA",
    "AdjunctVol3sliceSelectOutputs",
    "adjunct_vol_3slice_select",
]