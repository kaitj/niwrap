# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


DWI2TENSOR_METADATA = Metadata(
    id="6de247fcb34ba8e697e30249bce5a1d41889ca65",
    name="dwi2tensor",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Dwi2tensorFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in FSL bvecs/bvals format files. If a diffusion gradient scheme is present in the input image header, the data provided with this option will be instead used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-fslgrad")
        cargs.extend(["", execution.input_file(self.bvecs)])
        cargs.extend(["", execution.input_file(self.bvals)])
        return cargs


@dataclasses.dataclass
class Dwi2tensorConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class Dwi2tensorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwi2tensor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dt: OutputPathType
    """the output dt image."""
    b0: OutputPathType | None
    """the output b0 image. """
    dkt: OutputPathType | None
    """the output dkt image. """
    predicted_signal: OutputPathType | None
    """the predicted dwi image. """


def dwi2tensor(
    dwi: InputPathType,
    dt: InputPathType,
    ols: bool = False,
    mask: InputPathType | None = None,
    b0: InputPathType | None = None,
    dkt: InputPathType | None = None,
    iter_: int | None = None,
    predicted_signal: InputPathType | None = None,
    grad: InputPathType | None = None,
    fslgrad: Dwi2tensorFslgrad | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Dwi2tensorConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Dwi2tensorOutputs:
    """
    dwi2tensor by Ben Jeurissen (ben.jeurissen@uantwerpen.be).
    
    Diffusion (kurtosis) tensor estimation.
    
    By default, the diffusion tensor (and optionally its kurtosis) is fitted to
    the log-signal in two steps: firstly, using weighted least-squares (WLS)
    with weights based on the empirical signal intensities; secondly, by further
    iterated weighted least-squares (IWLS) with weights determined by the signal
    predictions from the previous iteration (by default, 2 iterations will be
    performed). This behaviour can be altered in two ways:
    
    * The -ols option will cause the first fitting step to be performed using
    ordinary least-squares (OLS); that is, all measurements contribute equally
    to the fit, instead of the default behaviour of weighting based on the
    empirical signal intensities.
    
    * The -iter option controls the number of iterations of the IWLS prodedure.
    If this is set to zero, then the output model parameters will be those
    resulting from the first fitting step only: either WLS by default, or OLS if
    the -ols option is used in conjunction with -iter 0.
    
    The tensor coefficients are stored in the output image as follows:
    volumes 0-5: D11, D22, D33, D12, D13, D23
    
    If diffusion kurtosis is estimated using the -dkt option, these are stored
    as follows:
    volumes 0-2: W1111, W2222, W3333
    volumes 3-8: W1112, W1113, W1222, W1333, W2223, W2333
    volumes 9-11: W1122, W1133, W2233
    volumes 12-14: W1123, W1223, W1233
    
    References:
    
    References based on fitting algorithm used:
    
    * OLS, WLS:
    Basser, P.J.; Mattiello, J.; LeBihan, D. Estimation of the effective
    self-diffusion tensor from the NMR spin echo. J Magn Reson B., 1994, 103,
    247–254.
    
    * IWLS:
    Veraart, J.; Sijbers, J.; Sunaert, S.; Leemans, A. & Jeurissen, B. Weighted
    linear least squares estimation of diffusion MRI parameters: strengths,
    limitations, and pitfalls. NeuroImage, 2013, 81, 335-346.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dwi2tensor.html
    
    Args:
        dwi: the input dwi image.
        dt: the output dt image.
        ols: perform initial fit using an ordinary least-squares (OLS) fit (see
            Description).
        mask: only perform computation within the specified binary brain mask
            image.
        b0: the output b0 image.
        dkt: the output dkt image.
        iter_: number of iterative reweightings for IWLS algorithm (default: 2)
            (see Description).
        predicted_signal: the predicted dwi image.
        grad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in a text file. This should be supplied as a 4xN text file
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe
            the direction of the applied gradient, and b gives the b-value in units
            of s/mm^2. If a diffusion gradient scheme is present in the input image
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient
            scheme is present in the input image header, the data provided with this
            option will be instead used.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Dwi2tensorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWI2TENSOR_METADATA)
    cargs = []
    cargs.append("dwi2tensor")
    if ols:
        cargs.append("-ols")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if b0 is not None:
        cargs.extend(["-b0", execution.input_file(b0)])
    if dkt is not None:
        cargs.extend(["-dkt", execution.input_file(dkt)])
    if iter_ is not None:
        cargs.extend(["-iter", str(iter_)])
    if predicted_signal is not None:
        cargs.extend(["-predicted_signal", execution.input_file(predicted_signal)])
    if grad is not None:
        cargs.extend(["-grad", execution.input_file(grad)])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(dwi))
    cargs.append(execution.input_file(dt))
    ret = Dwi2tensorOutputs(
        root=execution.output_file("."),
        dt=execution.output_file(f"{pathlib.Path(dt).stem}"),
        b0=execution.output_file(f"{pathlib.Path(b0).stem}") if b0 is not None else None,
        dkt=execution.output_file(f"{pathlib.Path(dkt).stem}") if dkt is not None else None,
        predicted_signal=execution.output_file(f"{pathlib.Path(predicted_signal).stem}") if predicted_signal is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DWI2TENSOR_METADATA",
    "Dwi2tensorConfig",
    "Dwi2tensorFslgrad",
    "Dwi2tensorOutputs",
    "dwi2tensor",
]