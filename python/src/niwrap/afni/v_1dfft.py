# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DFFT_METADATA = Metadata(
    id="bfbe0649f04d4738ad777521fd804d6932aecfa7.boutiques",
    name="1dfft",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dfftOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dfft(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_fft: OutputPathType
    """Output file with the absolute value of the FFT of the input columns."""


def v_1dfft(
    infile: InputPathType,
    outfile: str,
    ignore: float | None = None,
    use: float | None = None,
    nfft: float | None = None,
    tocx: bool = False,
    fromcx: bool = False,
    hilbert: bool = False,
    nodetrend: bool = False,
    runner: Runner | None = None,
) -> V1dfftOutputs:
    """
    Compute the absolute value of the FFT of input columns from an AFNI 1D file.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dfft.html
    
    Args:
        infile: Input .1D file containing an ASCII list of numbers arranged in\
            columns.
        outfile: Output file to store the FFT results.
        ignore: Skip the first 'sss' lines in the input file. [default = no\
            skipping].
        use: Use only 'uuu' lines of the input file. [default = use them all].
        nfft: Set FFT length to 'nnn'. [default = length of data (# of lines\
            used)].
        tocx: Save Re and Im parts of transform in 2 columns.
        fromcx: Convert 2 column complex input into 1 column real output. Note:\
            This will not work if the original data FFT length was an odd number.
        hilbert: When -fromcx is used, the inverse FFT will do the Hilbert\
            transform instead.
        nodetrend: Skip the detrending of the input.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dfftOutputs`).
    """
    if ignore is not None and not (0 <= ignore): 
        raise ValueError(f"'ignore' must be greater than 0 <= x but was {ignore}")
    if use is not None and not (0 <= use): 
        raise ValueError(f"'use' must be greater than 0 <= x but was {use}")
    if nfft is not None and not (1 <= nfft): 
        raise ValueError(f"'nfft' must be greater than 1 <= x but was {nfft}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DFFT_METADATA)
    cargs = []
    cargs.append("1dfft")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if ignore is not None:
        cargs.extend([
            "-ignore",
            str(ignore)
        ])
    if use is not None:
        cargs.extend([
            "-use",
            str(use)
        ])
    if nfft is not None:
        cargs.extend([
            "-nfft",
            str(nfft)
        ])
    if tocx:
        cargs.append("-tocx")
    if fromcx:
        cargs.append("-fromcx")
    if hilbert:
        cargs.append("-hilbert")
    if nodetrend:
        cargs.append("-nodetrend")
    ret = V1dfftOutputs(
        root=execution.output_file("."),
        out_fft=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dfftOutputs",
    "V_1DFFT_METADATA",
    "v_1dfft",
]
