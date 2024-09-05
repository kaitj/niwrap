# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FIRST_METADATA = Metadata(
    id="8bc389023ba8ba5dabd7d2c7064b7839d244a275",
    name="first",
)


class FirstOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output_image: OutputPathType
    """Segmented output image"""


def first(
    input_file: InputPathType,
    output_name: str,
    input_model: InputPathType,
    flirt_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    input_model2: InputPathType | None = None,
    nmodes: float | int | None = None,
    intref: bool = False,
    multi_image_input: bool = False,
    binary_surface_output: bool = False,
    bmap_name: InputPathType | None = None,
    bvars: InputPathType | None = None,
    shcond: bool = False,
    loadbvars: bool = False,
    runner: Runner | None = None,
) -> FirstOutputs:
    """
    first by Brian Patenaude, University of Oxford.
    
    A command-line tool for segmenting subcortical structures in MRI images
    using models and transformations.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST
    
    Args:
        input_file: Filename of input image to be segmented.
        output_name: Output name.
        input_model: Filename of input model (the structure to be segmented).
        flirt_matrix: Filename of flirt matrix that transform input image to\
            MNI space (output of first_flirt).
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        input_model2: Filename of second input model (the structure to be\
            segmented).
        nmodes: Specifies number of modes used.
        intref: Use structure specified by modelname2 as intensity reference.
        multi_image_input: Use structure specified by modelname2 as intensity\
            reference.
        binary_surface_output: Use structure specified by modelname2 as\
            intensity reference.
        bmap_name: Filename of conditional mapping matrix.
        bvars: Initialize using bvars from a previous segmentation. When using\
            with --shcond specifies the shape of the structure we are conditioning\
            on.
        shcond: Use conditional shape probability.
        loadbvars: Load initial parameter estimates from a previous\
            segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_METADATA)
    cargs = []
    cargs.append("first")
    cargs.extend(["-i", execution.input_file(input_file)])
    cargs.extend(["-k", output_name])
    cargs.extend(["-m", execution.input_file(input_model)])
    cargs.extend(["-l", execution.input_file(flirt_matrix)])
    if verbose:
        cargs.append("-v")
    if help_:
        cargs.append("-h")
    if input_model2 is not None:
        cargs.extend(["-p", execution.input_file(input_model2)])
    if nmodes is not None:
        cargs.extend(["-n", str(nmodes)])
    if intref:
        cargs.append("--intref")
    if multi_image_input:
        cargs.append("--multiImageInput")
    if binary_surface_output:
        cargs.append("--binarySurfaceOutput")
    if bmap_name is not None:
        cargs.extend(["-b", execution.input_file(bmap_name)])
    if bvars is not None:
        cargs.extend(["-o", execution.input_file(bvars)])
    if shcond:
        cargs.append("--shcond")
    if loadbvars:
        cargs.append("--loadbvars")
    ret = FirstOutputs(
        root=execution.output_file("."),
        segmented_output_image=execution.output_file(f"{output_name}_seg.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIRST_METADATA",
    "FirstOutputs",
    "first",
]