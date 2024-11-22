# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_BANDPASS_METADATA = Metadata(
    id="c70317bd402feee3b10b4b0a4bdd6a544f0ec629.boutiques",
    name="3dBandpass",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dBandpassOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_bandpass(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output file from 3dbandpass."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_bandpass(
    highpass: float,
    in_file: InputPathType,
    lowpass: float,
    automask: bool = False,
    blur: float | None = None,
    despike: bool = False,
    local_pv: float | None = None,
    mask: InputPathType | None = None,
    nfft: int | None = None,
    no_detrend: bool = False,
    normalize: bool = False,
    notrans: bool = False,
    orthogonalize_dset: InputPathType | None = None,
    orthogonalize_file: list[InputPathType] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    tr: float | None = None,
    runner: Runner | None = None,
) -> V3dBandpassOutputs:
    """
    Program to lowpass and/or highpass each voxel time series in a dataset, offering
    more/different options than Fourier.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        highpass: Highpass.
        in_file: Input file to 3dbandpass.
        lowpass: Lowpass.
        automask: Create a mask from the input dataset.
        blur: Blur (inside the mask only) with a filter width (fwhm) of 'fff'\
            millimeters.
        despike: Despike each time series before other processing. hopefully,\
            you don't actually need to do this, which is why it is optional.
        local_pv: Replace each vector by the local principal vector (aka first\
            singular vector) from a neighborhood of radius 'rrr' millimeters. note\
            that the pv time series is l2 normalized. this option is mostly for bob\
            cox to have fun with.
        mask: Mask file.
        nfft: Set the fft length [must be a legal value].
        no_detrend: Skip the quadratic detrending of the input that occurs\
            before the fft-based bandpassing. you would only want to do this if the\
            dataset had been detrended already in some other program.
        normalize: Make all output time series have l2 norm = 1 (i.e., sum of\
            squares = 1).
        notrans: Don't check for initial positive transients in the data. the\
            test is a little slow, so skipping it is ok, if you know the data time\
            series are transient-free.
        orthogonalize_dset: Orthogonalize each voxel to the corresponding voxel\
            time series in dataset 'fset', which must have the same spatial and\
            temporal grid structure as the main input dataset. at present, only one\
            '-dsort' option is allowed.
        orthogonalize_file: Also orthogonalize input to columns in f.1d.\
            multiple '-ort' options are allowed.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        tr: Set time step (tr) in sec [default=from dataset header].
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBandpassOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BANDPASS_METADATA)
    cargs = []
    cargs.append("3dBandpass")
    if automask:
        cargs.append("-automask")
    if blur is not None:
        cargs.extend([
            "-blur",
            str(blur)
        ])
    if despike:
        cargs.append("-despike")
    cargs.append(str(highpass))
    cargs.append(execution.input_file(in_file))
    if local_pv is not None:
        cargs.extend([
            "-localPV",
            str(local_pv)
        ])
    cargs.append(str(lowpass))
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if nfft is not None:
        cargs.extend([
            "-nfft",
            str(nfft)
        ])
    if no_detrend:
        cargs.append("-nodetrend")
    if normalize:
        cargs.append("-norm")
    if notrans:
        cargs.append("-notrans")
    if orthogonalize_dset is not None:
        cargs.extend([
            "-dsort",
            execution.input_file(orthogonalize_dset)
        ])
    if orthogonalize_file is not None:
        cargs.extend([
            "-ort",
            *[execution.input_file(f) for f in orthogonalize_file]
        ])
    if outputtype is not None:
        cargs.append(outputtype)
    if tr is not None:
        cargs.extend([
            "-dt",
            str(tr)
        ])
    ret = V3dBandpassOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(in_file).name + "_bp"),
        out_file_=execution.output_file("out_file"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBandpassOutputs",
    "V_3D_BANDPASS_METADATA",
    "v_3d_bandpass",
]
