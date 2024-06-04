# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

STD2IMGCOORD_METADATA = Metadata(
    id="7be566a68eee07d5b0e2af03e9e33ed5e33be910",
    name="std2imgcoord",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Std2imgcoordOutputs(typing.NamedTuple):
    """
    Output object returned when calling `std2imgcoord(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def std2imgcoord(
    filename_coordinates: InputPathType,
    input_image: InputPathType,
    standard_image: InputPathType | None = None,
    affine_transform: InputPathType | None = None,
    warp_field: InputPathType | None = None,
    prewarp_affine_transform: InputPathType | None = None,
    output_mm: bool = False,
    output_vox: bool = False,
    verbose: bool = False,
    more_verbose: bool = False,
    runner: Runner = None,
) -> Std2imgcoordOutputs:
    """
    std2imgcoord by FMRIB Centre.
    
    Convert standard space coordinates to image space coordinates.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        filename_coordinates: Path to the filename containing coordinates or '-'
            to read from standard input
        input_image: Filename of input image
        standard_image: Filename of standard image
        affine_transform: Filename of affine transform (e.g.
            example_func2standard.mat)
        warp_field: Filename of warpfield (e.g. highres2standard_warp.nii.gz)
        prewarp_affine_transform: Filename of pre-warp affine transform (e.g.
            example_func2highres.mat). Defaults to identity matrix.
        output_mm: Outputs coordinates in mm (default)
        output_vox: Outputs coordinates in voxels
        verbose: Verbose output
        more_verbose: More verbose output
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Std2imgcoordOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STD2IMGCOORD_METADATA)
    cargs = []
    cargs.append("std2imgcoord")
    cargs.append("[OPTIONS]")
    cargs.append("<FILENAME_COORDINATES>")
    ret = Std2imgcoordOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "STD2IMGCOORD_METADATA",
    "Std2imgcoordOutputs",
    "std2imgcoord",
]