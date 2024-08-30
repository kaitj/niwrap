# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_DFT_METADATA = Metadata(
    id="1f3c907e9349251724f755a698e5ef1d0c5d20dc",
    name="3dDFT",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dDftOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dft(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output dataset file"""
    outheader: OutputPathType
    """Output dataset header file"""


def v_3d_dft(
    infile: InputPathType,
    prefix: str,
    abs_output: bool = False,
    nfft: float | int | None = None,
    detrend: bool = False,
    taper: float | int | None = None,
    inverse: bool = False,
    runner: Runner | None = None,
) -> V3dDftOutputs:
    """
    3dDFT by AFNI Team.
    
    Performs Discrete Fourier Transform (DFT) along the time axis of a complex-
    or float-valued dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dDFT.html
    
    Args:
        infile: Input dataset (complex- or float-valued).
        prefix: Prefix for the output file.
        abs_output: Output float dataset = abs(DFT).
        nfft: DFT length (must be >= number of time points).
        detrend: Least-squares remove linear drift before DFT.
        taper: Fraction (0 <= f <= 1) of data to taper at ends (Hamming taper).
        inverse: Perform the inverse DFT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDftOutputs`).
    """
    runner = runner or get_global_runner()
    if taper is not None and not (0.0 <= taper <= 1.0): 
        raise ValueError(f"'taper' must be between 0.0 <= x <= 1.0 but was {taper}")
    execution = runner.start_execution(V_3D_DFT_METADATA)
    cargs = []
    cargs.append("3dDFT")
    cargs.append(execution.input_file(infile))
    cargs.extend(["-prefix", prefix])
    if abs_output:
        cargs.append("-abs")
    if nfft is not None:
        cargs.extend(["-nfft", str(nfft)])
    if detrend:
        cargs.append("-detrend")
    if taper is not None:
        cargs.extend(["-taper", str(taper)])
    if inverse:
        cargs.append("-inverse")
    ret = V3dDftOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{prefix}+orig.BRIK"),
        outheader=execution.output_file(f"{prefix}+orig.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDftOutputs",
    "V_3D_DFT_METADATA",
    "v_3d_dft",
]