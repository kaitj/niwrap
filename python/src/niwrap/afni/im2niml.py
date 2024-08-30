# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IM2NIML_METADATA = Metadata(
    id="1c277947634c9951683af052380da51d28540e5b",
    name="im2niml",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class Im2nimlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `im2niml(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    niml_output: OutputPathType
    """NIML element"""


def im2niml(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> Im2nimlOutputs:
    """
    im2niml by AFNI Team.
    
    Converts the input image(s) to a text-based NIML element and writes the
    result to stdout.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/im2niml.html
    
    Args:
        input_files: Input image file(s) (e.g. image.jpg).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Im2nimlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IM2NIML_METADATA)
    cargs = []
    cargs.append("im2niml")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.append("[MORE_INPUT_FILES]")
    ret = Im2nimlOutputs(
        root=execution.output_file("."),
        niml_output=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IM2NIML_METADATA",
    "Im2nimlOutputs",
    "im2niml",
]