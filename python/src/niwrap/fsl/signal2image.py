# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIGNAL2IMAGE_METADATA = Metadata(
    id="ee51e599579afe1ad9e1eb37382cd7781755836a.boutiques",
    name="signal2image",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class Signal2imageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `signal2image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType | None
    """The resultant image file from the input signal and pulse sequence."""
    kspace_outfile: OutputPathType | None
    """The resultant k-space file."""


def signal2image(
    pulse_sequence: InputPathType,
    input_signal: InputPathType | None = None,
    output_image: str | None = None,
    kspace_coordinates: InputPathType | None = None,
    output_kspace: str | None = None,
    abs_flag: bool = False,
    homodyne_flag: bool = False,
    verbose_flag: bool = False,
    apodize_flag: bool = False,
    cutoff: float | None = 100,
    rolloff: float | None = 10,
    save_flag: bool = False,
    runner: Runner | None = None,
) -> Signal2imageOutputs:
    """
    A tool for converting MR signal data to images using specified k-space
    coordinates and pulse sequences.
    
    Author: University of Oxford (Mark Jenkinson & Ivana Drobnjak)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        pulse_sequence: 8-column pulse_sequence matrix. Expects to find all\
            other pulse sequence files in the same directory.
        input_signal: Input signal file.
        output_image: Output image file.
        kspace_coordinates: K-space coordinates file.
        output_kspace: Output k-space file.
        abs_flag: Save absolute magnitude and phase.
        homodyne_flag: Do the homodyne reconstruction.
        verbose_flag: Switch on diagnostic messages.
        apodize_flag: Do apodization.
        cutoff: Apodization with this cutoff; default 100.
        rolloff: Apodization with this rolloff; default 10.
        save_flag: Save window as ASCII matrix (DEBUG!).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Signal2imageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGNAL2IMAGE_METADATA)
    cargs = []
    cargs.append("signal2image")
    cargs.extend([
        "-p",
        execution.input_file(pulse_sequence)
    ])
    if input_signal is not None:
        cargs.extend([
            "-i",
            execution.input_file(input_signal)
        ])
    if output_image is not None:
        cargs.extend([
            "-o",
            output_image
        ])
    if kspace_coordinates is not None:
        cargs.extend([
            "-c",
            execution.input_file(kspace_coordinates)
        ])
    if output_kspace is not None:
        cargs.extend([
            "-k",
            output_kspace
        ])
    if abs_flag:
        cargs.append("-a")
    if homodyne_flag:
        cargs.append("--homo")
    if verbose_flag:
        cargs.append("-v")
    if apodize_flag:
        cargs.append("-z")
    if cutoff is not None:
        cargs.extend([
            "-l",
            str(cutoff)
        ])
    if rolloff is not None:
        cargs.extend([
            "-r",
            str(rolloff)
        ])
    if save_flag:
        cargs.append("-s")
    ret = Signal2imageOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(output_image) if (output_image is not None) else None,
        kspace_outfile=execution.output_file(output_kspace) if (output_kspace is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIGNAL2IMAGE_METADATA",
    "Signal2imageOutputs",
    "signal2image",
]
