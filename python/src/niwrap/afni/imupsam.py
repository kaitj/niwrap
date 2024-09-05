# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMUPSAM_METADATA = Metadata(
    id="9286f3f7518042c2bd3883a0415335d2383e812d",
    name="imupsam",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImupsamOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imupsam(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Upsampled image output file"""


def imupsam(
    factor: int,
    input_image: InputPathType,
    output_image: str,
    ascii_flag: bool = False,
    runner: Runner | None = None,
) -> ImupsamOutputs:
    """
    imupsam by AFNI Team.
    
    Upsamples a 2D image by a specified factor.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/imupsam.html
    
    Args:
        factor: Upsampling factor; must be an integer in the range 2 to 30.
        input_image: Path of the input 2D image file.
        output_image: Path of the output upsampled image file. Use '-' to write\
            to stdout.
        ascii_flag: Write the result in ASCII format: all numbers for the file\
            are output, with no header info.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImupsamOutputs`).
    """
    runner = runner or get_global_runner()
    if not (2 <= factor <= 30): 
        raise ValueError(f"'factor' must be between 2 <= x <= 30 but was {factor}")
    execution = runner.start_execution(IMUPSAM_METADATA)
    cargs = []
    cargs.append("imupsam")
    if ascii_flag:
        cargs.append("-A")
    cargs.append(str(factor))
    cargs.append(execution.input_file(input_image))
    cargs.append(output_image)
    ret = ImupsamOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(f"{output_image}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMUPSAM_METADATA",
    "ImupsamOutputs",
    "imupsam",
]