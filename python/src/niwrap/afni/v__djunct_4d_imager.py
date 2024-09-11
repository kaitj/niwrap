# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__DJUNCT_4D_IMAGER_METADATA = Metadata(
    id="14809aab601922358a6256d966a2cc6c07d0aaf8.boutiques",
    name="@djunct_4d_imager",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VDjunct4dImagerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_4d_imager(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    onescl_png: OutputPathType
    """Output montage image with constant brightness range"""
    sepscl_png: OutputPathType
    """Output montage image with varying brightness range"""
    onescl_mpeg: OutputPathType
    """Output movie with constant brightness range (one slice at a time)"""
    sepscl_mpeg: OutputPathType
    """Output movie with varying brightness range (one slice at a time)"""
    onescl_gif: OutputPathType
    """Output animated GIF with constant brightness range (one slice at a
    time)"""
    sepscl_gif: OutputPathType
    """Output animated GIF with varying brightness range (one slice at a
    time)"""


def v__djunct_4d_imager(
    inset: InputPathType,
    prefix: str,
    do_movie: typing.Literal["MPEG", "AGIF"] | None = None,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunct4dImagerOutputs:
    """
    The program is useful for viewing the same slice across the 'time' dimension of
    a 4D data set.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@djunct_4d_imager.html
    
    Args:
        inset: ULay dataset, probably 4D (required).
        prefix: Prefix for output files (required).
        do_movie: Specify type of movie file. Options: MPEG, AGIF.
        no_clean: Keep the final intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunct4dImagerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_4D_IMAGER_METADATA)
    cargs = []
    cargs.append("@djunct_4d_imager")
    cargs.append(execution.input_file(inset))
    cargs.append(prefix)
    if do_movie is not None:
        cargs.extend([
            "-do_movie",
            do_movie
        ])
    if no_clean:
        cargs.append("-no_clean")
    ret = VDjunct4dImagerOutputs(
        root=execution.output_file("."),
        onescl_png=execution.output_file(prefix + "_onescl.png"),
        sepscl_png=execution.output_file(prefix + "_sepscl.png"),
        onescl_mpeg=execution.output_file(prefix + "_onescl.mpg"),
        sepscl_mpeg=execution.output_file(prefix + "_sepscl.mpg"),
        onescl_gif=execution.output_file(prefix + "_onescl.gif"),
        sepscl_gif=execution.output_file(prefix + "_sepscl.gif"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VDjunct4dImagerOutputs",
    "V__DJUNCT_4D_IMAGER_METADATA",
    "v__djunct_4d_imager",
]